# Brief

## Verbatim basis

`project-setup` INCREMENTAL, Phase 5.6 (FULL_GRAPH): "run `audit-dep-closure` over the accepted inventory (its `SCOPE: ALL` rules, with retired exemptions)". The rerun follows independent review of `0ca5ffcca..1d5909491`: "Rerun dependency closure and scope closure if any row changed." Rows changed in place (ESR-1 re-evidence of eight rows; DEP-08-02-003 `TargetName`); no edge changed.

## Normalized

```
EXECUTION_ROOT: projects/chirality-app-dev/execution
SCOPE: ALL rules; inventory = the 54 PKG-*/1_Working/DEL-* folders
EXEMPT_UNITS: DEL-00-01 CONTROL; DEL-00-02 CONTROL; DEL-09-07 RETIRED (authorities as in CLOSURE_SCA_APP_011_POST_EXTRACTION_2026-09-27_1656/Brief.md)
SCOPE_UNITS: the 51 non-exempt units (primary, Evidence/); ALL as a census (Evidence/ALL/)
RUN_LABEL: SCA_APP_011_ESR1_REEVIDENCE
UPDATE_LATEST_POINTER: false
FILTER_ACTIVE_ONLY: true; NORMALIZE_IDS: true; EDGE_FILTER: EXECUTION / DELIVERABLE; HUB_THRESHOLD: 20; MAX_CYCLES: 10000; INCLUDE_DECLARED: true
PRIOR_SUMMARY: CLOSURE_SCA_APP_011_POST_EXTRACTION_2026-09-27_1656 (Evidence/ and Evidence/ALL/)
RERUN: python3 projects/chirality-app-dev/execution/_Evaluation/DepClosure/CLOSURE_SCA_APP_011_ESR1_REEVIDENCE_2026-09-27_1725/closure_run.py
```
