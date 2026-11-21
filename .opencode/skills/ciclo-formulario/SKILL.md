---
name: ciclo-formulario
description: Ciclo de vida completo de formularios y encuestas del Cuerpo Técnico (judo/artes marciales). Úsala cuando haya que solicitar, generar, desplegar, responder o archivar un formulario/encuesta, o cuando un agente necesite recoger información de deportistas.
---

# Ciclo de formularios y encuestas

Proceso canónico para que el staff mida el tono, la forma y las condiciones de los deportistas.
El único agente que genera/despliega formularios es el **documentador** (RF-04). El resto delega.

## 1. Solicitud

El agente de dominio identifica qué necesita medir y **delega en `documentador`** vía `task`, indicando:

- **Qué quiere saber** (constructo): tono, forma, condiciones, carga interna, estado de lesión, psicometría, etc.
- **A quién:** equipo(s) y/o deportistas concretos.
- **Cuándo:** momento de la temporada, plazo de respuesta.
- **Criterios:** frecuencia de repetición, escala preferida, anonimato, etc.

## 2. Generación (solo documentador)

- Define `formulario-id` (slug kebab-case).
- Crea la plantilla en `formularios/<formulario-id>.md` con:
  - Frontmatter: `dominio`, `formulario-id`, `estado: borrador`, `autor: documentador`, `fecha`.
  - Instrucciones de uso, preguntas (escalas Likert 1-5, frecuencias, abiertas), y campos de respuesta.
- Si el harness ofrece herramientas (MCP/plugin) para formularios, el documentador puede usarlas y
  dejar en la plantilla la referencia de despliegue externo.

## 3. Validación

- El documentador confirma con el agente solicitante que las preguntas miden lo necesario.
- Estado → `activo`.

## 4. Instancia (despliegue)

- Instancia por equipo en `encuestas/<dominio>/<formulario-id>/<equipo>/`.
- README de la instancia con metadatos (plazo, destinatarios).
- Un fichero de respuesta por deportista: `encuestas/<dominio>/<formulario-id>/<equipo>/<deportista>.md`
  (plantilla rellenable).

## 5. Respuestas

- El documentador crea ficheros de respuesta **nominales** por deportista (o por equipo, torneo o
  temporada según lo que se mida). El **usuario** los rellena (o los edita) y los deja en la misma carpeta.
- El documentador archiva y mantiene el estado de la encuesta.
- **Nunca se sobrescriben** formularios o respuestas previos: si el usuario quiere rehacer algo y ya
  existe, se crea una versión nueva (`<slug>-v2.md`, `-v3`, ...). Borrar documentos es decisión del usuario.

## 6. Análisis y publicación

- El agente **propietario del dominio** lee las respuestas de su dominio (las de `psicologia/**` y
  `medicina/**` son privadas y solo las lee su agente) y publica un **resumen** en `compartido/`
  (anonimizado si contiene información sensible).
- El `entrenador-principal` consolida los resúmenes y ajusta el plan.

## 7. Archivo

- El documentador marca la encuesta `estado: archivado` y lo refleja en el índice de la temporada.

## 8. Generación de informes (Excel y PDF)

- El usuario puede pedir el informe en Markdown, Excel (.xlsx) o PDF.
- El agente de dominio genera primero el informe en Markdown (con tablas) y lo guarda en su dominio.
- Si el usuario pide Excel/PDF, el `documentador` coordina la conversión:
  - En opencode: delega en `build`, que ejecuta `scripts/generar-informe.py`.
  - En Claude Desktop/AnythingLLM: usa un MCP (Google Sheets/Docs) si está conectado; si no, entrega
    el Markdown listo para exportar (CSV para Excel, imprimir a PDF).
- El `.xlsx`/`.pdf` se guarda en la misma carpeta, mismo nombre base; versionado `-v2` si ya existe.

## Convenciones

- Nombres de respuestas: `<apellido>-<nombre>.md` (nominales: por competidor, o por equipo/torneo/temporada).
- Estados: `borrador` → `activo` → `archivado`.
- Nunca generar un formulario fuera del ciclo: toda solicitud pasa por el `documentador`.
- **No sobrescribir:** si el usuario quiere rehacer algo existente, crear versión nueva (`-v2`, `-v3`, ...).
- **Borrado:** el usuario es el único responsable de eliminar documentos.