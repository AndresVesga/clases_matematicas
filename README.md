# Clases de Matemáticas

Este proyecto es un **taller para escribir, editar y entregar clases escolares**.
Las clases se escriben una sola vez en archivos de texto sencillos y de ahí salen los documentos Word listos para imprimir o compartir.

Contenido actual: una unidad de **6 clases de 80 minutos** sobre números reales, potenciación, radicación y números complejos.

## Qué hay en cada carpeta

| Carpeta | Qué contiene |
|---|---|
| `contexto/` | Las reglas del proyecto: cómo debe ser una clase, quién la dicta y la plantilla en blanco. |
| `clases/` | **El contenido real de las clases.** Aquí se edita todo. |
| `banco_ejercicios/` | Ejercicios extra por clase, con respuestas, para tarea o refuerzo. |
| `entregables/word/` | Los documentos `.docx` generados. Se pueden abrir, editar e imprimir. |
| `scripts/` | Un programa pequeño que convierte las clases a Word. |
| `recursos/` | Espacio para material complementario y futuras actividades interactivas. |

## Dónde modificar una clase

Abre el archivo de la clase en `clases/` (por ejemplo `clases/clase_03.md`) con el Bloc de notas o cualquier editor de texto.
Es texto normal: se escribe encima y se guarda.

Detalles útiles del formato:

* `#` al comienzo de una línea es un título grande, `##` uno mediano y `###` uno pequeño.
* El texto entre dos asteriscos, así `**importante**`, sale en **negrita**.
* Las listas con viñetas empiezan con `*` y las numeradas con `1.`, `2.`, etc.

**Los archivos de `clases/` son la fuente principal.** Si editas directamente el Word, ese cambio se pierde la próxima vez que se regeneren los documentos.

## Cómo generar otra vez los Word

Una sola vez, para instalar lo que necesita el conversor:

```
pip install python-docx
```

Y luego, cada vez que quieras actualizar los documentos:

```
python scripts/md_a_word.py
```

Eso vuelve a crear los seis archivos de `entregables/word/` y también el documento único con toda la unidad:
`Matematicas_Unidad_Numeros_Reales_y_Complejos.docx`.

Para convertir una sola clase:

```
python scripts/md_a_word.py clases/clase_03.md
```

## Cómo crear clases nuevas

Basta con pedirlo en lenguaje normal, por ejemplo:

> "Crea cuatro clases sobre ecuaciones lineales."

Quien las escriba debe leer primero `contexto/criterios_pedagogicos.md` y `contexto/docente.md`, y luego seguir `contexto/plantilla_clase.md`. Los archivos nuevos van en `clases/` con el nombre `clase_07.md`, `clase_08.md`, y así.

Si prefieres hacerlo a mano: copia `contexto/plantilla_clase.md`, guárdalo en `clases/` con el nombre que sigue y reemplaza el contenido entre corchetes.

Al terminar, vuelve a correr `python scripts/md_a_word.py`.

## Cómo cambiar de tema o de área

Las reglas del proyecto no dependen de las matemáticas: sirven igual para física, química o sociales.

1. Ajusta `contexto/docente.md` si cambia el área, el nivel o la duración de la clase.
2. Deja `contexto/criterios_pedagogicos.md` como está, salvo que quieras cambiar una regla de fondo (por ejemplo, pasar de 15 a 10 problemas por clase).
3. Escribe las clases nuevas en `clases/` siguiendo la plantilla.

Si vas a manejar varias unidades a la vez, lo más cómodo es crear subcarpetas dentro de `clases/`, por ejemplo `clases/numeros/` y `clases/ecuaciones/`.

## Dónde están las reglas pedagógicas

En **`contexto/criterios_pedagogicos.md`**. Ese archivo manda: define el nivel escolar, la estructura obligatoria de cada clase (dos objetivos, tres ejemplos resueltos, quince problemas), el uso de contextos colombianos, el tipo de lenguaje, la progresión de dificultad y las dos reglas de formato del proyecto: **sin minutaje por secciones y sin líneas divisorias**.

Si quieres cambiar cómo se escriben las clases, cambia ese archivo y no cada clase por separado.

## Más adelante

La carpeta `recursos/interactivos/` está reservada para actividades sencillas en HTML (quizzes, tarjetas de preguntas, verdadero/falso, ejercicios que se autocorrigen). Todavía no hay ninguna, y cuando las haya serán archivos sueltos que se abren con doble clic en el navegador, sin instalar nada.
