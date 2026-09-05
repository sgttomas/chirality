from pathlib import Path
import subprocess,csv,hashlib,json
E=Path('projects/pec/execution/_Coordination/_DECISIONS/D-PEC-80_LOOP_HOME_2026-09-05');D=E/'D_RETIREMENT';sha=lambda b:hashlib.sha256(b).hexdigest()
ret=list(csv.DictReader((D/'RELOCATION_MAP.csv').open()));moves={r['old_path']:r['new_path'] for r in ret}
for r in ret:
 assert sha(Path(r['new_path']).read_bytes())==r['before_sha256']==r['after_sha256']
 assert sha(subprocess.check_output(['git','show','c241cfe84911c7584ec36a2d1c58bcb0fb03f2e2:'+r['old_path']]))==r['before_sha256']
for r in csv.DictReader((E/'RELOCATION_MAP.csv').open()):
 p=moves.get(r['new_path'],r['new_path'])
 if p not in {'projects/pec/loop/LOOP_INIT.md','projects/pec/loop/LOOP_RECEIPTS.md'}:assert sha(Path(p).read_bytes())==r['before_sha256'],p
assert not list(Path('projects/pec/loop').glob('WORKPLAN_*.md'));assert not list(Path('projects/pec/loop').glob('PLAN_CURRENCY*'))
plan=Path('projects/pec/plans/workplans/WORKPLAN_2026-07-24_pec_coordination_plane.md').read_text();intent=plan.split('## Owner intent\n\n',1)[1].split('\n## Loop protocol',1)[0]
record=Path('projects/pec/execution/_Coordination/_DECISIONS/D-PEC-80_D_RULING_OWNER_INTENT_OF_RECORD_2026-09-05.md').read_text();assert intent in record
assert sha(Path('projects/pec/loop/LOOP_RECEIPTS.md').read_bytes()[:426714])=='153732e389a1dd948805dd71150f63d865ef3c70cb8b8f8230a36b836dda0dd7'
(D/'INTEGRITY.json').write_text(json.dumps({'all_six_moves_sha256_equal':True,'all_335_original_historical_files_unchanged_at_final_homes':True,'owner_intent_verbatim':True,'frozen_receipts_prefix_unchanged':True,'loop_plans_and_currency_notes_absent':True},indent=2)+'\n')
known={(moves.get(r['path'],r['path']),r['line_sha256']) for r in csv.DictReader((E/'FINAL_REFERENCE_INVENTORY.csv').open())}
files=subprocess.check_output(['git','ls-files','--cached','--others','--exclude-standard','-z']).decode().split('\0');rows=[];bad=[]
for name in sorted(set(files)-{''}):
 p=Path(name)
 if not p.is_file() or p.is_symlink():continue
 try:s=p.read_text()
 except UnicodeError:continue
 for n,line in enumerate(s.splitlines(),1):
  if not any(x in line for x in ['_DomainEngines/pec/','loop/WORKPLAN_']):continue
  if name.startswith(str(E)) or name.startswith('projects/pec/execution/_Coordination/_DECISIONS/D-PEC-80'):cl='new candidate provenance/ruling evidence'
  elif (name,sha(line.encode())) in known:cl='preserved historical reference'
  elif name=='projects/pec/loop/LOOP_RECEIPTS.md' and 'Stale-Map-Delta' in line:cl='candidate receipt historical map continuation'
  elif '_DomainEngines/pec/' not in line and 'projects/pec/loop/WORKPLAN_' not in line:cl='other-loop or generic reference; no retired PEC target'
  else:cl='UNCLASSIFIED';bad.append([name,n,line])
  rows.append([name,n,sha(line.encode()),cl])
with (D/'FINAL_REFERENCE_INVENTORY.csv').open('w') as f:
 w=csv.writer(f,lineterminator='\n');w.writerow(['path','line','line_sha256','classification']);w.writerows(rows)
(D/'FINAL_REFERENCE_SUMMARY.json').write_text(json.dumps({'matching_lines':len(rows),'unclassified':bad,'scope':'all tracked/unignored regular UTF-8 repository files including hidden paths; excludes Git internals, builds, binaries and symlinks'},indent=2)+'\n')
print('integrity PASS; references',len(rows),'unclassified',len(bad));print(json.dumps(bad,indent=2));assert not bad
