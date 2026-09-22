from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
from collections import Counter
import json,re,hashlib,sys
R=Path('/Users/ryan/.codex/worktrees/da43/chirality');D=R/'docs/alignment-manual';Q=Path('/tmp/manual-v4-20260922');S=Path('/Users/ryan/Library/CloudStorage/ProtonDrive-Ryan.Tufts@protonmail.com-folder/GBT');stem='Project_Management_for_Human_Agent_Teams_Consolidated_';md=(D/(stem+'v4.md')).read_text();assert hashlib.sha256(md.encode()).hexdigest()=='2d9638c50a948623e7b94e7544308c1bd411765e679873a6911cdf09a8e37ca6';z=ZipFile(D/(stem+'v4.docx'));a=ZipFile(S/(stem+'v3.docx'));W='http://schemas.openxmlformats.org/wordprocessingml/2006/main';N={'w':W};r=E.fromstring(z.read('word/document.xml'));ar=E.fromstring(a.read('word/document.xml'))
def text(p):return ''.join((c.text or '') if c.tag=='{'+W+'}t' else '\n' for c in p.iter() if c.tag in ['{'+W+'}t','{'+W+'}br','{'+W+'}tab'])
def norm(s):
 s=re.sub(r'!?\[([^\]]+)\]\([^)]*\)',r'\1',s);s=re.sub(r'^#+\s*','',s);s=s.replace('**','').replace('*','').replace('`','');return re.sub(r'\s+',' ',s).strip()
body='\n'.join(text(p) for p in r.xpath('//w:body//w:p',namespaces=N));nt=norm(body);missing=[];checked=0;fence=False
for ln,line in enumerate(md.splitlines(),1):
 line=line.strip()
 if not line or line.startswith(('<a ','- [','```','![')):continue
 if re.fullmatch(r'\|[-:| ]+\|',line):continue
 vals=[s.strip() for s in line.strip('|').split('|')] if line.startswith('|') else [line]
 for val in vals:
  v=norm(val);checked+=1
  if v and v not in nt and not (ln<=5 and v.casefold() in nt.casefold()):missing.append([ln,v])
assert not missing,missing[:20]
bms=r.xpath('//w:bookmarkStart/@w:name',namespaces=N);anchors=r.xpath('//w:hyperlink/@w:anchor',namespaces=N);assert len(bms)==len(set(bms));assert set(anchors)<=set(bms),set(anchors)-set(bms)
mdanchors=re.findall(r'<a id="([^"]+)"',md);assert set(mdanchors)<=set(bms)
rels=E.fromstring(z.read('word/_rels/document.xml.rels'));origrels=E.fromstring(a.read('word/_rels/document.xml.rels'));assert all(any(E.tostring(x)==E.tostring(y) for y in rels) for x in origrels if not x.get('Type','').endswith('/hyperlink'))
activeids=r.xpath('//w:hyperlink/@r:id',namespaces={**N,'r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'});relmap={x.get('Id'):x.get('Target') for x in rels};active=[relmap[x] for x in activeids]
assert 'CHIRALITY_AGENT_USER_MANUAL_v2.md' in active
assert not any('/tmp/' in x or 'ProtonDrive' in x or x.startswith('file:') for x in active)
for t in active:
 if '://' not in t:assert (D/t.split('#')[0]).exists(),t
changed=[x for x in a.namelist() if a.read(x)!=z.read(x)];assert set(changed)<={'word/document.xml','word/_rels/document.xml.rels','word/footer5.xml','word/settings.xml','docProps/core.xml','docProps/app.xml'},changed
for x in ar.xpath('//w:sectPr',namespaces=N):
 for key in list(x.attrib):
  if E.QName(key).localname.startswith('rsid'):del x.attrib[key]
assert [E.tostring(x) for x in ar.xpath('//w:sectPr',namespaces=N)]==[E.tostring(x) for x in r.xpath('//w:sectPr',namespaces=N)]
for forbidden in ['CONSOLIDATED MANUSCRIPT','EDITION 3','EDITION 4','Prepared with ChatGPT','For author review']:
 assert forbidden not in body,forbidden
 assert forbidden not in z.read('word/footer5.xml').decode()
 assert forbidden not in z.read('docProps/core.xml').decode()
report={'md_sha256':hashlib.sha256(md.encode()).hexdigest(),'docx_sha256':hashlib.sha256((D/(stem+'v4.docx')).read_bytes()).hexdigest(),'all_md_content_lines_and_cells_checked':checked,'missing_content':missing,'md_explicit_anchors':len(mdanchors),'word_bookmarks':len(bms),'internal_hyperlinks':len(anchors),'active_external_hyperlink_targets':sorted(set(active)),'changed_package_parts':changed,'preserved_package_parts':len(a.namelist())-len(changed),'sections':2,'data_and_nested_figure_tables':len(r.xpath('//w:tbl',namespaces=N)),'specimens':len(r.xpath('//w:pStyle[@w:val="PMSpecimen"]',namespaces=N))}
(Q/'content-check.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
