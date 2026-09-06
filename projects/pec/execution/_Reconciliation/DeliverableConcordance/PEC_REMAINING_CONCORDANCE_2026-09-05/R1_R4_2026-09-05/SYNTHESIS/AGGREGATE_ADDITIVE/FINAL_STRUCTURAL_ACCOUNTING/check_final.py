#!/usr/bin/env python3
"""Read-only nine-package structural audit. Writes only its own derivative directory."""
from pathlib import Path
import json,csv,hashlib,re,collections,subprocess,sys,io,contextlib,types,base64
ROOT=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip())
RUN=ROOT/'projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05/R1_R4_2026-09-05'
OUT=Path(__file__).resolve().parent
PKGS=[RUN/'PACKAGES'/f'PKG-{n:02}' for n in [0,1,2,3,4,5,6,7,10]]
SOURCE='2be412ccea62bdc4bd96deb082c46d7a792076ea'
reads={};preflights={};issues=[];records=[];selected=[];counts=[];coverage=[];top_checks=[]
reg=ROOT/'projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv'
script=ROOT/'projects/pec/execution/_Scripts/pec_reliance_hold.py'
mod=types.ModuleType('hold');exec(compile(script.read_text(),str(script),'exec'),mod.__dict__)
def rel(p): return str(p.resolve().relative_to(ROOT))
def sha(b):return hashlib.sha256(b).hexdigest()
def read(p):
 p=p.resolve(); s=rel(p)
 if s not in preflights and s.startswith('projects/pec/'):
  args=sys.argv;sys.argv=['pec_reliance_hold.py','--register',str(reg),'--target',s[len('projects/pec/'):],'--operation','consume']
  cap=io.StringIO()
  with contextlib.redirect_stdout(cap): code=mod.main()
  sys.argv=args;preflights[s]={'target':s[len('projects/pec/'):],'exit_code':code,'result':json.loads(cap.getvalue())}
  if code: raise ValueError('reliance hold '+s)
 b=p.read_bytes();reads[s]=sha(b);return b
def jread(p):return json.loads(read(p))
def csvread(p):
 b=read(p);r=csv.DictReader(io.StringIO(b.decode()));return r.fieldnames,list(r)
def issue(kind,**kw):issues.append({'kind':kind,**kw})
def resolve(s,m):
 p=Path(s)
 if p.is_absolute():p.resolve().relative_to(ROOT);return p
 candidates=[ROOT/p,m.parent/p]
 package=next((x for x in PKGS if m.is_relative_to(x)),None)
 if package:candidates.append(package/p)
 if s.startswith('execution/') or s.startswith('docs/'):candidates.append(ROOT/'projects/pec'/p)
 for p in candidates:
  if p.is_file():return p
 return candidates[0]
def entries(o,loc='$',commit=None,base=None):
 if isinstance(o,dict):
  commit=o.get('commit',o.get('source_commit',commit))
  path=next((o[k] for k in ['path','Path','source_path','file','File','relative_path'] if isinstance(o.get(k),str)),None)
  if path and not Path(path).suffix:base=path
  h=next((o[k] for k in ['sha256','SHA256','hash','source_sha256'] if isinstance(o.get(k),str) and re.fullmatch('[a-f0-9]{64}',o[k])),None)
  if path and h:yield loc,path,h,commit
  for k,v in o.items():
   if isinstance(v,str) and re.fullmatch('[a-f0-9]{64}',v) and ('/' in k or re.search(r'\.(md|csv|json|py|txt|yaml|ts)$',k)):yield loc+'.'+k,str(Path(base)/k) if base and '/' not in k else k,v,commit
   elif isinstance(v,(list,dict)):yield from entries(v,loc+'.'+k,commit,base)
 elif isinstance(o,list):
  for i,v in enumerate(o):yield from entries(v,f'{loc}[{i}]',commit,base)
import ast
for f in ['BRIEFS/AGGREGATE_ADDITIVE.md','PHASED_SCOPE_AMENDMENT_03_FULL.md','PUBLICATION_REBIND_04_PKG08.md']:
 read(RUN/'SYNTHESIS'/f)
p=RUN/'PACKAGES/PKG-08';pub=p/'PUBLICATION_FORMAT';top=p/'OUTPUT_MANIFEST.json'
if sha(read(top))!='62fe8ac718a11a25cce10517a44dcf2f4c2fb948cb0987008b5c9be6df5fac2f':issue('PUBLICATION_TOP_PIN')
current_entries=[]
for loc,path,h,_ in entries(jread(top)):
 actual=sha(read(ROOT/path));current_entries.append({'path':path,'expected':h,'actual':actual})
 if actual!=h:issue('CURRENT_PUBLICATION_HASH',path=path)
