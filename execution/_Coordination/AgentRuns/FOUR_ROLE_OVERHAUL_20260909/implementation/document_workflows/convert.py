from pathlib import Path
import re, json, shutil, hashlib, yaml
ROOT=Path.cwd()
E=ROOT/'execution/_Coordination/AgentRuns/FOUR_ROLE_OVERHAUL_20260909'
plan=json.loads((E/'implementation/MIGRATION_PLAN.json').read_text())
assigned=plan['assignments']['document_workflows']
rolemap={Path(x['source']).stem.removeprefix('AGENT_'):Path(x['destination']).parent.name for x in plan['dispositions'] if x['disposition'] in ('workflow','merge-workflow')}
manager={'CHANGE','DBM_PUBLISHER','DOMAIN_DECOMP','DOMAIN_ENGINE','DRAWING_EXTRACT','EQUATION_AUDIT','EVALUATION','PDF2MD','PROJECT_DECOMP','PROJECT_SETUP','RECONCILIATION','RESEARCH','REVIEW','SCOPE_CHANGE','SOFTWARE_DECOMP','TASK_MANAGEMENT'}
def remove_section(s,heading):
 return re.sub(r'^## '+re.escape(heading)+r'\n.*?(?=^## |\Z)','',s,flags=re.M|re.S)
def clean(s):
 s=re.sub(r'^\[\[.*?\]\]\s*\n','',s,flags=re.M)
 s=re.sub(r'^TaskProfile:.*\n','',s,flags=re.M)
 s=re.sub(r'^- `TaskProfile`.*\n','',s,flags=re.M)
 s=remove_section(s,'TaskProfile')
 for r,n in rolemap.items():
  s=s.replace('agents/AGENT_'+r+'.md','workflows/'+n+'/WORKFLOW.md').replace('AGENT_'+r+'.md','workflows/'+n+'/WORKFLOW.md')
  s=re.sub(r'(?m)^(RequestedBy:\s*)'+re.escape(r)+r'\s*$',r'\1WORKING_ITEMS\nParentWorkflow: '+n,s)
 s=s.replace('skills/','workflows/').replace('SKILL.md','WORKFLOW.md').replace('TaskSkill:','Workflow:')
 s=s.replace('BRIEF_SCHEMA.md','CONTRACT.md#brief').replace('QA_CHECKS.md','CONTRACT.md#acceptance').replace('TOOL_POLICY.md','CONTRACT.md#tool-use')
 # Names in prose become workflow references. Identifier substrings in schemas stay unchanged.
 for r,n in sorted(rolemap.items(),key=lambda x:-len(x[0])):
  s=re.sub(r'(?<![A-Z_/-])'+re.escape(r)+r'(?![A-Z_-])',n,s)
 s=re.sub(r'\bskills\b','workflows',s)
 s=re.sub(r'\bskill\b','workflow',s)
 s=s.replace('Skills','Workflows').replace('Skill','Workflow').replace('SKILL —','WORKFLOW —')
 s=s.replace('strong-model semantic reasoning','semantic reasoning')
 s=s.replace('tools/pdf2md/clean_pdf2md_output.py','tools/reporting/clean_pdf2md_output.py')
 s=re.sub(r'^.*(?:chirality-task-profile|chirality-skill-version|chirality-workflow-version).*\n','',s,flags=re.M)
 s=re.sub(r'\n(?:---\s*\n){2,}','\n---\n',s)
 s=re.sub(r'\n{4,}','\n\n\n',s)
 return s.strip()+'\n'
def front(name,description):
 return '---\nname: '+name+'\ndescription: '+json.dumps(description,ensure_ascii=False)+'\n---\n\n'
def execution(dst,commands,roles):
 obj={'schema_version':1,'compatible_roles':roles}
 if commands is not None:obj['tools']={'commands':commands}
 (dst/'execution.json').write_text(json.dumps(obj,indent=2)+'\n')
