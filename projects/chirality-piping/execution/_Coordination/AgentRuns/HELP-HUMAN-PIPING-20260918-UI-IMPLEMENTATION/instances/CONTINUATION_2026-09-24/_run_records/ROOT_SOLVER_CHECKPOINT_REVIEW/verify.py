from pathlib import Path
import json,hashlib,subprocess,math,re
out=Path(__file__).parent
c=json.loads((out/'candidate.json').read_text()); r=Path(c['root']); paths=c['paths']; sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks={}; checks['candidate_count']=len(paths);checks['candidate_hash_mismatches']=[x['path'] for x in paths if sha(r/x['path'])!=x['sha256']]
native=r/paths[2]['path'];native=native.parent; custody=json.loads((native/'CUSTODY.json').read_text());private=Path(custody['private_source_root'])
checks['committed_raw_count']=len(custody['committed_raw_files']); checks['raw_copy_mismatches']=[]
for x in custody['committed_raw_files']:
 a=native/x['path'];b=private/Path(x['path']).relative_to('_run_records')
 if sha(a)!=x['sha256'] or sha(b)!=x['sha256'] or a.stat().st_size!=x['bytes']: checks['raw_copy_mismatches'].append(x['path'])
checks['private_hash_count']=len(custody['private_only_files']); checks['private_hash_mismatches']=[x['private_relative_path'] for x in custody['private_only_files'] if sha(private/x['private_relative_path'])!=x['sha256'] or (private/x['private_relative_path']).stat().st_size!=x['bytes']]
inputs=json.loads((native/'_run_records/inputs-pre.json').read_text());m35=Path('/private/tmp/piping-generated-loads-20260924');checks['native_input_count']=len(inputs);checks['native_input_mismatches']=[x['path'] for x in inputs if sha(m35/x['path'])!=x['sha256']]
git=lambda root,*args:subprocess.check_output(['git',*args],cwd=root,text=True).strip()
checks['m35_head']=git(m35,'rev-parse','HEAD');checks['m35_tracked_dirty']=git(m35,'diff','--name-only','HEAD')
selectors=['projects/chirality-piping/apps/desktop','projects/chirality-piping/core','projects/chirality-piping/schemas','projects/chirality-piping/fixtures','projects/chirality-piping/package.json','projects/chirality-piping/package-lock.json']
checks['built_to_current_native_input_diff']=git(m35,'diff','--name-status',custody['built_candidate'],custody['current_candidate'],'--',*selectors)
a=json.loads((native/'_run_records/artifact-identity.json').read_text());checks['native_executable_hash_matches']=sha(Path(a['executable']))==a['executable_sha256'];checks['native_bundle_hash_mismatches']=[x['path'] for x in a['bundle_files'] if sha(Path(a['app'])/x['path'])!=x['sha256']]
checks['pre_post_identical']=(native/'_run_records/inputs-pre.json').read_bytes()==(native/'_run_records/inputs-post.json').read_bytes()
checks['audit_reconstruction_mismatches']=[];models={};results={}
for name in ['baseline','refreshed','span3','manual-preserved','manual-density4000']:
 d=json.loads((private/'private-rows'/f'{name}.json').read_text());row=d['row'];model=json.loads(row['model_json']);result=json.loads(row['mechanics_result_json']);models[name]=model;results[name]=result
 assert d['model_json_sha256']==hashlib.sha256(row['model_json'].encode()).hexdigest(); assert d['query_project_id']==model['project']['id']=='project:blank-local-20260925t030113z'
 case=next(x for x in model['load_cases'] if x['id']=='case:weight')
 derived={'project_id':d['query_project_id'],'density':model['pipe_segments'][0]['section'].get('material_density'),'span_tip_x':model['nodes'][1]['position']['x'],'model_hash':json.loads(row['model_hash_json']),'load_ids':[x['id'] for x in case['primitive_loads']],'magnitudes':[x['magnitude'] for x in case['primitive_loads']],'result_status':result.get('status'),'reactions':[x for x in result.get('results',[]) if 'reaction' in x.get('kind','')][:12],'diagnostics':[x.get('code') for x in result.get('diagnostics',[])]}
 if derived!=json.loads((native/'_run_records/row-audits'/f'{name}.json').read_text()):checks['audit_reconstruction_mismatches'].append(name)
checks['manual_density_invariance']={'density_before':models['manual-preserved']['pipe_segments'][0]['section']['material_density']['value'],'density_after':models['manual-density4000']['pipe_segments'][0]['section']['material_density']['value'],'all_load_cases_equal':models['manual-preserved']['load_cases']==models['manual-density4000']['load_cases'],'all_results_equal':results['manual-preserved']['results']==results['manual-density4000']['results']}
checks['independent_balance']=[]
for name in models:
 m=models[name];res=results[name];case=next(x for x in m['load_cases'] if x['id']=='case:weight');loads=case['primitive_loads'];q=loads[0]['magnitude']['value'];tip=loads[1]['magnitude']['value'] if len(loads)>1 else 0;L=m['nodes'][1]['position']['x']
 expectedF=-q*L-tip;expectedM=-q*L*L/2-tip*L
 actualF=next(x['value'] for x in res['results'] if x['kind']=='reaction_resultant');actualM=next(x['value'] for x in res['results'] if x['kind']=='element_local_bending_moment_z' and x['metadata']['location']=='end_i')
 checks['independent_balance'].append({'state':name,'force_error':actualF-expectedF,'moment_error':actualM-expectedM,'rounded_matches':round(expectedF,6)==actualF and round(expectedM,6)==actualM})
checks['privacy_full_model_markers']={}
for x in paths:
 p=r/x['path'];s=p.read_text()
 if any(k in s for k in ['"nodes": [','"pipe_segments": [','"model_json": "','"operations": [']):checks['privacy_full_model_markers'][x['path']]=True
checks['input_basis_hashes']=[{'path':p,'sha256':sha(r/p)} for p in ['AGENTS.md','agents/AGENT_TASK.md','projects/chirality-piping/AGENTS.md','projects/chirality-piping/loop/LOOP_INIT.md','.agents/skills/software-code-review/SKILL.md']]
checks['review_inputs']=[{'path':p.name,'sha256':sha(p)} for p in [out/'candidate.json',out/'graph.diff']]
checks['checkpoint_heads']={x:git(Path(x),'rev-parse','HEAD') for x in ['/private/tmp/piping-numerical-corrections-20260924','/private/tmp/piping-pressure-stress-20260924','/private/tmp/piping-engine-integration-20260925']}
(out/'verification.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps({k:v for k,v in checks.items() if k not in ['input_basis_hashes','review_inputs']},indent=2))
