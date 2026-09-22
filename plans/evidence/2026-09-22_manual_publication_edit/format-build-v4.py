"""One-off source-derived v4 publication patch; approved Markdown is sole content input."""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
from copy import deepcopy
from lxml import etree as E
from collections import defaultdict,Counter
import re,json,hashlib
R=Path('/Users/ryan/.codex/worktrees/da43/chirality');D=R/'docs/alignment-manual';Q=Path('/tmp/manual-v4-20260922');S=Path('/Users/ryan/Library/CloudStorage/ProtonDrive-Ryan.Tufts@protonmail.com-folder/GBT');stem='Project_Management_for_Human_Agent_Teams_Consolidated_';MD=D/(stem+'v4.md');REF=S/(stem+'v3.docx');OUT=D/(stem+'v4.docx')
assert hashlib.sha256(MD.read_bytes()).hexdigest()=='2d9638c50a948623e7b94e7544308c1bd411765e679873a6911cdf09a8e37ca6'
assert hashlib.sha256(REF.read_bytes()).hexdigest()=='72071478c4ce5e9813971c797c0943648dfb9107e1adc3849389854908e2e369'
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main';REL='http://schemas.openxmlformats.org/officeDocument/2006/relationships';PK='http://schemas.openxmlformats.org/package/2006/relationships';N={'w':W}
def w(s):return '{'+W+'}'+s
def el(tag,**attrs):
 x=E.Element(w(tag))
 for k,v in attrs.items():x.set(w(k),str(v))
 return x
def norm(s):
 s=re.sub(r'!?\[([^\]]+)\]\([^)]*\)',r'\1',s);s=re.sub(r'^#+\s*','',s);s=s.replace('**','').replace('`','').replace('*','');return re.sub(r'\s+',' ',s).strip()
def text(x):
 ps=[x] if E.QName(x).localname=='p' else x.xpath('.//w:p',namespaces=N)
 return '\n'.join(''.join((c.text or '') if c.tag==w('t') else '\n' for c in p.iter() if c.tag in [w('t'),w('br'),w('tab')]) for p in ps)
def parse(md):
 ls=md.splitlines();out=[];i=0;pending=[]
 while i<len(ls):
  line=ls[i].strip();ln=i+1;i+=1
  if not line:continue
  if line.startswith('<a '):pending.append(re.search(r'id="([^"]+)"',line)[1]);continue
  bk={'line':ln,'anchors':pending,'kind':'p','raw':line};pending=[]
  if line.startswith('```'):
   vals=[]
   while i<len(ls) and not ls[i].startswith('```'):vals.append(ls[i]);i+=1
   assert i<len(ls);i+=1;bk.update(kind='code',raw='\n'.join(vals))
  elif line.startswith('|'):
   vals=[line]
   while i<len(ls) and ls[i].strip().startswith('|'):vals.append(ls[i].strip());i+=1
   rows=[[a.strip() for a in v.strip('|').split('|')] for v in vals]
   if len(rows)>1 and all(re.fullmatch(r':?-+:?',v) for v in rows[1]):rows.pop(1)
   bk.update(kind='table',rows=rows,raw='\n'.join(vals))
  elif line.startswith('#'):
   bk.update(kind='heading',level=len(line)-len(line.lstrip('#')),raw=re.sub(r'^#+\s*','',line))
  elif line.startswith('!['):bk.update(kind='image')
  out.append(bk)
 merged=[];i=0
 while i<len(out):
  bk=out[i];i+=1
  if bk['kind']=='code' and i<len(out) and re.match(r'^\*?Figure [\dA-Z]+\.',out[i]['raw']):
   bk.update(kind='figure',caption=out[i]['raw']);bk['anchors']+=out[i]['anchors'];i+=1
  merged.append(bk)
 return merged
