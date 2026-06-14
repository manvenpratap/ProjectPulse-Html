"""
docx_helpers.py
===============
Shared styling primitives, brand palette, and layout helpers used by all
three ProjectPulse document builders (build_pcd / build_fsd / build_umi).
"""

import os, glob, datetime
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# ── Paths ──────────────────────────────────────────────────────────────────
BASE_DIR  = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SS_DIR    = os.path.join(BASE_DIR, "docs", "screenshots")
DOCS_DIR  = os.path.join(BASE_DIR, "docs")

# ── Brand Palette ──────────────────────────────────────────────────────────
CLR_NAVY    = RGBColor(0x0D, 0x1B, 0x2A)
CLR_TEAL    = RGBColor(0x00, 0xC2, 0xA8)
CLR_ACCENT  = RGBColor(0x1E, 0x9E, 0xD5)
CLR_WHITE   = RGBColor(0xFF, 0xFF, 0xFF)
CLR_LIGHT   = RGBColor(0xF4, 0xF7, 0xFA)
CLR_DARK    = RGBColor(0x1A, 0x1A, 0x2E)
CLR_WARN    = RGBColor(0xE6, 0x7E, 0x22)
CLR_DANGER  = RGBColor(0xC0, 0x39, 0x2B)
CLR_SUCCESS = RGBColor(0x27, 0xAE, 0x60)
CLR_TEXT    = RGBColor(0x1C, 0x1C, 0x1E)
CLR_MUTED   = RGBColor(0x6C, 0x75, 0x7D)
CLR_BORDER  = RGBColor(0xD1, 0xD5, 0xDB)
CLR_PURPLE  = RGBColor(0x6C, 0x3F, 0xC2)
CLR_GOLD    = RGBColor(0xD4, 0xAF, 0x37)

# ── Document Setup ─────────────────────────────────────────────────────────

def new_document(top=1.0, bottom=1.0, left=1.1, right=1.1):
    doc = Document()
    section = doc.sections[0]
    section.top_margin    = Inches(top)
    section.bottom_margin = Inches(bottom)
    section.left_margin   = Inches(left)
    section.right_margin  = Inches(right)
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(10.5)
    style.font.color.rgb = CLR_TEXT
    for level, size in [(1,18),(2,13.5),(3,11.5)]:
        h = doc.styles[f"Heading {level}"]
        h.font.name = "Calibri"
        h.font.size = Pt(size)
        h.font.color.rgb = CLR_NAVY
        h.font.bold = True
    return doc

# ── Cell / Table Helpers ───────────────────────────────────────────────────

def set_cell_bg(cell, hex_color):
    tc   = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd  = OxmlElement("w:shd")
    shd.set(qn("w:val"),   "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"),  hex_color)
    tcPr.append(shd)


def add_horizontal_rule(doc, color="D1D5DB"):
    p   = doc.add_paragraph()
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bot  = OxmlElement("w:bottom")
    bot.set(qn("w:val"),   "single")
    bot.set(qn("w:sz"),    "6")
    bot.set(qn("w:space"), "1")
    bot.set(qn("w:color"), color)
    pBdr.append(bot)
    pPr.append(pBdr)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after  = Pt(6)
    return p


def add_page_break(doc):
    doc.add_page_break()

# ── Typography ─────────────────────────────────────────────────────────────

def make_heading(doc, text, level=1, color=None, space_before=18, space_after=6):
    h   = doc.add_heading(text, level=level)
    h.paragraph_format.space_before = Pt(space_before)
    h.paragraph_format.space_after  = Pt(space_after)
    run = h.runs[0] if h.runs else h.add_run(text)
    if color: run.font.color.rgb = color
    return h


def make_body(doc, text, space_before=0, space_after=6, color=None,
              bold=False, italic=False, size=10.5):
    p   = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after  = Pt(space_after)
    run = p.add_run(text)
    run.font.size = Pt(size)
    if color:  run.font.color.rgb = color
    if bold:   run.bold  = True
    if italic: run.italic = True
    return p


