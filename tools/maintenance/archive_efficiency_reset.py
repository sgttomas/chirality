"""Phase-5 archive selection; dry-run by default, --apply only after batch review."""
from pathlib import Path
import subprocess,json,collections,re
root=Path.cwd(); paths=subprocess.check_output(['git','ls-files','-z']).decode().split('\0')
chosen=[];counts=collections.Counter()
for path in paths:
 if not path:continue
 parts=Path(path).parts;reason=None
 execution=parts[0]=='execution' or (len(parts)>2 and parts[0]=='projects' and parts[2]=='execution')
 if execution:
  for marker in ['AgentRuns','_run_records','_Reconciliation','_Evaluation']:
   if marker in parts:reason=marker;break
  if reason is None and '_ScopeChange' in parts and any(x.lower() in ['before','after','preimages','postimages','repair_preimages','checkpoint_snapshots','_postacceptancevalidation','preacceptance','prestate','poststate'] for x in parts):reason='scope snapshots'
  if reason is None and '_DAG' in parts:
   i=parts.index('_DAG');version=parts[i+1] if len(parts)>i+1 else ''
   keep=('DAG-011' if path.startswith('projects/chirality-piping/') else 'DAG-004' if path.startswith('projects/chirality-app-v4/') else None)
   if version.startswith('DAG-') and keep and version!=keep:reason='superseded DAG'
   if version in ['_Candidates','PHYSICS_UI_EXECUTION_20260908_CANDIDATE']:reason='DAG candidates'
  name=parts[-1]
  if reason is None and (name.startswith(('LOOP_RECEIPTS','ROOT_RULINGS','NOTICE','STEER','WORKPLAN')) or any(x in ['Notices','Steers','Workplans'] for x in parts)):reason='closed coordination records'
 if path.startswith('plans/evidence/'):reason='plan evidence'
 if path.startswith('docs/governance_harness/') and any(x in parts for x in ['_PROPOSALS','tranche_manifests']):reason='governance records'
 if path.startswith('docs/') and re.search(r'(?:^|/)D-GOV[-_]',path):reason='D-GOV history'
 if reason:chosen.append(path);counts[reason]+=1
if '--list' in __import__('sys').argv:
 print(json.dumps(chosen, indent=2))
print(dict(counts));print('total',len(chosen))
if '--apply' in __import__('sys').argv:
 baseline = subprocess.check_output(['git','rev-parse','archive/pre-efficiency-cleanup-2026-10-09^{commit}'], text=True).strip()
 if baseline != '24e9117b9c2d9d10f57642da4eef0d13c90bb166':
  raise SystemExit('Recovery tag does not name the reviewed pre-removal baseline')
 changed = set(subprocess.check_output(['git','diff','--name-only',baseline,'--'],text=True).splitlines())
 if changed.intersection(chosen):
  raise SystemExit('An archive candidate differs from the recovery baseline; review before removing it')
 for path in chosen:
  p=root/path
  if p.is_file() or p.is_symlink():p.unlink()
 # Remove now-empty directories only; don't recursively erase untracked files.
 for p in sorted({parent for x in chosen for parent in (root/x).parents if parent!=root and parent.is_relative_to(root)},key=lambda x:len(x.parts),reverse=True):
  try:p.rmdir()
  except OSError:pass
