"""Sealed M001 mechanical derivative. --check replays read-only full equality checks."""
import csv, hashlib, json, re, sys
from pathlib import Path
from collections import Counter
P=Path('projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05/R1_R4_2026-09-05/PACKAGES/PKG-10')
S=P/'MECHANICAL_CORRECTION_01'
CL=P.parent.parent/'COMMON/BRIEF_CLARIFICATION_01.md'
IDS=['DEL-10-01','DEL-10-02','DEL-10-04']
SCHEMAS={'CLAIMS.csv':'ClaimID,DeliverableID,ClaimClass,NormativeSource,ScopeItemIDs,DeclaredSource,CurrentState,ImplementationEvidence,VerificationEvidence,ValidationOrProvenanceEvidence,LifecycleEvidence,ExistingRemaining,Disposition,ProposedResidualID,ProposedResidualText,Depends,ExactGate,AuthorityNeeded,Selectability,SourceCommit,SourceHashes,EvidenceReferences,Notes'.split(','),'RESIDUALS.csv':'ResidualID,DeliverableID,ClaimIDs,ProposedText,Depends,ExactGate,ClosureEvidence,AuthorityNeeded,Selectability,Notes'.split(',')}
IDMAP={f'R-DEL-10-02-{n:02d}':f'DEL-10-02-REM-{n:03d}' for n in range(1,5)}
BASE='2be412ccea62bdc4bd96deb082c46d7a792076ea'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump(p,obj):p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
def readcsv(p):
 with p.open(newline='') as f:
  r=csv.DictReader(f);return r.fieldnames,list(r)
def renamed(v,d):
 if d=='DEL-10-02':
  for old,new in IDMAP.items():v=v.replace(old,new)
 return v
def allowed(v,col,row,d):
 v=renamed(v,d)
 if col=='Depends' and not v:v='NONE'
 if col=='ExactGate' and not any(m in v for m in ['(gated:', '(stage-gated:', 'NOT_SELECTABLE_UNTIL:']):
  if v:v='NOT_SELECTABLE_UNTIL: '+v
  else:
   assert row.get('Disposition')=='ALIGNED' and not row.get('ProposedResidualID')
   v='NOT_SELECTABLE_UNTIL: no new act proposed; any later act requires its owning grant.'
 return v

def backcheck():
 evidence=[]
 for d in IDS:
  w=P/'WORKERS'/d;o=w/'REVISION_M001'
  cm=json.loads((o/'CHANGE_MAP.json').read_text())
  for p,h in cm['original_hashes'].items():assert sha(p)==h,('original changed',p)
  for p,h in cm['output_hashes'].items():assert sha(p)==h,('output changed',p)
  oldm=json.loads((w/'READ_MANIFEST.json').read_text());newm=json.loads((o/'READ_MANIFEST.json').read_text())
  assert newm['source_commit']==oldm['source_commit']==BASE
  assert all(newm['hashes'][p]==h and sha(p)==h for p,h in oldm['hashes'].items())
  assert all(sha(p)==h for p,h in newm['hashes'].items())
  assert newm['historical_sources']==oldm['historical_sources']
  assert newm['source_unchanged'] is True
  actual=[];totals={};data={}
  for name,schema in SCHEMAS.items():
   ah,a=readcsv(w/name);bh,b=readcsv(o/name)
   assert ah==bh==schema
   assert len(a)==len(b)
   assert b'\r' not in (o/name).read_bytes()
   assert (o/name).read_bytes().endswith(b'\n')
   key=schema[0]
   for i,(before,after) in enumerate(zip(a,b),1):
    for col in schema:
     expect=allowed(before[col],col,before,d)
     assert after[col]==expect,(d,name,i,col)
     if before[col]!=after[col]:actual.append({'file':name,'data_row_1based':i,'row_id_before':before[key],'row_id_after':after[key],'column':col,'old':before[col],'new':after[col]})
    assert after['DeliverableID']==d
    assert after['Depends']
    assert any(m in after['ExactGate'] for m in ['(gated:', '(stage-gated:', 'NOT_SELECTABLE_UNTIL:'])
   assert len({r[key] for r in b})==len(b)
   totals[name]=len(b);data[name]=b
  assert actual==cm['changes']
  claims={r['ClaimID']:r for r in data['CLAIMS.csv']}
  residuals={r['ResidualID']:r for r in data['RESIDUALS.csv']}
  assert list(residuals)==[f'{d}-REM-{n:03d}' for n in range(1,len(residuals)+1)]
  for cid,r in claims.items():
   for rid in filter(None,r['ProposedResidualID'].split(';')):
    assert rid in residuals and cid in residuals[rid]['ClaimIDs'].split(';')
  for rid,r in residuals.items():
   for cid in r['ClaimIDs'].split(';'):assert cid in claims and rid in claims[cid]['ProposedResidualID'].split(';')
  assert (o/'COVERAGE.md').read_text()==renamed((w/'COVERAGE.md').read_text(),d)+cm['coverage_appendix']
  for name in ['CLAIMS.csv','RESIDUALS.csv','COVERAGE.md','RETURN.md','READ_MANIFEST.json']:
   assert not re.search(r'R-DEL-10-02-0[1-4]',(o/name).read_text())
  evidence.append({'deliverable':d,'rows':totals,'csv_cells_checked':sum(totals[f]*len(SCHEMAS[f]) for f in totals),'changed_cells':len(actual),'changes_by_column':dict(Counter(c['column'] for c in actual)),'original_files_preserved':len(cm['original_hashes']),'original_source_hashes_checked':len(oldm['hashes']),'full_manifest_hashes_checked':len(newm['hashes']),'all_checks':'PASS','source_commit':BASE,'ledger_hashes':{f:sha(o/f) for f in SCHEMAS}})
 return {'status':'PASS','semantic_rerun':False,'product_tests_run':False,'role':'Agent2 instruction-asserted; not mechanically enforced','command':f'python3 {S}/correct_and_backcheck.py --check','command_sha256':sha(S/'correct_and_backcheck.py'),'checks':['canonical schema and LF','full cell equality against permitted transformation','complete exact cell change-map equality','residual unique owner-prefix sequence and reciprocal links','Depends explicit and ExactGate marked','original file preservation','original source map equality and current source SHA256 equality','historical source records preserved','coverage body preserved except exact ID normalization and labeled mechanical appendix'],'members':evidence}