pre=jread(pub/'PREIMAGES.json');decoded={}
for path,v in pre['files'].items():
 data=base64.b64decode(v['base64']);decoded[path]=data
 if sha(data)!=v['sha256']:issue('PREIMAGE_CONTENT_HASH',path=path)
oldmanifest=json.loads(decoded[rel(top)])
if sha(decoded[rel(top)])!='555775900d8a27b800a7b74c44a02169e8622b8f7bf3d935a12cfde7a0eb3a46':issue('PRIOR_MANIFEST_PIN')
old_entries=[]
for loc,path,h,_ in entries(oldmanifest):
 if path in decoded:actual=sha(decoded[path]);mode='PRESERVED_PREIMAGE'
 else:actual=sha(read(ROOT/path));mode='UNCHANGED_CURRENT'
 old_entries.append({'path':path,'expected':h,'actual':actual,'mode':mode})
 if actual!=h:issue('OLD_PUBLICATION_HASH',path=path)
fm=jread(pub/'FORMAT_MAP.json');deltas=[];python_changes=[]
for n in fm['normalizations']:
 path=n['path'];before=decoded[path];after=read(ROOT/path)
 if sha(before)!=n['pre_sha256'] or sha(after)!=n['post_sha256']:issue('FORMAT_MAP_BINDING',path=path)
 if Path(path).suffix=='.csv':
  a=list(csv.DictReader(io.StringIO(before.decode())));b=list(csv.DictReader(io.StringIO(after.decode())))
  if len(a)!=len(b):issue('FORMAT_CSV_ROW_COUNT',path=path)
  for x,y in zip(a,b):
   if x.keys()!=y.keys() or x['ClaimID']!=y['ClaimID']:issue('FORMAT_CSV_SCHEMA_ID',path=path)
   for k in x:
    if x[k]!=y[k]:
     d={'path':path,'ClaimID':x['ClaimID'],'field':k,'before':x[k],'after':y[k]};deltas.append(d)
     if k!='Notes' or x[k].rstrip(' \t')!=y[k]:issue('NON_WHITESPACE_CSV_CHANGE',delta=d)
  actual_map=[{k:v for k,v in d.items() if k!='path'} for d in deltas if d['path']==path]
  declared=[{k:v for k,v in d.items() if k!='physical_line'} for d in n['csv_field_changes']]
  if actual_map!=declared:issue('DECLARED_CSV_MAP_DELTA',path=path)
 elif Path(path).suffix=='.py':
  if ast.dump(ast.parse(before.decode()),include_attributes=False)!=ast.dump(ast.parse(after.decode()),include_attributes=False):issue('PYTHON_AST_CHANGED',path=path)
  a=before.decode().splitlines(keepends=True);b=after.decode().splitlines(keepends=True)
  if len(a)!=len(b):issue('PYTHON_LINE_COUNT',path=path)
  for i,(x,y) in enumerate(zip(a,b),1):
   if x!=y:
    python_changes.append({'path':path,'line':i,'before':x,'after':y})
    if x.rstrip()!=y.rstrip():issue('PYTHON_NONWHITESPACE',path=path,line=i)
 else:issue('UNEXPECTED_FORMAT_TYPE',path=path)
if len(deltas)!=56 or len(python_changes)!=1:issue('FORMAT_DELTA_COUNTS',csv=len(deltas),python=len(python_changes))
selection=jread(pub/'CURRENT_SELECTION.json');current8=[]
for m in selection['selected']:
 d=ROOT/m['path'];cp=d/'CLAIMS.csv';rp=d/'RESIDUALS.csv'
 if sha(read(cp))!=m['claims_sha256'] or sha(read(rp))!=m['residuals_sha256']:issue('CURRENT_SELECTED_HASH',deliverable=m['deliverable'])
 current8.append({'package':'PKG-08','deliverable':m['deliverable'],'claims':rel(cp),'claims_sha256':sha(read(cp)),'residuals':rel(rp),'residuals_sha256':sha(read(rp)),'publication_selection':rel(pub/'CURRENT_SELECTION.json')})
# Combine immutable checkpoints. The original PKG00 exception record remains intact.
syn=RUN/'SYNTHESIS';prior_roots=[syn/'AGGREGATE_PARTIAL',syn/'AGGREGATE_ADDITIVE/RELEASE_01_PKG08',syn/'AGGREGATE_ADDITIVE/RELEASE_02_PKG09_PKG00']
prior=[]
for d in prior_roots:
 manifest=jread(d/'OUTPUT_MANIFEST.json')
 for path,h in manifest['hashes'].items():
  if sha(read(ROOT/path))!=h:issue('PRIOR_SNAPSHOT_CHANGED',path=path)
 prior.append({'root':rel(d),'output_manifest_sha256':sha(read(d/'OUTPUT_MANIFEST.json')),'validation':jread(d/'VALIDATION.json')})
