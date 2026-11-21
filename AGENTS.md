# AGENTS.md — Cuerpo Técnico de Selección Olímpica (Judo y Artes Marciales)

Constitución operativa del Cuerpo Técnico de agentes. Todo agente de este proyecto la lee y la cumple.
El análisis de requisitos completo vive en `docs/analisis-requisitos.md`.

## 1. Propósito

Un Cuerpo Técnico de agentes da soporte integral a una selección olímpica de judo (y artes marciales):
planificación, técnica, preparación física, estiramientos/movilidad, psicología, medicina, fisioterapia,
nutrición, análisis de rendimiento y documentación. Cada agente actúa **solo en su dominio**; cuando se
necesita algo de otro dominio, se **delega** al agente experto.

## 2. Estructura de carpetas

```
temporadas/<año>/
├── README.md                  # Índice de la temporada (documentador)
├── calendario/                # Competiciones, concentraciones y convocatorias — entrenador-principal
│   └── convocatorias.md       # Plazos y criterios de selección por categoría
├── planificacion/             # Plan de temporada — entrenador-principal
├── formularios/               # Plantillas de formularios — documentador
└── equipos/
    ├── README.md              # Lista de equipos
    └── <equipo>/
        ├── README.md          # Ficha del equipo (categorías, deportistas)
        ├── compartido/        # Resúmenes y actas visibles a todo el staff
        ├── tecnica/           # entrenador-tecnica
        ├── preparacion-fisica/# preparador-fisico
        ├── estiramientos/     # entrenador-estiramientos
        ├── psicologia/        # PRIVADO — psicologo-deportivo
        ├── medicina/          # PRIVADO — medico-deportivo
        ├── fisioterapia/      # fisioterapeuta
        ├── nutricion/         # nutricionista
        ├── rendimiento/       # analista-rendimiento
        └── encuestas/         # Instancias y respuestas — documentador
            └── <dominio>/<formulario-id>/<equipo>/<deportista>.md
```

## 3. Agentes y dominios

| Agente | Escribe (exclusivo) | Función |
|---|---|---|
| `entrenador-principal` | `planificacion/`, `calendario/`, `compartido/` | Coordina, planifica, calendariza, decide qué info pedir, delega |
| `entrenador-tecnica` | `tecnica/` | Técnica y táctica de judo (incl. kata y normativa de arbitraje) |
| `preparador-fisico` | `preparacion-fisica/` | S&C, acondicionamiento, tests, carga |
| `entrenador-estiramientos` | `estiramientos/` | Flexibilidad, movilidad, estiramiento |
| `psicologo-deportivo` | `psicologia/` (**privado**) | Preparación mental, psicometría |
| `medico-deportivo` | `medicina/` (**privado**) | Aptitud, lesiones, peso seguro, antidopaje |
| `fisioterapeuta` | `fisioterapia/` | Rehabilitación, vuelta al tatami, vendajes |
| `nutricionista` | `nutricion/` | Nutrición, peso/categorías, suplementación |
| `analista-rendimiento` | `rendimiento/` | Ranking IJF y nacional (RFEJYDA), scouting, informes |
| `documentador` | `formularios/`, `encuestas/`, READMEs de temporada | Genera/organiza formularios y encuestas |

## 4. Reglas de oro

1. **Aislamiento de dominio:** cada agente escribe SOLO en su dominio (y en `compartido/`). Los
   permisos del harness lo bloquean; el prompt lo refuerza. No intentes escribir donde no tienes permiso.
2. **Privacidad:** `medicina/**` y `psicologia/**` son de acceso restringido (solo su agente propietario).
   La información clínica/psicológica sale de esos dominios como **resúmenes anonimizados** en `compartido/`.
3. **Un solo documentador:** ningún agente genera formularios/encuestas. Se solicitan delegando en el
   agente `documentador` (RF-04).
4. **Delegación:** si una tarea pertenece al expertise de otro agente, no la improvises: delega vía
   `task` y espera su resultado/resumen.
5. **Comunicación por ficheros:** los acuerdos y resúmenes se publican en `compartido/`; no «hables»
   con otros agentes fuera del mecanismo de delegación del harness.
6. **No ejecutes bash:** el staff no ejecuta comandos de sistema salvo el agente `build`.

## 5. Ciclo de vida de formularios y encuestas

1. Un agente de dominio identifica qué necesita medir (tono, forma, condiciones, psicometría, estado de salud, etc.).
2. **Delega la solicitud en `documentador`** indicando: qué quiere saber, a quién (equipo/deportistas), cuándo, y cualquier criterio.
3. El documentador genera el formulario (plantilla en `formularios/`) y despliega la instancia en `encuestas/<dominio>/<formulario-id>/<equipo>/`.
4. El documentador despliega la instancia y crea los ficheros de respuesta **nominales** (por
   deportista, o por equipo/torneo/temporada según lo que se mida):
   `encuestas/<dominio>/<formulario-id>/<equipo>/<deportista>.md`.
