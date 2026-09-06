"""Run-local evidence check; not the standing D-14 currency capability."""
from pathlib import Path
import csv, hashlib, json, re, subprocess, datetime
R=Path(__file__).resolve().parents[5]
E=Path(__file__).resolve().parent
P=R/'execution/_ScopeChange/SCA-005_2026-09-06_GATE4_PLAN'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
rows=[r for r in csv.DictReader((P/'WRITE_TARGETS.csv').open()) if r['Owner']=='HELPS_HUMANS' and r['ApprovedSource']]
checks=[]
for x in rows:
 p=R/x['Target']; checks.append({'path':x['Target'],'expected_sha256':x['ApprovedSHA256'],'actual_sha256':sha(p) if p.is_file() else None,'matches':p.is_file() and sha(p)==x['ApprovedSHA256']})
prior=R/'execution/_ScopeChange/SCA-005_2026-09-05_2344/ADDENDUM_REVIEW/ACCEPTED_ROOT_PRD_REV8.md'
prior_ok=sha(prior)=='d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4'
b=list(csv.DictReader((R/'execution/_Coordination/GovernanceControls/_AUTHORITY_BINDINGS.csv').open()))
refrows=[]
for x in b:
 for k in ['ControllingInstrument','ExactPredicateRegister']:
  for rel in x[k].split(';'):
   p=R/rel;refrows.append({'control':x['ControlID'],'role':k,'path':rel,'exists':p.is_file(),'sha256':sha(p) if p.is_file() else None})
text=(R/'docs/PRD_ROOT.md').read_text();stable=[line for line in text.splitlines() if re.match(r'^\| \*\*[NODE]-\d+\*\* \|',line)]
invariants=sorted(set(re.findall(r'\bK-[A-Z]+-\d+\b','\n'.join(stable))));contract=(R/'docs/CONTRACT.md').read_text();missing=[i for i in invariants if i not in contract]
expected_edges=[r for r in csv.DictReader((P/'DEPENDENCY_DISTRIBUTION.csv').open()) if r['Predecessor'].startswith('root::')]
actual_edges=list(csv.DictReader((R/'execution/_Coordination/GovernanceControls/_DEPENDENCIES.csv').open()))
r=subprocess.run(['python3','-B','execution/_Reconciliation/References/reconcile_authority_corpus.py','status'],cwd=R/'projects/chirality-app-dev',capture_output=True,text=True)
(E/'APP_CORPUS_STATUS_POST_CUTOVER.txt').write_text(r.stdout+r.stderr)
result={'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'basis':subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip(),'payload_checks':checks,'all_52_payloads_match':len(checks)==52 and all(x['matches'] for x in checks),'immutable_revision8_preserved':prior_ok,'control_bindings':len(b),'reference_checks':refrows,'references_resolve':all(x['exists'] for x in refrows),'stable_requirement_rows':len(stable),'stable_invariant_ids':invariants,'invariant_ids_not_found_in_contract':missing,'exact_two_governance_edges':actual_edges==expected_edges and len(actual_edges)==2,'app_corpus_status_exit':r.returncode,'standing_D14_checker_built':False,'gate5_owner_confirmation':'PENDING'}
(E/'APPLIED_AUTHORITY_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['payload_checks','reference_checks','stable_invariant_ids']},indent=2))
raise SystemExit(0 if result['all_52_payloads_match'] and prior_ok and result['references_resolve'] and result['exact_two_governance_edges'] and r.returncode==0 else 1)
