# B2's readers: combination coverage in RS, PY and TS

TASK (Type 2), dispatched by WORKING_ITEMS for T3 (Agent 1), your return path. You do not delegate. **You are a fresh instance.** `R/BRIEFS/B1_COMMON.md`'s host, Git and records rules apply, with WORKING_ITEMS in ROOT's place. **Production code first:** working, tested reader code on your lane branch, with a short record.

**Owners, one lane each, in parallel.** The dispatch message names your ID and lane:
- RS: `RE/src/retained_precision.rs` and RE's tests;
- PY: `P/core/analysis_runs/retained_precision.py` and `P/tests/`;
- TS: `apps/desktop/src/features/results/retainedPrecision.ts`, its tests, and the T6S tests below.

Each lane is cut by WORKING_ITEMS from `b2` after J0b. The dispatch message names the head, your worktree and your branch. That head carries B2-P's producer (lane P, RV123 confirmed), the kernel (lane K), the admission (lane A), B3's readers (RV120 confirmed), PR-B1, PR-N and U3.

## Why

All three readers still refuse any model combination at G8 (`INVOCATION_MISMATCH`). B2's producer now emits combination receipts. PLAN §1.2.5 and REVISION_01's J6 put combination coverage in all three readers before SC2's 07o, the pin updates and the J7 freeze. ROOT confirmed this route (2026-10-09).

## The specification

