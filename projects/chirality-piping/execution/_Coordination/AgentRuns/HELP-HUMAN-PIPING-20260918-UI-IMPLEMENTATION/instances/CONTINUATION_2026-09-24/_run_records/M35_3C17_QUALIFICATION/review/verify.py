"""Read-only final M35 qualification evidence backcheck; no suites or native actions."""
from pathlib import Path
import datetime, hashlib, importlib.util, json, re, subprocess, sys
sys.dont_write_bytecode = True
OUT=Path(__file__).resolve().parent
R=Path('/private/tmp/piping-generated-loads-20260924')
P=R/'projects/chirality-piping'
V=Path('/private/tmp/piping-m35-validation-3c17-20260925')
CI=Path('/private/tmp/piping-m35-ci-3c17-20260925')
HEAD='3c17e267dd06ee561e8dc9984f6623126095eec1'
EVIDENCE='e350573450daa35f00f4a45cc6a1dab6b204b223'
C='projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/'
N=C+'_run_records/M35_NATIVE/'
REVIEW=C+'_run_records/ROOT_SOLVER_CHECKPOINT_REVIEW/'
git=lambda *a:subprocess.check_output(['git','-C',str(R),*a])
sha=lambda b:hashlib.sha256(b).hexdigest()
fsha=lambda p:sha(p.read_bytes())
load=lambda p:json.loads(p.read_text())
blob=lambda path:git('show',EVIDENCE+':'+path)
obj=lambda path:json.loads(blob(path))

assert git('rev-parse','HEAD').decode().strip()==HEAD
assert not git('diff','--name-only','HEAD').decode()
summary=load(OUT/'sweep-summary.reviewed.json')
invocation=load(V/'sweep-invocation.json');result=load(V/'sweep-result.json')
binding=load(CI/'surface4-ci-binding.json');ci_source=load(CI/'IDENTITY_EXECUTION_CHECK.json')
ci_num=load(CI/'NUMERICAL_EXECUTION_CHECK.json');run=load(CI/'run.json')
assert result['exit_code']==0 and result['candidate']==invocation['candidate']==HEAD
assert result['initial_status']==invocation['initial_status']==''
assert summary['git']['commit_hash']==HEAD and summary['git']['working_tree_dirty'] is False
assert summary['git']['status_capture_failed'] is False and summary['git']['dirty_paths']==[]
assert invocation['binding_sha256']==result['binding_sha256']==fsha(CI/'surface4-ci-binding.json')
assert binding['head_sha']==ci_source['head']==ci_num['candidate']==run['head_sha']==HEAD
assert run['conclusion']=='success' and run['status']=='completed'

module_path=P/'tools/release/run_evidence_sweep.py'
spec=importlib.util.spec_from_file_location('qualification_sweep',module_path)
module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module;spec.loader.exec_module(module)
errors=module.validate_summary(summary)
assert not errors and module.is_complete_sweep_summary(summary) and summary['overall_status']=='pass'
assert module.validate_ci_binding(binding,commit_hash=HEAD)==[]
planned=module.build_sweep_plan(binding)
surface_checks=[]
for actual,expected in zip(summary['surfaces'],planned):
    assert actual['surface_id']==expected.surface_id and actual['execution_capability']==expected.execution_capability
    assert actual['status']=='pass' and all(x['exit_code']==0 for x in actual['commands'])
    assert [x['argv'] for x in actual['commands']]==[list(x) for x in expected.commands]
    if expected.ci_binding is not None:assert actual['ci_binding']==binding and actual['commands']==[]
    surface_checks.append({'surface_id':actual['surface_id'],'status':actual['status'],'capability':actual['execution_capability'],
                           'command_count':len(actual['commands']),'matches_candidate_plan':True})
log=re.sub(r'\x1b\[[0-9;]*m','',(V/'sweep.log').read_text())
assert '[evidence-sweep] overall: pass' in log and '[evidence-sweep] commit: '+HEAD in log
for s in summary['surfaces']:
    for command in s['commands']:assert '[evidence-sweep] '+s['surface_id']+': '+' '.join(command['argv']) in log
