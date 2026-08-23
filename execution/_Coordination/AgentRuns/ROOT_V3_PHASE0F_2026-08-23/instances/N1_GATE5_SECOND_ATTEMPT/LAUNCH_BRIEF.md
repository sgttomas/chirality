# Sealed launch brief — N1 Gate-5 second attempt

Instance: `N1_GATE5_SECOND_ATTEMPT`
Agent type: `2 — bounded ephemeral generalist`
Parent: `HELP_HUMAN`
Role entry: `SCOPE_CHANGE execution specialist`
Role enforcement: `instruction-asserted`
Delegation: forbidden; do not spawn or message another agent
Canonical root: `/Users/ryan/.codex/worktrees/0b6e/chirality`
Branch: `codex/root-v3-phase0f-2026-08-23`
Accepted branch basis: `origin/main@119e08647afdb380704ff660fb32d714d7bd1dad`

## Objective

Execute exactly the single N1 in the Phase-0f steer. Build the applied-state
validator and conduct the full scratch rehearsal without touching the seven
governed live files. Proceed to the one live Gate-5 act only when Stage A
passes its exact three-part gate. Then record the application and closure
lane. Unlimited repair applies to Stage-A artifacts and evidence/record writes;
the live Stage-B act is permitted once.

## Authority and required reading

Before acting, read in full:

- `AGENTS.md`
- `agents/AGENT_SCOPE_CHANGE.md`
- `plans/steers/chirality_app_v3_phase0f_steer_root_2026-08-23.md`
- `plans/steers/chirality_app_v3_root_ruling_record_r5_2026-08-23.md`
- `plans/steers/chirality_app_v3_root_ruling_record_r4_2026-08-23.md`
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_5_Brief.md`
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Propagation_Plan.md`
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_5_Applied_Preview.md`
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_5_Slot_Inventory.md`
- `execution/_Coordination/LOOP_RECEIPTS.md` Receipt 118
- this brief and the parent run plan/graph

R5-A condition (1), verbatim and controlling for the seven live writes:

> (1) Materialization method, mandatory: byte copy of the seven exact
>     `Gate_3_Candidate/` files to their live paths by shell copy
>     (`/bin/cp`) or by `git show <basis>:<candidate path>` redirected to the
>     live path; then `git apply --unidiff-zero --check` and one
>     `git apply --unidiff-zero` of `Gate_5_Application_Append.diff` from the
>     repository root. Patch editing, editor tools, `apply_patch`, or any
>     re-expression of the approved diffs is forbidden for these writes.

For avoidance of doubt: patch editing, editor tools, `apply_patch`, Python
file rewriting, Perl/Sed/Awk rewriting, or any re-expression of either
approved diff is forbidden for the seven live decomposition writes. Use only
`/bin/cp` for candidate materialization and the exact `git apply` commands for
the append. You must have shell access to `/bin/cp`, `shasum`, and `git apply`;
if any is unavailable, stop before any write and return the blocker.

## Exact write targets

SCA-004 additions/updates only:

- `execution/_ScopeChange/SCA-004_2026-08-22_1749/validate_gate5_applied.py`
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_5_Rehearsal_Record.md`
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_5_Applied_Validation.json`
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_5_Application_Record.md`
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Evidence/AUDIT_DECOMP_POST_GATE5/**`
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Decision_Log.md`
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Handoff_State.md`

Seven live files, writable only during Stage B by the exact method above:

- `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`
- `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`
- `execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv`
- `execution/_Decomposition/chirality_root_objective_register_v1_0.csv`
- `execution/_Decomposition/chirality_root_prd_coverage_forward_v1_0.csv`
- `execution/_Decomposition/chirality_root_trace_reverse_v1_0.csv`
- `execution/_Decomposition/chirality_root_coverage_telemetry_v1_0.md`

Runtime evidence owned by this instance:

- `execution/_Coordination/AgentRuns/ROOT_V3_PHASE0F_2026-08-23/instances/N1_GATE5_SECOND_ATTEMPT/RETURN.md`
- `execution/_Coordination/AgentRuns/ROOT_V3_PHASE0F_2026-08-23/instances/N1_GATE5_SECOND_ATTEMPT/STATUS.json`

Nothing else is writable. Approved/published SCA-004 inputs are read-only.

## Pre-write fence

Reverify every SHA and condition in the steer basis gate. Run the published
`validate_gate5_package.py` fresh and require PASS 64/64, zero failures, with
`Gate_5_Validation.json` still SHA-256
`4831fb2757bfcdeb2faa0dff51a15d4f04ec68d4c9716928a36f1ea8844df966`.
Require the governed checkout to be clean except for this run's control-plane
records. Any drift stops before substantive writes.

