# RV113 (RV-R), addendum 01 to the SR-TS review: confirmation of SR-TS repair round 1 (the three-reader alignment set, TS's side)

TASK (Type 2), RV113, for ROOT (HELP_HUMAN, Agent 0), who is the return path. I made no delegation and wrote none of the change. 2026-10-08 UTC.

## Basis

- **The request:** the coordinator's message. Confirm I92's SR-TS repair 01 against RR "I91's and I92's rounds verified; the header move's nine transport changes ruled in; TS's G3 combinations conjunct moves to G8", and the alignment set's items 1–4 (RR "RV113's three returns verified; …"). Confirm independently:
  1. each item's gate and code, bound and unbound;
  2. the C2 precondition keying;
  3. the header at G2 equal to RS check for check, with the metadata at G7 equal to PY's and RS's;
  4. the conjunct's removal;
  5. the census;
  6. my own mutants.
- **I92's records** (`R/I92/b1_sr_ts_01/`), both verified with their sums:
  - `REPAIR_01.md`, sha256 `592d616432fd39e285a6b9281b5150fbf865358326541b1074fc3278165c6ace` (SHA256SUMS.repair_01, 36 of 36 OK);
  - `REPAIR_01_ITEM3.md`, `8f1fc645ca58bacf076921aae305f448d7adfd9309e383e27f9efe67af4bb613` (SHA256SUMS.repair_01_item3, 13 of 13 OK).
- **The candidate:** `codex/piping-t3-b1-t-20261007` at `6fa6a64658f6e94c817d26e0cab28e5087b2cf01`, the branch tip in `WT/b1-t`. It is three commits over `7e47e51b5d` (`b82b932923`, `1d9455c714`, `6fa6a64658`), touching exactly TS (+38/−10) and TT, `retainedPrecision.test.ts` (+141/−0). My archive copies' files equal `git show` (`static/copies.txt`).
- **Order of reading.** I read the ruling and the diff, then ran my census, probes, suite and mutants, and only then I92's two records.

**Placeholders:** as in my SR-TS review and its addenda. RS is at `6e3e4fe219` (SR-RS round 2, confirmed in `rvr_sr_rs_01/ADDENDUM_02.md`). PY is at `2843a59a16` (SR-PY repair 02, my `rvr_sr_py_01/ADDENDUM_01.md`) and, for the "before" columns, at `11cc14e3e6` (R01).

## CONFIRMED

**SR-TS repair 01 is confirmed.** Each of the three commits does what the ruling says, and nothing else:
- the census over 07m moves exactly the nine ruled transport verdicts, each onto RS's;
- every probe verdict that moved since `7e47e51b5d` (93) moved onto RS's;
- vitest +3 with 0 changed, and tsc is clean;
- all 16 of my mutants are killed by the new tests.

**Findings: 0 blocking, 1 should-fix, 2 notes.** None is in the round's own change:
- S-1 is a pre-existing false accept in TS's raw evidence reader, outside the alignment set;
- N-1 and N-2 are record matters.

## 1. The census over 07m

My harness (`rv113Census.test.ts`, `abcc6e36…`) ran in my copy of the head. It was compared with my census at `7e47e51b5d` (SR-TS review, `ts_head.jsonl`) and with RS at `6e3e4fe219`:
- **339 entries; input 0, bound 0, unbound 0; transport 9;** 0 misses against the corpus's TS expectations (`expected_by_reader.typescript`, else `expected`; must-pass eligibilities and standings; bases).
- **The nine are exactly the ruled ones:** entries 277 and 286–293. Each moves onto RS's G2 reading:
  - five case-enum and member defects, admitted at `7e47e51b5d`: now `SOURCE_NUMERICAL_CASE_INVALID`;
  - the quality status, admitted: now `SOURCE_NUMERICAL_QUALITY_INVALID`;
  - the empty limitations, G7 `…EVIDENCE_INVALID`: now `SOURCE_FORMULATION_BASIS_UNSUPPORTED`;
  - the null `contract_evidence`, G7 `…EVIDENCE_INVALID`: now `SOURCE_PREVIEW_PHYSICS_EVIDENCE_REQUIRED`;
  - `source_block_recovery`, G7 `…EVIDENCE_INVALID`: now `SOURCE_BLOCKS_LEGACY_DOWNGRADE_FORBIDDEN`.

  Six of the nine were admitted on transport before. Those six false accepts are now refused.
