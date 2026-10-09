# RV127 addendum 03: A2-B-1's repair on PR #1168

**Who:** RV127, TASK (Type 2), for WORKING_ITEMS (T3, Agent 1), 2026-10-09 UTC. I wrote none of this and did not delegate.

**The request:** WORKING_ITEMS' message. Confirm, from my kept scratch, that A2-B-1 is repaired as ROOT ruled.

**Basis:**
- ADDENDUM_02 (`5482aa72…`);
- the carry-over conditions as WORKING_ITEMS relayed them (A3-N-3);
- `T/IMPLEMENTATION/U3/` at the PR head;
- `T/IMPLEMENTATION/F2A_D1/source_equality.py` at NUM `70aa51b076`.

| Object | Commit |
|---|---|
| PR #1168 head | `3bfcceb4c0`: the package corrected; parent `ed012c7ccf`. GitHub reports head `3bfcceb4c0`, base main `ba500defa4`, OPEN |
| The repair | `ed012c7ccf`, on `98733368f9`: the three deletions |
| ADDENDUM_02's subject | `8a12de28db` (code) and `98733368f9` (package) |
| NUM | `70aa51b076` |

**Placeholders:** as in REVIEW.md. `E` = `_run_records/addendum_03/`. The scratch is `WT/scratch/rv127_u3/a3/`.

## Verdict: **PASS** at `3bfcceb4c0`: 0 BLOCKING, 1 SHOULD-FIX, 3 NOTE

- **A2-B-1 is repaired,** and the PR's code now equals NUM's U3 merge without rename detection.
- **A2-N-1 is fixed.** Run on the same pair, the fixed tool fails the unrepaired commit and passes the repaired one. The old tool passes both.
- **ADDENDUM_02's results carry over to the head unchanged.** These are the byte sample, the T2 check, the merge resolution and the test runs. The only code change is the deletion of three files, and nothing builds from them, reads them or walks over them (§2).
- **A3-S-1 is a package record fix.** It touches no code and needs no re-review of code. I recommend it before merge.

## Findings

| ID | Class | Where | Evidence | Remedy |
|---|---|---|---|---|
| A3-S-1 | SHOULD-FIX (record truthfulness) | `T/IMPLEMENTATION/U3/CHANGE_RECORD.md`, the checks-table row for `source_equality.py` and `check_citations.py` | **What the row says:** "**PASS**: 133 maintained paths, equal in blob and mode … Recorded in `R/I110/pressure_retire_06/`". **Why that is wrong:** that run is the rename-detection run that missed A2-B-1. **What it does not say:** the row neither marks the run as superseded nor cites the `--no-renames` rerun (136 of 136). The header's new equality statement ("from `ed012c7ccf` on") also cites no run. The only trace of the rerun is one line in `T/WORKING_ITEMS_LOG.md` | **Mark the old result:** the 133 PASS was run with rename detection, missed A2-B-1, and is superseded. **Cite the replacement run:** WORKING_ITEMS' own record of it, or `E/source_equality_pos.txt` and `E/source_equality_neg.txt`. It is a package-only commit |
| A3-N-1 | NOTE (stale count) | `T/IMPLEMENTATION/U3/citations.json`, `about` | **The wording:** it still says "the 133 maintained files of 7eae707bb7..source_basis", a count taken with rename detection. **Coverage is unaffected:** `--no-renames` adds only deletions, which add no lines to scan. `check_citations.py` passes at the head: 2 resolved, 0 ambiguous, 0 unresolved (`E/citations.txt`) | Optional: say "133 with rename detection (136 without)" |
| A3-N-2 | NOTE (counts in the relay) | WORKING_ITEMS' list of the remaining mentions | **What WORKING_ITEMS said:** "16 old `validation/evidence/sweeps/SWEEP_202606*.json` summaries". **What I found:** 14 SWEEP summaries name `invented_mechanics_result.json`. Three `REPRO_DEL0904_*/checks/evidence-sweep.json` files name only an old build chunk, `invented_mechanics_result-DftuaeNr.js`. **The rest of the list** is as relayed: SMOKE.md `:4382` and `:9655`, PLAN_COMPLETION_LOG.md (7 lines) and DEMO_FIXTURES.md `:16` (`E/readers_sweep.txt`). Outside agents' records, nothing names the precision pair. The condition holds | None |
| A3-N-3 | NOTE (basis) | RR at NUM `70aa51b076` | RR does not yet record ROOT's ruling on A2-B-1 (its last change is `b828e20800`). I checked the conditions as WORKING_ITEMS relayed them | ROOT records the ruling in RR |

**Carried from ADDENDUM_02:**
- A2-N-2 (optional) was not taken, which WORKING_ITEMS stated.
- A2-N-3 is noted.
- A2-N-4 is unchanged: the PY and TS readers, the full suites and the e2e tests rest on CI at the final head. The change record lists those as pending.

## 1. The repair (`E/repair_tree.txt`)

**Condition 1 (exactly three deletions):** `git diff --no-renames --name-status 98733368f9 ed012c7ccf` gives exactly three `D` lines, both over all paths and outside `P/execution`:
- `invented_mechanics_result.json`;
- `invented_mechanics_result_precision_1_dense.json`;
- `invented_mechanics_result_precision_1_sparse.json`.