if '--check' in sys.argv:
 print(json.dumps(backcheck(),indent=2));sys.exit(0)

preflight=json.loads(Path('/tmp/pec10_m001_preflight.json').read_text())
dump(S/'PREFLIGHT.json',preflight)
for f in json.loads((P/'MECHANICAL_FINDINGS_01.json').read_text()):assert sha(f['file'])==f['sha256']
for d in IDS:
 w=P/'WORKERS'/d;o=w/'REVISION_M001'
 assert not o.exists(),('immutable output already exists',o)
 original={str(f):sha(f) for f in sorted(w.iterdir()) if f.is_file()}
 oldm=json.loads((w/'READ_MANIFEST.json').read_text())
 assert all(sha(p)==h for p,h in oldm['hashes'].items())
 o.mkdir()
 changes=[];counts={}
 for name,schema in SCHEMAS.items():
  header,rows=readcsv(w/name);assert header==schema
  out=[]
  for i,row in enumerate(rows,1):
   after={col:allowed(row[col],col,row,d) for col in schema};out.append(after)
   for col in schema:
    if row[col]!=after[col]:changes.append({'file':name,'data_row_1based':i,'row_id_before':row[schema[0]],'row_id_after':after[schema[0]],'column':col,'old':row[col],'new':after[col]})
  with (o/name).open('w',newline='') as f:
   writer=csv.DictWriter(f,fieldnames=schema,lineterminator='\n');writer.writeheader();writer.writerows(out)
  counts[name]=len(rows)
 appendix=f'\n## Mechanical derivative REVISION_M001\n\nOriginal coverage above retained with exact residual-ID normalization where applicable. This derivative changes only residual IDs/reciprocal references, empty Depends to NONE, and governed ExactGate markers. No semantic rerun or new product tests. Original source assessment and owner conditions remain unchanged. Upstream original worker outputs are hash-bound by CHANGE_MAP.json and READ_MANIFEST.json; clarification: `{CL}`. Independent package verification and manager selection remain pending. Role instruction-asserted, not mechanically enforced.\n'
 (o/'COVERAGE.md').write_text(renamed((w/'COVERAGE.md').read_text(),d)+appendix)
 m=json.loads((w/'READ_MANIFEST.json').read_text())
 additions=[CL,P/'PACKAGE_BASIS.md',P/'MECHANICAL_FINDINGS_01.json',P/'BRIEF_MECHANICAL_CORRECTION_01.md',P/f'BRIEF_{d}.md',P.parent.parent/'COMMON/BRIEFS/PKG-10.md',S/'PREFLIGHT.json',S/'correct_and_backcheck.py']+[Path(x) for x in original]
 m['hashes'].update({str(f):sha(f) for f in additions})
 m['checks']=m['checks']+[{'command':'Original manifest checks above are inherited provenance; M001 performs mechanical normalization only.','cwd':str(Path.cwd()),'environment':{},'exit_code':0,'result':f'Original source hash map reproduced unchanged: {len(oldm["hashes"])} entries. Exact original outputs and clarification hashes added.'}]+[r for r in preflight if d in r['command']]+[{'command':f'python3 {S}/correct_and_backcheck.py --check','cwd':str(Path.cwd()),'environment':{},'exit_code':0,'result':'Full permitted-transformation, cell-map equality, source hashes, original preservation, schema/LF/sequence/reciprocity backcheck; detailed evidence in MECHANICAL_CORRECTION_01/BACKCHECK.json.'}]
 m['source_unchanged']=True;dump(o/'READ_MANIFEST.json',m)
 hashes={f:sha(o/f) for f in ['CLAIMS.csv','RESIDUALS.csv','COVERAGE.md','READ_MANIFEST.json']}
 disposition=Counter(r['Disposition'] for r in readcsv(o/'CLAIMS.csv')[1])
 (o/'RETURN.md').write_text(f'# {d} REVISION_M001 mechanical return\n\nCOMPLETE_FOR_INDEPENDENT_VERIFICATION. Derivative of original `{w}` at base `{BASE}`, accepted decomposition revision1.4, D81 accepted conventions and effective D82. Original substantive assessment is preserved: {counts["CLAIMS.csv"]} claims, {counts["RESIDUALS.csv"]} residuals; dispositions {dict(disposition)}. Coverage and substantive upstream findings are retained in COVERAGE.md and hash-bound original RETURN.md. No decomposition, source, Remaining, gate condition, disposition, evidence, lifecycle, release or authority change.\n\nCorrected {len(changes)} CSV cells using the sealed mechanical rules. CHANGE_MAP.json lists every cell old/new and original/output hashes. Full comparison checks every CSV cell, exact schemas, LF, owner-prefixed sequential residual IDs, reciprocal links, explicit Depends, governed gate markers, source equality and preserved originals. Source-hash checks passed; exact correction-preparation hold checks ALLOW. No semantic rerun or product tests. All existing selectability values remain unchanged.\n\nHandoff: select this derivative only after independent package verification; manager fan-in remains outstanding. Closure is mechanical report readiness only. Relevant source/hold/owner/contract changes require owning reassessment; mechanical backcheck may be replayed with the command in BACKCHECK.json. No new blockers beyond original substantive unknowns/gates and pending independent verification. Sole writes this REVISION_M001 and package MECHANICAL_CORRECTION_01 subtree; no delegation or source/Git/service/network mutation. Agent2 role instruction-asserted, not mechanically enforced.\n\nOutput SHA-256:\n'+''.join(f'- {f}: `{h}`\n' for f,h in hashes.items()))
 dump(o/'CHANGE_MAP.json',{'deliverable':d,'revision':'REVISION_M001','source_commit':BASE,'original_hashes':original,'output_hashes':{str(o/f):sha(o/f) for f in ['CLAIMS.csv','RESIDUALS.csv','COVERAGE.md','READ_MANIFEST.json','RETURN.md']},'residual_id_map':IDMAP if d=='DEL-10-02' else {},'changes':changes,'coverage_appendix':appendix,'non_csv_policy':'COVERAGE retains complete original text except exact residual ID substitutions plus the recorded appendix; READ_MANIFEST preserves original source map/historical records and appends exact provenance and correction checks; RETURN is derivative-specific and cites unchanged original return.'})

