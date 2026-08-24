# AUDIT_DEP_CLOSURE — Sealed Brief

- `Parent`: `N4-SCOPE-CHANGE-01`
- `RequestedBy`: `SCOPE_CHANGE`
- `Role`: `AUDIT_DEP_CLOSURE` (named dedicated Agent 2)
- `RunLabel`: `SCA-APP-008-GATE5-POST-APPLICATION`
- `Basis`: `cc196023a5532fe58955655c1144cd09ee88343a`
- `PostApplicationDecomposition`: `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`, SHA-256 `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f`
- `Objective`: independently audit post-application dependency closure after the registered Gate-5 dependency refresh for DEL-02-05, DEL-08-04, DEL-08-05, and DEL-09-05; resolve every endpoint, reproduce the accepted SCC moves and non-gating posture, surface any new SCC without linearization, and return one new immutable evidence package.
- `ExecutionRoot`: `projects/chirality-app-dev/execution`
- `Scope`: `ALL`
- `FilterActiveOnly`: `true`
- `NormalizeIds`: `true`
- `ReadScope`: repository read-only as needed to consume the post-application decomposition, all deliverable-local dependency registers, the accepted SCA-APP-008 DAG/SCC records, and the four newly extracted records; no network.
- `ContentWriteRoot`: `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/Phase5/Audit/SCA-APP-008-GATE5-POST-APPLICATION_2026-08-24/**`
- `ControlWriteRoot`: `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_GATE5_2026-08-24/instances/N4-SCOPE-CHANGE-01/children/AUDIT-DEP-CLOSURE-GATE5-01/**`

## Human override to the generic role

The owner's exact Gate-5 write set and the manager's sealed brief supersede the generic `AGENT_AUDIT_DEP_CLOSURE.md` default `_Evaluation/DepClosure/` tool root and pointer update. Write the new immutable package only under the `ContentWriteRoot` above. Do not create or modify `projects/chirality-app-dev/execution/_Evaluation/**`; do not move any `_LATEST.md` pointer; do not modify dependency registers, deliverable source documents, SOWs, statuses, lifecycle files, contracts, decomposition, registers, frontend, Root surfaces, or any path outside the two exact write roots. Record this override in `Decision_Log.md` and both returns.

## Required checks

1. Read `AGENTS.md` and `agents/AGENT_AUDIT_DEP_CLOSURE.md` completely before acting. Agent 2 must not delegate.
2. Run the deterministic registered analyzer exactly once:
   `PYTHONDONTWRITEBYTECODE=1 python3 tools/coordination/analyze_dep_closure.py projects/chirality-app-dev/execution --output-dir <ContentWriteRoot>/Evidence`
3. Verify all discovered dependency registers against the v3.1 schema; resolve every active deliverable endpoint and evidence row. Record missing/invalid registers without guessing.
4. Explicitly consume and identify the four refreshed dependency records:
   - DEL-02-05 `c39a3d533bf5f811f35d3a3b7fbfd839e7c1baedc28607cc4d59ad9eb200b8d0`
   - DEL-08-04 `6c838e527a0f45f26dd12ae8ff15724369be23a8fce2f15114c9abf46ad9c9ed`
   - DEL-08-05 `70b4ef79271978b1b6d99ed34d768f8970ca67307ea819c024a2fe9138634042`
   - DEL-09-05 `bde522ad79fb274157fe2bfa27ae527bb6c8715ed167235cf89a6576a8310afb`
5. Confirm the managed and delegated-harness-native descendant classes each occur once in DEL-08-04 and once in DEL-08-05, with no Agent-role inference from native descent.
6. Compare observed graph closure with accepted A2-B orderings in Gate-4 section 4. E-018, E-020, and E-032 remain non-gating objective-relative feedback edges; absence from an individual dependency register is not permission to invent one. Preserve the accepted DECOMPOSE/INVERT moves and all downstream gates.
7. Identify every observed directed SCC. Any new SCC is reported and never silently linearized. Distinguish the live dependency-register graph from the accepted objective-relative SCA DAG rather than falsely treating one as a substitute for the other.
8. Return `PASS`, `WARNINGS`, or `BLOCKER` with evidence. Any blocking result is returned verbatim and not upgraded.

## Required package outputs

- `Brief.md` containing this brief verbatim plus a normalized summary
- `RUN_SUMMARY.md`
- `QA_Report.md`
- `Decision_Log.md`
- `Dependency_Closure_Report.md`
- `Dependency_Closure_IssueLog.csv`
- `Evidence/closure_summary.json`
- `Evidence/coverage.csv`
- `Evidence/orphans.csv`
- `Evidence/cycles_sample.csv`
- `Evidence/scc_summary.csv`
- `Evidence/hubs.csv`
- `Evidence/bidirectional_pairs.csv`
- `Evidence/id_normalization.csv`
- reproducible analyzer copy or exact analyzer identity and invocation as required by `AGENT_AUDIT_DEP_CLOSURE.md`
- child `RETURN.md` and `STATUS.json`

No source repair, no delegation, no Git action, and no pointer movement.
