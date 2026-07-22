# Agent-Index Re-disposition Orchestration Plan

Status: `ACTIVE — PR-0 DRAFTED, AWAITING OWNER RULING`
Date: 2026-07-21
Parent: `HELP_HUMAN`
Run: `AGENT-INDEX-REDISPOSITION-20260721`

## Objective

Re-dispose four agent-index roles and the two control-loop artifact functions
per owner in-session direction 2026-07-21, recorded as D-GOV-18 items 1–8:
ORCHESTRATOR → PROJECT_SETUP (rename/narrow); EVALUATION → thin Agent 1 shell +
`evaluation-protocol` skill; control-loop Function 5 → HELPS_HUMANS (Function 3
stays); CHANGE slim-to-authority; REVIEW/SCOPE_CHANGE ruled SAFE; App Dev
couplings deferred to the App Dev loop. PR-0 (this run) drafts the D-GOV-18
ruling record and run scaffold only. It applies no role change.

## Selection authority

Owner in-session direction 2026-07-21 plus Agent 0 (HELP_HUMAN) cross-manager
judgment, pending the D-GOV-18 owner ruling. No item has operative effect
before that ruling and its SHA-binding. This plan records the intended
sequence; it is not itself authority to execute any item beyond PR-0's
drafting.

## Accepted basis

- Synchronized integration basis at run start:
  `main@0c066652cd527eb1559f715e914262d2bda42602`.
- Framing record: D-GOV-11 (runtime role ownership and Agent-2 construction
  forms).
- Proposed decision record: `D-GOV-18_agent_index_redisposition.md`
  (Status PROPOSED).

## Posture

Terminal fan-out/fan-in within each PR; supervised sequencing across PRs.
Each PR freezes sealed subagent briefs with disjoint write scopes, one
integration owner per stage, and CHANGE as the sole Git closeout. The human
approves every merge. PR-2 serializes behind closure of the App Dev in-flight
EVALUATION fan-in.

## Subagent dispatch policy

- Model: Opus, high reasoning effort.
- Sealed briefs; disjoint write scopes; one declared integration owner per
  stage.
- A Bash-bearing managed child requires explicit project-root read/write scope
  and becomes the serialized integration owner for its stage; package-parallel
  work uses bounded file tools.
- CHANGE is the sole Git closeout (commits only; no merge/push/rebase/reset
  outside its gate). The human approves every merge.

## PR sequence

- **PR-0** — D-GOV-18 ruling record + run scaffold (this run). No role change.
- **PR-1** — CHANGE slim (D-GOV-18 Item 4).
- **PR-2** — EVALUATION shell + `evaluation-protocol` skill (Item 2), gated on
  App Dev in-flight EVALUATION fan-in closure.
- **PR-3** — atomic ORCHESTRATOR → PROJECT_SETUP rename (Item 1), including the
  `REQUIRED_DELEGATION_EDGES` key rename in
  `tools/validation/validate_agent_instructions.py` and the `OWNER_WORKFLOWS`
  legacy-accepting shim in `tools/validation/validate_scc_resolution_case.py`.
- **PR-4** — control-loop Function 5 move to HELPS_HUMANS (Item 3).

## Terminal gate

`AGENT-INDEX-REDISPOSITION_RULED_IMPL_SEQUENCED`. Reached only after the owner
rules D-GOV-18, the ruling is SHA-bound, and PR-1..PR-4 land in sequence under
their per-PR gates with the human approving each merge. Approval of D-GOV-18 is
authority for the exact eight items; it is not this run's authority to execute
them before ruling.