The same three lines are the whole code difference from `8a12de28db`. Their blobs at `98733368f9` equal main's (`cf0aa1ce…`, `cb3a6554…`, `6817e6aa…`), and they are absent at `ed012c7ccf`, `3bfcceb4c0` and `70aa51b076`.

**The package commit:** `ed012c7ccf..3bfcceb4c0` changes only three package files: CHANGE_RECORD.md, SHA256SUMS and radius_sweep.txt.

**Equality without rename detection,** outside `P/execution`:

| Pair | Name-status lines |
|---|---|
| `3bfcceb4c0` vs `70aa51b076` | 0 |
| `ed012c7ccf` vs `70aa51b076` | 0 |
| `ed012c7ccf` vs `cfeb5b76fe` | 0 |
| `ed012c7ccf` vs `2fd24aedf1` | 0 |
| `ed012c7ccf` vs `29710d848e` (where WORKING_ITEMS ran the radius sweep) | 0 |

The package at the head equals NUM's.

**Size:** `ba500defa4..ed012c7ccf` changes 136 maintained paths without rename detection (121 M, 9 D, 6 A) and 133 with it. This matches the corrected CHANGE_RECORD.

## 2. Nothing reads the three files (`E/readers_sweep.txt`, `E/walks.txt`)

**Condition 2 (no readers):**
- In `.rs`, `.ts`, `.tsx`, `.js`, `.mjs`, `.py`, `.toml` and `.yml` files outside `P/execution`, nothing names the three basenames.
- The other files that share the stem name `invented_mechanics_result_preview_physics_1_*`, a different, retained file.
- My ADDENDUM_02 byte sample used none of the three files.

**Directory walks:** none walks `fixtures/product_preview/` itself.
- The three `import.meta.glob` calls name its `physics_source/` and `source_blocks/ui/` subfolders.
- The recursive Rust and TS walks keep only source files; the RE walk also skips `fixtures/`.
- The demo generator's source inventory walks the `core/` dependency closure and `schemas/`.
- One walk does reach the three files. `test_results_dispatcher_v0_3.py` collects every committed result document under `fixtures/`, but none of the three contains one: no object anywhere in them has a string `schema_version` together with an object `result_envelope`.

**Consequence:** the builds, the published bytes and the tests at `3bfcceb4c0` are those of `8a12de28db`. ADDENDUM_02 §§2–5 apply to the head unchanged.

## 3. A2-N-1 and the package claims

**The tool:** `names()` in `source_equality.py` now calls `git diff --no-renames --name-only`, with a dated comment. That is the only change to the tool. I ran the NUM `70aa51b076` copy and the `cfeb5b76fe` copy, matched by sha256 to their blobs (`E/tools.txt`), with `--int 70aa51b076 --main ba500defa4 --package T/IMPLEMENTATION/U3`:

| Tool | `--pr 98733368f9` (unrepaired) | `--pr 3bfcceb4c0` (head) |
|---|---|---|
| fixed (`--no-renames`) | **FAIL**, checks 1, 2 and 5, exit 1: the three paths are in S but not in the PR. S has 136 paths; 133 are equal | **PASS**, exit 0: 136 of 136 equal; 5 execution files, all in the package, whose SHA256SUMS verify |
| old (rename detection) | PASS, 133 of 133: the blind spot | PASS, 133 of 133 |

Check 3 has nothing to compare here: NUM already contains main `ba500defa4`, so `B` equals main. The three-way merge evidence is ADDENDUM_02 §4, and the code it covers is unchanged.

**Citations:** `check_citations.py` (main's tool, unchanged) at `--base ba500defa4 --head 3bfcceb4c0` with the U3 index passes: 2 resolved, 0 ambiguous, 0 unresolved, 0 verification failures.

**The package's claims:**
- **CHANGE_RECORD's header is true.** It names the PR, its two code commits and the equality "from `ed012c7ccf` on". Its erratum states the cause and the negative control. Its size line gives 136, counted without rename detection.
- **The radius sweep header is true.** NUM `29710d848e`'s maintained tree equals `ed012c7ccf`'s.
- **One row is not updated:** the checks-table row (A3-S-1).
- **The PR body** (at the head and on GitHub) makes no claim about tree equality or size; its "equal" lines are about byte equality.

## 4. Host

- **Git:** reads only, with `GIT_OPTIONAL_LOCKS=0`. `gh pr view` was read only.
- **Cargo:** none run. Nothing new needed a build: the code change is the three deletions, and §2 shows that nothing builds from them.
- **Scratch:** `WT/scratch/rv127_u3/a3/` holds the tool copies, the work directories and the outputs. The archive copies, targets and dumps went with ADDENDUM_02.

## Records (`_run_records/addendum_03/`)

- **`scripts/run_a3.sh`:** regenerates every output below from `WT`.
- **Tree evidence:** `repair_tree.txt`.
- **Mention and walk sweeps:** `readers_sweep.txt` and `walks.txt`.
- **Tool runs:**
  - `source_equality_{pos,neg}.{txt,json}`;
  - `source_equality_{pos,neg}_oldtool.txt`;
  - `citations.txt` and `citations_resolved.md`.
- **Tool hashes:** `tools.txt`.

Sums are in the folder's `SHA256SUMS`. Paths use placeholders only.
