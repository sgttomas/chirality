from pathlib import Path
import json,re,subprocess,hashlib,yaml
ROOT=Path(__file__).resolve().parents[6]
# Derive repository from the run directory, independent of invocation cwd.
while not (ROOT/'AGENTS.md').is_file():ROOT=ROOT.parent
RUN=ROOT/'execution/_Coordination/AgentRuns/FOUR_ROLE_OVERHAUL_20260909';E=RUN/'implementation/project_workflows';p=json.loads((RUN/'implementation/MIGRATION_PLAN.json').read_text());owned=[x for x in p['dispositions'] if x['owner']=='project_workflows'];dirs={ROOT/Path(x['destination']).parent for x in owned};checks=[]
def check(name,ok,detail=None):checks.append({'check':name,'passed':bool(ok),'detail':detail})
check('48 assigned source dispositions / 46 workflow entrypoints',len(owned)==48 and len(dirs)==46)
issues=[]
for d in dirs:
 try:
  y=yaml.safe_load((d/'WORKFLOW.md').read_text().split('---',2)[1]);assert y['name']==d.name and set(y)=={'name','description'}
  c=json.loads((d/'execution.json').read_text());assert c['schema_version']==1 and 'stages' not in c
 except Exception as exc:issues.append({'path':str(d),'error':str(exc)})
check('frontmatter and execution contracts',not issues,issues)
check('assigned former sources removed',all(not (ROOT/x['source']).exists() for x in owned))
check('frozen agent sources preserved',all(hashlib.sha256((RUN/'source_basis'/x['source']).read_bytes()).hexdigest()==x['source_sha256'] for x in owned if x['source'].startswith('agents/')))
check('NEXT_INSTANCE contracts absent',all('NEXT_INSTANCE_' not in f.read_text() for d in dirs for f in d.rglob('*.md')))
check('role envelopes absent from resources',all(not re.search(r'^## Agent Type|^AGENT_TYPE:|^\[\[BEGIN:',f.read_text(),re.M) for d in dirs for f in d.rglob('*.md')))
missing=[];validlinks=0
for d in dirs:
 for f in d.rglob('*.md'):
  for href in re.findall(r'\]\(([^)]+)\)',f.read_text()):
   if re.match(r'https?:|#|mailto:',href) or any(x in href for x in '{}<>…') or href in ['path','...']:continue
   path=href.split('#')[0]
   if path and not (f.parent/path).exists():missing.append({'file':str(f.relative_to(ROOT)),'href':href})
   else:validlinks+=1
check('concrete markdown links resolve',not missing,{'checked':validlinks,'missing':missing})
resolver=ROOT/'tools/workflow_runtime/resolve_workflow.py'
cases=[('project selected contract',['--role','WORKING_ITEMS','--workflow','project-decomp','--resource','resources/contract.md'],0),('bounded researcher selected evidence',['--role','TASK','--workflow','researcher','--resource','resources/evidence.md','--resource','resources/inquiry.md'],0),('TASK cannot orchestrate research',['--role','TASK','--workflow','research-orchestration'],2),('matching legacy selector',['--role','TASK','--workflow','researcher','--task-skill','researcher'],0),('unbound scope placeholder rejected',['--role','TASK','--workflow','scope-of-work'],2),('conflicting selectors',['--role','TASK','--workflow','scope-of-work','--task-skill','researcher'],2),('missing selected resource',['--role','TASK','--workflow','researcher','--resource','resources/absent.md'],2)]
for name,args,expected in cases:
 r=subprocess.run(['python3',str(resolver),'--root',str(ROOT),*args],cwd='/tmp',capture_output=True,text=True);data=None
 try:data=json.loads(r.stdout)
 except json.JSONDecodeError:pass
 detail={'exit':r.returncode,'expected':expected}
 if data:detail['loaded_paths']=[x.get('path') for x in data.get('context',[])];detail['enforcement']=data.get('enforcement')
 else:detail['error']=r.stderr.strip()
 check('resolver from foreign cwd: '+name,r.returncode==expected,detail)
r=subprocess.run(['python3','tools/validation/validate_workflow_metadata.py','workflows','--json'],cwd=ROOT,capture_output=True,text=True);result=json.loads(r.stdout);check('library workflow validator',r.returncode==0,{'count':result.get('checked_workflow_count'),'invalid':result.get('invalid_workflow_count')})
report={'status':'PASS' if all(c['passed'] for c in checks) else 'FAIL','checks':checks};(E/'VALIDATION.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