assert f"desktop_playwright_e2e: bound CI run {binding['run_id']} attempt {binding['run_attempt']}" in log
rust=log.split('[evidence-sweep] cargo_crate_sweep:',1)[1].split('[evidence-sweep] python_pytest:',1)[0]
rust_summaries=re.findall(r'test result: ok\. (\d+) passed; (\d+) failed; (\d+) ignored; (\d+) measured; (\d+) filtered out',rust)
assert rust_summaries and all(int(x[1])==0 for x in rust_summaries)
local_rust_passed=sum(int(x[0]) for x in rust_summaries)
py_summary=re.search(r'(\d+) passed, (\d+) warnings, (\d+) subtests passed in ',log)
unit_summary=re.search(r'Test Files\s+(\d+) passed \(\d+\)\s+Tests\s+(\d+) passed \(\d+\)',log)
assert py_summary and unit_summary
profiles=load(V/'profile-results.json');profile_rows=[]
assert len(profiles)==3
for row in profiles:
    assert row['candidate']==HEAD and row['exit_code']==0
    profile_rows.append({**row,'log_sha256':fsha(V/row['log'])})
assert '379 passed' in (V/'profile-1.log').read_text()
self_check=(V/'profile-0.log').read_text()
assert 'BLOCK=' not in self_check and '| BLOCK |' not in self_check

coverage=obj(REVIEW+'COVERAGE.json')['paths'];coverage_mismatches=[x['path'] for x in coverage if sha(blob(x['path']))!=x['sha256']]
review_output=obj(REVIEW+'OUTPUT_HASHES.json')
review_output_mismatches=[x['path'] for x in review_output if sha(blob(REVIEW+x['path']))!=x['sha256']]
assert not coverage_mismatches and not review_output_mismatches
native_files=git('ls-tree','-r','--name-only',EVIDENCE,'--',N).decode().splitlines()
assert {x['path'] for x in coverage if x['path'].startswith(N)}==set(native_files)
custody=obj(N+'CUSTODY.json');native_raw=[]
for row in custody['committed_raw_files']:
    b=blob(N+row['path']);actual=sha(b)
    assert actual==row['sha256'] and len(b)==row['bytes']
    native_raw.append({'path':row['path'],'sha256':actual,'bytes':len(b)})
pre=obj(N+'_run_records/inputs-pre.json');post=obj(N+'_run_records/inputs-post.json')
assert pre==post and len(pre)==len({x['path'] for x in pre})
native_input_mismatches=[x['path'] for x in pre if fsha(R/x['path'])!=x['sha256']]
assert not native_input_mismatches
assert not git('diff','--name-only',custody['built_candidate'],HEAD,'--',*[x['path'] for x in pre]).decode()
artifact=obj(N+'_run_records/artifact-identity.json')
assert fsha(Path(artifact['executable']))==artifact['executable_sha256']
bundle_mismatches=[x['path'] for x in artifact['bundle_files'] if fsha(Path(artifact['app'])/x['path'])!=x['sha256']]
assert not bundle_mismatches
assert obj(N+'_run_records/build-command.json')['exit_code']==0
assert obj(N+'_run_records/basis.json')['status']==''

balances=[]
for row in obj(N+'_run_records/analytical-native-checks.json')['checks']:
    q,L,tip=row['q_N_per_m'],row['length_m'],row['manual_tip_N']
    force=-(q*L+tip);moment=-(q*L*L/2+tip*L)
    assert round(force,6)==row['observed_support_force_N']
    assert all(round(moment,6)==x['value'] for x in row['matching_actual_moment_rows'])
    balances.append({'state':row['state'],'correct_signed_force':force,'correct_signed_moment':moment,'published_rounding_matches':True})
native_return=blob(N+'RETURN.md').decode()
assert 'supportY = -(qL + P_y)' in native_return and 'raw record is preserved' in native_return
assert 'independent practitioner/live-human witnesses' in blob(REVIEW+'RETURN.md').decode()
privacy=[]
def find_models(v,path):
    if isinstance(v,dict):
        if 'nodes' in v and 'pipe_segments' in v:privacy.append(path)
        for val in v.values():find_models(val,path)
    elif isinstance(v,list):
        for val in v:find_models(val,path)
    elif isinstance(v,str) and v.startswith('{'):
        try:decoded=json.loads(v)
        except ValueError:return
        find_models(decoded,path)
for path in native_files:
    if path.endswith('.json'):find_models(obj(path),path)
assert not privacy
private_model_paths=[x['private_relative_path'] for x in custody['private_only_files']
    if x['private_relative_path'].startswith('private-rows/') or x['private_relative_path'].endswith('-batch.json')]
assert not any('/private-rows/' in x or x.endswith('-batch.json') for x in native_files)