## Stage A — validator and rehearsal; no live write

1. Create deterministic `validate_gate5_applied.py` and its JSON output as
   specified by the steer. It must support validation of an arbitrary repo
   root so it can run in scratch and in the governed checkout. It must not rely
   on pre-application-only assertions such as `live_basis_untouched` or
   `candidate_ids_absent_from_live_register`.
2. Create a detached scratch worktree outside the governed checkout. Record
   the exact scratch creation command. Copy the validator into the scratch SCA
   path if its uncommitted source is not present there; that copy is scratch
   only and does not widen the governed write set.
3. From the scratch root, `/bin/cp` each of the seven exact Gate-3 candidate
   files to its matching live path. Hash all seven and require the exact R3-A
   identities.
4. From the scratch root, run exactly:
   `git apply --unidiff-zero --check execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_5_Application_Append.diff`
   then exactly one:
   `git apply --unidiff-zero execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_5_Application_Append.diff`.
5. Hash all seven scratch live files and require the exact R4-A identities.
6. Run the applied validator against the scratch and require PASS, zero
   failures. Record its check count and output.
7. Remove the scratch worktree cleanly. Record every command and every
   observed intermediate/final hash in `Gate_5_Rehearsal_Record.md`.
8. Rehash the governed live files and require all seven still equal revision
   1.2. Record that fact.

The Stage-A gate is `R3-A 7/7 + R4-A 7/7 + applied validator PASS with zero
failures`. If it does not pass, do not write any live decomposition file.
Record the blocker in the rehearsal record and SCA handoff, write RETURN and
STATUS, then stop.

## Stage B — one live act

Only after the Stage-A gate passes:

1. From the governed repository root, run seven explicit `/bin/cp` commands
   from `Gate_3_Candidate/` to the matching live paths. Hash all seven; require
   R3-A 7/7. Any mismatch: restore all seven revision-1.2 files with the
   authorized `git checkout -- execution/_Decomposition/`, verify every 1.2
   identity, record, and stop without retry.
2. From the governed repository root, run the same exact `git apply
   --unidiff-zero --check` command and then exactly one `git apply
   --unidiff-zero` command named in Stage A. Hash all seven; require R4-A 7/7.
   Any mismatch: restore and verify revision 1.2, record, and stop without
   retry.
3. Write `Gate_5_Application_Record.md` with the complete before→after table,
   R4-A/R4-B/R5-A references and both ruling-record SHAs, exact commands,
   rehearsal-record SHA, applied-validator result/check count, Git-effect
   `TBD`, and unchanged `_LATEST.md` under R4-C.
4. Execute and record `Propagation_Plan.md` §6 items 1–6 exactly as the steer
   restates them. Produce the scoped `AUDIT_DECOMP` post-Gate5 evidence in the
   new evidence folder without overwriting the Gate-1 baseline. Cite every
   one of the ten `HELD_UNAVAILABLE` bindings by file and line.
5. Update Decision Log and SCA Handoff exactly as the steer specifies. For the
   R4-A, R4-B, R4-C, and R5-A verbatim entries, copy the exact recorded-form
   text from the published ruling records without paraphrase.
6. Write a complete RETURN and terminal STATUS. Include exact changed paths,
   protected paths verified, all hashes/check counts, derivative disposition,
   blockers, and rerun requirements.

After a successful live identity fence, any closure-lane failure is recorded
and returned; never silently revert the applied files. Do not commit, fetch,
merge, rebase, push, open a PR, or touch `_LATEST.md`.

## Acceptance contract

- Stage A record proves R3-A 7/7, R4-A 7/7, validator PASS/zero failures, and
  governed live revision 1.2 throughout rehearsal.
- Stage B produces all seven exact R4-A live identities.
- Applied validator passes on the governed live state with zero failures.
- Post-Gate5 audit evidence reports 53 deliverables, PKG-02=12, PKG-04=11,
  packages=6, scope items=104, objectives=7, zero unmapped IN items, zero
  unmapped objectives, and zero untraced reverse units.
- Only sealed write targets and own runtime evidence change.
- `_LATEST.md`, every `_STATUS.md`, live folders, Task Management, and all
  other protected paths remain byte-identical to the branch basis.
- Final state is `AWAITING_OWNER_GATE_5_CONFIRMATION` if closure passes, or a
  precise evidence-backed blocker state if it does not.
