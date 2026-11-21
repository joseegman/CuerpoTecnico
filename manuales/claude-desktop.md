# Manual de instalación — Claude Desktop

Para personas **sin conocimientos de informática**. Pasos exactos, qué verás en cada paso y qué hacer
si algo falla.

---

## 1. Qué necesitas antes de empezar

- Un ordenador (Windows 10/11 o macOS).
- Conexión a internet.
- Una cuenta de **Claude** (se crea gratis en https://claude.ai). Para uso intensivo se recomienda un
  plan de pago (Claude Pro o Max).

## 2. En 1 minuto: cómo funciona

1. Instalas el programa **Claude** en el ordenador.
2. Creas un **Proyecto** llamado «Cuerpo Técnico 2026» dentro del programa.
3. Añades las carpetas del Cuerpo Técnico al proyecto.
4. Pegas las instrucciones del proyecto.
5. Chateas con Claude y él actúa como el Cuerpo Técnico completo (cambias de rol con `Rol: ...`).

## 3. Instalación paso a paso

### Paso 1 — Instalar el programa Claude

1. Abre tu navegador y entra en **https://claude.ai/download**.
2. Pulsa el botón de descarga para tu sistema (Windows o Mac).
3. Abre el archivo descargado (suele estar en «Descargas»).
   - **Windows:** haz doble clic y pulsa «Sí» / «Ejecutar» cuando lo pida.
   - **Mac:** arrastra el icono de Claude a la carpeta «Aplicaciones».
4. Abre Claude. Te pedirá **iniciar sesión**: escribe tu correo y contraseña de Claude (o crea la cuenta
   aquí mismo si aún no la tienes).

**Comprobación:** al abrir Claude ves una ventana de chat con un recuadro para escribir.

### Paso 2 — Crear el Proyecto «Cuerpo Técnico 2026»

1. En la barra lateral (a la izquierda) busca **«Projects»** o **«Proyectos»**.
2. Pulsa **«New Project»** o **«Nuevo proyecto»**.
3. Ponle de nombre: **Cuerpo Técnico 2026**.
4. Pulsa «Crear».

### Paso 3 — Añadir las carpetas del Cuerpo Técnico

1. Dentro del proyecto, busca el icono de **adjuntar** (un clip o el botón «Add files» / «Añadir archivos»)
   o arrastra y suelta las carpetas directamente en la ventana del proyecto.
2. Añade estas dos carpetas (están en el ordenador, dentro de `CuerpoTecnico`):
   - `claude-desktop` (las tarjetas de los roles y las instrucciones)
   - `temporadas` (calendario, planificación y equipos)

**Comprobación:** al abrir el proyecto ves los archivos de esas carpetas listados.

### Paso 4 — Pegar las instrucciones del proyecto

1. Abre el archivo **`claude-desktop/instrucciones-proyecto.md`** (haz doble clic en el ordenador).
2. Copia TODO el contenido (clic derecho → copiar, o `Ctrl+C`).
3. En Claude Desktop, dentro del proyecto, busca las **instrucciones personalizadas** (Custom
   Instructions / «Cómo debe responder») y pégalo todo (`Ctrl+V`).
4. Guarda.

**Comprobación:** al escribir en el chat del proyecto la frase `Rol: entrenador-principal`, Claude
responde como el entrenador principal.

---

## 4. Comprobación de que todo funciona

- Escribe en el chat del proyecto:
  > `Rol: entrenador-principal`. Crea el plan de temporada 2026 con estos objetivos: clasificar
  > 3 deportistas para el Mundial y 2 para los Juegos.
- Si te responde un plan organizado en español → instalación correcta.

## 5. Uso diario (resumen)

- Cada mensaje empieza con `Rol: <rol>` (por defecto es el entrenador-principal).
- Si Claude te dice «esto corresponde a otro rol», cambia de rol escribiendo `Rol: <ese rol>`.
- Los agentes crean las carpetas y documentos que necesitan: **tú no subes documentos** a las carpetas.
- Tu tarea es **usar** los formularios, rellenarlos y dejarlos en las mismas carpetas.
- Los documentos **no se sobrescriben**: si pides rehacer algo, se añade `-v2` al nombre.
- **Eliminar documentos** lo decides tú.

## 5b. Generar informes en Excel o PDF

- Pide al asistente: «dame este informe en Excel», «en PDF» o «en ambos».
- El asistente te dará el texto listo para copiar en Excel o para imprimir a PDF.
- Si tienes conectado Google Drive/Docs (ver `claude-desktop/mcp/`), puede crear el archivo por ti.

## 6. Problemas frecuentes

| Problema | Solución |
|---|---|
| No veo «Projects» | Actualiza Claude a la última versión o usa https://claude.ai en el navegador (los proyectos también existen en la web). |
| No encuentro el archivo de instrucciones | Pide a quien te pasó el proyecto que te indique la ruta, o usa el buscador de Windows (`temporadas`/`claude-desktop`). |
| Claude no recuerda los roles | Vuelve a pegar las instrucciones en el proyecto y escribe `Rol: entrenador-principal`. |
| El chat va lento | Cierra y vuelve a abrir Claude, o usa la versión web https://claude.ai. |

## 7. Dónde están tus archivos

En el ordenador, en la carpeta del proyecto:
`C:\Users\user\Develop\CuerpoTecnico\temporadas\2026\`