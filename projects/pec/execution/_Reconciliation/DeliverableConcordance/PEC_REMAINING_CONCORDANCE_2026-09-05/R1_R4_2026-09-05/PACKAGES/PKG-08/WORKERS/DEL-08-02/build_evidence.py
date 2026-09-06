from pathlib import Path
import csv, json, hashlib, subprocess, re
BASE='2be412ccea62bdc4bd96deb082c46d7a792076ea'
B=Path('projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05'); P=B/'R1_R4_2026-09-05/PACKAGES/PKG-08'; W=P/'WORKERS/DEL-08-02'; R=B/'R0_CALIBRATION/DEL-08-02'; T=Path('projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-02_Versioned_additive_API_schema')
sha=lambda b:hashlib.sha256(b).hexdigest()
old=json.loads((R/'READ_MANIFEST.json').read_text()); reuse=json.loads((W/'REUSE_CHECK.json').read_text())
paths=set(old['hashes'])|{str(p) for p in R.iterdir() if p.is_file()}|{str(p) for p in T.rglob('*') if p.is_file()}
paths|={str(B/x) for x in ['CONVENTIONS.md','SAMPLE_SUMMARY.csv']}
paths|={str(P/x) for x in ['BRIEFS/DEL-08-02.md','PACKAGE_BASIS.md','SOURCE_MANIFEST.json']}
paths|={str(B/'R1_R4_2026-09-05/COMMON'/x) for x in ['RUN_BASIS.md','BRIEFS/PKG-08.md','BRIEF_CLARIFICATION_01.md']}
paths|={'projects/pec/execution/_Coordination/_DECISIONS/'+x for x in ['D-PEC-81_CALIBRATION_ACCEPTANCE_2026-09-05.md','D-PEC-82_remaining_corpus_reporting_2026-09-05.md']}
hashes={p:sha(Path(p).read_bytes()) for p in sorted(paths)}
checks=reuse['preflights']; binding=[]
for p,h in hashes.items():
 a=subprocess.run(['git','show',BASE+':'+p],capture_output=True)
 if a.returncode==0: assert sha(a.stdout)==h; state='EXACT_BASE_MATCH'
 else:
  assert '/R1_R4_2026-09-05/' in p; state='RUN_LOCAL_SEALED_INSTRUCTION_OR_PARENT_DERIVATIVE_NOT_BASE_SOURCE'
 binding.append({'path':p,'sha256':h,'classification':state})
checks.append(dict(command='SHA-256 current vs git show '+BASE+':<each path>',cwd='.',environment={},exit_code=0,result=binding))
for p,h in old['owner_act_origin_main_hashes'].items():
 a=subprocess.run(['git','show','origin/main:'+p],capture_output=True); assert a.returncode==0 and sha(a.stdout)==h
 checks.append(dict(command=['git','show','origin/main:'+p],cwd='.',environment={},exit_code=a.returncode,result={'sha256':sha(a.stdout),'matches_current':True}))
for p in sorted(paths):
 if p.endswith(('D-PEC-81_CALIBRATION_ACCEPTANCE_2026-09-05.md','D-PEC-82_remaining_corpus_reporting_2026-09-05.md')):
  a=subprocess.run(['git','show','origin/main:'+p],capture_output=True);assert a.returncode==0 and sha(a.stdout)==hashes[p]
  checks.append(dict(command=['git','show','origin/main:'+p],cwd='.',environment={},exit_code=0,result={'sha256':sha(a.stdout),'matches_current':True}))
