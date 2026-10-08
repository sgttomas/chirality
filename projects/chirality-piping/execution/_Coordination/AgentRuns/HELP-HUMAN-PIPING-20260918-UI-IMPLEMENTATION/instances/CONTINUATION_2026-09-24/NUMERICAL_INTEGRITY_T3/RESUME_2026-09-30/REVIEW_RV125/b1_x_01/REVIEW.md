# RV125 (RV-X, B1): the fresh complete-diff review of PR-B1 (#1154)

**Who:** RV125, TASK (Type 2), independent reviewer dispatched by ROOT (HELP_HUMAN, Agent 0), 2026-10-08 UTC. I wrote none of this code.
**Brief:** `R/BRIEFS/RV125_RVX_B1.md` (sha256 `aaae7740…611836d`, verified) with `R/BRIEFS/B1_COMMON.md` (`2d170307…2eb2c75`, verified). Mid-task, ROOT sent three things:
- the recut and one added item: RR "I108's package returned; the `threshold_bytes` citation corrected; PR-B1 recut from main `3d73db745e` with a true message" (NUM `75cd6be76b`), item 5;
- PR #1154's head, with SK's package to include.

**Basis:** PLAN_v2 (`R/I84/b1_plan_01/PLAN_v2.md`), RR "B1's PLAN_v2 accepted; …" through that ruling, and the slice reviews under `R/REVIEW_RV1*/`.
**Candidates:**

| Head | Main base | Int for source equality | Status |
|---|---|---|---|
| `8248921552c2bc70f95a3a6ea60f92fb18aa0317` (first) | `6c821d9ccf36d6b5f6a81ccbece6bee5a09fc9e6` | `a41eea7b5f` | superseded |
| `d07006c2f001be5565646d6f1cf046e6dc96006c` (the recut code commit) | `3d73db745edd3378e0bb254a1b263215ef0861e9` | `75cd6be76b` | reviewed here |
| **`0752ae8b98449d0aba4dbf332dc20b812df99d2d`** (#1154's head) | the same | the same | `d07006c2f0` + SK's package `T/IMPLEMENTATION/B1/` (7 files); reviewed here |

The recut and the PR head are on `codex/piping-t3-pr-b1-20261008` (`WT/pr-b1`); the first head was replaced there by the recut. #1154 is open, and its body equals the package's `PR_BODY.md` less the title line.
**Placeholders:** `WT`, `NUM`, `P`, `PP` (= `P/core/product_physics`), `RE` (= `P/core/reporting/result_export`), `T`, `R`, `RR` as in the brief. `S` = my scratch `WT/scratch/rv125_b1_x/`. `E` = this folder's `_run_records/`.

## Verdict: **PASS** at #1154's head `0752ae8b98`: 0 BLOCKING, 0 SHOULD-FIX, 7 NOTE

- **No correctness defect in the shipped code.**
  - Source equality holds on the recut.
  - Every hunk of the 33 files is covered by a review of its own commit. The one post-review code change is byte-equal to the reviewed `registration.diff`, and the recut's one comment I read myself.
  - My spot checks and custody probes at C = 3 pass on both heads, with byte-identical outputs.
- **At `8248921552` I had two SHOULD-FIX, both text only:**
  - SF-1: the `threshold_bytes` comment;
  - SF-2: the commit message.

  The recut repairs both, and I confirm them here. One residual of SF-2 is now N-4.
- **ROOT's added item** (N-5's composite physics-source clause) is met in substance, and no composite-path test is needed (N-5 below).
- **SK's package checks out:**
  - source equality passes checks 1–5 with `--package`;
  - `check_citations.py` passes with its index (98 resolved, 0 failures);
  - the three copies equal NUM's records at `75cd6be76b`;
  - `SHA256SUMS` 6 of 6;
  - no machine data.

  Its scope statements are true. Three text NOTEs remain (N-4, N-6, N-7).
- **RV109 round 2's N-1,** routed to RV-X by the CHANGE_RECORD, is closed: mutant M11 is now killed by five SP tests (§6).

## Findings

