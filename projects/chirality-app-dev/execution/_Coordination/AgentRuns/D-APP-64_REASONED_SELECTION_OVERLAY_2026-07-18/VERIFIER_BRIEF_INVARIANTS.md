# Sealed Verifier Brief — V2 Invariant Matrix I1–I12 (refutation-only)

- **Parent:** HELP_HUMAN (Agent 0), RunID `D-APP-64_REASONED_SELECTION_OVERLAY_2026-07-18`
- **Verifier posture:** fresh context; no shared authorship; read-only except
  the single return file; sole deliverable `COMMIT-SAFE` or `BLOCK`.
- **Write scope:** exactly
  `projects/chirality-app-dev/execution/_Coordination/AgentRuns/D-APP-64_REASONED_SELECTION_OVERLAY_2026-07-18/RETURN_INVARIANTS_1.md`.

## Task

Check every row of `CLOSED_INVARIANT_MATRIX.md` (this run directory) against
the CURRENT STAGED TRANCHE (pre-commit). Derive all evidence with your own
commands — `git diff --cached`, `git ls-tree`, `git ls-files`, independent
span extraction and SHA-256 hashing — never trusting run records, briefs, or
returns as proof of the facts they assert.

State interpretation at this check time (pre-commit; the receipt append and
final staging verification run after you):

- I1: the active path exists in worktree AND index at check time — that is
  the choreography's declared final window; the invariant you check is that
  it is absent from `HEAD`.
- I4, and the post-commit halves of I7: commit-dependent — verify they are
  recorded staged-empty, then mark `PENDING-COMMIT`, not FAIL.
- I7 staged-scope half: the staged file list must contain only manifest items
  1–4 and 6; manifest item 5 (`LOOP_RECEIPTS.md` Receipt-70) is not yet
  staged at your check time by design — flag anything ELSE as FAIL. Also
  verify pre-commit `HEAD` discovery (bytewise-last `WORKPLAN_*.md` among
  `HEAD` entries under `projects/chirality-app-dev/loop/`) still selects
  `WORKPLAN_2026-07-18_app_dev_loop.md`.
- I12: packet §10 must show V1 filled (its return exists) and V2/V3 and the
  closeout cell still staged-empty; your own verdict must not appear anywhere
  before you write it.
- I8 cross-project half: the piping record for comparison is
  `/Users/ryan/ai-env/projects/chirality-session-20260718/projects/chirality-piping/execution/_Coordination/_DECISIONS/D-50_shared_block_adoption.md`
  (read-only; confirm its recorded block hash equals the app-dev
  recomputation).

Any invariant that fails outright, any staged path outside the manifest
scope, or any staged-empty violation is `BLOCK`. Default to `BLOCK` if
uncertain.

## Return format

`RETURN_INVARIANTS_1.md`: verdict line first, then one line per invariant
I1–I12 (`PASS` / `PENDING-COMMIT` / `FAIL`) with the evidence commands and
observed values.
