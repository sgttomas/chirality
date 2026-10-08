# I110 round 2: legacy pressure retirement, Stage 1 (implemented)

I110 is a TASK for WORKING_ITEMS (T3). The brief is `R/BRIEFS/U3_PRESSURE_RETIRE_02.md` (sha256 `d313dca0635a085b94c7f8af427d4a7bde01725334f805481ca8f9b95710d8de`, verified). The rulings are those in RR "U3 rulings on I110's pressure inventory: D-1 A, D-2 A1, D-3 held with M07". The plan is round 1's §5 Stage 1 (`R/I110/pressure_retire_01/RETURN.md`).

The branch is `codex/piping-t3-pressure-retire-20261008` in `WT/t3-pret`, cut from main `7eae707bb7` (B). It contains product files only and is not pushed.

**Stop: none.** In particular:
- No held item was touched. The diff does not include any of these:
  - the scope file;
  - `preview_physics.rs`;
  - O1–O4;
  - `request_with_refused_joint`;
  - the thread-local scope test;
  - `previewService.ts`;
  - the precision-1 fixtures;
  - the scope's pressure-bypass lines in `pressure_runtime.rs`.
- No exact-contract value was re-pinned.
- B0, B2-C and B3-D are unchanged.
- No check was weakened.
- Every outcome change is in the plan, and every byte comparison is equal.

## Commits (B..`4c0d5d7c00`)

| Commit | What |
|---|---|
| `79a5a7f316` | **Refusals.** `validate_profile` handles the cases below. The test-only scope bypass is unchanged, so O1–O4 run as before. The commit also includes the edits needed to keep the suite green (listed below). |
| `390c882619` | **Pressure-only scope oracles deleted.** 11 `*_historical_pressure_premise` tests (all except O2 and O4) and `curved_bend_pressure_load`. S-11F's F10 (2 tests, 3 helpers). S-11G's T6a pressure run and its helper. |
| `28bc6a25e1` | **Authoring.** The changes are listed below. |
| `4c0d5d7c00` | **Refusal tests.** One per route and reader, listed below. |

`validate_profile` in `79a5a7f316`:
- **Label:** `1.0.0/legacy_pressure_v1` gets `PRESSURE_MODEL_REAUTHOR_REQUIRED` (ref `pressure_contract`), with the re-author text.
- **Unknown contracts:** keep `PRESSURE_CONTRACT_UNSUPPORTED`. Its text now names only the exact contract.
- **Non-exact documents:** a pressure primitive of any value, zero included, is refused with the same code.
  - Nonzero values keep their old text, so the demo's refusal envelopes keep their bytes.
  - A zero value gets the re-author text.

Edits in `79a5a7f316` that keep the suite green:
- the dispatch unit test (zero is refused; the label is refused; `1.0.1` stays unsupported; a document without primitives passes);
- the label test becomes the ordinary-route refusal, and a new retained-entry test pins D1.3 plus the ordinary refusal it publishes;
- the shared demo fixture strips the pressures instead of zeroing them for its 39 non-held users, while O1 and O3 keep zeroing;
- 5 runner helpers strip the pressures, and the binding test skips `curved-pressure-full`, which would be load-free once stripped;
- `f1b_w2_admission_refuses_a_zero_legacy_pressure_as_pressure_thrust` is removed.

Authoring changes in `28bc6a25e1`:
- The applier refuses a pressure `create_primitive_load` with `OP-PRESSURE-PRIMITIVE-RETIRED`. Existing primitives stay editable and deletable.
- The load-case manager no longer offers the pressure category, and shows a note pointing to exact regions.
- The panel shows a model without a contract as "none (pressure-free; …)" and a labelled model as "retired". The panel's queue-profile path re-authors such a model to exact.
- The migration doc comment is updated.
- Tests: the applier test is updated, `App.test` now checks the category is "not offered", 2 panel tests are added, and the e2e smoke is updated.

