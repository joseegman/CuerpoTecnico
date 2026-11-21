# Cuerpo Técnico — Selección Olímpica (Judo y Artes Marciales)

> **¿No eres de informática?** Empieza por aquí. Este manual explica qué es el proyecto y cómo
> instalarlo en tu programa habitual (ChatGPT, Claude Desktop o AnythingLLM) **sin necesidad de
> programar**.

---

## ¿Qué es esto?

Un **equipo de asistentes de inteligencia artificial** que te ayuda a gestionar una selección olímpica
de judo y artes marciales. Cada asistente tiene un rol (como un cuerpo técnico real): entrenador
principal, técnica, preparación física, estiramientos, psicología, medicina, fisioterapia, nutrición y
análisis de rendimiento. También hay un **documentador** que genera formularios y encuestas.

Trabajas con **carpetas y archivos de texto** (como los de Word, pero más sencillos). Los asistentes
crean y editan esos archivos; tú rellenas los formularios y dejas los archivos donde están.

## ¿Qué te da?

- **Planificación** de la temporada (calendario de competiciones, concentraciones, picos de forma).
- **Formularios y encuestas** para conocer el tono, la forma y las condiciones de cada deportista.
- **Resúmenes** de cada área (técnica, física, nutrición, etc.) para que el entrenador principal
  ajuste el plan.
- **Privacidad**: la medicina y la psicología son confidenciales (solo su asistente las lee).

## ¿En qué programa lo uso?

Elige el que te resulte más cómodo:

| Programa | Lo mejor para... | Guía de instalación |
|---|---|---|
| **ChatGPT** | Si ya usas ChatGPT y quieres cero instalación | [Manual ChatGPT](manuales/claude-desktop.md) (muy parecido) |
| **Claude Desktop** | Interfaz de chat cómoda, con proyectos y archivos | [Manual Claude Desktop](manuales/claude-desktop.md) |
| **AnythingLLM** | Si quieres que todo se quede en tu ordenador (privado) | [Manual AnythingLLM](manuales/anythingllm.md) |
| **opencode** | Si alguien técnico te lo instala y quieres el sistema completo | [Manual opencode](manuales/opencode-web.md) |

> **Recomendación para no técnicos:** Claude Desktop o ChatGPT (no requieren instalación técnica).

## Instalación rápida (Claude Desktop, la más sencilla)

1. Instala **Claude Desktop** desde https://claude.ai/download y entra con tu cuenta.
2. Crea un **Proyecto** llamado «Cuerpo Técnico 2026».
3. Añade las carpetas `claude-desktop/` y `temporadas/` al proyecto.
4. Pega el contenido de `claude-desktop/instrucciones-proyecto.md` en las instrucciones del proyecto.
5. Escribe en el chat: `Rol: entrenador-principal` y empieza.

**Pasos detallados con imágenes de botones y solución de problemas:** [Manual completo](manuales/claude-desktop.md).

## Instalación rápida (AnythingLLM, todo en tu ordenador)

1. Instala **AnythingLLM** desde https://anythingllm.com.
2. Configura el «cerebro» (pega tu clave de API de OpenAI o Anthropic en el primer arranque).
3. Crea un **workspace** «Cuerpo Técnico 2026» y sube los documentos (`AGENTS.md`, `temporadas/`,
   `roles/`).
4. Crea un **agente** llamado `cuerpo-tecnico` y pega el contenido de `anythingllm/instrucciones-agente.md`.

**Pasos detallados:** [Manual completo](manuales/anythingllm.md).

## Primer uso (ejemplo)

Escribe esto en el chat:

> `Rol: entrenador-principal`. Objetivos de la temporada: clasificar 3 deportistas para el Mundial
> y 2 para los Juegos. Calendario: Grand Prix de Viena (marzo), Europeo (abril), Mundial
> (septiembre). Crea el plan de temporada 2026 y decide qué encuestas iniciales necesitamos.

El entrenador principal elaborará el plan y, si necesita información de los deportistas, pedirá al
documentador que genere los formularios.

## Cómo se trabaja día a día

- **No tienes que crear ni subir documentos** a las carpetas: los asistentes crean las suyas y las
  editan.
- **Tu tarea** es usar los formularios y documentos generados, rellenarlos y dejarlos donde están.
- Los formularios son **nominales** (un fichero por competidor, equipo, torneo o temporada).
- **Nunca se sobrescriben** documentos: si pides rehacer algo, se crea una versión nueva (`-v2`,
  `-v3`, ...).
- **Eliminar documentos** es tu decisión: bórralos tú si ya no los quieres.

## Generar informes en Excel o PDF

Puedes pedir a los asistentes que te den cualquier informe en **Excel (.xlsx)** o **PDF** (además del
texto normal, que siempre se guarda).

- Dile: «dame este informe en Excel», «en PDF» o «en ambos».
- En **Claude Desktop / ChatGPT**: el asistente te da el texto listo para copiar en Excel o para
  imprimir a PDF (también puede crear el archivo si tienes conectado Google Drive/Docs).
- En **AnythingLLM**: igual, con la opción de guardar en tu ordenador o en Drive si tienes MCP.
- En **opencode** (si un técnico te lo instaló): el sistema genera el archivo `.xlsx`/`.pdf`
  automáticamente en la carpeta del informe.

Ejemplo de petición:

> `Rol: analista-rendimiento`. Haz el informe de scouting de los rivales del próximo torneo y
> **dámelo en Excel y PDF**.

## Privacidad y datos personales (importante)

- La medicina y la psicología son **confidenciales** (categoría especial por RGPD).
- En Claude Desktop y ChatGPT la protección se basa en las instrucciones (no en bloqueos técnicos).
- En AnythingLLM en **Docker multiusuario** puedes aislar las carpetas de medicina y psicología en
  espacios de trabajo restringidos (más seguro).
- Antes de compartir el repositorio con otras personas, revisa qué incluyes de `temporadas/`.

## ¿Dónde están mis archivos?

Todo está en la carpeta del proyecto:
- `temporadas/<año>/` — calendario, planificación, formularios y equipos de la temporada.
- Dentro de cada equipo: `compartido/` (resúmenes visibles a todos), y una subcarpeta por dominio
  (`tecnica/`, `preparacion-fisica/`, `psicologia/`, `medicina/`, `nutricion/`, etc.).

## Más información

- [Análisis completo de requisitos](docs/analisis-requisitos.md)
- [Constitución operativa (reglas del cuerpo técnico)](AGENTS.md)
- [Manuales de instalación (no técnicos)](manuales/)