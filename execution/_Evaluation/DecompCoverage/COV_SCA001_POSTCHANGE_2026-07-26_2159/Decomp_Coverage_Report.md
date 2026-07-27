# Decomposition Coverage Report — SCA001_POSTCHANGE

## Audit basis

This immutable snapshot is derivative audit evidence. It evaluates `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` revision 1.1, physically applied from the approved candidate at `execution/_ScopeChange/SCA-001_2026-07-26_1454/Gate_3_Candidate/`, against current filesystem state at Git HEAD `196c98a0c777abc2df00341b1ff6a0f92f0ecd54`. It supports `SCA-001_GATE_5_OWNER_CONFIRMATION` and does not accept, amend, or replace decomposition truth.

## Overall verdict

`OVERALL_STATUS = BLOCKERS`
`CLOSURE_READINESS = FAIL`

The applied decomposition package is internally referentially coherent: 104 scope rows, 46 deliverable rows, 7 objectives, and the SOW-104 → PKG-02 → DEL-02-06 → OBJ-001/002/004/007 lineage resolve. Filesystem forward coverage is incomplete by one deliberately unmaterialized downstream carrier: DEL-02-06 is declared but its folder does not exist. AUDIT_DECOMP classifies that fact as a Check 2 BLOCKER; the audit does not downgrade it because PROJECT_SETUP is intentionally blocked.

## Twelve-check summary

| Check | Name | Verdict | Evidence |
|---|---|---|---|
| 1 | Forward Coverage — Packages | PASS | 6/6 declared packages found. |
| 2 | Forward Coverage — Deliverables | BLOCKER | 45/46 declared deliverables found; missing: DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance. |
| 3 | Reverse Coverage — Folders | PASS | No reverse-only folder found. |
| 4 | ID Consistency | PASS | All 45 matched SOFTWARE IDs and parent-package paths agree. |
| 5 | Context Fidelity | PASS | 45/46 declared contexts match; the missing scaffold has no context to evaluate. |
| 6 | Artifact Presence | PASS | 45/45 present SOW_V1 contracts validate; 0/137 anticipated outputs present and 132 lifecycle-appropriate INFO findings emitted. |
| 7 | Objective Mapping | PASS | All 7 objective support sets match the deliverable register; every objective retains at least one filesystem-backed supporter. |
| 8 | Ledger Integrity | PASS | 104 rows (95 IN, 9 OUT); every IN reference resolves to declared package, deliverable, and objective IDs. |
| 9 | Derivative Package Parity | SKIPPED | Not variant-owned by this SOFTWARE audit. |
| 9b | Package-Shape Conformance | PASS | §3 labels authoritative companions; no derived publication surface is treated as amendment truth. |
| 10 | Active Snapshot and Handoff State | PASS | PASS: active snapshot execution/_ScopeChange/SCA-001_2026-07-26_1454 contains the required artifact set. Handoff honesty is PASS. |
| 11 | Lifecycle Distribution | PASS | {'INITIALIZED': 45, 'UNKNOWN': 1}; the missing deliverable is UNKNOWN because no status file exists. |

## Top issues

1. **BLOCKER — DEL-02-06 filesystem carrier absent.** The deliverable is declared under PKG-02 in revision 1.1 but `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/` is absent. This is the exact downstream gap reserved to PROJECT_SETUP.
2. **PASS — active SCA snapshot and handoff posture are internally honest for the current Gate 5 phase.**
3. **INFO — anticipated outputs remain unproduced.** 132 existing-deliverable anticipated-output absences remain INFO because all present deliverables are INITIALIZED.

## What to fix for a cleaner rerun

Do not materialize DEL-02-06 from this audit. After the owner confirms Gate 5 and the authorized Git closeout is complete, PROJECT_SETUP may scaffold DEL-02-06 and refresh the registered guard state under its own gates. Rerun AUDIT_DECOMP afterward. Any active-snapshot artifact-contract finding must be corrected by SCOPE_CHANGE before it claims closure; this audit does not perform that correction.
