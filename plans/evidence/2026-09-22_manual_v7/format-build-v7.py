from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
from copy import deepcopy
from lxml import etree as E
import ast,re,difflib,hashlib,json
R=Path('/Users/ryan/.codex/worktrees/da43/chirality');D=R/'docs/alignment-manual';Q=Path('/tmp/manual-v7-20260922');EV=R/'plans/evidence/2026-09-22_manual_v7'
OLDMD=D/'Project_Management_for_Human_Agent_Teams_Consolidated_v5.md';NEWMD=D/'Project_Management_for_Human_Agent_Teams_Consolidated_v7.md';REF=OLDMD.with_suffix('.docx');OUT=NEWMD.with_suffix('.docx')
assert hashlib.sha256(REF.read_bytes()).hexdigest()=='73cf67dea870ebfbfccb903f1b0c4c275b5d3f4770f48f0ce2cc83f2990d2722'
# Reuse the already exercised Markdown block reader, without executing its old authoring script.
p=R/'plans/evidence/2026-09-22_manual_publication_edit/format-build-v4.py';tree=ast.parse(p.read_text());helpers={'re':re}
exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name in ['parse','norm']],type_ignores=[]),str(p),'exec'),helpers)
parse,norm=helpers['parse'],helpers['norm'];old=parse(OLDMD.read_text());new=parse(NEWMD.read_text())
old=old[next(i for i,b in enumerate(old) if 'h_preface' in b['anchors']):];new=new[next(i for i,b in enumerate(new) if 'h_preface' in b['anchors']):]
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main';REL='http://schemas.openxmlformats.org/officeDocument/2006/relationships';PK='http://schemas.openxmlformats.org/package/2006/relationships';NS={'w':W}
def w(s):return '{'+W+'}'+s
def el(s,**attrs):
 x=E.Element(w(s))
 for k,v in attrs.items():x.set(w(k),str(v))
 return x
def text(x):
 return '\n'.join(''.join((c.text or '') if c.tag==w('t') else '\n' for c in p.iter() if c.tag in [w('t'),w('br'),w('tab')]) for p in ([x] if x.tag==w('p') else x.xpath('.//w:p',namespaces=NS)))
def key(b):return (b['kind'],b['raw'],b.get('caption',''))
def want(b):return ' '.join(' '.join(row) for row in b['rows']) if b['kind']=='table' else b['raw']+'\n'+b['caption'] if b['kind']=='figure' else b['raw']
z=ZipFile(REF);infos=z.infolist();parts={i.filename:z.read(i) for i in infos};root=E.fromstring(parts['word/document.xml']);body=root.find('w:body',NS);orig=list(body)
start=next(i for i,x in enumerate(orig) if x.xpath('.//w:bookmarkStart[@w:name="h_preface"]',namespaces=NS));oldels=orig[start:-1]
assert len(oldels)==len(old)==1299
for b,x in zip(old,oldels):
 if b['kind']!='image':assert norm(want(b))==norm(text(x)),(b['line'],b['kind'])
rels=E.fromstring(parts['word/_rels/document.xml.rels']);rids={r.get('Target'):r.get('Id') for r in rels if r.get('Type','').endswith('/hyperlink')};nextrid=max(int(r.get('Id')[3:]) for r in rels)+1
nextbm=max(int(b.get(w('id'))) for b in root.xpath('//w:bookmarkStart',namespaces=NS))+1

def linkid(url):
 global nextrid
 if url not in rids:
  rid='rId'+str(nextrid);nextrid+=1;r=E.SubElement(rels,'{'+PK+'}Relationship');r.set('Id',rid);r.set('Type',REL+'/hyperlink');r.set('Target',url);r.set('TargetMode','External');rids[url]=rid
 return rids[url]
def inline(parent,md,flags=()):
 for s in re.split(r'(`[^`]+`|\*\*[^*]+\*\*|\*[^*]+\*|\[[^\]]+\]\([^)]*\))',md):
  if not s:continue
  m=re.fullmatch(r'\[([^\]]+)\]\(([^)]*)\)',s)
  if m:
   h=el('hyperlink');h.set(w('anchor') if m[2].startswith('#') else '{'+REL+'}id',m[2][1:] if m[2].startswith('#') else linkid(m[2]));parent.append(h);inline(h,m[1],flags);continue
  if s.startswith('**') and s.endswith('**'):inline(parent,s[2:-2],flags+('b',));continue
  if s.startswith('*') and s.endswith('*'):inline(parent,s[1:-1],flags+('i',));continue
  code=s.startswith('`') and s.endswith('`');s=s[1:-1] if code else s
  rr=el('r');rp=el('rPr');rp.append(el('color',val='000000'))
  for f in flags:rp.append(el(f))
  if code:rp.append(el('rFonts',ascii='Liberation Mono',hAnsi='Liberation Mono'));rp.append(el('sz',val=18))
  rr.append(rp);t=el('t');t.set('{http://www.w3.org/XML/1998/namespace}space','preserve');t.text=s;rr.append(t);parent.append(rr)
