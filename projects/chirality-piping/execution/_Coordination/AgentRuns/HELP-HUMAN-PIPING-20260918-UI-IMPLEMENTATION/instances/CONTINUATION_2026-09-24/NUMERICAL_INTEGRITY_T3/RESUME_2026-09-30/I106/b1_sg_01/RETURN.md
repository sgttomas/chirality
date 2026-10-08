# I106 B1 SG RETURN: the Direct-entry gates on B1's candidate with the registration applied

**Verdict: PASS on all four gates. No unexplained row, no stop.**
- **Pressure:** refused at D1.5 `Family(Case, PressureRegions)` with the exact ordinary bytes and no notice, at c = 1 and at c = 2 (pressure on the second case only).
- **Coexistence:** n05 and n06 (16 rows) and SP's multi-case pin input (`n05_two_cases`) are admitted and settle by `Coexistence`, with the exact ordinary bytes and no notice.
- **Sweep:** Stale is byte-identical to base. Registered differs from base in 8 rows. All 8 are D1.4's widening, and the published bytes are unchanged in every one of them.
- **Callers:** no product caller of the retained entries.

**Who and when:** I106 (TASK, Type 2), role I-G, dispatched directly by ROOT; 2026-10-08 UTC. The brief is ROOT's dispatch with `R/BRIEFS/B1_COMMON.md`. The method is PLAN_v2 §3.10 (`R/I84/b1_plan_01/PLAN_v2.md`, sha256 `c85786b7…19be0`, verified) by I61's `R/I61/u9_g8_01/`.

**What I read:** NUM `AGENTS.md`, `agents/AGENT_TASK.md` and B1_COMMON; PLAN_v2 §1, §2, §3 and §4; I61 u9_g8_01 (RETURN, `run_g8.sh`, `compare_g8.py`, the pressure harness, outputs) and u3_grant2_01's sweep harness; RR "I4 made at `30f3d1b24a`; …", "R6a: …" and "SQ complete; …"; `R/I85/b1_sp_01/RETURN.md` (T-1 to T-13, T-12's notices), `I3_01.md` §0–§2 and `R/I85/b1_st_01/RETURN.md` §0–§3 (T-4); and `R/I104/b1_sq_01/registration.diff`.

**Placeholders:** WT, NUM, P, PP, T, R and RR as in B1_COMMON. `S` = `WT/scratch/i106_b1_sg`; `O` = this folder's `outputs/`.

## 0. Candidate and base

