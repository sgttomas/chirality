from pathlib import Path
import subprocess,sys,os,json,hashlib,csv
root=Path.cwd(); E=Path('projects/pec/execution/_Coordination/_DECISIONS/D-PEC-80_LOOP_HOME_2026-09-05')
phase=sys.argv[1];out=E/phase;out.mkdir(exist_ok=True)
py='/Users/ryan/.local/share/mise/installs/python/3.13/bin/python3.13'
commands=[
('entrypoints',['python3','tools/validation/validate_instruction_entrypoints.py','.'],'.'),
('receipts',['python3','tools/validation/validate_pec_loop_receipts.py','--repo-root','.'],'.'),
('task-live',['python3','tools/taskmgmt/taskmgmt.py','validate','--register','projects/pec/execution/_Coordination/_TaskManagement/REGISTER.csv'],'.'),
('task-archive',['python3','tools/taskmgmt/taskmgmt.py','validate','--register','projects/pec/execution/_Coordination/_TaskManagement/REGISTER_CLOSED.csv'],'.'),
('tests',[py,'-m','pytest','-q','tools/validation/test_validate_instruction_entrypoints.py','tools/validation/test_validate_pec_loop_receipts.py','tools/practitioner_harness/test_bridge_status.py','tools/taskmgmt/test_taskmgmt.py'],'.'),
('self-check',['python3','tools/practitioner_harness/harness.py','self-check'],'.'),
('api-contract',[py,'-m','unittest','discover','-s','v2/tests/contracts/api','-p','test_*.py'],'projects/pec'),
('loop-registry',[py,'-m','unittest','discover','-s','v2/tests/config','-p','test_*.py'],'projects/pec'),
('core-posture',[py,'v2/tools/check_service_core_posture.py','--config','v2/config/service_core_posture.json','--workflow','software-workflow.json'],'projects/pec'),
('whitespace',['git','diff','--check'],'.'),
]
results=[]
for label,cmd,cwd in commands:
 p=subprocess.run(cmd,cwd=cwd,capture_output=True,text=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
 (out/f'{label}.stdout').write_text(p.stdout);(out/f'{label}.stderr').write_text(p.stderr)
 results.append({'label':label,'command':cmd,'cwd':cwd,'exit_code':p.returncode,'stdout':f'{label}.stdout','stderr':f'{label}.stderr'})
 print(label,p.returncode,flush=True)
(out/'CHECKS.json').write_text(json.dumps({'head':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'python3':subprocess.check_output(['python3','--version'],text=True).strip(),'test_python':subprocess.check_output([py,'--version'],text=True).strip(),'PYTHONDONTWRITEBYTECODE':'1','checks':results},indent=2)+'\n')
sys.exit(any(r['exit_code'] for r in results))
