# Clase 6. Operar con números complejos

## Para empezar

Ya sabemos escribir números como $`3+2i`$ y ubicarlos en el plano. Pero un número sirve de poco si no se puede **operar**.

Antes de explicar nada, intenta esto en el cuaderno:

$`(3+5i)+(2-8i)=\;?`$

Casi seguro te salió bien, aunque nadie te lo haya enseñado. Con la multiplicación pasa algo distinto, porque aparece $`i^{2}`$ y ahí se esconde una sorpresa que cambia el resultado.

## Objetivos

Al terminar esta clase el estudiante será capaz de:

1. Sumar, restar y multiplicar números complejos en forma binómica aplicando $`i^{2}=-1`$.
2. Dividir dos números complejos usando el conjugado del denominador y expresar el resultado en la forma $`a+bi`$.

## Lo que vamos a entender

### Sumar y restar: cada parte con la suya

Un complejo tiene dos partes que **no se mezclan**, igual que no se suman metros con kilos. La parte real se opera con la parte real, y la imaginaria con la imaginaria.

$`(3+5i)+(2-8i)=(3+2)+(5-8)i=5-3i`$

Para restar, lo único delicado es **repartir el signo menos a todo el paréntesis**:

$`(4+2i)-(6-3i)=4+2i-6+3i=-2+5i`$

Fíjate en el cambio de $`-3i`$ a $`+3i`$. Es el error número uno del tema.

**Pregunta al curso:** ¿cuánto da $`(7-3i)+(-7+3i)`$? (Cero. Acabamos de sumar un complejo con su opuesto.)

### Multiplicar: como cualquier binomio, más un detalle

Se multiplica igual que $`(a+b)(c+d)`$: cada término del primer paréntesis por cada término del segundo. Lo nuevo llega al final.

$`(3+2i)(4-5i)`$

1. $`3\times 4=12`$
2. $`3\times(-5i)=-15i`$
3. $`2i\times 4=8i`$
4. $`2i\times(-5i)=-10i^{2}`$

Queda $`12-15i+8i-10i^{2}`$.

**Aquí está el detalle:** $`i^{2}`$ no se deja escrito, porque $`i^{2}=-1`$. Entonces $`-10i^{2}=-10\times(-1)=+10`$.

Resultado: $`12+10-7i=22-7i`$

Regla práctica: **multiplica normal y al final cambia $`i^{2}`$ por $`-1`$.**

**Mini reto:** ¿cuánto vale $`(2i)(3i)`$? $`\left(6i^{2}=-6\right)`$. Da un número real, y negativo.

### El producto notable que hay que memorizar

Multiplica un complejo por su **conjugado** y observa:

$`(2+3i)(2-3i)=4-6i+6i-9i^{2}=4+9=13`$

Los términos con $`i`$ **se cancelan siempre**, y el resultado es un número **real y positivo**. En general:

$`(a+bi)(a-bi)=a^{2}+b^{2}`$

Esta es la herramienta que hacía falta para dividir.

### Dividir: hacer que el denominador se vuelva real

Un resultado como $`\frac{5}{2+i}`$ no está terminado: la forma correcta de un complejo es $`a+bi`$, y ahí abajo estorba una $`i`$.

La estrategia es la misma que usamos para racionalizar en la clase 4: **multiplicar arriba y abajo por el conjugado del denominador**. Como se multiplica por lo mismo arriba y abajo, el valor no cambia.

Ejemplo: $`\frac{5}{2+i}`$

1. El conjugado del denominador es $`2-i`$.
2. Arriba: $`5\times(2-i)=10-5i`$.
3. Abajo: $`(2+i)(2-i)=2^{2}+1^{2}=5`$.
4. Queda $`\frac{10-5i}{5}`$.
5. Se separa la fracción en sus dos partes: $`\frac{10}{5}-\frac{5}{5}i=2-i`$.

Comprobación: $`(2-i)(2+i)=4+1=5`$ ✔ Volvimos al dividendo, así que está bien.

**Pregunta al curso:** ¿por qué multiplicamos justo por el conjugado y no por otra cosa? (Porque es lo único que borra la $`i`$ de abajo dejando un número real.)

### Errores frecuentes

* **No repartir el menos en la resta.** $`(4+2i)-(6-3i)`$ no es $`4+2i-6-3i`$. El signo entra a los dos términos.
* **Dejar $`i^{2}`$ en la respuesta.** Siempre se reemplaza por $`-1`$.
* **Sumar partes distintas.** $`3+2i`$ no es $`5i`$. Son cantidades de tipos diferentes.
* **$`(2i)(3i)=6i`$.** No: es $`6i^{2}=-6`$.
* **Dejar la respuesta como fracción con $`i`$ abajo.** Falta multiplicar por el conjugado.
* **Confundir $`(1+i)^{2}`$ con $`1+i^{2}`$.** Hay que desarrollar: $`(1+i)^{2}=1+2i+i^{2}=2i`$.

