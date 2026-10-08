# RV120 (RV-R): B1's reader follow-up toward I4′ — RS and TS confirmed; PY pending

TASK (Type 2), RV120, for ROOT (HELP_HUMAN, Agent 0), the return path. No delegation; I wrote none of the change. 2026-10-08 UTC.

## Basis

- **Brief:** `R/BRIEFS/RV120_RVR_I4P.md`, sha256 `64e74af4…8ab2` (verified). **Specification:** RR "I4 made at `30f3d1b24a`; …" rulings 1–5; `BRIEFS/B1_I4P_RS_TS.md`; `BRIEFS/B1_I4P_PY.md`; RV113's SR-RS addendum 02, SR-TS addendum 01 and SR-PY addendum 01. RV113's harnesses and probe sets are reused unchanged (`evidence/harness/RV113_FILES_USED.txt`).
- **Candidates,** over I4 `30f3d1b24a`:
  - **RS** `codex/piping-t3-b1-r-20261007` at `e879118348` (`990339d94f`, `e879118348`): RS +18/−6; `RE/tests/retained_precision_contract.rs` +342/−0.
  - **TS** `codex/piping-t3-b1-t-20261007` at `819e44f63e`: TS +4/−1, its test +33, `retainedPrecision.test.ts` +33. `retainedPrecision.ts` is unchanged.
- **Copies:** `git archive` copies of P without `execution/` at I4, at each head, and a mutant copy of each head; each file equals `git show` (`evidence/static/copies.txt`). TS copies: NMS linked after a `package-lock.json` cmp (equal at I4 and the head); an empty `apps/desktop/node_modules` of their own, so vite writes nothing into NMS's tree; the eight wasm assets copied from `WT/sweep-skewpin`, equal to ROOT's I4 set (`evidence/static/wasm.sha256`).
- **Order:** rulings, diffs and code; then my runs. I101's RETURN (`R/I101/b1_i4p_rs_ts_01/RETURN.md`, sha256 `c5e3269e…6b336`, verified) was read after my RS results, before my TS results.
- **Placeholders:** WT, NUM, P, RE, DT, R, RR as in the brief; RS = `RE/src/retained_precision.rs`; TS = `DT/features/results/previewPhysicsEvidence.ts`; NMS = the linked `node_modules`.
- **My probes:** RV113's 392 (`probes_ts1.json`), its 2 r2x, and 41 of mine written from the rulings (`evidence/probes/probes_rv120_own.json`): every non-number shape of each member (string, numeric string, null, booleans, lists, object), both at once, later cases and extrema, the u8 L = 0 bases, numbers that must stay admitted (0, −1.0, a large fraction, a large integer), the demand's place against shape, identity, fractions, integers and bounds, a missing member, and five withheld-multiplicity shapes. 435 in all.

## Verdicts

| Lane | Head | Verdict |
|---|---|---|
| RS | `e879118348` | **CONFIRMED** |
| TS | `819e44f63e` | **CONFIRMED** |
| PY | — | not yet received: brief items 2 and 6, and PY's part of items 1, 3, 7, 8 and 9, are open |

## Brief items, RS and TS

