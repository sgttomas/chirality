# RV120 (RV-R): SC (corpus 07n) and the readers' pins — PASS

TASK (Type 2), RV120, for ROOT (HELP_HUMAN, Agent 0), the return path. No delegation; I wrote none of the change. 2026-10-08 UTC.

## Basis

- **Brief:** `R/BRIEFS/RV120_RVR_I4P.md` ("then SC") and ROOT's message. **Specification:** `R/BRIEFS/B1_SC.md` (sha256 `58ca6174…6cce6e`, verified), items 1–14 and Acceptance; PLAN_v2 §2.5; ROOT's rulings since: detail texts not pinned (A-N1); the A-N2 shapes not in 07n; the per-reader form for the 45 entries; the four optional fields accepted.
- **Candidate:** `codex/piping-t3-b1-20261007` at `57c92a7b33` over I4′ `8d46b045e2`: `09fe4cc69b` (07n and PY's pins), `90d8fbeea5` (RS's pins), `901745f46b` (TS's pins), `57c92a7b33` (RV108 N6(b)). Reader sources at I4′ equal the heads I confirmed (RS `e879118348`, TS `819e44f63e`, PY `52d83da275`), and SC changes no reader source.
- **07n:** `P/fixtures/results/retained_precision_cases.json`, sha256 `ea113e7b…e283` (verified): 26 cases (+9), 534 mutations (+240), 78 must-pass (+50). The 07m prefix and every other top-level key are unchanged.
- **Copies:** a `git archive` copy of P at the head (plus PKG-15's folder for PY), with RV113's three harnesses, NMS linked after a lock cmp, its own `apps/desktop/node_modules`, and the eight wasm assets. A second copy carries a corpus with nine corrupted expectations (item 5). PY's authority binaries are my I4 builds (`rvr_i4p_01`, byte-equal to RV113's and I91's).
- **Order:** the brief, diffs and pins, then my runs and checks; I100's RETURN (`a4bd24f9…`) and I101's RETURN (`6343e404…`) and ADDENDUM_01 (`ba4f17ab…`), all verified, after my census.
- **Placeholders** as in `rvr_i4p_01/REVIEW.md`.

## Result by review priority

| # | Check | Result |
|---|---|---|
| 1 | Each 07n entry's first failure designed, reached in all three readers, pinning its item | **Yes.** RV113's harnesses over the whole corpus, each reader's every verdict against the corpus's own expectation for that reader (bound, or eligibility and standing for bases and must-pass; unbound; transport; class counts): **1,218 checks per reader, 0 misses in RS, TS and PY.** Origins (`static/STATIC_CHECKS.json`): 272 entries are RV113's designed probes (233 with the same base and edits, 39 re-encoded into edit lists that materialize identically), and all 292 of RV113's stated expectations for them agree with the corpus. 18 are new designs from PLAN_v2 §2.5 and RR: D38 m1–m9, F-1's five, `not_required` on W-C2 case B (three, the product attempt being case B's own, reaching G5 ATTEMPT), and N2. Items 1–14 are each covered (one literal gap: SC-N2) |
| 1 | D38 base: derivation and reseal | `d38_beside_selected` differs from W-C2 sparse exactly by PLAN_v2 §2.5's steps: case C's Run, its `execution_order` entry and the four Builds its Run originated removed; C's source removed from the call's and the group's `source_refs` (and the call's owner and Run lists); `charged` and the call's after-value set to A's; the cause a typed capture `origin` error; resealed (receipt changed, invocation unchanged). PY's pin re-derives it. All three readers pass it G0–G8 with `needs_recompute` |
| 1 | The nine bases' provenance | The W-C2 bases equal I85's committed fixtures (sha256 `7922e3e5…`, `f2800bd4…`), source and invocation. The six other producer-solved bases carry the receipts and bytes digests that PP's own tests pin (`REVERSED_PINNED`, `CBA_PINNED`, `AA2_PINNED` in `retained_facade_tests.rs`); each receipt binds its source, and all three readers verify it. No tampered-preparation successor is a base |
| 2 | 07m census unchanged | **0 changes** in RS, TS and PY on 339 entries × bound, unbound, transport (and RS's standing), details included, against the I4′ readers' census |
| 3 | Must-pass entries | All 50 pass in all three readers with the stated eligibility (46 eligible in all, 07m included) and classes. The 16 entries with their own `expected_classifications` each differ from their base's (an unselected case, or a parity row added or removed) |
| 4 | Per-reader entries | **Exactly the declared class.** Reader agreement over all 638 entries: TS = PY on all 1,914 verdicts; RS differs from both only on 46 entries' raw G7 codes (both refusing at G7, bound and unbound): the 45 per-reader 07n entries and 07m's entry 139. Each per-reader entry is a real difference; no other entry differs, and transport agrees everywhere |
| 5 | Pins read the new fields and fail on a wrong one | Nine corrupted expectations (`exp/`), each failed by exactly the readers that read that field: the bound `expected` (all three); `expected_by_reader.rust` (RS only); the shared Python/TS expectation (TS and PY only); `expected_unbound` on a mutation and on a must-pass entry (all three); `expected_transport` (all three); a must-pass entry's `expected_classifications` and a base's (all three); a must-pass `standing` (TS and PY; RS, see SC-N1) |
| 6 | Readers' own tests at the head | RE: 198 → **201 ok** (+3 added: `snapshot_07n_*`), 0 changed. vitest (whole suite): 3,639 → **4,247 passed** (+608, all in `retainedPrecision.test.ts`), 0 changed; tsc rc 0. PY (contract, carriers, schema): 531 → **1,131 passed** (+600), 0 changed. Carrier tests with N6(b): RS 17, TS integration and PY 52 within these runs, all passing |
| 7 | Coverage gaps | None material: SC-N2 to SC-N4 |

## Findings

| # | Severity | Finding |
|---|---|---|
| SC-N1 | NOTE | RS's own tests pin a base's and a must-pass entry's eligibility by `numerical_eligible` and `invocation_bound`, not `standing`, so a corrupted `standing` fails TS and PY but not RS. This predates SC. My census confirms RS's standing on all 638 entries |
| SC-N2 | NOTE | Item 7 lists `combinations` `[{}]`; 07n's non-empty case is `[{"id": "combination:rv113"}]` (RV113's probe). It breaks the same conjunct, but the literal `[{}]` is absent |
| SC-N3 | NOTE | Items 12–13's scope sentences are stated once for the declared class, in the three readers' 07n test comments and I100's RETURN. The corpus has no per-entry scope field; if ROOT wants one per entry, it needs a field or a side table |
| SC-N4 | NOTE | Item 9's "(a)" has no counterpart in RR, which rules (b), (c), (d1) and (d2), plus m9. 07n covers those and (e). I agree with I100 |
| SC-N5 | NOTE | 07n is 16.2 MB. PY's three retained files took 6 min 51 s in a slot |

