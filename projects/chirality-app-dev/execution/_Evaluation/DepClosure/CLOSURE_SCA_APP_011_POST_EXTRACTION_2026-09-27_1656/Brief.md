# Brief

## Verbatim basis

`project-setup` INCREMENTAL, Phase 5.6 (FULL_GRAPH): "dispatch `dependency-extract` for the same deliverables as above, then run `audit-dep-closure` over the accepted inventory (its `SCOPE: ALL` rules, with retired exemptions): a new cycle through a changed edge can pass through unaffected deliverables. The audit reads existing registers; it does not re-extract them. Route new SCCs to `scc-resolution-case`."

The owner confirmed the SCA-APP-011 incremental plan on 2026-09-27 (`execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION.md`).

## Normalized

```
EXECUTION_ROOT: projects/chirality-app-dev/execution
SCOPE: ALL rules; inventory = the 54 PKG-*/1_Working/DEL-* folders
EXEMPT_UNITS:
  - DEL-00-01 CONTROL (its _CONTEXT.md excludes product graph participation; no Dependencies.csv by design)
  - DEL-00-02 CONTROL (same)
  - DEL-09-07 RETIRED (decomposition Deliverables row annotated [RETIRED]; SOW-080 OUT)
SCOPE_UNITS passed to the analyzer: the 51 non-exempt units (primary run, Evidence/); ALL as a census (Evidence/ALL/)
RUN_LABEL: SCA_APP_011_POST_EXTRACTION
REQUESTED_BY: WORKING_ITEMS (workflow: project-setup), run APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27
UPDATE_LATEST_POINTER: false (no brief sets it; the move is proposed, not made)
FILTER_ACTIVE_ONLY: true
NORMALIZE_IDS: true
EDGE_FILTER: DependencyClass=EXECUTION; TargetType=DELIVERABLE
HUB_THRESHOLD: 20
MAX_CYCLES: 10000
INCLUDE_DECLARED: true
PRIOR_SUMMARY: CURRENT51 -> CLOSURE_APP_RECORD_CLOSEOUT_2026-09-22_211905Z/Evidence/CURRENT51/closure_summary.json;
               ALL -> AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/dep_closure/closure_summary.json (pre-extraction)
```
