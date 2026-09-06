from pathlib import Path
import csv,json,hashlib
ROOT=Path(__file__).resolve().parents[6];OUT=Path(__file__).resolve().parent;P=ROOT/'projects/chirality-runtime/execution/_Coordination/SCA005_SCHEDULE_BASIS'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rows(p):return list(csv.DictReader(p.open()))
expected='3bffb22f758fbdc4a8eac44c7756cb77bea9fa070d6779a33581795322c81e4e'
m=P/'ARTIFACTS.sha256';assert sha(m)==expected
for line in m.read_text().splitlines():
 h,f=line.split(maxsplit=1);q=P/f
 if not q.exists():q=ROOT/f
 assert sha(q)==h
edges=rows(P/'ORDERING_EDGES.csv');approved=rows(ROOT/'execution/_ScopeChange/SCA-005_2026-09-06_GATE4_PLAN/DEPENDENCY_DISTRIBUTION.csv');assert {(x['Predecessor'],x['Consumer'],x['Class']) for x in edges}=={(x['Predecessor'],x['Consumer'],x['Class']) for x in approved}
streams=rows(P/'WORK_STREAMS.csv');assert len(streams)==8;assert all(x['CurrentRemainingEffort']=='UNKNOWN' and not x['CalendarDuration'] and not x['Staffing'] for x in streams)
assert all(x['Satisfaction']=='UNKNOWN_ACTUAL_ACCEPTED_EVIDENCE_REQUIRED' for x in edges)
vertices={x[k] for x in edges for k in ['Predecessor','Consumer']};preds={x['Predecessor'] for x in edges};cons={x['Consumer'] for x in edges};assert not preds&cons # two disjoint depth-one fans; proves no directed cycle
result={'seal':expected,'members_verified':len(m.read_text().splitlines()),'qualified_nodes':len(vertices),'edges':len(edges),'runtime_edges':sum(x['Scope']=='RUNTIME' for x in edges),'governance_edges':sum(x['Scope']=='ROOT_GOVERNANCE' for x in edges),'cycles':0,'streams':len(streams),'historical_base_sum':sum(int(x['HistoricalBaseHours']) for x in streams),'remaining_effort':'UNKNOWN','owner_acceptance':'PENDING_NEW_DERIVATIVE','verdict':'PASS_MAPPING_ONLY','pricing_audit':'NOT_PERFORMED_OUT_OF_SCOPE'}
(OUT/'Ordering_Backcheck.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
