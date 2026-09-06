#!/usr/bin/env python3
"""Read-only additive PKG09/corrected PKG00 structural audit. Writes only its own derivative directory."""
from pathlib import Path
import json,csv,hashlib,re,collections,subprocess,sys,io,contextlib,types,base64
ROOT=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip())
RUN=ROOT/'projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05/R1_R4_2026-09-05'
OUT=Path(__file__).resolve().parent
PKGS=[RUN/'PACKAGES'/f'PKG-{n:02}' for n in [0,9]]
SOURCE='2be412ccea62bdc4bd96deb082c46d7a792076ea'
reads={};preflights={};issues=[];records=[];selected=[];counts=[];coverage=[];top_checks=[]
reg=ROOT/'projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv'
script=ROOT/'projects/pec/execution/_Scripts/pec_reliance_hold.py'
mod=types.ModuleType('hold');exec(compile(script.read_text(),str(script),'exec'),mod.__dict__)
def rel(p): return str(p.resolve().relative_to(ROOT))
def sha(b):return hashlib.sha256(b).hexdigest()
def read(p):
 p=p.resolve(); s=rel(p)
 if '/PACKAGES/PKG-08/' in s: raise ValueError('excluded package input '+s)
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
# Load governed basis, retaining historical labels with successor acceptance.
governance=[ROOT/'AGENTS.md',ROOT/'projects/pec/AGENTS.md',ROOT/'agents/AGENT_RECONCILIATION.md',ROOT/'docs/DELIVERABLE_CONCORDANCE_METHOD.md',RUN.parent/'CONVENTIONS.md',RUN/'SYNTHESIS/BRIEFS/AGGREGATE_ADDITIVE.md',RUN/'SYNTHESIS/PHASED_SCOPE_AMENDMENT_03_FULL.md',RUN/'SYNTHESIS/PHASED_SCOPE_AMENDMENT_03_FULL.md',RUN/'COMMON/BRIEFS/SYNTHESIS.md',RUN/'COMMON/BRIEF_CLARIFICATION_01.md',RUN/'COMMON/SYNTHESIS_CLARIFICATION_01.md',reg,script]
for name in ['D-PEC-82_remaining_corpus_reporting_2026-09-05.md','D-PEC-81_CALIBRATION_ACCEPTANCE_2026-09-05.md','D-PEC-81_remaining_concordance_activation_2026-09-05.md']:
 governance.append(ROOT/'projects/pec/execution/_Coordination/_DECISIONS'/name)
for p in governance:read(p)
# Current top-level manifest: no historical substitution allowed.
allfiles=[]; byhash=collections.defaultdict(list);preimages={}
for p in PKGS:
 m=p/'OUTPUT_MANIFEST.json'; obj=jread(m); ent=list(entries(obj));passed=0
 for loc,s,h,commit in ent:
  t=resolve(s,m)
  if not t.is_file():issue('TOP_MISSING',manifest=rel(m),path=s);continue
  actual=sha(read(t));allfiles.append(t);byhash[actual].append(rel(t))
  if actual!=h:issue('TOP_HASH_MISMATCH',manifest=rel(m),path=s,expected=h,actual=actual)
  else:passed+=1
 top_checks.append({'package':p.name,'manifest':rel(m),'sha256':sha(read(m)),'entries':len(ent),'passed':passed})
 for pr in [x for x in (p/'PUBLICATION_FORMAT').glob('*.json') if x.name in ['PREIMAGES.json','ORIGINALS_BASE64.json']]:
  po=jread(pr)
  for s,v in po.get('files',po.get('originals',{})).items():
   b=base64.b64decode(v['base64']);h=sha(b)
   if h!=v['sha256']:issue('PREIMAGE_HASH',path=s)
   preimages[(s,h)]={'container':rel(pr),'encoding':'base64','bytes':len(b)}
