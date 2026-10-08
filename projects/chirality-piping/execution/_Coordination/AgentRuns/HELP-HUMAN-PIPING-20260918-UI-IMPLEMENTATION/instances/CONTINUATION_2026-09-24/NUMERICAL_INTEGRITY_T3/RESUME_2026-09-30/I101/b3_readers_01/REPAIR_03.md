# I101 B3 readers, repair 03: N2b fixed in RS, the hash-order class closed, and the N2b probe pinned in all three readers

TASK (Type 2), I101, for WORKING_ITEMS for T3 (Agent 1), the return path by the owner's decision of 2026-10-08, as its message stated. I made no delegation. 2026-10-08 UTC.

**Basis:**
- WORKING_ITEMS' repair 03 message: N2b, and closing the class;
- ROOT's rule: a reader's reported code must not depend on hash order on any path;
- my repair 02 record (`REPAIR_02.md`, its open point N2b and the scratch probe).

The lanes start from repair 02's heads: `b2-r` `7873884fb4`, `b2-t` `d933514312` and `b2-p` `101ebcff76`. `b2` itself is untouched.

## Heads (not pushed)

| Lane | Head | Commits |
|---|---|---|
| RS `b2-r` | **`d86c0805c6`** | the N2b fix, the class fix in the preview validator, and the RS pins |
| TS `b2-t` | **`dc6b7359ba`** | merge of `b2-r` at `d86c0805c6` (`41d298abdb`), then the TS pins |
| PY `b2-p` | **`27c45da2ba`** | the PY pin: test and fixture shapes |

The host screen found 0 hits on all three ranges (`7873884fb4..d86c0805c6`, `d933514312..dc6b7359ba`, `101ebcff76..27c45da2ba`).

## N2b: the fix (RS only)

`RE/src/physics_evidence.rs` `validate_physics_evidence_in` (physics-1's base validator; the exact route's G7 on the bound and unbound path) iterated hash maps and sets in loops whose bodies fail with different codes, so its first failure code depended on per-process hash order.

