# I100 B1-SC: corpus 07n and PY's harness pins

TASK (Type 2), I100 (I-PY, the one corpus writer), for ROOT (HELP_HUMAN, Agent 0), the return path. I made no delegation. 2026-10-08 UTC.

**Basis:**
- `R/BRIEFS/B1_SC.md`, sha256 `58ca61740cb17e2e83a0b4622bf7c165e3a7f925ecd685a5ddd0884a642cce6e` (with I4′);
- PLAN_v2 §2.5 and DESIGN_v2 §2–§3;
- the coordinator's rulings relayed in this round:
  - the two extrema shapes pin gate and code only;
  - RV120's A-N1 (transport metadata detail texts are declared, not pinned) and A-N2 (the unsafe `span_index` and PY's 16,384-item bound are declared and unpinned);
  - a negative or zero bound pins nothing.

**Placeholders:** `WT`, `NUM`, `P`, `R`, `VENV`; `S` = `WT/scratch/i100_b1_sc`.

## Result

- **HEAD = `09fe4cc69bce6b48621d4c4c3bc455e9ff32a5d8`** on `codex/piping-t3-b1-20261007` in `WT/b1`: one commit on I4′ `8d46b045e2`. Not pushed.
- **The commit changes two files:**
  - the corpus: +283,214 lines, 0 deleted, so 07m's text is untouched;
  - `tests/test_retained_precision_contract.py`: +130 −11, PY's pins.
- **07n:** `P/fixtures/results/retained_precision_cases.json`, sha256 **`ea113e7b25b96cbabcbd3fe43a8604da38a67e681f8a5ab3ad490eb37313e283`** (16.2 MB; 07m was `c21112fd…`, 5.5 MB).

| Kind | 07m | 07n | Added |
|---|---|---|---|
| Bases (`cases`) | 17 | 26 | 9 |
| Mutations | 294 | 534 | 240 |
| Must-pass | 28 | 78 | 50 |

**Bases added:**
- `w_c2_sparse_interactive` and `w_c2_dense_scrutiny`: D-U6-5 copies of I85's fixtures;
- `d38_beside_selected`: synthetic, "not producer-emittable under T-8". It is W-C2 sparse rewritten by DESIGN_v2 §2's derivation and resealed; it passes G0–G8 with `needs_recompute`;
- `cause_milestone_reversed_*`, `sf2_c_b_a_*` and `sf2_a_a2_*`, both modes. These are copies of the successors that PP's own tests pin. I dumped them from those tests in a scratch copy, after each test's pin assertion held: receipt and bytes sha256 equal `REVERSED_PINNED`, `CBA_PINNED` and `AA2_PINNED` (`pp_dump/`).

