from pathlib import Path
import sqlite3,json,hashlib,sys
store=Path('/Users/ryan/Library/Application Support/com.chirality.swbpipe/openpipestress-projects.sqlite3')
c=sqlite3.connect(store.as_uri()+'?mode=ro',uri=True)
pid='project:blank-local-20260924t213049z'
keys=['project_id','model_json','editor_intents_json','mechanics_result_json','analysis_run_json','model_hash_json','project_envelope_hash_json']
row=c.execute('SELECT project_id,model_json,editor_intents_json,mechanics_result_json,analysis_run_json,model_hash_json,project_envelope_hash_json FROM local_projects WHERE project_id=?',(pid,)).fetchone();assert row
record=dict(zip(keys,row));model=json.loads(record['model_json']);assert model['project']['units']['temperature']=='degC';assert len(model['nodes'])==1;assert model['nodes'][0]['id']=='node:native72-unit-check';assert model['nodes'][0]['position']=={'x':1,'y':2,'z':3}
label=sys.argv[1];assert label.isascii() and label.replace('-','').isalnum()
out=Path(__file__).parent/'ui'/(label+'.json');out.write_text(json.dumps({'store_read_only':str(store),'query_project_id':pid,'row':record,'model_json_sha256':hashlib.sha256(record['model_json'].encode()).hexdigest()},indent=2)+'\n');print({'temperature':model['project']['units']['temperature'],'persisted_nodes':len(model['nodes']),'position':model['nodes'][0]['position'],'model_hash':json.loads(record['model_hash_json'])})
