# DEL-02-03 M2 Preparation Package

Status: `PREPARED — BLOCKED ON D-GOV-35 RULING`

Run: `ROOT_V3_PHASE0_2026-08-22`, node `N2`

Deliverable: `DEL-02-03 — Delegation Hierarchy and Entry Rules`

This derivative preparation package stages the Root instruction-application
tranche described by the 2026-08-22 owner steer. It changes no live
instruction, standard, decision, notice, lifecycle, pointer, status, hold,
pin, product source, project loop, or release state. Structural validation of
the draft manifest is evidence only; it is not an M2 authorization, an owner
ruling on D-GOV-35, or authority to apply the referenced patch.

## Package contents

| File | Purpose |
|---|---|
| `ROOT-DGOV35-DELEGATED-HARNESS-NATIVE-20260822.yaml` | Structurally valid draft instruction-tranche manifest, with the unresolved M2 authorization stated rather than inferred. |
| `AGENTS_DELTA_REFERENCE.md` | Exact identity of the N1 patch without duplicating its bytes. |
| `DRAFT_NOTICE_APP.md` | Unrouted draft coordination notice for the Chirality App loop. |
| `DRAFT_NOTICE_PIPING.md` | Unrouted draft coordination notice for the Chirality Piping loop. |
| `VALIDATION_PLAN.md` | Required application-tranche checks and their evidence expectations. |
| `BASIS_EVIDENCE.md` | Preparation-basis identities and read-only precondition evidence. |
| `VALIDATION_EVIDENCE.md` | Reproduced N2 preparation checks and exact outcomes. |
| `HANDOFF_STATE.md` | Explicit blocked handoff, rerun requirements, and next owner. |

## Controlling inputs

- Owner steer:
  `plans/steers/chirality_app_v3_phase0_steer_root_2026-08-22.md`, SHA-256
  `c348e9767db4af20787bbcb74c64791ef08d700b08dc19d86289a88a58f067e3`.
- Owner G0 record:
  `plans/steers/chirality_app_v3_g0_record_2026-08-22.md`, SHA-256
  `86b9877c6bea08a9f79c2af2378d5d38722a09c1a10deb37f87211c76d2c290b`.
- Accepted N1 proposal packet:
  `docs/governance_harness/_PROPOSALS/D-GOV-35_2026-08-22_delegated_harness_native_class/`.
- Exact proposed Root instruction delta: the N1 patch identified in
  `AGENTS_DELTA_REFERENCE.md`.

The accepted N1 packet is candidate state awaiting an owner ruling. This
package consumes it as an accepted upstream preparation result, not as adopted
governance.
