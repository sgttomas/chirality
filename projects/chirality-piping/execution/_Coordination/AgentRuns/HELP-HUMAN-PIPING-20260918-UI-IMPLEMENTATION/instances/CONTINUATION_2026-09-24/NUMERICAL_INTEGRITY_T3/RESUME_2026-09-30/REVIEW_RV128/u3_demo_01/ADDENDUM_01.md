# RV128 addendum 01: I114's round 2 on the demo lane (head `9744ed7e69`)

**Who:** RV128, TASK (Type 2), the same independent reviewer, re-dispatched by WORKING_ITEMS for T3 (Agent 1) by message, 2026-10-08 UTC. I wrote none of the work and did not delegate. I made no Git writes.
**Candidate:** branch `codex/piping-t3-demo-fixtures-20261008`, head `9744ed7e69`: one commit on `180bf9b26d`, 30 files.
**Records under review:** I114's round 2 record `R/I114/demo_fixtures_02/RETURN.md` (sha256 `d8a03b7d…5f4a2ade`; its 18 SHA256SUMS entries verify).
**Basis:** RR "U3, I114's demo lane and WORKING_ITEMS' three items" (item 1: the default session model switches; item 2: the comparison throw goes to T6; item 3: the carrier is accepted). RR "U3, I110's round-4 stop on two published texts" (T4: `preview_physics.rs:75` stays unchanged). My round 1 review is `REVIEW.md` here (sha256 `286a315e…0f5b77`).
**Working copies:** archive `WT/rv128/cand2` (head); clone `WT/rv128/regen2`; my base archive `WT/rv128/base` (`4c0d5d7c00`). Targets `WT/targets/rv128-{demo,tauri,pybins}`.
**How things ran:**
- Every cargo went through `WT/tools/t3_cargo.sh --locked --offline`; vitest, pytest and e2e went through `WT/tools/t3_slot.sh`.
- e2e ran with `CI=1` and one worker, after checking that port 5174 was free.
- `node_modules` is a copy-on-write clone (same lockfile). The wasm engines are my round 1 build; their crates are unchanged since `4c0d5d7c00`.

## Verdict

**CONFIRMED. 0 BLOCKING, 0 SHOULD-FIX, 5 NOTES.** Round 1's two SHOULD-FIX items are closed (S-1) or acceptably marked under ROOT's routing (S-2).
- **The default-model switch is complete,** and the solve check is real.
- **No test was weakened.**
- **The 8 B4 wheel-scroll failures are host-specific.** They come from the browser binary the Playwright config picks on macOS, not from the code or this lane.

## 1. The default-model switch (ROOT item 1)

**Complete for the app.**
- **Browser fallback:** `loadModelFixture` reads `invented_demo_model.json` (`P/apps/desktop/src/services/previewService.ts:627-634`) and serves both the session model and the bundled reference's model.
- **Native:** `load_preview_model` and `resolve_solve_model_payload(None)` read it (`P/apps/desktop/src-tauri/src/lib.rs:1535-1540`, `:1568-1573`), and the agent-proposal fallback id names the demo (`:1896`).
- **Other references:** the review-geometry source basis and the e2e benchmark route matchers name it.
- **Nothing left behind:**
  - No non-test app code (src, src-tauri, Python service) reads `invented_preview_model.json` any more.
  - The one remaining `project:invented-loop-01` in src-tauri is synthetic test data (`lib.rs:6776`).
  - The runner's references are its refusal tests.

**The solve check is real** (`_run_records/a1_native_checks.out.txt`).
- **Suite:** src-tauri full, 118 passed, including `default_session_model_solves_in_both_modes`.
- **Mutant M1:** the default goes back to `invented_preview_model.json`. Killed, at `lib.rs:7168`.
- **Mutant M2b:** the demo keeps its id but carries the refused model's `load:L-100-P` primitive. Killed by the `MECHANICS_SOLVED` assertion at `lib.rs:7157`, because the solve returns `MODEL_INCOMPLETE`.
- **Probe 3:** the native solve of the default model in each mode equals the committed bundled reference (`invented_demo_result_preview_physics_1_{sparse,dense}.json`) as a JSON value. The reference is therefore exactly the product's output for the app's own default model.
- After each probe and mutant the archive was restored, and its files compare equal to the head's blobs.