source=load(R/(C+'GENERATED_LOADS_MANAGER/CANDIDATE_FILES.json'))['files']
assert all(fsha(R/x['path'])==x['sha256'] for x in source)
consumed=[V/x for x in ['profile-results.json','profile-0.log','profile-1.log','profile-2.log','run_profile.py',
    'sweep-invocation.json','sweep-result.json','sweep.log','run_sweep.py']]
consumed += [CI/x for x in ['surface4-ci-binding.json','RETURN.md','IDENTITY_EXECUTION_CHECK.json','NUMERICAL_EXECUTION_CHECK.json','CI_RETURN_HASHES.json','PR_CHECKS.json']]
consumed += [R/x for x in ['AGENTS.md','agents/AGENT_TASK.md','.agents/skills/software-code-review/SKILL.md',
    'projects/chirality-piping/AGENTS.md','projects/chirality-piping/loop/LOOP_INIT.md']]
consumed += [module_path,OUT/'sweep-summary.reviewed.json']
report={'reviewer':'/root/m35_integration_review','parent':'/root','role':'TASK','time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'candidate':HEAD,'native_evidence_commit':EVIDENCE,'source_files_match':len(source),'current_status':git('status','--porcelain').decode(),
    'sweep_initial_clean':True,'sweep_complete':True,'sweep_validation_errors':errors,'sweep_exit_code':result['exit_code'],
    'sweep_surfaces':surface_checks,'sweep_summary_sha256':fsha(OUT/'sweep-summary.reviewed.json'),
    'sweep_binding_sha256':fsha(CI/'surface4-ci-binding.json'),'sweep_log_sha256':fsha(V/'sweep.log'),
    'local_rust_summary_passed':local_rust_passed,'local_rust_ignored':sum(int(x[2]) for x in rust_summaries),
    'local_python_passed':int(py_summary[1]),'local_python_warnings':int(py_summary[2]),'local_python_subtests_passed':int(py_summary[3]),
    'local_desktop_files_passed':int(unit_summary[1]),'local_desktop_tests_passed':int(unit_summary[2]),'profile_results':profile_rows,
    'self_check_note':'Exit0; INFO14,NOT_APPLICABLE1,REVIEW4,WARN124 retained, no BLOCK. Pass does not erase standing observations.',
    'hosted_browser':{k:ci_source[k] for k in ['run_id','discovered','passed','skipped','missing','duplicates','unexpected']},
    'hosted_numerical':{k:ci_num[k] for k in ['discovered_manifests','test_summary_passed','test_summary_ignored']},
    'native_coverage_paths':len(native_files),'independent_checkpoint_candidate_paths':len(coverage),
    'coverage_hash_mismatches':coverage_mismatches,'review_output_hash_mismatches':review_output_mismatches,
    'native_raw_hashes':native_raw,'native_input_count':len(pre),'native_input_mismatches':native_input_mismatches,
    'native_executable_sha256':artifact['executable_sha256'],'native_bundle_hash_mismatches':bundle_mismatches,
    'native_signed_balance_backcheck':balances,'native_full_model_json_matches':privacy,
    'private_model_or_batch_paths_absent':True,'private_captures_reopened':False,
    'native_limits':'Relies on independently reviewed actual ROOT UI/owned-store evidence; no new native execution. Native v1 and queued-edit journeys not repeated; human practitioner/live-controller witnesses remain unclaimed.',
    'broader_open_items':['M30 mass-source/model completeness','Native connect_pipe_run density omission assigned to joined engine tranche',
        'Native v1 upgrade and edit-after-queued-refresh not repeated in this witness','Independent practitioner/live-human witnesses',
        'N05 accuracy, Sensitive containment, N06 ordinary failure, broader pressure/physical/consumer integration','M34 full precision not qualified by this six-decimal witness','WholeM35/all38finding closure, engineering acceptance and release'],
    'consumed_files':[{'path':str(x),'sha256':fsha(x)} for x in consumed],
    'native_committed_files':[{'path':x,'sha256':sha(blob(x))} for x in native_files],
    'reviewer_limits':'No source/graph/Git/native changes, delegation, suite rerun, or remote polling. Deterministic validator/hash/arithmetic inspection only.'}
(OUT/'HASHES.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['candidate','sweep_complete','local_rust_summary_passed','local_python_passed','local_desktop_files_passed','local_desktop_tests_passed','native_coverage_paths','native_input_count','current_status']},indent=2))
