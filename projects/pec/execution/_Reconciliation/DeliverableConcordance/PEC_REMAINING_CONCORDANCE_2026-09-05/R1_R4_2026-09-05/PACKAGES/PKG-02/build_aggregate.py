from pathlib import Path
import csv,json,hashlib,importlib.util,sys
sys.dont_write_bytecode=True
P=Path(__file__).resolve().parent; REPO=Path.cwd()
spec=importlib.util.spec_from_file_location('validator',P/'validate_members.py'); mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
def digest(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def writecsv(name,cols,rows):
 with (P/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=cols,lineterminator='\n');w.writeheader();w.writerows(rows)
sel=json.loads((P/'SELECTED_MEMBERS.json').read_text()) if (P/'SELECTED_MEMBERS.json').exists() else {f'DEL-02-{n:02d}':str((P/'WORKERS'/f'DEL-02-{n:02d}').relative_to(REPO)) for n in range(1,8)}
claims=[]; residuals=[]; summary=[]; results=[]; census=json.loads((P/'MANAGER_CLAIM_CENSUS.json').read_text()); errors=[]
for d,loc in sel.items():
 p=REPO/loc; v=mod.validate(p); results.append(v)
 cc=list(csv.DictReader((p/'CLAIMS.csv').open()));rr=list(csv.DictReader((p/'RESIDUALS.csv').open())); claims.extend(cc); residuals.extend(rr)
 ids={x['ClaimID'] for x in cc}; expected=next(x for x in census if x['DeliverableID']==d); mandatory={d+'::'+x for x in expected['mandatory_ids']}; missing=sorted(mandatory-ids)
 if missing:errors.append({'deliverable':d,'missing_mandatory':missing})
 unknown=sum(x['Disposition']=='UNKNOWN' for x in cc);summary.append({'DeliverableID':d,'Claims':len(cc),'RawResidualProposals':len(rr),'UnknownClaims':unknown,'NonAlignedClaims':sum(x['Disposition']!='ALIGNED' for x in cc),'CandidateAssessment':'ASSESSED_UNKNOWN' if unknown else ('ASSESSED_WITH_RESIDUALS' if rr else 'ASSESSED_NO_RESIDUAL'),'WarrantedNONE':'FALSE' if unknown or rr else 'REQUIRES_SEMANTIC_WARRANT','SelectedClaims':str((p/'CLAIMS.csv').relative_to(REPO)),'SelectedClaimsSHA256':digest(p/'CLAIMS.csv'),'SelectedResiduals':str((p/'RESIDUALS.csv').relative_to(REPO)),'SelectedResidualsSHA256':digest(p/'RESIDUALS.csv')})
writecsv('PACKAGE_CLAIMS.csv',mod.C,claims);writecsv('PACKAGE_RESIDUALS.csv',mod.R,residuals);writecsv('PACKAGE_SUMMARY.csv',list(summary[0]),summary)
(P/'AGGREGATE_VALIDATION.json').write_text(json.dumps({'source_commit':mod.BASE,'members':results,'mandatory_coverage_errors':errors,'counts':{'members':len(summary),'claims':len(claims),'residuals':len(residuals),'unknowns':sum(x['Disposition']=='UNKNOWN' for x in claims)},'pass':not errors and all(x['pass'] for x in results)},indent=2)+'\n')
print((P/'AGGREGATE_VALIDATION.json').read_text())
