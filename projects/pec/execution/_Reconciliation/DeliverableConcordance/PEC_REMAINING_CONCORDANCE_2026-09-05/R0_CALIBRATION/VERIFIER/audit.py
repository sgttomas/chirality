import csv,hashlib,json,re,subprocess,sys,os,tempfile,argparse,importlib.util
from pathlib import Path
repo=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip())
r=repo/'projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05'; out=r/'R0_CALIBRATION/VERIFIER'
base='faf22452528b5ba895e88ba0ad3770855100de08'; read={}; errors=[]; hist=[]
def consume(p):
 p=Path(p); p=p if p.is_absolute() else repo/p
 b=p.read_bytes();read[str(p.relative_to(repo))]=hashlib.sha256(b).hexdigest();return b
m=json.loads(consume(r/'SOURCE_MANIFEST.json'));orig=json.loads(consume(r/'ORIGINAL_WORKER_MANIFEST.json'))
for p,h in m['hashes'].items():
 if hashlib.sha256(consume(p)).hexdigest()!=h:errors.append('source drift '+p)
for p,h in orig['hashes'].items():
 if hashlib.sha256(consume(p)).hexdigest()!=h:errors.append('worker drift '+p)
def scan_manifest(obj):
 if isinstance(obj,dict):
  if isinstance(obj.get('path'),str) and isinstance(obj.get('sha256'),str):
   p=obj['path']
   obj=dict(obj)
   if obj.get('source_commit'):obj['commit']=obj['source_commit']
   if (repo/p).is_file() and not obj.get('commit'):
    if hashlib.sha256(consume(p)).hexdigest()!=obj['sha256']:errors.append('read hash '+p)
   if obj.get('commit'):
    try:
     b=subprocess.check_output(['git','show',obj['commit']+':'+p],stderr=subprocess.DEVNULL); h=hashlib.sha256(b).hexdigest(); hist.append({'path':p,'commit':obj['commit'],'sha256':h})
     if h!=obj['sha256']:errors.append('historical drift '+p)
    except subprocess.CalledProcessError:pass
  for k,v in obj.items():
   if isinstance(v,str) and re.fullmatch('[0-9a-f]{64}',v) and (repo/k).is_file():
    if hashlib.sha256(consume(k)).hexdigest()!=v:errors.append('read map hash '+k)
   elif isinstance(v,(list,dict)):scan_manifest(v)
 elif isinstance(obj,list):
  for v in obj:scan_manifest(v)
coverage=[]; holds=[]
for did,target in m['sample'].items():
 d=r/'R0_CALIBRATION'/did
 wm=json.loads(consume(d/'READ_MANIFEST.json'));scan_manifest(wm)
 claims=list(csv.DictReader(consume(d/'CLAIMS.csv').decode().splitlines()));res=list(csv.DictReader(consume(d/'RESIDUALS.csv').decode().splitlines()))
 ids={x['ClaimID'] for x in claims};rids={x['ResidualID'] for x in res}
 for x in claims:
  for rid in filter(None,map(str.strip,x['ProposedResidualID'].split(';'))):
   if rid not in rids:errors.append('bad residual link '+x['ClaimID']+' '+rid)
 for x in res:
  for cid in filter(None,map(str.strip,x['ClaimIDs'].split(';'))):
   if cid not in ids:errors.append('bad claim link '+x['ResidualID']+' '+cid)
   elif x['ResidualID'] not in next(y for y in claims if y['ClaimID']==cid)['ProposedResidualID']:errors.append('nonreciprocal '+cid)
 sow=repo/target/'ScopeOfWork.md'; defs=set()
 if sow.exists():
  txt=consume(sow).decode();defs=set(re.findall(r'^- \*\*((?:REQ|AC|VER)-\d{3})\*\*',txt,re.M));missing=defs-{x.split('::')[1] for x in ids}
  if missing:errors.append('uncovered '+did+str(missing))
 for filename in ['ScopeOfWork.md','_STATUS.md']:
  target_file=str((Path(target)/filename).relative_to('projects/pec'))
  cmd=[sys.executable,'projects/pec/execution/_Scripts/pec_reliance_hold.py','--register','projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv','--target',target_file,'--operation','exact-correction-preparation']
  x=subprocess.run(cmd,cwd=repo,text=True,capture_output=True);holds.append({'command':cmd,'exit_code':x.returncode,'stdout':x.stdout,'stderr':x.stderr})
  if x.returncode:errors.append('hold '+target_file)
 coverage.append({'deliverable':did,'claims':len(claims),'residuals':len(res),'REQ_AC_VER_definitions':len(defs),'lowest_aligned':min((x['ClaimID'] for x in claims if x['Disposition']=='ALIGNED'),default=None),'non_aligned':[x['ClaimID'] for x in claims if x['Disposition']!='ALIGNED']})
for p in ['AGENTS.md','projects/pec/AGENTS.md','agents/AGENT_RECONCILIATION.md','docs/DELIVERABLE_CONCORDANCE_METHOD.md','projects/pec/execution/_Scripts/pec_reliance_hold.py']:
 consume(p)
