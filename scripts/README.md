# scripts/ — Herramientas auxiliares del Cuerpo Técnico

## generar-informe.py

Convierte un informe en Markdown (con tablas) a **Excel (.xlsx)** y/o **PDF**.

### Uso

```bash
python scripts/generar-informe.py <entrada.md> --format xlsx pdf --out <carpeta>
```

Ejemplos:

```bash
# Generar Excel y PDF del informe de scouting
python scripts/generar-informe.py temporadas/2026/rendimiento/2026-09-10-scouting-rivales.md --format xlsx pdf

# Solo Excel
python scripts/generar-informe.py temporadas/2026/preparacion-fisica/2026-09-10-tests.md --format xlsx --out temporadas/2026/preparacion-fisica/
```

### Instalación (una sola vez, por el técnico)

```bash
pip install -r scripts/requirements.txt
```

### Quién lo usa

- En **opencode**, el agente `documentador` (o cualquier agente) delega la conversión al agente
  `build` (que tiene acceso a `bash`), que ejecuta el script y deja el `.xlsx`/`.pdf` en la carpeta
  del dominio.
- En **Claude Desktop / AnythingLLM**, el agente produce el informe en Markdown y, si el usuario
  quiere Excel/PDF, lo genera con un MCP (p. ej. Google Docs/Sheets) o le indica cómo exportarlo
  (guardar como CSV y abrir en Excel, o imprimir a PDF).

### Convención

- El informe fuente se guarda siempre como `.md` en la carpeta del dominio (auditable).
- El `.xlsx`/`.pdf` se guarda en la misma carpeta con el mismo nombre base.
- Nunca se sobrescriben: si ya existe, se crea versión (`-v2`).