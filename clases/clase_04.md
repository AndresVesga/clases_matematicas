# Clase 4. Radicación: deshacer una potencia

## Para empezar

En la clase pasada respondimos preguntas como "¿cuánto es 8²?".

Hoy la pregunta va al revés: **un salón cuadrado tiene 64 m². ¿Cuánto mide cada pared?**

Nadie te da el lado: te dan el área y toca devolverse. Y hay una pregunta más incómoda que dejaremos para el final de la clase:

**¿Qué número multiplicado por sí mismo da −9?**

## Objetivos

Al terminar esta clase el estudiante será capaz de:

1. Calcular y simplificar raíces de números reales, reconociendo cuáles son exactas y cuáles irracionales.
2. Convertir entre raíces y potencias de exponente fraccionario, y aplicar la radicación para resolver problemas de áreas y volúmenes.

## Lo que vamos a entender

### La raíz es la operación contraria a la potencia

Si 8² = 64, entonces **√64 = 8**. Una operación deshace a la otra.

Las partes tienen nombre:

* **Radicando:** el número que está adentro (el 64).
* **Índice:** el numerito de arriba, que dice qué potencia se deshace.
* Si no se escribe índice, se entiende que es **2** (raíz cuadrada).

∛27 = 3, porque 3³ = 27.
⁴√16 = 2, porque 2⁴ = 16.

**Pregunta al curso:** ¿cuánto es ∛125? (5, porque 5 × 5 × 5 = 125. La pregunta siempre se responde pensando en la potencia.)

### Raíces exactas y raíces que no lo son

Algunas raíces caen justo en un entero: √49 = 7, √100 = 10, ∛8 = 2.
Otras no caen en ningún entero **ni en ninguna fracción**: √2, √5, √30. Esas son los **irracionales** de la clase 1.

Cuando la raíz no es exacta, hay dos formas correctas de responder, y sirven para cosas distintas:

* **Valor exacto:** √30 (así se deja en matemáticas, sin perder precisión).
* **Valor aproximado:** √30 ≈ 5,48 (así se usa para comprar materiales o medir).

Para acorralarla entre enteros basta con dos multiplicaciones: como 25 < 30 < 36, entonces **5 < √30 < 6**.

### El signo dentro de la raíz

Aquí hay una diferencia clave según el índice.

**Índice impar:** siempre se puede, incluso con negativos.
∛(−27) = −3, porque (−3)³ = −27.

**Índice par:** con radicando negativo **no hay respuesta entre los números reales**.
√(−9) no existe en ℝ, porque ningún número real multiplicado por sí mismo da negativo: si es positivo da positivo, y si es negativo, al elevarlo al cuadrado, también da positivo.

**Guarda bien esa idea.** No es que la pregunta esté mal hecha; es que la respuesta no cabe en los números que conocemos hasta hoy. La próxima clase se dedica exactamente a eso.

### Simplificar raíces

Una raíz se puede partir cuando hay una **multiplicación** adentro:

√(a × b) = √a × √b

Eso permite sacar del radical lo que sí es exacto:

√72 = √(36 × 2) = √36 × √2 = **6√2**

El truco es buscar el **cuadrado perfecto más grande** que quepa: 4, 9, 16, 25, 36, 49, 64, 100.

Lo mismo funciona con divisiones: √(50/2) = √25 = 5.

**Advertencia grande:** esto **no** funciona con sumas.
√(9 + 16) = √25 = 5, pero √9 + √16 = 3 + 4 = 7. **No son iguales.**

### Sumar y restar raíces

Solo se pueden juntar las raíces **iguales**, igual que 3 manzanas + 2 manzanas.

2√5 + 3√5 = **5√5**

Si no se ven iguales, primero se simplifican:
√18 + √8 = 3√2 + 2√2 = **5√2**

### La raíz escrita como potencia

Toda raíz se puede escribir con un exponente fraccionario. El **índice va abajo**:

√7 = 7^(1/2) ∛5 = 5^(1/3) ⁴√x = x^(1/4)

Y si el radicando ya tiene exponente, ese número va arriba:
∛(8²) = 8^(2/3) = (∛8)² = 2² = **4**

