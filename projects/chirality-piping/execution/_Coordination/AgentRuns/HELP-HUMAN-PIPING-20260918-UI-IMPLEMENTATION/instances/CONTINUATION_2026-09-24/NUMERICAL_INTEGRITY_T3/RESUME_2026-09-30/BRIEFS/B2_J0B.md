# I105, J0b: `b2` absorbs U3 (the legacy pressure retirement)

TASK (Type 2), continued by WORKING_ITEMS for T3 (Agent 1), your return path. You do not delegate. `R/BRIEFS/B1_COMMON.md`'s host, Git and records rules apply, with WORKING_ITEMS in ROOT's place. Production code: a working merge with tests, and a short record.

## Why

J0a brought PR-B1 and PR-N into `b2` (`e582b61f9e`; RV123 confirmed). J0b brings U3: the legacy pressure contract retired product-wide (RR "Owner decisions: the legacy pressure contract is retired product-wide; …"; "U3 rulings on I110's pressure inventory: D-1 A, D-2 A1, D-3 held with M07"; "Owner decision: M07's flawed joint element, option A; U3 Stage 2 released"; "U3 Stage 2 rulings: …"; "U3, T2's outcome under the extended check; …"). U3 is PR #1168. Its package is `T/IMPLEMENTATION/U3/` (CHANGE_RECORD.md).

**Two steps, so the work starts before #1168 merges:**
1. **Now:** on a new branch `codex/piping-t3-b2-j0b-20261009`, cut from `b2` at `e582b61f9e` in a new worktree `WT/b2-j0b`, merge #1168's head (`37724dea27`, or the later head WORKING_ITEMS names). `b2` itself does not move.
2. **After #1168 merges:** merge main into the same branch. WORKING_ITEMS names the main commit; it adds only the merge commit and records-only main commits. Then WORKING_ITEMS fast-forwards `b2` to it.

## The task

1. **The merge.** A trial `git merge-tree` of `b2` `e582b61f9e` with `37724dea27` is textually clean. Nine files change on both sides: `PP/src/lib.rs`, `PP/src/retained_product.rs`, `PP/src/retained_product_tests.rs`, `PP/src/retained_memory_law_tests.rs`, `PP/tests/s11f_site_test.rs`, RE's `tests/retained_precision_contract.rs`, `P/tests/test_retained_precision_contract.py`, the TS `retainedPrecision.test.ts` and `previewService.ts`. Read each merged hunk on both sides and say in the record why the result is right.
   - **Do not change B2/B3 behaviour or U3's behaviour** to make a test pass. If the two need a design choice, stop and return.
2. **U3 against `b2`'s B3a drop** (I113, `0ef9a8ace9`). Both refuse the legacy label on the retained route. Check that they agree, and state each refusal's gate and code after the merge: PP's D1.3, and the three readers' G8 `INVOCATION_MISMATCH` with one shared shape. If U3 now refuses a document earlier than B3a's drop expected, the refusal test may need its expected gate updated. Explain each such change from U3's change record. Do not remove a refusal.
3. **T2's text in `b2`'s own files.** U3 corrects the `preview_formulation_basis` limitation [1] text and re-pins 12 source-block raws, the Rust pin's 2 constants and `generation.json` under ROOT's extended check. `b2` adds its own fixtures and pins (the combination, exact and derivative successors, `retained_precision_rv120_b3_inputs.json`, `retained_precision_prepared_*`, the B2-P and B3b-P pins in PP and the readers).
   - Search every file `b2` adds or changes, and every pin it holds, for the old text and for the old digests that U3 replaced. The old text is in `11a026b628`'s diff; the U3 package's `radius_sweep.txt` lists the old digests. WORKING_ITEMS' plain-text pre-search found the old text in no file that `b2` adds; confirm it, including escaped and hashed forms.
   - The two historical `rejected_stress_range` captures and `ORACLE.json` keep the old text as captured (RR "Owner decisions: T4 starts now; …", paragraph "U3, T2's re-pin check, option (a)").
   - U3 deletes three retired fixtures (`invented_mechanics_result.json` and its two `_precision_1_` forms). `b2` adds no reference to them; a test that still reads one is a stop.
   - Re-pin each hit under the same extended check: replace only the declared string; recompute `publication_sha256` and `receipt_sha256` by the product's rule; recompute any file hash that binds the file; the result must equal what the merged head's producer emits, byte for byte; all three readers verify it.
   - List every hit and every re-pin. Anything that moves for any other reason is a stop.
4. **Run, and compare test by test** with `b2` `e582b61f9e` and with #1168's head:
   - PP's suite (including rule 8, the s11f site test and the law tests), the runner, `result_export`, the PY and TS reader suites;
   - the readers' 07m and 07n census: 0 changes is required.

   Every outcome change is explained: U3 arriving (a retired path, a removed or rewritten test), a T2 re-pin, or a B3a refusal whose gate moved under item 2.
5. **Ask for the Linux CI dispatch** of the merged head in your return. WORKING_ITEMS pushes and dispatches. RV123 confirms J0b, as it did J0a.

## Host and records

- **The exclusive lock may be held** by #1168's exact-head DEC-025 until about 04:15Z. Cargo and slot jobs queue behind it; do the merge and the reading while they wait.
- Targets under `WT/targets/i105-j0b*`; scratch in `WT/scratch/i105_j0b/`. Cargo through `WT/tools/t3_cargo.sh`; other heavy jobs through `WT/tools/t3_slot.sh`. One heavy job of yours at a time. No DEC-025, no installs, and never signal another job.
- Commit on `codex/piping-t3-b2-j0b-20261009` with truthful messages. WORKING_ITEMS pushes.
- Records go in `R/I105/b2_j0b_01/` (RETURN.md, `_run_records/`, SHA256SUMS), placeholder paths only, written there directly (not in scratch). If the host refuses a record file, put its full content in your final message with its intended path; do not work around the refusal.
- Budget: 3–5 h.

End your turn with:
- the merge commits and the nine files' resolution;
- the U3 and B3a-drop agreement;
- the T2 hits and re-pins with their checks;
- the suite and census comparison;
- the dispatch request;
- any stop.