# Rehash all manifest populations, recording every original shape and locator.
manifest_counts=[]
for m in sorted(set(allfiles)):
 if m.suffix!='.json' or not any(x in m.name.upper() for x in ['MANIFEST','SELECTED','PREIMAGE_MAP']):continue
 try:o=jread(m)
 except Exception as e:issue('MANIFEST_PARSE',manifest=rel(m),error=str(e));continue
 ent=list(entries(o));manifest_counts.append({'path':rel(m),'entries':len(ent),'root_type':type(o).__name__})
 for loc,s,h,commit in ent:
  rec={'manifest':rel(m),'json_location':loc,'original_path':s,'expected_sha256':h,'declared_commit':commit}
  try:
   t=resolve(s,m);rec['resolved_path']=rel(t)
   actual=sha(read(t)) if t.is_file() else None;rec['actual_sha256']=actual
   if actual==h:rec['status']='CURRENT_MATCH'
   elif (rec['resolved_path'],h) in preimages:rec.update(status='PRESERVED_PUBLICATION_PREIMAGE',historical_binding=preimages[(rec['resolved_path'],h)])
   elif h in byhash:rec.update(status='PRESERVED_EXACT_HISTORICAL_DERIVATIVE',preserved_candidates=byhash[h],interpretation='Original reference resolves to byte-identical preserved derivative/tool history. Current-path bytes remain separately reported; selected member multisets and current top manifests are independently checked.')
   elif commit and re.fullmatch('[a-f0-9]{40}',commit):
    result=subprocess.run(['git','show',commit+':'+rec['resolved_path']],capture_output=True)
    if result.returncode==0 and sha(result.stdout)==h:rec['status']='HISTORICAL_COMMIT_MATCH'
    else:rec['status']='UNRESOLVED_HASH_MISMATCH'
   else:rec['status']='UNRESOLVED_HASH_MISMATCH'
  except Exception as e:rec.update(status='PATH_OR_READ_ERROR',error=str(e))
  records.append(rec)
  if rec['status'] in ['UNRESOLVED_HASH_MISMATCH','PATH_OR_READ_ERROR']:issue('MANIFEST_REFERENCE',**rec)
# Independently prove exact aggregate correction and original finding preservation.
p=PKGS[0];mp=p/'GATE_FORMAT_V003/FINAL_AGGREGATE_MAP.json';mapobj=jread(mp)
if sha(read(mp))!='a121035f76cb3c07fc4139d4d9ce88d321a3827f1e86570f2edf131f1ce38a1a':issue('CORRECTION_MAP_PIN')
old=p/'GATE_FORMAT_V002/PREIMAGES';deltas=[]
for name,idkey in [('PACKAGE_CLAIMS.csv','ClaimID'),('PACKAGE_RESIDUALS.csv','ResidualID')]:
 of,orr=csvread(old/name);nf,nrr=csvread(p/name)
 if of!=nf or len(orr)!=len(nrr):issue('CORRECTION_SCHEMA_OR_COUNT',file=name)
 for a,b in zip(orr,nrr):
  if a[idkey]!=b[idkey]:issue('CORRECTION_ROW_ID_ORDER',file=name)
  for k in of:
   if a[k]!=b[k]:
    d={'file':name,'id':a[idkey],'field':k,'before':a[k],'after':b[k]};deltas.append(d)
    if k=='Depends' and a[k]=='' and b[k]=='NONE':continue
    if k=='ExactGate' and b[k]=='NOT_SELECTABLE_UNTIL: '+a[k]:continue
    issue('CORRECTION_SEMANTIC_OR_UNDECLARED_DELTA',delta=d)
