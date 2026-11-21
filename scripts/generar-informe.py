#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar-informe.py — Convierte un informe en Markdown a Excel (.xlsx) y/o PDF.

Uso:
  python scripts/generar-informe.py <entrada.md> --format xlsx pdf --out <carpeta>

Dependencias (instalar una vez, por el técnico):
  pip install -r scripts/requirements.txt

Ejemplo:
  python scripts/generar-informe.py temporadas/2026/rendimiento/informe-scouting.md \
      --format xlsx pdf --out temporadas/2026/rendimiento/
"""

import argparse
import os
import re
import sys


def parse_markdown(text):
    """Devuelve (titulo, lista de secciones). Cada sección: (heading, [bloques]).
    Bloques: ('p', texto) o ('table', [[celda,...], ...])."""
    lines = text.splitlines()
    title = ""
    sections = []
    current_heading = ""
    blocks = []
    table_acc = []

    def flush_table():
        nonlocal table_acc
        if table_acc:
            rows = []
            for row in table_acc:
                cells = [c.strip() for c in row.strip().strip("|").split("|")]
                rows.append(cells)
            # descarta la fila separadora (---)
            if len(rows) >= 2 and all(re.match(r"^[-: ]+$", c) for c in rows[1]):
                rows.pop(1)
            blocks.append(("table", rows))
            table_acc = []

    for line in lines:
        if line.strip().startswith("# "):
            flush_table()
            if not title:
                title = line.strip()[2:].strip()
            else:
                if current_heading or blocks:
                    sections.append((current_heading, blocks))
                current_heading = line.strip()[2:].strip()
                blocks = []
        elif line.strip().startswith("## ") or line.strip().startswith("### "):
            flush_table()
            h = line.strip().lstrip("#").strip()
            if current_heading or blocks:
                sections.append((current_heading, blocks))
            current_heading = h
            blocks = []
        elif "|" in line and line.strip().startswith("|"):
            table_acc.append(line)
        else:
            flush_table()
            if line.strip():
                blocks.append(("p", line.strip()))
    flush_table()
    if current_heading or blocks:
        sections.append((current_heading, blocks))
    if not title and sections:
        title = sections[0][0] or "Informe"
    if not sections:
        sections = [("", [("p", text.strip())])]
    return title, sections


def to_excel(title, sections, out_path):
    try:
        from openpyxl import Workbook
        from openpyxl.styles import Font, PatternFill, Alignment
        from openpyxl.utils import get_column_letter
    except ImportError:
        print("ERROR: falta openpyxl. Instala con: pip install openpyxl")
        return False

    wb = Workbook()
    # Portada
    ws = wb.active
    ws.title = "Portada"
    ws["A1"] = title
    ws["A1"].font = Font(size=16, bold=True)
    ws["A3"] = "Generado automáticamente por el Cuerpo Técnico."
    ws["A3"].font = Font(italic=True, size=10)

    used_names = {"Portada"}
    for heading, blocks in sections:
        name = (heading or "Seccion").strip()[:28] or "Seccion"
        # limpiar caracteres no válidos en nombres de hoja
        name = re.sub(r"[\\/*?\[\]:]", "", name)
        base = name
        i = 2
        while name in used_names:
            name = f"{base[:25]}_{i}"
            i += 1
        used_names.add(name)
        wsh = wb.create_sheet(title=name)
        r = 1
        if heading:
            wsh.cell(row=r, column=1, value=heading).font = Font(bold=True, size=12)
            r += 2
        for kind, payload in blocks:
            if kind == "p":
                wsh.cell(row=r, column=1, value=payload).alignment = Alignment(wrap_text=True)
                r += 1
            elif kind == "table":
                for row_idx, row in enumerate(payload):
                    for col_idx, cell in enumerate(row, start=1):
                        c = wsh.cell(row=r, column=col_idx, value=cell)
                        if row_idx == 0:
                            c.font = Font(bold=True)
                            c.fill = PatternFill("solid", fgColor="D9E2F3")
                        c.alignment = Alignment(wrap_text=True, vertical="top")
                    r += 1
                r += 1
        # ancho de columnas
        for col in range(1, 12):
            wsh.column_dimensions[get_column_letter(col)].width = 22

    wb.save(out_path)
    print(f"  Excel guardado: {out_path}")
    return True


def to_pdf(title, sections, out_path):
    try:
        from reportlab.lib import colors
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
    except ImportError:
        print("ERROR: falta reportlab. Instala con: pip install reportlab")
        return False

    doc = SimpleDocTemplate(out_path, pagesize=A4,
                            leftMargin=40, rightMargin=40, topMargin=50, bottomMargin=50)
    styles = getSampleStyleSheet()
    story = []
    story.append(Paragraph(title, styles["Title"]))
    story.append(Spacer(1, 12))

    for heading, blocks in sections:
        if heading:
            story.append(Paragraph(heading, styles["Heading2"]))
            story.append(Spacer(1, 6))
        for kind, payload in blocks:
            if kind == "p":
                story.append(Paragraph(payload, styles["BodyText"]))
                story.append(Spacer(1, 4))
            elif kind == "table":
                data = payload
                t = Table(data, repeatRows=1)
                t.setStyle(TableStyle([
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#D9E2F3")),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("GRID", (0, 0), (-1, -1), 0.4, colors.grey),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("FONTSIZE", (0, 0), (-1, -1), 9),
                ]))
                story.append(t)
                story.append(Spacer(1, 8))
    doc.build(story)
    print(f"  PDF guardado: {out_path}")
    return True


def main():
    parser = argparse.ArgumentParser(description="Convierte un informe Markdown a Excel/PDF.")
    parser.add_argument("input", help="Fichero Markdown de entrada")
    parser.add_argument("--format", nargs="+", choices=["xlsx", "pdf"], default=["xlsx", "pdf"],
                        help="Formatos de salida (por defecto ambos)")
    parser.add_argument("--out", default=None, help="Carpeta de salida (por defecto, junto al .md)")
    args = parser.parse_args()

    if not os.path.isfile(args.input):
        print(f"ERROR: no existe el fichero {args.input}")
        sys.exit(1)

    with open(args.input, encoding="utf-8") as f:
        text = f.read()

    title, sections = parse_markdown(text)
    base = os.path.splitext(os.path.basename(args.input))[0]
    out_dir = args.out or os.path.dirname(os.path.abspath(args.input)) or "."
    os.makedirs(out_dir, exist_ok=True)

    print(f"Informe: {title}")
    for fmt in args.format:
        out_path = os.path.join(out_dir, base + "." + fmt)
        if fmt == "xlsx":
            to_excel(title, sections, out_path)
        elif fmt == "pdf":
            to_pdf(title, sections, out_path)


if __name__ == "__main__":
    main()