def make_bullet(doc, text, level=0, space_after=3):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after  = Pt(space_after)
    p.paragraph_format.left_indent  = Inches(0.25 + level * 0.25)
    run = p.add_run(text)
    run.font.size = Pt(10.5)
    return p


def make_numbered(doc, text, level=0, space_after=3):
    p = doc.add_paragraph(style="List Number")
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after  = Pt(space_after)
    run = p.add_run(text)
    run.font.size = Pt(10.5)
    return p


def make_formula(doc, text, space_before=6, space_after=8):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after  = Pt(space_after)
    p.paragraph_format.left_indent  = Inches(0.4)
    run = p.add_run(text)
    run.font.size = Pt(10.5)
    run.font.name = "Courier New"
    run.font.bold = True
    run.font.color.rgb = CLR_ACCENT
    return p


def make_code(doc, text, space_before=4, space_after=8):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after  = Pt(space_after)
    p.paragraph_format.left_indent  = Inches(0.3)
    run = p.add_run(text)
    run.font.size = Pt(9.5)
    run.font.name = "Courier New"
    run.font.color.rgb = CLR_DARK
    return p

# ── Callout Boxes ──────────────────────────────────────────────────────────

def add_callout(doc, text, style="note"):
    configs = {
        "note":        ("INFO",         "0D4F8B", "E8F4FD", "1565C0"),
        "tip":         ("TIP",          "145A32", "E9F7EF", "1E8449"),
        "warning":     ("WARNING",      "7D4E00", "FEF9E7", "C67C00"),
        "caution":     ("CAUTION",      "6E2222", "FDEDEC", "C0392B"),
        "rule":        ("BUSINESS RULE","1A237E", "EDE7F6", "5E35B1"),
        "constraint":  ("CONSTRAINT",   "1B5E20", "E8F5E9", "2E7D32"),
        "integration": ("INTEGRATION",  "01579B", "E1F5FE", "0277BD"),
    }
    label, label_col, bg_col, border_col = configs.get(style, configs["note"])

    tbl  = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.style     = "Table Grid"
    cell = tbl.cell(0, 0)
    set_cell_bg(cell, bg_col)

    tc   = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = OxmlElement("w:tcBorders")
    for edge, col, sz in [("left",border_col,18),("top","FFFFFF",4),
                           ("right","FFFFFF",4),("bottom","FFFFFF",4)]:
        tag = OxmlElement(f"w:{edge}")
        tag.set(qn("w:val"),   "single")
        tag.set(qn("w:sz"),    str(sz))
        tag.set(qn("w:color"), col)
        tcBorders.append(tag)
    tcPr.append(tcBorders)

    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after  = Pt(2)
    p.paragraph_format.left_indent  = Inches(0.1)
    lbl = p.add_run(f"[{label}]  ")
    lbl.bold = True
    lbl.font.size = Pt(9)
    lbl.font.color.rgb = RGBColor.from_string(label_col)

    p2 = cell.add_paragraph()
    p2.paragraph_format.space_before = Pt(2)
    p2.paragraph_format.space_after  = Pt(6)
    p2.paragraph_format.left_indent  = Inches(0.1)
    body = p2.add_run(text)
    body.font.size = Pt(10)
    doc.add_paragraph()
    return tbl

# ── Data Tables ────────────────────────────────────────────────────────────

def add_data_table(doc, headers, rows, col_widths=None,
                   header_bg="0D1B2A", header_fg="FFFFFF"):
    tbl = doc.add_table(rows=1+len(rows), cols=len(headers))
    tbl.style     = "Table Grid"
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr_cells = tbl.rows[0].cells
    for i, h in enumerate(headers):
        hdr_cells[i].text = h
        set_cell_bg(hdr_cells[i], header_bg)
        p   = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.runs[0]
        run.bold = True
        run.font.size = Pt(9.5)
        run.font.color.rgb = RGBColor.from_string(header_fg)
    for r_idx, row in enumerate(rows):
        cells = tbl.rows[r_idx+1].cells
        bg    = "F8F9FA" if r_idx % 2 == 0 else "FFFFFF"
        for c_idx, val in enumerate(row):
            cells[c_idx].text = str(val)
            set_cell_bg(cells[c_idx], bg)
            p = cells[c_idx].paragraphs[0]
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after  = Pt(3)
            if p.runs: p.runs[0].font.size  = Pt(9.5)
    if col_widths:
        for i, w in enumerate(col_widths):
            for row in tbl.rows:
                row.cells[i].width = Inches(w)
    doc.add_paragraph().paragraph_format.space_after = Pt(6)
    return tbl