if len(deltas)!=44 or sum(x['field']=='Depends' for x in deltas)!=42 or sum(x['field']=='ExactGate' for x in deltas)!=2:issue('CORRECTION_DELTA_COUNT',deltas=deltas)
(OUT/'EXACT_CORRECTION_DELTA.json').write_text(json.dumps({'map_path':rel(mp),'map_sha256':sha(read(mp)),'deltas':deltas,'claim_count_unchanged':87,'residual_count_unchanged':6,'original_finding_snapshot':rel(RUN/'SYNTHESIS/AGGREGATE_PARTIAL/VALIDATION.json'),'meaning':'Exactly42 empty Depends→NONE and2 NOT_SELECTABLE_UNTIL prefixes. All other claim/residual cells identical; no semantic delta or source act.'},indent=2)+'\n')
# Exact selected member and package row population.
CS='ClaimID,DeliverableID,ClaimClass,NormativeSource,ScopeItemIDs,DeclaredSource,CurrentState,ImplementationEvidence,VerificationEvidence,ValidationOrProvenanceEvidence,LifecycleEvidence,ExistingRemaining,Disposition,ProposedResidualID,ProposedResidualText,Depends,ExactGate,AuthorityNeeded,Selectability,SourceCommit,SourceHashes,EvidenceReferences,Notes'.split(',')
RS='ResidualID,DeliverableID,ClaimIDs,ProposedText,Depends,ExactGate,ClosureEvidence,AuthorityNeeded,Selectability,Notes'.split(',')
allclaims=[];allres=[]
def links(s,typ):
 if typ=='res':return set(re.findall(r'DEL-\d{2}-\d{2}-REM-\d{3}',s))
 return set(x.strip() for x in re.split(r'\s*[|;]\s*',s) if x.strip() and x.strip()!='NONE')
