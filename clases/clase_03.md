# Clase 3. Potenciación: cuando multiplicar muchas veces se vuelve enorme

## Para empezar

Le mandas un video a **4** amigos. Cada uno se lo manda a otros **4**. Y esos, a otros **4**.

Si eso se repite **diez veces**, ¿cuántas personas lo habrán visto en la última ronda?

Escribe tu predicción en el cuaderno antes de calcular nada. Casi siempre el número real es muchísimo más grande de lo que uno piensa, y hoy vamos a ver por qué.

## Objetivos

Al terminar esta clase el estudiante será capaz de:

1. Calcular potencias de números reales aplicando correctamente las reglas de signo, el exponente cero y el exponente negativo.
2. Simplificar expresiones usando las propiedades de la potenciación y expresar cantidades muy grandes o muy pequeñas en notación científica.

## Lo que vamos a entender

### Qué es una potencia

Sumar el mismo número muchas veces se abrevia multiplicando: $`5+5+5+5=4\times 5`$.

**Multiplicar** el mismo número muchas veces también se abrevia. Ahí aparece la potencia:

$`3\times 3\times 3\times 3=3^{4}`$

Los nombres, que hay que usar bien:

* **Base:** el número que se repite (aquí, el 3).
* **Exponente:** cuántas veces se repite (aquí, el 4).
* Se lee "tres elevado a la cuarta" y vale 81.

**Pregunta al curso:** ¿$`3^{4}`$ y $`4^{3}`$ son lo mismo? Predícelo antes de calcular. (No: 81 contra 64. La base y el exponente no se pueden intercambiar.)

### El signo: la trampa más común del tema

Todo depende de **dónde está el paréntesis**.

**Si la base es negativa y está dentro del paréntesis**, el signo también se multiplica:

* $`(-2)^{3}=(-2)\times(-2)\times(-2)=-8`$
* $`(-2)^{4}=(-2)\times(-2)\times(-2)\times(-2)=16`$

Regla corta: **exponente par da positivo, exponente impar conserva el negativo.**

**Si no hay paréntesis**, el signo se queda afuera y solo se eleva el número:

* $`-2^{4}`$ significa "el opuesto de $`2^{4}`$", o sea $`-16`$.

Compara: $`(-2)^{4}=16`$ pero $`-2^{4}=-16`$. **Un paréntesis cambia el resultado.**

### Exponente 0, 1 y negativo

**Exponente 1:** $`7^{1}=7`$. La base aparece una sola vez.

**Exponente 0:** cualquier número (distinto de 0) elevado a 0 da **1**.

$`7^{0}=1`$, $`100^{0}=1`$, $`(-3)^{0}=1`$.

¿Por qué? Mira el patrón bajando de a un exponente: $`2^{3}=8`$, $`2^{2}=4`$, $`2^{1}=2`$. Cada paso divide entre 2. El siguiente paso da $`2^{0}=2\div 2=1`$.

**Exponente negativo:** significa **dar la vuelta a la fracción**, no que el resultado sea negativo.

$`2^{-3}=\frac{1}{2^{3}}=\frac{1}{8}`$

Siguiendo el mismo patrón de antes: después de $`2^{0}=1`$ viene $`2^{-1}=1\div 2=\frac{1}{2}`$. Todo encaja.

**Error clásico:** creer que $`2^{-3}=-8`$. Falso: $`2^{-3}=\frac{1}{8}`$, que es **positivo**.

### Las propiedades

Sirven para no calcular de más. Todas se explican con la definición.

**Misma base, se multiplican → se suman los exponentes**

$`4^{3}\times 4^{5}=4^{8}`$

(Tres cuatros por cinco cuatros son ocho cuatros.)

**Misma base, se dividen → se restan los exponentes**

$`7^{9}\div 7^{6}=7^{3}=343`$

**Potencia de una potencia → se multiplican los exponentes**

