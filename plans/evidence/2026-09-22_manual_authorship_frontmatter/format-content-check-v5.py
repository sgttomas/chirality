"""Independent local parity checks for the v5 source, Word package, and render."""
from pathlib import Path
from zipfile import ZipFile
from lxml import etree as ET
from pypdf import PdfReader
import hashlib
import json
import re

ROOT = Path('/Users/ryan/.codex/worktrees/da43/chirality')
DOCS = ROOT / 'docs/alignment-manual'
EVIDENCE = ROOT / 'plans/evidence/2026-09-22_manual_authorship_frontmatter'
BASE = DOCS / 'Project_Management_for_Human_Agent_Teams_Consolidated_v4.md'
MD = DOCS / 'Project_Management_for_Human_Agent_Teams_Consolidated_v5.md'
DOCX = DOCS / 'Project_Management_for_Human_Agent_Teams_Consolidated_v5.docx'
PDF = Path('/tmp/manual-v5-authorship-20260922/final2/Project_Management_for_Human_Agent_Teams_Consolidated_v5.pdf')
REPO_PDF = DOCS / 'Project_Management_for_Human_Agent_Teams_Consolidated_v5.pdf'
README = DOCS / 'README.md'
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
NS = {'w': W}
def q(name): return '{' + W + '}' + name
def normalized(text):
    text = ' '.join(text.split())
    return re.sub(r'\s+([,.;:?!])', r'\1', text)

source = MD.read_text()
prior = BASE.read_text()
anchor = '<a id="h_authorship"></a>'
assert source.count(anchor) == 1
auth_start = source.index(anchor)
auth_end = source.index('\n## Contents', auth_start)
auth_lines = source[auth_start:auth_end].splitlines()
source_units = []
for line in auth_lines:
    line = line.strip()
    if not line or line.startswith('<a id='):
        continue
    if line.startswith('#'):
        line = re.sub(r'^#+\s*', '', line)
    line = line.replace('**', '').replace('*', '').replace('`', '')
    source_units.append(line)
assert source_units[0] == 'Authorship and preparation of this manual'
assert all(f'[A{i}]' in source for i in range(1, 6))
assert 'Acceptance of this new note remains outstanding.' not in source
assert 'Edition 2' not in source[auth_start:auth_end] and 'Edition 3' not in source[auth_start:auth_end]
assert source[source.index('<a id="h_preface"></a>'):] == prior[prior.index('<a id="h_preface"></a>'):]
anchors = set(re.findall(r'<a id="([^"]+)"', source))
for href in re.findall(r'\[[^\]]+\]\(([^)]+)\)', source):
    if href.startswith('#'):
        assert href[1:] in anchors, href
    elif href.startswith(('http://', 'https://')):
        continue
    else:
        assert (DOCS / href.split('#', 1)[0]).exists(), href
for name, digest in {
    'Project_Management_for_Human_Agent_Teams_Consolidated_v4.md': '2d9638c50a948623e7b94e7544308c1bd411765e679873a6911cdf09a8e37ca6',
    'Project_Management_for_Human_Agent_Teams_Consolidated_v4.docx': '084fe225407be696e8a525c48315bd7725031d6c18decdc9ed21713c66b80f36',
    'Project_Management_for_Human_Agent_Teams_Consolidated_v4.pdf': 'ae8585916f3eea365e112fb7b8fe6a72edfafe9a75dea312e029bf9f71164411',
}.items():
    assert hashlib.sha256((DOCS / name).read_bytes()).hexdigest() == digest
assert hashlib.sha256(REPO_PDF.read_bytes()).hexdigest() == hashlib.sha256(PDF.read_bytes()).hexdigest()
readme = README.read_text()
for name in ['Project_Management_for_Human_Agent_Teams_Consolidated_v5.md',
             'Project_Management_for_Human_Agent_Teams_Consolidated_v5.docx',
             'Project_Management_for_Human_Agent_Teams_Consolidated_v5.pdf',
             'Project_Management_for_Human_Agent_Teams_Consolidated_v4.md']:
    assert (DOCS / name).exists() and name in readme
    if name.endswith('.pdf'):
        assert (DOCS / name).stat().st_size > 0
with ZipFile(DOCX) as meta_zip:
    app = ET.fromstring(meta_zip.read('docProps/app.xml'))
    app_ns = ET.QName(app).namespace
    assert app.find('{' + app_ns + '}Pages').text == '165'
    core = ET.fromstring(meta_zip.read('docProps/core.xml'))
    core_ns = {'dc': 'http://purl.org/dc/elements/1.1/'}
    assert core.find('dc:creator', core_ns).text == 'Ryan Tufts'
    assert core.find('dc:title', core_ns).text == 'Project Management for Human–Agent Teams'
    assert not core.xpath('//*[local-name()="version" or local-name()="revision" or local-name()="description"]')
    media_hash = hashlib.sha256(meta_zip.read('word/media/image1.png')).hexdigest()
    assert media_hash == '0a1f2f1dbeeff97a6c0f9c6ae0aaa3263aa1360ae49c62751e673b6b2f6b71e1'
    assert not any('comments.xml' in n for n in meta_zip.namelist())
    doc_parts = ET.fromstring(meta_zip.read('word/document.xml'))
    assert not doc_parts.xpath('//w:ins|//w:del|//w:moveFrom|//w:moveTo', namespaces=NS)
    rels = ET.fromstring(meta_zip.read('word/_rels/document.xml.rels'))
    link_targets = [r.get('Target') for r in rels if r.get('Type', '').endswith('/hyperlink')]
    assert 'CHIRALITY_AGENT_USER_MANUAL_v2.md' in link_targets
    assert all(t.startswith(('https://', 'http://')) or t == 'CHIRALITY_AGENT_USER_MANUAL_v2.md' for t in link_targets)
    cover_text = ' '.join(PdfReader(PDF).pages[0].extract_text().split()).upper()
    assert 'EDITION' not in cover_text and 'DRAFT' not in cover_text and 'CHATGPT' not in cover_text

