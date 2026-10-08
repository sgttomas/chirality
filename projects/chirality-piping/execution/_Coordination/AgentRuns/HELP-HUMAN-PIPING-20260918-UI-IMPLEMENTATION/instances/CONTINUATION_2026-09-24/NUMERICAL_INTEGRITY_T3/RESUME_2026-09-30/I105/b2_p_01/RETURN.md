# I105 lane P (I-P for B2/B3): Part 1, B3b-P (the exact route), and a stop before Part 2

TASK (Type 2), I105, lane P's implementer, for ROOT (HELP_HUMAN, Agent 0); no delegation. 2026-10-08 UTC. Fresh instance.

**Brief:** `R/BRIEFS/B2_P_LANE.md` (`525e5cd8…`) with `R/BRIEFS/B1_COMMON.md` (`2d170307…`), both verified. Basis read (sums verified against each folder's SHA256SUMS): I93 PLAN (`e1147dbd…`) §1.2.4–§1.2.8, §1.4, §6 with REVISION_01 (`63abb73f…`); B3-D `R/I96/b3_d_01/` DESIGN (`ad7942f6…`) with REVISION_01 (`6f5b1a6d…`); I99's PROBE; I85's RETURN; I102's and I103's RETURNs; RR "RV116 (RV-D) accepts B3-D …", "RV116 confirms B3-D's revision 01; …", "RV115's addendum accepts B3-K …", "I99's B3-W verified; …", "Lane A returned; `b2` built …".

## Heads

| Part | Commits (`WT/b2`, `codex/piping-t3-b2-20261008`, over `e67c364680`; not pushed) |
|---|---|
| 1. B3b-P | `8d3419b542` (producer, pins, fixtures), `cc24cd955c` (tests), then **`22e9d00062`** (tests: two mutant kills) |
| 2. B2-P | **not started** (the stop below) |

## The stop (brief: "if you need a change outside your files")

B3b-P changes the behaviour that lane A's interim oracle pins. `PP/retained_memory_law_tests.rs` `b3b_direct_entry_keeps_the_exact_ordinary_bytes` asserts `W1Fallback::Domain` for m3x, n05 and n06 (its doc: "no producer change yet"). After B3b-P the exact route runs W1: n05 and n06 are `Coexistence` with the same exact bytes, and m3x reaches precommit, where today's RS refuses `physics-retained-1` at G0, so it publishes the ordinary bytes plus one notice. **In the registered build that one lane-A test now fails; nothing else changed.**

- **Proposed, not applied:** `_run_records/proposal/lane_a_b3b_direct_oracle.diff` (that test only: coexistence pins keep exact bytes; m3x accepts the successor, or today's G0 refusal with one notice).
- **Checked:** applied in a scratch archive of `cc24cd955c` (`22e9d00062` changes only my tests), lane A's law tests pass 55 of 55 in the registered build (`proposal/propcheck_law_tests.log`).
- **For ROOT:** route it to lane A, or authorize me to apply it; then Part 2 can start from `22e9d00062`.

## Part 1: what changed (PP only; B3-D's P-numbers)

- **P-1:** `lib.rs` `w1_route` decides the route once from lane A's `namespace_branch`: L and L3 preview, E exact; load states and 0.4.0 stay `Domain`. The observer is built on the route (`permitted_probe_on`); the private driver uses the same decision.
- **P-2:** `w1_budget`: the exact route's per-case exact-block limit is `PHYSICS_SOURCE_WORK_LIMIT` (8,000,000), as `ordinary_dispatch`'s.
- **P-3, P-5:** on the exact route the capture records each used material's ν and refuses typed unless the basis is `homogeneous_isotropic_E_nu_v1` and Ĝ is a positive normal equal to RN64(E/(2·RN64(1+ν))); members carry `ProductMaterial::BaseENu`; a selected basis is refused.
- **P-6:** the exact route's observables over physics-1's closed evidence (`{pressure: [], connector: [], exact_cases}`; the eight entry keys; profile, basis, complete coverage, no assembly group and +0 vectors; sections and materials bound to the captured OD, wall, E, ν, Ĝ), then the shared extrema, support and headline checks.
- **P-7, P-8:** maxima read `exact_cases[c]`; the owner case's `pipe_sections` take the prepared A, I, J, Z beside its extrema (same stage); unselected entries untouched.
- **P-9, S-1:** one route descriptor (`retained_wire::route_wire`): identity `physics-retained-1`, profile `exact_straight_retained_w1a_v2`, DEF-E's id on every attempt and DEF-E's H (`5a3bac43…`) in the preparation payload, `derived_e_nu` shear origin, `geometry.route: exact`. The preview route's bytes are unchanged.
- **P-10, P-11:** no PP change: precommit calls `retained_precision::validate` as before, and the legacy disposition is the existing machinery. The receipt carries no legacy disclosure on the selected case (asserted).
- **P-12:** two new hooks, `fault_next_exact_capture` and `break_next_section_overlay`.
- **P-13:** the pins below. Refused exact requests take the ordinary route: a combination, regions absent or non-empty, 0.4.0, and a point basis (`b3b_refused_exact_requests_take_the_ordinary_route`).
- **P-4** is a static test: no retained file or W1 function names a pressure-runtime builder.
- **One expected-text change** in a guard of mine: `u3_capture_permit_is_linear` now looks for `ProductCapture::permitted_probe_on(permit, route);` (the permit still moves into the observer; the test states why).

## Pins (both modes; `retained_facade_tests.rs`)

| Witness | Sparse | Dense |
|---|---|---|
| m3x exact successor: receipt; bytes; fixture document | `b1b4a668…896f`; `f18227f7…b20d`; `02465c6c…56d6` | `eabd2fc5…776d`; `e31f03a4…db2a`; `31f10f04…47cc` |
| m3x_mix_anchor (`case` selected, `case:b` not_required): receipt; bytes | `71703ab1…b29f`; `ca2cd750…a53b` | `b5cf5a4f…eec3`; `a50c530f…1337` |

- **New fixtures:** `P/fixtures/results/retained_precision_exact_successor_{sparse_interactive,dense_scrutiny}.json` are the live successor documents, byte for byte (tested).
- **The section evidence** (m3x, M1): SourceAnnulus's I/J/Z `…210b/…210b/…a7` become the prepared `…210a/…210a/…a6` (A unchanged), exactly B3-D §1.3's table; the receipt's section terms equal them (G5b's cross-check, asserted).
- **The receipt** shows Ĝ `4232a05f20000000` (8e10), ν `3fd0…`, `legacy_source_work[0].limit` 8,000,000, no legacy disclosure on the selected case, 98/99 rows all with the method token, `not_covered` empty.
- **Inputs:** m3x, m3x_mix_anchor and m3l built in the tests equal B3-W's Value sha256s (`c920a96d…`, `6ca777a6…`, `2f5ff465…`); n05, n06 and `fields` are the committed requests (`332319ee…`, `5551f164…`, `7f8ff9d5…`).
- **SCHEMA (G1 shape):** both new successors' `retained_precision` validate with 0 errors (jsonschema 2020-12; `scripts/schema_check.py`).

## What the readers do today (pinned and stated)

- **RS's precommit refuses every exact successor at G0 `SOURCE_PRODUCER_CONTRACT_UNSUPPORTED`** (no `physics-retained-1` branch until B3's readers land). So m3x and the mixed base fall back with the ordinary physics-1 bytes plus one N1 notice per case in A. The tests accept that or a validated successor and print which.
- **m3l (B3a): no producer change.** W1 runs to precommit; RS's G8 refuses (`INVOCATION_MISMATCH`, the contract); the successor differs from the milestone's pinned one in exactly `invocation.value`, `legacy_source_work[0].charged` and `receipt_sha256`; the ordinary bytes differ in exactly `diagnostics[3].message`.
- **N-11:** the noticed physics-1 fallback (Direct; and after serializer, section-overlay and precommit faults) is accepted by physics-1's base readers with the same contract and standing in **RS** (test), **PY** (`compatibility._source_contract`, standing; 8 of 8, each with a refused negative control) and **TS** (`sourceContract`, `validatePhysicsEvidence`, `numericalResultStanding`; vitest 9 of 9) (`_run_records/n11/`).

