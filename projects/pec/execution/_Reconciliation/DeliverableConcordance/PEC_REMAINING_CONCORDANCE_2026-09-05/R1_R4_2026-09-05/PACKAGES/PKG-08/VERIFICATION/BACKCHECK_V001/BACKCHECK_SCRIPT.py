import pathlib,hashlib,json,csv,subprocess,re,collections,copy
root=pathlib.Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip());base='2be412ccea62bdc4bd96deb082c46d7a792076ea'
p=root/'projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05/R1_R4_2026-09-05/PACKAGES/PKG-08';v=p/'VERIFICATION';old=p/'WORKERS/DEL-08-05';new=old/'CORRECTION_V001';o=v/'BACKCHECK_V001';o.mkdir(exist_ok=True);hashes={};checks=[]
def read(f):
 f=root/f if not f.is_absolute() else f;b=f.read_bytes();hashes[str(f.relative_to(root))]=hashlib.sha256(b).hexdigest();return b
def doc(f):return json.loads(read(f))
for f in [root/'AGENTS.md',root/'projects/pec/AGENTS.md',p/'BRIEFS/VERIFIER_V1.md',p/'BRIEFS/BACKCHECK_DEL0805_V001.md',p/'BRIEFS/CORRECTION_DEL0805_V001.md']:read(f)
for target in ['execution/_Decomposition/ScopeLedger.csv','execution/_Decomposition/Deliverables.csv','execution/_Decomposition/SOFTWARE_DECOMP.md','execution/PKG-08_API_Access/1_Working/DEL-08-05_SSE_delta_presence_subscription/ScopeOfWork.md','execution/PKG-08_API_Access/1_Working/DEL-08-05_SSE_delta_presence_subscription/_STATUS.md','execution/PKG-08_API_Access/1_Working/DEL-08-05_SSE_delta_presence_subscription/Dependencies.csv']:
 cmd=['python3','projects/pec/execution/_Scripts/pec_reliance_hold.py','--register','projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv','--target',target,'--operation','candidate-validation'];r=subprocess.run(cmd,cwd=root,capture_output=True,text=True);assert r.returncode==0;checks.append({'command':cmd,'cwd':'.','environment':{'PYTHONDONTWRITEBYTECODE':'1'},'exit_code':r.returncode,'result':r.stdout.strip()})
manifestresults={}
for folder in [v,old,new]:
 m=doc(folder/'OUTPUT_MANIFEST.json')
 entries=m.get('files',m.get('hashes')); manifestroot=folder if 'files' in m else root
 for f,h in entries.items():assert hashlib.sha256(read(manifestroot/f)).hexdigest()==h
 manifestresults[str(folder.relative_to(root))]={'entries':len(entries),'sha256':hashlib.sha256(read(folder/'OUTPUT_MANIFEST.json')).hexdigest(),'PASS':True}
for n in ['CLAIMS.csv','RESIDUALS.csv','COVERAGE.md','CURRENT_EVIDENCE.json']:assert read(old/n)==read(new/n)
a=doc(old/'SCOPE_FALLBACK.json');b=doc(new/'SCOPE_FALLBACK.json');expect=copy.deepcopy(a);expect['mappings'][0]['locus']='row SOW-044, ScopeItemStatement; physical line 45';assert b==expect and a['mappings'][0]['locus']=='row SOW-044, Description; physical line 45'
assert read(new/'SCOPE_FALLBACK.json')==read(old/'SCOPE_FALLBACK.json').replace(b'row SOW-044, Description; physical line 45',b'row SOW-044, ScopeItemStatement; physical line 45')
for x in b['mappings']:
 s=read(pathlib.Path(x['path']));assert hashlib.sha256(s).hexdigest()==x['file_sha256'];assert x['quote'] in s.decode();assert hashlib.sha256(x['quote'].encode()).hexdigest()==x['quote_sha256'];line=int(re.search(r'line (\d+)',x['locus']).group(1));assert x['quote'] in s.decode().splitlines()[line-1]