- **I93's PLAN** §1.2.5 (the gate table), with REVISION_01 (`R/I93/b2b3_plan_01/`).
- **B2-C, final for J1** (`R/I97/b2_c_01/`):
  - CONTRACT §5 (R-COMB-1), §6 (SCHEMA's `$defs`), §8 (G0 per N-12 and decision 31), §10.1 (every new check, by gate, in identical order and with identical codes in all three readers), §10.3 (the mutations and their designed first failures) and §10.4 (the reader-local unit tests);
  - REVISION_01 §2 (R-COMB-1's rows), §4 (gate placement: N-3's branching conjuncts, which replace §10.1's "widened" wording; N-11's G3 (h) and (i); N-12; D6b case-only; N-6, N-8, N-10 and N-14) and §5.3 (the mutation table's changes);
  - REVISION_02 §1 (option (ii), the displacement magnitude: G7's guard holds by construction), §3 (NC-2, `stages.observables`) and §4 (A-2 to A-6).
  - Where a revision amends or replaces a CONTRACT section, the revision governs.
- **The rulings:** RR "RV118 (RV-C) accepts B2-C with amendments; B2-C ruled; C-1 to C-16 selected; …", "RV118 confirms B2-C revision 01; …" and "RV115 and RV118 confirm B2-C revision 02: B2-C is final for J1; …".

## Also in these lanes

1. **RV122 N-2 (RS lane).** Package DEF-C, DEF-E and XTABLE in RS as DEF-O is (CONTRACT §8 row 4), and return `reviewed_inputs_bind_the_lock_and_the_reader_statics` from `[1..14]` to `[1..]`.
2. **RV125 N-1 (all three).** The readers admit a negative or zero `global_upper_bound_pa` or `certified_gap_pa`. Add a refusal with one shared shape, at the same gate and code in all three readers. The RS lane proposes the gate and code from the contract's existing gate families. WORKING_ITEMS confirms the choice before the other lanes land it.
3. **Entry 22 (all three).** A combination in an invocation is refused today at G8 `INVOCATION_MISMATCH`, which was provisional (RR "PR-B1 cut (`8248921552`); …", ruling 2). B2-C admits model combinations, so settle entry 22's expected outcome where B2-C places the check.
4. **TS lane, T6S, tests only (CONTRACT §10.4, N-8).** Add combination-successor tests in `StressNeutralExportPanel.test.tsx` (`basisReference` on combination rows, and their withheld witnesses) and `analysisRunCompatibility.test.ts` (`sourceBasisReference`). There is no source edit. A changed disclosure meaning is a stop.

## The method, per lane

1. **The census first:** run 07m and 07n before and after your change. 0 changes is required (R5's rule). At z = 0 every branched conjunct is today's predicate. Any census change is a stop.
2. **Gates, in CONTRACT §10.1's order**, each new check appended after the gate's existing checks, with the codes stated. G0's table-dependent checks take the table as an internal parameter, so the 11 G0 unit tests can pass a test-only copy (§8).
3. **Inputs:**
   - B2-P's producer-solved successors on the branch, in both modes: W-CB1, W-CB1z, W-CB2, W-CB3, W-CB4a and W-CB4b, W-CB5, `b2_c1_range_mechanics` and the B + A forms. The fixtures are under `P/fixtures/results/` and in PP's B2-P pins.
   - Synthetic receipts only for REVISION_01 §5.1's synthetic bases (`b2_base_withheld`, `b2_pre_source_refusal`), labelled so.
   - Hook-produced bases as REVISION_01 §5.1 lists them.
4. **Mutations:** each row of CONTRACT §10.3, as amended by REVISION_01 §5.3 and REVISION_02 §4.3 (69 in all), applied to its base. Your reader must give the designed first failure (gate and code). A row your reader cannot meet as designed is a stop for WORKING_ITEMS, not a per-reader declaration.
   - **The RS lane** writes its materialized mutation inputs to one JSON file in its records, as I101 did for B3 (`R/I101/b3_readers_01/`), and tells WORKING_ITEMS when it is committed.
   - **The PY and TS lanes** run that file before returning, if it is ready. Otherwise WORKING_ITEMS runs the three-reader cross-check at fan-in.
   - 07o itself is SC2's, after your lanes merge. Do not write 07o.
5. **The three readers agree** on every new shape's gate and code. A disagreement goes to WORKING_ITEMS.
6. **Mutants:** one per new check, each killed by an assertion.

## Stops

- Any change needed in PP, FK, the schemas, the statics, the corpus files or another lane's reader. The producer's receipts are fixed inputs.
- A census change over 07m or 07n.
- A mutation whose designed first failure your reader cannot give.
- **An estimate past the top of B2-C's range by more than half** (RS above 36 h, PY above 24 h, TS above 27 h). Tell WORKING_ITEMS as soon as you see it.

## Evidence

- The census over 07m and 07n: 0 changes.
- Suites against your base head, test by test: only added tests. Explain any other change.
- The 69 mutations, each with the designed and observed first failure.
- The mutants, with the assertion that kills each.
- Keep the RETURN short. The tables carry the evidence.

## Host

- **Every cargo** goes through `WT/tools/t3_cargo.sh` (`--locked --offline`), with fresh targets under `WT/targets/<id>-b2r-*`. **Other heavy commands** go through `WT/tools/t3_slot.sh`.
- **vitest** runs in an archive, as `T/IMPLEMENTATION/B1_I4/` shows.
- **One heavy job of yours at a time;** one wait per job, ending when its process has gone. Never signal another job. Three lanes share three slots.
- **Not allowed:** DEC-025, measurements and installs.
- **Paths:** absolute paths only. Scratch goes in `WT/scratch/<id>_b2r/`.
- **Records:** placeholder paths only, no symlink, and no folder named `build`. Write them directly in `R/<id>/b2_readers_01/` in NUM. If the host refuses a record file, give its full content in your final message with its intended path; do not work around the refusal.

## Output

- **Commits** on your lane branch only, with truthful messages. WORKING_ITEMS pushes and merges into `b2` after RV-R2.
- **The record:** `R/<id>/b2_readers_01/RETURN.md`, with `_run_records/` and SHA256SUMS.
- **Budget** (B2-C REVISION_01 §8, unchanged by REVISION_02): RS 17–24 h, PY 11.5–16 h, TS 12.5–18 h.
- **End your turn with:**
  - the head;
  - the census;
  - the suites;
  - the 69 mutations;
  - the mutants;
  - the routed items 1 to 4;
  - any stop.
