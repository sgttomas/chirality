# I113: B3a dropped from `b2` (the legacy pressure label's admission to the retained route)

TASK (Type 2), I113, for WORKING_ITEMS (T3, Agent 1), the return path. I made no delegation. 2026-10-08 UTC.

**Basis:**
- the brief `R/BRIEFS/B3A_DROP.md` (sha256 `ea28b9da…0bac`, verified), with `R/BRIEFS/B1_COMMON.md`'s host, Git and records rules (WORKING_ITEMS in ROOT's place), `NUM/AGENTS.md` and `NUM/agents/AGENT_TASK.md`;
- RR "Owner decisions: the legacy pressure contract is retired product-wide; …" (decision 1) and "U3 rulings on I110's pressure inventory: …";
- B3-D `R/I96/b3_d_01/DESIGN.md` §4.1, §6.3, §6.4 and decision B3D-10, with REVISION_01 §3;
- I110's inventory `R/I110/pressure_retire_01/inventory.json`, kind `b3a` (34 sites);
- RR "I99's B3-W verified; …" (m3l, B3a's witness).

**Placeholders:** WT, NUM, P, PP, RE, R as in the brief; APPWT is the App worktree whose `node_modules` the archive copies link (read only); HOME and TMP as I101's records use them.

## Head and commit

| | |
|---|---|
| Branch | `codex/piping-t3-b2-20261008` (`WT/b2`), not pushed |
| Start head | `51f339a11e` |
| **Candidate head** | **`0ef9a8ace9`** "piping(T3 B3a drop): D1.3 and the three readers' G8 refuse 0.3.0 legacy_pressure_v1" |

One commit, 11 files, +205 −206 (`_run_records/suites/diffstat.txt`; the full diff is `b3a_drop.diff`, sha256 `97c9f387…815e`). The host screen (`WT/tools/t3_host_screen.py`) over `51f339a11e..0ef9a8ace9`: 11 files, 0 hits.

## What changed

**Production (the admission removed):**
- **PP:** `NamespaceBranch::LegacyPressure` and D1.3's L3 arm are removed (`retained_memory.rs`). 0.3.0 with `{1.0.0, legacy_pressure_v1}` now falls to the existing arm and refuses with `Family(Namespace, PressureContract)`, as any contract outside L and E does. `w1_route` (`lib.rs`) loses the variant, so the label has no W1 route. The census still reads a contract's two typed strings, because branch E admits one; only its comment changed. No other clause, row or price changed.
- **RS** (`RE/src/retained_precision.rs`), **TS** (`retainedPrecision.ts`) and **PY** (`core/analysis_runs/retained_precision.py`): G8's preview-branch namespace is now `schema ∈ {0.1.0, 0.2.0}` with `pressure_contract` absent or JSON null. Anything else is G8 `RETAINED_PRECISION_INVOCATION_MISMATCH`. This keeps B3D-10's tightenings: 0.3.0 without a contract stays refused, and PY's `{}` and the other falsy values stay refused. PY's `LEGACY_PRESSURE_CONTRACT` constant was removed with its one use. The exact branch is untouched.

**m3l stays, as a refusal witness.** It is still used in two places:
- PP: its B3-W Value sha256 `2f5ff465…` is still pinned; its route is now `None`; the Direct entry refuses it at D1.3 and publishes the ordinary route's bytes.
- PY: `m3l(mode)` is refused at G8. B3b's `test_b3b_carriers` also reads m3l's invocation against the exact successor (`unsupported`, unchanged).

RS and TS have no m3l.

**The shared refusal shape:**
- RS's `b3a_legacy_pressure_contract_namespace_at_g8` and TS's "B3a (I101)" block already pinned one 29-entry table, entry for entry. They keep their names, bases and edits.
- I added the same table to PY (`B3A_DROPPED_TABLE`, `test_b3a_dropped_namespace_table`), so **RS, TS and PY now pin one shape alike**: same names, same five shared-corpus bases, same invocation edits (rehash all), same expectations.
- In the table, only branch L passes. "L3" in the entry names means B3a's retired contract on 0.3.0, which is now refused on all five bases.
- The two former N-11 entries (the label plus a zero-magnitude element pressure load) are now refused at G8's namespace step, before any load is read.

**I110's 34 sites** (each located at both heads; `_run_records/sites.json`):
- **5 removed:**
  - PP's L3 variant (with its doc line) and arm;
  - PY's constant;
  - RS's L3 arm;
  - TS's L3 arm.
- **12 edited** (a doc or comment).
- **3 lines unchanged, but their test changed:** two assertions now expect the refusal (PP's law test, PY's d31), and PY's module docstring around m3l's description was edited.
- **14 unchanged.** These include the B3b pins that use the label as a refusal:
  - PP's `profile mode` evidence tamper;
  - PP's law test of mode → legacy on 2.0.0;
  - PY's x13;
  - RS's and TS's entry 19.

  B3b is kept byte-identical, so these stay as they are.

Comments mentioning L3 outside the inventory (no label text) were updated in `retained_memory.rs`, `lib.rs`, RS, TS and PY.

## The test diff (start head → candidate)

**PP (`PP`, all targets):**

| Test | Change |
|---|---|
| `retained_memory::law_tests::b3a_d1_3_admits_the_legacy_pressure_contract_on_0_3_0` | removed → **`b3a_dropped_d1_3_refuses_the_legacy_pressure_contract_on_0_3_0`** (added). The label refuses at D1.3 (`PressureContract`) on m3l, at C cases and at the cap-maximal shape, with no permit in either mode. The refusal map is unchanged except that the label is now refused. The label with an empty region list, an element pressure load or a nodal `pressure` category refuses at D1.3 first. The census still counts the contract's two strings; their capacity pin moves to branch E (`exact3`), the only branch that admits a contract |
| `retained_memory::law_tests::b3a_direct_entry_oracles` | removed (**FAILED at the start head**; see below) → **`b3a_dropped_direct_entry_refuses_m3l`** (added). m3l and the 1.0.1 variant are refused at G-A with `PressureContract`, with no W1, no successor and the exact ordinary bytes. The helper `with_one_notice`, which only this pin used, is removed |
| `retained_facade_tests::b3a_m3l_needs_no_producer_change` | removed → **`b3a_dropped_m3l_takes_the_ordinary_route`** (added). Both modes: D1.3 `PressureContract`, no W1, `ONE_RUN`, and the publication equals the plain bytes. The former pin of m3l's ordinary bytes against the milestone is not carried over: that is an ordinary-route fact, which the pressure retirement's Stage 1 owns |
| `retained_facade_tests::b3b_witness_inputs_and_routes` | edited: `w1_route(m3l)` `Some(Preview)` → `None`; doc |
| `retained_memory::law_tests::b3b_d1_admits_the_exact_route_with_empty_regions` | edited: "a combination on L or L3 is inside D1" now uses the milestone (L) instead of the label |
| `retained_memory::law_tests::every_family_clause_refuses_with_its_fact` | comment only (0.3.0 without a contract: `PressureContract`, unchanged) |

**RS (`RE`):** `b3a_legacy_pressure_contract_namespace_at_g8` is edited:
- the five "L3 on <base>" entries: pass → G8 `INVOCATION_MISMATCH`;
- the two "N-11" entries: G8 `PREPARATION_MISMATCH` → `INVOCATION_MISMATCH`;
- the doc is updated.

`d31` is unchanged.

**TS (desktop vitest):** in "B3a (I101): G8's namespace predicate, type-strict …", the same seven `it`s are edited in their expectations only (names unchanged), and the comment is updated. D31 is unchanged.

**PY:**

| Test | Change |
|---|---|
| `test_b3a_m3l_successor_is_admitted_like_the_milestone[sparse_interactive, dense_scrutiny]` | removed → **`test_b3a_dropped_m3l_successor_is_refused[…]`** (added): m3l is G8 `INVOCATION_MISMATCH`; the milestone control stays eligible |
| `test_b3a_m3l_mutations[{a zero-magnitude element pressure load, a non-zero element pressure load, a non-zero node force with category pressure}-{both modes}]` | edited (6): `PREPARATION_MISMATCH` → `INVOCATION_MISMATCH` (the label is refused first). The other nine labels are unchanged |
| `test_model_schema_versions_d31` | edited: 0.3.0 with the legacy contract was admitted; it is now G8 `INVOCATION_MISMATCH`. Docstring updated |
| `test_b3a_dropped_namespace_table[29 entries]`, `test_b3a_dropped_namespace_table_has_the_rust_tests_29_entries` | **added** (30): the shared shape |

These PY tests are unchanged: `test_b3a_branch_l_admits_only_an_absent_or_null_contract` and `test_b3a_tightening_0_3_0_needs_the_legacy_contract`. The second still pins B3D-10's 0.3.0-without-a-contract refusal; its name predates the drop.

**Discrimination check** (`_run_records/reverse/`): the candidate's tests were run against the start head's five production files. Every new or edited B3a test failed, and nothing else in the targeted sets did:

| Suite | Failures |
|---|---|
| PY | 16: the 2 m3l, the 6 load mutations, the table's 7, and d31 |
| TS | 7 |
| RS | the table, with exactly 7 misses |
| PP | 4: the three `b3a_dropped_*` tests and `b3b_witness_inputs_and_routes` |

## Suites against the start head (test by test; `_run_records/suites/`)

Each suite ran on `git archive` copies of the two heads (`P` without `execution/`).

| Suite | `51f339a11e` | `0ef9a8ace9` | Differences |
|---|---|---|---|
| PP, all targets | 790 ok, **2 FAILED**, 11 ignored | 791 ok, 1 FAILED, 11 ignored | the 3 renamed pairs above; `b3a_direct_entry_oracles` (FAILED) is gone |
| Runner (`core/runner/headless`) | 85 ok, 2 FAILED | 85 ok, 2 FAILED | 0 |
| RE (`result_export`) | 206 ok | 206 ok | 0 (the edited table keeps its name) |
| PY reader set (I100's 29 modules) | 2,387 passed, 19 failed, 30 skipped | 2,417 passed, 19 failed, 30 skipped | +32 added, −2 removed (the renamed m3l pair; the 30 table tests) |
| Desktop vitest (whole) | 3,678 passed | 3,678 passed | 0 (seven expectations edited, names unchanged) |
| `tsc --noEmit` | rc 0 | rc 0 | — |

The compiler warnings are the same at both heads (PP 18, RE 2, runner 15).

**The failures at both heads:**
- PP's `t13`, RR's known Mac `t13`.
- The runner's two load-reference tests, which are the base's own (I105).
- **PY's 19:** all in `test_handoff_package_schema.py` and `test_handoff_export_workflow.py`. They are an artifact of my archive copies: they read fixtures under `P/execution/`, which the copies exclude (`FileNotFoundError`). In the full `WT/b2` tree at the candidate head, both modules pass 20 of 20 (`handoff_full_tree_cand.log`).

**The start head carried one more failure: `b3a_direct_entry_oracles`** (`SparseInteractive: the interim cause`, left `None`, right `Precommit G8 INVOCATION_MISMATCH`):
- That pin said it "changes at J5". Once the readers' B3a merged into `b2`, the RS reader admitted m3l, so W1 validated a successor instead of falling back.
- The drop replaces the pin, so the candidate no longer has this failure.

**Kept byte-identical:**
- every exact-route and 0.1.0/0.2.0 outcome;
- lane P's pins (EXACT, MIX and the B2-P pins in the facade suite);
- every B3b test in all four suites: each passes at both heads with no outcome change.

## Census (RV113's harnesses; `_run_records/census/`)

**Harnesses:**
- RS and TS use I101's copies of `rv113_census.rs` and `rv113Census.test.ts` (sha256 `c0dadef9…5d30`, `abcc6e36…2b45`, checked at each copy).
- PY uses I100's `rv113_py_harness.py` (`df4310a8…6e41`).

**Corpora:**
- 07m is the in-tree corpus (`c21112fd…6807`);
- 07n is SC's corpus (`ea113e7b…e283`), substituted in a third copy.

Every record field was compared entry by entry: the input digest, the bound, unbound and transport verdicts in full, and RS's standing.

| Corpus | Reader | Entries (base / mutation / must-pass) | Changes |
|---|---|---|---|
| 07m | RS | 339 (17 / 294 / 28) | **0** |
| 07m | TS | 339 | **0** |
| 07m | PY | 339 | **0** |
| 07n | RS | 638 (26 / 534 / 78) | **0** |
| 07n | TS | 638 | **0** |
| 07n | PY | 638 | **0** |

## Stops

**None.** The drop changed nothing outside B3a, and it needed no design change.

Four judgement calls, stated:
1. **One B3b assertion moved from L3 to L.** The point it makes, that a combination on a non-exact branch is inside D1, is unchanged.
2. **The contract strings' capacity pin moved to branch E.** The census code it covers is kept for B3b.
3. **The ordinary-route byte pin for m3l was not carried over** into the refusal test.
4. **Inventory sites that are B3b refusals were left unchanged.**

## Host and records

**Jobs:**
- Every cargo ran through `WT/tools/t3_cargo.sh --locked --offline`, with targets `WT/targets/i113-{base,cand}-{pp,runner,re,rh}`, `WT/targets/i113-dev-{pp,re}` and `WT/targets/i113-pyh` (PY's two helper binaries, built once from the start head's copy).
- pytest, vitest and tsc ran through `WT/tools/t3_slot.sh`.
- My base and candidate chains ran side by side, with at most three of my jobs at once. I signalled no other job.
- No DEC-025, no installs, no RSS or timing measurement.
- Scratch and `TMPDIR` were `WT/scratch/i113_b3a/`.

**Records:**
- placeholder paths only (`tools/sanitize.py`);
- no symlink and no `build` folder;
- the record screen (`tools/screen_files.py`, the host screen's patterns) has 0 hits;
- `SHA256SUMS` covers every file.

`_run_records/` holds:
- `tools/`: the chain, copy, compare, census and gather scripts as run;
- `suites/`: comparisons, junit and vitest reports, commits, diffstat and the diff;
- `census/`: both heads' census lines and the comparison;
- `reverse/`;
- `logs/`;
- `sites.json`.