**Entries added (290; `corpus/ENTRIES.tsv` lists each one, with its base, item, origin and every reader's three reads):**
- **Item 1, D38 m1–m9 on `d38_beside_selected`** (9):
  - m4 is G3 COVERAGE and m7 is G5 ATTEMPT, as I90 noted;
  - m1 sets the whole error value;
  - m9 keeps case C's Builds and reads G5 WORK.
- **Item 2, F-1's five:** P1–P4 and the requested mode, each G8 PREPARATION. Also RV113's 20 G8 probes, including the copied parity row's `recovery_method` at G6 (item 10), and the 4 disclosed-limit probes.
- **Item 3, `not_required` on W-C2 case B** (3): sensitive verdict, `not_attempted`, and case B's own product attempt. Each reads G5 ATTEMPT. Also RV113's 17 `not_required` probes.
- **Item 7:**
  - (f), 17;
  - (g), 25;
  - C2: C-a 21, C-b 12, the precondition keying 30 (each key's own code at routing and preparation, the wrong phase, and each wrong code), C-c 6, C-d 5, and the whole-reader set 6;
  - the transport header H, 31;
  - the transport metadata T, 40, plus 2 from `r2x`.
- **Items 8–9:** I91's (b), (c), (d1), (d2) and (e), with the control and the basis count (17). The brief's "(a)" has no counterpart in RR, which rules (b)–(e).
- **Item 11:** RV108 N1 (the 8 list and dict enums), N2 (1, on W-C2 case B) and N4 (5).
- **Items 12–14:**
  - the compound N6 pair and `h_formulation_limitations_other`;
  - ruling 1's six header probes;
  - ruling 2's three shapes on transport, and ruling 3's extrema pair, bound and unbound;
  - ruling 5's `cb_kernel_no_run`;
  - (4a)'s three probes and RV113's orphan-source audit.

**Every first failure is the three readers' agreement at I4′.** `scripts/gen_07n.py` (step 1) and `scripts/fix_07n.py` (step 2) write the corpus. Each entry also carried its design expectation, and every one matched. My first draft had four construction slips, all corrected before 07n was fixed, with no reader involved:
- m1 lacked the run reference;
- two parity rows were inserted mid-list;
- `not_attempted` lacked its cause.

**Format (additive; 07m's entries carry none of these):**
- every 07n entry states `expected_unbound`, or `expected_unbound_by_reader` beside `expected_by_reader`;
- every 07n entry states `expected_transport`, as `"pass"` (admitted, not eligible) or a gate and code;
- 16 admitted rewrites whose classes differ from their base's state `expected_classifications`. All three readers' must-pass rules compare the base's classes today. Without this field, an admitted rewrite that unselects a case cannot be a must-pass entry;
- detail texts are not pinned (A-N1).

**Per reader: 45 entries, all in one declared form.** Python and TS share the expectation at G7, and Rust gives its own raw G7 code (bound and unbound):
- 39 are evidence defects, Rust's specific code: 36 T probes (the multiset probe and ruling 3's extrema pair among them), the 2 `r2x` probes and `h_formulation_limitations_other` (item 12);
- 6 are the compound and carrier header probes (item 13; `h_carrier_present`'s Rust code is `…FOREIGN_METHOD_EVIDENCE`).

**No new disagreement.** At I4′, no 07n entry has a bound read that differs outside that form, and no entry has a transport read that differs at all.

## Acceptance, at the SC head

The run used a `git archive` of `09fe4cc69b`, whose tree equals I4′ plus the commit. RV113's harnesses were added in scratch, printing each reader's full classifications (`scripts/harness_patches/`).

| | Python | Rust | TS |
|---|---|---|---|
| **07n: every stated check** (bases: bound with eligibility and classes, unbound, transport; mutations; must-pass with eligibility and classes; unbound and transport where stated) | **1,374 of 1,374** | **1,374 of 1,374** | **1,374 of 1,374** |
| **07m census against I4′** (339 entries × 3 reads, detail and input hash included) | **0 changes** | **0 changes** | **0 changes** |
| The reader's own corpus tests | **1,131 passed, 0 failed** (contract, schema and carriers, with my pins) | 19 fail, all pins for I-RS (below) | 20 fail, all pins for I-TS (below) |

- **I-RS's pins** (I101; `acceptance/own_rs.log.gz`):
  - 17 `snapshot_*_mutation_outcomes` assert `mutations.len() == 294`;
  - `snapshot_07m_mutation_outcomes` lists `mutations[286..]` as 07m's eight;
  - `shared_must_pass_entries_validate` asserts 28 entries and compares each with its base's classes. It should read `expected_classifications`.
- **I-TS's pins** (`acceptance/own_ts.json.gz`):
  - 16 must-pass tests compare with the base's classes;
  - three 07l count and slice tests;
  - SR-TS repair 01's list of G2-on-transport mutation indices, which now includes 07n's.
- **Both** should read `expected_unbound`, `expected_unbound_by_reader` and `expected_transport`, as PY's new `test_snapshot_07n_unbound_and_transport_reads` does.
- **PY's pins:**
  - the 07m count test reads 07m's slices;
  - must-pass entries use `expected_classifications` when stated;
  - three new tests pin 07n's counts and format, its 290 entries' unbound and transport reads, and its bases (the fixture and PP pins, and the D38 derivation re-run).
- **T-12 (SP's several-notice bytes; I85 `final/t12_bytes`, sealed sums verified): PY passes** (`t12/T12_PY.json`). Both modes' noticed envelopes (plain, and with the receipt detail) read as the base: the same raw and transport contract, `needs_recompute`, the same binding refusals and summary, and an AnalysisRun that validates. Each has two notices. TS's check is I-TS's.

## For ROOT

1. **Format:** the four fields above are additive. I-RS and I-TS need to read them (their pin round).
2. **Breadth of the declared per-reader form:** 39 of the 45 entries rest on the "Rust's specific raw evidence code" form that entry 139 and ruling 3 declare, extended to RV113's T probes (RV113's RS addendum 02, N-3). Confirm, or tell me to drop their bound expectation.
3. **Not done here, needing an RS pin:**
   - RV108 N6(b), the carrier case file's scope sentence. RS's `retained_precision_carriers.rs:861` pins the old phrase "Rust and Python the reader's G0 code or their base header code", so the wording and RS's pin must change together;
   - I83 §7 item 8, Rust's `slice_outcomes` ids.

   Both fit I101's pin round.
4. **Size:** 07n is 16.2 MB. Every reader parses it per test, and PY's three retained files took 7 min 12 s in a slot.

## Host and records

- **Heavy jobs: 32,** each through `WT/tools/t3_slot.sh` or `t3_cargo.sh`, one at a time and none overlapping (`host/cargo_jobs_i100_sc.log`). They were:
  - the readers' census runs;
  - PP's two pinned tests, with the scratch dump;
  - the own-suite runs and the PY pin run.
- **The scratch merge:** before I4′ existed, I prepared on a scratch merge of the three heads, `git archive` copies only. Its tree equals I4′'s (`static/merge_copies.txt`).
- **Light work outside a slot:** the generator, fixer and evaluators (JSON, plus PY validating the nine bases) and the T-12 check.
- **Waits:** one background completion per chain. No process of mine remains, and I signalled or killed no job.
- **Records:**
  - placeholder paths only, junit `hostname` attributes removed, no symlink, no folder named `build`;
  - screened with the host screen's patterns and the machine's names, `.gz` files decompressed: 0 hits;
  - `git status --ignored` shows nothing ignored.

  `SHA256SUMS` covers `_run_records/`.
- **Cleanup:** the scratch trees and SC targets are deleted. The scripts and outputs stay in `S/`.
