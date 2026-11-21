# Manual de instalación — AnythingLLM

Para personas **sin conocimientos de informática**. Pasos exactos, qué verás en cada paso y qué hacer
si algo falla.

---

## 1. Qué necesitas antes de empezar

- Un ordenador (Windows 10/11 o macOS) con conexión a internet.
- Una **clave de API** de un proveedor de IA (OpenAI, Anthropic, Google, etc.). Es como una contraseña
  de acceso al «cerebro» de la IA:
  - **OpenAI:** entra en https://platform.openai.com → «API keys» → «Create new secret key» → copia la
    clave (empieza por `sk-...`).
  - **Anthropic:** entra en https://console.anthropic.com → «API Keys» → «Create Key» → copia la clave
    (empieza por `sk-ant-...`).
  - Guarda la clave en un sitio seguro. Si no tienes cuenta, créala primero (puede requerir meter una
    tarjeta para el uso; sin uso, sin coste).

> Alternativa local (sin internet ni claves): conectar un modelo local (Ollama). Es algo más técnico;
> al final de este manual hay una nota.

## 2. En 1 minuto: cómo funciona

1. Instalas el programa **AnythingLLM** en el ordenador.
2. En la primera puesta en marcha le dices qué «cerebro» usar (pegas tu clave de API).
3. Creas un **espacio de trabajo** («workspace») llamado «Cuerpo Técnico 2026».
4. Subes los documentos del Cuerpo Técnico a ese espacio.
5. Creas el **agente** «cuerpo-tecnico» con las instrucciones del proyecto.
6. Chateas escribiendo `@cuerpo-tecnico` y el Cuerpo Técnico responde.

## 3. Instalación paso a paso

### Paso 1 — Instalar el programa

1. Abre tu navegador y entra en **https://anythingllm.com**.
2. Pulsa **«Download»** y descarga la versión para tu sistema (Windows o Mac).
3. Abre el archivo descargado (en «Descargas») e instala como cualquier programa (siguiente →
   siguiente → instalar).
4. Abre **AnythingLLM**.

### Paso 2 — Configurar el «cerebro» (LLM) la primera vez

1. Al abrirlo por primera vez, saldrá un asistente de configuración.
2. En **LLM Provider** elige tu proveedor:
   - **OpenAI** → pega tu clave `sk-...`.
   - **Anthropic** → pega tu clave `sk-ant-...` y elige el modelo (p. ej. Claude Sonnet).
   - (Si no aparece asistente: menú **Settings → LLM Preference** y elige el proveedor igualmente.)
3. Pulsa **«Test Connection»** (probar conexión). Debe decir algo como «Connected» (conectado).
4. Pulsa **Guardar** / **Save**.

**Comprobación:** en la parte inferior de la pantalla ves un recuadro donde escribir, como un chat.

### Paso 3 — Crear el espacio de trabajo

1. En la barra lateral pulsa **«New Workspace»** o el símbolo **+**.
2. Ponle de nombre: **Cuerpo Técnico 2026**.
3. Pulsa «Create» / «Crear».

### Paso 4 — Subir los documentos del Cuerpo Técnico

1. Entra en el workspace «Cuerpo Técnico 2026».
2. Busca **«Upload Documents»** / «Subir documentos» y arrastra y suelta estos archivos y carpetas
   (están en el ordenador, dentro de `CuerpoTecnico`):
   - `AGENTS.md`
   - todas las tarjetas de `anythingllm/roles/` (10 archivos)
   - los documentos de `temporadas/2026/` (calendario, planificación, formularios, equipos)
3. Espera a que termine de procesarlos (aparecerán en la lista de documentos del workspace).

**Comprobación:** los documentos aparecen listados en el workspace.

### Paso 5 — Crear el agente del Cuerpo Técnico

1. Abre la configuración del workspace (rueda dentada de «Cuerpo Técnico 2026»).
2. Ve a la sección **«Agents»** / «Agente» y pulsa **«Custom Agent»** / «Crear agente».
3. Nombre del agente: **cuerpo-tecnico**.
4. En el cuadro de **instrucciones / system prompt**, pega el contenido del archivo
   **`anythingllm/instrucciones-agente.md`** (ábrelo con doble clic, copia todo con `Ctrl+C`, pega con
   `Ctrl+V`).
5. Guarda / Save.

### Paso 6 — Activar las herramientas del agente (recomendado)

1. Ve a **Settings → Agent Skills**.
2. Activa (enciende) **Web Search** y **Web-Browsing** (búsqueda en internet). Esto permite al analista
   consultar datos actualizados.
3. Guarda.

**Comprobación final:** en el chat del workspace escribe:

> `@cuerpo-tecnico` Rol: entrenador-principal. Crea el plan de temporada 2026 con estos objetivos:
> clasificar 3 deportistas para el Mundial y 2 para los Juegos.

Si responde un plan organizado en español → instalación correcta.

---

## 4. Uso diario (resumen)

- Empieza siempre con `@cuerpo-tecnico` y luego `Rol: <rol>` (por defecto es entrenador-principal).
- Si el agente te dice que la tarea es de otro rol, escribe `Rol: <ese rol>` y se la pides.
- Los agentes crean el contenido que necesitan: **tú no subes documentos** a las carpetas del equipo
  (la «subida» del paso 4 solo sirve para que el programa conozca tus carpetas la primera vez).
- Tu tarea es **usar** los formularios, rellenarlos y dejar los archivos en las mismas carpetas.
- Los documentos **no se sobrescriben**: si pides rehacer algo, se añade `-v2` al nombre.
- **Eliminar documentos** lo decides tú.

## 5. Problemas frecuentes

| Problema | Solución |
|---|---|
| «Test Connection» falla | Revisa que la clave esté bien copiada (sin espacios) y que tengas internet. |
| El agente no responde con `@cuerpo-tecnico` | Comprueba que el agente se llame exactamente `cuerpo-tecnico` y que hayas guardado. |
| No recuerda los documentos | Asegúrate de haber subido los documentos al workspace y espera a que terminen de procesarse. |
| Va muy lento | Cierra y vuelve a abrir AnythingLLM. |
| Quiero que no salga nada de internet | En Settings → Agent Skills desactiva Web Search / Web-Browsing. |

## 6. Alternativa local (sin internet, opcional)

Para no usar claves de API ni enviar nada a la nube:
1. Instala **Ollama** (https://ollama.com) y en el asistente inicial elige **Ollama** como LLM Provider y
   un modelo (p. ej. `llama3.1` o `qwen`). La configuración del resto es idéntica.
2. Requiere un ordenador potente y algo más de paciencia; es la opción más privada.

## 7. Dónde están tus archivos

En el ordenador, en la carpeta del proyecto:
`C:\Users\user\Develop\CuerpoTecnico\temporadas\2026\`

Los documentos que genere el agente los guardará en tu escritorio o en la carpeta de descargas; cópialos
a la carpeta de la temporada para tenerlo todo junto.