sl=csv.DictReader(read(root/b['mappings'][0]['path']).decode().splitlines());assert 'ScopeItemStatement' in sl.fieldnames and 'Description' not in sl.fieldnames;assert next(x for x in sl if x['ScopeItemID']=='SOW-044')['ScopeItemStatement']==b['mappings'][0]['quote']
cs=list(csv.DictReader(read(new/'CLAIMS.csv').decode().splitlines()));rs=list(csv.DictReader(read(new/'RESIDUALS.csv').decode().splitlines()));counts=collections.Counter(c['Disposition'] for c in cs);assert len(cs)==18 and counts=={'ALIGNED':15,'UNKNOWN':3} and len(rs)==1
for c in cs:
 assert c['Depends']=='NONE' and re.search(r'\(gated:|NOT_SELECTABLE_UNTIL:|\(stage-gated:',c['ExactGate']);assert c['SourceCommit']==base
 for f,h in json.loads(c['SourceHashes']).items():assert hashlib.sha256(read(pathlib.Path(f))).hexdigest()==h
r=rs[0];assert r['Depends']=='NONE' and r['Selectability']=='NON_SELECTABLE_PENDING_OWNER_APPLICATION'
linked=[c for c in cs if c['ProposedResidualID']==r['ResidualID']];assert set(r['ClaimIDs'].split(';'))=={c['ClaimID'] for c in linked}
m=doc(new/'READ_MANIFEST.json');assert m['source_unchanged'] is True
binding={}
for f,h in m['hashes'].items():
 assert hashlib.sha256(read(pathlib.Path(f))).hexdigest()==h
 proc=subprocess.run(['git','show',base+':'+f],cwd=root,capture_output=True)
 if proc.returncode==0:assert hashlib.sha256(proc.stdout).hexdigest()==h;binding[f]='BASE_EQUAL'
 else:assert '/R1_R4_2026-09-05/' in f;binding[f]='RUN_LOCAL_DERIVATIVE'
# Reproduce original verifier source inventory without touching it.
for f,h in doc(v/'READ_MANIFEST.json')['hashes'].items():assert hashlib.sha256(read(pathlib.Path(f))).hexdigest()==h
for f in new.iterdir():
 if f.is_file():read(f)
selected={str((new/n).relative_to(root)):hashlib.sha256(read(new/n)).hexdigest() for n in ['CLAIMS.csv','RESIDUALS.csv','SCOPE_FALLBACK.json','OUTPUT_MANIFEST.json']}
validation={'verdict':'PASS','finding':'PKG08-V1-001','finding_disposition':'RESOLVED_IN_CORRECTION_V001_ONLY','original_verdict_unchanged':'CORRECTION_REQUIRED','claims':18,'ALIGNED':15,'UNKNOWN':3,'residuals':1,'semantic_changes':0,'exact_delta':'/mappings/0/locus: Description -> ScopeItemStatement; no other byte difference in fallback','manifests':manifestresults,'source_binding':binding,'selected':selected,'remaining_product_closure':False}
(o/'VALIDATION.json').write_text(json.dumps(validation,indent=2)+'\n')
with (o/'CHECKED_DELTA_POPULATION.csv').open('w',newline='') as f:
 w=csv.writer(f,lineterminator='\n');w.writerow(['Artifact','ExactCheck','Verdict']);w.writerow(['SCOPE_FALLBACK.json','Only mappings[0].locus Description→ScopeItemStatement; complete JSON and byte replacement equality; all3 quote/file hashes and physical lines match','PASS'])
 for n in ['CLAIMS.csv','RESIDUALS.csv','COVERAGE.md','CURRENT_EVIDENCE.json']:w.writerow([n,'Byte-identical to original','PASS'])
 for c in cs:w.writerow([c['ClaimID'],'Original row bytes/semantics retained; source hashes, exact gate, Depends and disposition '+c['Disposition'],'PASS'])
 w.writerow([r['ResidualID'],'Exact unchanged reciprocal3 claim links; NONE evidence dependency and owner selectability gate','PASS'])
 for f in manifestresults:w.writerow([f+'/OUTPUT_MANIFEST.json','Every listed file hash reproduced','PASS'])
