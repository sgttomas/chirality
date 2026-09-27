# Brief

## Verbatim basis

`project-setup` INCREMENTAL, Phase 5.6 (FULL_GRAPH): "run `audit-dep-closure` over the accepted inventory (its `SCOPE: ALL` rules, with retired exemptions)". This rerun rebinds the closure evidence after the independent review fix N2 (`ed2afdd37`), following the SCA-APP-011 precedent `d08b589ea` ("rebind closure evidence"). N2 reworded only the EVQ-006 note line in the DEL-05-03 and DEL-06-01 `_DEPENDENCIES.md` indexes; no register row, count or edge changed.

## Normalized

```
EXECUTION_ROOT: projects/chirality-app-dev/execution
SCOPE: ALL rules; inventory = the 54 PKG-*/1_Working/DEL-* folders
EXEMPT_UNITS: DEL-00-01 CONTROL; DEL-00-02 CONTROL; DEL-09-07 RETIRED (as in CLOSURE_SCA_APP_012_POST_EXTRACTION_2026-09-27_2234/Brief.md)
SCOPE_UNITS: the 51 non-exempt units (primary, Evidence/); ALL as a census (Evidence/ALL/)
RUN_LABEL: SCA_APP_012_REBIND
REQUESTED_BY: WORKING_ITEMS, run APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27 (review follow-up)
UPDATE_LATEST_POINTER: false (no brief sets it)
FILTER_ACTIVE_ONLY: true; NORMALIZE_IDS: true; EDGE_FILTER: EXECUTION / DELIVERABLE; HUB_THRESHOLD: 20; MAX_CYCLES: 10000; INCLUDE_DECLARED: true
PRIOR_SUMMARY: CLOSURE_SCA_APP_012_POST_EXTRACTION_2026-09-27_2234 (Evidence/ and Evidence/ALL/)
EDGE_DELTA_BASIS: 63e5de1f2 (the extraction's basis, as in 2234)
RERUN: python3 projects/chirality-app-dev/execution/_Evaluation/DepClosure/CLOSURE_SCA_APP_012_REBIND_2026-09-27_2311/closure_run.py
```