def refill(p,md,flags=()):
 for c in list(p):
  if c.tag not in [w('pPr'),w('bookmarkStart'),w('bookmarkEnd')]:p.remove(c)
 inline(p,md,flags);return p
def cleanmarks(x):
 for c in x.xpath('.//w:bookmarkStart|.//w:bookmarkEnd',namespaces=NS):c.getparent().remove(c)
 return x
def style(p):
 s=p.find('w:pPr/w:pStyle',NS);return s.get(w('val')) if s is not None else 'Normal'
normal=next(x for x in oldels if x.tag==w('p') and text(x).startswith('This manual concerns'))
ht={i:next(x for x in oldels if x.tag==w('p') and style(x)=='Heading'+str(i)) for i in [1,2,3]}
figs={re.match(r'^\*?Figure ([\dA-Z]+\.\d+)\.',b['caption'])[1]:x for b,x in zip(old,oldels) if b['kind']=='figure'}

def attach(x,names):
 global nextbm
 p=x if x.tag==w('p') else x.find('.//w:p',NS)
 existing=x.xpath('.//w:bookmarkStart/@w:name',namespaces=NS)
 for name in names:
  if name in existing:continue
  p.insert(1,el('bookmarkStart',id=nextbm,name=name));p.append(el('bookmarkEnd',id=nextbm));nextbm+=1

def changed(b,base=None,preserve_marks=False):
 k=b['kind']
 if base is not None:x=deepcopy(base)
 elif k=='heading':x=deepcopy(ht[min(b['level'],3)])
 elif k=='p':x=deepcopy(normal)
 elif k=='figure':x=deepcopy(figs[re.match(r'^\*?Figure ([\dA-Z]+\.\d+)\.',b['caption'])[1]])
 else:raise AssertionError(('unmapped new component',k,b['line']))
 if not preserve_marks:cleanmarks(x)
 if k in ['p','heading']:
  refill(x,b['raw'])
  if k=='heading':
   pr=x.find('w:pPr',NS);sp=pr.find('w:pStyle',NS)
   if sp is None:sp=el('pStyle');pr.insert(0,sp)
   sp.set(w('val'),'Heading'+str(min(b['level'],3)))
 elif k=='figure':
  cp=x.xpath('.//w:p[w:pPr/w:pStyle[@w:val="PMSpecimen"]]',namespaces=NS)[0]
  for c in list(cp):
   if c.tag not in [w('pPr'),w('bookmarkStart'),w('bookmarkEnd')]:cp.remove(c)
  rr=el('r');cp.append(rr)
  for i,line in enumerate(b['raw'].splitlines()):
   if i:rr.append(el('br'))
   t=el('t');t.set('{http://www.w3.org/XML/1998/namespace}space','preserve');t.text=line;rr.append(t)
  cap=x.xpath('.//w:p[w:pPr/w:pStyle[@w:val="PMFigureCaption"]]',namespaces=NS)[0];refill(cap,b['caption'])
 elif k=='table':
  rows=x.findall('w:tr',NS);assert all(len(r.findall('w:tc',NS))==len(b['rows'][0]) for r in rows)
  while len(rows)>len(b['rows']):x.remove(rows.pop())
  while len(rows)<len(b['rows']):row=cleanmarks(deepcopy(rows[-1]));x.append(row);rows.append(row)
  for i,(row,vals) in enumerate(zip(rows,b['rows'])):
   for cell,s in zip(row.findall('w:tc',NS),vals):
    ps=cell.findall('w:p',NS);assert ps
    for extra in ps[1:]:cell.remove(extra)
    refill(ps[0],s,('b',) if i==0 else ())
 else:raise AssertionError(k)
 attach(x,b['anchors'])
 if k=='heading' and not x.xpath('.//w:bookmarkStart',namespaces=NS):attach(x,['h7_'+hashlib.sha256(b['raw'].encode()).hexdigest()[:24]])
 return x