Esto es útil porque permite aplicar a las raíces **todas las propiedades de las potencias** que aprendiste en la clase anterior.

**Mini reto:** ¿cuánto vale 81^(1/4)? (3, porque es ⁴√81.)

### Racionalizar: quitar la raíz del denominador

Por costumbre matemática no se deja una raíz abajo en una fracción. Se arregla multiplicando arriba y abajo por esa misma raíz:

3/√5 = (3 × √5) / (√5 × √5) = **3√5 / 5**

Funciona porque √5 × √5 = 5, y porque multiplicar arriba y abajo por lo mismo no cambia el valor de la fracción.

### Errores frecuentes

* **√(9 + 16) = 3 + 4.** No. La raíz no se reparte sobre sumas.
* **√(−16) = −4.** No. (−4)² = 16, no −16. Con índice par y radicando negativo no hay respuesta real.
* **√8 = 4.** No: eso sería 8 ÷ 2. √8 ≈ 2,83, y simplificada es 2√2.
* **√2 + √3 = √5.** No. Solo se suman raíces iguales.
* **Confundir ∛(−8) con √(−8).** La primera vale −2; la segunda no existe en los reales.

## Ejemplos resueltos

### Ejemplo 1 (básico)

**Problema.** Calcula: a) √49 b) ∛(−27) c) ⁴√16 d) √0,25 e) √(−4)

**Solución.**

1. **√49**: buscamos el número que al cuadrado da 49. Es 7, porque 7 × 7 = 49. → **7**
2. **∛(−27)**: el índice es impar, así que sí admite negativos. (−3)³ = −27. → **−3**
3. **⁴√16**: buscamos el número que elevado a la cuarta da 16. 2⁴ = 16. → **2**
4. **√0,25**: 0,5 × 0,5 = 0,25. → **0,5** (también se puede pensar como √(1/4) = 1/2).
5. **√(−4)**: índice par con radicando negativo. → **no existe en los números reales**.

**Respuesta:** 7; −3; 2; 0,5; y la última no tiene respuesta real.

### Ejemplo 2 (intermedio)

**Problema.** Simplifica: √72 − √18 + √50

**Solución.**

1. Las tres raíces se ven distintas, así que no se pueden restar todavía. Primero hay que simplificar cada una buscando cuadrados perfectos adentro.
2. √72 = √(36 × 2) = 6√2.
3. √18 = √(9 × 2) = 3√2.
4. √50 = √(25 × 2) = 5√2.
5. Ahora las tres son "del mismo tipo" (√2), así que se pueden operar los números de adelante: 6 − 3 + 5 = 8.

**Respuesta:** **8√2** (aproximadamente 11,31)

### Ejemplo 3 (aplicado)

**Problema.** Una empresa fabrica cajas **cúbicas** para domicilios. Una de ellas tiene un volumen de 3.375 cm³. a) ¿Cuánto mide cada arista? b) ¿Cuánto cartón se necesita para forrar toda la superficie exterior?

**Solución.**

1. En un cubo, volumen = arista × arista × arista, es decir arista³. Como conocemos el volumen y buscamos la arista, hay que deshacer un cubo: usamos la raíz cúbica.
2. arista = ∛3.375. Probamos: 10³ = 1.000 (muy poco), 20³ = 8.000 (mucho), 15³ = 3.375. ✔
3. La arista mide **15 cm**.
4. Un cubo tiene 6 caras cuadradas iguales. El área de una cara es 15² = 225 cm².
5. Superficie total: 6 × 225 = 1.350 cm².

**Respuesta:** cada arista mide **15 cm** y se necesitan **1.350 cm² de cartón**. Si el volumen hubiera sido 3.000 cm³, la arista no habría dado exacta y habría tocado usar un valor aproximado.

## Actividad práctica

Resuelve en tu cuaderno.

**Comprensión**

1. Calcula: a) √64 b) √121 c) ∛8 d) ∛(−64) e) ⁴√81
2. Calcula: a) √0,49 b) √(9/25) c) √1 d) ∛1000 e) √0
3. ¿Cuáles de estas raíces **no** tienen resultado en los números reales? Justifica. a) √(−9) b) ∛(−8) c) √(−16) d) ⁴√(−1) e) ∛(−1)
4. ¿Entre qué dos enteros consecutivos está cada raíz? a) √20 b) √50 c) √90 d) ∛30
5. Escribe como potencia de exponente fraccionario: a) √7 b) ∛5 c) ⁴√x d) √(x³)

