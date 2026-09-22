from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
from lxml import etree as E
import hashlib,json,re
D=Path('/Users/ryan/.codex/worktrees/da43/chirality/docs/alignment-manual/Project_Management_for_Human_Agent_Teams_Consolidated_v4.docx');Q=Path('/tmp/manual-v4-20260922');z=ZipFile(D);parts={i.filename:z.read(i) for i in z.infolist()};W='http://schemas.openxmlformats.org/wordprocessingml/2006/main';N={'w':W};r=E.fromstring(parts['word/document.xml']);changes={};removed=0
for x in r.iter():
 for k in list(x.attrib):
  if E.QName(k).localname.startswith('rsid'):del x.attrib[k];removed+=1
for x in r.xpath('//w:bookmarkStart',namespaces=N):
 name=x.get('{'+W+'}name')
 if len(name)>40:
  new=name[:30]+'_'+hashlib.sha256(name.encode()).hexdigest()[:8];changes[name]=new;x.set('{'+W+'}name',new)
for x in r.xpath('//w:hyperlink[@w:anchor]',namespaces=N):
 name=x.get('{'+W+'}anchor')
 if name in changes:x.set('{'+W+'}anchor',changes[name])
parts['word/document.xml']=E.tostring(r,encoding='UTF-8',xml_declaration=True,standalone=True)
with ZipFile(D,'w',ZIP_DEFLATED) as out:
 for i in z.infolist():out.writestr(i,parts[i.filename])
(Q/'identifier-cleanup.json').write_text(json.dumps({'section_session_attributes_removed':removed,'generated_bookmark_names_shortened':changes},indent=2));print('Removed',removed,'rsidattributes; shortened',len(changes),'generatedbookmarknames')