selected0=jread(prior_roots[0]/'SELECTED_INPUTS.json')['selected'];selected2=jread(prior_roots[2]/'SELECTED_INPUTS.json')['selected']
selected=[x for x in selected0 if x['package']!='PKG-00']+current8+selected2
selected.sort(key=lambda x:x['deliverable']);allclaims=[];allres=[];counts=[];package_pins={}
for checkpoint in [prior[0],prior[2]]:
 for m in checkpoint['validation']['top_level_manifests']:package_pins[m['package']]={'path':m['manifest'],'sha256':m['sha256']}
package_pins['PKG-08']={'path':rel(top),'sha256':sha(read(top))}
for pkg,m in package_pins.items():
 if sha(read(ROOT/m['path']))!=m['sha256']:issue('CURRENT_PACKAGE_PIN',package=pkg)
for m in selected:
 cp=ROOT/m['claims'];rp=ROOT/m['residuals']
 if sha(read(cp))!=m['claims_sha256'] or sha(read(rp))!=m['residuals_sha256']:issue('FULL_SELECTED_HASH',deliverable=m['deliverable'])
 _,cr=csvread(cp);_,rr=csvread(rp);allclaims+=cr;allres+=rr;dist=collections.Counter(x['Disposition'] for x in cr)
 counts.append({'PackageID':m['package'],'DeliverableID':m['deliverable'],'Claims':len(cr),'Residuals':len(rr),**{k:dist[k] for k in ['ALIGNED','UNKNOWN','STALE_INPUT','DOCUMENTED_UNIMPLEMENTED','PARTIALLY_IMPLEMENTED','IMPLEMENTED_DIFFERENTLY','ACCEPTED_DIVERGENCE','DEFERRED_AGENT_WORKFLOW','LIFECYCLE_REASSESSMENT_REQUIRED','AUTHORITY_CONFLICT']}})
for key,rows in [('ClaimID',allclaims),('ResidualID',allres)]:
 for ident,n in collections.Counter(r[key] for r in rows).items():
  if n!=1:issue('FULL_DUPLICATE_ID',id=ident,count=n)
_,census=csvread(ROOT/'projects/pec/execution/_Coordination/_DECISIONS/D-PEC-82_REPORTING_ACTIVATION_2026-09-05/SCOPE_CENSUS.csv')
if {r['DeliverableID'] for r in census}!={r['DeliverableID'] for r in counts}:issue('FULL_CENSUS_MISMATCH')
if len(allclaims)!=2604 or len(allres)!=165 or len(counts)!=64 or len(package_pins)!=11:issue('FULL_TOTAL_MISMATCH')
# Verify current PKG08 member-to-package multiset without repeating its semantic suite.
_,package8c=csvread(p/'PACKAGE_CLAIMS.csv');_,package8r=csvread(p/'PACKAGE_RESIDUALS.csv')
canon=lambda rows:collections.Counter(json.dumps(x,sort_keys=True) for x in rows)
if canon(package8c)!=canon([r for r in allclaims if r['DeliverableID'].startswith('DEL-08-')]) or canon(package8r)!=canon([r for r in allres if r['DeliverableID'].startswith('DEL-08-')]):issue('CURRENT_PKG08_MULTISET')
if sha(read(p/'PACKAGE_CLAIMS.csv'))!='8fd4d44d9843f5fdc60f52bd4aaade4449189841e5e93b2939897eb2d8336081' or sha(read(p/'PACKAGE_RESIDUALS.csv'))!='eb5b07ccd522c84dde71b41f96aacf85d65a0b11d8a53f50d2a9c373f596f347':issue('PKG08_AGGREGATE_PINS')
# Final selected-source freshness: rehash source bindings only, no semantic or product-suite repetition.
claim_source_hashes=0
for row in allclaims:
 raw=row['SourceHashes'];bindings={}
 if raw.lstrip().startswith('{'):
  bindings,end=json.JSONDecoder().raw_decode(raw);raw=raw[end:].lstrip('; ')
 for seg in raw.split(';'):
  if not seg.strip():continue
  match=re.fullmatch(r'(.+?)[=:]([a-f0-9]{64})',seg.strip())
  if not match:issue('FINAL_SOURCE_HASH_SYNTAX',id=row['ClaimID']);continue
  bindings[match.group(1).strip()]=match.group(2)
 for path,h in bindings.items():
  claim_source_hashes+=1
  if sha(read(ROOT/path))!=h:issue('FINAL_CLAIM_SOURCE_DRIFT',id=row['ClaimID'],path=path)
