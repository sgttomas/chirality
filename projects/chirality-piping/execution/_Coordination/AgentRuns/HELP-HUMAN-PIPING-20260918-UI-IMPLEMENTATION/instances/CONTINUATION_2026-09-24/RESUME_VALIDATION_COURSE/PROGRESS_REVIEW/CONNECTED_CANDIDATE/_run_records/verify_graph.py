from pathlib import Path
import subprocess,json,hashlib,re,datetime
RAW=Path(__file__).parent;OUT=RAW.parent;PRIMARY=Path('/Users/ryan/.codex/worktrees/6614/chirality');ENGINE=Path('/private/tmp/piping-engine-integration-20260925');QUAL=Path('/private/tmp/piping-joined-qualification-20260925');C=Path('projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24');G=Path('projects/chirality-piping/execution/_Coordination/WorkGraphs/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/WORK_GRAPH.md');HEAD='a26fe2f171881c9b284f14d840cbc29bc3828dde';H='c278f64ba122eb8b848b9f14e58a0e533e94439a'
def git(root,*args):return subprocess.check_output(['git',*args],cwd=root)
def blob(rev,path):return git(ENGINE,'show',rev+':'+str(path))
def sha(data):return hashlib.sha256(data).hexdigest()
def binding(p):return {'origin':str(p),'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size}
assert git(PRIMARY,'rev-parse','HEAD').decode().strip()==HEAD
old=git(PRIMARY,'show',HEAD+':'+str(G));new=(PRIMARY/G).read_bytes();patch=git(PRIMARY,'diff','--',str(G));(RAW/'REVIEWED_DELTA.patch').write_bytes(patch)
removed=[line[1:] for line in patch.decode().splitlines() if line.startswith('-|')];added=[line[1:] for line in patch.decode().splitlines() if line.startswith('+|')]
expected={'COR-NUMERICS','COR-PRESSURE','COR-RESULTS','VP-HARNESS','VP-ORACLES','VP-STATIC'}
assert len(removed)==len(added)==6 and {x.split(' — ')[0].removeprefix('| ') for x in removed}==expected
text=new.decode();assert '| CORRECTNESS-MILESTONE' in text and '4of38 assessed groups closed (M04/M09/M24/M35)' in text and 'Original finding closure remains4of38' in text
assert 'one undertaking CLOSE→RECORD→FINAL boundary' in text and 'General UI/C4/live work remains deferred' in text
commits={}
for rev in [H,'1792774a2c5b77612e666332151f10f4b14dbc2c','8b982aa7ce64afe37e6067d1038d92608f4aaf3f','26b9904a1e8d2b997315165572d732ce4320df3b']:
 commits[rev]={'parents':git(ENGINE,'show','-s','--format=%P',rev).decode().strip().split(),'subject':git(ENGINE,'show','-s','--format=%s',rev).decode().strip()}
assert commits[H]['parents']==['8b982aa7ce64afe37e6067d1038d92608f4aaf3f','26b9904a1e8d2b997315165572d732ce4320df3b']
refs={name:git(ENGINE,'rev-parse','refs/remotes/origin/codex/'+name).decode().strip() for name in ['piping-engine-integration-20260925','piping-validation-foundation-20260925']};assert refs['piping-engine-integration-20260925']=='1792774a2c5b77612e666332151f10f4b14dbc2c' and refs['piping-validation-foundation-20260925']=='26b9904a1e8d2b997315165572d732ce4320df3b'
links=[]
for line in patch.decode().splitlines():
 if not line.startswith('+') or line.startswith('+++'):continue
 for url in re.findall(r'\]\((https://github.com/sgttomas/chirality/blob/[^)]+)\)',line):
  rev,path=url.split('/blob/',1)[1].split('/',1);assert rev==H;data=blob(rev,path);links.append({'url':url,'sha256':sha(data),'local_pinned_object_exists':True})
assert len(links)==3
N=C/'_run_records/JOINED_ENGINE_NATIVE';A=C/'VALIDATION_FOUNDATION/ORDINARY_PHYSICS_ADAPTER';nr=json.loads(blob(H,N/'INDEPENDENT_REVIEW/VERIFICATION.json'));pr=json.loads(blob(H,A/'COMPARISON_RUN_01/PROGRAMME.json'))
assert nr['primary_comparisons']==348 and nr['repeated_comparisons']==129 and nr['primary_comparisons']+nr['repeated_comparisons']==477
assert pr['actual_case_mode_executions']==4 and pr['all_selected_obligations_matched'];assert pr['programme_denominator']=={'case_mode_executions':4,'scalar_obligations':292,'structural_obligations':40,'section_subchecks_nested':36}
log=(QUAL/'practitioner.log').read_bytes();assert b'1 failed, 378 passed' in log and b'test_live_gen8_semantic_portability_invariants' in log and b'Left contains 168 more items' in log
findings=json.loads((QUAL/'portability-findings.json').read_text());assert len(findings)==len({x['path'] for x in findings})==168
scope=json.loads((QUAL/'scope.log').read_text());assert scope['status']=='PASS' and scope['violations']==[]
(RAW/'practitioner.log').write_bytes(log)
# Check that in-progress portability work has not edited the native/source or final adapter inputs.
source_records=json.loads(blob(H,N/'_run_records/inputs-pre.json'));assert len(source_records)==1092
for row in source_records:assert sha((ENGINE/row['path']).read_bytes())==row['sha256']
f=json.loads(blob(H,A/'SOURCE_FREEZE_03.json'))
for row in f['files']:assert sha((ENGINE/row['path']).read_bytes())==row['sha256']
review_path=ENGINE/C/'ENGINE_INTEGRATION/ROOT_VALIDATION_UNION/INDEPENDENT_REVIEW/RETURN.md'
raw={'status':'CLEAR graph current-state checkpoint','checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer':'/root/numerical_resume/n05_admission','original_parent':'/root/numerical_resume','cross_manager_assignment':'/root','role':'TASK','delegation':'none','primary_head':HEAD,'graph_sha256':sha(new),'base_graph_sha256':sha(old),'delta_sha256':sha(patch),'changed_existing_rows':sorted(expected),'commit_bindings':commits,'local_fetched_remote_refs':refs,'new_link_bindings':links,'native_observations':{'primary':348,'repeated':129,'total':477,'distinct_test_claim':False},'validation_observations':pr['programme_denominator'],'practitioner':{'passed':378,'failed':1,'failed_case':'test_live_gen8_semantic_portability_invariants','affected_record_paths':168,'finding_paths_unique':True},'scoped_path_check':'PASS','frozen_source_comparison':{'native_inputs_unchanged':1092,'validation_inputs_unchanged':26},'qualification_inputs':[binding(QUAL/x) for x in ['practitioner.log','portability-findings.json','scope.log']],'integration_review':binding(review_path),'boundaries':'4of38 unchanged; no fullQ1/current-head qualification/merge/release closure; one closeout and owner boundaries preserved. Root/manager relocation ownership is coordination, not completed repair verification.','notes':'Working-tree validation RETURN has moved during portability work; all new graph URLs use immutable c278 objects and resolve there. This is expected relocation, not a broken pinned link. No network check or gate rerun performed.'}
(RAW/'CHECKED_BASIS.json').write_text(json.dumps(raw,indent=2)+'\n');assert (PRIMARY/G).read_bytes()==new
print(json.dumps({'status':'CLEAR','graph_sha256':sha(new),'delta_sha256':sha(patch),'basis_sha256':sha((RAW/'CHECKED_BASIS.json').read_bytes())},indent=2))
