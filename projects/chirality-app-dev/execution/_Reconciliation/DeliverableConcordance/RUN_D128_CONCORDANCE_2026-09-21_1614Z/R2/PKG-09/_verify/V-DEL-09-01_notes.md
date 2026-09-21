# V-DEL-09-01 verifier notes (DEL-09-01)

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a (REMAINING_WORK) | 1 | 1 | 0 | 0 |
| a30 (other non-ALIGNED) | 9 | 9 | 0 | 0 |
| b (ALIGNED sample) | 3 | 3 | 0 | 0 |
| c (reverse PARTIAL) | 2 | 2 | 0 | 0 |
| e (errata) | 0 | 0 | 0 | 0 |
| **Total** | **15** | **15** | **0** | **0** |

There is no errata file. The ledger was briefed with Addenda 5, 6 and 8, R4-Q4, R4-Q5 and the manager's build/CI reach note. Addendum 9 (R4-Q6) arrived before sealing, and no selected row turns on it.

## (ii) Patterns and observations

1. **REF-006 MATCH restatements are handled consistently.** CLM-001, CLM-004 (bullet) and CLM-026 take STALE_SPECIFICATION with `SEE:DEL-09-01#REGISTER-1`, which follows tie-break rule 3. The hash recompute at the frozen tree (`17ca3f3c…`) matches the pack's `Match=NO`. `_DEPENDENCIES.md` also restates "REF-006 is MATCH" in its P40 annotation. That repeat falls outside this selection.
2. **Rows near the out-of-root boundary rely on in-root evidence.** CLM-003 rests on the ruled D-APP-56 P37/P45 amendment as transcribed in CLM-013 (MR-11), not on the repo-root workflow. The in-root `.github/workflows/harness-premerge.yml`, last changed 2026-05-18, still uploads `harness-section8-summary` and matches the old SoW row. What CI actually does can only be settled at the repo-root workflow, and the row's Notes say so.
3. **REM-1 was verified at its source.** 13 first-parent merges after `e2f8317da` touch the named trigger surfaces, including 19bca4930 (A2). The rerun method starts `main.js --runtime-daemon`, and `main.ts` has no such entry. The harness port expects a `project-*.token` basename, while `main.ts` sets `client-token`. MechanicallyUnblocked `NO` is correct because DEP-09-01-008 is ACTIVE PREREQUISITE with status TBD. None of the files cited on REM-1, STATE-1 or CLM-003 fall in the TOUCHED_PATHS ranges. Line 33 of `app-owned-composition.ts` blames to fca60696d.
4. **Readings considered but not taken:**
   - REGISTER-2: rule 1 could apply to "no … edges have been extracted yet". Rule 2(b) names TBD placeholders and lagging counts explicitly, so it decides the row.
   - STATE-1: AUTHORITY_CONFLICT could apply between SCA-APP-001 and D-GOV-43. It does not, because the amended App SPEC §25.6 states that Codex is the sole engine, and the DIRECTIVE §0 order resolves in its favour.
   - CLM-018.5: the grading key 4b proof bar could apply. The row is a check expectation for a generated, gitignored summary, not a claim that a recorded release run proved anything, so the bar does not apply.

## (iii) Effort

About 20 file reads and greps, all in the frozen tree and the run-folder inputs, plus read-only `git log` and `blame -L` against the frozen tree. The context budget was comfortable. No tests, builds or installs were run.