newels=[];operations=[];sm=difflib.SequenceMatcher(None,[key(b) for b in old],[key(b) for b in new],autojunk=False)
for tag,i,j,k,l in sm.get_opcodes():
 if tag=='equal':newels.extend(deepcopy(x) for x in oldels[i:j]);continue
 operations.append({'operation':tag,'old_lines':[old[i]['line'] if i<len(old) else None,old[j-1]['line'] if j>i else None],'new_lines':[new[k]['line'] if k<len(new) else None,new[l-1]['line'] if l>k else None]})
 used=set()
 for offset,b in enumerate(new[k:l]):
  chosen=i+offset if i+offset<j and old[i+offset]['kind']==b['kind'] else next((a for a in range(i,j) if a not in used and old[a]['kind']==b['kind']),None)
  if chosen in used:chosen=None
  x=changed(b,oldels[chosen] if chosen is not None else None,chosen is not None)
  if chosen is not None:used.add(chosen)
  newels.append(x)
assert len(newels)==len(new)
for b,x in zip(new,newels):
 if b['kind']!='image':assert norm(want(b))==norm(text(x)),(b['line'],b['kind'],want(b)[:120],text(x)[:120])
# Construct new authorship from the exact approved text. Keep the existing cover and numbering.
auth=parse((EV/'approved-authorship.md').read_text());auth[0]['anchors']=['h_authorship'];authels=[changed(b) for b in auth]
cover_end=next(i for i,x in enumerate(orig) if x.find('w:pPr/w:sectPr',NS) is not None)+1;cover=[deepcopy(x) for x in orig[:cover_end]]
ct=deepcopy(next(x for x in orig if x.tag==w('p') and text(x)=='Contents'))
toc_samples={s:next(x for x in orig if x.tag==w('p') and style(x)==s) for s in ['PMContents','PMContentsChapter']}
roman=deepcopy(root.xpath('//w:body/w:p/w:pPr/w:sectPr',namespaces=NS)[-1]);toc=[]
for b,x in zip(auth+new,authels+newels):
 if b['kind']=='heading' and (b['level']==1 or b['level']==2 and re.match(r'^(\d+\.|A\.)',b['raw'])):
  anchors=b['anchors'] or x.xpath('.//w:bookmarkStart/@w:name',namespaces=NS);assert anchors,b
  p=deepcopy(toc_samples['PMContentsChapter' if b['level']==1 else 'PMContents']);pr=p.find('w:pPr',NS)
  for s in pr.findall('w:sectPr',NS):pr.remove(s)
  for c in list(p):
   if c.tag!=w('pPr'):p.remove(c)
  h=el('hyperlink',anchor=anchors[0]);inline(h,b['raw']);p.append(h);rr=el('r');rr.append(el('tab'));t=el('t');t.text='i' if anchors[0]=='h_authorship' else '1';rr.append(t);p.append(rr);toc.append(p)
assert len(toc)==89;toc[-1].find('w:pPr',NS).append(roman)
for x in list(body):body.remove(x)
for x in cover+authels+[ct]+toc+newels+[deepcopy(orig[-1])]:body.append(x)
# Prune the replaced companion's unused hyperlink; preserve every non-hyperlink relationship.
used_relids=set(root.xpath('//@r:id',namespaces={'r':REL}))
for r in list(rels):
 if r.get('Type','').endswith('/hyperlink') and r.get('Id') not in used_relids:rels.remove(r)
allnames=root.xpath('//w:bookmarkStart/@w:name',namespaces=NS);assert len(allnames)==len(set(allnames))
for href in root.xpath('//w:hyperlink/@w:anchor',namespaces=NS):assert href in allnames,href
parts['word/document.xml']=E.tostring(root,encoding='UTF-8',xml_declaration=True,standalone=True);parts['word/_rels/document.xml.rels']=E.tostring(rels,encoding='UTF-8',xml_declaration=True,standalone=True)
with ZipFile(OUT,'w',ZIP_DEFLATED) as zz:
 for info in infos:zz.writestr(deepcopy(info),parts[info.filename])
changed_parts=[name for name in parts if parts[name]!=z.read(name)];z.close()
report={'source_md_sha256':hashlib.sha256(NEWMD.read_bytes()).hexdigest(),'reference_docx_sha256':hashlib.sha256(REF.read_bytes()).hexdigest(),'docx_sha256':hashlib.sha256(OUT.read_bytes()).hexdigest(),'old_body_components':len(old),'new_body_components':len(new),'authorship_components':len(auth),'toc_entries':len(toc),'modified_package_parts':changed_parts,'body_edit_groups':operations,'template_preservation':'all other package parts byte-identical'}
(EV/'build-check.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='body_edit_groups'},indent=2))
