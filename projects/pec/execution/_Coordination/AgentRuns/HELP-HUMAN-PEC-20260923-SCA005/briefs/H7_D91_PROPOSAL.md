# Brief H7 — draft D-PEC-91 proposal: DEL-01-03 L-2a review repairs (read-only TASK)

Parent: HELP_HUMAN run `HELP-HUMAN-PEC-20260923-SCA005`, node H7. Role: TASK (Type 2). You do not delegate. Model steer: `claude-opus-5-5`, high reasoning.

## Basis

- Checkout `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5`, detached at `origin/main` `088fb7868d3246361e7209dd9276c6b0f8fc75d9`. Do not change it. Report `git rev-parse HEAD`.
- The L-2a review report is at `<scratchpad>/h7/L2A_REVIEW_REPORT.md` (path given in the dispatch message; the only other scratchpad file you may read besides this brief and `<scratchpad>/l2a_review/**`, which holds the reviewer's probes). Findings F-1..F-12. HELP_HUMAN correction: F-7's statement that SCA-005 checkpoint 1 lacks owner acceptance is wrong; the owner accepted it on 2026-09-24 (`projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-005_GROUP-1_2026-09-24/`).
- Precedent format and rigour: `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-89_del_01_03_exact_type_closure_proposal_2026-09-24.md` and its ruling; `D-PEC-87_*` proposal and ruling. F-PEC-1 and `projects/pec/AGENTS.md` §"Write Scopes And Fences" require an owner-ruled packet for any `v2/**` write for DEL-01-03.
- Product basis: `projects/pec/docs/PRD.md` (PEC-K-10, §7.1/§7.2, PEC-SVC-005/006), DEL-01-03 `ScopeOfWork.md` (AC-004, AC-005, AC-009, REQ-005).

## Task

Draft a proposal `D-PEC-91` in the D-PEC-89 format that lets the owner rule one bounded repair slice for DEL-01-03:

1. **F-1 (MAJOR, required in the recommended option):** COUNT gets a finite, documented domain and out-of-domain values become a located `INVALID_VALUE` rejection; `guard()` and `admit_batch()` never raise on an exact-`int` COUNT regardless of `sys.get_int_max_str_digits()`. Choose and justify the bound from accepted sources and the store's storage type (read the adapter's schema); give alternatives if the sources do not settle it. Check whether any other field class has an unbounded conversion that can raise.
2. **F-2 (MINOR):** documentation of the deliberate-encoding residual (PATH, COUNT, identifiers) in `v2/docs/STORE_LIFECYCLE_AND_GUARD.md`, and a decision on a per-record field-count bound (recommend or not, with reasons).
3. **F-3, F-4 (carried D-PEC-89 N-1), F-11:** small doc and test repairs; include each only if it stays inside the same file set and is proportionate. Say which are in the recommended option.
4. F-5 stays Root/CI scope; F-6..F-10, F-12 optional or out, with a one-line disposition each.

For each repair: exact rule, file and function, proving test (extend existing tests in place; no new test IDs unless you justify it), and the mutation that the test must catch. Prototype the recommended repairs on a scratch copy exported with `git archive` into your own temporary directory (not the scratchpad, not the checkout); run the five registered checks there with `PYTHONDONTWRITEBYTECODE=1` and report exits and counts; run reproductions of F-1 before and after. Give options (recommended / narrower / defer), an exact product grant (paths, opened vs unopened with SHA-256 at `088fb7868`), administrative writes (run root `P1_STORE_GUARD_04/`, `MEMORY.md`), finite verification, rollback table, limits (no CHECKING, ISSUED or acceptance; the owner reserves CHECKING and it is not an owner gate), and the questions only the owner can answer. Run `python3 projects/pec/execution/_Scripts/pec_reliance_hold.py` with operation `exact-correction-preparation` on each opened path and record the result.

## Limits

Read-only on the repository: no edits in the checkout, no state-changing git, no PRs. Write only (a) the draft proposal to `<scratchpad>/h7/D-PEC-91_DRAFT.md` and (b) prototype files in your own temporary directory. Status line: `PROPOSAL / AWAITING_RULING`, prepared by TASK under HELP_HUMAN node H7.

## Return

A short return: the draft path and SHA-256, the recommended option in three lines, prototype check results, and anything the owner must decide.
