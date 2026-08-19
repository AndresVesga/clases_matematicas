# Clase 4. Radicación: deshacer una potencia

## Para empezar

En la clase pasada respondimos preguntas como "¿cuánto es \(8^{2}\)?".

Hoy la pregunta va al revés: **un salón cuadrado tiene 64 m². ¿Cuánto mide cada pared?**

Nadie te da el lado: te dan el área y toca devolverse. Y hay una pregunta más incómoda que dejaremos para el final de la clase:

**¿Qué número multiplicado por sí mismo da \(-9\)?**

## Objetivos

Al terminar esta clase el estudiante será capaz de:

1. Calcular y simplificar raíces de números reales, reconociendo cuáles son exactas y cuáles irracionales.
2. Convertir entre raíces y potencias de exponente fraccionario, y aplicar la radicación para resolver problemas de áreas y volúmenes.

## Lo que vamos a entender

### La raíz es la operación contraria a la potencia

Si \(8^{2}=64\), entonces \(\sqrt{64}=8\). Una operación deshace a la otra.

Las partes tienen nombre:

* **Radicando:** el número que está adentro (el 64).
* **Índice:** el numerito de arriba, que dice qué potencia se deshace.
* Si no se escribe índice, se entiende que es **2** (raíz cuadrada).

\(\sqrt[3]{27}=3\), porque \(3^{3}=27\).
\(\sqrt[4]{16}=2\), porque \(2^{4}=16\).

**Pregunta al curso:** ¿cuánto es \(\sqrt[3]{125}\)? (5, porque \(5\times 5\times 5=125\). La pregunta siempre se responde pensando en la potencia.)

### Raíces exactas y raíces que no lo son

Algunas raíces caen justo en un entero: \(\sqrt{49}=7\), \(\sqrt{100}=10\), \(\sqrt[3]{8}=2\).
Otras no caen en ningún entero **ni en ninguna fracción**: \(\sqrt{2}\), \(\sqrt{5}\), \(\sqrt{30}\). Esas son los **irracionales** de la clase 1.

Cuando la raíz no es exacta, hay dos formas correctas de responder, y sirven para cosas distintas:

* **Valor exacto:** \(\sqrt{30}\) (así se deja en matemáticas, sin perder precisión).
* **Valor aproximado:** \(\sqrt{30}\approx 5,48\) (así se usa para comprar materiales o medir).

Para acorralarla entre enteros basta con dos multiplicaciones: como \(25<30<36\), entonces \(5<\sqrt{30}<6\).

### El signo dentro de la raíz

Aquí hay una diferencia clave según el índice.

**Índice impar:** siempre se puede, incluso con negativos.
\(\sqrt[3]{-27}=-3\), porque \((-3)^{3}=-27\).

**Índice par:** con radicando negativo **no hay respuesta entre los números reales**.
\(\sqrt{-9}\) no existe en \(\mathbb{R}\), porque ningún número real multiplicado por sí mismo da negativo: si es positivo da positivo, y si es negativo, al elevarlo al cuadrado, también da positivo.

**Guarda bien esa idea.** No es que la pregunta esté mal hecha; es que la respuesta no cabe en los números que conocemos hasta hoy. La próxima clase se dedica exactamente a eso.

### Simplificar raíces

Una raíz se puede partir cuando hay una **multiplicación** adentro:

\(\sqrt{a\times b}=\sqrt{a}\times\sqrt{b}\)

Eso permite sacar del radical lo que sí es exacto:

\(\sqrt{72}=\sqrt{36\times 2}=\sqrt{36}\times\sqrt{2}=6\sqrt{2}\)

El truco es buscar el **cuadrado perfecto más grande** que quepa: 4, 9, 16, 25, 36, 49, 64, 100.

Lo mismo funciona con divisiones: \(\sqrt{\frac{50}{2}}=\sqrt{25}=5\).

**Advertencia grande:** esto **no** funciona con sumas.
\(\sqrt{9+16}=\sqrt{25}=5\), pero \(\sqrt{9}+\sqrt{16}=3+4=7\). **No son iguales.**

