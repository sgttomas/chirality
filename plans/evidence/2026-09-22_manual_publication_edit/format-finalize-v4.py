from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
from lxml import etree as E
from pypdf import PdfReader
import re,json,sys
R=Path('/Users/ryan/.codex/worktrees/da43/chirality');D=R/'docs/alignment-manual';Q=Path('/tmp/manual-v4-20260922');doc=D/'Project_Management_for_Human_Agent_Teams_Consolidated_v4.docx';pdf=PdfReader(sys.argv[1]);W='http://schemas.openxmlformats.org/wordprocessingml/2006/main';N={'w':W}
z=ZipFile(doc);parts={i.filename:z.read(i) for i in z.infolist()};r=E.fromstring(parts['word/document.xml']);entries=r.xpath('//w:body/w:p[w:pPr/w:pStyle[@w:val="PMContents" or @w:val="PMContentsChapter"]]',namespaces=N);ann=[];seen=set()
for page in pdf.pages[1:]:
 for a in sorted([a.get_object() for a in page.get('/Annots',[])],key=lambda a:-float(a['/Rect'][3])):
  dest=a.get('/Dest')
  if not dest:continue
  key=str(dest)
  if key not in seen:ann.append(a);seen.add(key)
 if len(ann)>=len(entries):break
assert len(ann)==len(entries)==88,(len(ann),len(entries));out=[]
for e,a in zip(entries,ann):
 pi=pdf.get_page_number(a['/Dest'][0].get_object());t=pdf.pages[pi].extract_text();folio=re.search(r'^PROJECT MANAGEMENT\s+(\d+)\s*$',t,re.M);assert folio,t[:180];v=int(folio[1]);ts=e.xpath('./w:r/w:t',namespaces=N);assert len(ts)==1;ts[0].text=str(v);out.append({'anchor':e.find('w:hyperlink',N).get('{'+W+'}anchor'),'physical_page':pi+1,'printed_folio':v})
# Document-property statistics describe this exported book, not the inherited template.
app=E.fromstring(parts['docProps/app.xml']);ns=E.QName(app).namespace;ap=lambda s:'{'+ns+'}'+s
body=' '.join(r.xpath('//w:t/text()',namespaces=N));vals={'Pages':str(len(pdf.pages)),'Words':str(len(body.split())),'Characters':str(len(re.sub(r'\s','',body))),'CharactersWithSpaces':str(len(body)),'Paragraphs':str(len(r.xpath('//w:p',namespaces=N))),'Application':'Codex'}
for name,value in vals.items():
 x=app.find(ap(name))
 if x is not None:x.text=value
for name in ['AppVersion','Lines']:
 x=app.find(ap(name))
 if x is not None:app.remove(x)
for name,x in [('word/document.xml',r),('docProps/app.xml',app)]:parts[name]=E.tostring(x,encoding='UTF-8',xml_declaration=True,standalone=True)
with ZipFile(doc,'w',ZIP_DEFLATED) as zz:
 for i in z.infolist():zz.writestr(i,parts[i.filename])
(Q/'toc-map.json').write_text(json.dumps(out,indent=2));print('Cached',len(out),'TOCpages; metadata pages',len(pdf.pages))