## Suites against `b2` at `e67c364680` (test by test; `_run_records/suites/`)

| Suite | `e67c364680` | `8d3419b542` | `22e9d00062` (head) |
|---|---|---|---|
| PP, all targets | 748 ok, 1 failed (t13), 11 ignored | 762 ok, 2 failed, 11 ignored: 15 added (all ok); **1 changed: lane A's oracle ok → FAILED** | 763 ok, 2 failed, 11 ignored: 16 added (all ok); the same 1 changed |
| Runner (all tests) | 85 ok, 2 failed (load-reference) | identical | identical |
| PP's dependents (`self_weight_wasm`, `operation_applier`; `--no-run --all-targets`) | compile | compile | compile |
| `src-tauri` (`cargo check --all-targets`, a PP dependent) | not run | not run | compiles |

The failures other than lane A's oracle are the base's own: PP `s11g_tests::t13_committed_fallback_uz_is_byte_identical` (RR's "known Mac `t13`"), and the runner's two load-reference tests. Every c = 1 and B1 multi-case pin is unchanged (no other test changed). FK is untouched.

## Mutants (`_run_records/mutants/`)

One per new check (59; `mutants/p1.json`), each an exact edit of a scratch archive, run with PP `--lib` filtered to the B3b, B3a, `u1_constants`, `u3_permitted_path` and W-C2 transaction tests (lane A's failing oracle skipped). Each is killed by a named failing assertion (`mutants/logs_*`).

- **On `cc24cd955c`'s tests: 56 killed, 3 survived.** I added assertions for two of the survivors in `22e9d00062`, then reran the three survivors on it: P1-42 (`ProductCaseView::number` reading the preview evidence) and P1-34 (the observables' section coverage) are now killed.
- **Result: 58 of 59 killed.**
- **The one survivor, P1-02, is equivalent:** `w1_route`'s load-state guard. 0.4.0 has no namespace branch, so `namespace_branch` already returns no route. I kept the guard as a defensive check.

## Notes for ROOT

1. **The stop** (above): one lane-A test; proposal and check attached.
2. **Readers:** until B3's readers land, no exact successor publishes; the new successors' bytes are pinned on the private driver and the Direct entry (the same bytes reach precommit).
3. **One defensive check kept, equivalent by construction:** `w1_route`'s load-state guard (P1-02).
4. **N-11** needed no physics-1 reader change: the readers accept the notice.

## Host and records

- Every cargo ran through `WT/tools/t3_cargo.sh --locked --offline` with targets `WT/targets/i105-b2-p-{pp,runner,self_weight_wasm,operation_applier,tauri,dev,mut}`; PY and vitest through `WT/tools/t3_slot.sh`; one heavy job of mine at a time; no RSS or timing measurement, no DEC-025, no install. Scratch and `TMPDIR`: `WT/scratch/i105_b2_p/`. The TS check ran in a scratch archive of `e67c364680` (TS is untouched) with `node_modules` linked from the App worktree and the wasm assets copied from `WT/sweep-skewpin` (sums in `n11/ts_wasm_assets.sha256`); vitest's cache stayed in the archive.
- **A slip, disclosed:** I started a second wait loop on the mutant job while my first wait was still running, then stopped it. Afterwards each job had one wait. I signalled no other job.
- Records: placeholder paths only (`scripts/sanitize.py`), no symlink, no folder named `build`. The host screen (`WT/tools/t3_host_screen.py`) over `e67c364680..22e9d00062`: 9 files, 0 hits; over these records (`scripts/screen_files.py`, its patterns read whole files): 0 hits.
