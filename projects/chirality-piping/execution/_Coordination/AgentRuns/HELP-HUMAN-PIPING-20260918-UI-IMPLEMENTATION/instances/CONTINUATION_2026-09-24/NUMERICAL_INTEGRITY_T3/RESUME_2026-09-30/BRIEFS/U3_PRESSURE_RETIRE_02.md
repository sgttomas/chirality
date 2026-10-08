# I110, round 2: the legacy pressure retirement, Stage 1 (implementation)

TASK (Type 2), continued by WORKING_ITEMS for T3 (Agent 1), your return path. Host, Git and records rules are `R/BRIEFS/B1_COMMON.md`'s, with WORKING_ITEMS in ROOT's place. This is production code: working, tested code on a branch, with a short record.

## The basis

- Your round 1, `R/I110/pressure_retire_01/RETURN.md` (`d6edc387…`), §5 Stage 1, with ROOT's rulings on D-1 and D-2 as WORKING_ITEMS states them in the dispatch message. D-3 is (a), a no-op in this stage. D-4 reuses `PRESSURE_MODEL_REAUTHOR_REQUIRED`.
- **Branch** `codex/piping-t3-pressure-retire-20261008` in `WT/t3-pret`, cut from main `7eae707bb7` (PR-B1 merged). The base B for every comparison is that commit.

## Held (owner's M07 ruling pending; RR via WORKING_ITEMS)

Do not touch:
- the historical scope file;
- the joint bypass at `PP/src/preview_physics.rs:111-115`;
- O1–O4, `request_with_refused_joint` and the thread-local scope test;
- the browser's bundled precision-1 results and their fixtures;
- I111's G10 and G11.

The scope's pressure bypass stays, so O1–O4 run unchanged. Stage 2 waits for the ruling.

## The task

1. **Implement Stage 1** as your §5 lists it:
   - the refusals and their texts;
   - pressure-primitive authoring removed from the app's load-case manager and the operation applier, and the panel text;
   - the deleted pressure-only oracles;
   - the strip-instead-of-zero fixture and runner helpers;
   - the edited tests;
   - one refusal test per route (ordinary, retained, runner), per reader (RS, PY, TS: a label case pinned as G8 `INVOCATION_MISMATCH`), and for the app and the applier;
   - the docs.

   Commit in reviewable steps on the branch, with product files only and truthful messages.
2. **The evidence, against B, on this host, in fresh targets:**
   - per-test outcomes: the 40 manifests (CI's numerical profile, `WT/scratch/calib/run_suites_nff.sh` through `WT/tools/t3_cargo.sh`), src-tauri, `P/tests` pytest and vitest. List every removed, edited, added or changed outcome; anything not in the plan is a stop;
   - byte-equal ordinary envelopes and RE exports, in both modes, for the 48 committed exact documents and the 214 pressure-free implicit documents, plus B1's 32-document corpus through W1 with B1's pins unchanged.
3. **Linux:** ask for a CI dispatch of the branch head in your return.

**Stop and return** if a disposition needs a held item, a re-pin of an exact-contract value, a change to B0, B2-C or B3-D, or a weakened check.

## Records and return

`R/I110/pressure_retire_02/` (RETURN.md, `_run_records/`, SHA256SUMS), placeholder paths only. If the host refuses a record file, put its full content in your final message with the intended path; do not work around the refusal.

End your turn with:
- the branch head and the commit list;
- the outcome diff's counts;
- the byte-equality result per document set;
- the dispatch request;
- any stop.