for n in ['RUN_BASIS.md','STRUCTURAL_FANIN.json','CONVENTIONS.md','MANAGER_SOURCE_AUDIT.json','validate_sample.py']:consume(r/n)
# Independent AST-only probes; no candidate source is executed.
cp=repo/'projects/pec/v2/tools/check_service_core_posture.py';consume(cp)
spec=importlib.util.spec_from_file_location('independent_posture',cp);checker=importlib.util.module_from_spec(spec);sys.modules[spec.name]=checker;spec.loader.exec_module(checker)
probes=[]
texts={
 'udp_external':'import socket\ns = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)\ns.sendto(b"probe", ("198.51.100.10", 443))\n',
 'alias_dynamic':'from importlib import import_module as load\nload("requests")\n',
 'direct_third_party_control':'import requests\n',
 'external_tcp_control':'import socket\nsocket.create_connection(("198.51.100.10", 443))\n',
 'loopback_control':'import socket\nsocket.create_connection(("127.0.0.1", 443))\n'}
for name,source in texts.items():
 with tempfile.TemporaryDirectory(prefix='pec-r0-verifier-',dir='/tmp') as td:
  p=Path(td);(p/'core').mkdir();(p/'core/probe.py').write_text(source);(p/'config.json').write_text(json.dumps({'schema_version':1,'target':'core','pec_local_source_root':'.','workspace_runtime_contract_packages':[]}))
  x=checker.evaluate(argparse.Namespace(config=str(p/'config.json'),workflow=str(repo/'projects/pec/software-workflow.json'),project_root=td,induce_tool_failure=False));probes.append({'name':name,'source':source,'sha256':hashlib.sha256(source.encode()).hexdigest(),'result':x})
sys.path.insert(0,str(repo/'projects/pec/v2/src'))
from pec_v2.adapters.config.loop_registry import JsonLoopRegistry,LoopRegistryConfigError
registry=[]
for loc in ['projects/pec/loop/LOOP_INIT.md','projects//pec/loop/LOOP_INIT.md','./projects/pec/loop/LOOP_INIT.md','projects/./pec/loop/LOOP_INIT.md','../pec/LOOP_INIT.md','/pec/LOOP_INIT.md']:
 try:
  val=JsonLoopRegistry('/tmp/not-read-r0.json')._validate_document({'schema_version':1,'loops':[{'loop_id':'pec','loop_init_path':loc}]});registry.append({'input':loc,'outcome':'ACCEPT','returned':val[0].loop_init_path})
 except LoopRegistryConfigError as e:registry.append({'input':loc,'outcome':'REJECT','error':str(e)})
struct=subprocess.run([sys.executable,str(r/'validate_sample.py')],capture_output=True,text=True);structval=json.loads(struct.stdout)
if structval!=json.loads((r/'STRUCTURAL_FANIN.json').read_text()):errors.append('structural difference')
# Hash and read C05 historical pair; retain exact diff for adjudication.
paths=[str(Path(m['sample']['DEL-00-03'])/f) for f in ['ScopeOfWork.md','artifacts/v2/SPEC.md']]
for p in paths:
 b=subprocess.check_output(['git','show','411cbe6ce7b03477889adf50e3d1665a61387db6:'+p]);hist.append({'path':p,'commit':'411cbe6ce7b03477889adf50e3d1665a61387db6','sha256':hashlib.sha256(b).hexdigest()})
diff=subprocess.check_output(['git','diff','411cbe6ce7b03477889adf50e3d1665a61387db6',base,'--',*paths],text=True)
(out/'C05_SOURCE_DIFF.txt').write_text(diff)
(out/'PROBE_RESULTS.json').write_text(json.dumps({'scanner':probes,'registry':registry,'method':'AST-only scanner text; registry document validation only; no sockets, imports from fixture or service runs'},indent=2)+'\n')
(out/'AUDIT_RESULTS.json').write_text(json.dumps({'status':'PASS' if not errors else 'REVISE','errors':errors,'coverage':coverage,'structural_reproduction':structval,'holds':holds,'original_worker_files':len(orig['hashes']),'read_source_count':len(read)},indent=2)+'\n')
# Hash-only validation does not imply that every full historical source received semantic review.
(out/'READ_MANIFEST.json').write_text(json.dumps({'source_commit':base,'hashes':dict(sorted(read.items())),'historical_sources':hist,'read_semantics':'Full worker ledgers/manifests consumed; targeted semantic source inspection described in VERIFICATION.md. Additional source bytes hashed for complete preservation audit, not blanket semantic review.','source_unchanged':all(hashlib.sha256((repo/p).read_bytes()).hexdigest()==h for p,h in read.items()),'original_workers_unchanged':all(hashlib.sha256((repo/p).read_bytes()).hexdigest()==h for p,h in orig['hashes'].items())},indent=2)+'\n')
print(json.dumps({'errors':errors,'sources':len(read),'workers':len(orig['hashes']),'coverage':coverage},indent=2))
