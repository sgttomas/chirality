# Sealed Launch Brief — N1 Gate-5 application package

BriefVersion: `1`

Role: `bounded ephemeral Agent 2` (`role not mechanically enforced`; governed evidence is instruction-asserted)

Parent: `HELP_HUMAN / ROOT_V3_PHASE0D_2026-08-23`

AcceptedBasis: `3da1eb38bff55deb6d08e2c5e44947fe1fb56315`

## Purpose

Act as the bounded SCOPE_CHANGE specialist for the single Phase-0d node.
Transcribe owner rulings R3-A/R3-B and draft—never apply—the exact Gate-5
application package satisfying CONDITION R3-B-1.

## Required reads

- root `AGENTS.md`
- `agents/AGENT_SCOPE_CHANGE.md`
- `plans/steers/chirality_app_v3_phase0d_steer_root_2026-08-23.md`
- `plans/steers/chirality_app_v3_root_ruling_record_r3_2026-08-23.md`
- all files in `execution/_ScopeChange/SCA-004_2026-08-22_1749/`
- the seven live revision-1.2 decomposition/companion files cited by the steer

## Content write scope

Only `execution/_ScopeChange/SCA-004_2026-08-22_1749/**`.

Control return only:
`execution/_Coordination/AgentRuns/ROOT_V3_PHASE0D_2026-08-23/instances/N1_GATE5_PACKAGE/RETURN.md`.

No other write is authorized. Do not stage, commit, push, fetch, merge, rebase,
or create a PR. Do not delegate.

## Exact outputs

Produce every N1 artifact and edit required by the Phase-0d steer:

- ruled `Decision_Log.md` entries and gate states;
- exhaustive `Gate_5_Slot_Inventory.md`;
- zero-context `Gate_5_Application_Append.diff` limited to inventoried status
  slots;
- seven files under `Gate_5_Applied_Candidate/`;
- `Gate_5_Applied_Preview.md` with approved→applied SHA table and slot table;
- deterministic `validate_gate5_package.py` and `Gate_5_Validation.json`;
- exact `Gate_5_Brief.md`;
- drafting-only `Gate_5_Pointer_Candidate.md`;
- four-state `Handoff_State.md` at
  `AWAITING_OWNER_GATE_5_APPEND_APPROVAL`.

Preserve all Phase-0c approved bytes named read-only by the steer. Gate 5 is
not executed.

## Acceptance checks

- rerun Gate-3 validation: PASS 98/98, JSON byte-identical;
- Gate-5 package validation: PASS, zero failures, deterministic count;
- exact append applies with `git apply --unidiff-zero --check` in a scratch
  candidate-at-live-path layout and reproduces applied candidates;
- every append hunk lies within an inventory slot;
- all structural CSV/tracing/count content is unchanged outside slots;
- protected live surfaces, `_LATEST.md`, every `_STATUS.md`, and Task
  Management register remain byte-identical;
- no forbidden path changes;
- return hashes, check results, changed-path list, and blockers in `RETURN.md`.

If completing the package would require a write outside scope or a change to
an approved byte, stop and return the blocker without narrowing silently.
