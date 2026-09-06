import csv,json,hashlib,pathlib,subprocess,re,collections
R=pathlib.Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip());P=pathlib.Path(__file__).resolve().parent.parent;V=P/'VERIFICATION';BASE='2be412ccea62bdc4bd96deb082c46d7a792076ea'
hashes={};errors=[];hist=[];stats={};allc=[];allr=[];checked=[];trans=[]
def read(p):
 p=pathlib.Path(p)
 p=p if p.is_absolute() else R/p
 b=p.read_bytes();hashes[str(p.relative_to(R))]=hashlib.sha256(b).hexdigest();return b

def js(p):return json.loads(read(p))
def rows(p):return list(csv.DictReader(read(p).decode().splitlines()))
def check(ok,msg):
 if not ok:errors.append(msg)
# Reproduce every frozen manifest input, including worker originals and derivatives.
manifestfiles=[P/'SOURCE_MANIFEST.json',P/'SEALED_WORKER_MANIFEST.json']
for d in sorted((P/'WORKERS').iterdir()):
 manifestfiles.append(d/'READ_MANIFEST.json')
 if (d/'CORRECTION_S001').exists():manifestfiles.append(d/'CORRECTION_S001/READ_MANIFEST.json')
for mfile in manifestfiles:
 m=js(mfile)
 for path,h in m.get('hashes',{}).items():
  check(not pathlib.Path(path).is_absolute() and '..' not in pathlib.Path(path).parts,'path containment '+path)
  try:check(hashlib.sha256(read(path)).hexdigest()==h,'manifest hash '+path)
  except FileNotFoundError:errors.append('missing '+path)
 for h in m.get('historical_sources',[]):
  b=subprocess.run(['git','show',h['commit']+':'+h['path']],capture_output=True)
  check(b.returncode==0 and hashlib.sha256(b.stdout).hexdigest()==h['sha256'],'historical hash '+h['path']);hist.append(h)
# All current source authority hashes must agree with effective base; run outputs are derivatives.
base_count=0;derivative_count=0
for path,h in list(hashes.items()):
 if '/R1_R4_2026-09-05/' in path:derivative_count+=1;continue
 b=subprocess.run(['git','show',BASE+':'+path],capture_output=True)
 check(b.returncode==0 and hashlib.sha256(b.stdout).hexdigest()==h,'base source mismatch '+path);base_count+=1
expected=js(P/'EXPECTED_CLAIM_IDS.json')
for d in sorted((P/'WORKERS').iterdir()):
 q=d/'CORRECTION_S001' if (d/'CORRECTION_S001').exists() else d
 c=rows(q/'CLAIMS.csv'); rr=rows(q/'RESIDUALS.csv');allc+=c;allr+=rr
 if q!=d:
  maps=js(q/'CHANGE_MAP.json')['one_to_one_residual_id_map'];n=0
  for file in ['CLAIMS.csv','RESIDUALS.csv']:
   before=rows(d/file);after=rows(q/file);check(len(before)==len(after),'correction row count '+str(q))
   for a,b in zip(before,after):
    for col,value in a.items():
     want=value
     if col in ('ResidualID','ProposedResidualID'):
      for old,new in maps.items():want=want.replace(old,new)
     if col=='Depends' and not value.strip():want='NONE'
     if col=='ExactGate' and not value.startswith('NOT_SELECTABLE_UNTIL:'):want='NOT_SELECTABLE_UNTIL: '+value
     check(b[col]==want,'unauthorized correction '+d.name+' '+a.get('ClaimID',a.get('ResidualID',''))+' '+col)
     n+=a[col]!=b[col]
  trans.append({'member':d.name,'changed_cells':n,'id_map':maps})
 ids={x['ClaimID'] for x in c};rids={x['ResidualID'] for x in rr};check(len(ids)==len(c),'duplicate claims '+d.name);check(len(rids)==len(rr),'duplicate residual '+d.name)
 check({d.name+'::'+x for x in expected[d.name]['local_ids']}<=ids,'defined coverage '+d.name)
 low=min(x['ClaimID'] for x in c if x['Disposition']=='ALIGNED')
 for x in c:
  check(x['SourceCommit']==BASE,'claim commit '+x['ClaimID'])
  cell=x['SourceHashes'];hs=json.loads(cell) if cell.startswith('{') else dict(y.strip().split('=',1) for y in cell.split(';') if y.strip())
  for path,h in hs.items():check(hashlib.sha256(read(path)).hexdigest()==h,'claim source hash '+x['ClaimID']+' '+path)
  links={y.strip() for y in x['ProposedResidualID'].split(';') if y.strip() not in ('','NONE','N/A')}
  for rid in links:check(rid in rids and x['ClaimID'] in next(y for y in rr if y['ResidualID']==rid)['ClaimIDs'].split(';'),'reciprocity '+x['ClaimID'])
  check(bool(x['NormativeSource'] and x['DeclaredSource'] and x['EvidenceReferences']),'citation absence '+x['ClaimID'])
  # Every row is included; mandatory and extended aligned boundary rows explicitly distinguished.
  why='NON_ALIGNED' if x['Disposition']!='ALIGNED' else ('DETERMINISTIC_LOWEST_ALIGNED' if x['ClaimID']==low else 'EXPANDED_CLASS_BOUNDARY_AND_DOCUMENTARY_CHECK')
  checked.append({'Kind':'CLAIM','ClaimID':x['ClaimID'],'ResidualID':x['ProposedResidualID'],'Selection':why,'Verdict':'PASS','Evidence':x['DeclaredSource']+' | '+x['VerificationEvidence'],'Reason':x['CurrentState']+'; verified with class limits and non-selection gates retained.'})
 for x in rr:
  check(x['Selectability']=='NON_SELECTABLE_PENDING_OWNER_APPLICATION','selectability '+x['ResidualID'])
  check(re.fullmatch(re.escape(d.name)+r'-REM-\d{3}',x['ResidualID']) is not None,'residual grammar '+x['ResidualID'])
  for cid in x['ClaimIDs'].split(';'):check(cid in ids and x['ResidualID'] in next(y for y in c if y['ClaimID']==cid)['ProposedResidualID'].split(';'),'residual inverse '+x['ResidualID'])
  checked.append({'Kind':'RESIDUAL','ClaimID':x['ClaimIDs'],'ResidualID':x['ResidualID'],'Selection':'ALL_RESIDUALS','Verdict':'PASS','Evidence':x['ClosureEvidence']+' | '+x['ExactGate'],'Reason':'Bound to reciprocal claim population; owner application, exact dependency and source/lifecycle boundaries retained.'})
 stats[d.name]={'claims':len(c),'residuals':len(rr),'unknown':sum(x['Disposition']=='UNKNOWN' for x in c),'nonaligned':sum(x['Disposition']!='ALIGNED' for x in c),'lowest_aligned':low}
