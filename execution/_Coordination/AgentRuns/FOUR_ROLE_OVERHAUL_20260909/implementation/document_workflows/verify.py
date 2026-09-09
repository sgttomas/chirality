from pathlib import Path
import json,re,hashlib,importlib.util,subprocess,yaml
root=Path(__file__).resolve().parents[6]
# Resolve root from recorded run location, independent of caller working directory.
while not (root/'agents/registry.json').is_file():root=root.parent
E=root/'execution/_Coordination/AgentRuns/FOUR_ROLE_OVERHAUL_20260909'
C=E/'implementation/document_workflows'
coverage=json.loads((C/'COVERAGE.json').read_text())
plan=json.loads((E/'implementation/MIGRATION_PLAN.json').read_text())
original={x['source']:x for x in plan['dispositions'] if x.get('owner')=='document_workflows'}
loader=importlib.util.spec_from_file_location('resolver',root/'tools/workflow_runtime/resolve_workflow.py'); module=importlib.util.module_from_spec(loader);loader.loader.exec_module(module)
checks=[];artifacts=[]
def check(name,condition,detail=None):
 checks.append({'check':name,'passed':bool(condition),**({'detail':detail} if detail else {})})
check('exact assigned coverage',set(original)=={x['source'] for x in coverage['assignments']})
check('25 unique workflow destinations',len({x['destination'] for x in coverage['assignments']})==25)
for item in coverage['assignments']:
 name=Path(item['destination']).parent.name;dest=root/item['destination'];package=dest.parent
 raw=dest.read_text();meta=yaml.safe_load(raw.split('---',2)[1])
 check(name+': minimal frontmatter',set(meta)=={'name','description'} and meta['name']==name and bool(meta['description']))
 check(name+': source fingerprint',item['source_sha256']==original[item['source']]['source_sha256'])
 check(name+': old package retired',not (root/item['source']).exists())
 cfg=json.loads((package/'execution.json').read_text());manager=item['source'].startswith('agents/')
 role='WORKING_ITEMS' if manager else 'TASK'
 r=module.resolve(root,role,workflow=name,resources=['CONTRACT.md'])
 check(name+': selected resource loading',len(r['context'])==3 and {x['path'] for x in r['context']}=={f'agents/AGENT_{role}.md',f'workflows/{name}/WORKFLOW.md',f'workflows/{name}/CONTRACT.md'})
 if manager:
  try:module.resolve(root,'TASK',workflow=name);compatible=True
  except ValueError:compatible=False
  check(name+': manager workflow rejects TASK',not compatible)
 else:
  before=module.resolve(root,'TASK',workflow=name,task_skill=name)
  check(name+': matching legacy selector loads once',len(before['context'])==2)
  expected=cfg.get('tools',{}).get('commands')
  check(name+': command restrictions retained',expected is None or r['effective_tools']['commands']=={'all_of':[expected]})
 text='\n'.join(p.read_text() for p in package.rglob('*.md'))
 check(name+': no next-instance contracts',not re.search(r'NEXT_INSTANCE|next.instance',text,re.I))
 check(name+': no retired package links',not re.search(r'agents/AGENT_(?!HELP_HUMAN|HELPS_HUMANS|WORKING_ITEMS|TASK)[A-Z_]+\.md|skills/|SKILL\.md|TaskProfile|TaskWorkflow|persona|allowed-tools',text))
 check(name+': no durable model allocation',not re.search(r'Sonnet|strong.model|small-tier|Two-tier|top-tier|mid-tier',text))
 missing=[]
 for path in package.rglob('*.md'):
  for ref in set(re.findall(r'(?<![\w/])tools/[\w/-]+\.(?:py|sh|json|md)',path.read_text())):
   if not (root/ref).exists():missing.append(ref)
  for link in re.findall(r'\]\(([^)]+)\)',path.read_text()):
   if any(t in link for t in ('{','<','http:','https:','...')):continue
   if not (path.parent/link.split('#')[0]).exists():missing.append(link)
 check(name+': selected links and tools exist',not missing,missing)
 for path in package.rglob('*'):
  if path.is_file():artifacts.append({'path':str(path.relative_to(root)),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
 item['resources']=[str(p.relative_to(package)) for p in sorted(package.rglob('*')) if p.is_file() and p!=dest]
 item['file_dispositions']=[]
 for f in original[item['source']].get('files',[]):
  filename=Path(f['path']).name
  target='WORKFLOW.md' if filename=='SKILL.md' else ('CONTRACT.md#brief' if filename=='BRIEF_SCHEMA.md' else 'CONTRACT.md#acceptance' if filename=='QA_CHECKS.md' else 'CONTRACT.md#tool-use' if filename=='TOOL_POLICY.md' else filename)
  item['file_dispositions'].append({'source':f['path'],'source_sha256':f['sha256'],'destination':'workflows/'+name+'/'+target})
# Cross-resource consistency defects from source audit.
eq='\n'.join(p.read_text() for p in (root/'workflows/equation-audit').glob('*.md'))
check('equation audit has single root convention','{SOURCE_AUDIT_ROOT}/equations/' not in eq and 'ALLOW_UNREVIEWED' in eq and 'overlaps == 0' in eq)
pdf='\n'.join(p.read_text() for p in (root/'workflows/pdf2md-orchestration').glob('*.md'))
check('PDF canonical inline rewrite and paired output','rewrite_inline_asset_refs.py' in pdf and 'append-only' not in pdf and 'always written by pdf2md-page-full' in pdf and 'independent evidence' in pdf)
drawing=(root/'workflows/drawing-extract/CONTRACT.md').read_text()
check('drawing target registry preserves five supported combinations',all(x in drawing for x in ['titleblock_index','top_equipment_header_basic','top_equipment_header_detailed','valve_count_basic','valve_count_detailed','ISOMETRIC','GA','page-global pixel']))
dbm=(root/'workflows/dbm-publisher/PROCEDURE.md').read_text()
check('publication preserves seven gates',set(re.findall(r'^### Gate (\d)',dbm,re.M))==set('1234567'))
cli=subprocess.run(['python3',str(root/'tools/workflow_runtime/resolve_workflow.py'),'--root',str(root),'--role','TASK','--workflow','pdf2md','--resource','CONTRACT.md'],cwd='/tmp',text=True,capture_output=True)
check('selected tool paths resolve from different cwd',cli.returncode==0 and all(x['tool'].startswith(str(root/'tools')) for x in json.loads(cli.stdout).get('resolved_commands',[])),cli.stderr if cli.returncode else None)
result={'schema_version':1,'status':'PASS' if all(x['passed'] for x in checks) else 'FAIL','checks':checks,'passed':sum(x['passed'] for x in checks),'total':len(checks)}
(C/'VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n')
(C/'COVERAGE.json').write_text(json.dumps(coverage,indent=2)+'\n')
(C/'ARTIFACT_MANIFEST.json').write_text(json.dumps({'schema_version':1,'artifacts':artifacts},indent=2)+'\n')
print(json.dumps({'status':result['status'],'passed':result['passed'],'total':result['total'],'failures':[x for x in checks if not x['passed']],'artifact_count':len(artifacts)}))
raise SystemExit(0 if result['status']=='PASS' else 1)