## Ejemplos resueltos

### Ejemplo 1 (básico)

**Problema.** Calcula:

* a) $`(3+5i)+(2-8i)`$
* b) $`(4+2i)-(6-3i)`$

**Solución.**

1. **Suma.** Se agrupan las partes reales por un lado y las imaginarias por otro, porque son cantidades de distinta naturaleza.
2. Reales: $`3+2=5`$. Imaginarias: $`5-8=-3`$.
3. Resultado: $`5-3i`$.
4. **Resta.** Primero se quita el paréntesis repartiendo el signo menos a los dos términos: $`-(6-3i)=-6+3i`$.
5. Queda $`4+2i-6+3i`$.
6. Reales: $`4-6=-2`$. Imaginarias: $`2+3=5`$.
7. Resultado: $`-2+5i`$.

**Respuesta:** a) $`5-3i`$ b) $`-2+5i`$

### Ejemplo 2 (intermedio)

**Problema.** Calcula $`(3+2i)(4-5i)`$

**Solución.**

1. Multiplicamos cada término del primer paréntesis por cada término del segundo, igual que con cualquier binomio.
2. $`3\times 4=12`$
3. $`3\times(-5i)=-15i`$
4. $`2i\times 4=8i`$
5. $`2i\times(-5i)=-10i^{2}`$
6. Reunimos: $`12-15i+8i-10i^{2}`$.
7. Reemplazamos $`i^{2}`$ por $`-1`$, que es el paso propio de los complejos: $`-10i^{2}=+10`$.
8. Agrupamos: parte real $`12+10=22`$; parte imaginaria $`-15+8=-7`$.

**Respuesta:** $`22-7i`$

### Ejemplo 3 (aplicado)

**Problema.** En un circuito de corriente alterna se cumple $`Z=V\div I`$, donde $`Z`$ es la impedancia, $`V`$ el voltaje y $`I`$ la corriente, y las tres se escriben como números complejos. Un técnico mide $`V=11+3i`$ voltios e $`I=2+i`$ amperios. ¿Cuál es la impedancia del circuito?

**Solución.**

1. Hay que calcular $`Z=\frac{11+3i}{2+i}`$. Como el denominador tiene parte imaginaria, usamos el conjugado.
2. El conjugado de $`2+i`$ es $`2-i`$. Multiplicamos arriba y abajo por él.
3. Numerador: $`(11+3i)(2-i)=22-11i+6i-3i^{2}=22-5i+3=25-5i`$.
4. Denominador: $`(2+i)(2-i)=2^{2}+1^{2}=5`$. Quedó real, que era justo lo que buscábamos.
5. Dividimos cada parte entre 5: $`\frac{25}{5}=5`$ y $`\frac{-5}{5}=-1`$.
6. Comprobamos multiplicando de vuelta: $`(5-i)(2+i)=10+5i-2i-i^{2}=10+3i+1=11+3i`$ ✔

**Respuesta:** la impedancia es $`Z=5-i`$ **ohmios**: 5 ohmios de resistencia y una reactancia de $`-1`$. Sin números complejos este cálculo, que los ingenieros hacen a diario, no se podría plantear.

## Actividad práctica

Resuelve en tu cuaderno.

**Comprensión**

1. Suma:
   - a) $`(3+2i)+(5+4i)`$
   - b) $`(-1+6i)+(4-2i)`$
   - c) $`(7-3i)+(-7+3i)`$
   - d) $`(2+i)+5`$
2. Resta:
   - a) $`(6+5i)-(2+3i)`$
   - b) $`(4-i)-(7+2i)`$
   - c) $`(-3+8i)-(-3+i)`$
   - d) $`10-(4-6i)`$
3. Multiplica:
   - a) $`3(2+5i)`$
   - b) $`-2(4-i)`$
   - c) $`0,5(6+8i)`$
   - d) $`i(3+2i)`$
4. Multiplica:
   - a) $`(1+i)(1-i)`$
   - b) $`(2+3i)(2-3i)`$
   - c) $`(1+i)^{2}`$
   - d) $`i(1-i)`$
5. Escribe **verdadero** o **falso** y corrige lo falso:
   - a) $`(2+3i)+(1+4i)=3+7i`$
   - b) $`(2i)(3i)=6i`$
   - c) $`i(2+i)=2i+1`$
   - d) El producto de un complejo por su conjugado siempre da un número real.
   - e) $`(3+i)-(3+i)=0`$

**Aplicación**

6. Multiplica:
   - a) $`(3+2i)(1+4i)`$
   - b) $`(5-i)(2+3i)`$
   - c) $`(-2+i)(3-2i)`$
   - d) $`(4+3i)(4-3i)`$