Refusal tests in `4c0d5d7c00`:
- **Ordinary route** (`PP/tests/pressure_runtime.rs`):
  - a labelled model, with and without a combination, is refused, and that is the only blocking finding;
  - a 0.2.0 document with a zero primitive is refused;
  - without the primitive, it solves.
- **Runner:** CLI solve in both modes.
- **RS, PY, TS readers:** the label case is pinned as G8 `INVOCATION_MISMATCH`, at the milestone schema and at 0.3.0.
- **src-tauri:** a labelled document opens unchanged and its solve is refused.

## Evidence (this host, fresh targets `WT/targets/i110-*`, B vs candidate)

**Per-test outcomes.** Every change is in the plan:

| Suite | B | Candidate | Changes |
|---|---|---|---|
| 40 manifests (CI numerical profile, `run_suites_nff.sh` in a T3 slot) | 2776 pass / 3 fail / 80 ignored | 2765 / 3 / 80 | 21: 16 removed, 5 added. Removed: the 11 historical tests, 2 F10 tests, the old label test, the W2 zero-thrust test, and the applier test under its old name. Added: 2 source-receipt tests, 1 `pressure_runtime` test, 1 runner CLI test, and the applier test under its new name |
| src-tauri | 116 | 117 | +1 |
| `P/tests` pytest | 4426 passed, 32 skipped | 4426 passed, 32 skipped | 0. The label cases were added inside an existing test |
| vitest | 4245 | 4247 | 4: `App.test` renamed (−1, +1), 2 panel tests added. The TS reader label cases are inside an existing test |

The three failures are the same tests at B and at the candidate. All are known Mac platform failures:
- PP `t13_committed_fallback_uz_is_byte_identical`;
- the runner's two load-reference frozen-golden tests.

Held O1–O4 and the scope tests pass unchanged.

**Byte equality.** A probe-only harness (`_run_records/scripts/i110_bytes_harness.rs`) was placed in two extra detached worktrees, at B and at the candidate; it was not committed. For each document and both modes it compares the SHA-256 of:
- PP's ordinary envelope;
- the runner's mechanics envelope;
- the runner's RE export document and its export unavailability.

| Set | Rows | Result |
|---|---|---|
| E (48 exact documents) | 96 | all equal; 96 solved, 84 export documents |
| F (182 pressure-free implicit documents outside B1) | 364 | all equal |
| B1 (32 documents) | 64 | all equal |
| B1 through the retained direct entry (W1) | 64 | all equal: 34 successors and 30 ordinary publications, identical on both sides |

- F and B1 together make up the 214 pressure-free implicit documents.
- The W1 pass ran in the debug build (the registered profile).
- The B1 pin tests are unchanged and pass inside the 40 manifests.

## Linux

**Please dispatch CI on the branch head `4c0d5d7c00`** (after your push). Linux is needed for the frozen goldens this Mac cannot check (`t13…` and the runner's two load-reference tests), and for the e2e spec (`r2-smoke`), which was edited but not run here.

## Host notes

- **`node_modules`:** cloned copy-on-write from `WT/sweep-skewpin`, which has an identical `package-lock.json`, into `WT/t3-pret` and `WT/t3-pret-base`. No install or network access was involved. I could not run vitest any other way.
- **Wasm engine:** built in both trees through a T3 slot.
- **Stray temp file:** one empty scratch file was written to the system temp directory by mistake and removed at once.
- **Stopped processes:** I killed two of my own harness runs and restarted them in release mode with progress output. The 1000-node fixture took about 4 minutes per mode in release, and far longer in debug.
- **Worktrees left in place:** `WT/t3-pret` (the branch), `WT/t3-pret-base` (B), and `WT/t3-pret-hb` and `WT/t3-pret-hc` (harness worktrees, each with the untracked harness file).

## Records

This folder contains:
- `RETURN.md`
- `_run_records/`:
  - `heads.txt`
  - manifest summaries
  - `outcome_and_byte_diff.json`, which holds every changed test and the byte counts
  - the byte JSONL files
  - per-test outcome lists for tauri, pytest and vitest
  - the scripts
- `SHA256SUMS`

Paths use placeholders only.
