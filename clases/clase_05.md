# Clase 5. El número que no existía: los números complejos

## Para empezar

La clase pasada quedamos con una pregunta sin respuesta:

**¿Cuánto vale √(−9)?**

Buscamos un número que multiplicado por sí mismo dé −9. Si es positivo, da positivo. Si es negativo, también da positivo. **Entre los reales no está.**

Durante siglos los matemáticos escribieron "no tiene solución" y pasaron a la siguiente. Hasta que a alguien se le ocurrió algo distinto: *si el número no existe, lo invento*.

Y funcionó tan bien que hoy sin él no habría electricidad domiciliaria, ni señal de celular, ni gráficos de videojuegos.

## Objetivos

Al terminar esta clase el estudiante será capaz de:

1. Expresar la raíz de un número negativo en términos de la unidad imaginaria i y calcular potencias de i.
2. Reconocer un número complejo en forma binómica a + bi, identificando su parte real, su parte imaginaria y su conjugado, y ubicarlo en el plano complejo.

## Lo que vamos a entender

### La unidad imaginaria

Se define un número nuevo, llamado **i** (de "imaginario"), con una única regla:

**i = √(−1)**, y por lo tanto **i² = −1**

Eso es todo. No hay que entenderlo como una cantidad que se pueda contar; hay que entenderlo como **una herramienta que resuelve algo que antes era imposible**. El nombre "imaginario" quedó por accidente histórico y es un poco injusto: son tan útiles como los demás.

Con esa sola regla ya se pueden calcular las raíces que faltaban:

√(−9) = √(9 × (−1)) = √9 × √(−1) = **3i**

Comprobación: (3i)² = 3² × i² = 9 × (−1) = −9 ✔

Si el radicando no es cuadrado perfecto, se simplifica igual que en la clase anterior:
√(−12) = √(4 × 3 × (−1)) = **2√3 i**

**Pregunta al curso:** ¿cuánto vale √(−25)? (5i. Se saca la raíz normal y se le pega la i.)

### Las potencias de i giran en círculo

Esto es lo más entretenido del tema. Calculemos en orden:

* i¹ = i
* i² = −1
* i³ = i² × i = (−1) × i = **−i**
* i⁴ = i² × i² = (−1) × (−1) = **1**
* i⁵ = i⁴ × i = 1 × i = **i** … y vuelve a empezar.

Los resultados se repiten en un ciclo de **cuatro**: i, −1, −i, 1.

**Truco para cualquier exponente:** divide el exponente entre 4 y quédate solo con el **residuo**.

| Residuo | Resultado |
|---|---|
| 0 | 1 |
| 1 | i |
| 2 | −1 |
| 3 | −i |

Ejemplo: i²² → 22 ÷ 4 = 5 y sobra **2** → i²² = **−1**.

**Mini reto:** ¿cuánto es i⁴⁰? (40 es múltiplo de 4, residuo 0, así que vale 1.)

### La forma binómica: a + bi

Un **número complejo** se escribe juntando una parte de cada mundo:

**z = a + bi**, donde a y b son números **reales**

* **a** es la **parte real**.
* **b** es la **parte imaginaria** (ojo: es b, sin la i).

Ejemplos:

| Número | Parte real | Parte imaginaria |
|---|---|---|
| 3 + 5i | 3 | 5 |
| −2 + i | −2 | 1 |
| 7 | 7 | 0 |
| −4i | 0 | −4 |

Fíjate en las dos últimas filas. **Todo número real es también complejo**, con parte imaginaria 0. Los reales no desaparecieron: ahora son un pedazo de un conjunto más grande, llamado ℂ.

Dos complejos son **iguales** solo si coinciden en las dos partes: si x + yi = 5 − 3i, entonces x = 5 y y = −3.

### El plano complejo

Un número real cabe en una recta. Un complejo necesita **dos datos**, así que necesita un plano:

* El **eje horizontal** guarda la parte real.
* El **eje vertical** guarda la parte imaginaria.

Así, 3 + 2i se dibuja como el punto que está 3 a la derecha y 2 arriba. Y −1 + 4i queda arriba a la izquierda.

Es la misma idea de las coordenadas de un mapa o de la posición de un personaje en un videojuego.

### El conjugado

El **conjugado** de un complejo es el mismo número con la parte imaginaria cambiada de signo. Se escribe con una barra encima o, aquí, como "conjugado de z".

* conjugado de 3 + 5i = **3 − 5i**
* conjugado de −2 − i = **−2 + i**
* conjugado de 6 = **6** (no tiene parte imaginaria que cambiar)

