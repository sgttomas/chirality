# Prior-ruling decomposition application: retirement and SOW-079

APPLIED; bounded checks PASS; parent independent review and integration pending.

Author: Codex native TASK `/root/reconciliation_closure_boundary`, parent HELP_HUMAN; no descendants. Shared-checkout write limits are instruction-enforced. Parent authorized the two source files below plus this report. After the TASK retirement return, HELP_HUMAN applied the existing D-GOV-43/D-APP-127 A2 observation wording to SOW-079 and its already-assigned DEL-04-01 carrier in those same files, then applied the affected OBJ-004, OI-001/OI-007 and SOW-045/075/076 current-applicability corrections identified during independent review, and reran the preservation checks. No product execution, Git mutation, new SCA, pointer change, dependency change, lifecycle change or retired-folder write occurred. Read-only Git object reads below recover the exact preimages; they do not alter repository state.

D-GOV-43 accepted revision-3 item 11 authorizes the named App scope/deliverable/hold application without another retirement vote; its IMPACT.md chain 2 retires the installer. D-APP-127 lines 159–175 applies retirement, recreates nothing and preserves the folder/SoW as immutable history. This completes that prior act's carrier propagation, not a new snapshot acceptance. SCA-APP-009/010 derivative closure stays open.

Both SOW-080 rows are OUT; DEL-09-07 remains its historical carrier with stable ID. OBJ-008, OI-003/OI-007 and current M-work wording no longer require installer work. The three invariant mappings K-VALIDATE-1/K-CONTROL-1/K-STORE-2 remove only installer enforcement/validation membership, preserving all other fields/obligations and historical provenance. Previous decomposition pins remain, with an additional exact current-application hash on the three changed rows. Retained identity/envelope totals are explicitly distinguished from selectable work. No successor requirement/deliverable is invented.

The initial inline patch/check command successfully applied the two files and passed mapping, parity, stable-ID, historical-decision and retired-folder equality predicates, but exited 1 because it trusted the prose's 81-invariant/48-family census. Actual preimage and postimage both contain **83 unique invariants / 50 families**. The parent then explicitly authorized lifting the four current 81/48 prose snapshots to the authoritative register/current source-coverage check, preserving completeness and all actual rows. That additional granularity repair is applied; historical DEC-022 and revision-history census records remain unchanged. The verification below checks exact pre/post identity, historical preservation and removal of the stale current snapshots; it does not claim a wider source-coverage audit. The additional SOW-079 propagation preserves both IN statuses, its DEL-04-01 assignment and App observation/conformance purpose, while removing the retired supplier-admission framing. It introduces no new scope or implementation claim. Other unrelated architecture/proof wording is not silently certified by these bounded checks.

The independent review found obsolete OI-001 Anthropic qualification and OI-007 supply/pilot prerequisites. HELP_HUMAN repaired these and retained their historical Root DEL-02-07/08 identities. The first expanded check correctly failed when those historical reference IDs had been dropped; the repair preserves them rather than weakening the identity check. Current Codex configuration/policy applicability is explicit in the affected scope descriptions and a source-qualified applicability note; membership and assignment are unchanged.

The fresh scope-closure auditor also found already-ruled Q15/Q16 still presented as owner questions and an operative hosted-consent description. HELP_HUMAN applied D-APP-108 in SOW-081/OI-008 and D-GOV-43/D-APP-127 in PKG-04/DEL-02-05, preserving all assignments, historical external IDs and surviving current interface/evidence duties. These affected edits require the auditor’s independent backcheck; no new acceptance act is implied.

The auditor’s workflow-path finding is also applied: current SOW-081/vocabulary use the package `<name>/WORKFLOW.md` prescribed by current Root/App instructions and accepted D-GOV-43 item 10. Flat documents retain historical compatibility. This does not claim blanket exact-byte D-GOV-42 acceptance, change package membership or waive workflow currency/advance duties.

## Reproduction and actual evidence

The following command was executed through Python `exec` by the TASK for retirement and rerun by HELP_HUMAN after the SOW-079 addition; the JSON below is the final observed output. It can be rerun from the repository root as `python3 -` with the code below on standard input. It reads frozen preimages, checks the actual postimages, and performs no writes. Output/exit: all predicates true, exit 0.