def add_transition_table(doc, rows):
    return add_data_table(
        doc,
        ["From Status","To Status","Guard / Condition","Required Effect"],
        rows, col_widths=[1.5,1.5,2.2,1.4], header_bg="1A1A2E")


def add_schema_table(doc, rows):
    return add_data_table(
        doc,
        ["Field","Type","Constraint","Default","Description"],
        rows, col_widths=[1.4,0.8,1.1,0.8,2.5], header_bg="0D1B2A")

# ── Screenshot Embedding ───────────────────────────────────────────────────

def add_screenshot(doc, filename, caption, width_inches=6.3):
    candidates = [os.path.join(SS_DIR, filename),
                  os.path.join(SS_DIR, filename+".png")]
    path = None
    for c in candidates:
        if os.path.exists(c): path = c; break
    if not path:
        matches = glob.glob(os.path.join(SS_DIR, f"{filename}*"))
        if matches: path = sorted(matches)[0]

    if path and os.path.exists(path):
        p_img = doc.add_paragraph()
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after  = Pt(0)
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.add_run().add_picture(path, width=Inches(width_inches))
    else:
        p_img = doc.add_paragraph(f"[Screenshot: {filename}]")
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.runs[0].font.color.rgb = CLR_MUTED
        p_img.runs[0].font.italic    = True

    cap = doc.add_paragraph()
    cap.paragraph_format.space_before = Pt(4)
    cap.paragraph_format.space_after  = Pt(14)
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = cap.add_run(caption)
    run.font.size   = Pt(9)
    run.font.italic = True
    run.font.color.rgb = CLR_MUTED
    return p_img

# ── Cover Page ─────────────────────────────────────────────────────────────