z=ZipFile(REF);parts={i.filename:z.read(i) for i in z.infolist()};root=E.fromstring(parts['word/document.xml']);body=root.find('w:body',N);orig=list(body);rels=E.fromstring(parts['word/_rels/document.xml.rels']);rid=max(int(x.get('Id')[3:]) for x in rels)+1
linkids={x.get('Target'):x.get('Id') for x in rels if x.get('Type','').endswith('/hyperlink')}
def linkid(url):
 global rid
 if url not in linkids:
  id='rId'+str(rid);rid+=1;x=E.SubElement(rels,'{'+PK+'}Relationship');x.set('Id',id);x.set('Type',REL+'/hyperlink');x.set('Target',url);x.set('TargetMode','External');linkids[url]=id
 return linkids[url]
def inline(parent,md,flags=(),size=None):
 pat=re.compile(r'(`[^`]+`|\*\*[^*]+\*\*|\*[^*]+\*|\[[^\]]+\]\([^)]*\))')
 for s in pat.split(md):
  if not s:continue
  m=re.fullmatch(r'\[([^\]]+)\]\(([^)]*)\)',s)
  if m:
   h=el('hyperlink')
   if m[2].startswith('#'):h.set(w('anchor'),m[2][1:])
   else:h.set('{'+REL+'}id',linkid(m[2]))
   parent.append(h);inline(h,m[1],flags,size);continue
  if s.startswith('**') and s.endswith('**'):inline(parent,s[2:-2],flags+('b',),size);continue
  if s.startswith('*') and s.endswith('*'):inline(parent,s[1:-1],flags+('i',),size);continue
  code=s.startswith('`') and s.endswith('`')
  if code:s=s[1:-1]
  rr=el('r');rp=el('rPr')
  for f in flags:rp.append(el(f))
  if size:rp.append(el('sz',val=size))
  if code:
   rp.append(el('rFonts',ascii='Liberation Mono',hAnsi='Liberation Mono'));rp.append(el('sz',val=15 if size==18 else 18))
  rr.append(rp);t=el('t');t.set('{http://www.w3.org/XML/1998/namespace}space','preserve');t.text=s;rr.append(t);parent.append(rr)
def refill(p,md,flags=(),size=None):
 for c in list(p):
  if c.tag!=w('pPr'):p.remove(c)
 inline(p,md,flags,size);return p
def cleanmarks(x):
 for p in x.xpath('.//w:bookmarkStart|.//w:bookmarkEnd',namespaces=N):p.getparent().remove(p)
 return x
ps=body.findall('w:p',N)
def style(p):
 v=p.find('w:pPr/w:pStyle',N);return v.get(w('val')) if v is not None else 'Normal'
templates={k:deepcopy(next(p for p in ps if style(p)==k)) for k in ['Heading1','Heading2','Heading3','PMContents','PMContentsChapter','PMFigureCaption']}
normal=deepcopy(next(p for p in ps if text(p).startswith('This manual concerns')))
for c in normal.findall('w:pPr/w:jc',N):normal.find('w:pPr',N).remove(c)
templates['Normal']=normal
sources=deepcopy(next(p for p in ps if text(p).startswith('[1] ')));templates['Source']=sources
ind=defaultdict(list)
for x in orig:
 if E.QName(x).localname not in ['p','tbl']:continue
 k=norm(text(x))
 if k:ind[k].append(x)
figs=[x for x in orig if x.xpath('.//w:pStyle[@w:val="PMSpecimen"]',namespaces=N)];fig_by_code={norm(text(x.xpath('.//w:p[w:pPr/w:pStyle[@w:val="PMSpecimen"]]',namespaces=N)[0])):x for x in figs}
data_tables=[x for x in orig if x.tag==w('tbl') and not x.xpath('.//w:pStyle[@w:val="PMSpecimen"]',namespaces=N)]
imagep=next(x for x in orig if x.xpath('.//w:drawing',namespaces=N));used=set();stats=Counter();log=[];nextbm=5000;bookmarks=set()
def attach(x,names):
 global nextbm
 p=x if x.tag==w('p') else x.find('.//w:p',N)
 for name in names:
  if name in bookmarks:continue
  bookmarks.add(name);p.insert(1,el('bookmarkStart',id=nextbm,name=name));p.append(el('bookmarkEnd',id=nextbm));nextbm+=1

