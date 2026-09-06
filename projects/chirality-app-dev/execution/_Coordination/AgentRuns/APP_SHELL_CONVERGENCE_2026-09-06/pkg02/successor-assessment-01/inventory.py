from pathlib import Path
import hashlib,json,csv,subprocess,datetime,sys
r=Path.cwd(); p=r/'projects/chirality-app-dev'; run=p/'execution/_Coordination/AgentRuns/APP_SHELL_CONVERGENCE_2026-09-06/pkg02'; out=Path(sys.argv[1]) if len(sys.argv)>1 else run/'successor-assessment-01'; out.mkdir(parents=True,exist_ok=True)
files=[r/'AGENTS.md',p/'AGENTS.md',p/'loop/LOOP_INIT.md']
files+=list((p/'execution/_Coordination/_DECISIONS').glob('D-APP-59*.md'))+list((p/'execution/_Coordination/_DECISIONS').glob('D-APP-60*.md'))+list((p/'execution/_Coordination/_DECISIONS').glob('D-APP-64*.md'))+list((p/'execution/_Coordination/_DECISIONS').glob('D-APP-108*.md'))+list((p/'execution/_Coordination/_DECISIONS').glob('D-APP-120*RULING*.md'))
base=p/'execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working'
files+=list(base.glob('*/_STATUS.md'))+list(base.glob('*/Dependencies.csv'))
f=next((p/'execution').glob('PKG-07*/1_Working/DEL-07-03*/_STATUS.md')); files += [f,f.parent/'_run_records/TASK_RUN_2026-09-05_APP_LOOP_SHELL_WORKFLOW_CONTRACT.md']
files += [run/x for x in ['integration-01/SOURCE_MANIFEST_v5.json','source-review-06/RETURN.md','browser-integration-04/RETURN.md','browser-integration-05/RETURN.md','SOURCE_REVIEW_ACCEPTANCE_v5.md','final-checks-v5-host.json','final-premerge-v5/summary.json','dependency-review-01/RETURN.md']]
files+=list((run/'dependency-candidate-01').glob('ci-*.json'))
files += [p/'frontend/src/components/woven-dialogue/navigator.tsx',p/'frontend/src/components/woven-dialogue/woven-dialogue-shell.tsx',p/'frontend/src/lib/runtime-client/runtime-daemon-harness-port.ts',p/'frontend/src/lib/woven-dialogue/woven-workspace-state.ts']
files += [p/'plans/shell-redesign_2026-09-04/03_TARGET_SPEC.md',p/'plans/shell-redesign_2026-09-04/04_IMPLEMENTATION_PLAN.md']
inv=[dict(path=str(f.relative_to(r)),sha256=hashlib.sha256(f.read_bytes()).hexdigest(),bytes=f.stat().st_size) for f in sorted(set(files))]
(out/'INPUT_INVENTORY.json').write_text(json.dumps({'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'repo_root':str(r),'head':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'observed_origin_main':subprocess.check_output(['git','rev-parse','origin/main'],text=True).strip(),'inputs':inv},indent=2)+'\n')
items=[]; rows=[]
for f in base.glob('*/_STATUS.md'):
 lines=f.read_text().splitlines()
 for i,l in enumerate(lines):
  if any(('**'+x+'**') in l for x in ['DEL-02-01-V3-01','DEL-02-01-V3-02','DEL-02-01-V3-03','DEL-02-02-V3-04','DEL-02-04-V3-01','DEL-02-05-V3-05']):
   end=next((j for j in range(i+1,len(lines)) if lines[j].startswith('- **') or lines[j].startswith('## ')),len(lines))
   items.append({'path':str(f.relative_to(r)),'start_line':i+1,'verbatim_lines':lines[i:end]})
for f in base.glob('*/Dependencies.csv'):
 for row in csv.DictReader(f.open()):
  if row['DependencyClass']=='EXECUTION': rows.append({'path':str(f.relative_to(r)),'row':row})
(out/'LIVE_CRITERIA.json').write_text(json.dumps({'items':items,'execution_rows':rows},indent=2)+'\n')
manifest=json.loads((run/'integration-01/SOURCE_MANIFEST_v5.json').read_text())
verification=[{'path':m['path'],'expected':m['sha256'],'actual':hashlib.sha256((r/m['path']).read_bytes()).hexdigest()} for m in manifest['members']]
(out/'SOURCE_VERIFICATION.json').write_text(json.dumps({'members':verification,'all_match':all(m['expected']==m['actual'] for m in verification)},indent=2)+'\n')
print('Inputs',len(inv),'source hashes match',all(m['expected']==m['actual'] for m in verification))