5. El **usuario** rellena los ficheros de respuesta (o los edita) y los deja en la misma carpeta; el
   agente propietario del dominio los lee y publica un **resumen** en `compartido/`.
6. El entrenador-principal consolida y ajusta el plan.
7. Al terminar, el documentador archiva la encuesta (`estado: archivado`).

Los formularios son **nominales** (por competidor, equipo, torneo o temporada) y **nunca se sobrescriben**:
si el usuario quiere rehacer uno existente se crea versión nueva (`-v2`, `-v3`, ...). **Borrar documentos
es decisión exclusiva del usuario.**

Detalle del workflow: skill `ciclo-formulario`.

## 6. Convenciones de ficheros

- Nombres de registros: `YYYY-MM-DD-<slug>.md` (fechas ISO).
- Fichas de deportista por dominio: `<dominio>/fichas/<apellido>-<nombre>.md`.
- Frontmatter mínimo en documentos de dominio:
  ```yaml
  equipo: <slug-del-equipo>
  deportista: <nombre> (si aplica)
  dominio: <tecnica|preparacion-fisica|...>
  estado: borrador|activo|archivado
  autor: <agente>
  fecha: YYYY-MM-DD
  ```
- Estados: `borrador` → `activo` → `archivado`.
- **Subcarpetas:** cada agente crea en su dominio las subcarpetas y documentos que precise; el usuario
  no sube documentos: los usa, los rellena/edita y los deja en las mismas carpetas.
- **Formularios nominales:** un fichero por competidor, o por equipo/torneo/temporada, según lo que se mida.
- **Versionado:** nunca sobrescribas un documento existente; si se rehace, crea versión nueva
  (`<slug>-v2.md`, `-v3`, ...).
- **Borrado:** solo el usuario elimina documentos; los agentes no borran archivos.

## 7. Flujo de trabajo típico

1. El usuario envía **objetivos** y **calendario de competiciones** al entrenador-principal.
2. El entrenador-principal crea/actualiza `planificacion/plan-temporada.md` y `calendario/competiciones.md`.
3. Decide qué información necesita de los deportistas y solicita los formularios al documentador.
4. Cada agente de dominio analiza sus respuestas y publica resúmenes en `compartido/`.
5. El entrenador-principal ajusta la planificación y delega tareas específicas.

## 7.1 Selección y normativa federativa

- Las competiciones federativas (RFEJYDA) se organizan por categorías de **edad** (alevín, infantil,
  cadete, junior, senior) y de **peso**. Las fichas de equipo y deportista incluyen ambas.
- El entrenador-principal mantiene `calendario/convocatorias.md` (plazos, criterios oficiales y
  convocados) y distingue en `competiciones.md` entre competición, concentración y stage (modelo CGTD).
- El entrenador-tecnica vigila la normativa de arbitraje y la modalidad de kata; el analista sigue el
  Ranking Nacional RFEJYDA además del IJF.
- Psicólogo y médico aplican el protocolo de prevención en el deporte (entornos seguros).

## 10. Generación de informes (Excel y PDF)

Los agentes pueden generar informes en **Excel (.xlsx)** y/o **PDF** según lo que pida el usuario, además
del Markdown (que siempre se conserva como fuente auditable).

- **Quién:** el `documentador` coordina la generación; la conversión la ejecuta el agente `build`
  (único con acceso a `bash`) usando `scripts/generar-informe.py`.
- **Cómo pedirlo:** el usuario dice «dame este informe en Excel», «en PDF» o «en ambos». El agente
  genera primero el informe en Markdown y luego lo convierte.
- **Dónde:** el `.xlsx`/`.pdf` se guarda en la misma carpeta del dominio que el `.md`, con el mismo
  nombre base (p. ej. `2026-09-10-scouting-rivales.xlsx`).
- **Versionado:** si ya existe, se crea `-v2`, `-v3`, ...; nunca se sobrescribe. El borrado es del usuario.
- **En Claude Desktop / AnythingLLM:** el agente produce el informe en Markdown y, si hay un MCP
  conectado (Google Docs/Sheets), genera el archivo ahí; si no, entrega el Markdown listo para exportar
  (CSV para Excel, imprimir a PDF).

Ver `scripts/README.md`.

## 8. Cómo escalar

- **Nueva temporada:** crear `temporadas/<año>/` copiando la estructura (o pedírselo al documentador).
- **Nuevo equipo:** crear `equipos/<slug>/` con sus subcarpetas de dominio (o pedírselo al documentador).
- **Nuevo deportista:** crear ficha en cada dominio relevante: `<dominio>/fichas/<apellido>-<nombre>.md`.
- **Nueva disciplina (otra arte marcial):** crear un equipo nuevo; los agentes reutilizan los mismos dominios.

## 9. Notas de privacidad

- Las carpetas `medicina/` y `psicologia/` contienen datos personales de categoría especial (RGPD).
- No publicar información clínica bruta en `compartido/`; solo conclusiones operativas anonimizadas.
- Antes de subir el repositorio a un control de versiones compartido, revisar qué se incluye de `temporadas/`.