from pathlib import Path
from collections import Counter
import importlib.util,json,hashlib,re
repo=Path('/private/tmp/piping-scientific-json-integration-20260925');p=repo/'projects/chirality-piping';d=Path('/private/tmp/piping-scientific-json-ci-98');head='98b423d93e41338551bf744def1e2c5a303aeaab'
spec=importlib.util.spec_from_file_location('ci_plan',p/'tools/ci/e2e_plan.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
a=json.loads((d/'run.json').read_text());assert a['status']=='completed' and a['conclusion']=='success' and a['headSha']==head
plan=json.loads((d/'selection/piping-e2e-plan.json').read_text());m.validate(repo,plan);assert plan['coverage_full'] and plan['head']==head
source=m.collected_tests(json.loads((d/'barrier/source.stdout.json').read_text()));m.validate_source(source)
selected=[];input_hashes={}
for directory in [d/'barrier']+[d/f'shard-{i}' for i in range(1,5)]:
 c=json.loads((directory/'collection.json').read_text());assert c['status']=='validated' and c['head']==head
 selected+=c['execution_tests'];identity=c['identity'];assert hashlib.sha256((p/'apps/desktop/playwright.config.ts').read_bytes()).hexdigest()==identity['config_sha256']
 for f,h in identity['source_file_sha256'].items():assert hashlib.sha256((p/'apps/desktop'/f).read_bytes()).hexdigest()==h;input_hashes[f]=h
m.assert_partition(source,selected)
def key(t):
 title=' › '.join(t['title_path']); extra=[tag for tag in t['tags'] if tag not in title.split()]
 return (t['project'],t['file'],int(t['line']),title + ((' ' + ' '.join(extra)) if extra else ''))
expected=Counter(key(t) for t in source);actual=[]
regex=re.compile(r'\s([✓×-])\s+\d+\s+\[(chromium-(?:desktop|compact))\] › (e2e/[^:]+):(\d+):\d+ › (.*)$')
for line in (d/'workflow.log').read_text().splitlines():
 z=regex.search(line)
 if not z:continue
 status,project,file,lineno,title=z.groups()
 title=re.sub(r' \([^()]*\)$','',title) if status!='-' else title
 actual.append({'key':(project,file,int(lineno),title),'outcome':'passed' if status=='✓' else 'skipped' if status=='-' else 'failed'})
observed=Counter(x['key'] for x in actual)
missing=list((expected-observed).elements());unexpected=list((observed-expected).elements());counts=Counter(x['outcome'] for x in actual)
result={'candidate':head,'workflow_run':36112629958,'attempt':1,'selected_mode':plan['mode'],'source_identities':len(source),'execution_identities':len(actual),'outcomes':dict(counts),'missing':missing,'unexpected_or_duplicate':unexpected,'source_specs_hashed':len(input_hashes),'projects':sorted({t['project'] for t in source}),'selection_is_not_pass':'Actual executed outcomes parsed independently from successful run log; every collected identity required once.','run_sha256':hashlib.sha256((d/'run.json').read_bytes()).hexdigest(),'log_sha256':hashlib.sha256((d/'workflow.log').read_bytes()).hexdigest()}
(d/'source-verified.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['missing','unexpected_or_duplicate']}))
if missing or unexpected:print('identity mismatches',{'missing':missing[:4],'unexpected':unexpected[:4]})
assert not missing and not unexpected and counts['failed']==0
binding={'workflow_path':'.github/workflows/piping-desktop-e2e.yml','run_id':36112629958,'run_attempt':1,'head_sha':head,'conclusion':'success','registered_e2e_specs_executed':True,'viewport_projects':['chromium-desktop','chromium-compact']}
(d/'surface4-ci-binding.json').write_text(json.dumps(binding,indent=2)+'\n')
