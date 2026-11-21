# Cuerpo Técnico — Versión para Claude Desktop

Versión del Cuerpo Técnico de selección olímpica (judo y artes marciales) adaptada a **Claude Desktop**,
para personas no técnicas que ya usan un chat (similar a ChatGPT).

> Diferencia clave con la versión opencode: Claude Desktop **no impone permisos por rol** ni delegación
> automática. La separación de dominios y la privacidad se mantienen **por convención** (instrucciones).
> Es más cómodo de usar, pero menos estricto.

## Qué incluye

| Carpeta | Contenido |
|---|---|
| `instrucciones-proyecto.md` | Instrucciones del Proyecto (se pegan en Claude Desktop). Es la «constitución» |
| `roles/*.md` | Tarjeta de cada miembro del Cuerpo Técnico (Claude los lee del Proyecto) |
| `mcp/claude_desktop_config.json.example` | Ejemplo para conectar Gmail, Google Drive y Microsoft 365 |
| `../temporadas/` | La misma carpeta de temporada del proyecto (se añade al Proyecto de Claude) |

## Configuración paso a paso (una sola vez)

> **¿No eres de informática?** Sigue el [manual de instalación completo](../manuales/claude-desktop.md),
> con pasos exactos y solución de problemas.

1. **Crea un Proyecto en Claude Desktop** llamado p. ej. «Cuerpo Técnico 2026».
2. **Añade estas carpetas al Proyecto:** `claude-desktop/` y `temporadas/` (en el Proyecto → Files/Folders).
3. **Pega el contenido de `instrucciones-proyecto.md`** en las instrucciones personalizadas del Proyecto
   (Project → Custom Instructions / «Cómo debe responder»).
4. **(Opcional) Conecta Gmail/Drive/Microsoft 365:** ver `mcp/README.md` y el JSON de ejemplo.

## Uso diario (para el staff no técnico)

- Abre el Proyecto y escribe **`Rol: entrenador-principal`** (o el rol que quieras) al inicio del mensaje.
- Habla en lenguaje normal: «objetivos de la temporada…», «pide a los deportistas el cuestionario de
  tono y forma…».
- Si la tarea pertenece a otro rol, Claude lo **indicará y te dirá a qué rol cambiar** (relevo manual).
- Los documentos quedan guardados en las carpetas de `temporadas/`, igual que en la versión opencode.

## Límites honestos de esta versión

- Cualquier persona con acceso al Proyecto puede leer todo (no hay bloqueo real de `medicina/` ni
  `psicologia/`). Se protegen por **instrucción**: Claude no debe resumir contenido clínico/psicológico
  en `compartido/`.
- No hay delegación automática entre agentes: el humano hace de coordinador siguiendo el relevo.
- Los formularios que genera el documentador se rellenan en el chat o en los ficheros del Proyecto.