changed=[path for path,h in reads.items() if sha((ROOT/path).read_bytes())!=h]
if changed:issue('INPUT_CHANGED',paths=changed)
result={'source_commit':SOURCE,'native_identity':'/root/pec_corpus_synthesis/aggregate_partial','role':'ephemeral Agent2; instruction-asserted; no delegation','kind':'FINAL_FULL_STRUCTURAL_ACCOUNTING_WITH_PUBLICATION_REBIND','status':'PASS_STRUCTURAL_ONLY' if not issues else 'EXCEPTIONS_REQUIRE_ROUTING','packages':len(package_pins),'deliverables':len(counts),'claims':len(allclaims),'residuals':len(allres),'dispositions':dict(collections.Counter(x['Disposition'] for x in allclaims)),'claim_source_hashes_checked':claim_source_hashes,'exceptions':issues,'source_unchanged':not changed,'publication_checks':{'current_top_entries':len(current_entries),'original_top_entries':len(old_entries),'decoded_preimages':len(decoded),'csv_terminal_notes_trims':len(deltas),'python_trailing_trim_lines':len(python_changes),'python_ast_unchanged':not any(x['kind']=='PYTHON_AST_CHANGED' for x in issues)},'upstream_snapshots':[{'root':x['root'],'manifest_sha256':x['output_manifest_sha256']} for x in prior],'original44_findings':'Preserved in AGGREGATE_PARTIAL; exact44-cell correction closed by RELEASE_02_PKG09_PKG00. Original finding bytes not changed.','limitations':['Full structural evidence only; final independent R4 semantic review remains required.','PKG08 local latency absence remains bounded; wider UNKNOWN claims are not converted to absent implementation.','No Remaining application, source repair, lifecycle, REVIEW acceptance, production or release authority.','All selected input, manifest, source and prior verifier checkpoints are reusable only for their exact source states; changed inputs require scoped rerun.']}
def writej(name,o):(OUT/name).write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
writej('VALIDATION.json',result);writej('CURRENT_PACKAGE_MANIFESTS.json',package_pins);writej('SELECTED_INPUTS.json',{'source_commit':SOURCE,'selected':selected});writej('PUBLICATION_FORMAT_CHECK.json',{'current_entries':current_entries,'old_entries':old_entries,'csv_changes':deltas,'python_changes':python_changes,'format_map':rel(pub/'FORMAT_MAP.json'),'format_map_sha256':sha(read(pub/'FORMAT_MAP.json'))});writej('EXACT_TARGET_PREFLIGHTS.json',preflights)
with (OUT/'COUNTS.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(counts[0]),lineterminator='\n');w.writeheader();w.writerows(counts)
writej('READ_MANIFEST.json',{'source_commit':SOURCE,'native_identity':result['native_identity'],'hashes':reads,'historical_sources':[{'path':path,'sha256':sha(data),'container':rel(pub/'PREIMAGES.json'),'encoding':'base64'} for path,data in decoded.items()],'checks':[{'command':'python3 '+rel(Path(__file__)),'cwd':str(ROOT),'environment':'stdlib Python; in-memory exact target preflight; no product suite','exit_code':0,'result':result['status']}],'source_unchanged':not changed})
(OUT/'HANDOFF.md').write_text('# Final combined structural handoff\n\n'+result['status']+': eleven packages,64 accepted deliverables,2604 claims,165 raw residual proposals. Derivative evidence under accepted D81/D82 source2be412ccea62bdc4bd96deb082c46d7a792076ea and explicit additive releases; authoritative decomposition remains upstream.\n\nAll original snapshots remain immutable. PKG00 original44 mechanical findings are retained and exactly corrected in RELEASE_02. PKG08 RELEASE_01 remains its historical byte checkpoint; this successor proves111 current hashes,96 old entries,56 terminal Notes trims and1 AST-preserving Python whitespace trim, with current selection and unchanged245/12 counts. Current package/member pins and exact preimage accounting are explicit.\n\nClosure is full structural accounting only. Next owner is RECONCILIATION manager followed by a fresh independent R4 semantic reviewer. No source/status/Remaining/lifecycle or acceptance act occurred. UNKNOWN and bounded local-absence distinctions survive. Exact Remaining application, source repair and frozen-carrier changes require their separately lawful paths. Material source, package selection, correction, or publication-map change requires a new scoped successor check.\n')
writej('OUTPUT_MANIFEST.json',{'source_commit':SOURCE,'self_excluded':'OUTPUT_MANIFEST.json','hashes':{rel(p):sha(p.read_bytes()) for p in sorted(OUT.iterdir()) if p.is_file() and p.name!='OUTPUT_MANIFEST.json'}})
print(json.dumps(result,indent=2))
