# I101, 07n pins, addendum 01: ruling 3 (RV108 N6(b)) applied

TASK (Type 2), I101, for ROOT (HELP_HUMAN, Agent 0). I made no delegation. 2026-10-08 UTC.

**Basis:**
- ROOT's message after RETURN.md (sha256 `6343e404…5768`), which accepted the pins and ruling 4's reading;
- ROOT's instruction to apply `N6B_PROPOSED.diff` as one commit, PY's test line included (a one-off authorization for `tests/test_retained_precision_carriers.py:364`), and then run the three affected tests.

## The commit

**HEAD = `57c92a7b33`** on `codex/piping-t3-b1-20261007` in `WT/b1`. It is one commit on `901745f46b`, not pushed, and is the patch exactly as proposed (`_run_records/addendum_01/commit.diff`). It changes 4 files, +5/−5:

| File | Change |
|---|---|
| `P/fixtures/results/retained_precision_carrier_cases.json` | The scope's "Rust and Python the reader's G0 code or their base header code" becomes "Rust and Python the reader's G0-G2 code or its base step's code" (RV108's wording, ASCII; the file stays pure ASCII) |
| RS `RE/tests/retained_precision_carriers.rs` | Pins the new phrase and refuses the old one |
| TS `…/results/retainedPrecisionIntegration.test.tsx` | Pins the new phrase |
| PY `P/tests/test_retained_precision_carriers.py:364` | Pins the new phrase (the authorized line) |

No reader source changed.

## The three tests, at `57c92a7b33`

Each ran in a `git archive` copy of P without `execution/`, as one heavy job, one at a time:

| Test | How | Result |
|---|---|---|
| RS `retained_precision_carriers` | `WT/tools/t3_cargo.sh test --locked --offline --test retained_precision_carriers`, fresh target | **17 passed, 0 failed** |
| TS `retainedPrecisionIntegration.test.tsx` | vitest through `WT/tools/t3_slot.sh`; `node_modules` linked (lock `cmp`-equal) and the eight wasm assets copied (hashes equal I4's) | **180 passed, 0 failed** |
| PY `tests/test_retained_precision_carriers.py` | `VENV` pytest through `WT/tools/t3_slot.sh` (`-p no:cacheprovider`, no bytecode, basetemp in scratch) | **52 passed, 0 failed** |

**PY's binaries** are I100's existing builds. Only the two variables ROOT named were set, and `OPENPIPESTRESS_BINARY64_JSON_BIN` was explicitly unset. PY's test needed nothing else.

| Variable | Binary | sha256 |
|---|---|---|
| `OPENPIPESTRESS_CHECKED_JSON_BIN` | `WT/targets/i100-b1-i4p-py/checked-json/release/openpipestress_jcs_ijson` | `549cc2ca…d9a9` |
| `OPENPIPESTRESS_UNITS_BIN` | `WT/targets/i100-b1-i4p-py/units-authority/release/openpipestress_units` | `57064fa9…4a33` |

The full hashes are in `_run_records/addendum_01/py_bins.sha256`.

## Host and records

- **Jobs:** 3, each the only heavy job of mine, with 3 STARTs and 3 ENDs in my job-log lines. One waiter, the chain's background completion, ended with the chain. No job was signalled.
- **Cleanup:** the copy (link removed first) and the target `WT/targets/i101-b1-sc-pins/` are deleted.
- **`_run_records/addendum_01/`:** `commit.txt`, `commit.diff`, `chain_n6b_head.sh`, the chain output and the three job logs, `py_bins.sha256`, `cargo_jobs_a1.log` and `wasm_n6.sha256`.
- **Hygiene:** placeholder paths only; no symlink or `build` folder; no junit. The screen (the host screen's patterns and the machine's names, `.gz` decompressed) and `git status --ignored` results are below.
- **Sums:** `SHA256SUMS.addendum_01` covers this file and `_run_records/addendum_01/`. The original `SHA256SUMS` is unchanged.

**Screen:** 13 files (ADDENDUM_01.md, SHA256SUMS.addendum_01 and the 11 in `_run_records/addendum_01/`), 0 hits, 5 names screened. **`git status --ignored`:** every file of the folder untracked, none ignored, so nothing needs force-adding.