**The browser:**
- the default model's solve is now `BROWSER_SOLVE_BACKEND_REQUIRED_REFERENCE_ONLY`;
- an edited copy is `…_FOR_EDITED_MODEL`;
- both are pinned in `sourceBlockRecovery.test.ts:241-253`.

**Provenance after round 2** (`_run_records/a1_regeneration.out.txt`). Both recipe modes, run in `WT/rv128/regen2`, reproduce all eight files byte-for-byte:
- the model;
- the demo pair;
- the carrier;
- the refusal pair;
- **both generation records.** They no longer hash stderr, so they now reproduce across checkouts.

**What changed from round 1:**
- The carrier differs in one line: `component_stress_modifier_count` is now `null`. This follows the producer's own definition (`PP/src/preview_physics.rs:680`, the count of intensified rows).
- The model differs only in its description and the two load-case labels. Against PP's model it now differs in identity, description and labels.

## 2. My round 1 items

| Item | Status | Evidence |
|---|---|---|
| S-1 | **Closed** | `P/apps/desktop/src/features/results/ResultsPanel.test.tsx:20-35`, on the actual unicode-ids output. It checks the row id, its two source refs, the recovery basis `explicit_user_linear_combination; combination:combination:Σ`, each source ref rendered, the absence of "not a combined result", and immutability. It is stronger than my probe |
| S-2 | **Acceptably marked** | The vacuous display-unit assertions are gone. The test is renamed to say what it pins (`App.test.tsx:13938-13949`), and `it.todo` (`:13957`) names the gap and ROOT's routing to T6 (RR item 2). The empty-state and gate assertions are kept. vitest reports the todo (4248 passed, 1 todo) |
| N-1 | Open, optional | Unchanged |
| N-2 | Open, optional | The oracle now imports the invented preview model directly (`reportPackageRequest.test.ts:11`, `:98`), but `legacyProvenanceSession` still rebinds the carrier's `model_ref` (`:83`) |
| N-3 | **Closed** | L-100 "Invented operating gravity, occasional and thermal preview"; L-200 "Invented alternate gravity and occasional preview". They match the primitives (weight, occasional, thermal / weight, occasional) |
| N-4 | **Closed** | The recipe nulls a nonzero count of a removed kind and records it. `test_preview_physics_consumer_contract.py` asserts both nulled members. RE's carrier case pin follows it (RE 17/17) |
| N-5 | **Closed by ruling** | ROOT (T4): the limitation text stays; its wider wording waits for the next corpus generation |
| N-6 | **Closed** | `DEMO_FIXTURES.md` says four changes and names the Python service |
| N-7 | **Closed** | No `stderr_sha256`, and the record test asserts its absence |

## 3. No test was weakened (`_run_records/a1_test_inventory.out.txt`)

**Counts and renames.**
- No test was deleted, and every changed e2e spec keeps its test and assertion counts.
- `App.test.tsx` goes from 144 to 145 tests (the `it.todo`) and from 3906 to 3900 `expect` calls. All six fewer calls are accounted for:
  - **C-150's seven inspector and tree assertions** in the viewport-selection test become one absence assertion: the default model has no joint. The expansion-joint inspector content (mapped pipe, area, movement, 3200000 N/m, 620000 N·m/rad, the no-catalog source) stays covered by the authoring test (`App.test.tsx:12950-12959`). Component selection with an active tree row stays covered for C-110, C-130 and C-140 (`:4930-4972`).
  - **Two Tier3 assertions** were vacuous (S-2).
  - **The MODEL_INCOMPLETE workflow test gains two.**
- `ResultsPanel.test.tsx` adds one test (6 to 13 `expect` calls). `sourceBlockRecovery`, `previewService`, src-tauri and the consumer-contract test each gain assertions.

**Re-pointed tests.**
- **The load-manager magnitude flow** moves from the retired pressure primitive (Pa) to the demo's thermal primitive at the same index (12.5 to 20 degC). The flow under test is the same, and its expectations are the product's rendering.
- **The MODEL_INCOMPLETE workflow test** now opens the refused model through the native `load_preview_model` mock, so its real envelope stays paired with its own model.

**Suites on the head** (`_run_records/a1_suites.summary.txt`):

