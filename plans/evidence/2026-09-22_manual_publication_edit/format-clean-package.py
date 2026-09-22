from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
from lxml import etree as E
import re,json
D=Path('/Users/ryan/.codex/worktrees/da43/chirality/docs/alignment-manual/Project_Management_for_Human_Agent_Teams_Consolidated_v4.docx');Q=Path('/tmp/manual-v4-20260922');z=ZipFile(D);parts={i.filename:z.read(i) for i in z.infolist()};W='http://schemas.openxmlformats.org/wordprocessingml/2006/main';N={'w':W,'r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'};r=E.fromstring(parts['word/document.xml']);used=set(r.xpath('//w:hyperlink/@r:id',namespaces=N));rels=E.fromstring(parts['word/_rels/document.xml.rels']);removed=[]
for rel in list(rels):
 if rel.get('Type','').endswith('/hyperlink') and rel.get('Id') not in used:removed.append(dict(rel.attrib));rels.remove(rel)
settings=E.fromstring(parts['word/settings.xml']);removed_settings=[]
for x in list(settings):
 if E.QName(x).localname in ['rsids','docId']:removed_settings.append(E.QName(x).localname);settings.remove(x)
app=E.fromstring(parts['docProps/app.xml']);body=' '.join(r.xpath('//w:t/text()',namespaces=N))
for x in app:
 if E.QName(x).localname=='Characters':x.text=str(len(re.sub(r'\s','',body)))
for name,x in [('word/_rels/document.xml.rels',rels),('word/settings.xml',settings),('docProps/app.xml',app)]:parts[name]=E.tostring(x,encoding='UTF-8',xml_declaration=True,standalone=True)
with ZipFile(D,'w',ZIP_DEFLATED) as out:
 for i in z.infolist():out.writestr(i,parts[i.filename])
(Q/'package-cleanup.json').write_text(json.dumps({'unused_hyperlink_relationships_removed':removed,'settings_identifiers_removed':removed_settings},indent=2));print('Removed',len(removed),'unused hyperlinks and settings',removed_settings)