def same(bk):
 if bk['kind']=='table':k=norm(' '.join(' '.join(row) for row in bk['rows']))
 else:k=norm(bk['raw'])
 for x in ind.get(k,[]):
  if id(x) not in used and x.tag!=w('sectPr'):
   used.add(id(x));return deepcopy(x)
 return None

def table(rows):
 cols=len(rows[0]);assert all(len(row)==cols for row in rows),rows
 choices=[x for x in data_tables if len(x.find('w:tr',N).findall('w:tc',N))==cols];assert choices,cols
 base=deepcopy(choices[0]);oldrows=base.findall('w:tr',N);head=deepcopy(oldrows[0]);sample=deepcopy(oldrows[1]);
 for tr in oldrows:base.remove(tr)
 for i,row in enumerate(rows):
  tr=deepcopy(head if i==0 else sample)
  for cell,s in zip(tr.findall('w:tc',N),row):
   p=cell.find('w:p',N)
   for other in list(cell):
    if other.tag not in [w('tcPr'),w('p')]:cell.remove(other)
    elif other.tag==w('p') and other is not p:cell.remove(other)
   refill(p,s,('b',) if i==0 else ())
  base.append(tr)
 return cleanmarks(base)

def component(bk):
 kind=bk['kind'];x=None
 if kind=='figure':
  base=fig_by_code.get(norm(bk['raw']),figs[0]);x=cleanmarks(deepcopy(base));cp=x.xpath('.//w:p[w:pPr/w:pStyle[@w:val="PMSpecimen"]]',namespaces=N)[0]
  for c in list(cp):
   if c.tag!=w('pPr'):cp.remove(c)
  rr=el('r');cp.append(rr)
  for i,line in enumerate(bk['raw'].splitlines()):
   if i:rr.append(el('br'))
   t=el('t');t.set('{http://www.w3.org/XML/1998/namespace}space','preserve');t.text=line;rr.append(t)
  cap=x.xpath('.//w:p[w:pPr/w:pStyle[@w:val="PMFigureCaption"]]',namespaces=N)[0];refill(cap,bk['caption'])
  fid=re.match(r'^\*?Figure ([\dA-Z]+)\.(\d+)\.',bk['caption']);assert fid,bk['caption'];bk['anchors']+=['fig_'+fid[1].lower()+'_'+fid[2]];stats['source_figure_patterns']+=1
 elif kind=='image':x=cleanmarks(deepcopy(imagep));stats['original_image']+=1
 else:
  x=same(bk)
  if x is not None:
   if kind=='p' and style(x).startswith('PMApplication'):
    x=cleanmarks(deepcopy(templates['Normal']));refill(x,bk['raw']);stats['application_text_mapped_to_body']+=1
   else:cleanmarks(x);stats['exact_text_source_components']+=1
  elif kind=='table':x=table(bk['rows']);stats['source_table_patterns']+=1
  else:
   sk='Heading'+str(min(bk.get('level',1),3)) if kind=='heading' else 'Source' if reference_section[0] else 'PMFigureCaption' if bk['raw'].startswith('*Figure ') else 'Normal'
   x=cleanmarks(deepcopy(templates[sk]));refill(x,bk['raw'],size=18 if sk=='Source' else None);stats['source_paragraph_patterns']+=1
 if kind=='heading':
  pr=x.find('w:pPr',N);sp=pr.find('w:pStyle',N)
  if sp is None:sp=el('pStyle');pr.insert(0,sp)
  sp.set(w('val'),'Heading'+str(min(bk['level'],3)))
  if not bk['anchors']:
   bk['anchors']=['h_'+re.sub(r'[^a-z0-9]+','_',bk['raw'].lower()).strip('_')]
 if kind=='p' and bk['raw'].startswith('*Figure '):
  fid=re.match(r'^\*?Figure ([\dA-Z]+)\.(\d+)\.',bk['raw'])
  if fid:bk['anchors']+=['fig_'+fid[1].lower()+'_'+fid[2]]
 attach(x,bk['anchors']);log.append({'md_line':bk['line'],'kind':kind,'anchors':bk['anchors']});return x

