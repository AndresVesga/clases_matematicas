# -*- coding: utf-8 -*-
"""
Traduce notacion matematica escrita entre signos de pesos a ecuaciones
nativas de Word (OMML), las mismas que produce el editor de ecuaciones.

Esto es lo que hace que en el documento final una fraccion se vea como
una fraccion de verdad (una raya con el numerador arriba) y no como "2/3".

No es un interprete completo de LaTeX: solo entiende lo que las clases
usan. La lista esta en la constante COMANDOS y en el README.

Ejemplos de entrada -> lo que se ve en Word:

    \\frac{2}{3}        una fraccion con raya horizontal
    \\sqrt{2}           una raiz cuadrada con su cajon
    \\sqrt[3]{27}       una raiz cubica
    x^{2}              x con un 2 elevado
    a_{1}              a con un 1 como subindice
    3 \\times 4         3 x 4 con el signo de multiplicar correcto

Uso desde otro modulo:

    from latex_a_omml import omml_de

    xml = omml_de(r"\\frac{2}{3}")   # devuelve el <m:oMath> listo para Word
"""

from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

# Simbolos que se escriben con un comando y salen como un caracter suelto.
COMANDOS = {
    "times": "×", "cdot": "·", "div": "÷", "pm": "±", "mp": "∓",
    "approx": "≈", "neq": "≠", "ne": "≠", "leq": "≤", "le": "≤",
    "geq": "≥", "ge": "≥", "equiv": "≡", "sim": "∼",
    "to": "→", "rightarrow": "→", "Rightarrow": "⇒", "iff": "⇔",
    "infty": "∞", "ldots": "…", "cdots": "⋯", "dots": "…",
    "pi": "π", "alpha": "α", "beta": "β", "theta": "θ", "lambda": "λ",
    "omega": "ω", "Delta": "Δ", "degree": "°", "circ": "°",
    "in": "∈", "notin": "∉", "subset": "⊂", "subseteq": "⊆",
    "cup": "∪", "cap": "∩", "emptyset": "∅", "forall": "∀", "exists": "∃",
    "%": "%", "$": "$", "{": "{", "}": "}", "_": "_", "^": "^", "&": "&",
}

# Conjuntos numericos: \mathbb{R} -> R de doble barra.
CONJUNTOS = {
    "N": "ℕ", "Z": "ℤ", "Q": "ℚ", "R": "ℝ", "C": "ℂ", "P": "ℙ",
}

ESPACIOS = {",": " ", ";": " ", ":": " ", " ": " ", "quad": "  ", "!": ""}

ESPECIALES = set("\\{}^_")


