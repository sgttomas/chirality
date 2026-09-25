"""Actual-candidate retained evidence audit. No tests/build/network/native execution."""
from pathlib import Path
from collections import Counter
import json,hashlib,re,subprocess,datetime
PRIMARY=Path('/Users/ryan/.codex/worktrees/6614/chirality')
REPO=Path('/private/tmp/piping-scientific-json-integration-20260925')
C=Path('projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24')
D=PRIMARY/C/'_run_records/SCIENTIFIC_JSON_INTEGRATION';OUT=D/'readiness_review'
H='98b423d93e41338551bf744def1e2c5a303aeaab';BASE='eec2855d829d9cd3704892fc7d603562fbd39b88';UP='8b6553850aa8a98cb44aed02e9fe91e23b1234bd'
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def git(*args):return subprocess.check_output(['git',*args],cwd=REPO)
def blob(rev,path):return git('show',rev+':'+path)
assert git('rev-parse','HEAD').decode().strip()==H
assert not git('status','--porcelain').strip()
custody=read(D/'CUSTODY.json');assert custody['candidate']==H
for record in custody['files']:
 p=D/record['path'];assert sha(p)==record['sha256'],str(p);assert p.stat().st_size==record['bytes']
context=read(D/'integration_review/CHECKED_MANIFEST.json');oldpath=context['portability_delta']['old_path'];newpath=context['portability_delta']['new_path']
oldhead=context['candidate'];prior=context['original_reviewed_commit'];changed=set(git('diff','--name-only',BASE,H).decode().splitlines());assert len(changed)==72
reviewed=set(r['path'] for r in context['files']);assert changed==(reviewed-{oldpath})|{newpath}
for row in context['files']:
 p=row['path'];assert hashlib.sha256(blob(oldhead,p)).hexdigest()==row['sha256'];assert blob(oldhead,p)==blob(prior,p)
 if p.endswith('/HANDOFF_WHITELIST.json'):assert hashlib.sha256(blob(H,p)).hexdigest()==context['portability_delta']['whitelist_final_sha256']
 elif p==oldpath:assert hashlib.sha256(blob(H,newpath)).hexdigest()==row['sha256']==context['portability_delta']['raw_sha256']
 else:assert blob(H,p)==blob(oldhead,p)
foundation=REPO/C/'SCIENTIFIC_TRANSPORT_FOUNDATION'
final=read(foundation/'INDEPENDENT_REVIEW/FINAL_CHECKED_BASIS.json')
assert final['finding_status']=={'SJ-R1':'resolved','SJ-R2':'resolved including pointer-budget parity'}
for r in final['source']:assert sha(REPO/r['path'])==r['sha256']
assert len(final['source'])==10
# Verify narrow commit has exactly the reviewed rename and whitelist edit.
delta=git('diff','--name-status','-M',oldhead,H).decode().splitlines();assert len(delta)==2 and any(x.startswith('R100\t'+oldpath+'\t'+newpath) for x in delta)
whitelist=next(r['path'] for r in context['files'] if r['path'].endswith('/HANDOFF_WHITELIST.json'))
assert blob(oldhead,whitelist).decode().replace('INDEPENDENT_REVIEW/INTERMEDIATE_REPAIR_CHECKS.json','INDEPENDENT_REVIEW/_run_records/INTERMEDIATE_REPAIR_CHECKS.json')==blob(H,whitelist).decode()
for r in context['current_context']:assert sha(REPO/r['path'])==r['sha256']
upstream=git('diff','--name-only',BASE,UP).decode().splitlines();assert len(upstream)==7 and all(p.startswith('projects/pec/') for p in upstream)
# Raw source collection is only the denominator; outcomes must come from actual log.
raw=read(D/'ci/barrier/source.stdout.json');assert not raw['errors'];source=[]
def collect(suite,titles):
 for spec in suite.get('specs',[]):
  for test in spec['tests']:source.append({'id':spec['id'],'file':'e2e/'+spec['file'],'line':spec['line'],'project':test['projectName'],'title_path':titles+[spec['title']],'tags':['@'+t.lstrip('@') for t in spec.get('tags',[])]})
 for child in suite.get('suites',[]):collect(child,titles+[child['title']] if child.get('line',0) else titles)
