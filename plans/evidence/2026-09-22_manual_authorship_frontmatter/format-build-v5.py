"""Source-derived v5 Word build; it preserves the reviewed v4 package."""
from copy import deepcopy
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
from lxml import etree as ET
import hashlib
import json
import re

ROOT = Path('/Users/ryan/.codex/worktrees/da43/chirality')
DOCS = ROOT / 'docs/alignment-manual'
EVIDENCE = ROOT / 'plans/evidence/2026-09-22_manual_authorship_frontmatter'
BASE_MD = DOCS / 'Project_Management_for_Human_Agent_Teams_Consolidated_v4.md'
BASE_DOCX = DOCS / 'Project_Management_for_Human_Agent_Teams_Consolidated_v4.docx'
SOURCE_AUTH = Path('/Users/ryan/Downloads/PM_Manual_Authorship_and_Preparation_v1.md')
MD = DOCS / 'Project_Management_for_Human_Agent_Teams_Consolidated_v5.md'
OUT = DOCS / 'Project_Management_for_Human_Agent_Teams_Consolidated_v5.docx'

EXPECTED = {
    BASE_MD: '2d9638c50a948623e7b94e7544308c1bd411765e679873a6911cdf09a8e37ca6',
    BASE_DOCX: '084fe225407be696e8a525c48315bd7725031d6c18decdc9ed21713c66b80f36',
    SOURCE_AUTH: '902ef23039a2d67d3c780a691a7797e6e169fc1d2af70c05f74c542e0c82f16b',
    MD: 'e7f8579110e95f57c618bec304462dc04419b6f48bada9a296404cf8b91f609d',
}
for path, expected in EXPECTED.items():
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    assert actual == expected, (path, actual, expected)
assert not OUT.exists(), OUT

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
NS = {'w': W}
def q(name): return '{' + W + '}' + name

source_md = MD.read_text()
auth_start = source_md.index('<a id="h_authorship"></a>')
contents_start = source_md.index('\n## Contents', auth_start)
auth_md = source_md[auth_start:contents_start]
lines = auth_md.splitlines()
blocks = []
for line in lines:
    line = line.strip()
    if not line or line.startswith('<a id='):
        continue
    if line.startswith('#'):
        blocks.append(('heading', len(line) - len(line.lstrip('#')), re.sub(r'^#+\s*', '', line)))
    else:
        blocks.append(('paragraph', 0, line))
assert blocks[0] == ('heading', 1, 'Authorship and preparation of this manual')
assert sum(1 for kind, _, text in blocks if kind == 'heading' and text.startswith('Basis of this account')) == 1

source_zip = ZipFile(BASE_DOCX)
members = {item.filename: source_zip.read(item.filename) for item in source_zip.infolist()}
root = ET.fromstring(members['word/document.xml'])
body = root.find('w:body', NS)
direct = list(body)
def paragraph_text(element):
    return ''.join(element.xpath('.//w:t/text()', namespaces=NS))

contents_heading = next(p for p in direct if p.tag == q('p') and paragraph_text(p) == 'Contents')
preface_heading = next(p for p in direct if p.tag == q('p') and paragraph_text(p) == 'Preface')
assert contents_heading.find('w:pPr/w:pStyle[@w:val="Heading1"]', NS) is not None
assert preface_heading.find('w:pPr/w:pStyle[@w:val="Heading1"]', NS) is not None
contents_index = direct.index(contents_heading)
preface_index = direct.index(preface_heading)
assert contents_index < preface_index

old_toc = root.xpath('//w:body/w:p[w:pPr/w:pStyle[@w:val="PMContents" or @w:val="PMContentsChapter"]]', namespaces=NS)
assert len(old_toc) == 88
preface_toc = next(p for p in old_toc if paragraph_text(p).startswith('Preface'))
preface_link = next(h for h in preface_toc.xpath('./w:hyperlink', namespaces=NS)
                    if h.get(q('anchor')) == 'h_preface')
assert preface_link is not None
toc_sample = deepcopy(preface_toc)
toc_style = toc_sample.find('w:pPr/w:pStyle', NS).get(q('val'))