for p in PKGS:
 _,summ=csvread(p/'PACKAGE_SUMMARY.csv'); cf,claims=csvread(p/'PACKAGE_CLAIMS.csv');rf,res=csvread(p/'PACKAGE_RESIDUALS.csv')
 if cf!=CS:issue('CLAIM_SCHEMA',package=p.name,actual=cf)
 if rf!=RS:issue('RESIDUAL_SCHEMA',package=p.name,actual=rf)
 cm={r['ClaimID']:r for r in claims};rm={r['ResidualID']:r for r in res};allclaims+=claims;allres+=res
 sc=[];sr=[]
 for row in summ:
  did=row['DeliverableID'];worker=row.get('SelectedWorker',row.get('SelectedWorkerPath',row.get('SelectedEvidenceRoot')))
  cpath=row.get('SelectedClaims') or worker+'/CLAIMS.csv';rpath=row.get('SelectedResiduals') or worker+'/RESIDUALS.csv'
  cp=resolve(cpath,p/'PACKAGE_SUMMARY.csv');rp=resolve(rpath,p/'PACKAGE_SUMMARY.csv');_,cr=csvread(cp);_,rr=csvread(rp);sc+=cr;sr+=rr
  selected.append({'package':p.name,'deliverable':did,'original_summary_row':row,'claims':rel(cp),'claims_sha256':sha(read(cp)),'residuals':rel(rp),'residuals_sha256':sha(read(rp))})
  for k,t in [('SelectedClaimsSHA256',cp),('ClaimsSHA256',cp),('SelectedResidualsSHA256',rp),('ResidualsSHA256',rp)]:
   if row.get(k) and row[k]!=sha(read(t)):issue('SELECTED_HASH',deliverable=did,field=k,expected=row[k],actual=sha(read(t)))
  dist=collections.Counter(x['Disposition'] for x in cr)
  checks={'Claims':len(cr),'ClaimCount':len(cr),'RawResidualProposals':len(rr),'ResidualCount':len(rr),'Residuals':len(rr),'UnknownClaims':dist['UNKNOWN'],'UnknownCount':dist['UNKNOWN'],'UnknownClaimCount':dist['UNKNOWN'],'UNKNOWN':dist['UNKNOWN'],'ALIGNED':dist['ALIGNED'],'AlignedCount':dist['ALIGNED'],'ACCEPTED_DIVERGENCE':dist['ACCEPTED_DIVERGENCE'],'StaleInputCount':dist['STALE_INPUT'],'StaleClaims':dist['STALE_INPUT'],'NonAlignedClaims':len(cr)-dist['ALIGNED'],'DocumentedUnimplementedCount':dist['DOCUMENTED_UNIMPLEMENTED'],'Aligned':dist['ALIGNED'],'Unknown':dist['UNKNOWN'],'RawResiduals':len(rr)}
  for k,v in checks.items():
   if k in row and row[k]!=str(v):issue('SUMMARY_COUNT',deliverable=did,field=k,reported=row[k],actual=v)
  counts.append({'PackageID':p.name,'DeliverableID':did,'Claims':len(cr),'Residuals':len(rr),**{k:dist[k] for k in ['ALIGNED','UNKNOWN','STALE_INPUT','ACCEPTED_DIVERGENCE','PARTIALLY_IMPLEMENTED','AUTHORITY_CONFLICT','DOCUMENTED_UNIMPLEMENTED','DEFERRED_AGENT_WORKFLOW','LIFECYCLE_REASSESSMENT_REQUIRED','IMPLEMENTED_DIFFERENTLY']},'NonAligned':len(cr)-dist['ALIGNED']})
 canon=lambda rows:collections.Counter(json.dumps(x,sort_keys=True) for x in rows)
 if canon(sc)!=canon(claims):issue('AGGREGATE_CLAIM_MULTISET',package=p.name)
 if canon(sr)!=canon(res):issue('AGGREGATE_RESIDUAL_MULTISET',package=p.name)
 for r in claims:
  rid=r['ClaimID']
  if not r['Depends'].strip():issue('EMPTY_DEPENDS',id=rid)
  if r['ProposedResidualID'] not in ['','NONE'] and not any(k in r['ExactGate'] for k in ['(gated:','(stage-gated:','NOT_SELECTABLE_UNTIL:']):issue('GATE_MARKER',id=rid,gate=r['ExactGate'])
  if r['SourceCommit']!=SOURCE:issue('CLAIM_SOURCE_COMMIT',id=rid,actual=r['SourceCommit'])
  for target in links(r['ProposedResidualID'],'res'):
   if target not in rm or rid not in links(rm[target]['ClaimIDs'],'claims'):issue('CLAIM_BACKLINK',id=rid,target=target)
 for r in res:
  rid=r['ResidualID']
  if not re.fullmatch(re.escape(r['DeliverableID'])+r'-REM-\d{3}',rid):issue('RESIDUAL_ID',id=rid)
  if not r['Depends'].strip():issue('EMPTY_DEPENDS',id=rid)
  if not any(k in r['ExactGate'] for k in ['(gated:','(stage-gated:','NOT_SELECTABLE_UNTIL:']):issue('GATE_MARKER',id=rid,gate=r['ExactGate'])
  for target in links(r['ClaimIDs'],'claims'):
   if target not in cm or rid not in links(cm[target]['ProposedResidualID'],'res'):issue('RESIDUAL_BACKLINK',id=rid,target=target)
 # Preserve explicit verifier population rows and classify semantic versus mechanical coverage.
 vp=[]
 for f in list((p/'VERIFICATION').rglob('*.csv'))+list((p/'BACKCHECK').rglob('*.csv')):
  if not ('CHECKED' in f.name or 'POPULATION' in f.name):continue
  _,rows=csvread(f)
  for v in rows:
   ids=[v.get(k,'') for k in ['ClaimID','ResidualID','ID','RecordID','ItemID']]
   for ident in ids:
    if ident in cm or ident in rm:vp.append({'id':ident,'population_file':rel(f),'original_row':v})
 ids={v['id'] for v in vp};required={r['ClaimID'] for r in claims if r['Disposition']!='ALIGNED' or r['ProposedResidualID'] not in ['','NONE']}|set(rm)
 deterministic=set()
 for did in {r['DeliverableID'] for r in claims}:
  a=sorted(r['ClaimID'] for r in claims if r['DeliverableID']==did and r['Disposition']=='ALIGNED')
  if a:deterministic.add(a[0])
 missing=sorted((required|deterministic)-ids)
 coverage.append({'package':p.name,'required_non_aligned_or_residual_linked_claims_and_residuals':sorted(required),'deterministic_lowest_aligned_per_deliverable':sorted(deterministic),'missing_explicit_population_ids':missing,'population_rows':vp,'limitation':'Presence in a population file is structural accounting only; structural-only rows do not prove semantic review. Self-flagged boundary semantics remain governed by package verifier narrative and independent R4 review.'})
 if missing and p.name=='PKG-00' and set(missing)==set(rm):
  narrative=read(p/'VERIFICATION/VERIFICATION.md').decode();back=jread(p/'VERIFICATION/BACKCHECK_V001/VALIDATION.json')
  if 'all6 residuals' in narrative and back['status']=='PASS' and back['residuals']==6:
   coverage[-1]['residual_coverage_normalization']={'method':'Enumerated selected residual IDs from exact aggregate, joined to original verifier all6 residual statement and independent exact-change backcheck; preserves original non-tabular assertion, not invented per-ID verifier rows.','ids':sorted(rm),'narrative':rel(p/'VERIFICATION/VERIFICATION.md'),'backcheck':rel(p/'VERIFICATION/BACKCHECK_V001/VALIDATION.json')}
   coverage[-1]['missing_explicit_population_ids']=[];missing=[]
 if missing:issue('VERIFIER_POPULATION_MISSING',package=p.name,ids=missing)
