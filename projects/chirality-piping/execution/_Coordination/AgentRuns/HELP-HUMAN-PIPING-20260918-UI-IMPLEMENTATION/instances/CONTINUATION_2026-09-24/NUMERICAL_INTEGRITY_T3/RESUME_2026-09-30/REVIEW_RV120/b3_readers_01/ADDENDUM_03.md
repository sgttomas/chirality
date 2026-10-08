# RV120 (RV-R2) ADDENDUM_03: (B) repairs 02 and 03 — CONFIRMED; N2 and N2b closed; the class inventory is complete

TASK (Type 2), RV120. Requested by WORKING_ITEMS for T3 (Agent 1), my return path. No delegation; I wrote none of the change. 2026-10-08 UTC.

## Basis

- **Candidates (repair 03):**
  - RS `b2-r` `d86c0805c6`: the N2b fix, plus the preview supports and combinations, plus the RS pins.
  - TS `b2-t` `dc6b7359ba`: merges `b2-r` at `41d298abdb` and adds the TS pins.
  - PY `b2-p` `27c45da2ba`: the shapes and the test.
- **Record:** `R/I101/b3_readers_01/REPAIR_03.md` (`a119c3ef…`; SHA256SUMS.repair_03 80 of 80). I read its inventory after my own pass.
- **Candidate under test, `m2`:** the dry-merge equivalent. It is `git archive` of `b2` `0ef9a8ace9` (the B3a drop, confirmed in ADDENDUM_02) with `65c04cd0c7..dc6b7359ba` and `6d3d4cdca6..27c45da2ba` applied by `patch`. Both applied cleanly. `physics_evidence.rs`, `preview_physics_evidence.rs`, `preview_physics_contract.rs` and the RV120 fixture equal the heads' bytes, and the reader sources equal `0ef9a8ace9`'s.
- **Baseline:** ADDENDUM_02's runs (`m1`; PY base `m0` = `51f339a11e`).

## The fixes

- **N2b, RS `physics_evidence.rs` `validate_physics_evidence_in`.** Every loop that can fail now walks the input arrays: the cases, materials, sections and extrema, the rows (both walks), the region members, duplicates and applied loads, the result ids, and the final `assembly` pass. The maps and sets (`indexed`, `strings`) are used only for duplicate refusal and lookups. Both helpers refuse a duplicate before any loop runs, so walking the array checks exactly the set the map held: the semantics are unchanged.
- **The class extension, RS `preview_physics_evidence.rs`.** Supports (two codes) and combinations (three codes) are now checked in the order each first appears in the rows. That is TS's and PY's grouping order.

## The class inventory: complete

My own pass, before reading I101's (`addendum_03/harness/class_scan.sh`, output `suites/CLASS_SCAN.txt`), found the same sites:

- **RS reader modules** (`retained_precision`, `physics_evidence`, `preview_physics_evidence`, `physics_source`, `semantic_contract`, `source_blocks`, `derivative`): 26 iteration sites over names bound to a `HashMap` or `HashSet`. Read by hand, each now falls into one of four kinds:
  - array order (the fixed loops);
  - collected for set equality or duplicate detection;
  - a boolean `.all()`;
  - a loop whose only failure is one code. These are `physics_evidence.rs:570` `SUPPORT_COMPONENT_COVERAGE` and `preview_physics_evidence.rs:430` `STRESS_COVERAGE_PARTITION`.

  `retained_precision.rs` uses only `BTreeMap` and `BTreeSet`. `serde_json::Map` iterates in key order (BTreeMap; `preserve_order` is not enabled), so it is deterministic.
- **PY** (`core/analysis_runs`, AST pass): 21 hits over set-valued expressions. None is order-sensitive:
  - `sorted(…)` is deterministic;
  - `all(…)`/`any(…)` are booleans. On transport, `physics_evidence.py:326` sees schema-typed values. On raw reads, `:122` guards with `_number` and the wrapper maps any error to the one code;
  - sets built from sets are only compared;
  - other hits are lists that share a name with a set elsewhere.

  Dicts iterate in insertion order.