### Sumar y restar raíces

Solo se pueden juntar las raíces **iguales**, igual que 3 manzanas + 2 manzanas.

\(2\sqrt{5}+3\sqrt{5}=5\sqrt{5}\)

Si no se ven iguales, primero se simplifican:
\(\sqrt{18}+\sqrt{8}=3\sqrt{2}+2\sqrt{2}=5\sqrt{2}\)

### La raíz escrita como potencia

Toda raíz se puede escribir con un exponente fraccionario. El **índice va abajo**:

\(\sqrt{7}=7^{1/2}\), \(\sqrt[3]{5}=5^{1/3}\), \(\sqrt[4]{x}=x^{1/4}\)

Y si el radicando ya tiene exponente, ese número va arriba:
\(\sqrt[3]{8^{2}}=8^{2/3}=\left(\sqrt[3]{8}\right)^{2}=2^{2}=4\)

Esto es útil porque permite aplicar a las raíces **todas las propiedades de las potencias** que aprendiste en la clase anterior.

**Mini reto:** ¿cuánto vale \(81^{1/4}\)? (3, porque es \(\sqrt[4]{81}\).)

### Racionalizar: quitar la raíz del denominador

Por costumbre matemática no se deja una raíz abajo en una fracción. Se arregla multiplicando arriba y abajo por esa misma raíz:

\(\frac{3}{\sqrt{5}}=\frac{3\times\sqrt{5}}{\sqrt{5}\times\sqrt{5}}=\frac{3\sqrt{5}}{5}\)

Funciona porque \(\sqrt{5}\times\sqrt{5}=5\), y porque multiplicar arriba y abajo por lo mismo no cambia el valor de la fracción.

### Errores frecuentes

* **\(\sqrt{9+16}=3+4\).** No. La raíz no se reparte sobre sumas.
* **\(\sqrt{-16}=-4\).** No. \((-4)^{2}=16\), no \(-16\). Con índice par y radicando negativo no hay respuesta real.
* **\(\sqrt{8}=4\).** No: eso sería \(8\div 2\). \(\sqrt{8}\approx 2,83\), y simplificada es \(2\sqrt{2}\).
* **\(\sqrt{2}+\sqrt{3}=\sqrt{5}\).** No. Solo se suman raíces iguales.
* **Confundir \(\sqrt[3]{-8}\) con \(\sqrt{-8}\).** La primera vale \(-2\); la segunda no existe en los reales.

## Ejemplos resueltos

### Ejemplo 1 (básico)

**Problema.** Calcula: a) \(\sqrt{49}\) b) \(\sqrt[3]{-27}\) c) \(\sqrt[4]{16}\) d) \(\sqrt{0,25}\) e) \(\sqrt{-4}\)

**Solución.**

1. **\(\sqrt{49}\)**: buscamos el número que al cuadrado da 49. Es 7, porque \(7\times 7=49\). → \(7\)
2. **\(\sqrt[3]{-27}\)**: el índice es impar, así que sí admite negativos. \((-3)^{3}=-27\). → \(-3\)
3. **\(\sqrt[4]{16}\)**: buscamos el número que elevado a la cuarta da 16. \(2^{4}=16\). → \(2\)
4. **\(\sqrt{0,25}\)**: \(0,5\times 0,5=0,25\). → \(0,5\) (también se puede pensar como \(\sqrt{\frac{1}{4}}=\frac{1}{2}\)).
5. **\(\sqrt{-4}\)**: índice par con radicando negativo. → **no existe en los números reales**.

**Respuesta:** \(7\); \(-3\); \(2\); \(0,5\); y la última no tiene respuesta real.

### Ejemplo 2 (intermedio)

**Problema.** Simplifica: \(\sqrt{72}-\sqrt{18}+\sqrt{50}\)

**Solución.**

1. Las tres raíces se ven distintas, así que no se pueden restar todavía. Primero hay que simplificar cada una buscando cuadrados perfectos adentro.
2. \(\sqrt{72}=\sqrt{36\times 2}=6\sqrt{2}\).
3. \(\sqrt{18}=\sqrt{9\times 2}=3\sqrt{2}\).
4. \(\sqrt{50}=\sqrt{25\times 2}=5\sqrt{2}\).
5. Ahora las tres son "del mismo tipo" \(\left(\sqrt{2}\right)\), así que se pueden operar los números de adelante: \(6-3+5=8\).