En el plano es una **reflexión respecto al eje horizontal**: el punto se voltea hacia el otro lado.

No lo inventaron por gusto: en la próxima clase será la llave para dividir complejos.

No lo confundas con el **opuesto**, que cambia los dos signos: el opuesto de 3 + 5i es −3 − 5i.

### Dónde aparecen de verdad

Recuerda las ecuaciones de segundo grado. Al resolver x² − 6x + 13 = 0 con la fórmula cuadrática aparece una raíz de un número negativo, y antes había que escribir "no tiene solución". Ahora sí la tiene: las soluciones son 3 + 2i y 3 − 2i.

Fíjate en un detalle que se repite siempre: **las soluciones complejas aparecen de a pares conjugados**.

### Errores frecuentes

* **√(−9) = −3.** No. (−3)² = 9, no −9. La respuesta es 3i.
* **i² = 1.** No: i² = −1. Es *la* definición del tema, y confundirla daña todo lo demás.
* **La parte imaginaria de 3 + 5i es 5i.** No: es **5**. La i no se incluye.
* **7 no es complejo.** Sí lo es: 7 = 7 + 0i.
* **i⁵⁰ = i × 50.** No. Se divide el exponente entre 4 y se usa el residuo.

## Ejemplos resueltos

### Ejemplo 1 (básico)

**Problema.** Escribe en términos de i: a) √(−25) b) √(−1) c) √(−8)

**Solución.**

1. **√(−25)**: separamos el signo del número. √(−25) = √25 × √(−1).
2. √25 = 5 y √(−1) = i, entonces queda **5i**.
3. **√(−1)** es directamente la definición: **i**.
4. **√(−8)**: primero se separa el negativo: √8 × √(−1).
5. Ahora se simplifica √8 como en la clase pasada: √8 = √(4 × 2) = 2√2.
6. Uniendo todo: **2√2 i**.

**Respuesta:** 5i; i; 2√2 i

### Ejemplo 2 (intermedio)

**Problema.** Calcula i⁷, i²² y i⁴⁵.

**Solución.**

1. Las potencias de i se repiten cada 4, así que en vez de multiplicar muchas veces, dividimos el exponente entre 4 y miramos el residuo.
2. **i⁷**: 7 ÷ 4 = 1 y sobra 3. Residuo 3 → **−i**.
3. **i²²**: 22 ÷ 4 = 5 y sobra 2. Residuo 2 → **−1**.
4. **i⁴⁵**: 45 ÷ 4 = 11 y sobra 1. Residuo 1 → **i**.
5. Comprobación rápida de la primera: i⁷ = i⁴ × i³ = 1 × (−i) = −i ✔

**Respuesta:** i⁷ = −i; i²² = −1; i⁴⁵ = i

### Ejemplo 3 (aplicado)

**Problema.** Un ingeniero modela un circuito y necesita resolver la ecuación x² − 6x + 13 = 0. Con los números reales diría que "no tiene solución". Encuéntrala usando números complejos e identifica la parte real y la imaginaria de cada respuesta.

**Solución.**

1. Usamos la fórmula cuadrática con a = 1, b = −6, c = 13.
2. Calculamos primero lo que va dentro de la raíz: b² − 4ac = (−6)² − 4 × 1 × 13 = 36 − 52 = **−16**.
3. Ese número negativo es el que antes cerraba el problema. Ahora se puede: √(−16) = 4i.
4. La fórmula queda x = (6 ± 4i) / 2.
5. Se divide cada parte entre 2: x = 3 ± 2i.
6. Entonces las soluciones son **3 + 2i** y **3 − 2i**. Observa que son conjugadas.
7. En ambas, la parte real es 3; las partes imaginarias son 2 y −2.

**Respuesta:** las soluciones son **3 + 2i** y **3 − 2i**, con parte real 3 y partes imaginarias 2 y −2. La ecuación sí tenía respuesta: lo que faltaba era un conjunto numérico más grande.

## Actividad práctica

Resuelve en tu cuaderno.

**Comprensión**

1. Escribe en términos de i: a) √(−4) b) √(−36) c) √(−100) d) √(−1) e) √(−81)
2. Calcula: a) i² b) i³ c) i⁴ d) i⁵
3. Identifica la parte real y la parte imaginaria: a) 3 + 5i b) −2 + i c) 7 d) −4i e) 0,5 − 2,5i
4. Escribe **verdadero** o **falso** y corrige lo falso: a) Todo número real es también complejo. b) i² = 1. c) 5 no es un número complejo. d) √(−9) = −3. e) El conjugado de 2 + 3i es 2 − 3i.
5. Escribe el **conjugado** y el **opuesto** de: a) 4 + 7i b) −3 + 2i c) 6i d) −5

