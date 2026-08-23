# Orchestration Plan — Root v3 Phase 0e

PlanVersion: `1`

SelectionAuthority: `HUMAN — R4-A/R4-B/R4-C`

Posture: `TERMINAL_FAN_OUT_IN` (one bounded execution node, followed by fresh read-only review)

TerminalDisposition: `BLOCKED_RECOVERED — one application attempt consumed; Gate 5 unexecuted`

AcceptedBasis: `origin/main@6da0b548d4ec5d303adecdd448ad1a5517c9e27b`

Owner: `Ryan Tufts (K-AUTH-1)`

## Objective

Execute SCA-004 Gate 5 exactly once under R4-B: replace the seven live
revision-1.2 decomposition surfaces with the exact R4-A applied identities,
run the approved closure-validation lane, and return the applied state for
owner confirmation. R4-C keeps `_LATEST.md` unchanged.

## Node and ownership

| Node | Executor | Content write targets | Control evidence | Depends on | Expected return |
| --- | --- | --- | --- | --- | --- |
| N1 | bounded ephemeral Agent 2 (`role not mechanically enforced`; instruction-asserted) | seven named `execution/_Decomposition/` files; `Gate_5_Application_Record.md`; `Evidence/AUDIT_DECOMP_POST_GATE5/**`; SCA `Decision_Log.md`; SCA `Handoff_State.md` | `instances/N1_GATE5_EXECUTION/**` | passed basis gate; R4-A append approval; R4-B one-time authorization; R4-C pointer deferral | exact applied identities, closure evidence, PASS results, blockers |

The seven-file application is executed once against exact identities. Evidence
and record writes may receive bounded repair and fresh re-review; the
application is not repeated. A closure-lane failure is recorded without a
silent reversal.

## Fan-in gates

1. Seven live decomposition identities equal R4-A exactly.
2. Fresh package validation remains PASS 64/64; the applied-state Gate-3
   equivalent remains PASS 98/98.
3. Post-Gate-5 scoped AUDIT_DECOMP backcheck records the expected 53 / 12 / 11
   topology and zero mapping/trace gaps against the preserved Gate-1 baseline.
4. All ten DEL-02-06 bindings remain `HELD_UNAVAILABLE` and are cited.
5. `_LATEST.md`, every `_STATUS.md`, Task Management, folders, and every other
   protected surface remain unchanged.
6. A fresh read-only Agent 2 review returns zero actionable findings; findings
   trigger bounded evidence/record repair and another fresh review.

## Human gates retained

Gate-5 confirmation, `_LATEST.md` pointer approval, Git-effect SHA backfill,
and all later propagation acts remain owner-gated. No hold is lifted.
