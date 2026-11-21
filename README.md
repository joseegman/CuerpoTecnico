# Cuerpo Técnico — Selección Olímpica (Judo y Artes Marciales)

> **¿No eres de informática?** Empieza por [`README-USUARIO.md`](README-USUARIO.md), que explica qué es
> el proyecto y cómo instalarlo en ChatGPT, Claude Desktop o AnythingLLM paso a paso.

Cuerpo Técnico de agentes para dar soporte integral a una selección olímpica: planificación, técnica,
preparación física, estiramientos/movilidad, psicología, medicina, fisioterapia, nutrición, análisis de
rendimiento y documentación.

- **Análisis de requisitos:** [`docs/analisis-requisitos.md`](docs/analisis-requisitos.md)
- **Constitución operativa:** [`AGENTS.md`](AGENTS.md)
- **Configuración del harness:** [`opencode.json`](opencode.json)

## Agentes

| Agente | Rol | Modo |
|---|---|---|
| `entrenador-principal` | Coordina, planifica y calendariza; decide qué info pedir | primary (por defecto) |
| `entrenador-tecnica` | Técnica y táctica | subagent |
| `preparador-fisico` | S&C, acondicionamiento, tests, carga | subagent |
| `entrenador-estiramientos` | Flexibilidad y movilidad | subagent |
| `psicologo-deportivo` | Preparación mental (privado) | subagent |
| `medico-deportivo` | Aptitud médica (privado) | subagent |
| `fisioterapeuta` | Rehabilitación y vuelta al tatami | subagent |
| `nutricionista` | Nutrición y peso/categorías | subagent |
| `analista-rendimiento` | Datos IJF, scouting, informes | subagent |
| `documentador` | Genera/organiza formularios y encuestas | subagent |

## Manuales de instalación (para personas sin conocimientos de informática)

- [Instalar y usar opencode (web)](manuales/opencode-web.md)
- [Instalar y usar Claude Desktop](manuales/claude-desktop.md)
- [Instalar y usar AnythingLLM](manuales/anythingllm.md)

## Cómo empezar

1. Reinicia opencode (la configuración de agentes se carga al arrancar).
2. Al abrir la sesión estarás como **Entrenador principal** (`Tab` para cambiar de agente).
3. Envía al entrenador-principal los **objetivos** y el **calendario de competiciones** de la temporada.
4. Él elaborará `temporadas/<año>/planificacion/` y `calendario/`, decidirá qué información necesita de
   los deportistas y lo solicitará al `documentador`.

Ejemplo de prompt inicial:

> Objetivos de la temporada: clasificar 3 deportistas para el Mundial y 2 para los Juegos. Calendario:
> Grand Prix de Viena (marzo), Europeo (abril), Mundial (septiembre). Crea el plan de temporada 2026 y
> decide qué encuestas iniciales necesitamos.

## Generar informes en Excel o PDF

Los agentes pueden generar informes en **Excel (.xlsx)** y/o **PDF** a elección del usuario (además del
Markdown, que siempre se conserva como fuente auditable).

- Pide al agente: «dame este informe en Excel», «en PDF» o «en ambos».
- En **opencode**: el `documentador` coordina la conversión usando `scripts/generar-informe.py`
  (requiere `pip install -r scripts/requirements.txt` una vez).
- En **Claude Desktop / AnythingLLM**: el agente genera el Markdown y, si hay un MCP conectado
  (Google Sheets/Docs), crea el archivo ahí; si no, entrega el Markdown listo para exportar
  (CSV para Excel, imprimir a PDF).
- El `.xlsx`/`.pdf` se guarda en la misma carpeta del dominio, con el mismo nombre base y versionado
  `-v2` si ya existe.

Ejemplo de uso (opencode):

```bash
python scripts/generar-informe.py temporadas/2026/rendimiento/2026-09-10-scouting.md --format xlsx pdf
```

Ver `scripts/README.md`.

## Modelo de trabajo

- Los agentes **crean** en su dominio las subcarpetas y documentos que necesiten; el usuario **no sube**
  documentos a las carpetas del equipo.
- El usuario **usa** los documentos y formularios generados, rellena los formularios (nominales por
  competidor, equipo, torneo o temporada) y deja o edita los archivos en las mismas carpetas.
- **Nunca se sobrescriben** documentos previos: si algo se rehace, se crea versión nueva (`-v2`, `-v3`, ...).
- **Eliminar documentos es decisión exclusiva del usuario.**

## Estructura

```
temporadas/<año>/          # carpeta de la temporada en curso
├── calendario/            # competiciones, concentraciones y convocatorias (entrenador-principal)
├── planificacion/         # plan de temporada (entrenador-principal)
├── formularios/           # plantillas (documentador)
└── equipos/<equipo>/      # varios equipos por temporada
    ├── compartido/        # resúmenes/actas visibles a todo el staff
    ├── <dominio>/         # una subcarpeta por dominio (técnica, S&C, psicología...)
    └── encuestas/         # instancias y respuestas (documentador)
```

Cada agente **solo escribe en su dominio** (y en `compartido/`); los permisos del harness lo imponen y
`medicina/**` y `psicologia/**` son de acceso restringido. Si un agente necesita algo de otro dominio,
**delega** vía `task`.

## Versión para Claude Desktop

Para personas no técnicas (interfaz de chat similar a ChatGPT), existe una versión adaptada en
[`claude-desktop/`](claude-desktop/): un **Proyecto de Claude** por temporada con instrucciones de rol
conmutables y tarjetas por miembro del Cuerpo Técnico. La separación de dominios es por convención
(Claude Desktop no impone permisos por rol). Incluye configuración MCP para Gmail, Google Drive y
Microsoft 365.

## Versión para AnythingLLM

Versión para ejecución local/privada en [`anythingllm/`](anythingllm/): un **workspace** por temporada con
RAG sobre las carpetas, un Custom Agent «cuerpo-tecnico» (prompt maestro con cambio de rol) y, opcionalmente,
un agente por rol. AnythingLLM es compatible con MCP, así que el `documentador` puede conectar Gmail,
Google Drive y Microsoft 365. En Docker multiusuario se pueden aislar `medicina/` y `psicologia/` en
workspaces restringidos. La separación de dominios es por convención (no impone permisos por rol).

## Herramientas del harness

El `documentador` usa los MCPs/plugins disponibles del harness para generar y desplegar formularios
(p. ej. Google Forms o Notion) y cae a markdown autocontenido si no existen. Para añadir un MCP, edita
`opencode.json` (sección `mcp`) y reinicia opencode.