**Aplicación**

6. Escribe en términos de i, simplificando la raíz: a) √(−8) b) √(−18) c) √(−50) d) √(−12)
7. Calcula usando el truco del residuo: a) i⁷ b) i¹² c) i²² d) i⁴⁵ e) i¹⁰⁰
8. Dibuja un plano complejo y ubica: 3 + 2i; −1 + 4i; −2 − 3i; 4; −3i.
9. Encuentra los valores reales de x y de y: a) x + yi = 5 − 3i b) 2x + 4i = 8 + yi
10. Resuelve y escribe las dos soluciones: a) x² = −9 b) x² = −49 c) x² + 4 = 0 d) x² + 20 = 0

**Problemas en contexto**

11. Un estudiante escribió en el tablero: √(−16) = −4. Explica por qué está mal, comprobando su respuesta, y escribe el resultado correcto.
12. Un videojuego guarda la posición de los objetos como números complejos: el personaje está en 2 + 3i, el cofre en −4 + i y la trampa en −5i. a) Ubica los tres en el plano complejo. b) ¿Cuál está sobre un eje? c) Escribe el conjugado de la posición del personaje y explica qué le pasó al punto en el dibujo.
13. En electricidad, la oposición que un circuito ofrece a la corriente se escribe como un complejo Z = 5 + 12i ohmios: la parte real es la resistencia y la parte imaginaria es la reactancia. a) ¿Cuánto vale cada una? b) Escribe el conjugado de Z. c) Si otro circuito tiene Z = 8 ohmios, ¿cuánta reactancia tiene?

**Retos**

14. Calcula i²⁰²⁶ explicando el procedimiento en dos renglones.
15. Un estudiante afirma: "√(−4) × √(−9) = √36 = 6". Calcula el producto correctamente pasando primero cada raíz a la forma con i, y explica qué regla de la clase anterior dejó de funcionar.

## Respuestas para el docente

1. a) 2i b) 6i c) 10i d) i e) 9i
2. a) −1 b) −i c) 1 d) i
3. a) real 3, imaginaria 5 b) real −2, imaginaria 1 c) real 7, imaginaria 0 d) real 0, imaginaria −4 e) real 0,5, imaginaria −2,5
4. a) V. b) F: i² = −1. c) F: 5 = 5 + 0i. d) F: es 3i. e) V.
5. a) conjugado 4 − 7i, opuesto −4 − 7i. b) conjugado −3 − 2i, opuesto 3 − 2i. c) conjugado −6i, opuesto −6i (aquí coinciden, porque no tiene parte real). d) conjugado −5, opuesto 5.
6. a) 2√2 i b) 3√2 i c) 5√2 i d) 2√3 i
7. a) −i b) 1 c) −1 d) i e) 1
8. 3 + 2i: arriba a la derecha. −1 + 4i: arriba a la izquierda. −2 − 3i: abajo a la izquierda. 4: sobre el eje real (horizontal). −3i: sobre el eje imaginario (vertical), hacia abajo.
9. a) x = 5, y = −3. b) 2x = 8 → x = 4; y = 4.
10. a) x = 3i o x = −3i b) x = 7i o x = −7i c) x² = −4 → x = ±2i d) x² = −20 → x = ±2√5 i
11. Está mal porque (−4)² = 16, no −16; al comprobar, su respuesta no cumple. Lo correcto es √(−16) = 4i, y en efecto (4i)² = 16i² = −16.
12. a) 2 + 3i arriba a la derecha; −4 + i arriba a la izquierda; −5i sobre el eje vertical, abajo. b) La trampa, −5i, está sobre el eje imaginario. c) El conjugado es 2 − 3i: el punto se reflejó al otro lado del eje horizontal.
13. a) Resistencia 5 ohmios, reactancia 12 ohmios. b) 5 − 12i. c) Reactancia 0, porque 8 = 8 + 0i.
14. 2026 ÷ 4 = 506 y sobra 2. Residuo 2 → i²⁰²⁶ = **−1**.
15. √(−4) = 2i y √(−9) = 3i, entonces el producto es 2i × 3i = 6i² = 6 × (−1) = **−6**, no 6. La regla √a × √b = √(a×b) **solo vale cuando los radicandos no son negativos**.

## Cierre

Idea para recordar: **i² = −1**. De esa sola regla salen todas las raíces de negativos, el ciclo de cuatro de las potencias de i y la forma a + bi.

Ya sabemos escribir y ubicar números complejos. Falta lo más importante: **operarlos**. Eso es exactamente la última clase de la unidad.