$`\left(5^{3}\right)^{2}=5^{6}`$

**Potencia de un producto → cada factor se eleva**

$`(2y)^{3}=2^{3}y^{3}=8y^{3}`$

**Advertencia importante:** estas propiedades **no** valen para sumas.

$`(3+4)^{2}`$ **no** es $`3^{2}+4^{2}`$. Comprueba: $`(3+4)^{2}=49`$, mientras que $`9+16=25`$.

**Mini reto:** simplifica $`2^{4}\times 2^{-6}`$ sin calculadora. $`\left(2^{-2}\text{, o sea }\frac{1}{4}\right)`$

### Notación científica

Sirve para escribir números enormes o diminutos sin llenar el renglón de ceros.

Un número en notación científica se escribe como **un número entre 1 y 10, multiplicado por una potencia de 10**.

* $`45.000=4,5\times 10^{4}`$ (la coma se corrió 4 lugares a la izquierda)
* $`0,0007=7\times 10^{-4}`$ (se corrió 4 lugares a la derecha, por eso el exponente es negativo)

Regla práctica: **exponente positivo, número grande; exponente negativo, número pequeño.**

### Errores frecuentes

* **$`3^{2}=6`$.** No. No se multiplica base por exponente: $`3^{2}=3\times 3=9`$.
* **$`2^{3}\times 2^{2}=2^{6}`$.** No: los exponentes se **suman**, da $`2^{5}=32`$.
* **$`2^{-3}`$ es negativo.** No: es $`\frac{1}{8}`$, positivo.
* **$`(3+4)^{2}=3^{2}+4^{2}`$.** No: primero se resuelve el paréntesis.
* **$`-5^{2}=25`$.** No: sin paréntesis, es $`-25`$. Con paréntesis, $`(-5)^{2}=25`$.

## Ejemplos resueltos

### Ejemplo 1 (básico)

**Problema.** Calcula:

* a) $`(-2)^{5}`$
* b) $`(-2)^{4}`$
* c) $`-2^{4}`$
* d) $`5^{0}`$
* e) $`3^{-2}`$

**Solución.**

1. **$`(-2)^{5}`$**: la base negativa está dentro del paréntesis y el exponente es impar, así que el resultado es negativo. $`2^{5}=32`$, entonces da $`-32`$.
2. **$`(-2)^{4}`$**: base negativa, exponente par → positivo. $`2^{4}=16`$, da $`16`$.
3. **$`-2^{4}`$**: aquí no hay paréntesis, así que el signo no se eleva. Se calcula $`2^{4}=16`$ y se le pone el menos: $`-16`$.
4. **$`5^{0}`$**: todo número distinto de cero elevado a 0 da $`1`$.
5. **$`3^{-2}`$**: el exponente negativo invierte: $`3^{-2}=\frac{1}{3^{2}}=\frac{1}{9}`$.

**Respuesta:** $`-32`$; $`16`$; $`-16`$; $`1`$; $`\frac{1}{9}`$

### Ejemplo 2 (intermedio)

**Problema.** Simplifica y calcula: $`\left(3^{2}\right)^{3}\div\left(3^{4}\times 3\right)`$

**Solución.**

1. Empezamos por el paréntesis de la izquierda. Potencia de una potencia: se multiplican los exponentes. $`\left(3^{2}\right)^{3}=3^{6}`$.
2. En el paréntesis de la derecha hay dos potencias de la misma base multiplicándose, así que se suman los exponentes. Recuerda que 3 es $`3^{1}`$: $`3^{4}\times 3^{1}=3^{5}`$.
3. Ahora tenemos $`3^{6}\div 3^{5}`$. Misma base dividiéndose: se restan los exponentes. $`3^{6-5}=3^{1}`$.
4. $`3^{1}=3`$.

**Respuesta:** $`3`$. Sin propiedades habríamos tenido que calcular $`729\div 243`$; con ellas fueron tres restas mentales.

