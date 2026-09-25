# Brief C3 — D-PEC-89 A exact-type closure slice (WORKING_ITEMS)

Parent: HELP_HUMAN run `HELP-HUMAN-PEC-20260923-SCA005`. Role: WORKING_ITEMS (Type 1), owning PKG-01 / DEL-01-03 only. Model steer: `claude-opus-5-5`, high reasoning, for you and your children (D-PEC-89 ruling).

## Purpose

Execute the owner-ruled D-PEC-89 option A (R9–R14) exactly as specified, and return a merge-ready PR with independent verification.

## Accepted basis (read first, in this order)

1. Root `AGENTS.md`; `projects/pec/AGENTS.md`; `agents/AGENT_WORKING_ITEMS.md`.
2. `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-89_RULING_2026-09-24.md` and the proposal it selects, `D-PEC-89_del_01_03_exact_type_closure_proposal_2026-09-24.md` at SHA-256 `962a7879788e75cac41bc73c8320eb2be11b65fe104fcbb163fff892b49f8a73`. The proposal's per-repair table, R9/R10 exact rule, E-2 exact wrapping, R14 exact documentation text, finite verification, administrative grant, rollback and limits are your specification. Do not enlarge them.
3. The D-PEC-87 slice records for context (immutable): DEL-01-03 `_run_records/P1_STORE_GUARD_02/`, especially `VERIFIER_VERDICT_01.md`–`_03.md` and `AUTHOR_RETURN_02.md`.
4. Methods: the bundled workflow `chirality-root:bundled:workflow:software-bounded-implementation` (`workflows/software-bounded-implementation/WORKFLOW.md`) for the author; `.agents/skills/software-code-review/SKILL.md` for the verifier.

## Preconditions (stop and return if any fails)

- The ruling and its register row are on fetched `origin/main`.
- Fresh preimage verification: the five opened paths and the three unopened paths match the proposal's rollback table.
- Reliance-hold preflight: `python3 projects/pec/execution/_Scripts/pec_reliance_hold.py --register projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv --target <path> --operation dispatch-for-production` per opened path, and `rely-for-production` before fan-in.

## Write scope (exactly)

Product, relative to `projects/pec/`: the five paths in the ruling. Administrative: DEL-01-03 `_run_records/P1_STORE_GUARD_03/**` and one appended `MEMORY.md` entry. `_STATUS.md` is not touched.

Do NOT write: `loop/LOOP_RECEIPTS.md`, the HELP_HUMAN `RUN.md`, `docs/STATUS.md`, `README.md`, `_DECISIONS/**`, `_ScopeChange/**`, `software-workflow.json`, `core/ports/store.py`, `adapters/storage/__init__.py`, any other deliverable, any Root/CI/sister path.

## Work graph

1. You: preconditions; branch `claude/pec-d89-exact-type-slice` from fresh `origin/main` (if the host refuses a new local branch, work on your worktree branch at the verified base and push to that remote branch name, recording it); create `P1_STORE_GUARD_03/` with `RUN.md` and `PREIMAGE.md`.
2. One TASK author (`subagent_type: pec-task`, `model: opus`): R9–R14 under the bundled workflow. Extend existing tests in place; no new test ID; `TEST_TO_VERIFICATION` unchanged; R10 changes exactly the two `test_ver_005` expected tuples the proposal names. Replicate the proposal's probe battery under the run root (never under `v2/**`) and record per-case outcomes. Record commands, exit codes, interpreter path and version.
3. Run every check in the proposal's finite-verification table; store outputs under `P1_STORE_GUARD_03/checks/`. Run the proposal's mutation list and record that each is caught.
4. One fresh read-only TASK verifier (`subagent_type: pec-reviewer`, `model: opus`) under software-code-review: substantive admissibility, not only green tests; independent probes of E-1, C2-2, LEN-1, TUP-1, DUP-1, SPF-1, E-3 and E-2 on the candidate; confirm the documentation states closure truthfully and keeps the C2-4 threat boundary. Defects return to the author; the verifier does not repair. Repeat until no blocking finding. Save each verdict under the run root.
5. Containment (`git diff --name-only origin/main`): only the five paths plus the run root and `MEMORY.md`. Whitespace check. No `__pycache__` staged.
6. `MEMORY.md` entry.
7. Commit (end messages with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`), push, open the PR against `main` (end the body with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`). Do not merge.

## Relay note

In this host, your children's completion notices reach HELP_HUMAN, not you. HELP_HUMAN relays each verbatim. Wait for the relay rather than reconstructing a return; save relayed returns with a header saying so.

## Return

PR URL and head SHA; per-repair status with proving test IDs; probe battery outcomes; check IDs with exit codes; mutation results; verifier verdicts and cycles; containment output; any discrepancy routed rather than worked around; delegation record.

## Limits

No CHECKING, ISSUED or artifact acceptance, and do not ask the owner about CHECKING (the owner reserves it). No SOW, field-class, store location/engine, port, workflow-configuration or hosted-CI change.
