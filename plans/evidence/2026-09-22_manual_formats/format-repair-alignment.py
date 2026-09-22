from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
from lxml import etree as E
D=Path('/Users/ryan/.codex/worktrees/da43/chirality/docs/alignment-manual/Project_Management_for_Human_Agent_Teams_Consolidated_v2.docx');z=ZipFile(D);parts={i.filename:z.read(i) for i in z.infolist()};n={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'};r=E.fromstring(parts['word/document.xml'])
for start in ['This edition was compared with Chirality at revision','The App and Piping persistent local-graph loops are now maintained repository instructions.']:
 p=next(p for p in r.xpath('//w:body/w:p',namespaces=n) if ''.join(p.xpath('.//w:t/text()',namespaces=n)).startswith(start));pr=p.find('w:pPr',n);jc=pr.find('w:jc',n)
 if jc is None:jc=E.SubElement(pr,'{'+n['w']+'}jc')
 jc.set('{'+n['w']+'}val','left')
parts['word/document.xml']=E.tostring(r,xml_declaration=True,encoding='UTF-8',standalone=True)
with ZipFile(D,'w',ZIP_DEFLATED) as out:
 for i in z.infolist():out.writestr(i,parts[i.filename])
