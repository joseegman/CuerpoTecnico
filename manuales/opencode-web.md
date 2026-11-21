# Manual de instalación — opencode (versión web)

Para personas **sin conocimientos de informática**. Guía con pasos exactos, qué tienes que ver en
cada paso y qué hacer si algo falla.

> opencode es una herramienta pensada para técnicos. **Para ti** el uso es un navegador como el del
> banco o el correo. Solo necesitas que **una persona técnica haga una vez la Parte A**.

---

## 1. Qué necesitas antes de empezar

- Un ordenador (Windows o Mac) conectado a internet.
- Una persona con conocimientos de informática para hacer la **Parte A** una sola vez (15–20 minutos).
- No necesitas instalar nada tú mismo.

## 2. En 1 minuto: cómo funciona

1. El técnico instala opencode en el ordenador y lo deja «encendido».
2. Tú abres el navegador (Chrome, Edge o Safari).
3. Escribes una dirección (te la dará el técnico) y entras en un chat.
4. Hablas con el **Entrenador principal** y él coordina a todo el Cuerpo Técnico.

---

## 3. Instalación paso a paso

### PARTE A — Lo que hace el técnico (solo una vez)

> Imprime o pasa esta parte a tu técnico.

1. Instalar **Node.js LTS** desde https://nodejs.org (siguiente → siguiente → instalar).
2. Abrir una ventana de terminal (PowerShell o WSL en Windows) y ejecutar:
   ```
   npm install -g opencode-ai
   ```
3. Conectar la cuenta de la IA que se vaya a usar:
   ```
   opencode auth login
   ```
   (elegir el proveedor, p. ej. Anthropic, y autorizar en el navegador).
4. Ir a la carpeta del proyecto Cuerpo Técnico:
   ```
   cd "C:\Users\user\Develop\CuerpoTecnico"
   ```
5. Arrancar la versión web con contraseña:
   ```
   $env:OPENCODE_SERVER_USERNAME="opencode"
   $env:OPENCODE_SERVER_PASSWORD="EligeUnaContraseñaSegura"
   opencode web
   ```
6. Anotar la dirección que aparece (p. ej. `http://localhost:4096`). Si se quiere que la usen otras
   personas en la misma red, arrancar con `opencode web --hostname 0.0.0.0` y darles la dirección IP
   de red (p. ej. `http://192.168.1.20:4096`).

**Comprobación del técnico:** al abrir esa dirección aparece una ventana de usuario y contraseña.

### PARTE B — Tu uso diario (sin conocimientos técnicos)

1. Abre el navegador.
2. Escribe la dirección que te ha dado el técnico y pulsa Enter.
3. Introduce el **usuario** (`opencode`) y la **contraseña** que te hayan dado.
4. Pulsa **«New session»** (nueva conversación).
5. Comprueba que arriba aparece el agente **«entrenador-principal»** (si no, pulsa la tecla `Tab`
   hasta verlo).
6. Ya puedes escribir. Ejemplo para empezar:
   > Objetivos de la temporada: clasificar 3 deportistas para el Mundial y 2 para los Juegos.
   > Calendario: Grand Prix de Viena (marzo), Europeo (abril), Mundial (septiembre).

---

## 4. Comprobación de que todo funciona

- ¿Ves la conversación y el entrenador-principal responde en español? → Instalación correcta.
- Pídele: «Crea el plan de temporada 2026». Debería crear documentos en las carpetas de la temporada.
- Pídele: «Pide el cuestionario inicial a los deportistas». Debería aparecer un formulario.

## 5. Uso diario (resumen)

- El entrenador-principal es tu puerta de entrada: le cuentas objetivos y él planifica y delega.
- Los agentes crean las carpetas y documentos que necesitan: **tú no subes documentos** a las carpetas.
- Tu tarea es **usar** los formularios y documentos, rellenarlos y dejarlos en las mismas carpetas.
- Los documentos **no se sobrescriben**: si pides rehacer algo, se añade `-v2` al nombre.
- **Eliminar documentos** lo decides tú (bórralos del ordenador si quieres quitarlos).
- Todo queda en `temporadas/2026/...` del ordenador.

## 6. Problemas frecuentes

| Problema | Solución |
|---|---|
| No se abre la dirección | El ordenador donde está instalado debe estar encendido con la ventana del técnico abierta. Avísale. |
| No recuerdo la contraseña | Pídesela al técnico (la cambia en el paso 5 de la Parte A). |
| La conversación se corta o va lenta | Cierra el navegador, vuelve a abrir la dirección y entra de nuevo. |
| El agente dice que no puede hacer algo | Puede ser que necesite permiso: pregunta «¿puedes delegar en el documentador?». |

## 7. Dónde están tus archivos

En el ordenador donde está instalado opencode:
`C:\Users\user\Develop\CuerpoTecnico\temporadas\2026\`