coverage=[]
for name in assigned['existing']:
 src=ROOT/'skills'/name; dst=ROOT/'workflows'/name
 raw=(src/'SKILL.md').read_text(); fm,body=raw.split('---',2)[1:]
 meta=yaml.safe_load(fm); sourcehash=hashlib.sha256(raw.encode()).hexdigest()
 shutil.move(str(src),str(dst)); (dst/'SKILL.md').unlink()
 body=clean(body)
 body=remove_section(body,'Suitable agent shells')
 body=remove_section(body,'Typical dispatcher')
 # Package-specific schema and QA are a single selectively loaded resource.
 parts=[]
 for filename,title in [('BRIEF_SCHEMA.md','Brief'),('QA_CHECKS.md','Acceptance'),('TOOL_POLICY.md','Tool use')]:
  path=dst/filename
  if not path.exists():continue
  text=clean(path.read_text())
  text=re.sub(r'^# .+\n','',text,count=1)
  if filename=='TOOL_POLICY.md':
   text=re.sub(r'^### TASK-enforced\n.*?(?=^### |^## |\Z)','',text,flags=re.M|re.S)
   text=re.sub(r'^_Tools named.*\n','',text,flags=re.M)
  # Demote heading hierarchy under the resource's selected section.
  text=re.sub(r'^(#{2,}) ',r'#\1 ',text,flags=re.M)
  parts.append('## '+title+'\n\n'+text.strip()+'\n')
  path.unlink()
 (dst/'CONTRACT.md').write_text('# '+name+' contract\n\n'+'\n'.join(parts))
 body=re.sub(r'^# .*\n','# '+name+'\n',body,count=1)
 body=body.replace('`WORKFLOW.md`','`WORKFLOW.md`')
 intro='\nLoad [CONTRACT.md](CONTRACT.md) when preparing the brief or validating the result; it contains the input schema, output checks, and tool responsibilities. Resolve repository commands against the brief\'s declared tool root.\n'
 legacy=meta.get('metadata',{}).get('chirality-skill-status')=='LEGACY' or name in {'pdf2md-page','pdf2md-page-assets'}
 if legacy:intro+='\nStatus: LEGACY. Use for explicitly selected historical or resume contracts; the current orchestration selects the replacement workflow.\n'
 body=body.replace('# '+name+'\n','# '+name+'\n'+intro,1)
 commands=meta.get('allowed-tools')
 if isinstance(commands,str):commands=[c.strip() for c in commands.split(', ') if c.strip()]
 # The symbol-instance method can use crop tooling supplied in its bounded brief.
 if commands is None and name!='pandid-valve-symbol-instance':commands=[]
 execution(dst,commands,['TASK','WORKING_ITEMS','HELPS_HUMANS'])
 (dst/'WORKFLOW.md').write_text(front(name,clean(meta['description']).strip())+body)
 coverage.append({'source':'skills/'+name+'/SKILL.md','source_sha256':sourcehash,'destination':'workflows/'+name+'/WORKFLOW.md','disposition':'migrate-workflow','status':'LEGACY' if legacy else 'ACTIVE','resources':['CONTRACT.md','execution.json']})

# Orchestration packages carry concise entrypoints and selected detailed resources.
for role,name in [('DBM_PUBLISHER','dbm-publisher'),('DRAWING_EXTRACT','drawing-extract'),('EQUATION_AUDIT','equation-audit'),('PDF2MD','pdf2md-orchestration')]:
 src=E/'source_basis/agents'/('AGENT_'+role+'.md'); raw=src.read_text()
 body=raw.split('---',2)[2]
 # Extract exact normative protocol, structure and spec; retain detailed schemas, not role envelopes.
 sections={}
 for sec in ['PROTOCOL','SPEC','STRUCTURE']:
  sections[sec]=re.search(r'^## '+sec+r'\n(.*?)(?=^## (?:PROTOCOL|SPEC|STRUCTURE|RATIONALE)\n|\Z)',body,re.M|re.S).group(1)
 prefix=body.split('## PROTOCOL')[0]
 start={'DBM_PUBLISHER':'## Runtime variables and defaults','DRAWING_EXTRACT':'## Drawing-type + extraction-target registry','EQUATION_AUDIT':'## Runtime Parameters','PDF2MD':'## Runtime Parameters'}[role]
 prefix=prefix[prefix.index(start):]
 for title in ['Precedence (conflict resolution)','Precedence','Dispatch Model Guidance','Explicit non-ownership']:
  prefix=remove_section(prefix,title)
 prefix=prefix.replace('## Non-negotiable invariants','## Publication requirements').replace('## Non-negotiable Invariants','## Workflow requirements')
 dst=ROOT/'workflows'/name; dst.mkdir(parents=True,exist_ok=True)
 (dst/'PROCEDURE.md').write_text('# '+name+' procedure\n\nWORKING_ITEMS coordinates this procedure and assigns bounded visual or semantic stages to TASK. Tool commands resolve against the declared tool root.\n\n'+clean(sections['PROTOCOL']))
 (dst/'CONTRACT.md').write_text('# '+name+' contract\n\n'+clean(prefix)+'\n## Artifacts and tool interfaces\n\n'+clean(sections['STRUCTURE']))
 spec=clean(sections['SPEC'])
 # Evidence matrices duplicate the detailed procedure; substantive success requirements remain.
 spec=re.split(r'^### Spec-satisfaction matrix',spec,flags=re.M)[0].strip()+'\n'
 (dst/'ACCEPTANCE.md').write_text('# '+name+' acceptance\n\n'+spec)
 execution(dst,None,['WORKING_ITEMS'])
 coverage.append({'source':'agents/AGENT_'+role+'.md','source_sha256':hashlib.sha256(raw.encode()).hexdigest(),'destination':'workflows/'+name+'/WORKFLOW.md','disposition':'workflow','status':'ACTIVE','resources':['PROCEDURE.md','CONTRACT.md','ACCEPTANCE.md','execution.json']})
 (ROOT/'agents'/('AGENT_'+role+'.md')).unlink()
(E/'implementation/document_workflows/COVERAGE.json').write_text(json.dumps({'schema_version':1,'assignments':coverage},indent=2)+'\n')
print('Converted',len(coverage),'sources; manager entrypoints next.')
