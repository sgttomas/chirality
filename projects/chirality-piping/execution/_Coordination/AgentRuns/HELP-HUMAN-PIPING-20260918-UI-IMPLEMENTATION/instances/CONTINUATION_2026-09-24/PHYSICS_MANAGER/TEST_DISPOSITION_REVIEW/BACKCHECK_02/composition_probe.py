from pathlib import Path
import difflib,hashlib,json,re
B=Path(__file__).resolve().parent;M=B.parent.parent;F3=M/'FREEZE_03';F4=M/'FREEZE_04';C=M/'TEST_DISPOSITION_CANDIDATE';P=M/'TEST_DISPOSITION_REPAIR';MP=M/'MEMBRANE_PUBLICATION'
ROOT=next(p for p in B.parents if (p/'.agents/skills/software-code-review/SKILL.md').exists());seen={}
def H(x):return hashlib.sha256(x.encode()).hexdigest()
def read(p):
 b=Path(p).read_bytes();seen[str(Path(p).relative_to(ROOT))]=hashlib.sha256(b).hexdigest();return b.decode()
def J(p):return json.loads(read(p))
def apply(files,text):
 files=files.copy();patch=text.splitlines(True);i=0;paths=[]
 while i<len(patch):
  assert patch[i].startswith('--- ');old=patch[i][4:].strip();new=patch[i+1][4:].strip()[2:];i+=2
  orig=[] if old=='/dev/null' else files[old[2:]].splitlines(True)
  assert old=='/dev/null' or old[2:]==new
  out=[];cur=0;hunks=0
  while i<len(patch) and not patch[i].startswith('--- '):
   m=re.fullmatch(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@\n',patch[i]);assert m,patch[i]
   a,n,b,k=map(int,(m[1],m[2] or 1,m[3],m[4] or 1));i+=1;target=max(0,a-1);assert target>=cur
   out+=orig[cur:target];cur=target;assert len(out)==max(0,b-1);dn=an=0
   while i<len(patch) and not patch[i].startswith(('--- ','@@ ')):
    line=patch[i];i+=1
    if line[0] in ' -':assert orig[cur]==line[1:],(new,cur+1);cur+=1;dn+=1
    if line[0] in ' +':out.append(line[1:]);an+=1
   assert (dn,an)==(n,k);hunks+=1
  out+=orig[cur:];files[new]=''.join(out);paths.append({'path':new,'hunks':hunks,'sha256':H(files[new])})
 return files,paths
f3=J(F3/'SOURCE_MANIFEST.json');f4=J(F4/'SOURCE_MANIFEST.json');refs=J(F4/'CHECKS_AND_REFERENCES.json')
base={row['path']:read(F3/'source'/row['path']) for row in f3['paths']}
assert len(base)==19
for row in f3['paths']:assert H(base[row['path']])==row['sha256']
assert f4['previous_candidate_content_sha256']==f3['candidate_content_sha256']
originalpatch=read(C/'TEST_DISPOSITION.patch');assert H(originalpatch)=='f7ee34f04a74e474a2f6fc97f2faeedfaa0476e54b2b1ee2082df1c3825678c3'
original,_=apply(base,originalpatch)
successor=J(P/'SUCCESSOR_BINDING.json');policy_delta=read(P/'policy_successor.delta.patch');kpa_delta=read(P/'exact_kpa.delta.patch')
assert H(policy_delta)==successor['patches']['policy_successor.delta.patch']=='db1f66527f093c68e6e068378e298703d2df7530d093d3db2e85b76e55cce53b'
assert H(kpa_delta)==successor['patches']['exact_kpa.delta.patch']=='aaa11cab61ea2cb4a89e69feafb0976b79394bdbfcbca511fb4fc9f7da72190f'
policy,_=apply(original,policy_delta);policy,_=apply(policy,kpa_delta)
lib='projects/chirality-piping/core/product_physics/src/lib.rs'
assert H(policy[lib])==successor['repaired_candidate_lib_sha256']=='61d7316246bc51983606c1bda006727b62c0e159d62c39b37b190d27d3e08568'
membrane_delta=read(MP/'PHYS_R4.delta.patch');repair=J(MP/'REPAIR_BINDING.json');assert H(membrane_delta)==repair['patch_sha256']=='177ef090e35d501efbc82685866d0ae2a23fb20dfca4cbe70d6d82e77db61aee'
membrane,_=apply(base,membrane_delta)
for path,values in repair['files'].items():assert H(membrane[path])==values['after_sha256']
# Independently compose nonoverlapping original-F03 coordinate edits, not line-number fuzzy application.
baselines=base[lib].splitlines(True);edits=[]
for kind,post in [('test_policy',policy[lib]),('PHYS_R4',membrane[lib])]:
 post=post.splitlines(True)
 for op,a,b,c,d in difflib.SequenceMatcher(None,baselines,post,autojunk=False).get_opcodes():
  if op!='equal':edits.append((a,b,post[c:d],kind))
edits.sort(key=lambda x:(x[0],x[1]));out=[];cur=0
for a,b,after,kind in edits:
 assert a>=cur,('overlap',a,cur,kind);out+=baselines[cur:a]+after;cur=b
out+=baselines[cur:];merged=policy.copy();merged[lib]=''.join(out)
for path in set(membrane)-set(base):merged[path]=membrane[path]
delta=read(F4/'from-freeze-03.delta.patch');assert H(delta)==refs['delta_sha256']
final,changed=apply(base,delta);assert len(changed)==5
assert final==merged,'F04 differs from exact reviewed composition'
assert len(final)==len(f4['paths'])==21
live=[]
for row in f4['paths']:
 path=row['path'];content=read(ROOT/path)
 assert H(content)==row['sha256']==H(final[path]);assert len(content.encode())==row['bytes']
 assert row['freeze_03_sha256']==(H(base[path]) if path in base else None)
 live.append({'path':path,'sha256':row['sha256'],'live_and_reconstructed_and_manifest_equal':True})
whitelist=read(F4/'SOURCE_WHITELIST.txt').splitlines();assert set(whitelist)==set(final)
digest=H(''.join(path+'\0'+H(final[path])+'\n' for path in sorted(final)))
assert digest==f4['candidate_content_sha256']==refs['candidate']=='6bb99354fa9591032f672a7c3bd488edd8d4cdb6df9135e211cff3a10556b546'
for path,h in refs['records'].items():assert H(read(M/path))==h,path
execution=J(MP/'integrated-product-01-execution.json');log=read(MP/'integrated-product-01.log')
assert H(log)==execution['log_sha256'];assert execution['exit_code']==0 and execution['all_inputs_unchanged']
assert execution['cwd']==str(ROOT)
for path,h in execution['inputs'].items():assert H(read(ROOT/path))==h,path
assert set(final)<=set(execution['inputs'])
cmd=execution['command'];assert cmd[0:2]==['cargo','test']
assert all(x in cmd for x in ['--offline','--locked','--lib','--test-threads=2','--nocapture'])
expected_tests={'pressure_runtime','pressure_section_geometry','pressure_membrane_range','elastic_extrema_runtime','stress_maximum_coverage','support_reactions_runtime','pressure_grouping_limits'}
selected={cmd[i+1] for i,x in enumerate(cmd[:-1]) if x=='--test'};assert selected==expected_tests
assert '--ignore' not in cmd and '--skip' not in cmd
summary=[tuple(map(int,m)) for m in re.findall(r'test result: ok\. (\d+) passed; (\d+) failed; (\d+) ignored; (\d+) measured; (\d+) filtered out;',log)]
assert len(summary)==8 and summary[0]==(213,0,0,0,0) and sum(x[0] for x in summary[1:])==36 and all(x[1:]==(0,0,0,0) for x in summary)
unitlog=log.split('running 213 tests',1)[1].split('test result:',1)[0]
unitpasses=re.findall(r'^test (\S+) \.\.\. ok$',unitlog,re.M);assert len(unitpasses)==len(set(unitpasses))==213
assert not re.search(r'^test .* \.\.\. (FAILED|ignored)$',log,re.M)
# Each original failure maps to exactly one final executable test, not a skipped/deleted assertion.
map=J(C/'PARENT_FUNCTION_MAP.json');rows=[]
for change in map['changes']:
 old=change['test'];stem=old.split('::')[-1];n=old+('_historical_pressure_premise' if stem in map['historical_tests'] else '')
 assert n in unitpasses,n
 assert re.search(r'\bfn '+re.escape(n.split('::')[-1])+r'\(',final[lib])
 rows.append({'original_test':old,'integrated_test':n,'purpose':change['kind'],'observed_result':'ok','prior_individual_review_retained':True})
assert len(rows)==len({r['integrated_test'] for r in rows})==50
added=map['added_current_counterparts']+['current_composite_derived_normal_friction_and_reversal','private_historical_pressure_scope_restores_public_refusal_and_rejects_exact','private_historical_scope_restores_after_unwind_and_is_thread_local']
assert len(added)==7 and all('tests::'+n in unitpasses for n in added)
caught=re.findall(r"thread '(tests::private_historical[^']+)' .*panicked",unitlog)
assert len(caught)==2 and all(n in unitpasses for n in caught)
# Read the composed-review evidence and origin records without re-running their probes.
for path in ['TEST_DISPOSITION_REVIEW/RETURN.md','TEST_DISPOSITION_REVIEW/BACKCHECK_01/RETURN.md','TEST_DISPOSITION_REVIEW/BACKCHECK_01/STATIC_BINDING.json','MEMBRANE_BACKCHECK/RETURN.md','MEMBRANE_BACKCHECK/verification.json','MEMBRANE_PUBLICATION/REFERENCE_BINDING_02.json','FREEZE_04/RETURN.md']:read(M/path)
for path in ['AGENTS.md','projects/chirality-piping/AGENTS.md','projects/chirality-piping/loop/LOOP_INIT.md','.agents/skills/software-code-review/SKILL.md']:read(ROOT/path)
result={'status':'PASS_EXACT_COMPOSITION_AND_RECORDED_EXECUTION_BINDING','candidate_content_sha256':digest,'F03_paths':19,'F04_paths':21,'changed_paths':changed,'reviewed_nonoverlapping_lib_edits':len(edits),'reviewed_composition_equals_F04_patch':True,'all21_live_hashes_equal':True,'live_paths':live,'all21_bound_before_and_after_integrated_run':True,'integrated_execution':{'actor':execution['actor'],'exit_code':execution['exit_code'],'command':cmd,'cwd':execution['cwd'],'started_utc':execution['started_utc'],'finished_utc':execution['finished_utc'],'versions':execution['versions'],'log_sha256':execution['log_sha256'],'library_passed':213,'public_passed':36,'ignored':0,'filtered':0,'summaries':summary,'intentional_caught_panic_tests':caught},'all50_mapped_passed':True,'added_tests_passed':added,'limits':'Reviewer did not execute product. Command input manifest covers all21 selected files plus records, not every transitive workspace dependency or Cargo.lock. Broader consumer/native/CI/registered-sweep/merge gates remain open.'}
(B/'COMPOSITION_AND_EXECUTION.json').write_text(json.dumps(result,indent=2)+'\n')
(B/'ALL50_PASS_MAPPING.json').write_text(json.dumps(rows,indent=2)+'\n')
seen[str(Path(__file__).resolve().relative_to(ROOT))]=H(Path(__file__).read_text());(B/'INSPECTED_INPUTS.json').write_text(json.dumps(seen,indent=2)+'\n')
print(json.dumps({'status':result['status'],'candidate':digest,'changed_paths':len(changed),'live_paths':len(live),'library_passed':213,'public_passed':36,'original50_mapped_and_passed':True,'input_hashes':len(seen)}))
