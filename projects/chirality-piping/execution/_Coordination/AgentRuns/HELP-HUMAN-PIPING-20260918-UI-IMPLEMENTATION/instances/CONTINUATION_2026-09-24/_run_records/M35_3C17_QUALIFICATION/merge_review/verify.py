"""Read-only review of the two-path M35 post-merge record delta."""
from pathlib import Path
import datetime, hashlib, json, re, subprocess

R=Path('/Users/ryan/.codex/worktrees/6614/chirality')
OUT=Path(__file__).resolve().parent
BASE='e604139a089d2cee3f56ad1da12652d9ec97ad6c'
CHECKED='3c17e267dd06ee561e8dc9984f6623126095eec1'
MERGED='7e7d37b5fdeac698b425446d01259dc6609c14e3'
G='projects/chirality-piping/execution/_Coordination/WorkGraphs/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/WORK_GRAPH.md'
C='projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/'
M=C+'_run_records/M35_3C17_QUALIFICATION/MERGED_STATE.json'
git=lambda *a:subprocess.check_output(['git','-C',str(R),*a])
sha=lambda b:hashlib.sha256(b).hexdigest()
blob=lambda rev,p:git('show',rev+':'+p)
before=blob(BASE,G).decode();after=(R/G).read_text();merged=json.loads((R/M).read_text())
patch=git('diff',BASE,'--',G)
(OUT/'WORK_GRAPH.reviewed.patch').write_bytes(patch)
assert git('rev-parse','HEAD').decode().strip()==BASE
assert merged['headRefOid']==CHECKED and merged['mergeCommit']['oid']==MERGED and merged['state']=='MERGED'
assert merged['url']=='https://github.com/sgttomas/chirality/pull/892'
parents=git('show','-s','--format=%P',MERGED).decode().strip().split()
assert CHECKED in parents and len(parents)==2
commit_epoch=int(git('show','-s','--format=%ct',MERGED).decode())
merged_epoch=int(datetime.datetime.fromisoformat(merged['mergedAt'].replace('Z','+00:00')).timestamp())
assert commit_epoch==merged_epoch
assert git('rev-parse','origin/main').decode().strip()==MERGED
extra=git('diff','--name-only',CHECKED,MERGED).decode().splitlines()
assert extra and all(p.startswith('projects/pec/') for p in extra)
assert not git('diff','--name-only',CHECKED,MERGED,'--','projects/chirality-piping').decode()
assert subprocess.run(['git','-C',str(R),'merge-base','--is-ancestor','f702b439536c6e76af8e1c81ee536d5685e87907',MERGED]).returncode==0

def table(text):
    rows={}
    for line in text.splitlines():
        match=re.match(r'^\| (M\d{2}) \| (.*?) \| (.*?) \|$',line)
        if match:rows[match[1]]={'outcome':match[2],'state':match[3]}
    return rows
old,new=table(before),table(after)
assert len(old)==len(new)==38 and set(old)==set(new)=={f'M{i:02}' for i in range(1,39)}
old_closed=sorted(k for k,v in old.items() if v['state'].startswith('COMPLETE'))
new_closed=sorted(k for k,v in new.items() if v['state'].startswith('COMPLETE'))
assert old_closed==['M04','M09','M24'] and new_closed==['M04','M09','M24','M35']
assert [k for k in old if old[k]!=new[k]]==['M35']
assert 'current closure count is4of38 original finding groups (M04/M09/M24/M35), with34open' in after
historical='## Implementation checkpoint after PR886 (superseded in priority below)'
section=lambda t:t.split(historical,1)[1].split('## Current priority: solver findings first',1)[0]
assert section(before)==section(after)
assert 'M04/M09/M24 are complete;35groups remain open' in section(after)
assert after.count('single CLOSE→RECORD→FINAL boundary')==before.count('single CLOSE→RECORD→FINAL boundary')
assert after.endswith('Actual-human live witnesses, later engineering validation and release remain distinct.\n')
assert 'no M35 group closure yet' not in after.split('### Current solver integration checkpoint',1)[1]
assert 'General mass modelling, the separately found section-density authoring omission and actual-human live witnesses remain open.' in after

assessment=C+'SOLVER_FINDINGS_ASSESSMENT/ASSESSMENT.md'
assessment_text=(R/assessment).read_text()
assessment_row=next(x for x in assessment_text.splitlines() if x.startswith('| M-35 '))
assert 'moment direction mismatch' in assessment_row and 'stale' in assessment_row and 'dependency-aware stale detection/regeneration' in assessment_row
qualification=C+'_run_records/M35_3C17_QUALIFICATION/RETURN.md'
qual=(R/qualification).read_bytes();assert qual==blob(BASE,qualification)
ready=C+'_run_records/M35_3C17_QUALIFICATION/review/RETURN.md'
ready_bytes=blob(BASE,ready)
assert b'READY for ROOT to merge' in ready_bytes and CHECKED.encode() in ready_bytes
assert '495 identities:475 passed,20 explicit existing skips' in qual.decode()
scope=[G,M]
full_status=git('status','--porcelain').decode()
record={'reviewer':'/root/m35_integration_review','parent':'/root','role':'TASK','time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'base':BASE,'scope':scope,'graph_before_sha256':sha(before.encode()),'graph_after_sha256':sha(after.encode()),'graph_diff_sha256':sha(patch),
 'merged_state_sha256':sha((R/M).read_bytes()),'merged_state':merged,'actual_merge_parents':parents,'commit_epoch_matches_merged_at':True,
 'origin_main':MERGED,'checked_to_merged_other_paths':extra,'checked_to_merged_piping_delta_empty':True,
 'finding_rows':len(new),'previous_complete':old_closed,'current_complete':new_closed,'remaining_original_groups':38-len(new_closed),
 'only_table_state_change':'M35','historical_checkpoint_byte_identical':True,'original_assessment_m35':assessment_row,
 'qualified_before_actual_merge':True,'broader_graph_complete':False,
 'remote_dependency_checkpoints':git('for-each-ref','--format=%(refname) %(objectname)','refs/remotes/origin/codex/piping-numerical-corrections-20260924','refs/remotes/origin/codex/piping-pressure-stress-20260924').decode(),
 'current_primary_status_excluded_from_review':full_status,
 'read_basis':[{'path':p,'sha256':sha((R/p).read_bytes())} for p in ['AGENTS.md','agents/AGENT_TASK.md','projects/chirality-piping/AGENTS.md','projects/chirality-piping/loop/LOOP_INIT.md','.agents/skills/software-code-review/SKILL.md',assessment,C+'SOLVER_FINDINGS_ASSESSMENT/_run_records/loads/RETURN.md',qualification]],
 'limits':'Complete scoped graph diff plus new merged-state JSON reviewed. Existing source/qualification reviews carried; no fresh source review, suites, native actions, remote calls, source/graph/Git edits, or delegation. Other live primary writes remain excluded.'}
(OUT/'HASHES.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'scope_paths':len(scope),'rows':len(new),'complete':new_closed,'open':record['remaining_original_groups'],
 'historical_unchanged':True,'merge':MERGED,'merge_extra_paths':len(extra),'piping_delta_empty':True},indent=2))