| Suite | Result |
|---|---|
| vitest, full | 141 files; 4248 passed, 1 todo |
| pytest, the 6 files | 277 passed |
| RE carriers | 17/17 |
| src-tauri | 118 |
| e2e, four reference-dependent specs (`r2-smoke`, `gui-workflow-validation`, `result-compatibility`, `ui-foundation`), both projects, browser as configured | 118 passed (`_run_records/a1_e2e_head.summary.txt`) |

**Correction to my round 1 review.** Its §3 said "No dangling consumer". That missed four e2e specs that pin the bundled reference through the UI rather than by file name:
- `result-compatibility{,-dist}.spec.ts:20`;
- `ui-foundation-dist.spec.ts:51`;
- `ui-foundation.spec.ts:880-894`.

At `180bf9b26d` they still expected 830/832 rows and `project:invented-loop-01`. Round 2 fixes them.

## 4. The 8 B4 wheel-scroll e2e failures (WORKING_ITEMS' question)

**Host-specific: the browser binary, not the code.** Evidence in `_run_records/a1_b4_wheel.out.txt`:

| Run | Browser | Result |
|---|---|---|
| A. Base `4c0d5d7c00` on this Mac | Installed Google Chrome, which `P/apps/desktop/playwright.config.ts:4-11` selects on macOS whenever it exists | **All 8 fail.** `b4-table-editing.spec.ts:704`: `scrollTop` stays 0 after `mouse.wheel` |
| B. Same commit, same Mac | Playwright's bundled `chrome-headless-shell` 1223 (already in the Playwright cache; nothing installed), set with `PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH` | **All 8 pass** |
| C. Round 2 head `9744ed7e69` | Bundled headless shell | **All 8 pass** |
| D. Linux CI on `4c0d5d7c00` (Actions run 37830652481, job 113494967954, ubuntu-latest) | CI default | **The same 8 pass** |

The failures follow the browser binary chosen on macOS, not the commit or the lane. Route it as a test-environment item:
- either point this host's e2e evidence runs at the bundled browser;
- or make the wheel step independent of the browser's synthetic-wheel handling.

## Notes

| ID | Where | Note |
|---|---|---|
| A1-N-1 | `P/apps/desktop/e2e/result-compatibility.spec.ts:4`, `result-compatibility-dist.spec.ts:4` | The comment still says "The retained 830-row / 828-witness package oracles remain in StressNeutralExportPanel.test.tsx". They are now 513 and 511. Comment only |
| A1-N-2 | `P/apps/desktop/e2e/ui-foundation/benchmark-harness.ts:1517`; `previewService.ts:627-634`, `:719` | The session default and the bundled reference's model now load the same module. So `routeModelFixture` (used by `gotoRoutedFixture` and `gotoModel`) also replaces the reference's model. Latent: no routed test inspects the reference today (the dist test's "regular" branch loads unrouted). A routed test that did would get `BROWSER_FIXTURE_MODEL_BINDING_MISMATCH` |
| A1-N-3 | src-tauri tests | Optional: pin probe 3's equality (default-model native solve = bundled reference, both modes) as a test. It would tie the reference to the default model, and it would demand regeneration when I110's merge changes the product's output |
| A1-N-4 | `PP/src/lib.rs:1944` (ROOT's T2 correction in I110's lane) | Its re-pin reaches `P/fixtures/results/precision_connected_ui_mechanics_{sparse,dense}.json` (RR "I114's precision-1 pair"), which round 1 adopted as the precision-1 subject of four tests (`physicsResultExport`, `KnownSemanticNotices`, `test_analysis_run_compatibility.py`, `test_preview_physics_consumer_contract.py`). Re-run those after the merge. The demo pair does not carry that text |
| A1-N-5 | Merge with I110 | My round 1 §5.1 still applies: re-run both recipe modes on the merge commit. Records now compare byte-for-byte across checkouts, so compare them too |

## Records

- `ADDENDUM_01.md` (this file)
- `_run_records/`:
  - `a1_regeneration.out.txt`, `a1_native_checks.out.txt`, `a1_probe3_native_default_vs_reference.rs.txt`;
  - `a1_b4_wheel.out.txt`, `a1_suites.summary.txt`, `a1_test_inventory.out.txt`, `a1_e2e_head.summary.txt`.
- `SHA256SUMS`, regenerated over the folder; `REVIEW.md` is unchanged.

Paths use placeholders only.
