"""Narrow records/wording audit. No arithmetic, product, parser, or conformance execution."""
from pathlib import Path
import json, hashlib, datetime, sys
PRIMARY=Path('/Users/ryan/.codex/worktrees/6614/chirality')
SOURCE=Path('/private/tmp/piping-source-recovery-20260924')
REL=Path('projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24')
D=PRIMARY/REL/'CORRECTNESS_DESIGN/SCIENTIFIC_JSON_PROFILE'
B=D/'_run_records/ATTRIBUTION_INDEPENDENT_BACKCHECK'
RUN=SOURCE/REL/'SOLVER_MANAGER/ORDINARY_NUMERICAL_CUT/SOURCE_RECOVERY_IMPLEMENTATION_01'
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def read(path): return json.loads(path.read_text())
delta=read(D/'_run_records/ATTRIBUTION_DELTA.json')
prior=read(D/'_run_records/INDEPENDENT_REVIEW/FINAL_HASHES.json')
prior_by_name={Path(x['path']).name:x['sha256'] for x in prior['files']}
packet=[]
for item in delta['changes']:
 name=Path(item['path']).name; p=D/name
 assert item['prior_reviewed_sha256']==prior_by_name[name]
 assert sha(p)==item['current_sha256']
 assert item['changed']==(sha(p)!=prior_by_name[name])
 packet.append({'file':name,'actual_origin':str(p),'prior_reviewed_sha256':prior_by_name[name],'final_sha256':sha(p),'changed':item['changed']})
assert {r['file'] for r in packet if r['changed']}=={'DESIGN.md','RETURN.md','BASIS.json'}
basis=read(D/'BASIS.json'); additional=[]
for row in basis['basis']:
 if row['kind'].startswith('narrow attribution backcheck'):
  p=SOURCE/row['origin'].split('/',1)[1]
  assert sha(p)==row['sha256']
  additional.append({'origin':str(p),'sha256':sha(p),'matches_basis':True})
initial_request=read(RUN/'_run_records/stress_range_before/dense_scrutiny.request.json')
initial_raw=read(RUN/'_run_records/stress_range_before/dense_scrutiny.raw.json')
assert initial_request['model']['load_cases'][0]['primitive_loads'][0]['magnitude']['value']==1e-306
assert initial_raw['producer']['semantic_contract_id'].endswith('/precision-1')
assert initial_raw['numerical_quality']['status']=='sensitive'
assert 'source_block_recovery' not in initial_raw
refused=[d for d in initial_raw['diagnostics'] if d['code']=='SOURCE_BLOCK_RECOVERY_UNAVAILABLE']
assert len(refused)==1 and 'exact radix loses represented bits' in refused[0]['message']
scalar=read(D/'_run_records/INDEPENDENT_REVIEW/PYTHON_REFERENCE.json')['stress_units']
assert scalar['force_bits']=='0066789e3750f791' and scalar['area_bits']=='4122374d355759df'
scaled=[]; oracle=read(RUN/'_run_records/stress_range_scaled_before/ORACLE.json')
for row in oracle['records']:
 folder=RUN/'_run_records/stress_range_scaled_before'; raw_path=folder/row['raw']; request_path=folder/row['request']
 assert sha(raw_path)==row['raw_sha256'] and sha(request_path)==row['request_sha256']
 raw=read(raw_path); request=read(request_path); mode=row['raw'].split('.raw.json')[0]; model=request['model']
 assert model['pipe_segments'][0]['section']['outside_diameter']['value']==2e15
 assert model['pipe_segments'][0]['section']['wall_thickness']['value']==1e14
 assert model['materials'][0]['elastic_modulus']['value']==1e-29
 assert model['materials'][0]['shear_modulus']['value']==1e-53
 assert model['load_cases'][0]['primitive_loads'][0]['magnitude']['value']==1e-282
 assert raw['producer']['semantic_contract_id'].endswith('/source-blocks-1')
 receipt=raw['source_block_recovery']['body']; assert receipt['status']=='qualified'
 assert len(receipt['cases'])==1 and receipt['cases'][0]['outcome']=='qualified'
 assert receipt['cases'][0]['requested_mode']==mode
 assert len(row['samples'])==6
 emitted={x['id']:x for x in raw['results']}
 for sample in row['samples']:
  actual=emitted[sample['id']]
  assert actual['value']==sample['value'] and actual['unit']==sample['unit']=='MPa'
  assert sample['relative_error_against_represented_F_A_MPa']==1.2694501751682153e-6
 scaled.append({'mode':mode,'actual_request':str(request_path),'request_sha256':sha(request_path),'actual_raw':str(raw_path),'raw_sha256':sha(raw_path),'producer_semantic_id':raw['producer']['semantic_contract_id'],'receipt_status':receipt['status'],'case_outcome':receipt['cases'][0]['outcome'],'samples_match_owning_oracle':True,'sample_count':len(row['samples']),'recorded_oracle_error':row['samples'][0]['relative_error_against_represented_F_A_MPa'],'oracle_basis':row['oracle']})