blocks=parse(MD.read_text());start=next(i for i,b in enumerate(blocks) if 'h_preface' in b['anchors']);blocks=blocks[start:];new=[];reference_section=[False];toc=[]
for bk in blocks:
 if 'h_selected_references' in bk['anchors']:reference_section[0]=True
 x=component(bk);new.append(x)
 if bk['kind']=='heading' and (bk['level']==1 or (bk['level']==2 and re.match(r'^(\d+\.|A\.)',bk['raw']))):toc.append((bk['raw'],bk['anchors'][0],bk['level']))
# Preserve cover composition, remove all obsolete editorial/draft/date wording.
cover=[deepcopy(x) for x in orig[:10]]
cover[3]=refill(cover[3],'') # source's unlisted secondary subtitle becomes white space
cover[5]=refill(cover[5],'Ryan Tufts')
cover=[x for i,x in enumerate(cover) if i not in [6,7,8]]
contents=deepcopy(orig[10]);cleanmarks(contents);attach(contents,['contents']);cover.append(contents)
for label,anchor,lev in toc:
 p=deepcopy(templates['PMContentsChapter' if lev==1 else 'PMContents']);pr=p.find('w:pPr',N)
 for child in list(p):
  if child.tag!=w('pPr'):p.remove(child)
 h=el('hyperlink',anchor=anchor);inline(h,label);p.append(h);rr=el('r');rr.append(el('tab'));t=el('t');t.text='1';rr.append(t);p.append(rr);cover.append(p)
for x in list(body):body.remove(x)
for x in cover+new:body.append(x)
body.append(deepcopy(orig[-1]))
# Readability repair carried from reference QA, font and table grid unchanged.
for cell in body.xpath('.//w:tc',namespaces=N):
 if norm(text(cell))=='Engineering stage':
  for side in ['left','right']:
   v=cell.find('w:tcPr/w:tcMar/w:'+side,N)
   if v is not None:v.set(w('w'),'45')
footer=E.fromstring(parts['word/footer5.xml'])
for t in footer.xpath('//w:t',namespaces=N):
 if t.text=='CONSOLIDATED MANUSCRIPT · 3':t.text='PROJECT MANAGEMENT'
settings=E.fromstring(parts['word/settings.xml']);v=settings.find('w:updateFields',N)
if v is None:v=el('updateFields');settings.append(v)
v.set(w('val'),'true')
core=E.fromstring(parts['docProps/core.xml']);NS={'dc':'http://purl.org/dc/elements/1.1/','cp':'http://schemas.openxmlformats.org/package/2006/metadata/core-properties','dcterms':'http://purl.org/dc/terms/'}
for path,value in [('dc:creator','Ryan Tufts'),('dc:subject','A Practical Manual'),('cp:lastModifiedBy','Codex')]:core.find(path,NS).text=value
for path in ['dc:description','cp:version','cp:revision','dcterms:created','dcterms:modified']:
 e=core.find(path,NS)
 if e is not None:core.remove(e)
for f,x in [('word/document.xml',root),('word/_rels/document.xml.rels',rels),('word/settings.xml',settings),('word/footer5.xml',footer),('docProps/core.xml',core)]:parts[f]=E.tostring(x,encoding='UTF-8',xml_declaration=True,standalone=True)
with ZipFile(OUT,'w',ZIP_DEFLATED) as zz:
 for i in z.infolist():zz.writestr(i,parts[i.filename])
(Q/'build-map.json').write_text(json.dumps({'source_sha256':hashlib.sha256(MD.read_bytes()).hexdigest(),'stats':dict(stats),'toc_entries':len(toc),'blocks':log},indent=2));print(OUT,dict(stats),'TOC',len(toc))
