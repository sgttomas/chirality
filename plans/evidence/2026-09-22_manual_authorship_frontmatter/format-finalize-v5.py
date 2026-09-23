"""Update static Contents folios and Word summary fields from the final render."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
from lxml import etree as ET
from pypdf import PdfReader
import hashlib
import json
import re
import sys

ROOT = Path('/Users/ryan/.codex/worktrees/da43/chirality')
DOCS = ROOT / 'docs/alignment-manual'
EVIDENCE = ROOT / 'plans/evidence/2026-09-22_manual_authorship_frontmatter'
DOCX = DOCS / 'Project_Management_for_Human_Agent_Teams_Consolidated_v5.docx'
MD = DOCS / 'Project_Management_for_Human_Agent_Teams_Consolidated_v5.md'
PDF = Path(sys.argv[1])
EXPECTED_MD = 'e7f8579110e95f57c618bec304462dc04419b6f48bada9a296404cf8b91f609d'
assert hashlib.sha256(MD.read_bytes()).hexdigest() == EXPECTED_MD
reader = PdfReader(PDF)
assert len(reader.pages) == 165, len(reader.pages)

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
NS = {'w': W}
def q(name): return '{' + W + '}' + name

z = ZipFile(DOCX)
parts = {item.filename: z.read(item.filename) for item in z.infolist()}
root = ET.fromstring(parts['word/document.xml'])
entries = root.xpath('//w:body/w:p[w:pPr/w:pStyle[@w:val="PMContents" or @w:val="PMContentsChapter"]]', namespaces=NS)
assert len(entries) == 89, len(entries)
annotations = []
seen = set()
for page in reader.pages[1:]:
    links = [item.get_object() for item in page.get('/Annots', [])]
    links.sort(key=lambda item: -float(item['/Rect'][3]))
    for item in links:
        dest = item.get('/Dest')
        if not dest:
            continue
        key = str(dest)
        if key not in seen:
            seen.add(key)
            annotations.append(item)
    if len(annotations) >= len(entries):
        break
assert len(annotations) == len(entries), (len(annotations), len(entries))

folio_pattern = re.compile(r'^PROJECT MANAGEMENT\s+((?:[ivxlcdm]+)|\d+)\s*$', re.I | re.M)
maps = []
for paragraph, annotation in zip(entries, annotations):
    dest = annotation['/Dest']
    physical = reader.get_page_number(dest[0].get_object()) + 1
    text = reader.pages[physical - 1].extract_text() or ''
    match = folio_pattern.search(text)
    assert match, (physical, text[:400])
    folio = match[1]
    page_text = paragraph.xpath('./w:r/w:t', namespaces=NS)
    assert len(page_text) == 1, ET.tostring(paragraph, encoding='unicode')
    page_text[0].text = folio
    links = paragraph.xpath('./w:hyperlink[@w:anchor]', namespaces=NS)
    assert len(links) == 1
    maps.append({'anchor': links[0].get(q('anchor')), 'physical_page': physical, 'printed_folio': folio})

# Store the rendered state in standard Word document properties without touching body formatting.
app = ET.fromstring(parts['docProps/app.xml'])
app_ns = ET.QName(app).namespace
def app_tag(name): return '{' + app_ns + '}' + name
body_text = ' '.join(root.xpath('//w:t/text()', namespaces=NS))
values = {
    'Pages': str(len(reader.pages)),
    'Words': str(len(body_text.split())),
    'Characters': str(len(re.sub(r'\s', '', body_text))),
    'CharactersWithSpaces': str(len(body_text)),
    'Paragraphs': str(len(root.xpath('//w:p', namespaces=NS))),
    'Application': 'Codex',
}
for name, value in values.items():
    element = app.find(app_tag(name))
    if element is not None:
        element.text = value
for name in ['AppVersion', 'Lines']:
    element = app.find(app_tag(name))
    if element is not None:
        app.remove(element)

parts['word/document.xml'] = ET.tostring(root, encoding='UTF-8', xml_declaration=True, standalone=True)
parts['docProps/app.xml'] = ET.tostring(app, encoding='UTF-8', xml_declaration=True, standalone=True)
z.close()
with ZipFile(DOCX, 'w', ZIP_DEFLATED) as dest:
    for name, data in parts.items():
        dest.writestr(name, data)

toc_map = {'render_pdf_sha256': hashlib.sha256(PDF.read_bytes()).hexdigest(), 'pages': len(reader.pages),
           'frontmatter_folio_pattern': 'lowercase Roman, beginning at i',
           'body_folio_pattern': 'Arabic, restarting at Preface 1', 'entries': maps, 'word_properties': values}
(EVIDENCE / 'toc-map-v5.json').write_text(json.dumps(toc_map, indent=2) + '\n')
print(json.dumps({'toc_entries_updated': len(maps), 'page_count': len(reader.pages),
                  'roman_frontmatter': [m['printed_folio'] for m in maps if m['printed_folio'].isalpha() and m['printed_folio'].islower()][:5],
                  'preface_folio': next(m['printed_folio'] for m in maps if m['anchor'] == 'h_preface'),
                  'docx_sha256': hashlib.sha256(DOCX.read_bytes()).hexdigest()}, indent=2))
