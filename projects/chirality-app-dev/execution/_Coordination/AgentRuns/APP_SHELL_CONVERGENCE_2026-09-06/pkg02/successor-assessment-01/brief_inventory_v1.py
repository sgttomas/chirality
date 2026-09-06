from pathlib import Path
import hashlib,json,re,subprocess,sys
r=Path.cwd();p=r/'projects/chirality-app-dev';d=p/'execution/_Coordination/AgentRuns/APP_SHELL_CONVERGENCE_2026-09-06/pkg02/successor-assessment-01';o=Path(sys.argv[1]) if len(sys.argv)>1 else d;o.mkdir(parents=True,exist_ok=True)
paths=[p/'plans/shell-redesign_2026-09-04'/n for n in ['mock/chirality-shell-mocks.html','01_DECISIONS.md','03_TARGET_SPEC.md','04_IMPLEMENTATION_PLAN.md']]
paths += [p/'frontend/src'/n for n in ['lib/workspace/governed-workflow.ts','lib/woven-dialogue/woven-workspace-state.ts','lib/workspace/filesystem.ts','components/shell/chat-panel.tsx','components/woven-dialogue/right-panel.tsx','components/woven-dialogue/woven-dialogue-shell.tsx','app/api/working-root/file/route.ts','app/api/working-root/file/file-policy.ts','app/api/working-root/deliverable/status/transition/route.ts']]
paths+=list((p/'execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working').glob('*/_STATUS.md'))
paths += [p/'execution/_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/Decision_Log.md']
paths+=list((p/'execution/_Coordination/_DECISIONS').glob('D-APP-108*md'))+list((p/'execution/_Coordination/_DECISIONS').glob('D-APP-120_RULING*md'))
inputs=[{'path':str(f.relative_to(r)),'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in sorted(set(paths))]
(o/'BRIEF_INPUT_INVENTORY_v1.json').write_text(json.dumps({'head':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'inputs':inputs},indent=2)+'\n')
f=paths[0];txt=f.read_text();start=txt.index('  var STEPS = [');end=txt.index('\n  ];',start)+5;steps=txt[start:end]
(o/'WALKTHROUGH_STEPS_EXTRACT_v1.txt').write_text(steps+'\n')
scenes=[{'scene':i+1,'title':m.group(1),'state_literal':m.group(2)} for i,m in enumerate(re.finditer(r"\{ t: '([^']+)', s: (\{[^\n]+\}),",steps))]
(o/'WALKTHROUGH_SCENES_v1.json').write_text(json.dumps({'source':str(f.relative_to(r)),'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'one_based_scenes':scenes},indent=2)+'\n')
print(len(inputs),'inputs;',len(scenes),'scenes; mock SHA',hashlib.sha256(f.read_bytes()).hexdigest())
