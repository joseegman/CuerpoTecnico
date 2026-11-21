# Conectar Gmail, Google Drive y Microsoft 365 en Claude Desktop

Claude Desktop soporta servidores MCP (Settings → MCP, o editando el fichero de configuración).
Ruta del fichero de configuración:

- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`

## Configuración de ejemplo

Copia este bloque en `claude_desktop_config.json` (créalo si no existe):

```json
{
  "mcpServers": {
    "gmail": {
      "type": "remote",
      "url": "https://gmailmcp.googleapis.com/mcp/v1"
    },
    "drive": {
      "type": "remote",
      "url": "https://drivemcp.googleapis.com/mcp/v1"
    },
    "ms365": {
      "type": "local",
      "command": ["npx", "-y", "@softeria/ms-365-mcp-server"]
    }
  }
}
```

## Requisitos previos (una sola vez)

- **Gmail / Google Drive (MCP oficiales de Google):** necesitas un proyecto en Google Cloud, habilitar
  las APIs (Gmail, Drive) y crear credenciales OAuth. La primera vez, Claude Desktop abrirá el flujo de
  autorización en el navegador.
- **Microsoft 365 (`ms-365-mcp-server`):** necesitas una app registrada en Microsoft Entra con permisos
  de Graph (`Mail.ReadWrite`, `Mail.Send`, `Calendars.ReadWrite`, `Files.ReadWrite`...) y `npx` instalado.

## Qué permite en este sistema

- El rol `documentador` puede **enviar emails** (convocatorias, comunicados a deportistas y rivales),
  **subir/leer ficheros en Drive** (formularios, informes) y crear eventos de calendario.
- El rol `analista-rendimiento` puede leer informes compartidos en Drive.
- El resto de roles debe delegar cualquier envío/gestión externa en el `documentador` (relevo).

## Alternativas

- `workspace-mcp` (muy completo: Gmail, Drive, Calendar, **Google Forms**): `uvx workspace-mcp`.
- `outlook-local-mcp` o `MCP-MS365` si prefieres otro servidor de Microsoft 365.

Reinicia Claude Desktop tras editar el fichero de configuración.