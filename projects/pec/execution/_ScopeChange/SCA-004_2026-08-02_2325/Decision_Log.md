---
amendment_id: SCA-004
doc_kind: scope_change.decision_log
decomp_variant: SOFTWARE
current_gate: 5
status: gate_4_confirmed_gate_5_not_authorized
---

# SCA-004 Decision Log

| DecisionRef | Gate | Decision | Status | Authority |
|---|---:|---|---|---|
| SCA004-G1 | 1 | Confirm MODIFY-only parsing; map SOW-077 to PKG-01 → DEL-01-06 → OBJ-004; resolve OI-003 by D-PEC-78 O-A; preserve DEL-01-06 name/path | `CONFIRMED` | Owner ruling, 2026-08-02 |
| SCA004-G2 | 2 | Accept `Impact_Assessment.md` at SHA-256 `df366142e47063b452e43fc90958b839bba6ab0709f556f336e32d52e9556661` | `CONFIRMED` | Owner ruling, 2026-08-03 |
| SCA004-G3 | 3 | Approve exact `Amendment_Preview.md` SHA-256 `4a473ca087ba4f0fa63cc98432165ec46a819a36f22c9ab44f3c98778dae245f` | `CONFIRMED` | Owner ruling, 2026-08-03 |
| SCA004-G4 | 4 | Approve `Propagation_Plan.md` SHA-256 `f63d45eb6c56bd5396e71ddce5c84cbd088aa2eb876864f06039b299336757f2` for later Gate 5 execution only | `CONFIRMED` | Owner ruling, 2026-08-03 |
| SCA004-G5 | 5 | Execute and validate | `NOT AUTHORIZED` | Requires separate owner Gate 5 authorization |

The Gate 3 confirmation approves only the exact amendment content and opens
preparation of the Gate 4 propagation plan. It does not approve a propagation
plan, open Gate 5, or authorize a live decomposition edit, pointer move,
metadata repair, downstream rerun, or foreign write.

The Gate 4 plan is prepared and mechanically validated. Its preparation does
not approve the plan, open Gate 5, or execute any planned act.

The owner subsequently approved the exact plan for later Gate 5 execution
only. No Gate 5 act is authorized by that approval.