- **The fix:** every such loop now runs in array order, as TS's and PY's do. The maps and sets only detect duplicates and answer lookups.

  | Loop (repair 02's line) | Now (line at `d86c0805c6`) |
  |---|---|
  | cases `:385` | `exact_cases` in array order (`:388`) |
  | each case's materials and sections `:421`/`:424` | `pipe_materials`, `pipe_sections` (`:425`, `:428`) |
  | each case's extrema `:445` | `pipe_stress_extrema` (`:449`) |
  | rows `:514` | `results` (`:519`) |
  | region members (overlap) `:638` | `member_pipe_ids` (`:645`) |
  | region duplicates `:655`/`:660` | `geometry` / `materials` (`:662`) |
  | applied loads `:676` | `applied_loads` (`:684`) |
  | region result ids `:762` | `result_ids` (`:770`) |
  | region members (row coverage) `:765` | `member_pipe_ids` (`:773`) |
  | pressure rows `:805` | `results` (`:814`); one code, converted anyway |
  | assemblies `:810` | `exact_cases` (`:820`) |

- **Verdicts:** unchanged. Every check still runs on every entry; only the order of a refusal's first failure changes.
- **TS and PY:** their reader code is unchanged.

## Closing the class

**RS (all of `RE/src`, retained and physics paths).** Every iteration over a `HashMap` or `HashSet` (and their iterators, `.keys()`, `.values()`, `into_iter`). Candidates: `class/rs_hash_sites.txt` (a finder, then a reading of each site).

| Site (at `d86c0805c6`) | Verdict |
|---|---|
| `physics_evidence.rs` `validate_physics_evidence_in`: the loops above | **fixed** (N2b) |
| `physics_evidence.rs:570` support components `.values()` | one code (`SUPPORT_COMPONENT_COVERAGE`) whatever the order |
| `physics_evidence.rs` `.keys()` at `:340`, `:356`, `:415`/`:417`, `:445`, `:659`, `:681` and in `validate_transport_metadata` | collected into sets for set equality or duplicate detection |
| `physics_evidence.rs:844` `rows.values()` in `.all()` | a boolean (`HEADLINE_MAXIMUM`) |
| `physics_evidence.rs` `validate_transport_metadata` | fixed in repair 02 (N2) |
| **`preview_physics_evidence.rs:573`** supports `actions.values()` (repair 02's `:566`) | **fixed**: two codes (`SUPPORT_COMPONENT_COVERAGE`, `SUPPORT_MAGNITUDE`). Now the order in which each support first appears in the case's rows, as TS's and PY's grouping is |
| **`preview_physics_evidence.rs:710`** combinations `combined.values()` (repair 02's `:695`) | **fixed**: several codes (`COMBINATION_SUPPORT_DUPLICATE`, `COMBINATION_MAGNITUDE_COMPONENTS`, `COMBINATION_MAGNITUDE`). Now first-appearance order in the rows, as TS's and PY's grouping is |
| `preview_physics_evidence.rs:570` `actions.keys()`; other preview sets | set equality, membership, duplicate detection |
| `source_blocks.rs:1176` treatments dependency walk | one code (`ROW_DEPENDENCY_CYCLE`); the walk's result does not depend on order |
| `source_blocks.rs:1581` headline candidates `raw.values()` | rows are prevalidated finite; `number` has one code; the maximum is a fold that does not depend on order |
| `source_blocks.rs` `.keys()` at `:1049`, `:1171`, `:1225`, and `expected` | set equality |
| `source_blocks.rs` treatments | already in receipt row order ("Receipt row order, never hash order") |
| `physics_source.rs` (sets at `:84`, `:373`, `:643`–`:674`, `:989`; a rows map at `:530`) | set equality, duplicate detection, lookups only |
| `load_reference.rs` (`:746`/`:747` maps; sets `:468`–`:906`) | entry consistency, lookups, set equality |
| `derivative.rs`, `semantic_contract.rs` | duplicate-detection sets; `retained_row_classes` returns a map read only by lookup |
| `retained_precision.rs` | `BTreeMap`/`BTreeSet` only (ordered) |
| `lib.rs`, `load_reference_source.rs` | no hashed collection |

Two RS walks iterate a `serde_json` object's values: `finite_tree` (one code) and the preview summary's `result_ref` fields (`preview_physics_evidence.rs:319`). Without `preserve_order` (not enabled in this crate's graph) a `serde_json::Map` is a `BTreeMap`, so these walks are in key order: deterministic, not hash order. TS and PY walk the same objects in insertion order. This is outside the hash-order class, and I changed nothing there.

**PY (`core/analysis_runs/*.py`).**
- **Where hash order can enter:** dicts are insertion-ordered, but a `set` or `frozenset` of `str` iterates in a per-process order (`PYTHONHASHSEED`).
- **Candidates:** the finder (`class/py_set_sites.txt`, an AST pass) flags every for-loop or comprehension over a set-valued expression, and every rendering of one (list, tuple, join, `next(iter(...))`, min, max, pop, str, repr, format, `%`, f-string).
- **Reading:** none is order-sensitive.
  - `physics_evidence.py:122`, `:326`: `GEOMETRY - {...}` inside `all(...)`. These are booleans; on transport the schema has already typed the values.
  - `preview_physics_evidence.py:361`, `:363`: sets built from the `records` set, then compared.
  - The other hits are lists that share a name with a set elsewhere in the module: `members` at `:390`–`:401`, `ids` in `retained_precision.py`, `values` in `records.py`.
  - `source_blocks.py:364`: the dependency walk, one code (`ROW_DEPENDENCY_CYCLE`).
- **Elsewhere:** no reader module reads an unordered source (no directory listing or glob). Set-typed parameters are compared, never iterated.
- **Grouping:** PY groups supports and combinations in row order (dicts).

**TS (`features/results` readers).**
- **Insertion order:** Map, Set and object keys all iterate in insertion order; integer-like object keys come first, in a fixed order.
- **Candidates:** `class/ts_iteration_sites.txt`.
- **Reading:** no reader builds a Set or Map from an unordered source. Every `Object.keys`, `Object.values` or `Object.entries` walk is over a constant table or an input object in its own key order, or feeds a boolean. Nothing is order-nondeterministic.
- **Grouping:** TS groups supports and combinations in row order (`grouped`, `combinationRows`). This is the order RS now uses.

## The pins

| Reader | Pins |
|---|---|
| RS | `repair03_probes` puts the N2b probe (entry 0's `profile_mode` "x", entry 1's `material_basis` 0) and its swap on the exact `two_case_synthetic` into the B3b shape list, now 177 shapes. They expect G7 `SOURCE_PHYSICS_CASE_PROFILE` and `SOURCE_PHYSICS_STRING_INVALID`: entry 0's fault in each case. The new test `b3b_repair03_n2b_physics_code_is_array_ordered_and_stable` reads each 64 times. Bound and unbound always give entry 0's code; transport always gives `SOURCE_PHYSICS_TRANSPORT_SHAPE`. It also pins the canonical input digests `ab2807e3…` and `9451b827…`. Two preview tests read each fault pair 64 times, both ways round: `repair03_support_faults_are_read_in_row_order` (S-100's force magnitude and NL-140's missing `Mz` in L-100) and `repair03_combination_faults_are_read_in_row_order` (two admitted combinations, one with its displacement magnitude off and one with its support `Fz` row missing). In each, the earlier support's or combination's fault is the code. |
| TS | The same 2 shapes in the same list; the shape test is renamed 175 → 177 shapes. A new test reads each 8 times. TS's single case check fails on both faults, so bound and unbound always give TS's own G7 `PHYSICS_EVIDENCE_CASE_INVALID`, and transport gives `PHYSICS_EVIDENCE_TRANSPORT_SHAPE`. The digests are the same as RS's. |
| PY | RV120's fixture gains the 2 shapes. Each is stated as edits from the corpus `two_case_synthetic` and re-materializes through `rv120_input` to the RS input's `input_sha256` (RV120's formula): `4b0c7b62…` and `53127951…`. `test_repair03_n2b_reads_the_cases_in_array_order` reads each 8 times. Bound and unbound give G7 `case profile/material basis` (PY's one case check fails on both faults); transport gives `transport evidence shape`. |

Under the C1 G7 settlement each reader names its own code. In RS the two faults have distinct codes, so RS's pin shows the order itself; TS's and PY's pins show their codes are stable.

## Mutants (with a passing control)

| Mutant | Result |
|---|---|
| control (the copy at `d86c0805c6`, `retained_precision_contract` and `preview_physics_contract`) | passes: 87 and 21 tests |
| N2bH: physics-1's base validator reads the cases in `HashMap` order again (`physics_evidence.rs`) | **killed** by `b3b_repair03_n2b_physics_code_is_array_ordered_and_stable`: on run 0 the probe read bound `SOURCE_PHYSICS_STRING_INVALID`, entry 1's fault. Also killed by `b3b_exact_successor_shapes_first_failures`, where both N2b shapes read the other entry's code. |
| PSH: the preview validator reads its supports in `HashMap` order again | **killed** by `repair03_support_faults_are_read_in_row_order`: run 1 read `SUPPORT_COMPONENT_COVERAGE` |
| PCH: the preview validator reads its combinations in `HashMap` order again | **killed** by `repair03_combination_faults_are_read_in_row_order`: run 0 read `COMBINATION_MAGNITUDE_COMPONENTS` |

## Evidence at the heads

- **Census, 0 changes in all three readers:**

  | Reader | 07m (339 entries) | 07n (638 entries) |
  |---|---|---|
  | RS | 0, against I100's I4′ census | 0, against SC's head |
  | TS | 0, against I100's I4′ census | 0, against SC's head |
  | PY | 0, against I100's addendum-01 census (I100's harness, unchanged) | 0, against I100's addendum-01 census |

- **Suites, only added tests change** (base: repair 02's heads):

  | Suite | Repair 02's heads | Repair 03's heads | Change |
  |---|---|---|---|
  | RE at RS's head | 204 | **207** | +3: the N2b test and the two preview tests |
  | RE at TS's head | 207 | **210** | +3: the same |
  | Vitest | 3,679 | **3,680** | +1, the N2b test; my shape-list test renamed 175 → 177 shapes |
  | PY B3 and contract modules | 806 (`101ebcff76`) | **808** | +2, the N2b test's two parameters |

  - `tsc` rc 0.
  - PY carrier schemas at TS's head: 1,205 passed and 29 skipped (unchanged).
  - PP's 20 B3 tests pass.
- **Three readers:** 177 shapes; PY at `27c45da2ba` read RS's inputs, and TS's inputs equal RS's as JSON values (177 of 177).
  - RS = TS = PY on bound, unbound and transport, except G7's per-reader base codes.
  - G7 now shows 19 code triples, up from 15: the N2b shapes add 4 (bound and unbound, each with RS's `CASE_PROFILE` or `STRING_INVALID`, against TS's `CASE_INVALID` and PY's `EVIDENCE_INVALID`).
  - **The N2b shapes:** G7 bound and unbound, and G7 transport by the shape, in all three readers.
- **Identity:** `readers/IDENTITY.txt`.

## Host

- **Jobs:**
  - Every cargo run went through `WT/tools/t3_cargo.sh --locked --offline` with toolchain 1.97.1 (targets `WT/targets/i101-b3r-*`, removed afterwards). This includes the PY helper binaries (`py_helpers.sh`, plus the binary64 profile for PY's census).
  - Other heavy jobs went through `t3_slot.sh`.
  - One heavy job of mine at a time, one wait per job, and I signalled no other job.
  - No DEC-025 and no installs.
- **Light work, run directly:**
  - the PY fixture generation (`gen_py_n2b.py`), in an archive copy;
  - `rustfmt --check` on the changed RS files (the two source files and the preview test file are clean; `retained_precision_contract.rs` was not rustfmt-clean before this repair);
  - the class finders (`hash_sites.py`, `py_set_sites.py`).
- **Copies:** vitest ran in archive copies with `node_modules` linked after a `cmp` of `package-lock.json` and the eight wasm assets copied, never built.
- **Junit:** host attributes were removed.

## Records

- **Location:** `_run_records/repair_03/` holds `harness/`, `class/`, `mutants/`, `readers/`, `census/`, `suites/` and `logs/`.
- **Sums:** in `SHA256SUMS.repair_03`.
- **Paths:** placeholders only.