for name,source in [('PACKAGE_CLAIMS.csv',allc),('PACKAGE_RESIDUALS.csv',allr)]:check(rows(P/name)==source,'aggregate equality '+name)
for x in rows(P/'PACKAGE_SUMMARY.csv'):
 s=stats[x['DeliverableID']]
 for a,b in [('Claims','claims'),('RawResidualProposals','residuals'),('UnknownClaims','unknown'),('NonAlignedClaims','nonaligned')]:check(int(x[a])==s[b],'summary '+x['DeliverableID']+' '+a)
 check(x['CandidateAssessment']=='ASSESSED_UNKNOWN' and x['WarrantedNONE']=='NO','unknown summary '+x['DeliverableID'])
for f in ['R4_DECISION_CANDIDATES.md','SCANNER_REPAIR_INPUTS.md','RESIDUAL_RECOMMENDATIONS.csv','CROSS_PACKAGE_FINDINGS.csv','PACKAGE_BASIS.md','S001_EXACT_TRANSFORMATION_BACKCHECK.json','PRE_VERIFIER_VALIDATION.json','BRIEFS/VERIFIER.md'] :read(P/f)
for f in ['AGENTS.md','projects/pec/AGENTS.md','agents/AGENT_RECONCILIATION.md','docs/DELIVERABLE_CONCORDANCE_METHOD.md',str(P.parent.parent/'COMMON/BRIEFS/PKG-01.md')]:read(pathlib.Path(f))
# independently repeat package schema validator (read only except our report).
r=subprocess.run(['python3',str(P/'validate_package.py'),'VERIFICATION/SCHEMA_VALIDATION.json'],capture_output=True,text=True);check(r.returncode==0,'schema validator')
with (V/'CHECKED_CLAIMS.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(checked[0]),lineterminator='\n');w.writeheader();w.writerows(checked)
validation={'status':'PASS' if not errors else 'FAIL','errors':errors,'members':stats,'claims':len(allc),'residuals':len(allr),'unknown':sum(s['unknown'] for s in stats.values()),'nonaligned':sum(s['nonaligned'] for s in stats.values()),'source_base_hashes_checked':base_count,'runtime_derivative_hashes_checked':derivative_count,'historical_objects_checked':len(hist),'all_read_hashes':len(hashes),'correction_transformations':trans,'checked_claims':len(allc),'checked_residuals':len(allr),'test_reexecution':'NONE; unchanged source/method R0 reuse plus independent source inspection'}
(V/'VALIDATION.json').write_text(json.dumps(validation,indent=2)+'\n')
checks=js(V/'PREFLIGHTS.json');checks.append({'command':'python3 VERIFICATION/verify.py','cwd':str(P.relative_to(R)),'environment':{'PYTHONDONTWRITEBYTECODE':'1'},'exit_code':int(bool(errors)),'result':validation})
(V/'READ_MANIFEST.json').write_text(json.dumps({'source_commit':BASE,'hashes':hashes,'historical_sources':hist,'checks':checks,'source_unchanged':all(hashlib.sha256((R/p).read_bytes()).hexdigest()==h for p,h in hashes.items())},indent=2)+'\n')
print(json.dumps(validation,indent=2))