| ID | Class | Where | Evidence | Remedy / status |
|---|---|---|---|---|
| SF-1 | SHOULD-FIX at `8248921552`; **CONFIRMED REPAIRED** | `PP/src/retained_memory.rs:983-984`, the comment on `threshold_bytes` | The first head cited RR "R6a: B1's G5 holds on **B1's** real code; …". The heading reads "…on **the** real code; …", so this was the only one of the 13 distinct added `RR "…"` titles (fixtures excluded) that starts no RR heading. It also called M provisional, which R6b superseded. **At `d07006c2f0`** the comment is two lines, citing RR "R6b: RV124 passes SQ and confirms M", which starts R6b's heading. It agrees with R6b and QUAL_B1 (0.8745 M dense, 0.8693 M sparse). It is the only P change between the heads. | Repaired. `QUAL_B1.md` stays a bare name; the package's index resolves it, and my citation run on #1154's head passes (§4b) |
| SF-2 | SHOULD-FIX at `8248921552`; **CONFIRMED REPAIRED** (except (c), now N-4) | The commit message | The first message credited RV121–RV123, which reviewed B2/B3 lanes, and gave the registration to SA. It also said the readers "agree on every gate and code", and stated no scope. **`d07006c2f0`'s message** names RV109 (ST, SP), RV112 (SA), RV113 and RV120 (readers, SC), RV124 (SQ) and I106's gates, marked "not personal review by the owner". It gives the registration to SQ "after its review". It states "The Direct entry stays in the registered dev/test build only" and "No product caller and no public activation". Author and committer are the owner's configured identity, with the Co-Authored-By trailer. | Repaired |
| N-1 | NOTE (RV120 N-2, routed here) | RS `RE/src/retained_precision.rs:4663`; TS `previewPhysicsEvidence.ts:167`; PY `preview_physics_evidence.py:178` | All three readers admit a negative or zero `global_upper_bound_pa` or `certified_gap_pa`. Zero is legitimate. A negative value is never produced: `P/core/loads/stress_recovery/src/elastic_extrema.rs:196` sets the gap to `0.0` or to `(upper − best).next_up()`, with `upper ≥ best ≥ 0`. The leniency is main's ("typed, never bounded"); B1 only added the number demand. It affects only forged statements, and nothing has public meaning before B8. | None for PR-B1. A later three-reader round may add gap ≥ 0 and bound ≥ `value_upper_pa`, with 07n entries |
| N-2 | NOTE (forward) | `PP/src/retained_product.rs:110-114`; `:680` `successful_basis_record`; `:753` `basis_source_case` | The modulus-basis custody (`selections`, `basis_record`, `basis_record_calls`, `basis_expected`) is invocation-level, not in `CaseSlot`. It records once per distinct basis key, before the case's early hook parks the previous case. At c ≥ 2, a case with `modulus_basis_ref` or `modulus_basis_temperature` would fail closed: either custody refuses the invocation, or, with mixed cases, a case is refused at T-9 for a basis that is not its own. **This is unreachable in B1:** D1.5 refuses both members on every case (`retained_memory.rs:766`), and the serializer refuses any non-base selector (`retained_wire.rs:878`) | None for B1. Before any lane widens D1.5 to material selectors at c ≥ 2 (B2's combinations, for example), move these four fields into the per-case slot or key them by case |
| N-3 | NOTE | `PP/src/retained_product.rs:223` `with_case` | Inside `with_case(i, f)`, `parked[i]` is a default slot and the last case's fields sit in a local. A cross-case accessor called inside `f` (`case_scope`, `case_native`, `case_prepared_source`, `case_observation_state`, `parked_cases`) would read defaults. **No call site does this today:** `prepare_attempt`, `freeze_case`, `serialize_attempt`, `native_call`'s moves and `bind_case_rows` all compute what they need outside the closure | Optional: a debug assertion or a doc line on `with_case` |
| N-4 | NOTE (residual of SF-2 (c)) | `d07006c2f0`'s message ("agree on every gate and code"); PR body, "The readers"; CHANGE_RECORD §2 ("apart from the declared raw G7 codes") | The message has no qualifier. The PR body and CHANGE_RECORD except only the raw codes. RV120's A-N2 has two more declared, unpinned differences, both PY-only on transport: PY refuses an array over 16,384 items, and PY admits an unsafe integral `span_index` that RS refuses at G7 and TS at **G1**. So the readers differ there in gate and in acceptance, not only in code. These are forged shapes the producer cannot emit, and nothing has public meaning before B8 | Optional: "apart from the declared differences (the raw G7 codes; RV120 A-N2's two PY-only transport cases)". The PR body can be edited without a push. ROOT's call |
| N-5 | NOTE (ROOT's added item) | `RE/src/source_blocks.rs:1780` `rv95_n5_integer_tests`, against DESIGN_v2 §7's PR-B1 row ("It also covers `failure.block_order` … and the composite physics-source receipt") | See the reading below. In short: `integer` is private to `source_blocks.rs`. The composite receipt reaches it only through `source_blocks::validate_in(…, true)` (`physics_source.rs:1131`), at the same call sites the test's census enumerates, including the one composite branch, `work["limit"] ≤ 8_000_000`. The composite receipt schema has the same maxima on all 13 fields except case `work.limit` (8,000,000, not 4,000,000). So S1 and its off-by-one are killed for both receipts by the direct test (RV113 M30 and M31), and the bound needs no composite-path test. What the test does not do is name the composite receipt or exercise it | The clause is met in substance. Optionally, add one doc line to the test: the composite physics-source receipt reads the same call sites through `validate_in(…, true)`, with case `work.limit` ≤ 8,000,000. **No composite-path test is needed** |
| N-6 | NOTE | PR body, "Corpus 07n is appended to 07m: 26 cases, 534 mutations and 78 must-pass entries" | Those are the corpus file's totals after the append. 07n itself adds 9 bases, 240 mutations and 50 must-pass entries (RR "SC passed its acceptance; …"; RV120 `sc_01`). CHANGE_RECORD §2 states it correctly, with the + counts | Optional: "the corpus then holds 26 cases (+9), 534 mutations (+240) and 78 must-pass entries (+50)" |
| N-7 | NOTE | CHANGE_RECORD §1 (`PP/src/lib.rs` row) and §2 ("T-4: … is not attempted (decision 21)") | `checks_passed` → `not_required` is decision 1 (DESIGN_v2's decision table, row 1). Decision 21 is DN §4.3's exclusion: a seed's `structural_failure` of kind mechanism, asymmetric or invalid_input, with no W2 publication. That exclusion is also in T-4 (`case_triggers`, `dn_trigger_excluded`), and the record never states it | Optional: "(decision 1; decision 21's exclusion also keeps such a failed case out of A)" |

**N-5 in full: the composite clause.**
- **What the test does.**
  - `integer_admits_two_to_53_minus_1_and_refuses_two_to_53` calls `integer` directly. It kills S1 (the bound removed) and its off-by-one.
  - `every_field_read_through_integer_refuses_two_to_53` reads the production text of `source_blocks.rs` and requires the exact argument set of its `integer(&…)` calls: 14 arguments on 13 receipt fields, among them `failure["block_order"]` and the composite-only line `integer(&work["limit"])? <= if composite { 8_000_000 } else { 4_000_000 }`, plus `summary[key]`.
  - It runs `source_plan` and `summary` at 2^53 and 2^53 − 1.
  - Its per-field loop exercises `integer` alone, as RV113's N-5 noted.
- **The composite physics-source receipt adds no `integer` site.**
  - `physics_source::validate` calls `crate::source_blocks::validate_in(source, actual_invocation, true)` (`physics_source.rs:1131`), the same function the plain receipt runs with `composite = false`.
  - `physics_source.rs` never calls `integer` (it cannot: `integer` is private).
  - Its own integer reads (`as_u64`) are functional indices, in `maximum_link`, `validate_derived` and `section_functionals`. Each is compared with the plan's `functional_count` or bound by an exact id string.
    - On the full read, they run after `validate_in`'s `source_plan` (`source_blocks.rs:991`) has read the counts through `integer`.
    - On `validate_transport_metadata`, they read the plan's count raw.
    - None is an `integer` site, and B1 changes none of them: `physics_source.rs` is not among the 33.
- **The masking layers are the same.**
  - `physics_source_recovery.schema.json` and `source_block_recovery.schema.json` set the same maxima on all 13 fields: 2^53 − 1, or 64,000,000 on `invocation_work`. The one difference is case `work.limit`: 8,000,000 for the composite receipt, 4,000,000 for the plain one.
  - The checked-profile hash refuses unsafe integers on both paths.
- **So:** the direct test pins the bound for both receipts, and a composite-path test would pin only the order of the masking layers on the composite statement, not the bound. The clause is met in substance. Its literal reading ("covers … the composite physics-source receipt") is met by the census of the shared call sites, not by a composite fixture.
- **On the recut head:** both N-5 tests pass (`E/outputs/test_results.txt`).

## 1. Source equality (brief item 1)

| Head | Main | Int | B | Checks |
|---|---|---|---|---|
| `8248921552` | `6c821d9ccf` | `a41eea7b5f` | `6c821d9ccf` | 1, 2, 3 and 5 pass |
| `d07006c2f0` | `3d73db745e` | `75cd6be76b` | `6c821d9ccf` | 1, 2, 3 and 5 pass |
| **`0752ae8b98`**, with `--package …/IMPLEMENTATION/B1` | `3d73db745e` | `75cd6be76b` | `6c821d9ccf` | **1–5 pass.** Check 4: 7 execution files, all inside the package, and `SHA256SUMS` verifies |

All three runs used `T/IMPLEMENTATION/F2A_D1/source_equality.py`; the logs are `E/outputs/source_equality{,_d07006c2f0,_0752ae8b98}.{log,json}`.
- **On the recut,** |S| = 33, the PR's non-execution paths equal S, and all 33 have the same blob and mode at the int and the PR (33 of 33 rows equal).
- **On the two code-commit runs,** check 4 is FAIL only because no `--package` was given. `execution_files: 0`, so the code commit carries no execution record.
- **Main `6c821d9ccf` → `3d73db745e`** (#1153) changes 179 paths, none under P.
- **The recut's P delta from `8248921552`** is `git diff 8248921552 d07006c2f0 -- projects/chirality-piping`: one hunk, the two-line comment in `retained_memory.rs` (SF-1). `retained_memory.rs` is not among the 14 reviewed inputs, so the registered identity is unchanged.

## 2. The ledger (brief item 2)

**Merges.** Every merge on `b1` equals `git merge-tree --write-tree` of its parents, with no hand resolution:
- `262bd687f0` (I1, absorbing main `2007709549`);
- `77f4391a85`;
- `eca6c00a72` (I2);
- `2ba2f81863` (I3);
- `b6327a5155`, `abff6d1ee5` and `30f3d1b24a` (I4);
- `61782676ad`, `1c5228866f` and `8d46b045e2` (I4′);
- `0d19f995b5`.

**Main since `b1`'s base** touches none of the 33 files. **Changes after review:**
- `ddc8eaaf54` is byte-equal to `R/I104/b1_sq_01/registration.diff` (`d85101ea…`), which RV124 reviewed;
- NUM `75cd6be76b`'s comment I read myself (SF-1).

| Files (33) | Commits on `b1` (no merges) | Covered by (reviewed head) |
|---|---|---|
| PP producer: `src/lib.rs`, `retained_product.rs`, `retained_wire.rs`, `retained_receipt.rs`, `retained_tests_hooks/grant2.rs` | ST `4a51783e65`; SP `56c5579f07`, `7458527ff7`, `89222942ee`, `59393e2d43`, `0ec3651a36`, `8db7906ee7`, `603e238517`; I3 step `2fb55b60e2` (wire) | RV109 R1 (`a8e719f5b4`); RV109 r3p notes (`56c5579f07`); RV109 R2 (`603e238517`, I2 included); RV109 R2 A1 (`03f55e7178`) |
| PP admission and profile: `src/retained_memory.rs` | ST `4a51783e65`; SA `6b62606778`, `9812c83ded`; SQ `b075c5c59f`, `69002bc862`; registration `ddc8eaaf54`; NUM `75cd6be76b` (comment) | RV109 R1; RV112 (`9812c83ded`); RV124 (`b075c5c59f`, `69002bc862` + `registration.diff`); RV125 (the comment) |
| PP tests: `retained_facade_tests.rs`, `retained_product_tests.rs`, `retained_wire_tests.rs`, `retained_memory_law_tests.rs`, `retained_memory_witness_tests.rs`, `tests/common/b1_sq_inputs.rs`, `tests/retained_memory_challenge.rs`, `tests/s11f_site_test.rs` | ST, `98a77c716e`, SP, `c17340d50b`, `105e1a78c6`, `03f55e7178`, SA, SQ `69002bc862` | RV109 R1 and A1; RV109 R2 and A1; RV112; RV124 |
| RE: `src/retained_precision.rs`, `src/source_blocks.rs`, `tests/retained_precision_contract.rs`, `tests/retained_precision_carriers.rs` | SR-RS `d7c76de43f`, `a4eab1dd01`, `cc81e78801`, `b5cb7faaeb`, `6e3e4fe219`; I4′ `990339d94f`, `e879118348`; SC `90d8fbeea5`, `57c92a7b33` | RV113 SR-RS (`cc81e78801`), A1 (`b5cb7faaeb`), A2 (`6e3e4fe219`); RV120 i4p (`e879118348`); RV120 SC (`57c92a7b33`) |
| PY: `core/analysis_runs/{retained_precision,compatibility,preview_physics_evidence}.py`, `tests/test_retained_precision_{contract,carriers}.py` | SR-PY `a514f4ca74` … `11cc14e3e6` (9), repair 02 `a721e58483` … `2843a59a16`; I4′ `8fa5aac15c`, `52d83da275`; SC `09fe4cc69b`, `57c92a7b33` | RV113 SR-PY (`11cc14e3e6`), A1 (`2843a59a16`); RV120 i4p A1 (`52d83da275`); RV120 SC |
| TS: `retainedPrecision.ts`, `previewPhysicsEvidence.ts`, and their tests, `retainedPrecisionIntegration.test.tsx` | SR-TS `5d7b4447cd` … `7e47e51b5d`, repair 01 `b82b932923`, `1d9455c714`, `6fa6a64658`; I4′ `819e44f63e`; SC `901745f46b`, `57c92a7b33` | RV113 SR-TS (`7e47e51b5d`), A1 (`6fa6a64658`); RV120 i4p (`819e44f63e`); RV120 SC |
| Runner test `core/runner/headless/tests/retained_precision_admission.rs` | SA `6b62606778` | RV112 |
| Fixtures: 07n `retained_precision_cases.json`, `retained_precision_carrier_cases.json`, W-C2 successors (2) | SC `09fe4cc69b`, `57c92a7b33`; I3 step `2fb55b60e2` | RV120 SC; RV109 R2 A1. The W-C2 bytes are reproduced here (§5) |

**Uncovered hunks: none.** Nevertheless, I read the production diff in full myself, against the brief's list:
- **Files read:** PP `lib.rs`, `retained_product.rs` (with `-w`), `retained_wire.rs`, `retained_receipt.rs` and `retained_memory.rs` outside the generated block; RE `retained_precision.rs` and the N-5 tests in `source_blocks.rs`; TS `retainedPrecision.ts` and `previewPhysicsEvidence.ts`; PY `compatibility.py`, `preview_physics_evidence.py` and `retained_precision.py`.
- **What I followed:**
  - case indexing (`CaseSet`, A's request indices, `case_scope`);
  - custody (`CaseSlot` and `park_case`, `with_case`, invocation-level against per-case fields; N-2, N-3);
  - failure atomicity (T-5's reservations, the ordinary owner untouched, `w1_transaction`'s returns);
  - ordinals (batch ordinal to request index in `invocation_arrays`, `case_run` and `execution_order`; `attempt.attempt` to `product_attempts[]` and `bind_preparation`);
  - the multi-case receipt (`serialize_cases_with`);
  - T-12's bitset (bit k is A's k-th case, in `selected_attempts` and in `publish`);
  - `stage_headlines` against `maximum_across_cases`, preview-physics' per-case ties and RS `headline`/`governs` (all four agree: greater value, then smaller case id, then smaller entity);
  - G-B and G-C fact alignment (`late_observations` against `phase_caps().late`).

## 3. Scope truthfulness (brief item 3)

- **Maintained text:** I found no claim beyond the Direct entry in the registered dev/test build, C ≤ 3 at S3, and the readers and 07n.
  - `RetainedPreviewOutput`'s doc says that a permit exists only for a D1 Direct call in the one registered (dev/test) build.
  - Headless stays refused at D1.0. The runner test's `C_PLUS_ONE` = 4 is tied to `caps::LOAD_CASES` + 1 by PP's law test `b1_sa_runner_oracle_literal_is_load_cases_plus_one`.
  - No added line claims product callers, public activation, B8, a supported machine, B2, B3, S-I2, F2b or F3.
- **The recut's message** now states the scope (SF-2), with N-4 residual.
- **#1154's body (= `PR_BODY.md`) and the CHANGE_RECORD** say exactly what is public:
  - "What stays closed" / §3: the Direct entry only in the registered dev/test build, where every other build publishes the ordinary bytes; no product caller and no public activation (B8's); no supported-machine statement (owner-held), with R9's figures and "Behaviour on a 16 GB machine was not observed"; not B2, B3, S-I2, F2b or F3; no kernel, schema, `Cargo.lock` or reviewed-input change. Each holds against the code and §4.
  - **Claims I checked against the code:** D1.4 at 1–3 cases with ≤ 384 loads, no combination or component; pressure refused (D1.5); T-4's `NoTriggeredCase` with exact bytes; one notice per attempted case; c = 1 on the same path; the ordinal repair; `threshold_bytes` and 0.8745 M.
  - **File counts and hashes:** "33 files, 3 added, 30 modified, +329,865 / −943, +283,214 the corpus" is exact, and all 33 per-file sha256 values in CHANGE_RECORD §1 equal the blobs at `d07006c2f0`.
  - **Reviews:** they are named truly and marked as agent reviews.
  - **Gates:** the open ones say "see the merge record".
  - **The text NOTEs** are N-4, N-6 and N-7.

## 4. M and the registration (brief item 4)

- **`threshold_bytes`** is 11,274,289,152 = 10.5 × 2^30, which is RR R6b's final M and QUAL_B1's figure. My arithmetic: 9,800,676,166 / M = 0.86929 and 9,859,807,510 / M = 0.87454. The comment now agrees (SF-1).
- **The rest of the `REGISTERED_PROFILES` entry is byte-identical to main's:** the identity, the reviewed inputs and the reader layouts. I checked this by sha256 of the entry with the threshold and comment lines removed.
- **The 14 reviewed inputs** each have, at the head, exactly the registered sha256, and each is unchanged from main. PP's `Cargo.lock` is among them.
- **No Cargo manifest or lock file is among the 33.**

## 4b. SK's package (ROOT's request)

- **`SHA256SUMS`:** 6 of 6 OK, on a `git archive` of `0752ae8b98`'s package.
- **The copies are byte-equal to NUM's records at `75cd6be76b`:**
  - `copies/QUAL_B1.md` = `R/I104/b1_sq_01/QUAL_B1.md` (`eb6541fc…`);
  - `copies/RSS_TIME.md` = `RSS_TIME.md` (`f230c7ec…`);
  - `copies/registration.diff` = `registration.diff` (`d85101ea…`, SQ's historical diff, as the CHANGE_RECORD says).
- **The citation index** `citations.json` (`u9-citation-index-v1`):
  - it is pinned at NUM `75cd6be76b`, which `origin/codex/piping-numerical-integrity-20260926` contains;
  - `source_basis` is `d07006c2f0`;
  - it holds 28 citations, 23 documents (#1082's), 3 copies and no code anchors;
  - **my run** of `T/IMPLEMENTATION/F2A_D1/check_citations.py --base 3d73db745e --head 0752ae8b98 --index <it> --package <it>` gives resolved 98, ambiguous 0, unresolved 0, verification failures 0, unused entries 0: **PASS** (`E/outputs/check_citations_0752ae8b98.{log,md}`). The recut comment's RR "R6b: …" and `QUAL_B1.md` resolve.
- **The package carries no machine data.** It has no strict path form. The only name hit is the 3-character host label inside ordinary words such as "machine", which is one of `t3_host_screen.py`'s generic labels.

## 5. My spot checks (brief item 5)

**The setup:**
- **The copies:** `git archive` copies (P without `execution/`) of `8248921552` (`WT/rv125/cand`) and `d07006c2f0` (`WT/rv125/head2`). In each, the 33 files equal the head's blobs (`git hash-object`, no `-w`). The only edit to a PR file is three lines appended to `lib.rs`, declaring my test module (`E/lib_rs_delta.txt`).
- **The builds:**
  - registered: debug, toolchain 1.97.1, no RUSTFLAGS, in `WT/targets/rv125-reg`;
  - Stale: `RUSTFLAGS=--cfg=rv125_stale`, in `WT/targets/rv125-stale`;
  - PY's authority binaries: `WT/targets/rv125-auth`;
  - RE: `WT/targets/rv125-re`.
- **TS:** vitest ran in the first copy as ROOT did at I4. `node_modules` was linked from `WT/sweep-skewpin` after a `package-lock.json` cmp, the copy had its own `apps/desktop/node_modules`, and the eight wasm assets were copied (`E/outputs/ts_wasm_assets.sha256`).
- **Harnesses and scripts:**
  - harnesses: `E/zz_rv125_spot.rs` (two tests), `E/zzRv125Readers.test.ts` and `E/test_zz_rv125_readers.py`;
  - scripts: `E/run_chain.sh` (first head: spot checks, Stale, PY and TS), `E/run_probe.sh` (first head: spot again plus the probes) and `E/run_head2.sh` (recut head: spot plus the probes, and RE's N-5 tests).
- **On the recut,** the registered outputs `reg_d07006c2f0.json` and `probe_d07006c2f0.json` and all eight successor and invocation files are byte-identical to the first head's. So the readers' results carry over unchanged.

| Check | Result |
|---|---|
| **W-C2 (3 cases) through the Direct entry, registered, both modes** | `Registered`, admitted, successor. Published bytes sha256 = SP's pins `c7a18593…` (sparse) and `a77c010b…` (dense). The successor equals each committed fixture's `source`. The ordinary owner equals the value route's bytes. One `RETAINED_PRECISION_UNAVAILABLE`, case-c's receipt diagnostic |
| W-C2, a Stale build, both modes | `Profile(Stale)`, exact: published = value-route bytes (`42b24d16…` and `c382c16e…`), 0 notices |
| Pressure on the **third** case of W-C2, registered and Stale | Registered: D1.5 `Family(Case, PressureRegions)`, exact value-route bytes, 0 notices. Stale: D1.1, the same bytes |
| **The three readers on the multi-case successor,** W-C2 and W-C2 permuted (c, a, b), both modes | RS, PY and TS agree on every one: bound → valid, `needs_recompute` (case-c is unavailable), 171 classes; unbound → valid, not bound, 171; transport → valid, 0 classes |
| **Ordinal mapping:** (c, a, b) against (a, b, c), both modes | Each case's rows (kind, entity, value bits, method) and preview evidence are equal. Each case keeps its status. Every Run origin, call owner, source owner and `execution_order` entry names the request index of its own case |
| **Custody at C = 3:** three copies of case a (a, a2, a3), against case a alone (c = 1), both modes | All three are selected. Each case's rows, evidence and RS classifications (normalized bits, scale, class; 171) equal case a's c = 1 successor exactly |
| **T-4 and T-12 at C = 3:** b b2 b3; c c2 c3; b c c2; both modes | b b2 b3: `NoTriggeredCase`, exact bytes, 0 notices. c c2 c3: `Native`; published = the value route's envelope plus exactly 3 N1 notices (c, c2, c3) in request order. b c c2: 2 notices (c, c2), none for b |

## 6. Routed to RV-X: RV109 round 2's N-1 (CHANGE_RECORD §7)

- **The finding.** RV109's mutant M11 (`native_call` moves the call's sources back to the wrong slots) survived the `--lib` suite before I3.
- **I applied it to the recut copy** (`.rev()` on the move-back; `E/run_m11.sh`) and ran SP's `b1_sp_` tests.
  - **Five fail:** the W-C2 pin, the W-C2 fixtures test, the T-12 test, the transaction and ordinal-mapping test, and the SF-2 pins. Each fails with `Precommit { gate: "G8", code: "RETAINED_PRECISION_PREPARATION_MISMATCH" }`.
  - **13 pass.**
- **So since I3's pins, M11 is killed in the lib suite.** In production a mis-slotted source is a fail-safe precommit abandonment, never a published successor.
- **RV109's optional producer-side check is not needed.** Closed.
- **Cleanup:** the copy was restored from its saved original (no mutant line left), and the mutant target was deleted with the others.

## 7. Host and limits

- **Jobs:** every cargo job went through `WT/tools/t3_cargo.sh` (`--locked --offline`), and pytest and vitest through `WT/tools/t3_slot.sh`, one job of mine at a time.
- **The chain:** it ran in the background with one waiter, which ended with the process. I signalled no job.
- **Not run:** DEC-025, RSS or timing jobs, solver-at-scale jobs, installs.
- **No Git writes.** Git reads used `GIT_OPTIONAL_LOCKS=0`. I never modified `WT/pr-b1`; its branch moved to the recut during my run, by ROOT.
- **Records:** placeholder paths only, no symlink and no folder named `build`. They were screened for the strict path forms and for this machine's names.
- **The package** was read from a `git archive` in `S/pkg`.
- **Cleanup:** the copies `WT/rv125/` and the targets `WT/targets/rv125-*` are deleted after this record. `S` is kept.
