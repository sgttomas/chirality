# Dependency closure report — after the SCA-APP-011 incremental refresh

## Current production conclusion

**PASS, with isolate warnings**, for the 51 current production deliverables.

- **Analyzer result.** The registered analyzer reports COMPLETE/PASS:
  - 107 unique directed edges;
  - 0 strongly connected components;
  - 0 unresolved workspace targets (orphans);
  - 0 existing targets outside the scope;
  - 0 bidirectional pairs;
  - 0 hubs at degree 20.
- **Isolates.** Three, as before: DEL-01-01, DEL-10-04 and DEL-10-05. These
  are topology warnings, not missing target rows.
- **No new SCC.** There is nothing to route to `scc-resolution-case`.
- **No accepted project DAG.** `_DAG/_LATEST.md` is absent, so there is no
  `dag_pending` and no currency audit.

**The ALL census.** Over 54 units it reports subject FAIL, only because the
two CONTROL units DEL-00-01 and DEL-00-02 have no register by design (schema
BLOCKER and anchor WARNING). The graph is identical: 107 edges, 0 SCC. This
matches the accepted convention of the 2026-09-22 snapshot.

## What changed (`Evidence/edge_delta.csv`)

The comparison is against the pre-extraction basis `0ca5ffcca`. There are 111
edges before and 107 after.

| Change | Edge | Rows |
|---|---|---|
| Removed | DEL-02-01 → DEL-02-02 | DEP-02-01-007 (DX-06), DEP-02-02-005 (DX-01) |
| Removed | DEL-02-01 → DEL-08-03 | DEP-02-01-008 (DX-07; owner's HGD-2 ruling) |
| Removed | DEL-07-04 → DEL-02-02 | DEP-02-02-007 (DX-03) |
| Removed | DEL-07-05 → DEL-02-02 | DEP-02-02-008 (DX-04) |
| Removed | DEL-08-03 → DEL-02-02 | DEP-02-02-009 (DX-05) |
| Added | DEL-07-04 → DEL-06-03 | DEP-07-04-009 (named in text SCA-APP-011 added) |
| Rows changed | DEL-02-03 → DEL-02-02 | DEP-02-02-006 retired (DX-02); the edge remains through the held DEP-02-02-021 |

The analyzer's comparison deltas agree: graph_edges −4, scc_count 0, nodes
unchanged.

## Held edges (ESR-1)

Eight ACTIVE deliverable edges rest on evidence that the 2026-09-23 finite Task
Management account retired:
- DEP-02-02-021, DEP-07-01-010, DEP-02-01-014;
- DEP-02-04-015, 016;
- DEP-08-01-018, 019;
- DEP-08-04-013.

They are held for the owner's decision, which is proposed as ESR-1 in the run
record. Retiring them only removes edges, so the graph stays acyclic in either
case.

## Evidence

- `Evidence/` is the primary 51-unit run, and `Evidence/ALL/` is the census.
- `Tool_Run.json` records:
  - the analyzer SHA-256 and exact arguments;
  - every input register and index with its SHA-256;
  - that the inputs were stable during the run.
- Findings are in `Dependency_Closure_IssueLog.csv`.

## Pointer

`_Evaluation/DepClosure/_LATEST.md` is an observation pointer. It is moved
only when a brief sets `UPDATE_LATEST_POINTER=true`, and no brief did here.
The proposed move is to this snapshot, which supersedes
`CLOSURE_APP_RECORD_CLOSEOUT_2026-09-22_211905Z` as the latest observation. It
is left to the manager. The accepted `_Reconciliation/DepClosure/_LATEST.md` is
untouched.
