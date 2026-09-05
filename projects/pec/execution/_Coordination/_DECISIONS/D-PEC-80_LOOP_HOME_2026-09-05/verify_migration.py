from pathlib import Path
import csv,hashlib,subprocess,json,shutil
root=Path.cwd(); e=root/'projects/pec/execution/_Coordination/_DECISIONS/D-PEC-80_LOOP_HOME_2026-09-05'
sha=lambda b:hashlib.sha256(b).hexdigest()
base='7458e9c1eb9399ed259da464207d9a507acdea2e'; a='aa17255b56f6b8e405cc633e9e88731f797bff31'
rows=list(csv.DictReader((e/'RELOCATION_MAP.csv').open())); exceptions={'projects/pec/loop/LOOP_INIT.md','projects/pec/loop/LOOP_RECEIPTS.md'}
for r in rows:
 assert sha(subprocess.check_output(['git','show',base+':'+r['old_path']]))==r['before_sha256']
 assert sha(subprocess.check_output(['git','show',a+':'+r['new_path']]))==r['after_sha256']==r['before_sha256']
 if r['new_path'] not in exceptions: assert sha(Path(r['new_path']).read_bytes())==r['before_sha256'],r['new_path']
assert not Path('_DomainEngines/pec').exists()
assert sha(Path('projects/pec/loop/LOOP_RECEIPTS.md').read_bytes()[:426714])=='153732e389a1dd948805dd71150f63d865ef3c70cb8b8f8230a36b836dda0dd7'
(e/'INTEGRITY_CHECKS.json').write_text(json.dumps({'basis':base,'corrected_migration_commit':a,'moved_files':len(rows),'all_migration_sha256_equal':True,'final_historical_files_unchanged':335,'final_exceptions':sorted(exceptions),'receipt_frozen_prefix_unchanged':True,'old_directory_absent':True},indent=2)+'\n')
inv=list(csv.DictReader((e/'REFERENCE_INVENTORY.csv').open())); oldnew={r['old_path']:r['new_path'] for r in rows}
allowed={(oldnew.get(r['path'],r['path']),r['original_text']) for r in inv if r['class']=='immutable record'}
files=subprocess.check_output(['git','ls-files','--cached','--others','--exclude-standard','-z']).decode().split('\0');hits=[];bad=[]
for name in sorted(set(files)-{''}):
 p=Path(name)
 if not p.is_file() or p.is_symlink():continue
 try:s=p.read_text()
 except UnicodeError:continue
 for n,line in enumerate(s.splitlines(),1):
  if '_DomainEngines/pec/' not in line:continue
  if (name,line) in allowed:cl='preserved immutable record'
  elif name.startswith(str(e.relative_to(root))) or name=='projects/pec/execution/_Coordination/_DECISIONS/D-PEC-80_loop_home_and_instruction_surface_2026-09-05.md':cl='new sealed migration evidence / relocation record'
  elif name=='projects/pec/loop/LOOP_INIT.md' and line.startswith('Historical receipts refer to the old '):cl='historical locator annotation (required by owner)'
  elif name=='projects/pec/loop/LOOP_RECEIPTS.md' and 'Stale-Map-Delta' in line:cl='new immutable receipt stale-map delta'
  else:cl='UNCLASSIFIED';bad.append([name,n,line])
  hits.append([name,n,sha(line.encode()),cl])
with (e/'FINAL_REFERENCE_INVENTORY.csv').open('w') as f:
 w=csv.writer(f,lineterminator='\n');w.writerow(['path','line','line_sha256','classification']);w.writerows(hits)
(e/'FINAL_REFERENCE_SUMMARY.json').write_text(json.dumps({'scan':'git ls-files --cached --others --exclude-standard; all regular UTF-8 files, including hidden repository paths; binary/symlink/excluded build artifacts omitted','matching_lines':len(hits),'matching_files':len({r[0] for r in hits}),'unclassified':bad},indent=2)+'\n')
print('Integrity PASS; references',len(hits),'unclassified',len(bad));print(json.dumps(bad,indent=2))
