from pathlib import Path
import re,json,hashlib,sys,platform
R=Path(__file__).resolve().parent
M=R.parent
C=M/'TEST_DISPOSITION_CANDIDATE'
F=M/'FREEZE_03'
root=next(p for p in R.parents if (p/'.agents/skills/software-code-review/SKILL.md').exists())
seen={}
def read(p):
 p=Path(p);b=p.read_bytes();seen[str(p.relative_to(root))]=hashlib.sha256(b).hexdigest();return b.decode()
def H(t):return hashlib.sha256(t.encode()).hexdigest()
def jl(p):return json.loads(read(p))
# Independently apply the complete unified patch, requiring every context/deletion line.
patch=read(C/'TEST_DISPOSITION.patch').splitlines(True)
i=0;patch_results=[]
while i<len(patch):
 assert patch[i].startswith('--- ')
 old=patch[i][4:].strip(); new=patch[i+1][4:].strip()[2:];i+=2
 original=[] if old=='/dev/null' else read(F/'source'/old[2:]).splitlines(True)
 output=[];cursor=0;hunks=0
 while i<len(patch) and not patch[i].startswith('--- '):
  m=re.fullmatch(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@\n',patch[i]);assert m,patch[i]
  a,n,b,k=map(int,(m[1],m[2] or 1,m[3],m[4] or 1));i+=1
  target=max(0,a-1);assert target>=cursor
  output+=original[cursor:target];cursor=target;deleted=added=0
  assert len(output)==max(0,b-1)
  while i<len(patch) and not patch[i].startswith(('@@ ','--- ')):
   line=patch[i];i+=1
   if line[0] in ' -':assert original[cursor]==line[1:],(new,cursor+1);cursor+=1;deleted+=1
   if line[0] in ' +':output.append(line[1:]);added+=1
  assert (deleted,added)==(n,k)
  hunks+=1
 output+=original[cursor:]
 candidate=read(C/'source'/new)
 assert ''.join(output)==candidate,new
 patch_results.append({'path':new,'hunks':hunks,'preimage_sha256':H(''.join(original)),'postimage_sha256':H(candidate),'strict_patch_matches_f03_and_postimage':True})
# Small lexical masker supports comments, escaped strings, Rust raw strings and character literals.
def mask(s):
 pattern=r'//[^\n]*|/\*.*?\*/|r(?P<h>\#*)".*?"(?P=h)|"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\\n])\''
 return re.sub(pattern,lambda m:''.join('\n' if c=='\n' else ' ' for c in m[0]),s,flags=re.S)
def func(s,name,test=False):
 ms=mask(s);m=re.search(r'\bfn\s+'+re.escape(name)+r'\s*\(',ms);assert m,name
 p=ms.index('{',m.end());depth=1;i=p+1
 while depth:
  if ms[i]=='{':depth+=1
  elif ms[i]=='}':depth-=1
  i+=1
 a=s.rfind('    #[test]\n',0,m.start()) if test else s.rfind('\n',0,m.start())+1
 return s[a:i]
rel='projects/chirality-piping/core/product_physics/src/lib.rs'
base=read(F/'source'/rel);cand=read(C/'source'/rel)
pm=jl(C/'PARENT_FUNCTION_MAP.json');cm=jl(C/'CURRENT_TESTS/FUNCTION_MAP.json')
assert H(base)==pm['base_live_sha256']==cm['base_live_file_sha256']
records=jl(M/'REGRESSION_DISPOSITION/DISPOSITIONS.json')['records']+jl(M/'REGRESSION_DISPOSITION/PARENT_12_DISPOSITIONS.json')
causes=jl(M/'REGRESSION_DIAGNOSIS/OBSERVED_CAUSES.json')
assert len(records)==len({r['test'] for r in records})==50
assert {r['test'] for r in records}=={r['test'] for r in causes}=={r['test'] for r in pm['changes']}
assert all(r['legacy_pressure_refusal_observed'] and 'PRESSURE_MODEL_REAUTHOR_REQUIRED' in r['observed_diagnostic_codes'] for r in causes)
raw=read(M/'REGRESSION_DIAGNOSIS/trace-01.log')
failures=set(re.findall(r'^---- (.+) stdout ----$',raw,re.M))
assert failures=={r['test'] for r in records}
assert all('PRESSURE_MODEL_REAUTHOR_REQUIRED' in raw.split('---- '+n+' stdout ----',1)[1].split('---- ',1)[0] for n in failures)
current=[]
for row in cm['functions']:
 n=row['test'].split('::')[-1];before=func(base,n,True);after=func(cand,n,True)
 post=read(C/'CURRENT_TESTS'/row['postimage_file'])
 assert H(before+'\n')==row['original_full_function_sha256']
 assert H(post)==row['postimage_full_function_sha256']
 assert post.rstrip('\n')==after
 reconstructed=before+'\n'
 for change in sorted(row['callsite_changes'],key=lambda x:x['original_function_offset_start'],reverse=True):
  a,b=change['original_function_offset_start'],change['original_function_offset_end']
  assert reconstructed[a:b]==change['before']
  reconstructed=reconstructed[:a]+change['after']+reconstructed[b:]
 assert reconstructed==post
 current.append({'test':row['test'],'before_sha256':H(before),'after_sha256':H(after),'only_declared_constructor_wrappers':True,'assertions_and_other_bytes_preserved':True})
for n in ['valid_invented_model_solves_deterministically','p5_adjacent_spans_and_qualified_case_edges_preserve_physics']:
 before=func(base,n,True);after=func(cand,n,True)
 assert before.replace('request()',f'mechanical_fixture_for_test(request(), "tests::{n}")')==after
 current.append({'test':'tests::'+n,'before_sha256':H(before),'after_sha256':H(after),'only_declared_constructor_wrappers':True,'assertions_and_other_bytes_preserved':True})
historical=[]
for n in pm['historical_tests']:
 before=func(base,n,True);after=func(cand,n+'_historical_pressure_premise',True)
 expected=before.replace('fn '+n+'(','fn '+n+'_historical_pressure_premise(').replace('run_linear_static_preview_with_mode(','historical_pressure_preview_with_mode(').replace('run_linear_static_preview(','historical_pressure_preview(')
 assert expected==after,n
 historical.append({'test':'tests::'+n,'before_sha256':H(before),'after_sha256':H(after),'only_name_and_entrypoint_changed':True,'original_values_assertions_tolerances_preserved':True})
assert func(base,'request')==func(cand,'request')
n='p5_adjacent_spans_and_qualified_case_edges_preserve_physics'
b=func(base,n,True);a=func(cand,n,True);prefix=b.index('            let output = run_linear_static_preview_with_mode(request(), mode);')
assert b[:prefix]==a[:prefix] and 'checked >= 20' in a
# All prepared input bindings, including path-rebased harness, not runtime validity.
prepared=jl(C/'PREPARED_INPUTS.json')
for p,h in prepared['files'].items(): assert H(read(C/p))==h,p
for row in pm['changes']:
 n=row['test'].split('::')[-1]
 assert H(func(base,n,True))==row['before_sha256']
 suffix='_historical_pressure_premise' if n in pm['historical_tests'] else ''
 aft=func(cand,n+suffix,True)
 if suffix:aft='    // Retained historical pressure premise; this private test route cannot qualify Current.\n'+aft
 assert H(aft)==row['after_sha256']
read(F/'source/projects/chirality-piping/core/product_physics/tests/pressure_runtime.rs')
# Read/hash the prior retained review and instruction sources, plus the actual fixture source.
for p in ['AGENTS.md','projects/chirality-piping/AGENTS.md','projects/chirality-piping/loop/LOOP_INIT.md','.agents/skills/software-code-review/SKILL.md','projects/chirality-piping/fixtures/product_preview/invented_preview_model.json','projects/chirality-piping/fixtures/product_preview/invented_mechanics_result.json']:read(root/p)
for p in ['TEST_DISPOSITION_REVIEW/BRIEF.md','FREEZE_03/RETURN.md','FREEZE_03/SOURCE_MANIFEST.json','INDEPENDENT_REVIEW/RETURN.md','INDEPENDENT_REVIEW/FREEZE_03_BACKCHECK/RETURN.md','REGRESSION_DIAGNOSIS/PROBE_BASIS.json','REGRESSION_DISPOSITION/RETURN.md','REGRESSION_DISPOSITION/HISTORICAL_ROUTE_PROPOSAL.md','TEST_DISPOSITION_CANDIDATE/PREPARATION_RETURN.md','TEST_DISPOSITION_CANDIDATE/prepare_candidate.py','TEST_DISPOSITION_CANDIDATE/setup_harness.py']:read(M/p)
result={'status':'STATIC_PROBES_PASS_NOT_PRODUCT_EXECUTION','python':sys.version,'platform':platform.platform(),'patch':patch_results,'all50_unique_proposal_and_failure_and_candidate_set_equal':True,'all50_raw_failure_sections_contain_preceding_pressure_refusal':True,'current_functions':current,'historical_functions':historical,'p5_early_full_split_current_prefix_unchanged':True,'p5_checked_at_least_20_retained':True,'global_request_unchanged':True,'prepared_input_hashes_all_match':True,'limits':'No build, test runtime, Git, native/network operation or live product edit. Frozen patch basis only; unrelated simultaneous live membrane changes excluded.'}
(R/'STATIC_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
seen[str((R/'static_probe.py').relative_to(root))]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
(R/'INSPECTED_INPUTS.json').write_text(json.dumps({'root':'active assigned checkout','reviewer':'/root/physics_resume/test_policy_review','actual_parent':'/root/physics_resume','mechanism':'delegated-harness-native','role':'TASK (full role in BRIEF.md)','hash_algorithm':'SHA-256','files':seen},indent=2)+'\n')
print(json.dumps({'status':result['status'],'patch_sha256':H(read(C/'TEST_DISPOSITION.patch')),'patch_paths':len(patch_results),'current':len(current),'historical':len(historical),'input_hash_count':len(seen)}))