def build_cover(doc, product_name, subtitle, doc_type, version,
                audience, confidentiality):
    doc.add_paragraph("\n\n\n")
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title_p.add_run(product_name)
    run.bold = True; run.font.size = Pt(44); run.font.color.rgb = CLR_NAVY

    sub_p = doc.add_paragraph()
    sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = sub_p.add_run(subtitle)
    run.font.size = Pt(20); run.font.color.rgb = CLR_TEAL

    doc.add_paragraph("\n")
    hr = doc.add_paragraph()
    hr.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = hr.add_run(u"\u2500"*60)
    run.font.color.rgb = CLR_TEAL; run.font.size = Pt(12)
    doc.add_paragraph("\n")

    meta = [("Document Type",doc_type),("Version",version),
            ("Audience",audience),
            ("Date",datetime.date.today().strftime("%d %B %Y")),
            ("Confidentiality",confidentiality)]
    tbl = doc.add_table(rows=len(meta), cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i,(label,value) in enumerate(meta):
        c0,c1 = tbl.rows[i].cells
        set_cell_bg(c0,"0D1B2A"); set_cell_bg(c1,"F4F7FA")
        c0.width = Inches(2.0); c1.width = Inches(3.5)
        p0 = c0.paragraphs[0]; p0.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r0 = p0.add_run(label)
        r0.bold=True; r0.font.size=Pt(9.5); r0.font.color.rgb=CLR_WHITE
        p1 = c1.paragraphs[0]
        r1 = p1.add_run(value)
        r1.font.size=Pt(9.5); r1.font.color.rgb=CLR_TEXT
    add_page_break(doc)

# ── Table of Contents ──────────────────────────────────────────────────────

def build_toc(doc, chapters, title="Table of Contents"):
    make_heading(doc, title, level=1, color=CLR_NAVY)
    add_horizontal_rule(doc, "00C2A8")
    tbl = doc.add_table(rows=len(chapters), cols=3)
    tbl.alignment = WD_TABLE_ALIGNMENT.LEFT
    for i,(num,title_text,pg) in enumerate(chapters):
        c0,c1,c2 = tbl.rows[i].cells
        c0.width=Inches(0.5); c1.width=Inches(5.3); c2.width=Inches(0.6)
        bg = "F4F7FA" if i%2==0 else "FFFFFF"
        for cell in (c0,c1,c2): set_cell_bg(cell,bg)
        r0 = c0.paragraphs[0].add_run(num)
        r0.bold=True; r0.font.size=Pt(10); r0.font.color.rgb=CLR_TEAL
        r1 = c1.paragraphs[0].add_run(title_text)
        r1.font.size=Pt(10.5)
        p2 = c2.paragraphs[0]; p2.alignment=WD_ALIGN_PARAGRAPH.RIGHT
        r2 = p2.add_run(pg)
        r2.font.size=Pt(10); r2.font.color.rgb=CLR_MUTED
    add_page_break(doc)

# ── Section Divider ────────────────────────────────────────────────────────

def add_section_divider(doc, part_label, part_title, description=""):
    add_page_break(doc)
    doc.add_paragraph("\n\n\n\n")
    lbl_p = doc.add_paragraph()
    lbl_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = lbl_p.add_run(part_label)
    run.font.size=Pt(13); run.font.color.rgb=CLR_TEAL; run.font.bold=True

    t_p = doc.add_paragraph()
    t_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = t_p.add_run(part_title)
    run.font.size=Pt(32); run.font.color.rgb=CLR_NAVY; run.font.bold=True

    hr = doc.add_paragraph()
    hr.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = hr.add_run(u"\u2500"*40)
    run.font.color.rgb=CLR_TEAL; run.font.size=Pt(14)

    if description:
        doc.add_paragraph("\n")
        d_p = doc.add_paragraph()
        d_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = d_p.add_run(description)
        run.font.size=Pt(12); run.font.color.rgb=CLR_MUTED; run.font.italic=True
    add_page_break(doc)

# ── Document Control (FSD) ─────────────────────────────────────────────────

def add_document_control(doc, version="v2.1.0", status="Approved",
                          authors="ProjectPulse Product Team",
                          reviewers="Engineering Lead / QA Lead / Product Manager"):
    make_heading(doc,"Document Control",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    add_data_table(doc,["Field","Value"],[
        ["Document Title",  "ProjectPulse - Functional Specification Document"],
        ["Version",         version],
        ["Status",          status],
        ["Author(s)",       authors],
        ["Reviewer(s)",     reviewers],
        ["Review Date",     datetime.date.today().strftime("%d %B %Y")],
        ["Classification",  "Internal - Restricted"],
        ["Next Review",     "Quarterly or upon major feature release"],
    ], col_widths=[2.0,4.4])
    add_page_break(doc)

# ── Footer ─────────────────────────────────────────────────────────────────

def add_footer(doc, doc_title):
    section = doc.sections[0]
    footer  = section.footer
    footer.is_linked_to_previous = False
    para = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
    para.clear()
    para.paragraph_format.space_before = Pt(6)
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = para.add_run(f"ProjectPulse  |  {doc_title}  |  Page ")
    run.font.size = Pt(8); run.font.color.rgb = CLR_MUTED
    fldChar1 = OxmlElement("w:fldChar"); fldChar1.set(qn("w:fldCharType"),"begin")
    instrText = OxmlElement("w:instrText"); instrText.text = "PAGE"
    fldChar2 = OxmlElement("w:fldChar"); fldChar2.set(qn("w:fldCharType"),"end")
    run2 = para.add_run()
    run2.font.size=Pt(8); run2.font.color.rgb=CLR_MUTED
    run2._r.append(fldChar1); run2._r.append(instrText); run2._r.append(fldChar2)
