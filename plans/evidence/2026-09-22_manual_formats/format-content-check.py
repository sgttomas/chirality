from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
from collections import Counter
import re,json,difflib
D=Path('/Users/ryan/.codex/worktrees/da43/chirality/docs/alignment-manual');n={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
z=ZipFile(D/'Project_Management_for_Human_Agent_Teams_Consolidated_v2.docx');r=E.fromstring(z.read('word/document.xml'));text='\n'.join(''.join(p.xpath('.//w:t/text()',namespaces=n)) for p in r.xpath('//w:body//w:p',namespaces=n))
md=(D/'Project_Management_for_Human_Agent_Teams_Consolidated_v2.md').read_text()
def normal(s):
 s=re.sub(r'\[([^\]]+)\]\([^)]*\)',r'\1',s);s=re.sub(r'<[^>]*>','',s);s=s.replace('**','').replace('`','').replace('*','');return re.sub(r'\s+',' ',s).strip()
# Paragraph-level coverage preserves multiline specimen/table text, allowing typographic whitespace only.
nt=normal(text);missing=[]
for num,line in enumerate(md.splitlines(),1):
 line=line.strip()
 if not line or line.startswith(('#','```','<','- [','|---')):continue
 vals=[x.strip() for x in line.strip('|').split('|')] if line.startswith('|') else [line]
 for v in vals:
  v=normal(v)
  if v and v not in nt:missing.append((num,v))
print('Markdown nonheading line/cell misses',len(missing));print(json.dumps(missing[:45],indent=2))
# Every original bookmark persists; every internal link targets an existing bookmark.
bms=r.xpath('//w:bookmarkStart/@w:name',namespaces=n);anchors=r.xpath('//w:hyperlink/@w:anchor',namespaces=n);print('bookmarks',len(bms),'duplicates',[(k,v) for k,v in Counter(bms).items() if v>1],'broken anchors',set(anchors)-set(bms))
a=ZipFile(D/'Project_Management_for_Human_Agent_Teams_Consolidated_v1.docx');changed=[p for p in a.namelist() if a.read(p)!=z.read(p)];print('changed parts',changed)
Path('/tmp/manual-formats-20260922/coverage-misses.json').write_text(json.dumps(missing,indent=2))