- **TS:** Map, Set and object keys iterate in insertion order, so TS has no hash-order class.
- **I101's inventory** names the same sites with the same verdicts, plus `load_reference*.rs`, which is outside the B3 reader paths.

**Completeness:** I found no order-sensitive site that is unfixed or unnamed. I also checked this empirically, below.

## Evidence at `m2`

- **Hash-order independence, broadly:**
  - all 679 of my inputs (128 probes, 4 forgeries, 177 shapes, I100's 52 and 318);
  - RS: two more fresh processes against the first run: **0 differences** in any verdict or detail;
  - PY under `PYTHONHASHSEED` 1 and 2 against the default random seed: **0 differences**, details included;
  - N2's probe: RS transport `SOURCE_PHYSICS_TRANSPORT_MAXIMUM_RESULT` in 5 of 5 processes;
  - the two N2b shapes: RS reads entry 0's fault in both orders (`SOURCE_PHYSICS_CASE_PROFILE`; `SOURCE_PHYSICS_STRING_INVALID`). TS and PY read their own single G7 codes.
- **Three-reader agreement:** 0 differences outside G7 on 128 + 4 + 177 + 52 + 318 inputs. The only missed expectations are B3a's three retired admissions, which are INV in all three readers (ADDENDUM_02).
- **No other outcome moved:** I compared 6,093 readings with ADDENDUM_02's; **0 moved**. The only new inputs are the two N2b shapes.
- **Census:** 0 changes and 0 misses in RS, TS and PY, for 07m (339 entries) and 07n (638).
- **Suites, test by test, against ADDENDUM_02:**
  - **RE:** 212 → **215**, +3: `repair03_support_faults_are_read_in_row_order`, `repair03_combination_faults_are_read_in_row_order` and `b3b_repair03_n2b_physics_code_is_array_ordered_and_stable`.
  - **vitest:** 3,684 → **3,685**: +1 (repair 03's N2b test), and the shape pin's title renamed from 175 to 177 shapes.
  - **tsc:** rc 0.
  - **PY's seven files:** 1,736 → **1,738**, +2 N2b pins (1,704 → 1,738 against `51f339a11e`).
  - No outcome was changed or failed. My copies' counts include my five no-op harness tests.
- **Mutants:** I101 reports N2bH, PSH and PCH killed by 64-run pins, with a passing control. I did not re-run them. The RS pins I ran assert a single code across 64 runs and pass.

## Findings

| # | Status | Line |
|---|---|---|
| N2 | **Closed** | RS's transport check is array-ordered, stable (5 of 5) and pinned in all three readers |
| N2b | **Closed** | RS's raw physics-1 check is array-ordered: it reads entry 0's fault in both orders, stable across processes, pinned |
| Class | **Complete** | RS's preview supports and combinations are fixed too. No other order-sensitive site in RS or PY, and TS is ordered by construction. 679 inputs read identically across RS processes and PY hash seeds |
| (A) | Unchanged | The B3a drop stays confirmed (ADDENDUM_02). Nothing moved |

## Verdict

**(B) CONFIRMED.** Repairs 02 and 03 close N2 and N2b. Together with (A) in ADDENDUM_02, the reader lanes may merge into `b2`. That covers `b2-t` (`dc6b7359ba`, carrying `b2-r` `d86c0805c6`) and `b2-p` (`27c45da2ba`), on `0ef9a8ace9`.

## Host

- **Jobs:**
  - Every cargo run went through `WT/tools/t3_cargo.sh --locked --offline` (target `WT/targets/rv120b3-m2`).
  - Every other heavy job went through `WT/tools/t3_slot.sh`, one heavy job of mine at a time.
  - No Git writes: I used `git show`, `git diff` and `git archive` only, and built `m2` with `patch`.
  - No DEC-025, no installs and no measurements.
- **Record:** `addendum_03/host/job_stamps.txt`. Placeholders as before.
