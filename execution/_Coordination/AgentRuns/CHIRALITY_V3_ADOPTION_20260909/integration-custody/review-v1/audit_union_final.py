import hashlib,json,re,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[6]
# Parent depth anchored explicitly to recorded checkout; never select another tree.
ROOT=Path('/private/tmp/chirality-v3-adoption-20260909')
R='execution/_Coordination/AgentRuns/CHIRALITY_V3_ADOPTION_20260909/'
A='projects/chirality-app-dev/'
AR=A+'execution/_Coordination/AgentRuns/CHIRALITY_V3_APP_ADOPTION_20260909/'
T='projects/chirality-runtime/execution/_Coordination/AgentRuns/CHIRALITY_V3_ADOPTION_20260909/MANAGER/'
out=ROOT/R/'integration-custody/review-v1'
sha=lambda p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
subjects=[];union={};overlays=[]
def add(subject,items,prefix=''):
 subjects.append({'path':subject,'sha256':sha(subject),'count':len(items)})
 for v in items:
  p=prefix+v['path'];h=v['sha256'];old=union.get(p)
  if old:overlays.append({'path':p,'priorSubject':old['subject'],'newSubject':subject,'identical':old['sha256']==h})
  union[p]={'path':p,'sha256':h,'subject':subject}
def j(p,k):return json.loads((ROOT/p).read_text())[k]
def lines(p):return [{'sha256':m[0],'path':m[1]} for m in re.findall(r'^([a-f0-9]{64})  (.+)$',(ROOT/p).read_text(),re.M)]
add(R+'ROOT_SCOPE_FREEZE_V7.json',j(R+'ROOT_SCOPE_FREEZE_V7.json','files'))
add(R+'ROOT_SEMANTIC_SUCCESSOR_V1.json',j(R+'ROOT_SEMANTIC_SUCCESSOR_V1.json','files'))
add(T+'SOURCE_FREEZE.json',j(T+'SOURCE_FREEZE.json','members'))
add(R+'runtime-context-review-v2/APP_SUBJECT.sha256',lines(R+'runtime-context-review-v2/APP_SUBJECT.sha256'),A+'frontend/')
add(R+'runtime-context-review-v2/supplement-v1/SUBJECT.json',j(R+'runtime-context-review-v2/supplement-v1/SUBJECT.json','files'))
add(T+'SOURCE_FREEZE_V5.json',j(T+'SOURCE_FREEZE_V5.json','members')+j(T+'SOURCE_FREEZE_V5.json','sharedFixtures'))
add(AR+'UI_SOURCE_FREEZE_v7.md',lines(AR+'UI_SOURCE_FREEZE_v7.md'),A)
add(AR+'CORPUS_V21_FREEZE_v2.md',lines(AR+'CORPUS_V21_FREEZE_v2.md'),A)
add(AR+'CORPUS_V21_REFERENCE_MANIFEST.sha256',lines(AR+'CORPUS_V21_REFERENCE_MANIFEST.sha256'),A)
add(R+'distribution/subject-v12.json',j(R+'distribution/subject-v12.json','members'))
# Explicit two-file independent supplemental subject.
supp=AR+'astra-second-pass-review/review-supplemental-two-files-v1/MANIFEST.json'
d=json.loads((ROOT/supp).read_text())
print('SUPPLEMENT KEYS',d.keys())
# Use exact supplemental manager identities, each crosschecked later to independent manifest.
add(AR+'CUSTODY_SUPPLEMENT_TWO_FILES_v1.md',[
 {'path':A+'execution/_Reconciliation/References/test_reconcile_authority_corpus.py','sha256':'d554422d5a221964e3279073aae6fef301516e1ebac360329415bcea3cda5ab1'},
 {'path':A+'frontend/src/__tests__/components/woven-dialogue-shell.test.tsx','sha256':'ac8f3938a45995c6a647bc16af28ab799b08f20b36607acbe1a3cbd3937021d0'}])
add(T+'SOURCE_FREEZE_V6.json',j(T+'SOURCE_FREEZE_V6.json','members')+j(T+'SOURCE_FREEZE_V6.json','sharedFixtures'))
add(AR+'astra-second-pass-review/review-supplemental-app-governance-v1/MANIFEST.json',j(AR+'astra-second-pass-review/review-supplemental-app-governance-v1/MANIFEST.json','subjects'))
changed=set(subprocess.check_output(['git','diff','--name-only','c16812685831a1cae3d44bf478d08b033c605c3a'],cwd=ROOT,text=True).splitlines())
changed.update(subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=ROOT,text=True).splitlines())
def evidence(p):return '/AgentRuns/' in p or p.startswith(R)
def product(p):return not evidence(p)
missing=sorted(p for p in changed if product(p) and p not in union)
drift=[dict(v,actual=sha(p) if (ROOT/p).exists() else None) for p,v in union.items() if not (ROOT/p).exists() or sha(p)!=v['sha256']]
report={'base':'c16812685831a1cae3d44bf478d08b033c605c3a','subjects':subjects,'sourceUnion':sorted(union.values(),key=lambda x:x['path']),'overlays':overlays,'drift':drift,'changedCount':len(changed),'changedOutsideAgentRunCount':sum(product(p) for p in changed),'missingOutsideAgentRuns':missing,'unchangedUnionPaths':sorted(set(union)-changed),'instructionContext':[{'path':p,'sha256':sha(p)} for p in ['AGENTS.md','agents/AGENT_TASK.md']]}
(out/'UNION_CHECK_FINAL.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ['sourceUnion','overlays','subjects']},indent=2));print('UNION',len(union))
