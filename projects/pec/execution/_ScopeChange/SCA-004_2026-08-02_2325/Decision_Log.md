---
amendment_id: SCA-004
doc_kind: scope_change.decision_log
decomp_variant: SOFTWARE
current_gate: complete
status: gate_5_executed_validated
---

# SCA-004 Decision Log

| DecisionRef | Gate | Decision | Status | Authority |
|---|---:|---|---|---|
| SCA004-G1 | 1 | Confirm MODIFY-only parsing; map SOW-077 to PKG-01 → DEL-01-06 → OBJ-004; resolve OI-003 by D-PEC-78 O-A; preserve DEL-01-06 name/path | `CONFIRMED` | Owner ruling, 2026-08-02 |
| SCA004-G2 | 2 | Accept `Impact_Assessment.md` at SHA-256 `df366142e47063b452e43fc90958b839bba6ab0709f556f336e32d52e9556661` | `CONFIRMED` | Owner ruling, 2026-08-03 |
| SCA004-G3 | 3 | Approve exact `Amendment_Preview.md` SHA-256 `4a473ca087ba4f0fa63cc98432165ec46a819a36f22c9ab44f3c98778dae245f` | `CONFIRMED` | Owner ruling, 2026-08-03 |
| SCA004-G4 | 4 | Approve `Propagation_Plan.md` SHA-256 `f63d45eb6c56bd5396e71ddce5c84cbd088aa2eb876864f06039b299336757f2` for later Gate 5 execution only | `CONFIRMED` | Owner ruling, 2026-08-03 |
| SCA004-G5 | 5 | Execute the approved amendment, produce revision 1.4, run post-change AUDIT_DECOMP, move pointers after completeness, and return a derivative-state handoff without downstream repair | `CONFIRMED / EXECUTED` | Owner direction, 2026-08-03 |

The Gate 3 confirmation approves only the exact amendment content and opens
preparation of the Gate 4 propagation plan. It does not approve a propagation
plan, open Gate 5, or authorize a live decomposition edit, pointer move,
metadata repair, downstream rerun, or foreign write.

The Gate 4 plan is prepared and mechanically validated. Its preparation does
not approve the plan, open Gate 5, or execute any planned act.

The owner subsequently approved the exact plan for later Gate 5 execution
only, then separately opened Gate 5 on 2026-08-03 with this direction:

> SCA-004 Gate 5: execute the approved amendment per the accepted propagation
> plan — verify preimage hashes, apply the exact postimage, produce revision
> 1.4 with the complete SCA-004 artifact set, rerun AUDIT_DECOMP post-change
> against the pre-change baseline, move the pointers, and return the
> derivative-state handoff naming every stale surface, its owner, and its
> rerun obligation as separately gated follow-ups. No downstream repair is
> authorized by Gate 5 itself.

All five preimage hashes matched. The direct postimage, one approved context
mirror, immutable post-change audit, complete SCA snapshot, and pointer moves
were serialized under the accepted propagation plan. No Lane B downstream
repair was performed.
