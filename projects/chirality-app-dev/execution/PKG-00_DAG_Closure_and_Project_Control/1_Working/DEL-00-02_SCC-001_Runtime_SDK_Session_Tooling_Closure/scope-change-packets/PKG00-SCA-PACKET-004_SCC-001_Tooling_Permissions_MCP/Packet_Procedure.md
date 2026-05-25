# Packet Procedure: PKG00-SCA-PACKET-004

## Intake Procedure

1. Confirm a human explicitly initiates SCOPE_CHANGE using or adapting `SCOPE_CHANGE_INIT.md`.
2. Load the cited decomposition authority and DepClosure snapshot.
3. Verify SCC-001 membership and the packet-relevant bidirectional pairs.
4. Review affected product deliverable `_CONTEXT.md`, `_STATUS.md`, `_DEPENDENCIES.md`, `Dependencies.csv`, and four-doc kit files before accepting any action.
5. Decide whether the issue is decomposition text, dependency classification, handoff-state wording, or no amendment.
6. Record unresolved rulings as `TBD`; do not infer approval from this packet.

## Gate-by-Gate Use

| Gate | Action |
|---|---|
| Gate 1 Evidence | Validate `Evidence_Index.csv` paths and references. |
| Gate 2 Impact | Compare `Affected_Surfaces.csv` against live affected deliverable files. |
| Gate 3 Amendment Design | Select or revise `Proposed_SCA_Actions.csv` rows. |
| Gate 4 Application | Apply changes only inside the authorized SCOPE_CHANGE write scope. |
| Gate 5 Verification | Re-run relevant dependency closure checks and record a new governed snapshot if accepted. |

## Operator Notes

- If a later workflow mutates dependency registers, cite the exact row IDs and pre/post evidence in that workflow.
- If a later workflow amends decomposition scope, cite the accepted upstream decomposition and produce the required snapshot or pointer update.
- If REF-006 remains hash-mismatched, keep PRD-only implementation details warning-qualified.
- Do not use this packet to report a global graph state.

## Packet Handoff State

| Field | Value |
|---|---|
| Accepted upstream snapshot | DepClosure `CLOSURE_POST_ID_CANONICALIZATION_2026-05-24_1431` |
| Derivative package status | Derivative SCOPE_CHANGE consumable packet |
| Closure verdict | Not a closure artifact |
| Rerun requirements | Re-run packet validation after any manual edit; run dependency closure only in authorized workflow |
| Remaining blockers | Human SCOPE_CHANGE initiation and all `TBD` rulings |