| | Commit | Why |
|---|---|---|
| **Candidate** | `0d19f995b503b7ce12ec05758ef3af3ec72ca758` | The brief's commit (b1: SP, SA, the three readers, SC and SQ merged). It was copied with `git archive` (P/core, P/fixtures, P/schemas; 1,047 blobs) into `S/cand/tree`, and `registration.diff` (sha256 `d85101ea…7d6526`, one hunk: `threshold_bytes` 4,026,531,840 → **11,274,289,152**) was applied there with `patch -p1` (`O/registration_applied.diff`) |
| **Base** | `2007709549e9701b302e0eb62a1474d82acc1c40` (main's #1107 merge, B6) | It is `git merge-base 0d19f995b5 origin/main`, and it is **b1's I1′ main base**: the second parent of `262bd687f0` ("I1 (= I1′): … absorb main 2007709549"). It is the only main commit that b1 absorbed, and no later main commit is reachable from the candidate. Outside `execution/`, P differs between the two only in B1's 33 files. Copied the same way (1,044 blobs) into `S/base/tree` |

**The copies were checked against the commits' blobs** (`git hash-object` without `-w`; `_run_records/verify_tree.sh`):
- the candidate differs only in `retained_memory.rs` (the registration) and `lib.rs`;
- the base differs only in `lib.rs`.

In both copies, `lib.rs` has the same 5 appended lines declaring two `#[cfg(test)]` harness modules (`O/lib_rs_delta_{cand,base}.diff`).

**Builds:** 4 fresh targets, `WT/targets/i106-sg-{cand,base}-{reg,stale}`. Stale is `RUSTFLAGS=--cfg=i106_sg_stale`. Every Direct row reports the intended status: `Registered`, or `Stale` at D1.1. Each run passed 2 of 2 harness tests (`O/run_summary.txt`, `O/archive_and_runs.txt`).

## 1. The harnesses (I61's, adapted to B1)

- **`zz_i106_sg_sweep.rs`** is I61's grant-2 sweep. The only change is T-12's notices:
  - **The new reading:** a fallback publishes the ordinary bytes plus one N1 notice per case in A, in request order. A form that is not exactly that is still `OTHER`, and the harness panics on it.
  - **At c = 1 the reading is I61's.** The class is still `notice` for one notice; `notice_x<k>` is new and stands for k ≥ 2 notices.
  - **Proof that the adaptation is neutral:** the base sweeps are byte-identical to I61's u9_g8_01 sweeps (registered `9a74ff16…`, Stale `0e2db8b8…`).
- **`zz_i106_sg_gates.rs`** is I61's pressure harness. Its four requests are unchanged, and B1 adds three:
  - `milestone_two_cases_pressure_on_second`;
  - `n05_two_cases`, a verbatim port of SP's pin builder;
  - `w_c2`, the request inside each committed W-C2 successor fixture.

  It also records `n1_notices` and `load_cases`.
- **On I61's four requests, every recorded field is identical to I61's `pressure_reg.json`,** in both the candidate and the base registered builds.

## 2. Gate 1: pressure (`O/gates_*.json`; checks in `O/compare_sg.json`)

| Request | Ordinary (value route) | Candidate, registered Direct | Stale | Base, registered |
|---|---|---|---|---|
| milestone | `MECHANICS_SOLVED` | **successor**, admitted, equal to the pinned `retained_precision_milestone_successor_<mode>.json` `source` (dumps `1d9ba709…` / `7c5fe5c5…` = I61's) | exact, D1.1 | the same successor |
| milestone with pressure | `MODEL_INCOMPLETE` (`PREVIEW_CONTRACT_VERSION_MISMATCH`) | **exact, refused at D1.5 `Family(Case, PressureRegions)`**, cause none, 0 notices | exact, D1.1 | the same |
| **milestone, two cases, pressure on `case-2` only** | the same refusal | **exact, D1.5 `Family(Case, PressureRegions)`**, 0 notices (D1.5 now checks every case) | exact, D1.1 | exact, D1.4 `Family(Invocation, LoadCases)` |
| PHYS-R4, pressurized | `MODEL_INCOMPLETE` (`NUMERICAL_INTEGRITY_UNRESOLVED`) | exact, D1.3 `Family(Namespace, SchemaVersion)`, 0 notices | exact, D1.1 | the same |
| PHYS-R4 without pressure | `MECHANICS_SOLVED` | exact, D1.3, 0 notices | exact, D1.1 | the same |

**Every check holds, both modes:**
- the value route's bytes are equal across the candidate's two builds and the base;
- each exact Direct row's bytes are the value route's.

## 3. Gate 2: coexistence

- **The sweep's 16 n05/n06 Direct rows** (top-level and `ui/`, both modes). Registered, every one is:
  - exact, equal to the value route's bytes;
  - `(Registered, None)`, that is, admitted;
  - `Coexistence`.

  Stale, every one is exact at D1.1. Each row equals base's.
- **SP's multi-case input `n05_two_cases`** (c = 2), both modes: admitted (no refusal), `Coexistence`, exact ordinary bytes, 0 notices. Stale gives exact at D1.1. Base refused it at D1.4.
- **W-C2** (c = 3, informational), registered: the successor. Its published bytes are `c7a18593…` (sparse) and `a77c010b…` (dense), equal to SP's pins (I3_01 §2) and to the fixtures' `source`. It carries no N1 notice; its one `RETAINED_PRECISION_UNAVAILABLE` is case-c's receipt-backed diagnostic. Stale gives exact at D1.1.

## 4. Gate 3: the u3g2 sweep, registered and Stale

The sweep is 36 request-shaped fixtures × 9 route/mode outputs = 324 rows per build. The row keys are the same in base and candidate.

| Build | Candidate sha256 | Base sha256 | Differing rows |
|---|---|---|---|
| **Stale** | `0e2db8b89745fdf11c1cc3a263e66d901ba134490ab14a1c5e2e83947c452586` | `0e2db8b8…` | **0, byte-identical** |
| Registered | `cc6350d0a3614aeebbd5ff68d498518759ad2ece6cd221f5a140e4d11f0c1425` | `9a74ff16d42c2b5afe321ee1889e0f307af946f65d3c1ab8f6dd01bd3c539b62` | **8**, all explained |

**Every registered difference, row by row** (all on `retained_direct`; the typed, value and Headless routes are identical):

| Fixture (c = 2, no combination or component) | Mode | Published sha256 (base = candidate) | Base | Candidate | Explained by |
|---|---|---|---|---|---|
| `product_preview/source_blocks/multicase-dense_scrutiny.request.json` | dense | `5affe0d9…` | exact, D1.4, none | exact, admitted, `Coexistence` | D1.4 |
| the same | sparse | `38d8e668…` | the same | the same | D1.4 |
| `…/source_blocks/multicase-sparse_interactive.request.json` | dense | `5affe0d9…` | the same | the same | D1.4 |
| the same | sparse | `38d8e668…` | the same | the same | D1.4 |
| `…/source_blocks/ui/multicase-dense_scrutiny.request.json` | dense | `e2fc5c13…` | the same | the same | D1.4 |
| the same | sparse | `ba1a75ed…` | the same | the same | D1.4 |
| `…/source_blocks/ui/multicase-sparse_interactive.request.json` | dense | `e2fc5c13…` | the same | the same | D1.4 |
| the same | sparse | `ba1a75ed…` | the same | the same | D1.4 |

**The explanation:**
- **Base refused c = 2 at D1.4** (C = 1). The candidate's D1.4 (SA: 1 ≤ c ≤ 3, no combination or component) admits it.
- **The ordinary route then selected exact blocks,** so `retained_w1` returns `Coexistence` before T-4 (D-15).
- **The published bytes are the same in both.** Only the private admission report and the cause differ.
- `compare_sg.py` checks each row against the rule: base at D1.4, c ∈ [2, 3], no combination or component, the candidate past D1.4, exact = value bytes. **No row is unexplained.**

**T-4 and T-12 explain no sweep row.** This is expected:
- **The only admitted c = 1 rows that reach W1** are the milestone (successor) and `rejected_stress_range` (4 Preparation notices). Their cases are in A, so T-4 does not fire, and they are unchanged.
- **Every other admitted row returns at `Coexistence`** first.
- **The newly admitted multi-case fixtures** also settle by `Coexistence`, so no notice is published, and T-12 is not reached.
- **T-4 at c ≥ 2** (W-C2's B is `not_required`) and the multi-case successor are shown by gate 2's W-C2 row.

**Still refused at D1.4 in the candidate:**
- `invented_dec092_temperature_g_request.json` (3 cases, 1 combination);
- `invented_preview_model.json` (2 cases, 1 combination, 5 components).

D1.9's 2 rows and D1.3's 32 rows are unchanged.

**Registered Direct counts** (classes; then the admission reports):

| Build | Classes | Reports |
|---|---|---|
| Base | exact 64, successor 2, notice 4 | D1.3 ×32, D1.4 ×12, D1.9 ×2, admitted ×24 |
| Candidate | exact 64, successor 2, notice 4 | D1.3 ×32, D1.4 ×4, D1.9 ×2, admitted ×32 |

The candidate's +8 admitted are the 8 rows above.

## 5. Gate 4: the caller scan (`O/caller_scan_classified.txt`)

`git grep` at `0d19f995b5` over the whole repository, except execution records, for `with_retained_direct`, `with_retained_headless`, `run_preview_model_value_with_retained_headless` and `RetainedHeadlessContext`: 43 hits (42 at base).

| Where | What |
|---|---|
| PP's definitions and re-export | `lib.rs` :122, :2264, :2271, :2274; `retained_memory.rs`, the context type |
| PP's `retained_memory.rs` :3060 | A call inside `#[cfg(test)] mod tests` (:3026–:3153) |
| PP's tests | The facade, law and wire tests; `tests/retained_memory_challenge.rs`; `tests/retained_precision_admission.rs` |
| `runner/headless/src/lib.rs` :740 | The wrapper, which calls only the Headless entry (refused at D1.0). Nothing in the runner calls the wrapper |
| `runner/headless/tests/retained_precision_admission.rs` | The reviewed runner test |
| Corpus and Python test | `"entry"` strings in `retained_precision_cases.json`, and the PY test asserting them. These are data, and already at base |
| **Everywhere else** | **None:** `P/apps` (src-tauri, desktop), `self_weight_wasm`, `operation_applier`, `validation/benchmarks/*`, and everything outside P |

**B1's delta is test-only:** one more Direct call in the law tests, and the challenge's import and call text.

## 6. Limits kept

- **Cargo:** every job went through `WT/tools/t3_cargo.sh` (`--locked --offline`), one of mine at a time. Four jobs ran one after another in slot 4, 12:52:18Z–12:54:34Z (`O/cargo_jobs_i106.log`).
- **Background work:** the chain ran in the background with one waiter, which ended when the chain's process had gone. I signalled or killed no job.
- **Not run:** DEC-025, measurements, native or solver-at-scale jobs, or installs. I ran nothing in `WT/b1`.
- **Git:** no writes. Reads used `GIT_OPTIONAL_LOCKS=0`, and `hash-object` ran without `-w`.
- **TMPDIR** was my scratch. I wrote one stray empty file to the system temp directory by mistake, and deleted it at once.
- **Records:**
  - placeholder paths only;
  - no symlink, and no folder named `build`;
  - screened for the strict path forms and this machine's names: none found.
- **Kept in `S`, not pruned:** both copies, the full logs, and the four successor dumps (hashes in `O/archive_and_runs.txt`).

## 7. Files

- **`_run_records/`:**
  - `zz_i106_sg_sweep.rs` (`f3d9642a…`) and `zz_i106_sg_gates.rs` (`f2c2f83a…`), as run;
  - `run_sg.sh` and `verify_tree.sh`, with machine paths replaced by `WT`/`NUM`;
  - `compare_sg.py`.
- **`outputs/`:**
  - `sweep_{cand,base}_{reg,stale}.tsv` and `gates_{cand,base}_{reg,stale}.json`;
  - `compare_sg.json` and `compare_sg.txt`;
  - `caller_scan.txt`, `caller_scan_base.txt` and `caller_scan_classified.txt`;
  - `registration_applied.diff` and `lib_rs_delta_{cand,base}.diff`;
  - `archive_and_runs.txt`, `run_summary.txt` and `cargo_jobs_i106.log`.
- `SHA256SUMS`, which covers every file above except itself.
