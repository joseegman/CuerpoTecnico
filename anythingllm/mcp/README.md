# Conectar Gmail, Google Drive y Microsoft 365 en AnythingLLM

AnythingLLM es **compatible con MCP** (v1.16+). Los servidores MCP se configuran en la interfaz:

1. Ve a **Settings → Agent Skills** (o la sección MCP de tu versión).
2. **Añade un MCP server** y pega la URL (remote) o el comando (local) del servidor.
3. Habilita ese MCP en el **Custom Agent** del Cuerpo Técnico (Settings → Agents → skills del agente).
4. La primera vez, autoriza con OAuth en el navegador.

## Servidores recomendados

| Servicio | Tipo | Configuración |
|---|---|---|
| **Gmail** (Google) | remote | URL: `https://gmailmcp.googleapis.com/mcp/v1` |
| **Google Drive** (Google) | remote | URL: `https://drivemcp.googleapis.com/mcp/v1` |
| **Microsoft 365** | local | `npx -y @softeria/ms-365-mcp-server` (requiere Node.js y app en Microsoft Entra) |
| Alternativa completa | local | `uvx workspace-mcp` (Gmail + Drive + Calendar + **Google Forms**) |

## Requisitos previos (una sola vez)

- **Google:** proyecto en Google Cloud con APIs de Gmail/Drive habilitadas y credenciales OAuth.
- **Microsoft:** app registrada en Microsoft Entra con permisos de Graph
  (`Mail.ReadWrite`, `Mail.Send`, `Calendars.ReadWrite`, `Files.ReadWrite`...) y `npx` instalado.

## Qué permite en este sistema

- El rol `documentador` puede **enviar emails** (convocatorias, comunicados a deportistas y rivales),
  **guardar/leer ficheros en Drive** (formularios, informes) y crear eventos de calendario.
- El rol `analista-rendimiento` puede leer informes compartidos en Drive.
- El resto de roles delega cualquier envío/gestión externa en el `documentador`.

## Nota

Si ejecutas AnythingLLM en **Docker multiusuario**, el agente del documentador puede vivir en su propio
workspace con los MCP habilitados y solo los usuarios autorizados acceden a los envíos.