**Aplicación**

6. Simplifica: a) √8 b) √48 c) √75 d) √200
7. Opera y simplifica: a) √3 × √12 b) √50 ÷ √2 c) (√5)² d) √2 × √8
8. Suma o resta: a) 2√5 + 3√5 b) √18 + √8 c) √27 − √12 d) 5√2 − √2
9. Escribe como raíz y calcula: a) 16^(1/2) b) 27^(1/3) c) 81^(1/4) d) 8^(2/3)
10. Racionaliza el denominador: a) 1/√2 b) 3/√5 c) 6/√3

**Problemas en contexto**

11. El salón de clase es cuadrado y tiene 64 m² de área. a) ¿Cuánto mide cada pared? b) ¿Cuántos metros de guardaescoba se necesitan para todo el borde?
12. Una cancha cuadrada de microfútbol tiene 400 m². Se quiere encerrar con malla y el metro de malla instalada cuesta $18.000. ¿Cuánto costará?
13. Un tanque **cúbico** almacena 216 litros de agua. Sabiendo que 1 litro equivale a 1 dm³, ¿cuánto mide la arista del tanque en decímetros y en centímetros?

**Retos**

14. Un lote cuadrado tiene 150 m². a) ¿El lado es racional o irracional? b) ¿Entre qué enteros está? c) Escribe √150 simplificada. d) Usando la aproximación √150 ≈ 12,25 m, ¿cuántos metros de cerca hay que comprar?
15. Andrés afirma que √(9 + 16) = √9 + √16. Comprueba si tiene razón calculando los dos lados y explica con tus palabras qué regla está usando mal.

## Respuestas para el docente

1. a) 8 b) 11 c) 2 d) −4 e) 3
2. a) 0,7 b) 3/5 = 0,6 c) 1 d) 10 e) 0
3. No existen en ℝ: **a), c) y d)**, porque tienen índice par y radicando negativo. b) = −2 y e) = −1, porque el índice es impar.
4. a) entre 4 y 5 (16 < 20 < 25) b) entre 7 y 8 (49 < 50 < 64) c) entre 9 y 10 (81 < 90 < 100) d) entre 3 y 4 (27 < 30 < 64)
5. a) 7^(1/2) b) 5^(1/3) c) x^(1/4) d) x^(3/2)
6. a) 2√2 b) 4√3 c) 5√3 d) 10√2
7. a) √36 = 6 b) √25 = 5 c) 5 d) √16 = 4
8. a) 5√5 b) 3√2 + 2√2 = 5√2 c) 3√3 − 2√3 = √3 d) 4√2
9. a) √16 = 4 b) ∛27 = 3 c) ⁴√81 = 3 d) (∛8)² = 2² = 4
10. a) √2/2 b) 3√5/5 c) 6√3/3 = 2√3
11. a) √64 = **8 m**. b) Perímetro = 4 × 8 = **32 m**.
12. Lado = √400 = 20 m. Perímetro = 80 m. Costo = 80 × 18.000 = **$1.440.000**.
13. ∛216 = **6 dm**, es decir **60 cm**.
14. a) Irracional. b) Entre 12 y 13, porque 144 < 150 < 169. c) √150 = √(25 × 6) = **5√6**. d) Perímetro ≈ 4 × 12,25 = 49 m; conviene comprar **49 m** o un poco más.
15. √(9 + 16) = √25 = 5, mientras que √9 + √16 = 3 + 4 = 7. **No tiene razón.** Está aplicando a una **suma** una regla que solo vale para productos y cocientes.

## Cierre

Idea para recordar: la raíz deshace la potencia, se simplifica sacando cuadrados perfectos y **se reparte sobre productos, nunca sobre sumas**.

Quedó una pregunta sin responder: √(−9) no existe entre los números reales. Los matemáticos no se resignaron a eso e inventaron un número nuevo. En la próxima clase lo conocemos.
