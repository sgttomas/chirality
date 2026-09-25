from pathlib import Path
import sqlite3,json,hashlib,sys
store=Path('/Users/ryan/Library/Application Support/com.chirality.swbpipe/openpipestress-projects.sqlite3')
c=sqlite3.connect(store.as_uri()+'?mode=ro',uri=True)
pid='project:blank-local-20260925t030113z'
keys=['project_id','model_json','editor_intents_json','mechanics_result_json','analysis_run_json','model_hash_json','project_envelope_hash_json']
row=c.execute('SELECT '+','.join(keys)+' FROM local_projects WHERE project_id=?',(pid,)).fetchone();assert row
record=dict(zip(keys,row));model=json.loads(record['model_json']);assert model['project']['id']==pid and len(model['nodes'])==2
label=sys.argv[1];assert label.isascii() and label.replace('-','').isalnum()
p=Path(__file__).parent/'private-rows';p.mkdir(exist_ok=True)
(p/(label+'.json')).write_text(json.dumps({'store_read_only':str(store),'query_project_id':pid,'row':record,'model_json_sha256':hashlib.sha256(record['model_json'].encode()).hexdigest()},indent=2)+'\n')
result=json.loads(record['mechanics_result_json']);case=next(x for x in model['load_cases'] if x['id']=='case:weight')
summary={'project_id':pid,'density':model['pipe_segments'][0]['section'].get('material_density'),'span_tip_x':model['nodes'][1]['position']['x'],'model_hash':json.loads(record['model_hash_json']),'load_ids':[x['id'] for x in case['primitive_loads']],'magnitudes':[x['magnitude'] for x in case['primitive_loads']],'result_status':result.get('status') if isinstance(result,dict) else None,'reactions':[x for x in result.get('results',[]) if 'reaction' in x.get('kind','')][:12] if isinstance(result,dict) else [],'diagnostics':[x.get('code') for x in result.get('diagnostics',[])] if isinstance(result,dict) else []}
q=Path(__file__).parent/'row-audits';q.mkdir(exist_ok=True);(q/(label+'.json')).write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