**Respuesta:** \(8\sqrt{2}\) (aproximadamente \(11,31\))

### Ejemplo 3 (aplicado)

**Problema.** Una empresa fabrica cajas **cúbicas** para domicilios. Una de ellas tiene un volumen de 3.375 cm³. a) ¿Cuánto mide cada arista? b) ¿Cuánto cartón se necesita para forrar toda la superficie exterior?

**Solución.**

1. En un cubo, volumen = arista × arista × arista, es decir \(\text{arista}^{3}\). Como conocemos el volumen y buscamos la arista, hay que deshacer un cubo: usamos la raíz cúbica.
2. \(\text{arista}=\sqrt[3]{3.375}\). Probamos: \(10^{3}=1.000\) (muy poco), \(20^{3}=8.000\) (mucho), \(15^{3}=3.375\). ✔
3. La arista mide **15 cm**.
4. Un cubo tiene 6 caras cuadradas iguales. El área de una cara es \(15^{2}=225\) cm².
5. Superficie total: \(6\times 225=1.350\) cm².

**Respuesta:** cada arista mide **15 cm** y se necesitan **1.350 cm² de cartón**. Si el volumen hubiera sido 3.000 cm³, la arista no habría dado exacta y habría tocado usar un valor aproximado.

## Actividad práctica

Resuelve en tu cuaderno.

**Comprensión**

1. Calcula: a) \(\sqrt{64}\) b) \(\sqrt{121}\) c) \(\sqrt[3]{8}\) d) \(\sqrt[3]{-64}\) e) \(\sqrt[4]{81}\)
2. Calcula: a) \(\sqrt{0,49}\) b) \(\sqrt{\frac{9}{25}}\) c) \(\sqrt{1}\) d) \(\sqrt[3]{1000}\) e) \(\sqrt{0}\)
3. ¿Cuáles de estas raíces **no** tienen resultado en los números reales? Justifica. a) \(\sqrt{-9}\) b) \(\sqrt[3]{-8}\) c) \(\sqrt{-16}\) d) \(\sqrt[4]{-1}\) e) \(\sqrt[3]{-1}\)
4. ¿Entre qué dos enteros consecutivos está cada raíz? a) \(\sqrt{20}\) b) \(\sqrt{50}\) c) \(\sqrt{90}\) d) \(\sqrt[3]{30}\)
5. Escribe como potencia de exponente fraccionario: a) \(\sqrt{7}\) b) \(\sqrt[3]{5}\) c) \(\sqrt[4]{x}\) d) \(\sqrt{x^{3}}\)

**Aplicación**

6. Simplifica: a) \(\sqrt{8}\) b) \(\sqrt{48}\) c) \(\sqrt{75}\) d) \(\sqrt{200}\)
7. Opera y simplifica: a) \(\sqrt{3}\times\sqrt{12}\) b) \(\sqrt{50}\div\sqrt{2}\) c) \(\left(\sqrt{5}\right)^{2}\) d) \(\sqrt{2}\times\sqrt{8}\)
8. Suma o resta: a) \(2\sqrt{5}+3\sqrt{5}\) b) \(\sqrt{18}+\sqrt{8}\) c) \(\sqrt{27}-\sqrt{12}\) d) \(5\sqrt{2}-\sqrt{2}\)
9. Escribe como raíz y calcula: a) \(16^{1/2}\) b) \(27^{1/3}\) c) \(81^{1/4}\) d) \(8^{2/3}\)
10. Racionaliza el denominador: a) \(\frac{1}{\sqrt{2}}\) b) \(\frac{3}{\sqrt{5}}\) c) \(\frac{6}{\sqrt{3}}\)

**Problemas en contexto**

