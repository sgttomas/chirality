"""Read one completed B result for TASK inspection; no model/guard execution."""
from pathlib import Path
import hashlib,json,sys
here=Path(__file__).resolve().parent
assert len(sys.argv) in [2,3]
cid=sys.argv[1]; case=here/'cases'/cid
r=json.loads((case/'CASE_RESULT.json').read_text())
comparison=json.loads((case/'COMPARISON.json').read_text()) if (case/'COMPARISON.json').exists() else {}
log=(case/'guard-workload.log').read_text() if (case/'guard-workload.log').exists() else ''
tags={'SELECTED','SCALE','FLOOR','FINAL_SUMMARY','THETA','CERTIFIED_BOUND','RESOLUTION','VERIFY_FLAGS','ATTEMPT','PUBLIC_RCM_ON_DERIVED_PATTERN','METER','STATUS','REFUSAL','UNRESOLVED','SOURCE_REFUSAL','STOP_RULE','ESTIMATE','CHARGE'}
facts=[line for line in log.splitlines() if line.split('\t')[0] in tags]
rows=[]
for row in comparison.get('comparisons',[]):
    rows.append({k:v for k,v in row.items() if k in ['key','row_class','outcome','truth','published','absolute_error','bound','claim_passes','range_agrees_with_exact_truth','relative_claim_published_passes','relative_truth_passes']})
compact=[[r['key'],r['outcome'],r['row_class'],r.get('claim_passes',r.get('range_agrees_with_exact_truth'))] for r in rows]
details=[r for r in rows if r.get('absolute_error',{}).get('n','0')!='0' or r['outcome']!='Value']
view=dict(case=cid,facts=facts,all_rows=compact,nonzero_error_or_range_details=details,limits=comparison.get('limits'),violations=comparison.get('violations'))
print(json.dumps(view,separators=(',',':')))
if len(sys.argv)==3:
    assert r['may_consider_next_B'] and not comparison.get('violations')
    review=dict(case=cid,actor='/root/design_manager/a1_diagnosis',advance_allowed=True,
        basis='TASK inspected case result, all row comparisons and limits, published scales/classes/bounds, attempt/verification summaries, guard completion and unchanged inputs before allowing next B case',
        note=sys.argv[2],case_result_sha256=hashlib.sha256((case/'CASE_RESULT.json').read_bytes()).hexdigest(),
        comparison_sha256=hashlib.sha256((case/'COMPARISON.json').read_bytes()).hexdigest())
    with open(case/'TASK_REVIEW.json','x') as f: json.dump(review,f,indent=2); f.write('\n')