result=backcheck();dump(S/'BACKCHECK.json',result)
(S/'RETURN.md').write_text('# Mechanical correction 01 terminal return\n\nCOMPLETE_FOR_INDEPENDENT_VERIFICATION. Base `'+BASE+'`; accepted upstream decomposition revision1.4/D81 calibration/effective D82. These mechanical derivatives never substitute for authoritative decomposition. Original worker outputs and their source maps are preserved and bound by each CHANGE_MAP.json and READ_MANIFEST.json.\n\nExact derivative selection for independent package verification:\n'+''.join(f'- `{P}/WORKERS/{d}/REVISION_M001/`: CLAIMS.csv, RESIDUALS.csv, COVERAGE.md, READ_MANIFEST.json, RETURN.md; complete cell map CHANGE_MAP.json.\n' for d in IDS)+'\nDEL-10-02 residual IDs normalize from R-DEL-10-02-01..04 to DEL-10-02-REM-001..004, including every reciprocal reference. Empty Depends becomes NONE; unmarked gates receive NOT_SELECTABLE_UNTIL: while original condition text remains exact. All other CSV cells, counts, dispositions, evidence and selectability remain unchanged.\n\nBACKCHECK.json: PASS for every mapped and unchanged cell, schemas/LF/sequence/reciprocity, original preservation and all original source hashes. No semantic rerun or product tests. Source/evidence/owner/hold changes retain original rerun requirements. Required derivative status: M001 complete, independent package verifier and manager selection pending; product/Remaining/lifecycle closure is not asserted. Original UNKNOWNs and named gates remain; no new substantive findings. Role instruction-asserted, not mechanically enforced; no delegation. Only authorized three REVISION_M001 subtrees and this summary subtree were written.\n')
dump(S/'OUTPUT_HASHES.json',{str(f):sha(f) for f in sorted(S.iterdir()) if f.is_file() and f.name!='OUTPUT_HASHES.json'}|{str(f):sha(f) for d in IDS for f in sorted((P/'WORKERS'/d/'REVISION_M001').iterdir()) if f.is_file()})
print(json.dumps(result,indent=2))
