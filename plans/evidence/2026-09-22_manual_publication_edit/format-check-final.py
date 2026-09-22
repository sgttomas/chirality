from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
from PIL import Image,ImageChops
from pypdf import PdfReader
import json,re,hashlib,shutil
R=Path('/Users/ryan/.codex/worktrees/da43/chirality');D=R/'docs/alignment-manual';Q=Path('/tmp/manual-v4-20260922');stem='Project_Management_for_Human_Agent_Teams_Consolidated_v4';pdfpath=Q/'final3'/(stem+'.pdf');pdf=PdfReader(pdfpath);assert len(pdf.pages)==162
changed=[]
for i in range(1,163):
 a=Image.open(Q/'final2'/f'page-{i}.png').convert('RGB');b=Image.open(Q/'final3'/f'page-{i}.png').convert('RGB')
 if ImageChops.difference(a,b).getbbox():changed.append(i)
assert not changed,changed
z=ZipFile(D/(stem+'.docx'));N={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'};r=E.fromstring(z.read('word/document.xml'));entries=r.xpath('//w:body/w:p[w:pPr/w:pStyle[@w:val="PMContents" or @w:val="PMContentsChapter"]]',namespaces=N);ann=[];seen=set()
for p in pdf.pages[1:3]:
 for a in sorted([a.get_object() for a in p.get('/Annots',[])],key=lambda a:-float(a['/Rect'][3])):
  if '/Dest' in a and str(a['/Dest']) not in seen:seen.add(str(a['/Dest']));ann.append(a)
assert len(ann)==len(entries)==88
pages=[]
for entry,a in zip(entries,ann):
 pi=pdf.get_page_number(a['/Dest'][0].get_object());actual=int(re.search(r'^PROJECT MANAGEMENT\s+(\d+)\s*$',pdf.pages[pi].extract_text(),re.M)[1]);cache=int(entry.xpath('./w:r/w:t/text()',namespaces=N)[0]);assert cache==actual;(pages.append({'anchor':entry.xpath('./w:hyperlink/@w:anchor',namespaces=N)[0],'physical_page':pi+1,'folio':actual}))
uris=[]
for i,p in enumerate(pdf.pages):
 text=p.extract_text()
 if i:assert re.search(r'^PROJECT MANAGEMENT\s+'+str(i)+r'\s*$',text,re.M),(i,text[:120])
 for a in p.get('/Annots',[]):
  act=a.get_object().get('/A')
  if act and '/URI' in act:uris.append(str(act['/URI']))
assert 'CHIRALITY_AGENT_USER_MANUAL_v2.md' in uris,uris
assert not any('/tmp/' in u or 'ProtonDrive' in u or u.startswith('file:') for u in uris)
shutil.copy2(pdfpath,D/(stem+'.pdf'))
report={'pages':162,'printed_folios':'unprinted cover,1–161','toc_links_and_folios_validated':88,'pdf_uris':sorted(set(uris)),'final3_pixel_changes_from_final2':changed,'docx_sha256':hashlib.sha256((D/(stem+'.docx')).read_bytes()).hexdigest(),'pdf_sha256':hashlib.sha256((D/(stem+'.pdf')).read_bytes()).hexdigest(),'toc_map':pages}
(Q/'final-check.json').write_text(json.dumps(report,indent=2));print(json.dumps({k:v for k,v in report.items() if k!='toc_map'},indent=2))