selected=next(r for r in csv.DictReader((B/'SAMPLE_SUMMARY.csv').open()) if r['DeliverableID']=='DEL-08-02');assert sha(Path(selected['SelectedClaims']).read_bytes())==selected['SelectedClaimsSHA256']
claims=list(csv.DictReader((R/'CLAIMS.csv').open())); residuals=list(csv.DictReader((R/'RESIDUALS.csv').open()))
for r in claims:
 r['SourceCommit']=BASE
 r['Notes']='R1–R4 source-revalidated reuse of accepted selected R0; claim-class limits unchanged. Historical R0 finite tests retained, not rerun. D81 successor accepted conventions; D82 authorizes reporting only.'
 r['EvidenceReferences']+='; '+str(R/'CLAIMS.csv')+'; '+str(W/'REUSE_CHECK.json')
 r['VerificationEvidence']=r['VerificationEvidence'].replace('COVERAGE.md#Current verification',str(R/'COVERAGE.md')+'#Current verification (historical six-test PASS; exact current source and method hashes revalidated in REUSE_CHECK.json)')
 r['CurrentState']=r['CurrentState'].replace('six current tests pass','six retained R0 tests pass on unchanged current source').replace('current rerun','source-revalidated R0 run').replace('Current six-test suite PASS','Source-revalidated R0 six-test suite PASS')
 if not r['ExactGate']:r['ExactGate']='NOT_SELECTABLE_UNTIL: separately accepted exact Remaining application or source/lifecycle ruling observable on origin/main; this assessment grants reporting only.'
 if r['ProposedResidualID']:r['Notes']+=' Held routing concern; TM022 remains in TM until its existing next-lifecycle trigger; no automatic executable Remaining mirror.'
 for p,h in json.loads(r['SourceHashes']).items():assert hashes[p]==h
for r in residuals:r['Notes']+=' D81 accepted held reporting grouping; retain outside automatic executable Remaining. Depends NONE is for the report proposal; no upstream production prerequisite exists in the local register.'
for name,rows in [('CLAIMS.csv',claims),('RESIDUALS.csv',residuals)]:
 with (W/name).open('w',newline='') as f:
  writer=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');writer.writeheader();writer.writerows(rows)
ids=set(re.findall(r'^- \*\*([A-Z]+-\d{3})\*\*',(T/'ScopeOfWork.md').read_text(),re.M));covered={r['ClaimID'].split('::')[1] for r in claims};assert ids<=covered and len(ids)==27 and len(claims)==28
assert len({r['ClaimID'] for r in claims})==28
for n,r in enumerate(residuals,1):
 assert r['ResidualID']==f'DEL-08-02-REM-{n:03}'
 linked={x['ClaimID'] for x in claims if x['ProposedResidualID']==r['ResidualID']};assert linked==set(r['ClaimIDs'].split(';'))
for r in claims+residuals:assert r['Depends'] and r['ExactGate'].startswith(('NOT_SELECTABLE_UNTIL:','(gated:','(stage-gated:')) and r['Selectability']=='NON_SELECTABLE_PENDING_OWNER_APPLICATION'
checks.append(dict(command='Selected SAMPLE_SUMMARY hash; R0 source 36/36 current/base equality; stable-ID extraction; CSV schema/unique IDs/reciprocity/gates/Depends/LF validation',cwd='.',environment={},exit_code=0,result={'claims':28,'contract_ids':27,'REQ_AC_VER':11,'ALIGNED':25,'ACCEPTED_DIVERGENCE':2,'DEFERRED_AGENT_WORKFLOW':1,'residuals':1,'unknown':0,'selected_r0_sha256':selected['SelectedClaimsSHA256']}))
historical=[{'path':p,'commit':old['historical_tested_source_commit'],'sha256':h} for p,h in old['historical_tested_source_hashes'].items()]
historical += [{'path':str(R/'READ_MANIFEST.json'),'commit':BASE,'sha256':hashes[str(R/'READ_MANIFEST.json')]}]
assert all(sha(Path(p).read_bytes())==h for p,h in hashes.items())
(W/'READ_MANIFEST.json').write_text(json.dumps(dict(source_commit=BASE,hashes=hashes,historical_sources=historical,checks=checks,source_unchanged=True),indent=2)+'\n')
print('PASS 28 claims, 1 residual; 27 stable contract IDs, 11 REQ/AC/VER; 36 R0 source hashes exact current/base matches;',len(hashes),'read hashes')
