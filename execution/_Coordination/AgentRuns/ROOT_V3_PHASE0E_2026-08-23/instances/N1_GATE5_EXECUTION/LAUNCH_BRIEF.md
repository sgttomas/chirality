# Sealed Launch Brief — N1 Gate-5 execution and closure lane

BriefVersion: `1`

Role: `bounded ephemeral Agent 2` (`role not mechanically enforced`; governed evidence is instruction-asserted)

Parent: `HELP_HUMAN / ROOT_V3_PHASE0E_2026-08-23`

AcceptedBasis: `6da0b548d4ec5d303adecdd448ad1a5517c9e27b`

## Purpose

Act as the bounded SCOPE_CHANGE specialist for the single Phase-0e node.
Execute the exact R4-B Gate-5 application once, require the R4-A identities,
run and record closure-validation items 1–6, and return the applied state for
owner confirmation. Do not write the pointer or perform later propagation.

## Required reads

- root `AGENTS.md`
- `agents/AGENT_SCOPE_CHANGE.md`
- `agents/AGENT_AUDIT_DECOMP.md`
- `plans/steers/chirality_app_v3_phase0e_steer_root_2026-08-23.md`
- `plans/steers/chirality_app_v3_root_ruling_record_r4_2026-08-23.md`
- all approved inputs named by the Phase-0e steer, especially
  `Gate_5_Brief.md`, `Propagation_Plan.md`, the Gate-3 and Gate-5 candidate
  folders, append, preview, inventory, validator, and validation JSON
- the seven live revision-1.2 files and preserved Gate-1 AUDIT_DECOMP baseline

## Content write scope

Exactly:

- `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`
- `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`
- `execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv`
- `execution/_Decomposition/chirality_root_objective_register_v1_0.csv`
- `execution/_Decomposition/chirality_root_prd_coverage_forward_v1_0.csv`
- `execution/_Decomposition/chirality_root_trace_reverse_v1_0.csv`
- `execution/_Decomposition/chirality_root_coverage_telemetry_v1_0.md`
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_5_Application_Record.md`
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Evidence/AUDIT_DECOMP_POST_GATE5/**`
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Decision_Log.md`
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Handoff_State.md`

Control return only:
`execution/_Coordination/AgentRuns/ROOT_V3_PHASE0E_2026-08-23/instances/N1_GATE5_EXECUTION/RETURN.md`.

No other write is authorized. Do not stage, commit, push, fetch, merge, rebase,
or create a PR. Do not delegate.

## Exact execution contract

1. Before any governed write, independently reverify every bound identity in
   the Phase-0e basis gate. Run `validate_gate5_package.py` fresh; require PASS
   64/64, both embedded 98/98 results, and byte-identical validation JSON.
2. Execute the approved seven-file application once. Materialize the exact
   Gate-3 candidate bytes at the seven live paths using repository-approved
   patch editing, verify all seven intermediate R3-A SHAs, then from repository
   root run the required `git apply --unidiff-zero --check` and one
   `git apply --unidiff-zero` of `Gate_5_Application_Append.diff`.
3. Require all seven live SHAs to equal R4-A exactly. If any application-stage
   identity mismatches, restore all seven revision-1.2 bytes and stop. Never
   execute the application again.
4. Produce `Gate_5_Application_Record.md` with the complete before→after table,
   R4-A/R4-B and R4-record references, fresh validator result, Git effect
   `TBD`, and R4-C pointer non-write.
5. Execute and record `Propagation_Plan.md` §6 items 1–6 exactly as the steer
   restates them. The applied-state Gate-3 equivalent comes from the Gate-5
   package validator; do not run the protected Phase-0c validator directly
   against the live applied state.
6. Put the post-application scoped AUDIT_DECOMP backcheck only in
   `Evidence/AUDIT_DECOMP_POST_GATE5/`; preserve the Gate-1 baseline. Record
   expected topology and all zero-gap counts, file/line citations for all ten
   holds, diff containment, and the derivative disposition table.
7. Append the four prescribed decision-log entries with R4-A/R4-B/R4-C
   verbatim and the application-record SHA; update Gate 5 to
   `EXECUTED_AWAITING_OWNER_CONFIRMATION`.
8. Update the four-state SCA handoff to
   `AWAITING_OWNER_GATE_5_CONFIRMATION` with all prescribed blockers.
9. If a closure-lane finding remains after bounded evidence/record repair, do
   not revert the live application silently. Record the finding in the
   application record and handoff, stop, and return it for the owner.

## Acceptance checks

- seven live SHAs equal R4-A exactly;
- Gate-5 validator applied-state PASS, zero failures, with embedded 98/98;
- post-Gate-5 AUDIT_DECOMP counts exactly match the steer;
- the append and every approved SCA byte remain unchanged;
- `_LATEST.md`, all `_STATUS.md`, Task Management, all live folder paths, and
  every forbidden surface remain unchanged;
- only authorized content and control-return paths changed;
- `RETURN.md` records hashes, check output, changed paths, derivative state,
  and blockers.

Evidence and record writes may be repaired without repeating application. If
any needed write is outside scope, stop and return the blocker.
