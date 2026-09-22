from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
from lxml import etree as E
from pypdf import PdfReader
import re,json,sys
D=Path('/Users/ryan/.codex/worktrees/da43/chirality/docs/alignment-manual');doc=D/'Project_Management_for_Human_Agent_Teams_Consolidated_v2.docx'; pdf=Path(sys.argv[1]);n={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'};W=n['w']
z=ZipFile(doc);parts={i.filename:z.read(i) for i in z.infolist()};r=E.fromstring(parts['word/document.xml']);entries=r.xpath('//w:body/w:p[w:pPr/w:pStyle[@w:val="PMContents" or @w:val="PMContentsChapter"]]',namespaces=n)
p=PdfReader(pdf);ann=[]
for page in p.pages[1:3]:ann+=sorted([a.get_object() for a in page.get('/Annots',[])],key=lambda a:-float(a['/Rect'][3]))
assert len(ann)==len(entries),(len(ann),len(entries));report=[]
for entry,a in zip(entries,ann):
 dest=a['/Dest']; pi=p.get_page_number(dest[0].get_object());pt=p.pages[pi].extract_text();match=re.search(r'CONSOLIDATED MANUSCRIPT · 2\s+(\d+)',pt);assert match
 folio=match[1];ts=entry.xpath('./w:r/w:t',namespaces=n);assert len(ts)==1;old=ts[0].text;ts[0].text=folio
 report.append({'anchor':entry.xpath('./w:hyperlink/@w:anchor',namespaces=n)[0],'physical_page':pi+1,'printed_page':int(folio),'old':old})
parts['word/document.xml']=E.tostring(r,xml_declaration=True,encoding='UTF-8',standalone=True)
with ZipFile(doc,'w',ZIP_DEFLATED) as zz:
 for i in z.infolist():zz.writestr(i,parts[i.filename])
Path('/tmp/manual-formats-20260922/toc-map.json').write_text(json.dumps(report,indent=2));print('Updated',len(report),'entries')