### Ejemplo 3 (aplicado)

**Problema.** Laura vende stickers por Instagram. En enero vendió 50 y desde entonces **duplica** sus ventas cada mes.

* a) ¿Cuántos stickers venderá en junio?
* b) Si cada sticker cuesta $1.500, ¿cuánto factura ese mes?

**Solución.**

1. Lo primero es contar bien las duplicaciones, que es donde casi todos se equivocan. De enero a junio hay **cinco** pasos: febrero, marzo, abril, mayo y junio.
2. Duplicar cinco veces es multiplicar por 2 cinco veces, o sea por $`2^{5}`$.
3. $`2^{5}=32`$.
4. Ventas de junio: $`50\times 32=1.600`$ stickers.
5. Facturación: $`1.600\times 1.500=`$ $2.400.000.

**Respuesta:** en junio venderá **1.600 stickers** y facturará **$2.400.000**. Fíjate en lo que hace la potenciación: en apenas cinco meses las ventas se multiplicaron por 32, no por 10.

## Actividad práctica

Resuelve en tu cuaderno.

**Comprensión**

1. Escribe como potencia y calcula:
   - a) $`3\times 3\times 3\times 3`$
   - b) $`5\times 5`$
   - c) $`2\times 2\times 2\times 2\times 2\times 2`$
   - d) $`10\times 10\times 10`$
2. Calcula:
   - a) $`(-2)^{3}`$
   - b) $`(-2)^{4}`$
   - c) $`-2^{4}`$
   - d) $`(-5)^{2}`$
   - e) $`-5^{2}`$
3. Calcula:
   - a) $`7^{0}`$
   - b) $`7^{1}`$
   - c) $`1^{9}`$
   - d) $`0^{5}`$
   - e) $`(-1)^{100}`$
4. Escribe sin exponente negativo y calcula:
   - a) $`2^{-3}`$
   - b) $`5^{-2}`$
   - c) $`10^{-1}`$
   - d) $`\left(\frac{1}{3}\right)^{-2}`$
5. Escribe **verdadero** o **falso** y corrige lo falso:
   - a) $`3^{2}=6`$
   - b) $`(-4)^{2}=16`$
   - c) $`2^{3}\times 2^{2}=2^{6}`$
   - d) $`5^{0}=0`$
   - e) $`\left(3^{2}\right)^{3}=3^{6}`$

**Aplicación**

6. Aplica las propiedades y deja una sola potencia:
   - a) $`4^{3}\times 4^{5}`$
   - b) $`7^{9}\div 7^{6}`$
   - c) $`\left(5^{3}\right)^{2}`$
   - d) $`2^{4}\times 2^{-6}`$
7. Simplifica:
   - a) $`\left(a^{3}\cdot a^{4}\right)\div a^{2}`$
   - b) $`\left(x^{2}\right)^{5}`$
   - c) $`(2y)^{3}`$
   - d) $`m^{5}\div m^{5}`$
8. Calcula paso a paso y compara los resultados de cada pareja:
   - a) $`3^{2}+4^{2}`$
   - b) $`(3+4)^{2}`$
   - c) $`2^{3}\times 3^{2}`$
   - d) $`(2\times 3)^{2}`$
9. Escribe en notación científica:
   - a) $`45.000`$
   - b) $`0,0007`$
   - c) $`3.200.000`$
   - d) $`0,00012`$
10. Escribe en notación decimal normal:
   - a) $`2,5\times 10^{3}`$
   - b) $`9\times 10^{-2}`$
   - c) $`1,08\times 10^{6}`$

**Problemas en contexto**

11. Un plan de celular ofrece $`2^{5}`$ GB al mes y ver un capítulo de serie consume $`2^{-1}`$ GB.
   - a) ¿Cuántos GB trae el plan?
   - b) ¿Cuántos GB consume un capítulo?
   - c) ¿Cuántos capítulos alcanzan a verse con el plan completo?
