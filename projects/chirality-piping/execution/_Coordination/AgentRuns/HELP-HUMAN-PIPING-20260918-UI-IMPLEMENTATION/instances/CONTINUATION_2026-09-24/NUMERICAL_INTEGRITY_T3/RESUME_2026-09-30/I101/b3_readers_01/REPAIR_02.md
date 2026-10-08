# I101 B3 readers, repair 02: RV120's N2 fixed in RS, and its N2 and F1 probes pinned in all three readers

TASK (Type 2), I101, for WORKING_ITEMS for T3 (Agent 1), the return path by the owner's decision of 2026-10-08, as its message stated. I made no delegation. 2026-10-08 UTC.

**Basis:**
- WORKING_ITEMS' message ruling N2 and F1's pins;
- RV120's `R/REVIEW_RV120/b3_readers_01/ADDENDUM_01.md` (`9a4b3abf…`; `SHA256SUMS.addendum_01` verified);
- its `evidence/readers/INPUTS_INDEX.jsonl` and `gen_b3_probes.py`.

The lanes start from `b2-r` `81d41baebf`, `b2-t` `65c04cd0c7` and `b2-p` `6d3d4cdca6`. `b2` itself is untouched.

## Heads (not pushed)

| Lane | Head | Commits |
|---|---|---|
| RS `b2-r` | **`7873884fb4`** | the fix and the RS pins |
| TS `b2-t` | **`d933514312`** | merge of `b2-r` at `7873884fb4` (`d602f7936c`), then the TS pins |
| PY `b2-p` | **`101ebcff76`** | the PY pin: test and fixture |

The host screen found 0 hits on all three ranges.

## N2: the fix (RS only)

`RE/src/physics_evidence.rs` `validate_transport_metadata` iterated hash maps and sets: the cases, and each case's materials, sections and maxima, and each pressure region's members. Its first failure code therefore depended on per-process hash order.
- **The fix:** these loops now run in array order, as TS's and PY's do. The maps and sets only detect duplicates and answer lookups.
- **Verdicts:** unchanged. Every check still runs on every entry.
- **TS and PY:** their reader code is unchanged.

## The pins (all on RV120's inputs)

Each probe re-materializes to RV120's `INPUTS_INDEX` `input_sha256`; all 6 match (`readers/IDENTITY.txt`).

| Reader | Pins |
|---|---|
| RS | `rv120_probes` puts N2's extra `exact_cases` entry on 2 bases, and F1's 4 G5b probes, into the B3b shape list (175 shapes). The new test `b3b_rv120_n2_transport_code_is_array_ordered_and_stable` reads N2 64 times per base: bound and unbound always give G7 `SOURCE_PHYSICS_NUMERICAL_CASE_COVERAGE`, transport always `SOURCE_PHYSICS_TRANSPORT_MAXIMUM_RESULT`. It also pins the canonical input digests. |
| TS | The same 6 shapes in the same list. A new test reads N2 8 times per base: bound and unbound `PHYSICS_EVIDENCE_CASE_COVERAGE`, transport `PHYSICS_EVIDENCE_TRANSPORT_MAXIMUM_ID`, with the same digests. |
| PY | RV120's fixture gains the 2 N2 shapes, as edits from bases its tests hold. `test_repair02_rv120_n2_reads_the_cases_in_array_order` reads each 8 times: bound and unbound `case coverage`; transport `transport maximum result ID`. F1 was already pinned by I100. |

## Mutant (with a passing control)

| Mutant | Result |
|---|---|
| N2H: the transport check's cases read in `HashMap` order again (`physics_evidence.rs`) | **killed** by `b3b_rv120_n2_transport_code_is_array_ordered_and_stable`. Run 2 of the 64 read `SOURCE_PHYSICS_RHS_METHOD`. |

## Evidence at the heads

- **Census, 0 changes in all three readers:**

  | Reader | 07m (339 entries) | 07n (638 entries) |
  |---|---|---|
  | RS | 0, against I100's I4′ census | 0, against SC's head |
  | TS | 0, against I100's I4′ census | 0, against SC's head |
  | PY | 0, against I100's addendum-01 census (I100's harness, unchanged) | 0, against I100's addendum-01 census |

- **Suites, only added tests change:**

  | Suite | Base | Repair 01's heads | Repair 02's heads | Change |
  |---|---|---|---|---|
  | RE at RS's head | 196 (`e67c364680`) | 203 | **204** | +1 |
  | RE at TS's head | 196 (`e67c364680`) | 206 | **207** | +1 |
  | Vitest | 3,637 (`e67c364680`) | 3,678 | **3,679** | +1, and my shape-list test renamed 169 → 175 shapes |
  | PY B3 and contract modules | 804 (`6d3d4cdca6`) | — | **806** | +2 |

  - `tsc` rc 0.
  - PY carrier schemas at TS's head: 1,205 (unchanged).
  - PP's 20 B3 tests pass.
- **Three readers:** 175 shapes; PY at `101ebcff76` read RS's inputs.
  - RS = TS = PY on bound, unbound and transport, except G7's per-reader base codes (15 triples).
  - **The N2 probe:** G7 bound and unbound in all three. On transport each reader names the copy's repeated maximum result id.
  - **F1's probes:** G5b `SCALE` or `SECTION` as RV120 wants, in all three.

## Open point for WORKING_ITEMS (not changed; outside the ruled item)

**N2b: the same defect in RS's physics-1 base validator on the bound and unbound path.**
- **Where:** `validate_physics_evidence` iterates hash maps and sets in the same way:
  - the cases at `:385` and `:810`;
  - members' materials and sections at `:421`/`:424`;
  - extrema at `:445`;
  - rows at `:514`;
  - region duplicates at `:660`;
  - applied loads at `:676`;
  - region members at `:638`/`:765`.
- **Probe:** a scratch probe in one process, never committed (`harness/n2b_scratch_test.rs`, `harness/n2b_scratch_result.txt`), on the exact `two_case_synthetic` with two faults: entry 0's `profile_mode` and entry 1's `material_basis` non-text.
- **Result:** over 64 runs, the bound and unbound G7 codes each alternated between `SOURCE_PHYSICS_CASE_PROFILE` and `SOURCE_PHYSICS_STRING_INVALID` (4 combinations). The gate and the refusal were stable throughout, and transport was stable after this repair.
- **Suggested fix:** the same array-order treatment, with a pin and a mutant. I did not apply it: the ruling named the transport check.

## Host

- **Jobs:**
  - Every cargo run went through `WT/tools/t3_cargo.sh --locked --offline` (targets `WT/targets/i101-b3r-*`, removed afterwards). This includes the PY helper binaries (`py_helpers.sh`, plus the binary64 profile for PY's census).
  - Other heavy jobs went through `t3_slot.sh`.
  - One heavy job of mine at a time. I stopped and restarted only my own timed-out waiters.
  - No DEC-025 and no installs.
- **Light work, run directly:** the PY fixture generation (`gen_py_n2.py`) ran directly in an archive copy, as light work.
- **The N2b probe:** I appended it to RS's test file in the working tree for one run, then restored the file before committing; it was never committed.
- **Junit:** host attributes were removed.

## Records

`_run_records/repair_02/` holds `harness/`, `mutants/`, `readers/`, `census/`, `suites/` and `logs/`. Sums are in `SHA256SUMS.repair_02`. Paths in the records use placeholders.
