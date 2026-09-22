from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
from lxml import etree as E
D=Path('/Users/ryan/.codex/worktrees/da43/chirality/docs/alignment-manual/Project_Management_for_Human_Agent_Teams_Consolidated_v2.docx');z=ZipFile(D);parts={i.filename:z.read(i) for i in z.infolist()};n={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'};r=E.fromstring(parts['word/document.xml']);tc=next(c for c in r.xpath('//w:tc',namespaces=n) if ''.join(c.xpath('.//w:t/text()',namespaces=n))=='Engineering stage')
for side in ['left','right']:tc.find('w:tcPr/w:tcMar/w:'+side,n).set('{'+n['w']+'}w','45')
parts['word/document.xml']=E.tostring(r,xml_declaration=True,encoding='UTF-8',standalone=True)
with ZipFile(D,'w',ZIP_DEFLATED) as out:
 for i in z.infolist():out.writestr(i,parts[i.filename])
