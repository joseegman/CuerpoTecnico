# Cuerpo Técnico — Versión para AnythingLLM

Versión del Cuerpo Técnico de selección olímpica (judo y artes marciales) adaptada a **AnythingLLM**
(Mintplex Labs), para gente no técnica que usa un chat tipo ChatGPT pero con control total de los datos
(se puede ejecutar local, sin enviar nada a la nube).

## Qué incluye

| Carpeta | Contenido |
|---|---|
| `instrucciones-agente.md` | Prompt maestro del agente «Cuerpo Técnico» (se pega en el system prompt del agente) |
| `roles/*.md` | Tarjeta de cada miembro del Cuerpo Técnico (se suben al workspace o se usan por rol) |
| `mcp/README.md` | Cómo conectar Gmail, Google Drive y Microsoft 365 (MCP compatible) |
| `../temporadas/` | La carpeta de temporada del proyecto (se sube al workspace para RAG) |

## Configuración paso a paso (una sola vez)

> **¿No eres de informática?** Sigue el [manual de instalación completo](../manuales/anythingllm.md),
> con pasos exactos, cómo obtener la clave de API y solución de problemas.

1. **Instala AnythingLLM** (Desktop: Windows/macOS/Linux; o Docker para multiusuario con permisos).
2. **Crea un workspace** llamado p. ej. «Cuerpo Técnico 2026».
3. **Sube la documentación del workspace (RAG):**
   - `AGENTS.md` (constitución)
   - `temporadas/2026/**` (calendario, planificación, formularios, equipos)
   - las tarjetas `roles/*.md`
4. **Crea el agente.** En el workspace: Settings → Agents → **Custom Agent**, nombre «cuerpo-tecnico»,
   y pega el contenido de `instrucciones-agente.md` como system prompt.
5. **Activa los skills** del agente que necesites (Settings → Agent Skills): Web Search / Web-Browsing
   (para analista y documentador), y los **MCPs** de Gmail/Drive/M365 si quieres envíos y nube (ver `mcp/`).
6. **(Opcional) Un agente por rol:** crea un Custom Agent por miembro (entrenador-principal,
   entrenador-tecnica, preparador-fisico, etc.) y usa cada tarjeta de `roles/` como su system prompt.
   Así el chat distingue roles con mención directa.

## Uso diario

- En el workspace, invoca el agente con **`@cuerpo-tecnico <tu mensaje>`** (o el nombre del agente).
- Empieza indicando el rol: **`Rol: entrenador-principal`** (si no lo indicas, asume entrenador-principal).
- Habla en lenguaje normal: «objetivos de la temporada…», «pide el cuestionario de tono y forma…».
- Si la tarea pertenece a otro rol, el agente te lo indicará y te dirá a qué rol cambiar (relevo manual).
- Los ficheros que genere el agente (formularios, informes) los guardará en tu escritorio o los podrás
  copiar a `temporadas/` (AnythingLLM no edita las carpetas del proyecto directamente; usa sus
  skills/memoria o los MCP de Drive para guardar).

## Privacidad (importante)

- En la versión **Desktop** (usuario único) la separación de `medicina/**` y `psicologia/**` es **por
  convención**: sube esas carpetas solo si aceptas que el mismo agente las vea, e instruye no resumirlas.
- En la versión **Docker (multiusuario)**: crea **workspaces separados** para `medicina/` y `psicologia/`
  con acceso restringido a los usuarios autorizados (médico/psicólogo). Es la opción más segura de la
  familia AnythingLLM.

## Límites honestos de esta versión

- No hay aislamiento real por rol dentro de un mismo workspace: la disciplina la impone el prompt.
- No hay delegación automática entre agentes: el humano hace de coordinador.
- Los agentes no escriben directamente en las carpetas del proyecto: guardan en escritorio/memoria o vía
  MCP (Drive). Para edición directa de ficheros se necesita la versión opencode.