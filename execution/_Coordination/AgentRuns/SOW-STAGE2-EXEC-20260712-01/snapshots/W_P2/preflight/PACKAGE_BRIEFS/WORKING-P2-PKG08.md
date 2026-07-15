
# WORKING-P2-PKG08 Sealed Package Brief

Status: `PARKED — AWAITING HELP_HUMAN ACCEPTANCE AND PREDECESSOR RELEASE`

Execute only after `W-P2-PKG07_PASS`. Incorporate
`../PACKAGE_EXECUTION_CONTRACT.md` exactly. This is one fresh package manager;
retain package ownership across all batches.

## Exact members

- `DEL-08-01` — 290 lines — `projects/chirality-piping/execution/PKG-08_Reporting, Audit, and Reproducibility/1_Working/DEL-08-01_Calculation report generator`
- `DEL-08-02` — 253 lines — `projects/chirality-piping/execution/PKG-08_Reporting, Audit, and Reproducibility/1_Working/DEL-08-02_Audit manifest and model hash`
- `DEL-08-03` — 341 lines — `projects/chirality-piping/execution/PKG-08_Reporting, Audit, and Reproducibility/1_Working/DEL-08-03_Warnings, assumptions, and provenance report section`
- `DEL-08-04` — 257 lines — `projects/chirality-piping/execution/PKG-08_Reporting, Audit, and Reproducibility/1_Working/DEL-08-04_Result export format`
- `DEL-08-05` — 347 lines — `projects/chirality-piping/execution/PKG-08_Reporting, Audit, and Reproducibility/1_Working/DEL-08-05_Report protected-content linter`
- `DEL-08-06` — 301 lines — `projects/chirality-piping/execution/PKG-08_Reporting, Audit, and Reproducibility/1_Working/DEL-08-06_State, comparison, and handoff report sections`

## Exact consecutive batches

- `PKG-08-B1`: 5 members, 1488 lines; `DEL-08-01,DEL-08-02,DEL-08-03,DEL-08-04,DEL-08-05`; author `WORKING-P2-PKG08/children/AUTHOR-B1` then verifier `WORKING-P2-PKG08/children/VERIFY-B1`
- `PKG-08-B2`: 1 members, 301 lines; `DEL-08-06`; author `WORKING-P2-PKG08/children/AUTHOR-B2` then verifier `WORKING-P2-PKG08/children/VERIFY-B2`

Candidate scope: `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/W_P2/PIP-PKG08/**`

Evidence scope: `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P2-PKG08/**`

Before dispatch, reproduce every package row and hash from `P2_MANIFEST.tsv`
and `EXPECTED_LIVE_BINDINGS.tsv`, current `IN_PROGRESS` lifecycle, valid exact
`LEGACY_FOUR_DOC`, SOW absence, accepted predecessors, PKG-00 direction, active
method/check bindings, and refs. Dispatch the author/verifier pair for each
batch serially. Child write scopes must be disjoint by role/batch; children do
not delegate. Do not write live project paths, Git, lifecycle, PKG-00,
integration, release, reliance, retirement, rollback execution, or H2 state.

Return PASS, BLOCKED, or DECISION_REQUIRED with complete per-member fan-in,
attempt history, repairs/rebindings, telemetry, blockers/unknowns/waivers,
derivative status, rerun triggers, and explicit handoff for direct RECON.