body_sample = deepcopy(next(p for p in direct if p.tag == q('p') and
                            paragraph_text(p).startswith('This manual concerns')))
heading1_sample = deepcopy(preface_heading)
heading2_sample = deepcopy(next(p for p in direct if p.tag == q('p') and
                                p.find('w:pPr/w:pStyle[@w:val="Heading2"]', NS) is not None))

def add_run(parent, text, *, bold=False, italic=False, code=False):
    if not text:
        return
    run = ET.SubElement(parent, q('r'))
    props = ET.SubElement(run, q('rPr'))
    if bold: ET.SubElement(props, q('b'))
    if italic: ET.SubElement(props, q('i'))
    if code:
        fonts = ET.SubElement(props, q('rFonts'))
        fonts.set(q('ascii'), 'Liberation Mono')
        fonts.set(q('hAnsi'), 'Liberation Mono')
    node = ET.SubElement(run, q('t'))
    node.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    node.text = text

TOKEN = re.compile(r'(`[^`]+`|\*\*.+?\*\*|\*[^*]+\*)')
def fill_paragraph(paragraph, text):
    ppr = paragraph.find('w:pPr', NS)
    for child in list(paragraph):
        if child is not ppr:
            paragraph.remove(child)
    for token in TOKEN.split(text):
        if not token:
            continue
        if token.startswith('**') and token.endswith('**'):
            add_run(paragraph, token[2:-2], bold=True)
        elif token.startswith('*') and token.endswith('*'):
            add_run(paragraph, token[1:-1], italic=True)
        elif token.startswith('`') and token.endswith('`'):
            add_run(paragraph, token[1:-1], code=True)
        else:
            add_run(paragraph, token)
    return paragraph

def source_paragraph(text):
    para = deepcopy(body_sample)
    ppr = para.find('w:pPr', NS)
    for child in list(para):
        if child is not ppr:
            para.remove(child)
    if re.match(r'^\[A[1-5]\]', text):
        label = re.match(r'^\[A[1-5]\]', text)[0]
        add_run(para, label, bold=True)
        for token in TOKEN.split(text[len(label):]):
            if not token:
                continue
            if token.startswith('**') and token.endswith('**'):
                add_run(para, token[2:-2], bold=True)
            elif token.startswith('*') and token.endswith('*'):
                add_run(para, token[1:-1], italic=True)
            elif token.startswith('`') and token.endswith('`'):
                add_run(para, token[1:-1], code=True)
            else:
                add_run(para, token)
    else:
        fill_paragraph(para, text)
    return para

def heading_paragraph(text, level):
    sample = heading1_sample if level == 1 else heading2_sample
    para = deepcopy(sample)
    for mark in para.xpath('.//w:bookmarkStart|.//w:bookmarkEnd', namespaces=NS):
        mark.getparent().remove(mark)
    style = para.find('w:pPr/w:pStyle', NS)
    style.set(q('val'), 'Heading' + str(level))
    fill_paragraph(para, text)
    return para

new_body = []
heading_para = None
for kind, level, text in blocks:
    if kind == 'heading':
        para = heading_paragraph(text, level)
        if level == 1:
            heading_para = para
    else:
        para = source_paragraph(text)
    new_body.append(para)
assert heading_para is not None

# Give the new section a short, stable Word bookmark matching the Markdown anchor.
bookmark_ids = [int(b.get(q('id'))) for b in root.xpath('//w:bookmarkStart', namespaces=NS)
                if b.get(q('id'), '').isdigit()]
bookmark_id = max(bookmark_ids, default=0) + 1
bookmark_start = ET.Element(q('bookmarkStart'))
bookmark_start.set(q('id'), str(bookmark_id))
bookmark_start.set(q('name'), 'h_authorship')
bookmark_end = ET.Element(q('bookmarkEnd'))
bookmark_end.set(q('id'), str(bookmark_id))
ppr = heading_para.find('w:pPr', NS)
heading_para.insert(list(heading_para).index(ppr) + 1 if ppr is not None else 0, bookmark_start)
heading_para.append(bookmark_end)

