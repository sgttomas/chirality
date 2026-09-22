from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
from lxml import etree as E
from copy import deepcopy
import re,json,hashlib
ROOT=Path('/Users/ryan/.codex/worktrees/da43/chirality'); D=ROOT/'docs/alignment-manual'; QA=Path('/tmp/manual-formats-20260922')
base=D/'Project_Management_for_Human_Agent_Teams_Consolidated_v1.docx'; out=D/'Project_Management_for_Human_Agent_Teams_Consolidated_v2.docx'
z=ZipFile(base);parts={i.filename:z.read(i) for i in z.infolist()}; W='http://schemas.openxmlformats.org/wordprocessingml/2006/main';R='http://schemas.openxmlformats.org/officeDocument/2006/relationships';P='http://schemas.openxmlformats.org/package/2006/relationships';n={'w':W}
def q(s):return '{'+W+'}'+s
def el(s,**attrs):
 e=E.Element(q(s))
 for k,v in attrs.items():e.set(q(k),str(v))
 return e
def txt(e):return ''.join(e.xpath('.//w:t/text()',namespaces=n))
def norm(s):
 s=re.sub(r'\[([^\]]+)\]\([^)]*\)',r'\1',s);s=s.replace('**','').replace('`','').strip('*');return re.sub(r'\s+',' ',s).strip()
r=E.fromstring(parts['word/document.xml']);b=r.find('w:body',n);rels=E.fromstring(parts['word/_rels/document.xml.rels'])
nextrel=max(int(x.get('Id')[3:]) for x in rels)+1; nextbm=max(int(x.get(q('id'))) for x in r.xpath('//w:bookmarkStart',namespaces=n))+1
links={x.get('Target'):x.get('Id') for x in rels if x.get('Type','').endswith('/hyperlink')}
def rel(url):
 global nextrel
 if url not in links:
  rid='rId'+str(nextrel);nextrel+=1;x=E.SubElement(rels,'{'+P+'}Relationship');x.set('Id',rid);x.set('Type',R+'/hyperlink');x.set('Target',url);x.set('TargetMode','External');links[url]=rid
 return links[url]
def inline(parent,s,baseprops=None,flags=()):
 pat=re.compile(r'(`[^`]+`|\*\*[^*]+\*\*|\*[^*]+\*|\[[^\]]+\]\([^)]*\))')
 def run(t,f):
  rr=el('r');rp=deepcopy(baseprops) if baseprops is not None else el('rPr')
  for v in ['b','i','rFonts']:
   if v in ('b','i') and v in f:rp.append(el(v))
  if 'code' in f:
   for old in rp.findall(q('rFonts'))+rp.findall(q('sz')):rp.remove(old)
   rp.append(el('rFonts',ascii='Liberation Mono',hAnsi='Liberation Mono'));rp.append(el('sz',val=15 if small_context[0] else 18))
  rr.append(rp);tt=el('t');tt.set('{http://www.w3.org/XML/1998/namespace}space','preserve');tt.text=t;rr.append(tt);parent.append(rr)
 for token in pat.split(s):
  if not token:continue
  m=re.fullmatch(r'\[([^\]]+)\]\(([^)]*)\)',token)
  if m:
   hh=el('hyperlink'); url=m[2]
   if url.startswith('#'):hh.set(q('anchor'),url[1:])
   else:hh.set('{'+R+'}id',rel(url))
   parent.append(hh);inline(hh,m[1],baseprops,flags)
  elif token.startswith('`') and token.endswith('`'):run(token[1:-1],flags+('code',))
  elif token.startswith('**') and token.endswith('**'):inline(parent,token[2:-2],baseprops,flags+('b',))
  elif token.startswith('*') and token.endswith('*'):inline(parent,token[1:-1],baseprops,flags+('i',))
  else:run(token,flags)
small_context=[False]
def refill(p,md):
 # Keep source paragraph properties and bookmarks, replace only run content.
 props=None
 for rr in p.findall('w:r',n):
  rp=rr.find('w:rPr',n)
  if rp is not None and rp.find('w:b',n) is None and rp.find('w:rFonts',n) is None:props=deepcopy(rp);break
 if props is None:props=el('rPr')
 small_context[0]=bool(p.xpath('./w:pPr/w:spacing[@w:line="220"]',namespaces=n))
 if small_context[0] and props.find('w:sz',n) is None:props.append(el('sz',val=18))
 for c in list(p):
  if E.QName(c).localname not in ['pPr','bookmarkStart','bookmarkEnd']:p.remove(c)
 if small_context[0]:md=re.sub(r'^(\[\d+\] [^.]+\.)',r'**\1**',md)
 inline(p,md,props)
 return p
def clonep(template,md):
 p=deepcopy(template)
 for bm in p.xpath('.//w:bookmarkStart|.//w:bookmarkEnd',namespaces=n):bm.getparent().remove(bm)
 return refill(p,md)
normal=deepcopy(next(p for p in b if E.QName(p).localname=='p' and txt(p).startswith('Actual projects use')))
heading=deepcopy(next(p for p in b if p.xpath('./w:pPr/w:pStyle[@w:val="Heading2"]',namespaces=n)))
def bookmark(p,name):
 global nextbm
 st=el('bookmarkStart',id=nextbm,name=name);en=el('bookmarkEnd',id=nextbm);nextbm+=1;p.insert(1,st);p.append(en)