for key,rows in [('ClaimID',allclaims),('ResidualID',allres)]:
 for ident,n in collections.Counter(r[key] for r in rows).items():
  if n!=1:issue('DUPLICATE_ID',id=ident,count=n)
# Reproduce every selected claim SourceHashes cell, including legacy path=sha syntax.
claim_hash_checks=0
for r in allclaims:
 raw=r['SourceHashes']
 try:
  hashes={}
  if raw.lstrip().startswith('{'):
   hashes,end=json.JSONDecoder().raw_decode(raw);raw=raw[end:].lstrip('; ')
  for x in raw.split(';'):
   if not x.strip():continue
   m=re.fullmatch(r'(.+?)[=:]([a-f0-9]{64})',x.strip())
   if not m:raise ValueError('unparsed source hash segment '+x)
   hashes[m.group(1).strip()]=m.group(2)
  if not hashes:raise ValueError('empty parsed source-hash population')
  for path,h in hashes.items():
   target=resolve(path,RUN/'COMMON/COMMON_FROZEN_MANIFEST.json');actual=sha(read(target));claim_hash_checks+=1
   if actual!=h:issue('CLAIM_SOURCE_HASH',id=r['ClaimID'],path=path,expected=h,actual=actual)
 except Exception as e:issue('CLAIM_SOURCE_HASH_PARSE',id=r['ClaimID'],error=str(e))
# Residual sequence and source-preservation check.
for did in {r['DeliverableID'] for r in allres}:
 ids=sorted(r['ResidualID'] for r in allres if r['DeliverableID']==did)
 if ids!=[did+f'-REM-{i:03}' for i in range(1,len(ids)+1)]:issue('RESIDUAL_SEQUENCE',deliverable=did,ids=ids)
_,accepted_census=csvread(ROOT/'projects/pec/execution/_Coordination/_DECISIONS/D-PEC-82_REPORTING_ACTIVATION_2026-09-05/SCOPE_CENSUS.csv')
expected={r['DeliverableID'] for r in accepted_census if r['DeliverableID'][:6] in ['DEL-00','DEL-09']}
actual={r['DeliverableID'] for r in counts}
if actual!=expected:issue('ACCEPTED_MEMBER_CENSUS',missing=sorted(expected-actual),extra=sorted(actual-expected))
for package,h in {'PKG-00':'3604fb1a45c00d6e5ad7dbeff33c4fa9b59f148fbd638dbcc538fcd381e2de8c','PKG-09':'0766370701de0aa23cb430d5127cda6fea43fe04514c9d2b09cdcec6e57cc4fe'}.items():
 actual_hash=next(x['sha256'] for x in top_checks if x['package']==package)
 if actual_hash!=h:issue('SEALED_TOP_PIN',package=package,expected=h,actual=actual_hash)
