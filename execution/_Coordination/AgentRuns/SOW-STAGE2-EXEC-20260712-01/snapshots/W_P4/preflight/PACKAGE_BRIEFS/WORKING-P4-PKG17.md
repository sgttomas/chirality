
# WORKING-P4-PKG17 Sealed Package Brief

Status: `PARKED — AWAITING HELP_HUMAN ACCEPTANCE AND PREDECESSOR RELEASE`

Execute only after `W-P4-PKG16_PASS`. Incorporate
`../PACKAGE_EXECUTION_CONTRACT.md` exactly. This is one fresh package manager;
retain package ownership across all batches.

## Exact members

- `DEL-17-01` — 276 lines — `projects/chirality-piping/execution/PKG-17_Export Format Interoperability/1_Working/DEL-17-01_CAEPIPE and export-format source basis`
- `DEL-17-02` — 437 lines — `projects/chirality-piping/execution/PKG-17_Export Format Interoperability/1_Working/DEL-17-02_Export package, profile, and stable ID map contracts`
- `DEL-17-03` — 163 lines — `projects/chirality-piping/execution/PKG-17_Export Format Interoperability/1_Working/DEL-17-03_Native open JSON export package`
- `DEL-17-04` — 213 lines — `projects/chirality-piping/execution/PKG-17_Export Format Interoperability/1_Working/DEL-17-04_CAEPIPE MBF export profile and deterministic writer`
- `DEL-17-05` — 439 lines — `projects/chirality-piping/execution/PKG-17_Export Format Interoperability/1_Working/DEL-17-05_CAEPIPE external run harness and CSV parser`
- `DEL-17-06` — 372 lines — `projects/chirality-piping/execution/PKG-17_Export Format Interoperability/1_Working/DEL-17-06_Stress-neutral CSV JSON package`
- `DEL-17-07` — 407 lines — `projects/chirality-piping/execution/PKG-17_Export Format Interoperability/1_Working/DEL-17-07_Conservative PCF subset exporter`
- `DEL-17-08` — 402 lines — `projects/chirality-piping/execution/PKG-17_Export Format Interoperability/1_Working/DEL-17-08_GLB glTF review geometry export`
- `DEL-17-09` — 412 lines — `projects/chirality-piping/execution/PKG-17_Export Format Interoperability/1_Working/DEL-17-09_Export adapter SDK and additional targets`

## Exact consecutive batches

- `PKG-17-B1`: 5 members, 1528 lines; `DEL-17-01,DEL-17-02,DEL-17-03,DEL-17-04,DEL-17-05`; author `WORKING-P4-PKG17/children/AUTHOR-B1` then verifier `WORKING-P4-PKG17/children/VERIFY-B1`
- `PKG-17-B2`: 4 members, 1593 lines; `DEL-17-06,DEL-17-07,DEL-17-08,DEL-17-09`; author `WORKING-P4-PKG17/children/AUTHOR-B2` then verifier `WORKING-P4-PKG17/children/VERIFY-B2`

Candidate scope: `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/W_P4/PIP-PKG17/**`

Evidence scope: `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P4-PKG17/**`

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
