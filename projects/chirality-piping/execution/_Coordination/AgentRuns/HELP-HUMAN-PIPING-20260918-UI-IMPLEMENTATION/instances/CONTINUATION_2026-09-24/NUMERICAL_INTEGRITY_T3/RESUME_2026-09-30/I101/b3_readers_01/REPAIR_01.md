# I101 B3 readers, repair 01: RV120's F2 (B28 and B29 pinned)

TASK (Type 2), I101, for ROOT. 2026-10-08 UTC.

**Basis:**
- ROOT's repair message;
- RV120's `R/REVIEW_RV120/b3_readers_01/REVIEW.md` (`1cf687f6…`; its `SHA256SUMS` verified, 87 files);
- its `harness/forge_eg.py` (`c0655844…`) and `readers/forge_eg_inputs.jsonl` (`d586f570…` uncompressed).

## Correction

**My B3 record called B28 and B29 equivalent. That was wrong.**
- **What my trace showed:** a forgery that leaves the native hashes unsealed is refused by those hashes.
- **What it missed:** a forger can reseal them, and RV120 did.

So step 4's E bits and Ĝ bits are the only anchors from the receipt to the authored material.

Corrected mutant tallies:

| Set | Killed |
|---|---|
| RS | **41 of 43** |
| TS | **45 of 47** |
| PY carrier schemas | 12 of 12 (unchanged) |
| Addendum 01 | 4 + 4 (unchanged) |

B06b and B30 remain the accepted equivalents; RV120 accepts both.

## Change: tests only; no reader code changes

| Lane | Commit | What |
|---|---|---|
| RS `b2-r` | **`81d41baebf`** | `rv120_forgeries` (RE `tests/retained_precision_contract.rs`) holds the 4 forgeries as edits on the synthetic exact base and lane P's sparse m3x successor; the 07e rehash recomputes the rest. They join the B3b shape list (169 shapes) at G8 `PREPARATION_MISMATCH`. New test: `b3b_rv120_f2_forgeries_are_refused_at_g8_step_4`. |
| TS `b2-t` | **`58fa652cc8`**, head **`65c04cd0c7`** (merge of `b2-r` at `81d41baebf`) | The same four, the same shape list, and the same test with the same pins. The shape-list test is renamed from "165 shapes" to "169 shapes". |

**The forgeries are RV120's inputs** (`readers/IDENTITY.txt`). Each materialized forgery equals RV120's input line as a value, and RV120's own `input_sha256` (its `INPUTS_INDEX.jsonl`) matches all four. Both languages' tests pin the sha256 of the canonical `[source, invocation]`:
- `97566866…` (E, synthetic);
- `6e67243c…` (Ĝ, synthetic);
- `3828c07c…` (E, m3x);
- `c17c8283…` (Ĝ, m3x).

## Mutants at the repair heads (each with a passing control)

| Mutant | RS (`81d41baebf`) | TS (`65c04cd0c7`) |
|---|---|---|
| B28: step 4's E bits unchecked | **killed**: the new test and the shape list | **killed**: the new test and the shape list |
| B29: step 4's Ĝ bits unchecked | **killed**: the same | **killed**: the same |

## Evidence at the repair heads

- **Census:**
  - 07m: 0 changes in RS and TS (339 entries, against I100's I4′ census).
  - 07n: 0 changes in RS and TS (638 entries, against I100's census at SC's head).
- **Suites against `e67c364680`:**
  - RE at RS's head: 196 → **203 ok** (+7).
  - RE at TS's head: 196 → **206 ok** (+10).
  - Vitest: 3,637 → **3,678 passed** (+42 added; D31 renamed).
  - `tsc`: rc 0.
  - PY carrier schemas: 1,202 → **1,205 passed** (+3).
- **Suites against the previous heads:** only the new test is added (1 RE test per head, 1 vitest), and the TS shape-list test is renamed (declared above). Nothing else changes.
- **Three readers:** 169 shapes, with PY (I100's repair head `6d3d4cdca6`) reading RS's inputs. RS = TS = PY on bound, unbound and transport, except G7's per-reader base codes.
  - **The four forgeries:** all three readers give G8 `PREPARATION_MISMATCH` bound, and neither error nor eligibility unbound or on transport.
  - **Bound totals:** eligible 5, G0 40, G1 3, G5b 36, G7 9, G8 76.
- **PP:** its 20 B3 tests pass at TS's head.

## Host

- Cargo ran through `t3_cargo.sh --locked --offline`, other heavy work through `t3_slot.sh`, one heavy job of mine at a time. I stopped and restarted only my own timed-out waiters. No DEC-025, no installs.
- **Disclosed:**
  - **Removed helper binaries:** the chain's first PY schema and PY shapes runs failed at once (`CHECKED-JSON-AUTHORITY-MISSING`). My earlier cleanup had removed the helper binaries, which were not rebuilt. I rebuilt them through `t3_cargo.sh` (`py_helpers.sh`) and reran both; the failed logs are kept (`logs/final3_py_schema.log.gz`, `logs/final3_py_shapes.log.gz`).
  - **Queue wait:** while an exclusive DEC-025 job held the slots, my dev job waited in the queue.

## Stop

None.

## Records

`_run_records/repair_01/` holds `harness/`, `mutants/`, `readers/`, `census/`, `suites/` and `logs/`; sums are in `SHA256SUMS.repair_01`.