(o/'BACKCHECK.md').write_text('''# DEL-08-05 V001 independent backcheck

PASS for corrected report selection only. PKG08-V1-001 is resolved in WORKERS/DEL-08-05/CORRECTION_V001; the original verifier verdict and finding remain CORRECTION_REQUIRED / OPEN_ORIGINAL as immutable historical evidence.

The fallback differs by exactly one literal byte-string replacement at /mappings/0/locus: Description → ScopeItemStatement. The corrected field exists in ScopeLedger.csv, row SOW-044 is physical line45, and its value is the unchanged scope quote. All three fallback source-file hashes, quote hashes, literal text and physical line locations reproduce. All other fallback values are unchanged. CLAIMS.csv, RESIDUALS.csv, COVERAGE.md and CURRENT_EVIDENCE.json are byte-identical to the originals.

The 18 original claims remain 15 ALIGNED and3 UNKNOWN, with1 evidence-only residual. All claim source hashes, source commit, exact gates, NONE evidence dependency and reciprocal links reproduce. Original verifier, original worker and correction output manifests all match every declared entry; full original verifier read-source hashes also remain unchanged. Correction authoritative sources match D82 base; run-local context is explicitly derivative. Six fresh exact-target candidate-validation preflights returned ALLOW and confer no product authority.

No claim, residual, source, owner gate or meaning changed. Remaining unknown SSE implementation/test evidence, missing canonical contract, P4 staging, TM023 dedicated held mapping and no invented scope remain. Broader original verification limits survive: DEL08-04's43 local absence classifications are not universal; all80 package UNKNOWNs and12 raw proposals remain, D66 decline and TM022 deferral survive, and held routing is not automatic executable Remaining.

Accepted upstream is D81 calibration plus D82 base2be412ccea62bdc4bd96deb082c46d7a792076ea. This backcheck is a derivative of the frozen original review and fresh correction; no authoritative decomposition pointer is updated. No unresolved correction defect remains. Manager aggregate fan-in remains required. Rehash and repreflight on source/hold/authority changes. Only VERIFICATION/BACKCHECK_V001/** was written, with no delegation, Git mutation or product/lifecycle/Remaining act. Native Agent2 role is instruction-asserted, not mechanism-proven.
''')
(o/'RETURN.md').write_text('PASS: corrected DEL08-05 V001 is selectable for package report fan-in only. Sole locator defect resolved by exact one-field substitution; 18 claims/15ALIGNED/3UNKNOWN/1residual and all original claim/residual bytes unchanged. Source and original/corrected manifests reproduce. Original V1 verdict remains immutable; no product/Remaining/lifecycle closure. Selected exact paths/hashes are in VALIDATION.json.\n')
checks.append({'command':'python3 /tmp/pkg08_backcheck.py','cwd':'.','environment':{'PYTHONDONTWRITEBYTECODE':'1'},'exit_code':0,'result':'Exact byte delta,3 manifests, full original source rehash, source/base bindings, populations/gates/reciprocity and3 fallback line/quote hashes PASS'})
(o/'READ_MANIFEST.json').write_text(json.dumps({'source_commit':base,'hashes':hashes,'historical_sources':[],'checks':checks,'source_unchanged':True},indent=2)+'\n')
(o/'BACKCHECK_SCRIPT.py').write_bytes(pathlib.Path(__file__).read_bytes())
(o/'OUTPUT_MANIFEST.json').write_text(json.dumps({'status':'TERMINAL_PASS_REPORT_SELECTION_ONLY','self_excluded':True,'files':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(o.iterdir()) if f.is_file() and f.name!='OUTPUT_MANIFEST.json'}},indent=2)+'\n')
print(json.dumps({'verdict':'PASS','selected':selected,'backcheck_manifest_sha256':hashlib.sha256((o/'OUTPUT_MANIFEST.json').read_bytes()).hexdigest()},indent=2))
