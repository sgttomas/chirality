from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
from pypdf import PdfReader
from collections import Counter
import re,json,hashlib,urllib.parse
ROOT=Path('/Users/ryan/.codex/worktrees/da43/chirality');D=ROOT/'docs/alignment-manual';Q=Path('/tmp/manual-formats-20260922');n={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
a=ZipFile(D/'Project_Management_for_Human_Agent_Teams_Consolidated_v1.docx');z=ZipFile(D/'Project_Management_for_Human_Agent_Teams_Consolidated_v2.docx');ar=E.fromstring(a.read('word/document.xml'));r=E.fromstring(z.read('word/document.xml'));pdf=PdfReader(D/'Project_Management_for_Human_Agent_Teams_Consolidated_v2.pdf');md=(D/'Project_Management_for_Human_Agent_Teams_Consolidated_v2.md').read_text()
def norm(s):return re.sub(r'\s+',' ',s).strip()
def txt(p):return ''.join(p.xpath('.//w:t/text()',namespaces=n))
body='\n'.join(txt(p) for p in r.xpath('//w:body//w:p',namespaces=n));lower=norm(body).lower();heading_miss=[]
for line in md.splitlines():
 if line.startswith('#'):
  title=re.sub(r'^#+\s*','',line)
  if norm(title).lower() not in lower:heading_miss.append(title)
# Cover title was split into two styled paragraphs; normalize space and case handles it.
assert not heading_miss,heading_miss
bms=r.xpath('//w:bookmarkStart/@w:name',namespaces=n);anchors=r.xpath('//w:hyperlink/@w:anchor',namespaces=n);assert set(anchors)<=set(bms);assert len(bms)==len(set(bms));assert set(ar.xpath('//w:bookmarkStart/@w:name',namespaces=n))<=set(bms)
entries=r.xpath('//w:body/w:p[w:pPr/w:pStyle[@w:val="PMContents" or @w:val="PMContentsChapter"]]',namespaces=n);ann=[]
for p in pdf.pages[1:3]:ann+=sorted([a.get_object() for a in p.get('/Annots',[])],key=lambda a:-float(a['/Rect'][3]))
assert len(ann)==len(entries)==81;pages=[]
for e,link in zip(entries,ann):
 pi=pdf.get_page_number(link['/Dest'][0].get_object());actual=int(re.search(r'CONSOLIDATED MANUSCRIPT · 2\s+(\d+)',pdf.pages[pi].extract_text())[1]);cached=int(e.xpath('./w:r/w:t/text()',namespaces=n)[0]);assert actual==cached,(txt(e),actual,cached);pages.append(pi+1)
# Source relative links should resolve in the shared repository.
rels=E.fromstring(z.read('word/_rels/document.xml.rels'));bad=[];external=[]
for link in rels:
 if not link.get('Type','').endswith('/hyperlink'):continue
 target=link.get('Target');external.append(target)
 if '://' not in target:
  file=urllib.parse.unquote(target.split('#')[0]);assert (D/file).exists(),target
# Preserve every original relationship and protected package part.
oldrels=E.fromstring(a.read('word/_rels/document.xml.rels'));assert all(any(E.tostring(x)==E.tostring(y) for y in rels) for x in oldrels)
changed=[name for name in a.namelist() if a.read(name)!=z.read(name)];assert set(changed)=={'word/document.xml','word/_rels/document.xml.rels','word/settings.xml','word/footer5.xml'}
assert [E.tostring(x) for x in ar.xpath('//w:sectPr',namespaces=n)]==[E.tostring(x) for x in r.xpath('//w:sectPr',namespaces=n)]
for i,p in enumerate(pdf.pages):
 t=p.extract_text()
 if i:assert f'CONSOLIDATED MANUSCRIPT · 2 {i}\n' in t,(i,t[:100])
 assert 'Error! Reference source not found' not in t
 assert '�' not in t
report={'pages':len(pdf.pages),'render_png_count':len(list((Q/'final2').glob('page-*.png'))),'toc_entries':81,'toc_destinations_match_final_printed_folio':True,'printed_folio_sequence':'unprinted cover, 1–179','bookmarks':len(bms),'internal_links':len(anchors),'external_links':len(external),'original_relationships_preserved':len(oldrels),'changed_package_parts':changed,'unchanged_package_parts':len(a.namelist())-len(changed),'table_count':len(r.xpath('//w:tbl',namespaces=n)),'heading_coverage':'all Markdown headings mapped','source_relative_links_resolve':True,'v1_docx_sha256':hashlib.sha256((D/'Project_Management_for_Human_Agent_Teams_Consolidated_v1.docx').read_bytes()).hexdigest(),'v2_docx_sha256':hashlib.sha256((D/'Project_Management_for_Human_Agent_Teams_Consolidated_v2.docx').read_bytes()).hexdigest(),'v2_pdf_sha256':hashlib.sha256((D/'Project_Management_for_Human_Agent_Teams_Consolidated_v2.pdf').read_bytes()).hexdigest()}
(Q/'structural-report.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
