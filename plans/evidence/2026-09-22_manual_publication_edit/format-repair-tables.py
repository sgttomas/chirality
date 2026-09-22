from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
from lxml import etree as E
D=Path('/Users/ryan/.codex/worktrees/da43/chirality/docs/alignment-manual/Project_Management_for_Human_Agent_Teams_Consolidated_v4.docx');z=ZipFile(D);parts={i.filename:z.read(i) for i in z.infolist()};W='http://schemas.openxmlformats.org/wordprocessingml/2006/main';N={'w':W};r=E.fromstring(parts['word/document.xml']);targets={'Undertaking':[1900,2900,2947],'Condition found':[2100,2700,2947]};found=[]
for table in r.xpath('//w:body/w:tbl',namespaces=N):
 first=table.find('w:tr/w:tc',N);label=''.join(first.xpath('.//w:t/text()',namespaces=N))
 if label not in targets:continue
 widths=targets[label];found.append(label)
 for col,width in zip(table.findall('w:tblGrid/w:gridCol',N),widths):col.set('{'+W+'}w',str(width))
 for row in table.findall('w:tr',N):
  for cell,width in zip(row.findall('w:tc',N),widths):cell.find('w:tcPr/w:tcW',N).set('{'+W+'}w',str(width))
assert len(found)==2,found
parts['word/document.xml']=E.tostring(r,encoding='UTF-8',xml_declaration=True,standalone=True)
with ZipFile(D,'w',ZIP_DEFLATED) as out:
 for i in z.infolist():out.writestr(i,parts[i.filename])
print('Balanced tables',found)