12. Camila fabrica manillas y cada mes **triplica** su producción. En marzo hizo 5 manillas. ¿Cuántas hará en julio?
13. Reenvías un video a 4 personas y cada una lo reenvía a otras 4.
   - a) ¿Cuántas personas lo reciben en la tercera ronda?
   - b) ¿Y en la quinta?
   - c) ¿Cuántas lo han recibido en total después de esas cinco rondas?

**Retos**

14. La distancia de la Tierra al Sol es de unos $`1,5\times 10^{8}`$ km y la luz viaja a $`3\times 10^{5}`$ km por segundo. ¿Cuántos segundos tarda la luz del Sol en llegar a la Tierra? Expresa también el resultado en minutos.
15. En un colegio de 900 estudiantes se riega un rumor: el día 1 lo saben 2 estudiantes y cada día el número se duplica. ¿En qué día lo sabría todo el colegio?

## Respuestas para el docente

1. a) $`3^{4}=81`$ b) $`5^{2}=25`$ c) $`2^{6}=64`$ d) $`10^{3}=1.000`$
2. a) $`-8`$ b) $`16`$ c) $`-16`$ d) $`25`$ e) $`-25`$. Insistir en la diferencia entre b) y c), y entre d) y e).
3. a) $`1`$ b) $`7`$ c) $`1`$ d) $`0`$ e) $`1`$ (exponente par).
4. a) $`\frac{1}{8}`$ b) $`\frac{1}{25}`$ c) $`\frac{1}{10}=0,1`$ d) $`\left(\frac{1}{3}\right)^{-2}=3^{2}=9`$.
5. a) F, es $`9`$. b) V. c) F, los exponentes se suman: $`2^{5}=32`$. d) F, es $`1`$. e) V.
6. a) $`4^{8}`$ b) $`7^{3}=343`$ c) $`5^{6}`$ d) $`2^{-2}=\frac{1}{4}`$
7. a) $`a^{5}`$ b) $`x^{10}`$ c) $`8y^{3}`$ d) $`m^{0}=1`$
8. a) $`25`$ b) $`49`$ c) $`72`$ d) $`36`$. Conclusión: la potencia **no** se reparte sobre una suma (a y b son distintos), pero **sí** sobre un producto, porque $`(2\times 3)^{2}=36=2^{2}\times 3^{2}`$.
9. a) $`4,5\times 10^{4}`$ b) $`7\times 10^{-4}`$ c) $`3,2\times 10^{6}`$ d) $`1,2\times 10^{-4}`$
10. a) $`2.500`$ b) $`0,09`$ c) $`1.080.000`$
11. a) $`2^{5}=32`$ GB. b) $`2^{-1}=0,5`$ GB. c) $`32\div 0,5=`$ **64 capítulos**.
12. De marzo a julio hay 4 pasos: $`5\times 3^{4}=5\times 81=`$ **405 manillas**.
13. a) $`4^{3}=64`$. b) $`4^{5}=1.024`$. c) $`4+16+64+256+1.024=`$ **1.364 personas**.
14. $`\left(1,5\times 10^{8}\right)\div\left(3\times 10^{5}\right)=0,5\times 10^{3}=`$ **500 segundos**, es decir 8 minutos y 20 segundos.
15. El día $`n`$ lo saben $`2^{n}`$ estudiantes. $`2^{9}=512`$ (todavía no alcanza) y $`2^{10}=1.024`$ (ya supera 900). Sería el **día 10**.

## Cierre

Idea para recordar: la potencia es una multiplicación repetida, el exponente negativo **invierte** en vez de cambiar el signo, y el paréntesis decide si el signo se eleva o no.

En la próxima clase haremos el camino contrario: si $`5^{2}=25`$, ¿qué número elevado al cuadrado da 25? Esa pregunta al revés es la radicación.