No BLOCKING or SHOULD-FIX finding.

## Against the returns

They agree with my runs on every count I can compare: 07n's counts and sha256; 45 per-reader entries in one form; 0 07m changes in three readers; every stated check met; RE +3, vitest +608 over I4′ (I101's +291 is counted against SC's commit, where the parametrized tests had already grown), PY 1,131; N6(b)'s three pins. T-12 (SP's several-notice bytes) was checked by I100 (PY) and I101 (TS) in scratch harnesses; I did not re-run it.

## Host

- **Cargo,** 2 jobs through `WT/tools/t3_cargo.sh` (`--locked --offline`, toolchain 1.97.1): RE's whole suite at the head (target `WT/targets/rv120-sc-head`), and the contract test on the corrupted copy (`rv120-sc-exp`).
- **Slot jobs,** one at a time: the three harness censuses, vitest whole suite, PY's retained files, tsc, and the corrupted copy's TS and PY runs.
- **Waits:** one waiter per chain; single progress reads only. None of mine remain, and I signalled no job. No DEC-025, installs or Git writes.
- **NMS's tree:** untouched; each copy had its own `apps/desktop/node_modules`.

## Records (`evidence/`)

Placeholder paths only; no symlink; no folder named `build`; junit host attributes removed; screened with `WT/tools/t3_host_screen.py`'s patterns, `.gz` decompressed.
- `harness/`: my scripts and `RV113_FILES_USED.txt`.
- `static/`: `copies.txt` and `STATIC_CHECKS.json` (prefix, D38 diff, provenance, entry origins with RV113's stated wants, own classes).
- `census/`: the three readers' outputs over all 638 entries, `CHECK_3.json` (each reader against the corpus, plus the 07m prefix) and `AGREE_3_07N.json`.
- `suites/`: RE log, vitest report, PY junit, the three test-by-test comparisons against I4′, and tsc.
- `exp/`: `CORRUPTIONS.json`, `EXP_RESULTS.json`, and the three readers' failing runs.
- `host/job_stamps.txt`.
