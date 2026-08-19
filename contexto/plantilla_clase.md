# Plantilla de clase

Plantilla reutilizable para cualquier área o tema. Copia este archivo a `/clases/clase_XX.md` y reemplaza el contenido entre corchetes. Las reglas completas están en `criterios_pedagogicos.md`.

## Cómo pedir clases nuevas

Basta con una instrucción como:

> "Crea cuatro clases sobre ecuaciones lineales."

Quien genere el material debe: leer `criterios_pedagogicos.md`, leer `docente.md`, diseñar primero la progresión (qué enseña cada clase y por qué en ese orden), y luego escribir cada clase siguiendo esta plantilla. Al final, regenerar los Word con `scripts/md_a_word.py`.

## Reglas fijas que la plantilla asume

* Exactamente 2 objetivos, 3 ejemplos resueltos y 15 problemas por clase.
* Sin minutaje interno. Sin líneas divisorias (`---`).
* Contexto colombiano y pesos colombianos cuando sea natural.
* Cada concepto: idea intuitiva → explicación → ejemplo → aplicación.
* Toda respuesta se verifica antes de entregar.

## Estructura a rellenar

```markdown
# Clase XX. [Título claro y atractivo]

## Para empezar

[Situación, pregunta o reto de entrada. Dos a cinco líneas. Comprensible en 30 segundos.
No revela la explicación: abre la curiosidad. Idealmente con contexto cotidiano.]

## Objetivos

Al terminar esta clase el estudiante será capaz de:

1. [Verbo observable + contenido concreto.]
2. [Verbo observable + contenido concreto.]

## Lo que vamos a entender

### [Subtema 1]

[Idea intuitiva en lenguaje cotidiano.]

[Explicación breve. Definir cada símbolo antes de usarlo.]

[Ejemplo corto incrustado.]

**Pregunta al curso:** [intervención breve para el docente.]

### [Subtema 2]

[Igual que arriba.]

### Errores frecuentes

* [Error típico] → [por qué está mal y cómo se corrige.]
* [Error típico] → [corrección.]

## Ejemplos resueltos

### Ejemplo 1 (básico)

**Problema.** [Enunciado.]

**Solución.**

1. [Paso + por qué se hace.]
2. [Paso + por qué se hace.]

**Respuesta:** [resultado final.]

### Ejemplo 2 (intermedio)

[Misma estructura.]

### Ejemplo 3 (aplicado)

[Misma estructura, con situación cotidiana y respuesta interpretada en contexto,
no solo el número.]

## Actividad práctica

Resuelve en tu cuaderno.

**Comprensión**

1. [ ]
2. [ ]
3. [ ]
4. [ ]
5. [ ]

**Aplicación**

6. [ ]
7. [ ]
8. [ ]
9. [ ]
10. [ ]

**Problemas en contexto**

11. [ ]
12. [ ]
13. [ ]

**Retos**

14. [ ]
15. [ ]

## Respuestas para el docente

Sección de uso exclusivo del profesor.

1. [respuesta]
2. [respuesta]
...
15. [respuesta]

[Desarrollar el procedimiento solo cuando sea especialmente instructivo.]

## Cierre

[Dos o tres líneas: la idea principal que el estudiante debe recordar
y una frase que anticipe la clase siguiente.]
```

## Checklist antes de dar por terminada la clase

* 2 objetivos, 3 ejemplos, 15 ejercicios (contar).
* Los ejercicios solo usan lo enseñado hasta ese punto.
* Al menos tres problemas con contexto cotidiano real.
* Todas las respuestas verificadas.
* Sin minutaje, sin `---`, sin bloques largos de texto.
* La clase siguiente continúa de forma lógica.