# Insert the article into the Roman-numbered section following the original cover.
for offset, paragraph in enumerate(new_body):
    body.insert(contents_index + offset, paragraph)

# Begin the Contents on a fresh page after the article while keeping both in front matter.
contents_ppr = contents_heading.find('w:pPr', NS)
if contents_ppr is None:
    contents_ppr = ET.Element(q('pPr'))
    contents_heading.insert(0, contents_ppr)
if contents_ppr.find('w:pageBreakBefore', NS) is None:
    ET.SubElement(contents_ppr, q('pageBreakBefore'))

# Add an Authorshi​p entry to the existing static, dotted-leader Contents.
new_toc = deepcopy(toc_sample)
new_toc_ppr = new_toc.find('w:pPr', NS)
for child in list(new_toc):
    if child is not new_toc_ppr:
        new_toc.remove(child)
hyperlink = ET.SubElement(new_toc, q('hyperlink'))
hyperlink.set(q('anchor'), 'h_authorship')
add_run(hyperlink, 'Authorship and preparation of this manual')
tabrun = ET.SubElement(new_toc, q('r'))
tab = ET.SubElement(tabrun, q('tab'))
folio_run = ET.SubElement(new_toc, q('r'))
folio_text = ET.SubElement(folio_run, q('t'))
folio_text.text = 'i'
body.insert(body.index(preface_toc), new_toc)

# Split front matter from the body: Roman folios through Contents, Arabic 1 at Preface.
final_sect = body.find('w:sectPr', NS)
assert final_sect is not None
roman_sect = deepcopy(final_sect)
sect_type = roman_sect.find('w:type', NS)
if sect_type is None:
    sect_type = ET.Element(q('type'))
    roman_sect.insert(0, sect_type)
sect_type.set(q('val'), 'nextPage')
page_numbers = roman_sect.find('w:pgNumType', NS)
if page_numbers is None:
    page_numbers = ET.SubElement(roman_sect, q('pgNumType'))
page_numbers.set(q('fmt'), 'lowerRoman')
page_numbers.set(q('start'), '1')
last_toc = root.xpath('//w:body/w:p[w:pPr/w:pStyle[@w:val="PMContents" or @w:val="PMContentsChapter"]]', namespaces=NS)[-1]
last_ppr = last_toc.find('w:pPr', NS)
assert last_ppr is not None
assert last_ppr.find('w:sectPr', NS) is None
last_ppr.append(roman_sect)

# The trailing body section deliberately restarts in Arabic numerals at the Preface.
body_sect_pn = final_sect.find('w:pgNumType', NS)
if body_sect_pn is None:
    body_sect_pn = ET.SubElement(final_sect, q('pgNumType'))
body_sect_pn.set(q('fmt'), 'decimal')
body_sect_pn.set(q('start'), '1')

bookmarks = root.xpath('//w:bookmarkStart', namespaces=NS)
names = [b.get(q('name')) for b in bookmarks]
assert len(names) == len(set(names))
assert 'h_authorship' in names
assert len(root.xpath('//w:p[w:pPr/w:pStyle[@w:val="PMContents" or @w:val="PMContentsChapter"]]', namespaces=NS)) == 89
assert len(root.xpath('//w:body/w:sectPr|//w:body/w:p/w:pPr/w:sectPr', namespaces=NS)) == 3

members['word/document.xml'] = ET.tostring(root, encoding='UTF-8', xml_declaration=True, standalone=True)
with ZipFile(OUT, 'w', ZIP_DEFLATED) as dest:
    for item in source_zip.infolist():
        dest.writestr(item, members[item.filename])
source_zip.close()
print(json.dumps({'output': str(OUT), 'toc_entries': 89, 'body_sections': 3,
                  'roman_section_folio': 'i', 'preface_section_folio': '1',
                  'new_bookmark': 'h_authorship', 'paragraphs_added': len(new_body),
                  'sha256': hashlib.sha256(OUT.read_bytes()).hexdigest()}, indent=2))