collect(raw,[]);assert len(source)==495
selected=[];spec_hashes={}
for folder in ['barrier','shard-1','shard-2','shard-3','shard-4']:
 r=read(D/'ci'/folder/'collection.json');assert r['status']=='validated' and r['head']==H and r['mode']=='full'
 selected+=r['execution_tests'];identity=r['identity'];assert sha(REPO/'projects/chirality-piping/apps/desktop/playwright.config.ts')==identity['config_sha256']
 for file,h in identity['source_file_sha256'].items():assert sha(REPO/'projects/chirality-piping/apps/desktop'/file)==h;spec_hashes[file]=h
assert Counter(t['id'] for t in source)==Counter(t['id'] for t in selected);assert len(spec_hashes)==16
# Existing source specs are byte-identical to base, including skip controls.
for file in spec_hashes:assert blob(H,'projects/chirality-piping/apps/desktop/'+file)==blob(BASE,'projects/chirality-piping/apps/desktop/'+file)
def key(t):
 title=' › '.join(t['title_path']);extra=[tag for tag in t['tags'] if tag not in title.split()]
 return (t['project'],t['file'],int(t['line']),title+(' '+' '.join(extra) if extra else ''))
expected=Counter(key(t) for t in source);actual=[]
pattern=re.compile(r'\s([✓×-])\s+\d+\s+\[(chromium-(?:desktop|compact))\] › (e2e/[^:]+):(\d+):\d+ › (.*)$')
for line in (D/'ci/workflow.log').read_text().splitlines():
 m=pattern.search(line)
 if not m:continue
 status,project,file,line_number,title=m.groups()
 if status!='-':title=re.sub(r' \([^()]*\)$','',title)
 actual.append(((project,file,int(line_number),title),{'✓':'passed','×':'failed','-':'skipped'}[status]))
assert Counter(k for k,s in actual)==expected
counts=Counter(s for k,s in actual);assert counts==Counter(passed=475,skipped=20)
# Required hosted jobs bind exact head, not old 0a271 evidence.
ci=read(D/'ci/run.json');assert ci['headSha']==H and ci['status']=='completed' and ci['conclusion']=='success';assert all(j['conclusion']=='success' for j in ci['jobs'])
pr=read(D/'ci/pr-final.json');assert pr['headRefOid']==H and pr['baseRefOid']==BASE;assert all(c['conclusion'] in ['SUCCESS','SKIPPED'] and c['status']=='COMPLETED' for c in pr['statusCheckRollup'])
for required in ['harness','Harness pre-merge','pec','Desktop E2E (source mode)','Numerical cargo suite']:
 assert any(c['name']==required and c['conclusion']=='SUCCESS' for c in pr['statusCheckRollup'])
gov=read(D/'ci/governance-run.json');assert gov['headSha']==H and gov['conclusion']=='success'
assert read(D/'ci/prior-governance-failure.json')['headSha']==oldhead and read(D/'ci/prior-governance-failure.json')['conclusion']=='failure'
assert read(D/'ci/prior-source-cancelled.json')['headSha']==oldhead and read(D/'ci/prior-source-cancelled.json')['conclusion']=='cancelled'
# Numerical command inventory distinguishes fetch from test and validates every byte.
n=read(D/'ci/numerical/numerical.json');assert n['head']==H and n['status']=='success' and n['exit_code']==0;assert len(n['manifests'])==38 and len(n['commands'])==78
for path,h in n['input_sha256'].items():assert sha(REPO/'projects/chirality-piping'/path)==h
assert len(n['input_sha256'])==76
tests=[];fetch=[];numeric=Counter()
for c in n['commands']:
 p=D/'ci/numerical'/c['output'];assert sha(p)==c['output_sha256'] and c['exit_code']==0
 if c['argv'][:2]==['cargo','fetch']:fetch.append(c)
 if c['argv'][:2]==['cargo','test']:
  tests.append(c);assert '--offline' in c['argv'] and '--locked' in c['argv']
  for passed,failed,ignored in re.findall(r'test result: ok\. (\d+) passed; (\d+) failed; (\d+) ignored;',p.read_text()):numeric.update(passed=int(passed),failed=int(failed),ignored=int(ignored))