```python
from pathlib import Path
import csv,io,re,hashlib,json,subprocess
basis='1b5adbf50142a4c01c454c62a31dfcdc60da1894'
b=Path('projects/chirality-app-dev'); d=b/'execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md'; c=d.with_name('contract_invariant_coverage_register.csv')
h=lambda x:hashlib.sha256(x).hexdigest()
old=lambda p:subprocess.check_output(['git','show',basis+':'+str(p)])
pre={str(p):old(p) for p in [d,c]}; post={str(p):p.read_bytes() for p in [d,c]}
assert h(pre[str(d)])=='c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61'
assert h(pre[str(c)])=='63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca'
a=list(csv.DictReader(io.StringIO(pre[str(c)].decode()))); z=list(csv.DictReader(io.StringIO(post[str(c)].decode())))
chosen={'K-VALIDATE-1','K-CONTROL-1','K-STORE-2'}; allowed={'AppDeliverableIDs','ValidationSurfaces','EnforcementSurfaces','RationaleEvidenceAnchor','AppDecompositionBasis'}
checks={}
checks['invariant_keys_and_families_preserved']=[(x['InvariantID'],x['InvariantFamily']) for x in a]==[(x['InvariantID'],x['InvariantFamily']) for x in z]
checks['unique_invariants']=len({x['InvariantID'] for x in z})==len(z)
checks['three_mapping_rows_only']=all(x==y if x['InvariantID'] not in chosen else all(x[k]==y[k] for k in x if k not in allowed) for x,y in zip(a,z))
checks['three_rows_changed']={x['InvariantID'] for x,y in zip(a,z) if x!=y}==chosen
checks['no_active_installer_membership']=all('DEL-09-07' not in x[k] for x in z if x['InvariantID'] in chosen for k in ['AppDeliverableIDs','ValidationSurfaces'])
def mapping(txt):
 reverse={}; ledger={}; states=[]; section=''
 for line in txt.splitlines():
  if line.startswith('## '):section=line
  if not line.startswith('|'):continue
  row=[x.strip() for x in line.strip('|').split('|')]
  if section=='## 8. Deliverables' and len(row)==10 and re.fullmatch(r'DEL-\d\d-\d\d',row[0]):
   for s in re.findall(r'SOW-\d{3}',row[6]):reverse.setdefault(s,set()).add(row[0])
  if section=='## 9. Scope Ledger' and len(row)==10 and re.fullmatch(r'SOW-\d{3}',row[0]):ledger[row[0]]=set(re.findall(r'DEL-\d\d-\d\d',row[5]))
  if row[0]=='SOW-080':states.append(row[1])
 return reverse,ledger,states
u=pre[str(d)].decode();v=post[str(d)].decode();m=mapping(u);n=mapping(v)
checks['full_forward_reverse_parity']=n[0]==n[1]
checks['all_assignment_edges_preserved']=m[:2]==n[:2]
checks['retired_boundary_only']=n[2]==['OUT','OUT'] and n[1]['SOW-080']=={'DEL-09-07'}
checks['stable_identifiers']=all(set(re.findall(q,u))==set(re.findall(q,v)) for q in [r'\bSOW-\d{3}\b',r'\bDEL-\d\d-\d\d\b',r'\bOBJ-\d{3}\b'])
checks['historical_decision_log_preserved']=u.split('## 12. Decision Log')[1].split('## 13.')[0]==v.split('## 12. Decision Log')[1].split('## 13.')[0]
ret=b/'execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-07_Two-Job_Runtime-Control_Installer_Migration_and_Rollback'
paths=subprocess.check_output(['git','ls-tree','-r','--name-only',basis,'--',str(ret)],text=True).splitlines()
expected={p:h(old(p)) for p in paths};actual={str(p):h(p.read_bytes()) for p in sorted(ret.rglob('*')) if p.is_file()}
checks['entire_retired_folder_identical_to_basis']=expected==actual
checks['SOW079_assignment_and_status_preserved']=n[1]['SOW-079']=={'DEL-04-01'} and all(row.split('|')[2].strip()=='IN' for row in v.splitlines() if row.startswith('| SOW-079 |'))
checks['SOW079_current_basis_applied']=sum('topology A2' in row for row in v.splitlines() if row.startswith('| SOW-079 |'))==2
checks['current_census_snapshot_lifted']=not re.search(r'81(?: CONTRACT| unique|-ID)|48-family',v.split('## 12. Decision Log')[0])
checks['affected_current_applicability_applied']=all(x in v for x in ['Codex-owned operational history','User-selected approval and sandbox policy','Current stock Codex/A2 protocol','prior Root DEL-02-08 supply and DEL-02-07 admission links remain historical'])
checks['later_rulings_not_reopened']=all(x in v for x in ['D-APP-108 already rules Q15','D-APP-108 rules Q15 as a read-only currency line','retired hosted admission and per-root brokerage/consent are not current prerequisites'])
checks['current_workflow_package_identity_applied']='.chirality/workflows/<slug>.md' not in v.split('## 12. Decision Log')[0] and '.chirality/workflows/<name>/WORKFLOW.md' in v
assert all(checks.values()),checks
result={'checks':checks,'invariants':len(z),'families':len({x['InvariantFamily'] for x in z}),'scope_ids':len(n[1]),'retired_files':len(actual),'retired_manifest_sha256':h(json.dumps(actual,sort_keys=True,separators=(',',':')).encode()),'source_hashes':{str(p):{'before':h(pre[str(p)]),'after':h(post[str(p)])} for p in [d,c]}}
print(json.dumps(result,indent=2))
```

```json
{
  "checks": {
    "invariant_keys_and_families_preserved": true,
    "unique_invariants": true,
    "three_mapping_rows_only": true,
    "three_rows_changed": true,
    "no_active_installer_membership": true,
    "full_forward_reverse_parity": true,
    "all_assignment_edges_preserved": true,
    "retired_boundary_only": true,
    "stable_identifiers": true,
    "historical_decision_log_preserved": true,
    "entire_retired_folder_identical_to_basis": true,
    "SOW079_assignment_and_status_preserved": true,
    "SOW079_current_basis_applied": true,
    "current_census_snapshot_lifted": true,
    "affected_current_applicability_applied": true,
    "later_rulings_not_reopened": true,
    "current_workflow_package_identity_applied": true
  },
  "invariants": 83,
  "families": 50,
  "scope_ids": 84,
  "retired_files": 25,
  "retired_manifest_sha256": "91b3785dcdd539d6388493ff10b089a00a0251ef7bf3fda1238e83546c468459",
  "source_hashes": {
    "projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md": {
      "before": "c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61",
      "after": "9261ce30f933a0b72364a5af09c8aeed9208372774959864ff24a805126ea8a6"
    },
    "projects/chirality-app-dev/execution/_Decomposition/contract_invariant_coverage_register.csv": {
      "before": "63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca",
      "after": "918e475a48899d18755139027e61db200d23a531e48ed9f969c526dd842fa944"
    }
  }
}
```
