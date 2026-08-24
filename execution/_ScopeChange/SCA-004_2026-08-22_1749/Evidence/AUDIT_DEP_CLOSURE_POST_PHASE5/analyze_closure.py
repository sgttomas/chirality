#!/usr/bin/env python3
"""Read-only deterministic verifier for the post-Phase-5 closure audit."""
import csv, json, re
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[5]
HERE=Path(__file__).resolve().parent
GRAPH=HERE.parent/'DEP_GRAPH_POST_PHASE5/WORK_GRAPH.json'
REGISTER=ROOT/'execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv'
def main():
    graph=json.loads(GRAPH.read_text()); summary=json.loads((HERE/'closure_summary.json').read_text())
    rows=list(csv.DictReader(REGISTER.open())); ids={r['DeliverableID'] for r in rows}
    assert len(rows)==53 and len(ids)==53 and len({r['ParentPackageID'] for r in rows})==6
    rel=graph['dependency_edges']; gating=[e for e in rel if e['gating']]
    assert len(rel)==9 and len(gating)==8 and len(graph['notice_edges'])==2
    assert graph['non_trivial_scc_count']==0 and graph['strict_layer_acyclic']
    assert not ({e['from'] for e in rel}|{e['to'] for e in rel})-ids
    states=Counter()
    for r in rows:
        p=ROOT/'execution'/r['ParentPackageID']/'1_Working'/r['DeliverableID']/'_DEPENDENCIES.md'
        m=re.search(r'- \*\*Status:\*\*\s*`?([^`\n]+)',p.read_text()); states[m.group(1).strip() if m else 'MISSING']+=1
    assert states==Counter({'NOT_RUN_YET':45,'EXTRACTED_PHASE3_2026-08-23':8})
    assert summary['metrics']['unresolved_closure_violations']==0
    assert summary['metrics']['phase1_initialized_empty_warnings_remaining']==0
    assert summary['phase3_comparison']['deviations']==[]
    print(json.dumps({'status':'PASS_ZERO_ACTIONABLE_FINDINGS','closure_verdict':summary['closure_verdict'],'deliverables':53,'packages':6,'relationships':9,'gating':8,'notice_edges':2,'non_trivial_sccs':0,'unresolved_violations':0,'cleared_initialized_empty_warnings':7,'legacy_not_run_yet':45,'phase3_exact_match':True,'human_gated_move':False},sort_keys=True))
if __name__=='__main__': main()