def make_table(lines):
 rows=[[x.strip() for x in a.strip().strip('|').split('|')] for a in lines];rows=[rows[0]]+rows[2:]
 template=deepcopy(r.xpath('//w:tbl',namespaces=n)[0]);ts=template.findall('w:tr',n);head=deepcopy(ts[0]);row=deepcopy(ts[1])
 for tr in ts:template.remove(tr)
 widths=[900,2850,3997]
 for gc,width in zip(template.findall('w:tblGrid/w:gridCol',n),widths):gc.set(q('w'),str(width))
 for i,cells in enumerate(rows):
  tr=deepcopy(head if i==0 else row)
  for tc,text,width in zip(tr.findall('w:tc',n),cells,widths):
   tc.find('w:tcPr/w:tcW',n).set(q('w'),str(width));p=tc.find('w:p',n);refill(p,('**'+text+'**') if i==0 else text)
  template.append(tr)
 return template
def blocks(md,template):
 result=[];pending=None;lines=md.splitlines();i=0
 while i<len(lines):
  line=lines[i].strip();i+=1
  if not line:continue
  if line.startswith('<a '):pending=re.search('id="([^"]+)"',line)[1];continue
  if line.startswith('## '):p=clonep(heading,line[3:])
  elif line.startswith('|'):
   tbl=[line]
   while i<len(lines) and lines[i].strip().startswith('|'):tbl.append(lines[i]);i+=1
   result.append(make_table(tbl));continue
  else:p=clonep(template,line)
  if pending:bookmark(p,pending);pending=None
  result.append(p)
 return result
m=json.loads((ROOT/'plans/evidence/2026-09-22_alignment_manual/v2-edit-manifest.json').read_text());oldmd=(D/m['input'].split('/')[-1]).read_text();newmd=(D/m['output'].split('/')[-1]).read_text()
assert hashlib.sha256(oldmd.encode()).hexdigest()==m['input_sha256']; assert hashlib.sha256(newmd.encode()).hexdigest()==m['output_sha256']
oldlines=oldmd.splitlines();rebuilt=oldlines.copy()
for op in reversed(m['operations']):assert oldlines[op['v1_line']-1]==op['old'];rebuilt[op['v1_line']-1:op['v1_line']]=op['new'].splitlines()
assert '\n'.join(rebuilt)+'\n'==newmd
log=[]
for idx,op in enumerate(m['operations']):
 if idx<3:continue
 if op['old'].startswith('|'):
  cells=[norm(s) for s in op['old'].strip('|').split('|')]; trs=[t for t in r.xpath('//w:tr',namespaces=n) if [norm(txt(c)) for c in t.findall('w:tc',n)]==cells];assert len(trs)==1,(idx,len(trs));tr=trs[0];parent=tr.getparent();pos=parent.index(tr)
  for j,line in enumerate(op['new'].splitlines()):
   newtr=deepcopy(tr)
   for tc,s in zip(newtr.findall('w:tc',n),line.strip('|').split('|')):refill(tc.find('w:p',n),s.strip())
   parent.insert(pos+j,newtr)
  parent.remove(tr);log.append({'operation':idx,'table_row':cells[0]});continue
 ps=[p for p in r.xpath('//w:body//w:p',namespaces=n) if norm(txt(p))==norm(op['old'])];assert len(ps)==1,(idx,len(ps));p=ps[0];parent=p.getparent();pos=parent.index(p)
 new=blocks(op['new'],p)
 # Keep bookmarks attached to original paragraph, particularly captions.
 for mark in p.xpath('./w:bookmarkStart|./w:bookmarkEnd',namespaces=n):new[0].append(deepcopy(mark))
 for j,v in enumerate(new):parent.insert(pos+j,v)
 parent.remove(p);log.append({'operation':idx,'source_paragraph':op['v1_line'],'new_blocks':len(new)})
# Edition cover, footer, and revision paragraph. Preserve source cover composition.
for t in r.xpath('//w:t',namespaces=n):
 if t.text=='CONSOLIDATED MANUSCRIPT · EDITION 1':t.text=t.text.replace('EDITION 1','EDITION 2')
pref=next(p for p in b if p.xpath('./w:bookmarkStart[@w:name="h_preface"]',namespaces=n));note=m['operations'][1]['new'].split('\n\n')[1];b.insert(b.index(pref)+1,clonep(normal,note))
# Contents entry for repository application.
contents=next(p for p in b if p.xpath('./w:hyperlink[@w:anchor="h_preface"]',namespaces=n));entry=deepcopy(contents);entry.find('w:pPr/w:pStyle',n).set(q('val'),'PMContents');entry.find('w:hyperlink',n).set(q('anchor'),'h_repository_application');entry.find('w:hyperlink/w:r/w:t',n).text='Repository application and source standing';b.insert(b.index(contents)+1,entry)
# Canonical simple PAGE footer field retained, edition label changed.
f=E.fromstring(parts['word/footer5.xml'])
for t in f.xpath('//w:t',namespaces=n):
 if t.text=='CONSOLIDATED MANUSCRIPT · 1':t.text='CONSOLIDATED MANUSCRIPT · 2'
settings=E.fromstring(parts['word/settings.xml']);uf=settings.find('w:updateFields',n)
if uf is None:uf=el('updateFields');settings.append(uf)
uf.set(q('val'),'true')
for name,tree in [('word/document.xml',r),('word/footer5.xml',f),('word/settings.xml',settings),('word/_rels/document.xml.rels',rels)]:parts[name]=E.tostring(tree,xml_declaration=True,encoding='UTF-8',standalone=True)
with ZipFile(out,'w',ZIP_DEFLATED) as zz:
 for i in z.infolist():zz.writestr(i,parts[i.filename])
(QA/'patch-log.json').write_text(json.dumps(log,indent=2));print(out)