7. Calcula:
   - a) $`(2+i)^{2}`$
   - b) $`(1-3i)^{2}`$
   - c) $`i^{3}+i^{2}`$
   - d) $`(3-i)(3+i)`$
8. Divide usando el conjugado:
   - a) $`\frac{-1+5i}{1+i}`$
   - b) $`\frac{10}{1-3i}`$
   - c) $`\frac{7-i}{2-i}`$
   - d) $`\frac{6+2i}{i}`$
9. Opera:
   - a) $`(2+3i)+(4-i)-(1+2i)`$
   - b) $`2(1+i)-3(2-i)`$
10. Calcula $`(3+i)(2-i)`$ y después escribe el conjugado del resultado.

**Problemas en contexto**

11. Dos componentes conectados en serie tienen impedancias $`Z_{1}=4+3i`$ ohmios y $`Z_{2}=2-5i`$ ohmios. En serie, las impedancias se suman. ¿Cuál es la impedancia total?
12. En un circuito, $`V=Z\times I`$. Si $`Z=3+4i`$ ohmios e $`I=2-i`$ amperios, ¿cuál es el voltaje $`V`$?
13. Un videojuego guarda la posición de un personaje como el complejo $`2+3i`$, y cada desplazamiento se **suma** a la posición.
   - a) El personaje se desplaza $`4-5i`$. ¿En qué posición queda?
   - b) ¿En qué parte del plano está ahora?
   - c) ¿Qué desplazamiento tendría que hacer para llegar exactamente al origen?

**Retos**

14. Comprueba que $`3+2i`$ es solución de la ecuación $`x^{2}-6x+13=0`$, reemplazándolo y operando paso a paso.
15. Explica, sin hacer toda la multiplicación, por qué $`(a+bi)(a-bi)`$ siempre da un número real. Comprueba tu explicación con $`5+2i`$.

## Respuestas para el docente

1. a) $`8+6i`$ b) $`3+4i`$ c) $`0`$ d) $`7+i`$
2. a) $`4+2i`$ b) $`-3-3i`$ c) $`7i`$ d) $`6+6i`$
3. a) $`6+15i`$ b) $`-8+2i`$ c) $`3+4i`$ d) $`3i+2i^{2}=-2+3i`$
4. a) $`1-i^{2}=2`$ b) $`4+9=13`$ c) $`1+2i+i^{2}=2i`$ d) $`i-i^{2}=1+i`$
5. a) V. b) F: $`(2i)(3i)=6i^{2}=-6`$. c) F: $`i(2+i)=2i+i^{2}=-1+2i`$. d) V, da $`a^{2}+b^{2}`$. e) V.
6. a) $`-5+14i`$ b) $`13+13i`$ c) $`-4+7i`$ d) $`25`$
7. a) $`3+4i`$ b) $`-8-6i`$ c) $`-1-i`$, porque $`i^{3}=-i`$ e $`i^{2}=-1`$ d) $`10`$
8. a) $`2+3i`$ b) $`1+3i`$ c) $`3+i`$ d) $`2-6i`$. En d) conviene multiplicar arriba y abajo por $`-i`$, o razonar que $`\frac{1}{i}=-i`$.
9. a) $`5`$ (la parte imaginaria se cancela: $`3-1-2=0`$) b) $`-4+5i`$
10. $`(3+i)(2-i)=7-i`$; su conjugado es $`7+i`$.
11. $`Z_{1}+Z_{2}=(4+2)+(3-5)i=6-2i`$ **ohmios**.
12. $`V=(3+4i)(2-i)=6-3i+8i-4i^{2}=6+5i+4=10+5i`$ **voltios**.
13. a) $`(2+3i)+(4-5i)=6-2i`$. b) Parte real positiva y parte imaginaria negativa: abajo a la derecha. c) Necesita sumar $`-6+2i`$.
14. $`(3+2i)^{2}=9+12i+4i^{2}=9+12i-4=5+12i`$. Luego $`-6(3+2i)=-18-12i`$. Sumando todo: $`(5+12i)+(-18-12i)+13=(5-18+13)+(12-12)i=0`$ ✔
15. Al desarrollar, los términos con $`i`$ son $`-abi`$ y $`+abi`$, que se cancelan siempre; y el término con $`i^{2}`$ se vuelve real. Queda $`a^{2}+b^{2}`$. Comprobación: $`(5+2i)(5-2i)=25+4=29`$.

## Cierre

Idea para recordar: sumar y restar complejos es juntar cada parte con la suya; multiplicar es desarrollar el binomio y cambiar $`i^{2}`$ por $`-1`$; y dividir es multiplicar arriba y abajo por el **conjugado**.

Con esto cerramos el recorrido completo: empezamos preguntando qué números existen, descubrimos que a los reales les faltaba algo, y terminamos operando con soltura en un conjunto donde **toda raíz tiene respuesta**.