assert len(tests)==len(fetch)==38 and numeric==Counter(passed=1154,failed=0,ignored=0)
# Five-surface clean candidate and raw local counts.
sweep=read(D/'local/sweep/SWEEP_20260925T084637Z_98b423d93e41.json');assert sweep['git']['commit_hash']==H and not sweep['git']['working_tree_dirty'] and not sweep['git']['status_capture_failed'];assert sweep['overall_status']=='pass' and len(sweep['surfaces'])==5
for surface in sweep['surfaces']:assert surface['status']=='pass' and all(c['exit_code']==0 for c in surface['commands'])
assert sweep['surfaces'][3]['ci_binding']==read(D/'ci/surface4-ci-binding.json')
local=(D/'local/sweep.log').read_text();rust=Counter()
for passed,failed,ignored in re.findall(r'test result: ok\. (\d+) passed; (\d+) failed; (\d+) ignored;',local):rust.update(passed=int(passed),failed=int(failed),ignored=int(ignored))
assert rust==Counter(passed=1154,failed=0,ignored=0)
assert '1200 passed, 304 warnings, 18 subtests passed' in local and re.search(r'Test Files\s+104 passed',local) and re.search(r'Tests\s+1675 passed',local)
assert read(D/'local/sweep-result.json')['exit_code']==0 and read(D/'local/sweep-result.json')['initial_status']==''
assert '379 passed' in (D/'local/practitioner-tests.log').read_text()
selfcheck=read(D/'local/self-check-working.json');assert not any(f.get('severity')=='BLOCK' for f in selfcheck['findings']);assert not any('ABS_PATH_IN_UNCLASSIFIED_SURFACE' in str(f) for f in selfcheck['findings'])
assert 'BLOCK' not in '\n'.join(l for l in (D/'local/g4.log').read_text().splitlines() if l.strip().startswith('BLOCK:'))
result={'status':'CLEAR','candidate':H,'clean_candidate':True,'tested_base':BASE,'upstream':UP,'upstream_only_pec_paths':upstream,'custody_records_verified':len(custody['files']),'source_review':{'ten_source_hashes_match':True,'complete_72_path_foundation_blobs_match_prior_review':True,'only_later_delta':'byte-identical evidence move plus sole whitelist path update','integration_review_covers_delta':True},'hosted':{'run':ci['url'],'head':H,'source_denominator':len(source),'source_identities_accounted':len(actual),'outcomes':dict(counts),'source_specs':len(spec_hashes),'viewports':sorted({r['project'] for r in source}),'all_required_recorded_checks_success':True,'unchanged_source_skips':20,'governance_actual_head':gov},'numerical':{'locked_crates':len(tests),'fetch_commands':len(fetch),'command_logs_hashed':len(n['commands']),'input_hashes_verified':len(n['input_sha256']),'counts':dict(numeric)},'local':{'clean_DEC025_surfaces':5,'rust':dict(rust),'python_passed':1200,'python_subtests':18,'desktop_passed':1675,'desktop_files':104,'production_build':True,'practitioner_passed':379,'selfcheck_no_portability_or_block_findings':True,'G4_no_block_lines':True},'history_preserved':{'prior_governance_failure':True,'prior_source_cancelled':True,'source_verifier_corrections_present':all((D/'ci'/p).exists() for p in ['source-verified-before-inline-tag-handling.json','source-verified-before-tag-display.json'])},'limits':['No source review repeated or solver accuracy claimed','No new native application path/adoption/witness','No network/current remote status query; Root owns final Git/PR state check','Original24Rust/55Python547token foundation evidence retains its original scope; fresh current-main counts used above']}
(OUT/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT/'UPSTREAM_PATHS.json').write_text(json.dumps(upstream,indent=2)+'\n')
print(json.dumps(result,indent=2))
