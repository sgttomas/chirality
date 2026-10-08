# I100 — B3 readers, repair 01: RV120's F1, N1 and F2 (PY's share)

TASK (Type 2), I-PY; return path ROOT. Basis: RV120 `R/REVIEW_RV120/b3_readers_01/REVIEW.md` (sha256 `1cf687f6…`).
Lane head **`6d3d4cdca6`** on `codex/piping-t3-b2-p-20261008` (parent `b7721d27e9`), one commit. Run records:
`_run_records/repair_01/` (sums in `SHA256SUMS.repair_01`).

## The change

- **F1.** `_g5_numeric` no longer calls `_g5b_exact_evidence` inside the per-case shared G5b loop. On the exact route
  it now runs in its own loop over every selected case after the shared loop, before `phase[0] = "G5c"` (DESIGN §6.2's
  G5b row), as RS's `g5b_exact_evidence` (`:4771`) and TS (`:1569`) run it.
- **N1.** `_preparation_payload(a, definition_hash)` has no default. Its two reader callers already passed the route's
  hash (G8, G1). The shared corpus harness (`tests/test_retained_precision_contract.py`) now passes DEF-O's H
  explicitly (its corpus is on the preview route); B3's S-1 test passes it too and asserts a call without it is a
  `TypeError`.
- **F2 pins**, with F1's probe, in `tests/test_retained_precision_b3.py`, from
  `fixtures/results/retained_precision_rv120_b3_inputs.json` (82 KB, sha256 `34f3846f…`). RV120's eight inputs are stated as edits from
  bases the tests already hold (the corpus's `ordinary_prepared_synthetic` and `two_case_synthetic`, from which RS's
  exact construction starts, and lane P's m3x successor), resealed by 07e with DEF-E's H. Each re-materializes
  byte-equal to RV120's input: the test asserts its INPUTS_INDEX sha256. Tests:
  - `test_repair01_g5b_shared_checks_precede_the_exact_evidence`: the order probe (case 0's evidence `As_m2` +1 ulp,
    case 1's `body_scales[0].force` +1 ulp) reads G5b `SCALE_MISMATCH` bound and unbound; its two controls and the
    other order probe read as before; transport passes.
  - `test_repair01_rv120_forgeries_are_refused_at_g8`: the E and Ĝ forgeries on `ordinary_prepared_synthetic` and
    `m3x_sparse_interactive` are G8 `PREPARATION_MISMATCH` bound; unbound and transport read as the base.

## Evidence

- **Census** (PY at `6d3d4cdca6`, against B3's base runs): 07m 339 entries, **0 changes**; 07n 638 entries,
  **0 changes**.
- **Suites**, test by test against `b7721d27e9` (29 modules, the B3 module included): 2395 → **2403 passed**, 30
  skipped at both. 0 removed, 0 changed, 8 added: the four F1 and four F2 tests above, all passing.
- **Mutants** (guarded, in a copy of `6d3d4cdca6`; the B3 module, 383 tests). The control has 0 failures, and every
  kill is an assertion:

  | Mutant | Edit | Result |
  |---|---|---|
  | R1 | the evidence check back in the per-case shared loop | **killed** by the order probe (1) |
  | R2 | step 4's E bits unchecked (both material-basis loops; PY's B28) | survives |
  | R3 | step 4's Ĝ bits unchecked (PY's B29) | survives |
  | R4 | R2, and the attempts loop's old-E binding to the authored material | **killed** by the two E forgeries (2) |
  | R5 | R3, and the attempts loop's old-Ĝ binding | **killed** (7: both Ĝ forgeries, and B3b's x26) |

  R2 and R3 survive because PY binds each prepared member's old E and Ĝ to the authored material a second time, in
  G8's attempts loop (`old[:2] == [bits(v) for v in pair]`, `retained_precision.py`:1858 at the head). The trace
  (`mutants/FORGE_TRACE.txt`) shows the forgeries refused there under R2 and R3, at step 4 (:1721 at the head) otherwise; the trace's line numbers are the mutant copy's, one higher, and
  read eligible only under R4 (E) and R5 (Ĝ). The second binding adds no refusal of its own: the old tuple already
  equals the id map, the id map the basis, and the basis the authored pair. So in PY the forgeries witness the two
  anchors together, and they are the only witnesses for E (R4).
- **Agreement** (`agreement/`). PY at `6d3d4cdca6` was read with RV120's own runner on RV120's inputs. Each input's
  sha256 equals its INPUTS_INDEX (`INPUTS_CHECK.txt`). The RS and TS readings are RV120's, at `c845e899da` and
  `77aaaa61d1`, which are still the lane heads. Compared with RV120's `cmp3.py`:

  | Set | Inputs | Differences outside G7 | Want misses | G7 triples |
  |---|---|---|---|---|
  | RV120's probes | 128 | **0** (was 2: F1, bound and unbound) | **0** (was 1) | 7 |
  | RV120's forgeries | 4 | 0 | 0 | 0 |
  | I100's addendum shapes | 52 | 0 | 0 | 0 |
  | I101's shapes | 165 | 0 | 18 (G7 codes, as RV120's) | 12 |
  | I100's B3 shapes | 318 | 0 | 0 | 14 |

  Across all 667 inputs, PY's lines are identical to RV120's PY lines except the one order probe.
- **Host:** one heavy job at a time through `t3_slot.sh`, PY only (RS and TS are unchanged). Light checks (the input
  hashes, the compaction, and the forgery trace) ran directly. The chain waited about an hour behind another
  agent's exclusive host job. No installs, no DEC-025.

## Stop

None.
