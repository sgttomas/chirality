# Run Manifest — ROOT-SCA001-PROJECT-SETUP-20260726

## Identity

- Parent role: `PROJECT_SETUP` (Agent 1)
- Child role: `PREPARATION` (Agent 2)
- Project root: repository root
- Execution root: `execution/`
- Accepted decomposition/release basis:
  `2db2c712825af13d6b5425c34d31ff9daf470c89` (PR #366)
- Resumed instruction basis:
  `ff04694afa709856a58f9f54a79ca2056b8e0b4e` (PR #368)
- Accepted decomposition: Root SOFTWARE decomposition revision 1.1
- Authorizing handoff:
  `execution/_ScopeChange/SCA-001_2026-07-26_1454/Handoff_State.md`
- Source preparation brief:
  `execution/_ScopeChange/SCA-001_2026-07-26_1454/Preparation_Brief.md`

## Objective

Close the sole post-SCA filesystem coverage blocker by scaffolding
DEL-02-06, then refresh the coupled Root G1/G2/G3 state to the accepted
revision 1.1 basis and verify 46/46 coverage.

## Work graph

1. `PREP-DEL0206` — PREPARATION creates the bounded DEL-02-06 minimum viable
   control-file scaffold.
2. `HARNESS-REFRESH` — PROJECT_SETUP, as serialized integration owner, updates
   G1/G2/G3 state after the scaffold return.
3. `G2-HOLD` — live G2 exposes a nested-deliverable capability gap;
   PROJECT_SETUP stops without weakening the accepted ownership entry.
4. `G2-RESUME` — after the separately governed HELPS_HUMANS/M2 correction is
   accepted through PR #368, PROJECT_SETUP consumes the new instruction basis
   and re-pins G3 without changing graph topology.
5. `GUARD-FANIN` — PROJECT_SETUP runs G0–G4 and targeted tests.
6. `POST-AUDIT` — AUDIT_DECOMP produces an immutable 46/46 coverage snapshot.
7. `HUMAN-HANDOFF` — PROJECT_SETUP reports the validated setup result. No
   production drafting follows in this run.

## Write boundaries

PREPARATION may write only:

`execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/**`

PROJECT_SETUP may additionally write:

- `execution/_harness/adapter.yaml`
- `execution/_harness/surface_ownership.yaml`
- `execution/_harness/work_graph.yaml`
- this run directory

AUDIT_DECOMP may write only a new snapshot and pointer under:

`execution/_Evaluation/DecompCoverage/`

## Prohibitions

- No `ScopeOfWork.md`.
- No `runtime/**` implementation.
- No dependency edge.
- No existing deliverable edit.
- No decomposition, PRD, governance, App, PEC, or other project edit.
- No lifecycle advancement beyond `OPEN`.

## Engine identity

- PROJECT_SETUP engine/provider/model: Codex / OpenAI / unknown exact model
- PREPARATION engine/provider/model: recorded in child return
- AUDIT_DECOMP engine/provider/model: recorded in child return
