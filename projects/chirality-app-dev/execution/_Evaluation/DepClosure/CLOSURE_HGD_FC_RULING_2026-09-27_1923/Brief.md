# Brief

## Verbatim basis

`dependency-extract` UPDATE on DEL-02-01 applied the owner's ruling, typed in chat on 2026-09-27: "HGD-1: invert DEP-02-01-006 to UPSTREAM INTERFACE; HGD-3: close without emitting; FC-1: resolve DEP-02-01-012 to DEL-05-03; FC-2 and FC-3: close without emitting." It is transcribed in `execution/_Coordination/AgentRuns/APP-HGD-1-3-RECOMMENDATION-2026-09-27/CHAT_TRANSCRIPTION_HGD_2026-09-27.md`. The coordinating session then directed a fresh `audit-dep-closure` run with `UPDATE_LATEST_POINTER=false`.

## Normalized

```
EXECUTION_ROOT: projects/chirality-app-dev/execution
SCOPE: ALL rules; inventory = the 54 PKG-*/1_Working/DEL-* folders
EXEMPT_UNITS: DEL-00-01 CONTROL; DEL-00-02 CONTROL; DEL-09-07 RETIRED (as in CLOSURE_SCA_APP_011_ESR1_RULING_2026-09-27_1739/Brief.md)
SCOPE_UNITS: the 51 non-exempt units (primary, Evidence/); ALL as a census (Evidence/ALL/)
RUN_LABEL: HGD_FC_RULING
UPDATE_LATEST_POINTER: false
FILTER_ACTIVE_ONLY: true; NORMALIZE_IDS: true; EDGE_FILTER: EXECUTION / DELIVERABLE; HUB_THRESHOLD: 20; MAX_CYCLES: 10000; INCLUDE_DECLARED: true
PRIOR_SUMMARY: CLOSURE_SCA_APP_011_ESR1_RULING_2026-09-27_1739 (Evidence/ and Evidence/ALL/)
EDGE_DELTA_BASIS: adc8bdae1 (origin/main before the ruling was applied; its registers hash-match the 1739 inputs)
RERUN: python3 projects/chirality-app-dev/execution/_Evaluation/DepClosure/CLOSURE_HGD_FC_RULING_2026-09-27_1923/closure_run.py
```
