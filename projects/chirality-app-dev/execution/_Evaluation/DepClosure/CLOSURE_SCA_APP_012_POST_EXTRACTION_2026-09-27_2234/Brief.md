# Brief

## Verbatim basis

`project-setup` INCREMENTAL, Phase 5.6 (FULL_GRAPH): "dispatch `dependency-extract` for the same deliverables as above, then run `audit-dep-closure` over the accepted inventory (its `SCOPE: ALL` rules, with retired exemptions): a new cycle through a changed edge can pass through unaffected deliverables. The audit reads existing registers; it does not re-extract them. Route new SCCs to `scc-resolution-case`."

The owner confirmed the SCA-APP-012 incremental plan on 2026-09-27 (`execution/_Coordination/AgentRuns/APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION.md`).

## Normalized

```
EXECUTION_ROOT: projects/chirality-app-dev/execution
SCOPE: ALL rules; inventory = the 54 PKG-*/1_Working/DEL-* folders
EXEMPT_UNITS: DEL-00-01 CONTROL; DEL-00-02 CONTROL; DEL-09-07 RETIRED (as in CLOSURE_HGD_FC_RULING_2026-09-27_1923/Brief.md)
SCOPE_UNITS: the 51 non-exempt units (primary, Evidence/); ALL as a census (Evidence/ALL/)
RUN_LABEL: SCA_APP_012_POST_EXTRACTION
REQUESTED_BY: WORKING_ITEMS (workflow: project-setup), run APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27
UPDATE_LATEST_POINTER: false (no brief sets it)
FILTER_ACTIVE_ONLY: true; NORMALIZE_IDS: true; EDGE_FILTER: EXECUTION / DELIVERABLE; HUB_THRESHOLD: 20; MAX_CYCLES: 10000; INCLUDE_DECLARED: true
PRIOR_SUMMARY: CLOSURE_HGD_FC_RULING_2026-09-27_1923 (Evidence/ and Evidence/ALL/), the latest snapshot
EDGE_DELTA_BASIS: 63e5de1f2 (the extraction's basis; its registers hash-match the 1923 inputs)
RERUN: python3 projects/chirality-app-dev/execution/_Evaluation/DepClosure/CLOSURE_SCA_APP_012_POST_EXTRACTION_2026-09-27_2234/closure_run.py
```
