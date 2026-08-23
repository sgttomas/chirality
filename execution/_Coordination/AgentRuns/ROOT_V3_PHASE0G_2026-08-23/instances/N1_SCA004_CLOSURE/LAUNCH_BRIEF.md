# Sealed launch brief — N1 SCA-004 closure

Instance: `N1_SCA004_CLOSURE`
Agent type: `2 — bounded ephemeral generalist`
Parent: `HELP_HUMAN`
Role entry: `SCOPE_CHANGE record specialist`
Role enforcement: `instruction-asserted`
Delegation: forbidden; do not spawn or message another agent
Canonical root: `/Users/ryan/.codex/worktrees/0b6e/chirality`
Branch: `codex/root-v3-phase0g-2026-08-23`
Accepted branch basis: `origin/main@d279bad6a5903678822ac8b3b85aec76f7a0cfed`

## Objective

Execute exactly N1 in the published Phase-0g steer: transcribe R6, replace the
live SCA pointer with the approved candidate block plus exactly three named
fills, backfill only the authorized Git-effect/reference slots, and close the
SCA handoff while leaving later propagation pending.

## Authority and required reading

Read in full before acting:

- `AGENTS.md`
- `agents/AGENT_SCOPE_CHANGE.md`
- `plans/steers/chirality_app_v3_phase0g_steer_root_2026-08-23.md`
- `plans/steers/chirality_app_v3_root_ruling_record_r6_2026-08-23.md`
- `plans/steers/chirality_app_v3_root_ruling_record_r4_2026-08-23.md`
- `plans/steers/chirality_app_v3_root_ruling_record_r5_2026-08-23.md`
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_5_Pointer_Candidate.md`
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_5_Application_Record.md`
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Decision_Log.md`
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Handoff_State.md`
- this brief and the parent plan/graph

The owner's supplied clarification is binding: the Gate-5 confirmation
reference fill is R6-A with record SHA-256
`4e39bf6df909d63b910db3d953db720d2bceb2d27f26ce7454c93551f2a822de`.

## Exact write targets

Project-content targets, exactly:

- `execution/_ScopeChange/_LATEST.md`
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Decision_Log.md`
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Handoff_State.md`
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_5_Application_Record.md`

Runtime evidence owned by this instance:

- `execution/_Coordination/AgentRuns/ROOT_V3_PHASE0G_2026-08-23/instances/N1_SCA004_CLOSURE/RETURN.md`
- `execution/_Coordination/AgentRuns/ROOT_V3_PHASE0G_2026-08-23/instances/N1_SCA004_CLOSURE/STATUS.json`

Nothing else is writable. The seven live decomposition files and all other
SCA-004 files are read-only.

## Pre-write fence

Reverify every SHA and condition in the steer basis gate. Rerun
`validate_gate5_applied.py` to a temporary output path and require PASS 65/65,
zero failures, while leaving committed `Gate_5_Applied_Validation.json`
byte-identical. Require the governed checkout to contain only this run's
control-plane additions before substantive writes. Any drift stops.

## Required work

1. Extract the fenced markdown replacement block from
   `Gate_5_Pointer_Candidate.md` and make it the complete live `_LATEST.md`,
   changing exactly these three candidate slots and no other bytes:
   - application-append approval reference: R4-A, R4 record SHA-256
     `5916aa599bf5953324636b8c5e0b0a5e2b9e6a793fd6dd9b1cac1c7e19e0755a`;
   - Gate-5 confirmation reference: R6-A, R6 record SHA-256
     `4e39bf6df909d63b910db3d953db720d2bceb2d27f26ce7454c93551f2a822de`;
   - Git effect: PR #633 merge
     `6d4438d8d3a580b65d6d50ad497dadfe07f177f2`, content
     `4ad3fea7ef9e397852913c08e533e1846e264134`, PR head
     `17d3bc2af666005676a517c0a37e5ebd7b3a6614`.
   Produce a deterministic diff proof against the fenced block for RETURN.
2. In `Gate_5_Application_Record.md`, fill only the `TBD` Git-effect and
   reference slots authorized by R6-C. Use the exact recorded Git chain and
   references R4-A, R4-B, R5-A, R6-A. Do not infer anything.
3. In `Decision_Log.md`, append `G5-CONFIRMED-001` with R6-A verbatim,
   `G5-POINTER-APPLIED-001` with R6-B verbatim and the final pointer SHA-256,
   and `G5-BACKFILL-001` with R6-C verbatim. Set Gate 5 to
   `CONFIRMED_BY_OWNER_R6-A` and fill only its R6-C-authorized TBD slots.
4. In `Handoff_State.md`, use the four-state form and status
   `CLOSED_CONFIRMED_PROPAGATION_PENDING`. List later propagation acts,
   TM-ROOT-106/122 as unchanged G1 blockers, and all ten holds as held.
5. Write a complete RETURN and terminal STATUS with the exact changed paths,
   pointer proof, one-line backfill diffs, hashes, validation, protected-state
   parity, remaining work, and blockers.

Use `apply_patch` for governed file edits. Do not commit, fetch, merge,
rebase, push, open a PR, or modify closeout receipts/handoff outside the exact
instance outputs.

## Acceptance contract

- Final pointer differs from the candidate fenced block only at the three
  named slots.
- Application record changes only authorized slot fills.
- Decision log preserves all prior bytes except the named status/slot fills
  and appended exact R6 entries.
- SCA handoff is `CLOSED_CONFIRMED_PROPAGATION_PENDING` and faithfully names
  deferred propagation and blockers.
- Applied validator passes 65/65 with committed validation JSON unchanged.
- Seven live decomposition files and every protected SCA file remain
  byte-identical.
- Fresh review can return zero actionable findings.
