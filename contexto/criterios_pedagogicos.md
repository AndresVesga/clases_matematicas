# Criterios pedagógicos del proyecto

Este archivo es la **fuente de verdad** de las reglas de generación. Cualquier clase nueva —de esta o de otra unidad— debe cumplirlas.

## Público y nivel

Estudiantes de colegio (educación secundaria). Nivel escolar, no universitario.
Se asume atención fragmentada: explicaciones cortas, ejemplos frecuentes, cambios de dinámica.

## Duración

Cada clase está diseñada para una sesión de 80 minutos.
**No se escribe minutaje interno.** Nunca aparecen marcas como "Introducción — 10 min" o "Actividad — 30 min". El documento es una secuencia pedagógica continua y el docente administra el ritmo.

## Estructura obligatoria de una clase

En este orden:

1. Título claro y atractivo.
2. Pregunta o situación de entrada (engancha, no revela la explicación).
3. Objetivos de aprendizaje: **exactamente 2**, concretos y observables (empiezan con un verbo de acción: clasificar, calcular, representar, resolver, comparar, aplicar…).
4. Desarrollo conceptual: teoría mínima necesaria, símbolos definidos antes de usarse, errores frecuentes señalados.
5. **Exactamente 3 ejemplos resueltos**, de menor a mayor dificultad; el tercero preferiblemente aplicado.
6. Actividad práctica: **exactamente 15 problemas**.
7. Respuestas para el docente, en sección separada.

## Reglas de los ejemplos resueltos

Cada ejemplo plantea el problema, muestra el procedimiento paso a paso, explica brevemente por qué se hace cada operación clave y cierra con la respuesta final destacada.

## Reglas de los 15 problemas

Distribución aproximada:

* problemas 1 a 5: comprensión directa de lo explicado;
* problemas 6 a 10: aplicación con más pasos;
* problemas 11 a 14: situaciones contextualizadas;
* problema 15 (o 14 y 15): reto alcanzable, nunca de nivel universitario.

Todos deben resolverse con lo enseñado hasta ese momento. Se evita la repetición mecánica: se varía el tipo de pregunta (calcular, clasificar, corregir un error, comparar, decidir, justificar).

## Contexto colombiano

Cuando resulte natural, los problemas usan situaciones cotidianas de Colombia: compras y descuentos, supermercado, transporte y TransMilenio, distancias entre ciudades, datos móviles y planes de celular, recibos, temperaturas, deportes, videojuegos, ahorro, pequeñas ventas y emprendimientos, áreas de habitaciones o terrenos, construcción, viajes, alturas, velocidades, situaciones escolares.

El dinero siempre se expresa en **pesos colombianos**.
No se fuerza la referencia local cuando resulta artificial.
El contexto no es decorativo: el problema debe exigir matemáticas reales.

## Lenguaje

Sencillo, directo, escolar. Frases cortas. Se evita el vocabulario universitario cuando existe una forma escolar equivalente.
Tampoco se infantiliza: el estudiante debe sentir que trabaja con matemáticas serias y útiles.

## Progresión de la dificultad

Dentro de cada clase y a lo largo de la unidad: **básico → intermedio → aplicación**.
Cada concepto nuevo sigue la lógica **idea intuitiva → explicación → ejemplo → aplicación**.
No se introducen varios conceptos nuevos al mismo tiempo.
Cada clase prepara conceptualmente la siguiente y no repite lo ya cubierto.

## Retención y participación

Dentro del desarrollo se incluyen intervenciones breves que el docente lanza en voz alta, marcadas como **Pregunta al curso** o **Mini reto**: predecir un resultado antes de calcularlo, detectar un error, comparar dos respuestas, escoger entre dos procedimientos.
Se usan solo donde aportan; el documento no se convierte en un cuestionario.

## Formato

* Sin líneas divisorias: no se usa `---` ni separadores decorativos equivalentes. La jerarquía se logra con títulos, subtítulos, listas y espacios.
* Sin minutaje por secciones.
* Lectura visualmente ligera: bloques cortos, listas, tablas pequeñas, negrita para lo esencial.
* Notación matemática **entre `` $` `` y `` `$ ``**: todo lo que va ahí se convierte en una ecuación real de Word (fracciones con raya, raíces con cajón, exponentes bien formados) y GitHub la renderiza igual. Se escribe `` $`\frac{2}{3}`$ `` y no `2/3`; `` $`\sqrt{-9}`$ `` y no `√(−9)`; `` $`2^{5}`$ `` y no `2⁵`.
* Se usa ese delimitador y no el signo de pesos suelto porque el peso colombiano aparece en casi todos los enunciados: `$3.200` debe seguir siendo texto normal.
* Comandos disponibles: `\frac{}{}`, `\sqrt{}`, `\sqrt[n]{}`, `^{}`, `_{}`, `\times`, `\div`, `\cdot`, `\pm`, `\approx`, `\le`, `\ge`, `\ne`, `\pi`, `\ldots`, `\overline{}`, `\mathbb{R}`, `\left( \right)`, `\text{}`.
* Las unidades y el dinero van **fuera** de la fórmula: `` $`6\times 225=1.350`$ `` cm², no dentro.
* **Los ítems a), b), c) de un ejercicio van en vertical**, como sublista, uno por línea:

```
1. Calcula:
   - a) ...
   - b) ...
```

* **Un párrafo por línea, separados por una línea en blanco.** Dos líneas seguidas sin línea en blanco entre ellas quedan pegadas como un solo párrafo en GitHub.

## Validación matemática

Antes de dar por terminada una clase se verifican operaciones, signos, exponentes, raíces, clasificaciones numéricas, operaciones con complejos y **las respuestas de los 15 ejercicios**.
Ninguna respuesta puede contradecir el enunciado. Ante la duda, se recalcula.

## Lista de verificación final por clase

* ¿Exactamente 2 objetivos?
* ¿Explicación clara para nivel escolar?
* ¿Exactamente 3 ejemplos resueltos?
* ¿Exactamente 15 ejercicios?
* ¿Los ejercicios corresponden a lo enseñado?
* ¿Hay aplicaciones cotidianas relevantes?
* ¿Las respuestas son correctas?
* ¿La dificultad aumenta progresivamente?
* ¿Cabe razonablemente en 80 minutos?
* ¿Sin minutaje y sin líneas divisorias?
* ¿La lectura es ligera?
* ¿La clase siguiente continúa de forma lógica?