11. El salón de clase es cuadrado y tiene 64 m² de área. a) ¿Cuánto mide cada pared? b) ¿Cuántos metros de guardaescoba se necesitan para todo el borde?
12. Una cancha cuadrada de microfútbol tiene 400 m². Se quiere encerrar con malla y el metro de malla instalada cuesta $18.000. ¿Cuánto costará?
13. Un tanque **cúbico** almacena 216 litros de agua. Sabiendo que 1 litro equivale a 1 dm³, ¿cuánto mide la arista del tanque en decímetros y en centímetros?

**Retos**

14. Un lote cuadrado tiene 150 m². a) ¿El lado es racional o irracional? b) ¿Entre qué enteros está? c) Escribe \(\sqrt{150}\) simplificada. d) Usando la aproximación \(\sqrt{150}\approx 12,25\) m, ¿cuántos metros de cerca hay que comprar?
15. Andrés afirma que \(\sqrt{9+16}=\sqrt{9}+\sqrt{16}\). Comprueba si tiene razón calculando los dos lados y explica con tus palabras qué regla está usando mal.

## Respuestas para el docente

1. a) \(8\) b) \(11\) c) \(2\) d) \(-4\) e) \(3\)
2. a) \(0,7\) b) \(\frac{3}{5}=0,6\) c) \(1\) d) \(10\) e) \(0\)
3. No existen en \(\mathbb{R}\): **a), c) y d)**, porque tienen índice par y radicando negativo. b) \(=-2\) y e) \(=-1\), porque el índice es impar.
4. a) entre 4 y 5 \(\left(16<20<25\right)\) b) entre 7 y 8 \(\left(49<50<64\right)\) c) entre 9 y 10 \(\left(81<90<100\right)\) d) entre 3 y 4 \(\left(27<30<64\right)\)
5. a) \(7^{1/2}\) b) \(5^{1/3}\) c) \(x^{1/4}\) d) \(x^{3/2}\)
6. a) \(2\sqrt{2}\) b) \(4\sqrt{3}\) c) \(5\sqrt{3}\) d) \(10\sqrt{2}\)
7. a) \(\sqrt{36}=6\) b) \(\sqrt{25}=5\) c) \(5\) d) \(\sqrt{16}=4\)
8. a) \(5\sqrt{5}\) b) \(3\sqrt{2}+2\sqrt{2}=5\sqrt{2}\) c) \(3\sqrt{3}-2\sqrt{3}=\sqrt{3}\) d) \(4\sqrt{2}\)
9. a) \(\sqrt{16}=4\) b) \(\sqrt[3]{27}=3\) c) \(\sqrt[4]{81}=3\) d) \(\left(\sqrt[3]{8}\right)^{2}=2^{2}=4\)
10. a) \(\frac{\sqrt{2}}{2}\) b) \(\frac{3\sqrt{5}}{5}\) c) \(\frac{6\sqrt{3}}{3}=2\sqrt{3}\)
11. a) \(\sqrt{64}=\) **8 m**. b) Perímetro \(=4\times 8=\) **32 m**.
12. Lado \(=\sqrt{400}=20\) m. Perímetro \(=80\) m. Costo \(=80\times 18.000=\) **$1.440.000**.
13. \(\sqrt[3]{216}=\) **6 dm**, es decir **60 cm**.
14. a) Irracional. b) Entre 12 y 13, porque \(144<150<169\). c) \(\sqrt{150}=\sqrt{25\times 6}=5\sqrt{6}\). d) Perímetro \(\approx 4\times 12,25=49\) m; conviene comprar **49 m** o un poco más.
15. \(\sqrt{9+16}=\sqrt{25}=5\), mientras que \(\sqrt{9}+\sqrt{16}=3+4=7\). **No tiene razón.** Está aplicando a una **suma** una regla que solo vale para productos y cocientes.

## Cierre

Idea para recordar: la raíz deshace la potencia, se simplifica sacando cuadrados perfectos y **se reparte sobre productos, nunca sobre sumas**.

Quedó una pregunta sin responder: \(\sqrt{-9}\) no existe entre los números reales. Los matemáticos no se resignaron a eso e inventaron un número nuevo. En la próxima clase lo conocemos.
