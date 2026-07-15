
# WORKING-P4-PKG15 Sealed Package Brief

Status: `PARKED — AWAITING HELP_HUMAN ACCEPTANCE AND PREDECESSOR RELEASE`

Execute only after `W-P4-PKG14_PASS`. Incorporate
`../PACKAGE_EXECUTION_CONTRACT.md` exactly. This is one fresh package manager;
retain package ownership across all batches.

## Exact members

- `DEL-15-01` — 300 lines — `projects/chirality-piping/execution/PKG-15_Handoff and External Prover Workflow/1_Working/DEL-15-01_Canonical handoff package schema and manifest`
- `DEL-15-02` — 307 lines — `projects/chirality-piping/execution/PKG-15_Handoff and External Prover Workflow/1_Working/DEL-15-02_Target mapping and unsupported-behavior contract`
- `DEL-15-03` — 251 lines — `projects/chirality-piping/execution/PKG-15_Handoff and External Prover Workflow/1_Working/DEL-15-03_Downstream modeling export workflow`
- `DEL-15-04` — 229 lines — `projects/chirality-piping/execution/PKG-15_Handoff and External Prover Workflow/1_Working/DEL-15-04_External prover boundary metadata`

## Exact consecutive batches

- `PKG-15-B1`: 4 members, 1087 lines; `DEL-15-01,DEL-15-02,DEL-15-03,DEL-15-04`; author `WORKING-P4-PKG15/children/AUTHOR-B1` then verifier `WORKING-P4-PKG15/children/VERIFY-B1`

Candidate scope: `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/W_P4/PIP-PKG15/**`

Evidence scope: `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P4-PKG15/**`

Before dispatch, reproduce every package row and hash from `P4_MANIFEST.tsv`
and `EXPECTED_LIVE_BINDINGS.tsv`, current `IN_PROGRESS` lifecycle, valid exact
`LEGACY_FOUR_DOC`, SOW absence, accepted predecessors, PKG-00 direction, active
method/check bindings, and refs. Dispatch the author/verifier pair for each
batch serially. Child write scopes must be disjoint by role/batch; children do
not delegate. Do not write live project paths, Git, lifecycle, PKG-00,
integration, release, reliance, retirement, rollback execution, or H2 state.

Return PASS, BLOCKED, or DECISION_REQUIRED with complete per-member fan-in,
attempt history, repairs/rebindings, telemetry, blockers/unknowns/waivers,
derivative status, rerun triggers, and explicit handoff for direct RECON.