def escapar(texto):
    return (texto.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def run(texto, recto=False):
    """Un trozo de texto dentro de la ecuacion.

    recto=True lo deja en vertical (para palabras); si no, Word pone las
    letras en cursiva, que es la convencion matematica para las variables.
    """
    if not texto:
        return ""
    props = "<m:rPr><m:nor/></m:rPr>" if recto else ""
    return '<m:r>%s<m:t xml:space="preserve">%s</m:t></m:r>' % (props, escapar(texto))


def envolver(nodos):
    """Une varios nodos; si hay varios, quedan uno detras de otro."""
    return "".join(nodos)


class Lector(object):
    def __init__(self, texto):
        self.t = texto
        self.i = 0

    def fin(self):
        return self.i >= len(self.t)

    def ver(self):
        return self.t[self.i] if not self.fin() else ""

    def siguiente(self):
        c = self.t[self.i]
        self.i += 1
        return c

    def comando(self):
        """Lee el nombre que va despues de la barra invertida."""
        nombre = ""
        while not self.fin() and self.t[self.i].isalpha():
            nombre += self.siguiente()
        if not nombre and not self.fin():
            nombre = self.siguiente()
        return nombre


def leer_grupo(lector):
    """Lee {...} y devuelve su contenido ya traducido."""
    if lector.ver() == "{":
        lector.siguiente()
        nodos = leer_secuencia(lector, parar="}")
        if lector.ver() == "}":
            lector.siguiente()
        return envolver(nodos)
    return leer_atomo(lector)


def leer_opcional(lector):
    """Lee [...] si esta presente. Se usa para el indice de la raiz."""
    if lector.ver() == "[":
        lector.siguiente()
        nodos = leer_secuencia(lector, parar="]")
        if lector.ver() == "]":
            lector.siguiente()
        return envolver(nodos)
    return None


def leer_atomo(lector):
    if lector.fin():
        return ""
    c = lector.ver()

    if c == "{":
        return leer_grupo(lector)

    if c == "\\":
        lector.siguiente()
        nombre = lector.comando()

        if nombre == "frac" or nombre == "dfrac" or nombre == "tfrac":
            num = leer_grupo(lector)
            den = leer_grupo(lector)
            return ("<m:f><m:fPr><m:ctrlPr/></m:fPr>"
                    "<m:num>%s</m:num><m:den>%s</m:den></m:f>" % (num, den))

        if nombre == "sqrt":
            indice = leer_opcional(lector)
            radicando = leer_grupo(lector)
            if indice is None:
                return ("<m:rad><m:radPr><m:degHide m:val=\"1\"/></m:radPr>"
                        "<m:deg/><m:e>%s</m:e></m:rad>" % radicando)
            return ("<m:rad><m:radPr><m:degHide m:val=\"0\"/></m:radPr>"
                    "<m:deg>%s</m:deg><m:e>%s</m:e></m:rad>" % (indice, radicando))

        if nombre == "text" or nombre == "mathrm" or nombre == "operatorname":
            crudo = leer_grupo_crudo(lector)
            return run(crudo, recto=True)

        if nombre == "mathbb":
            crudo = leer_grupo_crudo(lector)
            return run(CONJUNTOS.get(crudo.strip(), crudo), recto=True)

        if nombre == "overline" or nombre == "bar":
            base = leer_grupo(lector)
            return ("<m:bar><m:barPr><m:pos m:val=\"top\"/></m:barPr>"
                    "<m:e>%s</m:e></m:bar>" % base)

        if nombre == "left":
            # \left( ... \right) produce parentesis que crecen con lo que
            # encierran, que es lo que hace que una fraccion dentro de un
            # parentesis se vea bien y no con parentesis enanos al lado.
            abre = leer_delimitador(lector)
            dentro = envolver(leer_secuencia(lector, parar_right=True))
            cierra = ")"
            if lector.t.startswith("\\right", lector.i):
                lector.i += len("\\right")
                cierra = leer_delimitador(lector)
            return ("<m:d><m:dPr><m:begChr m:val=\"%s\"/><m:endChr m:val=\"%s\"/>"
                    "<m:ctrlPr/></m:dPr><m:e>%s</m:e></m:d>"
                    % (abre, cierra, dentro))

        if nombre in ("right", "big", "Big"):
            return run(leer_delimitador(lector))

        if nombre in ESPACIOS:
            return run(ESPACIOS[nombre], recto=True)

        if nombre in COMANDOS:
            return run(COMANDOS[nombre], recto=True)

        # Comando desconocido: se escribe como palabra vertical.
        return run(nombre, recto=True)

    # Numeros y signos de puntuacion se agrupan para que Word no los separe.
    if c.isdigit():
        texto = ""
        while not lector.fin() and (lector.ver().isdigit() or lector.ver() in ".,"):
            # Una coma solo se pega si despues viene otro digito (2,5).
            if lector.ver() in ".," :
                if lector.i + 1 < len(lector.t) and lector.t[lector.i + 1].isdigit():
                    texto += lector.siguiente()
                    continue
                break
            texto += lector.siguiente()
        return run(texto)

    if c.isalpha():
        return run(lector.siguiente())

    lector.siguiente()
    return run(c, recto=(c not in "+-=<>()[]/|"))


def leer_grupo_crudo(lector):
    """Lee {...} devolviendo el texto sin traducir (para \\text)."""
    if lector.ver() != "{":
        return lector.siguiente() if not lector.fin() else ""
    lector.siguiente()
    profundidad = 1
    texto = ""
    while not lector.fin():
        c = lector.siguiente()
        if c == "{":
            profundidad += 1
        elif c == "}":
            profundidad -= 1
            if profundidad == 0:
                break
        texto += c
    return texto


def leer_delimitador(lector):
    """Lee el simbolo que acompaña a \\left o \\right. El punto significa
    'sin delimitador visible'."""
    if lector.fin():
        return ""
    d = lector.siguiente()
    if d == "\\":
        nombre = lector.comando()
        d = {"{": "{", "}": "}", "langle": "⟨", "rangle": "⟩",
             "lvert": "|", "rvert": "|"}.get(nombre, nombre)
    return "" if d == "." else escapar(d)


def leer_secuencia(lector, parar=None, parar_right=False):
    nodos = []
    while not lector.fin():
        if parar and lector.ver() == parar:
            break
        if parar_right and lector.t.startswith("\\right", lector.i):
            break
        nodo = leer_atomo(lector)

        # Superindices y subindices se aplican al atomo que acaba de salir.
        while lector.ver() in ("^", "_"):
            marca = lector.siguiente()
            script = leer_grupo(lector)
            if marca == "^":
                nodo = ("<m:sSup><m:e>%s</m:e><m:sup>%s</m:sup></m:sSup>"
                        % (nodo, script))
            else:
                nodo = ("<m:sSub><m:e>%s</m:e><m:sub>%s</m:sub></m:sSub>"
                        % (nodo, script))
        nodos.append(nodo)
    return nodos


def cuerpo_omml(latex):
    """Traduce la formula y devuelve solo el contenido, sin la envoltura."""
    return envolver(leer_secuencia(Lector(latex)))


def omml_de(latex):
    """Devuelve el elemento <m:oMath> listo para insertar en un parrafo."""
    xml = "<m:oMath %s>%s</m:oMath>" % (nsdecls("m"), cuerpo_omml(latex))
    return parse_xml(xml)


if __name__ == "__main__":
    pruebas = [
        r"\frac{2}{3}", r"\sqrt{2}", r"\sqrt[3]{-27}", r"x^{2}", r"i^{2} = -1",
        r"3 \times 4", r"\mathbb{R}", r"\frac{-1+5i}{1+i} = 2+3i",
        r"1,5 \times 10^{8}", r"\text{area} = l^{2}",
    ]
    for p in pruebas:
        print(p, "->", cuerpo_omml(p)[:80], "...")