zip_file = ZipFile(DOCX)
document = ET.fromstring(zip_file.read('word/document.xml'))
all_paragraphs = document.xpath('//w:body/w:p', namespaces=NS)
body_text = [p for p in all_paragraphs]
paragraph_text = lambda p: ''.join(p.xpath('.//w:t/text()', namespaces=NS))
start = next(i for i,p in enumerate(body_text) if p.xpath('./w:bookmarkStart[@w:name="h_authorship"]', namespaces=NS))
end = next(i for i,p in enumerate(body_text) if i>start and paragraph_text(p) == 'Contents')
word_units = [paragraph_text(p) for p in body_text[start:end] if paragraph_text(p)]
assert word_units == source_units, (len(source_units), len(word_units), [(a,b) for a,b in zip(source_units,word_units) if a!=b][:5])
bookmarks = document.xpath('//w:bookmarkStart/@w:name', namespaces=NS)
assert len(bookmarks) == len(set(bookmarks))
assert bookmarks.count('h_authorship') == 1
entries = document.xpath('//w:body/w:p[w:pPr/w:pStyle[@w:val="PMContents" or @w:val="PMContentsChapter"]]', namespaces=NS)
assert len(entries) == 89
toc_targets = [p.xpath('./w:hyperlink/@w:anchor', namespaces=NS) for p in entries]
assert all(len(t)==1 and t[0] in bookmarks for t in toc_targets)
sections = document.xpath('//w:body/w:sectPr|//w:body/w:p/w:pPr/w:sectPr', namespaces=NS)
assert len(sections) == 3
fmt = [s.find('w:pgNumType', NS) for s in sections]
assert fmt[1] is not None and fmt[1].get(q('fmt')) == 'lowerRoman' and fmt[1].get(q('start')) == '1'
assert fmt[2] is not None and fmt[2].get(q('fmt')) == 'decimal' and fmt[2].get(q('start')) == '1'
pdf = PdfReader(PDF)
assert len(pdf.pages) == 165
folio_regex = re.compile(r'^PROJECT MANAGEMENT\s+((?:[ivxlcdm]+)|\d+)\s*$', re.I | re.M)
all_folios = []
for physical, page in enumerate(pdf.pages, start=1):
    text = page.extract_text() or ''
    matches = folio_regex.findall(text)
    if physical == 1:
        assert not matches
        all_folios.append(None)
    else:
        assert len(matches) == 1, (physical, matches)
        expected = ['i', 'ii', 'iii', 'iv', 'v'][physical-2] if physical <= 6 else str(physical-6)
        assert matches[0] == expected, (physical, matches[0], expected)
        all_folios.append(matches[0])
toc_map = json.loads((EVIDENCE / 'toc-map-v5.json').read_text())
assert len(toc_map['entries']) == len(entries) == 89
for para, row in zip(entries, toc_map['entries']):
    link = para.find('w:hyperlink', NS)
    label = ' '.join(link.xpath('.//w:t/text()', namespaces=NS))
    assert row['anchor'] == link.get(q('anchor'))
    destination_page = pdf.pages[row['physical_page']-1].extract_text() or ''
    assert normalized(label) in normalized(destination_page), (label, row['physical_page'])
pdf_lines = []
for page in pdf.pages[1:6]:
    t = page.extract_text() or ''
    pdf_lines.extend(line.strip() for line in t.splitlines() if not line.strip().startswith('PROJECT MANAGEMENT'))
pdf_auth_text = normalized(' '.join(pdf_lines))
for unit in source_units:
    assert normalized(unit) in pdf_auth_text, unit
print(json.dumps({'source_sha256': hashlib.sha256(MD.read_bytes()).hexdigest(),
                  'word_sha256': hashlib.sha256(DOCX.read_bytes()).hexdigest(),
                  'rendered_pdf_sha256': hashlib.sha256(PDF.read_bytes()).hexdigest(),
                  'article_paragraphs_and_headings': len(source_units),
                  'exact_markdown_word_paragraph_order': True,
                  'pdf_contains_all_frontmatter_units': True,
                  'unchanged_original_book_body_bytes': True,
                  'toc_links': len(entries), 'word_sections': 3,
                  'folio_sections': ['cover unnumbered', 'lowerRoman:start1', 'decimal:start1'],
                  'frontmatter_folios': all_folios[1:6], 'main_body_folios': [all_folios[6], all_folios[-1]],
                  'toc_destinations_match_headings': len(entries),
                  'source_v4_hashes_unchanged': True,
                  'docx_metadata_and_template_image': 'PASS',
                  'comments_and_tracked_changes': 'NONE',
                  'hyperlink_targets': link_targets,
                  'pdf_pages': len(pdf.pages)}, indent=2))
zip_file.close()
