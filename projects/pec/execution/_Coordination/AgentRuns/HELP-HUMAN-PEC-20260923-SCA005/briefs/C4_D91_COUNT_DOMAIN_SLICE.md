# Brief C4 — D-PEC-91 A-53 COUNT-domain repair slice (WORKING_ITEMS)

Parent: HELP_HUMAN run `HELP-HUMAN-PEC-20260923-SCA005`. Role: WORKING_ITEMS (Type 1), owning PKG-01 / DEL-01-03 only. Model steer: `claude-opus-5-5`, high reasoning, for you and your children (D-PEC-91 ruling).

## Purpose

Execute the owner-ruled D-PEC-91 option **A-53** (R15, R16, R17 with bound `2**53 - 1`) exactly as specified, and return a merge-ready PR with independent verification.

## Accepted basis (read first, in this order)

1. Root `AGENTS.md`; `projects/pec/AGENTS.md`; `agents/AGENT_WORKING_ITEMS.md`.
2. `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-91_RULING_2026-09-25.md` and the proposal it selects, `D-PEC-91_del_01_03_count_domain_encoding_residual_proposal_2026-09-25.md` at SHA-256 `5c044b095621bfb098bb3d4e69d55b5a0594a3c73322d58b440a767e2d2413ec`. The proposal's per-repair table, R15 exact rule, R17 documentation edits D1–D10, finite verification, administrative grant, rollback and limits are your specification, **with the ruling's A-53 substitutions**: `_MAX_COUNT = 2**53 - 1` (update the constant's comment to cite the JSON safe-integer range, RFC 8259, not SQLite INTEGER); `2**53 - 1` admitted and rendered `"9007199254740991"`; `2**53` in place of `2**63` in `invalid_values`; the over-bound list `(2**53, 2**63, 10**639, 10**5000)`; the D1/D2/D5 text uses `2**53 - 1` with the B2 rationale (design for the limiting component: JSON consumers that parse numbers as doubles). Mutations M2, M3 and M6 apply relative to that bound. Do not enlarge the specification.
3. The ruling's clarifications apply, including the A-53 consequential wording: `2**53 - 1` has 16 decimal digits (not 19) wherever D1 and R15 state a digit count; the R15 comment cites the JSON safe-integer range; D10 states the bound as `2**53 - 1`; M6 (widening to `10**4000`) is unchanged. N-2..N-5 also apply: in particular record, per N-4, whether R16's read-only block actually ran (permissions enforced) in each run; the verifier must run it where it does.
4. Prior slice records for context (immutable): DEL-01-03 `_run_records/P1_STORE_GUARD_03/` and the L-2a review `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/returns/L2A_REVIEW_DEL-01-03.md`.
5. Methods: the bundled workflow `chirality-root:bundled:workflow:software-bounded-implementation` (`workflows/software-bounded-implementation/WORKFLOW.md`) for the author; `.agents/skills/software-code-review/SKILL.md` for the verifier.

## Preconditions (stop and return if any fails)

- The ruling and its register row are on fetched `origin/main`.
- Fresh preimage verification: the four opened paths and the four unopened paths match the proposal's rollback table.
- Reliance-hold preflight: `python3 projects/pec/execution/_Scripts/pec_reliance_hold.py --register projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv --target <path> --operation dispatch-for-production` per opened path, and `rely-for-production` before fan-in.

## Write scope (exactly)

Product, relative to `projects/pec/`: the four paths in the ruling. Administrative: DEL-01-03 `_run_records/P1_STORE_GUARD_04/**` and one appended `MEMORY.md` entry. `_STATUS.md` is not touched.

Do NOT write: `v2/src/pec_v2/adapters/storage/sqlite_store.py`, `core/ports/store.py`, `adapters/storage/__init__.py`, `software-workflow.json`, `loop/LOOP_RECEIPTS.md`, the HELP_HUMAN `RUN.md`, `docs/STATUS.md`, `README.md`, `_DECISIONS/**`, `_ScopeChange/**`, any other deliverable, any Root/CI/sister path.

## Work graph

1. You: preconditions; branch `claude/pec-d91-count-domain-slice` from fresh `origin/main` (if the host refuses a new local branch, work on your worktree branch at the verified base and push to that remote branch name, recording it); create `P1_STORE_GUARD_04/` with `RUN.md` and `PREIMAGE.md`.
2. One TASK author (`subagent_type: pec-task`, `model: opus`): R15–R17 under the bundled workflow, with the A-53 substitutions. Extend existing tests in place; no new test ID; `TEST_TO_VERIFICATION` unchanged. Reproduce F-1 before and after at digit limits default, 640 and 0, under the run root (never under `v2/**`). Record commands, exit codes, interpreter path and version, and whether R16's block ran.
3. Run every check in the proposal's finite-verification table; store outputs under `P1_STORE_GUARD_04/checks/`. Run mutations M1–M7 (adjusted for A-53) and the nine D-PEC-89 mutations, and record that each is caught.
4. One fresh read-only TASK verifier (`subagent_type: pec-reviewer`, `model: opus`) under software-code-review: substantive admissibility, not only green tests; independent F-1 reproduction on preimage and candidate; boundary cases at `2**53 - 1`, `2**53`, `True`, `int` subclasses, and oversized values at the three digit limits; confirm R16's block runs where permissions are enforced; confirm the documentation states the bound, its JSON rationale and the encoding residual truthfully and keeps the threat boundary. Defects return to the author; the verifier does not repair. Repeat until no blocking finding. Save each verdict under the run root.
5. Containment (`git diff --name-only origin/main`): only the four paths plus the run root and `MEMORY.md`. Whitespace check. No `__pycache__` staged. Delete any large scratch exports you created.
6. `MEMORY.md` entry.
7. Commit (end messages with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`), push, open the PR against `main` (end the body with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`). Do not merge.

## Relay note

If your children's completion notices reach HELP_HUMAN rather than you, HELP_HUMAN relays each verbatim; wait for the relay rather than reconstructing a return, and save relayed returns with a header saying so.

## Return

PR URL and head SHA; per-repair status with proving test IDs; F-1 before/after results; check IDs with exit codes; mutation results; whether R16's block ran; verifier verdicts and cycles; containment output; any discrepancy routed rather than worked around; delegation record.

## Limits

No CHECKING, ISSUED or artifact acceptance, and do not ask the owner about CHECKING (the owner reserves it). No SOW, field-class, failure-code, store location/engine/DDL, port, workflow-configuration or hosted-CI change.