| # | Item | RS (`e879118348`) | TS (`819e44f63e`) |
|---|---|---|---|
| 1 | Census over 07m, I4 → head | 339 entries: **0 changes** on bound, unbound, transport and standing, details included; 0 misses against `expected_by_reader.rust` at I4 and head. RS at I4 is byte-equal to RV113's census at `6e3e4fe219` | 339 entries: **0 changes**, details included; 0 misses against `.typescript` at I4 and head. TS at I4 is byte-equal to RV113's census at `6fa6a64658` |
| 3 | Ruling 2 on transport | `t_withheld_duplicate_multiset`: G7 `…EVIDENCE_INVALID` (as at I4); `t_extrema_global_upper_string`, `t_extrema_certified_gap_null`: admitted → **G7 `…EVIDENCE_INVALID`**, "extrema numbers" | the same three: same gate, code and detail |
| 3 | Callers | `preview_physics_transport_metadata` ← `validate_transport_metadata` ← `semantic_contract::for_source_metadata` (retained statements only) ← headless runner (`core/runner/headless/src/lib.rs`). `validate`, and so PP's precommit, does not reach it | `readCases` serves both entry points. `validatePreviewPhysicsTransportMetadata`: the retained transport at G7, and `StressNeutralExportPanel.tsx` on the plain route. `validatePreviewPhysicsEvidence`: the retained raw G7, `resultExportAdapter`, `numericalResultQuality`, `analysisRunCompatibility`, `previewService` |
| 3 | Producer-emittable inputs | **No change in either reader.** The producer writes both members only from an `Ok` `CertifiedStressMaximum`: `upper_bound` is a finite interval bound (`objective` refuses a non-finite one) and `certified_gap` is at most the finite tolerance. All 126 extrema records in the 46 committed JSON fixtures carry numbers, and the suites' only differences are the added tests | (same) |
| 4 | Ruling 3, TS raw | RS raw unchanged: G7 `…NUMBER_INVALID` bound and unbound (declared per reader) | both shapes: admitted, eligible bound → **G7 `…EVIDENCE_INVALID`** bound and unbound |
| 5 | Ruling 4: twelve rows | **Each of RV113's twelve mutants is killed by exactly its own row** at `b1_table`'s assertion: N21, N25, N30 by `b1_i4p_c2_conjuncts_alone`; N45, N47, N48, N56, N58, N60, N63, N64, N65 by `b1_i4p_transport_metadata_demands_alone`. N18, N24, N34 survive, as RV113's three equivalents. The doc comment says what RV113's N-1 asked | — |
| 7 | RS against TS on the 435 probes | **Transport equal on all 435;** where both refuse, the detail texts are equal after RS's code prefix. Raw: 78 probes differ, each a raw G7 code difference with both refusing at G7 (RS's specific raw codes against TS's `…EVIDENCE_INVALID`: the declared class). **0 other differences.** The same comparison at I4 had 4 others: TS's raw false accepts of the two ruled shapes. On 07m, the one difference is entry 139's declared raw G7 code | (same) |
| 8 | Suites vs I4, test by test | RE 195 → 198 ok (my 2 harness tests on both sides): **+3 added** (`b1_i4p_*`), 0 removed, 0 changed | vitest, whole suite, 142 files on both sides (my harness file included): 3,631 → 3,639 passed, **+8 added** (7 in TS's test, 1 in `retainedPrecision.test.ts`), 0 removed, 0 changed. tsc rc 0 at the head |
| 9 | My mutants on the new check | **7 of 7 killed** at `b1_table`'s assertion, each by `b1_i4p_transport_extrema_numbers_at_g7` alone: the demand dropped (V01); either member's half dropped (V02, V03); null or a string admitted (V04, V07); the demand moved after the bounds (V05); another detail (V06) | **9 of 9 killed** by `AssertionError`s, with the whole suite per mutant and kills only in the two changed test files: the demand dropped (W01); either half (W02, W03); null or a string admitted (W04, W10); moved after the bounds (W05); another detail (W06); raw only (W07); transport only (W08) |

**Probe changes, I4 → head, every verdict in full:**
- **RS:** 24 transport verdicts, the 2 ruled shapes and my 22 non-number shapes, each admitted → G7 "extrema numbers". 3 detail-only: my order probes, "extrema fractions/integers/bounds" → "extrema numbers". No raw change.
- **TS:** 72 verdicts, the same 24 probes bound, unbound and transport → G7 "extrema numbers"; all 24 were admitted and eligible bound at I4. 9 detail-only: the same order probes.
- Nothing else moved in either reader. Of 471 stated expectations, each reader misses 0.

**Mutant controls:** RS 26 + 79 of 105 pass; TS 3,639 of 3,639 pass, and its probe outputs equal the head's on all 435.

## Findings

| # | Severity | Where | Finding |
|---|---|---|---|
| N-1 | NOTE (for SC item 14; to recheck on PY's head) | PY at I4 (RV113's recorded run), transport | On the two extrema shapes PY's transport detail is "transport evidence shape": its schema typing of `contract_evidence` runs first. RS and TS give "extrema numbers". Gate and code agree. I101 reports the same. If 07n pins details, this needs a per-reader detail or a PY change |
| N-2 | NOTE (for SC) | RS and TS | Ruling 2 asks for a number only. A negative or zero `global_upper_bound_pa` or `certified_gap_pa` is admitted on every path, and eligible bound, in both readers, as at I4 (A1 d + A2 1: typed, never bounded) |

No BLOCKING or SHOULD-FIX finding on RS or TS.

## Against I101's RETURN

My results agree with it on every count I can compare: 0 census changes in both readers; its 2 ruled probe changes (within my 24); RS = TS on every transport verdict; its 45 raw-code-class probes of RV113's set (my 78 add 33 of mine); RE +3 and vitest +8 with 0 changed; RV113's twelve killed by their rows; N18, N24 and N34 surviving. I ran RV113's 15 survivors at `6e3e4fe219` and my 7 RS mutants, not RV113's other 46. Those were killed at `6e3e4fe219` by tests that are unchanged at the head (the test diff is +342/−0), and I101 reports them killed again.

## Host

- **Cargo,** 3 jobs through `WT/tools/t3_cargo.sh` (`--locked --offline`, toolchain 1.97.1): RE's whole suite at I4 and at RS's head, which built them, and the mutant copy's test build. Targets are `WT/targets/rv120-rs-{i4,head,mut}`.
- **Slot jobs** through `WT/tools/t3_slot.sh`, one at a time: RS's harness at I4 and head, then its probe test alone on both; the RS mutants (control and 22); TS's harness at I4 and head; vitest whole suite at I4 and head; tsc; TS's mutants (control and 9) and the control's probe run.
- **Slips, disclosed:**
  - My first probe file held an integral 1e308, which checked JSON cannot hash. RS's harness wrote the census and then stopped at that probe (rc 101). I replaced it, dropped a subnormal as a precaution, and re-ran the probe test alone on both copies. The census outputs are from the first runs.
  - I stopped my own full RS mutant chain (all 68) after its control and part of N01, to save host time. I deleted N01's partial run and ran the targeted 22 instead. Only my own job was stopped.
- **Waits:** each chain had one waiter, its background completion. I read progress with single reads (listings, a log's tail), never as a second waiter. None of mine remain.
- **NMS's tree:** its `.vite-temp` mtime is unchanged by my runs.
- **Not done:** no DEC-025, installs or Git writes (`git archive` and reads only, `GIT_OPTIONAL_LOCKS=0`).
- **Kept for PY and SC:** `WT/scratch/rv120_rvr/` (copies, PY's I4 copy, probes, harness, outputs) and the three targets.

## Records (`evidence/`)

Placeholder paths only; no symlink; no folder named `build`; no junit output. Screened with `WT/tools/t3_host_screen.py`'s patterns, `.gz` files decompressed: 0 hits.
- `harness/`: my scripts (probe generator, comparisons, mutant schemas and table, copy maker, job wrapper, chains) and `RV113_FILES_USED.txt`.
- `static/`: `copies.txt`, `wasm.sha256`.
- `probes/`: `probes_rv120_own.json`; RS's and TS's outputs at I4 and head; `RS_PROBES_I4_HEAD.json`, `TS_PROBES_I4_HEAD.json`, `CROSS_RS_TS_HEAD.json`.
- `census/`: RS's and TS's census at I4 and head; `RS_CENSUS_07M.json`, `TS_CENSUS_07M.json`, `CROSS_CENSUS_HEADS.json`.
- `suites/`: RE's logs and `RS_SUITE_COMPARE.json`; vitest's JSON reports and `VITEST_COMPARE_TS.json`; `ts_head_tsc.log`.
- `mutants/`: `MUTANTS_RV113_R2.json`, `MUTANTS_RV120_RS.json`, `MUTANTS_RV120_TS.json`, `MUTANT_TABLE_RS.json`, `MUTANT_TABLE_TS.json`, `rs_runs/`, `ts_runs/`.
- `host/job_stamps.txt`.
