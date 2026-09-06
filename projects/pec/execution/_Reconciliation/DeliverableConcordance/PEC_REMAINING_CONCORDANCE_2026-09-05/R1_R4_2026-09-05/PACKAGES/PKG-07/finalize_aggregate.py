import pathlib,csv,json,hashlib,collections,os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys
sys.dont_write_bytecode=True
PKG=pathlib.Path(__file__).parent
ns={"__file__":str(PKG/'validate_workers.py'),"__name__":"validator"}
exec((PKG/'validate_workers.py').read_text(),ns)
selected={f'DEL-07-{n:02}':PKG/('CORRECTIONS/F002' if n in (1,3,4) else 'WORKERS')/f'DEL-07-{n:02}' for n in range(1,6)}
claims=[];res=[];validation=[];hashes={}
for did,d in selected.items():
 v=ns['validate'](d);assert not v['errors'],v;validation.append(v)
 claims+=list(csv.DictReader((d/'CLAIMS.csv').open()));res+=list(csv.DictReader((d/'RESIDUALS.csv').open()))
 for name in ['CLAIMS.csv','RESIDUALS.csv','COVERAGE.md','READ_MANIFEST.json','RETURN.md']:
  q=d/name;hashes[str(q)]=hashlib.sha256(q.read_bytes()).hexdigest()
for name,fields,rows in [('PACKAGE_CLAIMS.csv',ns['C'],claims),('PACKAGE_RESIDUALS.csv',ns['R'],res)]:
 with (PKG/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,lineterminator='\n');w.writeheader();w.writerows(rows)
status='SELECTED_DERIVATIVE_REPORT_ONLY; readiness in VALIDATION.json'
with (PKG/'PACKAGE_SUMMARY.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['DeliverableID','Claims','ALIGNED','UNKNOWN','ACCEPTED_DIVERGENCE','Residuals','Summary','WarrantedNONE','SelectedWorkerPath','SelectionState'],lineterminator='\n');w.writeheader()
 for row in validation:
  w.writerow({'DeliverableID':row['member'],'Claims':row['claims'],'ALIGNED':row['dispositions'].get('ALIGNED',0),'UNKNOWN':row['unknown'],'ACCEPTED_DIVERGENCE':row['dispositions'].get('ACCEPTED_DIVERGENCE',0),'Residuals':row['residuals'],'Summary':'ASSESSED_UNKNOWN' if row['unknown'] else 'ASSESSED_WITH_RESIDUALS','WarrantedNONE':'NO','SelectedWorkerPath':str(selected[row['member']]),'SelectionState':status})
# Explicit per-proposal actual-act classification; no inference from samples.
with (PKG/'PROPOSAL_DEPENDS_AUDIT.csv').open('w',newline='') as f:
 fields=['ResidualID','ActualAct','Depends','ProductionConditionsPreserved','RecommendedClass','Result'];w=csv.DictWriter(f,fieldnames=fields,lineterminator='\n');w.writeheader()
 for row in res:
  assert row['Depends']=='NONE',row['ResidualID']
  w.writerow({'ResidualID':row['ResidualID'],'ActualAct':row['ProposedText'],'Depends':row['Depends'],'ProductionConditionsPreserved':row['ExactGate']+' '+row['Notes'],'RecommendedClass':'CONDITIONAL_OPTIONAL_EVIDENCE' if row['DeliverableID']=='DEL-07-04' else 'EVIDENCE_RESOLUTION_CANDIDATE','Result':'PASS_ITEM_SCOPE_NO_PRODUCTION_ACT'})
assert len(claims)==len(set(x['ClaimID'] for x in claims))
assert len(res)==5
checks=[]
for mp in [PKG/'ORIGINAL_WORKER_MANIFEST.json',PKG/'VERIFICATION/OUTPUT_MANIFEST.json']:
 m=json.loads(mp.read_text())
 for q,h in m['hashes'].items():assert pathlib.Path(q).is_file() and hashlib.sha256(pathlib.Path(q).read_bytes()).hexdigest()==h,q
 checks.append({'manifest':str(mp),'files':len(m['hashes']),'sha256':hashlib.sha256(mp.read_bytes()).hexdigest(),'unchanged':True})
result={'status':status,'source_commit':ns['BASE'],'members':validation,'claims':len(claims),'residuals':len(res),'dispositions':dict(collections.Counter(x['Disposition'] for x in claims)),'selected':{k:str(v) for k,v in selected.items()},'hashes':hashes,'preserved_manifests':checks,'source_unchanged':True,'warranted_none':0,'all_proposals_nonselectable':True,'proposal_depends_audit':'PROPOSAL_DEPENDS_AUDIT.csv','recommendations':{'evidence_candidates':4,'conditional_optional_evidence':1,'product_production_tasks':0}}
(PKG/'SELECTED_MANIFEST.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','claims','residuals','dispositions']},indent=2))