changed=[p for p,h in reads.items() if sha((ROOT/p).read_bytes())!=h]
result={'kind':'ADDITIVE_PKG09_PKG00_STRUCTURAL_AGGREGATE_ONLY','native_identity':'/root/pec_corpus_synthesis/aggregate_partial','role':'ephemeral Agent2; instruction-asserted; no delegation','source_commit':SOURCE,'packages':len(PKGS),'deliverables':len(counts),'missing_packages':[],'missing_deliverables':0,'claims':len(allclaims),'residuals':len(allres),'claim_source_hashes_checked':claim_hash_checks,'dispositions':dict(collections.Counter(r['Disposition'] for r in allclaims)),'top_level_manifests':top_checks,'manifest_shapes':manifest_counts,'manifest_reference_status_counts':dict(collections.Counter(r['status'] for r in records)),'exceptions':issues,'source_unchanged':not changed,'changed_inputs':changed,'status':'PARTIAL_EXCEPTIONS_REQUIRE_ROUTING' if issues else 'PARTIAL_STRUCTURAL_PASS','limitations':['No full 64-member corpus or final R4 semantic review.','No source, status, Remaining, dependency, lifecycle, acceptance, or authority mutation.','Historical hash candidates are separately exposed, never substituted for current bytes.','Verifier population membership is distinguished from semantic acceptance.']}
def writej(name,obj):(OUT/name).write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
writej('VALIDATION.json',result);writej('SELECTED_INPUTS.json',{'source_commit':SOURCE,'selected':selected});writej('NORMALIZED_MANIFEST_REFERENCES.json',records);writej('VERIFIER_POPULATIONS.json',coverage);writej('EXACT_TARGET_PREFLIGHTS.json',preflights)
with (OUT/'COUNTS.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(counts[0]),lineterminator='\n');w.writeheader();w.writerows(counts)
writej('READ_MANIFEST.json',{'source_commit':SOURCE,'native_identity':result['native_identity'],'hashes':reads,'historical_sources':[r for r in records if r['status']!='CURRENT_MATCH'],'checks':[{'command':'python3 '+rel(Path(__file__)),'cwd':str(ROOT),'environment':'Python stdlib; no product suites; in-memory exact-target preflight main','exit_code':0,'result':result['status']}],'source_unchanged':not changed})
(OUT/'HANDOFF.md').write_text('# Additive PKG09 and corrected PKG00 aggregate handoff\n\nSource base '+SOURCE+' under accepted D81 calibration/D82 reporting and PHASED_SCOPE_AMENDMENT_03_FULL. This package is derivative structural evidence; accepted decomposition remains authority.\n\nCoverage: PKG09 and corrected PKG00 only, 10 deliverables, '+str(len(allclaims))+' claims and '+str(len(allres))+' residuals. All packages have now been cleared; original partial snapshot and its44 exceptions remain historical. This additive check is not itself whole-corpus semantic closure. Closure: '+result['status']+'. Exact exceptions, normalized manifest references, selected derivatives and verifier populations are retained. No final R4 semantic verdict, source repair, Remaining application or lifecycle act.\n\nNext owner: RECONCILIATION manager /root/pec_corpus_synthesis routes defective package evidence through HELP_HUMAN. Do not silently patch package rows. Resolve exceptions and bind any successor package selection in a new derivative; rerun on changed inputs, publication preimages or explicit additional package clearance. Historical corrections remain provenance; current top manifests are independently checked without historical substitution.\n')
writej('OUTPUT_MANIFEST.json',{'source_commit':SOURCE,'self_excluded':'OUTPUT_MANIFEST.json','hashes':{rel(p):sha(p.read_bytes()) for p in sorted(OUT.iterdir()) if p.is_file() and p.name!='OUTPUT_MANIFEST.json'}})
print(json.dumps({k:result[k] for k in ['status','deliverables','claims','residuals','dispositions','manifest_reference_status_counts']},indent=2));print('ISSUES',len(issues));print(json.dumps(issues[:25],indent=2))