cli=SOURCE/'projects/chirality-piping/core/serialization/canonical_json/src/bin/openpipestress_jcs_ijson.rs'
cli_expected=next(x for x in basis['basis'] if x['origin'].endswith('/src/bin/openpipestress_jcs_ijson.rs'))
assert sha(cli)==cli_expected['sha256']
cli_text=cli.read_text(); assert 'io::stdin().read_to_string(&mut input)' in cli_text
text=(D/'DESIGN.md').read_text()
assert 'Declare and enforce new-profile-only bounded request-byte, nesting and token limits' in text
assert 'no inherited generic v1 request/token limit is claimed or retrofitted here' in text
assert 'that probe is not the unsafe-admission reproduction' in text
assert 'A later structurally scaled request' in text
return_text=(D/'RETURN.md').read_text()
assert 'This pair is a scalar represented-operand example' in return_text
assert 'A separate later scaled request' in return_text
results={'status':'PASS','scope':'Final three-file attribution + prospective parser-limit wording only; prior six-file independent review preserved.','packet':packet,'added_basis_sources':additional,'scalar_reference_record':{'origin':str(D/'_run_records/INDEPENDENT_REVIEW/PYTHON_REFERENCE.json'),'sha256':sha(D/'_run_records/INDEPENDENT_REVIEW/PYTHON_REFERENCE.json'),'recorded_values':scalar,'classification':'previously independently evaluated scalar represented-operand arithmetic; not rerun and not production execution'},'initial_probe':{'request':str(RUN/'_run_records/stress_range_before/dense_scrutiny.request.json'),'request_sha256':sha(RUN/'_run_records/stress_range_before/dense_scrutiny.request.json'),'raw':str(RUN/'_run_records/stress_range_before/dense_scrutiny.raw.json'),'raw_sha256':sha(RUN/'_run_records/stress_range_before/dense_scrutiny.raw.json'),'producer_semantic_id':initial_raw['producer']['semantic_contract_id'],'ordinary_quality':initial_raw['numerical_quality']['status'],'source_receipt_present':False,'actual_refusal':refused[0]},'scaled_pre_repair_producer_records':scaled,'parser_wording':{'cli_origin':str(cli),'cli_sha256':sha(cli),'source_observation':'Whole current checked CLI file read: stdin read_to_string has no explicit request-byte or token-count cap. This is not a claim that serde has no implementation nesting limit.','prospective_new_profile_limits_explicit':True,'inherited_generic_v1_request_token_limit_claim':False},'new_arithmetic_or_product_runs':False}
(B/'CHECKS.json').write_text(json.dumps(results,indent=2)+'\n')
(B/'FINAL_CHECKED_HASHES.json').write_text(json.dumps({'scope':'Final DESIGN/RETURN/BASIS narrow delta; unchanged remainder retains prior independent review.','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':packet},indent=2)+'\n')
print(json.dumps({'status':'PASS','changed_files':[x['file'] for x in packet if x['changed']],'added_source_hashes_checked':len(additional),'actual_scaled_modes':[x['mode'] for x in scaled],'new_product_or_math_execution':False},indent=2))
