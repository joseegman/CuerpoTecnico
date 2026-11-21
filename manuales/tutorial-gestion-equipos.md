# Tutorial — Gestión de clubs, colegios y equipos

Guía práctica para organizar tu trabajo con varios clubs, colegios y equipos a lo largo de una temporada.
Pensada para personas no técnicas: los asistentes crean las carpetas; tú solo tienes que pedirles lo que
necesitas con frases sencillas.

---

## 1. La idea en 30 segundos

- Una **temporada** = una carpeta `temporadas/<año>/` (ej. `temporadas/2026/`).
- Dentro, **varios equipos** (clubs, colegios, selecciones por categoría) en `equipos/<nombre>/`.
- Cada equipo tiene sus **subcarpetas por área** (técnica, física, nutrición, etc.) y un espacio
  `compartido/` donde se publican los resúmenes.
- Los asistentes crean las carpetas y los documentos; tú rellenas los formularios y los dejas donde están.

## 2. Crear una nueva temporada

Escribe al **entrenador-principal**:

> Crea la temporada 2027. Objetivos: (tus objetivos). Calendario: (tus competiciones).

El entrenador principal creará la carpeta `temporadas/2027/` con su calendario, planificación y
la estructura base. También puedes pedírselo al **documentador** si prefieres.

## 3. Añadir un club, colegio o equipo

Escribe al **entrenador-principal** o al **documentador**:

> Crea el equipo `club-judo-madrid` (Judo Club Madrid, categoría cadete) en la temporada 2026.

El documentador creará la carpeta `temporadas/2026/equipos/club-judo-madrid/` con todas las subcarpetas
necesarias (técnica, preparación física, nutrición, compartido, encuestas, etc.) y su ficha.

**Consejo:** usa nombres cortos y sin espacios para la carpeta (ej. `club-madrid-cadete`,
`colegio-san-jose-junior`, `seleccion-galicia-senior`). El nombre largo va dentro de la ficha del equipo.

### Varios equipos por temporada

Puedes tener tantos como quieras en la misma temporada:

```
temporadas/2026/equipos/
├── club-judo-madrid/
├── colegio-san-jose-cadete/
├── club-barcelona-junior/
└── seleccion-galicia-senior/
```

Cada uno con sus propias subcarpetas. Los asistentes saben en cuál están trabajando porque el nombre del
equipo va en el frontmatter de cada documento.

## 4. Añadir deportistas a un equipo

Escribe al rol que corresponda (o al documentador para la ficha general):

> En `club-judo-madrid`, añade a la deportista María García, categoría -57 kg, cadete.

El rol correspondiente creará su ficha en `<dominio>/fichas/garcia-maria.md` dentro del equipo.

## 5. Planificar la temporada

1. Envía al **entrenador-principal** tus **objetivos** y el **calendario de competiciones**.
2. Él elabora `planificacion/plan-temporada.md` (macro → meso → microciclos, picos y tapering) y
   `calendario/competiciones.md` (fechas, sedes, categorías, prioridad).
3. Decide qué información necesita de los deportistas y solicita los formularios al **documentador**.

Ejemplo de prompt:

> Objetivos 2026: clasificar 3 deportistas para el Mundial y 2 para los Juegos. Calendario: Grand Prix
> de Viena (marzo), Europeo (abril), Mundial (septiembre). Crea el plan y decide qué encuestas
> iniciales necesitamos.

## 6. Recoger información (formularios)

1. El **documentador** genera el formulario (plantilla en `formularios/`) y lo despliega por equipo en
   `encuestas/<dominio>/<formulario-id>/<equipo>/`, con un fichero por deportista.
2. El deportista o el staff **rellena** los ficheros y los deja en la misma carpeta.
3. El rol propietario del dominio los lee y publica un **resumen** en `compartido/`.
4. El entrenador-principal consolida y ajusta el plan.

Los formularios son **nominales** (por competidor, equipo, torneo o temporada) y **nunca se sobrescriben**:
si quieres rehacer uno, se crea `-v2`, `-v3`, ...

## 7. Trabajar con varios equipos a la vez

- Di siempre **a qué equipo te refieres**: «en `club-judo-madrid`...», «para `colegio-san-jose-cadete`...».
- El entrenador-principal puede coordinar el plan de todos los equipos a la vez o por separado.
- Los resúmenes van a `compartido/` de cada equipo (visibles a todo el staff de ese equipo).

Ejemplo:

> Para `club-judo-madrid` y `club-barcelona-junior`, pide el cuestionario de tono y forma a todos los
> deportistas antes del Grand Prix de Viena.

## 8. Generar informes (Excel o PDF)

Pide al asistente que te da cualquier informe en **Excel (.xlsx)** o **PDF**:

> `Rol: analista-rendimiento`. Haz el informe de scouting de los rivales del próximo torneo y **dámelo
> en Excel y PDF**.

El asistente genera primero el texto y luego el archivo (`.xlsx`/`.pdf`) en la misma carpeta.

## 9. Privacidad

- `medicina/` y `psicologia/` son **confidenciales** (solo su asistente las lee).
- El resto del staff recibe resúmenes anonimizados en `compartido/`.
- No compartas el repositorio con datos personales sin revisar qué incluyes.

## 10. Resumen de quién hace qué

| Tarea | A quién pedírsela |
|---|---|
| Plan y calendario de la temporada | Entrenador principal |
| Crear equipo / temporada / deportista | Documentador (o entrenador principal) |
| Generar formularios y encuestas | Documentador |
| Técnica y táctica (incl. kata) | Entrenador de técnica |
| Fuerza, tests, carga | Preparador físico |
| Flexibilidad y movilidad | Entrenador de estiramientos |
| Preparación mental | Psicólogo deportivo |
| Aptitud médica, lesiones, peso | Médico deportivo |
| Rehabilitación | Fisioterapeuta |
| Nutrición y peso/categorías | Nutricionista |
| Datos y scouting | Analista de rendimiento |
| Organizar documentos y carpetas | Documentador |