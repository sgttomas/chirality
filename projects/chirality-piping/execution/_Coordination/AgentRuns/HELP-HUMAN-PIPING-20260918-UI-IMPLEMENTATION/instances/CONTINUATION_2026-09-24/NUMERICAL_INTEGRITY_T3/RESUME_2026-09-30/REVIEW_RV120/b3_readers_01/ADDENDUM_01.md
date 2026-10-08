# RV120 (RV-R2) ADDENDUM_01: B3's repair round 01 — CONFIRMED; F1, N1 and F2 closed

TASK (Type 2), RV120. The request came from WORKING_ITEMS for T3 (Agent 1), my return path by the owner's decision of 2026-10-08, as it stated. No delegation; I wrote none of the change. 2026-10-08 UTC.

## Basis

- **Candidates:**
  - PY `b2-p` `6d3d4cdca6`: one commit on `b7721d27e9`.
  - RS `b2-r` `81d41baebf`: tests only.
  - TS and lane T `b2-t` `65c04cd0c7`: `58fa652cc8`, tests only, plus a merge of `b2-r`.
- **Unchanged since my review:** RS's and TS's shipped sources, the three schemas, `outputPolicy.ts` and `numericalResultQuality.ts` are byte-equal to `77aaaa61d1`. PY's reader changes only in `_preparation_payload` and `_g5_numeric`.
- **Records**, read after my runs:
  - `R/I100/b3_readers_01/REPAIR_01.md` (`b7aacb9d…`; SHA256SUMS.repair_01 70 of 70);
  - `R/I101/b3_readers_01/REPAIR_01.md` (`f2e6fa28…`; 62 of 62).
- **Copies:** `git archive` into `WT/rv120b3/{ts2,py2,probe2,mut2,py2m}`, made as in REVIEW.md. The scripts are in `addendum_01/harness/`.

## Findings

| # | Status | Evidence |
|---|---|---|
| F1 | **Closed** | PY now runs the exact-route evidence check in its own loop after the shared G5b loop, before G5c, as RS and TS do. On the order probe, PY now reads G5b `SCALE_MISMATCH`, bound and unbound, as RS and TS do. The other three G5b probes read as before. PY pins all four probes (`test_repair01_g5b_*`; its fixture's `input_sha256` matches my index). RS and TS were already correct and do not pin the probe. That pin is optional |
| N1 | **Closed** | `_preparation_payload(a, definition_hash)` has no default. Every caller (the reader's G1 and G8 sites and the tests) passes a hash, and a call without one raises `TypeError` (pinned) |
| F2 | **Closed** | Every reader now pins my four forgeries. RS's dumped inputs are equal to my `forge_eg_inputs` bytes; PY's fixture re-materializes them to my `input_sha256`. **Mutants:** <ul><li>B28 and B29 are each **killed** in RS (`retained_precision_contract`: 2 failures each) and in TS (`retainedPrecision.test.ts`: 2 of 532 each). The failing tests in both are the forgery pin and the 169-shape pin.</li><li>**I100's PY note:** my own spellings of R2–R5 on my forgeries confirm it. Under R2 or R3 every forgery is still refused at G8, by the attempts loop's binding of each prepared member's old E/Ĝ to the authored pair (`retained_precision.py:1858`). Under R4 the E forgeries read eligible, and under R5 the Ĝ forgeries do, so PY's pins kill both.</li></ul> **This is acceptable.** That binding is PY's own stricter, independent anchor; RS and TS bind `old_source` to the receipt material instead. It covers only prepared members, so step 4 stays the only anchor for a material that reaches no attached `PreparedMember`, as it is in RS and TS. Step 4 must not be read as redundant |
| N2 | **New; low; pre-existing, outside B3's diff** | **RS's physics-1 transport check is nondeterministic.** Its first failure code can change from run to run. `physics_evidence.rs` `validate_transport_metadata` iterates `indexed(…)`, a `HashMap` (`:67`, loop `:1019`), so with faults in two `exact_cases` entries the first code depends on hash order. My probe "an exact_cases entry for a case not in the invocation" gave G7 `SOURCE_PHYSICS_RHS_METHOD` or `SOURCE_PHYSICS_TRANSPORT_MAXIMUM_RESULT` on transport across 5 fresh processes, on both bases. The gate (G7) and the bound reading are stable, and G7 codes are per-reader by settlement. TS and PY iterate in insertion order. B3's exact route reaches this through physics-1's unchanged validator. **Fix:** for the physics-1 lane, iterate in array order. It does not block B3's merge |

## The confirmations requested

| Check | Result |
|---|---|
| The three readers agree on my inputs (repaired heads; raw runners on identical bytes) | **Yes.** <ul><li>My 128 probes and 4 forgeries: 0 differences outside G7 and 0 missed wants.</li><li>I101's dump, now 169 shapes: 0 differences outside G7. The 165 earlier inputs are byte-identical, and the 4 additions are my forgeries.</li><li>I100's 52 and 318: 0 differences.</li></ul> |
| No other outcome moved | **Yes, apart from N2.** I compared 6,003 readings with the pre-repair heads; 4 moved. Two are F1's PY order probe, bound and unbound, as intended. The other two are RS's transport G7 code on N2's probe, a swap between two codes that I reproduced without any code change |
| Census | **0 changes and 0 misses** against the base census, in RS, TS and PY, for 07m (339) and 07n (638) |
| Suites, test by test against my review's heads | <ul><li>**RE:** 207 → **208** ok, +1 (`b3b_rv120_f2_forgeries_are_refused_at_g8_step_4`).</li><li>**vitest:** 3,679 → **3,680** passed: +1 (the F2 pin) and 1 renamed (the shape pin's title, 165 → 169 shapes).</li><li>My copies' counts include RV113's two no-op harness tests. Without them they are I101's 206 and 3,678.</li><li>**tsc:** rc 0.</li><li>**PY at its head:** 1,693 → **1,701** (+8: 4 G5b, 4 forgeries).</li><li>**PY's schema files at the TS head:** 1,321 → 1,321.</li><li>0 removed and 0 changed outcomes</li></ul> |

## Verdict

**CONFIRMED.** F1, N1 and F2 are closed, and the reader lanes may merge into `b2`. N2 is a pre-existing determinism defect in RS's physics-1 base validator. I route it to that lane; it does not block the merge.

## Host

- **Jobs:**
  - Every cargo run went through `WT/tools/t3_cargo.sh --locked --offline` (targets `WT/targets/rv120b3-{ts2,probe2,mut}`).
  - Every other heavy job went through `WT/tools/t3_slot.sh`.
  - One heavy job of mine ran at a time. The B29 job waited about 10 minutes for a slot that other jobs held.
  - No Git writes, no DEC-025, no installs and no measurements.
- **Disclosed:**
  - Two duplicate waiters of my own were stopped.
  - The mutated sources in `mut2` and `py2m` were reverted and cmp-checked.
- **Record:** `addendum_01/host/job_stamps.txt`. Placeholders: `WT`, `NUM`, `R`, `NMS`, `VENV`. Junit host attributes were removed.
