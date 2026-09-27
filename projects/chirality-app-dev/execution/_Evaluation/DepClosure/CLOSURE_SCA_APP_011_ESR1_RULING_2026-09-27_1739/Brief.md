# Brief

## Verbatim basis

`project-setup` INCREMENTAL, Phase 5.6 (FULL_GRAPH): "run `audit-dep-closure` over the accepted inventory (its `SCOPE: ALL` rules, with retired exemptions)". Rerun after the owner's ruling in chat on 2026-09-27: "ESR-1: retire DEP-02-02-021, DEP-02-04-015, DEP-02-04-016 and DEP-02-01-014." (transcription `execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION_ESR-1_2026-09-27.md`).

## Normalized

```
EXECUTION_ROOT: projects/chirality-app-dev/execution
SCOPE: ALL rules; inventory = the 54 PKG-*/1_Working/DEL-* folders
EXEMPT_UNITS: DEL-00-01 CONTROL; DEL-00-02 CONTROL; DEL-09-07 RETIRED (authorities as in CLOSURE_SCA_APP_011_POST_EXTRACTION_2026-09-27_1656/Brief.md)
SCOPE_UNITS: the 51 non-exempt units (primary, Evidence/); ALL as a census (Evidence/ALL/)
RUN_LABEL: SCA_APP_011_ESR1_RULING
UPDATE_LATEST_POINTER: false
FILTER_ACTIVE_ONLY: true; NORMALIZE_IDS: true; EDGE_FILTER: EXECUTION / DELIVERABLE; HUB_THRESHOLD: 20; MAX_CYCLES: 10000; INCLUDE_DECLARED: true
PRIOR_SUMMARY: CLOSURE_SCA_APP_011_ESR1_REEVIDENCE_2026-09-27_1725 (Evidence/ and Evidence/ALL/)
EDGE_DELTA_BASES: 1485271da (1725's register basis); 0ca5ffcca (pre-extraction)
RERUN: python3 projects/chirality-app-dev/execution/_Evaluation/DepClosure/CLOSURE_SCA_APP_011_ESR1_RULING_2026-09-27_1739/closure_run.py
```