- **TS against the other heads, all 1,017 verdicts** (`census/CENSUS_HEADS.json`):
  - **against RS: transport equal on all 339; bound and unbound equal on 338.** The one difference is `g7_maximum_off_enclosure`, the corpus's declared per-reader G7 code;
  - **against PY at `2843a59a16`: equal on all 1,017.**

## 2. Each item on my probes

My 392 probes are the 360 of my SR-RS round-2 confirmation (SR-TS's v5, the (f)/(g) table, the repair-01 table, and the 225 written from the ruling), plus:
- 31 transport header probes (`gen_probes_h.py`);
- one owner-kind probe.

TS at the head, RS at `6e3e4fe219` and TS at `7e47e51b5d` (my earlier run) are compared verdict by verdict (`probes/CROSS_TS1.json`). Of the probes' 430 stated expectations (the r2 and header sets), TS meets all 430, as RS does.

**TS changed from `7e47e51b5d` on 93 verdicts, exactly where the round rules, and every one onto RS's verdict:**
- **(g):** 21 bound verdicts move to G8 INVOCATION:
  - the (f)/(g) table's five;
  - 16 of mine, including two from G3 COVERAGE (the conjunct, §4) and the ordering probe from G8 PREPARATION;
- **the C2 keying:**
  - the 15 cross-code precondition pairs in both admitted phases, bound and unbound (60 verdicts);
  - C-c's cross code (2);
- **the header:** the ten N6 probes' transport verdicts move to G2.

**TS against RS, all three entry points:**

| Item | Probes | TS at `6fa6a64658` |
|---|---|---|
| 1 (f) family | the 16 index, case-list and owner probes; the owner consistent but not the source's case | **G3 COVERAGE bound and unbound**; the consistent owner is G5 ATTEMPT. **Equal to RS** |
| 1 ordinary basis | dangling, omitted, the three repair-01 inputs; controls | **G5 ATTEMPT bound and unbound**; controls G8 PREPARATION bound, admitted unbound. **Equal to RS** |
| 2 (g) | 31 model edits (absent, `[]`, null, `{}`, objects, strings, 0, false, `""`, non-empty; `reference_configurations`; `pressure_contract`) and the ordering pair | absent or `[]` admitted, and `pressure_contract` null admitted; every other value **G8 INVOCATION**; admitted unbound; INVOCATION before a P1 defect. **Equal to RS on every one** |
| 3 C2 (all branches) | C-a, C-b, C-c, C-d (144 probes) | **Equal to RS on every verdict:** the ten keyed pairs admitted, all 90 other precondition pairs G5 ATTEMPT, and the other branches as ruled |
| 4 header at G2 | 31 header probes and the ten N6 probes | **Equal to RS on every transport verdict** (§3) |
| 4 metadata at G7 | 41 metadata probes | **Equal to RS on every transport verdict** (my round-2 addendum §6: RS = TS there already) |

**TS equals RS on all three verdicts for 349 of 392 probes.** Transport is equal on all 392. The 43 differences are all on the raw path (bound and unbound):
- **two compound N6 probes:** each reader's raw G7 base code (declared, RV108 N6);
- **five header probes:**
  - four where TS's raw G7 keeps its Python order (carrier first, evidence before recovery), the same N6 class;
  - `h_formulation_limitations_other`: TS `…EVIDENCE_INVALID`, RS `…FORMULATION_BASIS` (I83 §7 item 6, routed to SC as a per-reader entry);
- **34 metadata-defect probes:** RS's raw evidence reader gives specific codes, and TS gives `…EVIDENCE_INVALID` (pre-existing; RS addendum 02, N-3);
- **two admissions (S-1):** `t_extrema_global_upper_string` and `t_extrema_certified_gap_null`. TS's raw path admits each, and reads it eligible bound. RS refuses both at G7 (`…NUMBER_INVALID`), and so does PY (`…EVIDENCE_INVALID`).

**The owner-kind probe** (`x:f_src_owner_kind_combination`, source 1's `owner.kind` `combination`): **G1 RECEIPT_MISMATCH** in TS, RS and PY, bound, unbound and transport. The schema's `CaseSource.owner.kind` is `const "case"`, and G1's shape check runs first.

## 3. The header at G2 against RS, check for check

**By reading.** TS's `headerCode(p, 'rust')` against RS's `semantic_contract::for_source_metadata`, on the transport projection (producer id and profile rewritten, receipt dropped):

| Step | RS | TS (`'rust'`) |
|---|---|---|
| 1 | `schema_version` not `0.2.0` → `SOURCE_SCHEMA_VERSION_UNSUPPORTED` (0.1.0 → `LEGACY_SOURCE_METADATA_CONTRADICTION`) | `!== '0.2.0'` → `SOURCE_SCHEMA_VERSION_UNSUPPORTED` |
| 2 | producer: exact keys, name, version, a known contract id → `SOURCE_PRODUCER_CONTRACT_UNSUPPORTED` | the same, with the id `BASE_ID` (the projection writes preview-physics-1) |
| 3 | (carrier only for load-reference ids: not reached) | no carrier branch (`'python'` only) |
| 4 | `source_block_recovery` present → `…LEGACY_DOWNGRADE_FORBIDDEN` | `recovery ?? evidence` |
| 5 | `contract_evidence` not an object → `…EVIDENCE_REQUIRED` | (the same expression) |
| 6 | numerical quality: exact keys, representation, quantization, policy, status, cases a list → `…QUALITY_INVALID` | the same conjuncts |
| 7 | each case: exact keys, the four enums, `evidence_refs` an array of non-empty strings, `basis_ref` exact with non-empty strings → `…CASE_INVALID` | the same conjuncts (in another order, one code) |
| 8 | formulation: exact keys, the profile, a non-empty list of non-empty strings → `…FORMULATION_BASIS_UNSUPPORTED` | the same |

Two differences are not reachable:
- RS's 0.1.0 branch: the successor's G0 refuses a non-0.2.0 schema version first, in both readers (my `h_schema_version_010`: G0 in both);
- RS's contract-id set: the projection always writes preview-physics-1.

**By run.** All 31 header probes and the ten N6 probes read the same transport verdict in TS and RS. They include:
- every single-defect branch;
- the order pairs (recovery with null evidence → LEGACY; quality before formulation; cases before formulation);
- `carrier_evidence` alone (G7 metadata) and beside a header defect (G2 header);
- an empty `evidence_refs` (admitted).

**The metadata check at G7** is unchanged in TS. As my RS round-2 addendum shows, RS's new check equals it, check for check and on all 41 probes. So "equal to PY's and RS's" holds for RS, not for PY. PY reads three shapes differently on transport (N-1 below):
- a duplicate withheld record: PY admits it (it compares the withheld records as sets), and TS and RS refuse it at G7;
- a non-number `global_upper_bound_pa`, and a null `certified_gap_pa`: PY refuses each at G7, and TS and RS admit them.

## 4. The conjunct's removal

`coverage` (G3) now checks only that the case ids match the invocation's. The `!(…combinations?.length)` conjunct is gone. By run, on my probes:
- `combinations` `[{"id": …}]` (non-empty): **G8 INVOCATION bound, admitted unbound** (was G3 COVERAGE bound);
- `combinations` `"x"`: the same (was G3 COVERAGE bound);
- my ordering probe (`combinations` null beside a P1 defect): G8 INVOCATION (was G8 PREPARATION).

TS now equals RS and PY there (PY at its repair-02 head). Before this commit, TS read G3 COVERAGE, which my round-2 work flagged.

## 5. The suite and tsc

- **TS's whole vitest suite at the head,** one slot job: **142 files, 3,631 passed, 0 failed** (`suites/vitest_ts1_head.json.gz`).
- **Against my run at `7e47e51b5d`** (SR-TS review, 3,628 passed): **+3, 0 removed, 0 changed in outcome** (`suites/VITEST_COMPARE_TS1.json`). The three are the round's new tests in `retainedPrecision.test.ts`:
  - "(g): the model-scope members are PP's acceptance, at G8 INVOCATION before any PREPARATION check; unbound reads admit them";
  - "C2's cause table: an unavailable_precondition code is keyed one-to-one by its precondition (N-2); the receipt_failure set form stands";
  - "the header at G2 with Rust's code, then the preview-physics metadata at G7; the raw path is unchanged".
- **`tsc --noEmit -p tsconfig.json`:** rc 0 (`suites/ts1_tsc.log`).

## 6. My mutants

Sixteen mutants, U01–U16 (`make_ts_mutants_r1.py`), each an edit to TS guarded by `RV113_MUT`, in my mutant copy. Each ran the seven test files that import the TS reader (807 tests) as one slot job. The control (`RV113_MUT` unset) passes 807 of 807, and its probe run equals the head's on all 392 probes.

| Mutants | Edit | Result |
|---|---|---|
| U01–U05 | (g): `reference_configurations` dropped; `pressure_contract` back to falsiness; `combinations` or `components` back to `!x?.length`; null allowed | **all killed**, by the (g) test |
| U06 | the G3 combinations conjunct restored | **killed**, by the (g) test |
| U07–U10 | C2: keying replaced by the old set of four codes; `source_family` keyed to `caller_not_qualified`; the phase dropped; the no-Run dropped | **all killed**, by the C2 keying test |
| U11–U16 | header: dropped; Python's order; reported at G7; evidence before recovery; the carrier branch kept; the formulation branch dropped | **all killed**, by the header test |

**16 of 16 are killed, each by an assertion failure, with 0 load failures.** Each is killed by exactly the new test for its item. So the new checks are pinned in TT, and no survivor needed my probes.

## 7. Against I92's records

My results agree with REPAIR_01 and REPAIR_01_ITEM3 on every count I can compare:
- the nine transport changes;
- 338 of 339 entries equal to RS;
- on I92's 135 probes, 133 equal to RS, with the same two compound probes;
- vitest +3;
- tsc clean.

Two notes:
- REPAIR_01 §6 item 3 says "No probe of RV113's carries a precondition cause". That was true of my earlier 135. My round-2 probes carry 100 precondition probes, plus C-c's six (§2). See N-2.
- REPAIR_01_ITEM3 corrects its own TT count (+48, not +47). That is a record fix, as stated.

## Findings

| # | Severity | Where | Finding | Proposed |
|---|---|---|---|---|
| S-1 | SHOULD-FIX (pre-existing; outside this round) | TS `previewPhysicsEvidence.ts` `validatePreviewPhysicsEvidence`, the extrema loop (the "A1 d + A2 1" checks) | **TS's raw evidence reader admits a non-number `global_upper_bound_pa` or a null `certified_gap_pa`.** It reads such a source admitted, and eligible bound. The extrema loop checks the shape and the two `value_*` numbers only, and `finiteTree` checks only the members that are numbers. RS refuses both at G7 `SOURCE_PREVIEW_PHYSICS_NUMBER_INVALID`, and PY at G7 `…EVIDENCE_INVALID` (my `t_extrema_global_upper_string`, `t_extrema_certified_gap_null`). TS at `7e47e51b5d` admits them too. Transport is not affected: it is never eligible, and RS and TS both admit there (N-1) | Require the two members to be finite numbers in TS's raw reader, refused at G7. Add an SC entry for each, expected refused in all three readers |
| N-1 | NOTE | TS `validatePreviewPhysicsTransportMetadata` against PY's `validate_transport_metadata` | **TS's metadata check equals RS's, but not PY's.** On transport, PY admits a duplicate withheld record (it compares the withheld records as sets), which TS and RS refuse at G7. PY refuses a non-number `global_upper_bound_pa` and a null `certified_gap_pa` at G7, which TS and RS admit. This is my RS addendum 02's N-1, seen from TS | ROOT rules which check is the reference, before SC pins these shapes |
| N-2 | NOTE | I92 `REPAIR_01.md` §6 item 3 | "No probe of RV113's carries a precondition cause" was true of my 135 probes, and is now outdated. My round-2 set has 100 precondition probes, and TS meets every one | None (the B1_SC brief's item 7 states the same of 07m; SC's entries close it) |

## For ROOT

1. **S-1:** route TS's raw extrema typing to a TS repair after I4, with SC entries expected refused in all three readers. It is outside the alignment set, and it does not block this confirmation.
2. **N-1:** rule which preview-physics metadata check is the reference for the three shapes. On transport, PY admits the duplicate withheld record that RS and TS refuse, and refuses the two extrema shapes that RS and TS admit. Neither B1_SC's item 13 nor RV108 declares this difference.
3. Nothing else on TS's side stands in the way of I4.

## Host

- **Slot jobs** through `WT/tools/t3_slot.sh`, one at a time, each the only heavy job of mine (`host/job_stamps.txt`):
  - TS's harness (census and the 392 probes);
  - RS's harness binary on the 392 probes (the round-2 target, before its deletion);
  - TS's whole vitest suite;
  - tsc;
  - the control's and 16 mutants' vitest runs, then the control's probe run.

  No vitest or test binary ran outside a slot. No cargo build was needed.
- **Waits:** each chain had one waiter, its background completion, which ended with it. I watched these chains no other way. None of mine remain. I killed no job.
- **Records:**
  - no symlink and no folder named `build`;
  - no junit output;
  - placeholder paths only;
  - screened, `.gz` files decompressed, with the strict pattern and the host name.
- **Not done:** no DEC-025, installs or Git writes (`git archive` and reads only, with `GIT_OPTIONAL_LOCKS=0`).
- **Cleanup:**
  - I deleted my copies `WT/rv113/ts1-head` and `WT/rv113/ts1-mut`, after removing each one's NMS link;
  - scratch is kept in `WT/scratch/rv113_rvr_01/tsr1/`.

## Records (`addendum_01/`)

- `static/`: `copies.txt` (file hashes against `git show`), `wasm_ts1-head.sha256`, `wasm_ts1-mut.sha256`.
- `harness/`:
  - `rv113Census.test.ts`, `gen_probes_h.py`, `cross_heads.py`, `compare_ts.py`, `compare_vitest.py`;
  - `make_tsr1_copies.sh`, `run_tsr1.sh`, `rsr2_job.sh`;
  - `make_ts_mutants_r1.py`, `run_ts_mutants_r1.sh`, `run_tsr1_mutants_all.sh`, `ts_mutant_table_r1.py`.
- `probes/`:
  - `probes_h.json`, `probes_ts1.json.gz` (the 392);
  - TS's and RS's outputs (`ts1_head.jsonl.gz`, `rs2_head_ts1.jsonl.gz`);
  - `CROSS_TS1.json`.
- `census/`: `census_ts1_head.jsonl.gz`, `TS1_CENSUS_07M.json`, `CENSUS_HEADS.json` (TS, RS and PY heads, and TS and PY before, pairwise).
- `suites/`: `vitest_ts1_head.json.gz`, `VITEST_COMPARE_TS1.json`, `ts1_vitest.log`, `ts1_tsc.log`.
- `mutants/`: `MUTANTS_TS1.json`, `MUTANT_TABLE_TS1.json`, and `runs/<id>/` (run stamps, the vitest log and JSON report, gzipped; the control's probe run).
- `host/`: `job_stamps.txt`.
