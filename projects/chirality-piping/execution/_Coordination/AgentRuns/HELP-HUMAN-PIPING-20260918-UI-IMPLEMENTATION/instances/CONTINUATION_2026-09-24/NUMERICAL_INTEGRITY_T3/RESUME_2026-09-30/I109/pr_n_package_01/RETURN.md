# I109 round 3: PR-N's evidence package

TASK (Type 2), for WORKING_ITEMS for T3 (Agent 1). Brief: `R/BRIEFS/PR_N_PACKAGE.md` (sha256 `a3ac1dcf…`, verified). B1_COMMON's rules apply, with WORKING_ITEMS in ROOT's place.

## 1. The package: `T/IMPLEMENTATION/PR_N/` in NUM

It is uncommitted; WORKING_ITEMS commits it. The host accepted every file.

| File | sha256 | What |
|---|---|---|
| `CHANGE_RECORD.md` | `3340376b17cf5bd8373fb1690daaaca6cd711519ad98c31459fb9f874907fd08` | §1 what changes and why: the norm, the call sites, the rank screen, the re-pins, and every moved value with its components; §2 scope (the remaining libm calls); §3 evidence; §4 reviews and gates (verdicts pending); §5 the D1 call sites |
| `PR_BODY.md` | `a7ab8888a1cd53892513b12b8d03909f5290270b8ea49f319c9ae6bfbe049432` | the PR description, ending with the Claude Code line |
| `citations.json` | `c89eea2834aaecaa048405f01557de38149bde6185b54ffe13f8328b3161e754` | the index for `check_citations.py` (num_commit NUM `ef8ab78473`, pushed; source_basis `8dd64c1835`; source_base `7eae707bb7`) |
| `SHA256SUMS` | over the three files above | |

**The moved values,** each one ulp and each now the exact correctly rounded 3-norm of its own components (`_run_records/moved_values.json`, reproduced by `tools/moved_values.py` from I109 round 1's regeneration):
- case C `rigid:N0` support force magnitude, `1.6258317075882521e-12` → `…523e-12`. It appears in W-C2 dense, SF-2 (C, B, A) dense and the rf_skew milestone's dense ordinary run. Its components are Fx `-0x1.d5ap-46`, Fy `-0x1.41b68p-40` and Fz `0x1.4561a2ed5be5bp-40`. **These are the re-pinned values.**
- The `load_reference/connected` root force magnitudes (sparse `cold`; sparse and dense `hot`) and the `fallback_uz` sparse anchor moment magnitude. Their committed bytes do not change; the Mac now reproduces the committed (Linux-taken) values.
- m08's intensified row, which is a test-side expectation only.

## 2. The checks

The scratch head is `91b6185e646baa3b95482e06093ad58bb3f3832f`: the code commit `8dd64c1835` plus the four package files at the package path. It was made with `git commit-tree` from a scratch index, so no ref or branch exists and it was never pushed.

**`source_equality.py`** (`T/IMPLEMENTATION/F2A_D1/`, unchanged; `--int ef8ab78473 --main 7eae707bb7 --package <PR_N>`): **PASS, checks 1–5** (`_run_records/source_equality.{out,json}`).
- B = main `7eae707bb7`; |S| = 21.
- Check 1: the PR's non-execution paths equal S.
- Check 2: 21 paths are identical in blob and mode.
- Check 3: no three-way merge was needed.
- Check 4: 4 execution files, all inside the package, and the package sums verify against the PR's blobs.
- Check 5: 21 of 21 rows are equal.

**`check_citations.py`** (`--base 7eae707bb7 --head <scratch head> --index PR_N/citations.json --package PR_N`): **PASS** (`_run_records/check_citations.out`, `citations_resolved.md`).
- Resolved 1, ambiguous 0, unresolved 0.
- 0 verification failures and 0 unused index entries.
- The PR adds a single citation, `R/I109/platform_norm_01`, in `correct_norm_oracle.rs`. It resolves at NUM `ef8ab78473`.

**D1 call sites, recomputed on `8dd64c1835`:** the same as round 2. 16 of 17 sites are in D1; the exception is `evaluate_elastic_section`, which has no caller (`_run_records/d1_norm_sites.json`, `callgraph_8dd64c1835.out.json`).

**Linux dispatch 37820998162** (`7bd84e0526`) was still in progress while this was written; its numerical suite had not finished. The package lists it as pending in CHANGE_RECORD §3 and §4.

## 3. Stops

None. The host accepted every package file and every record.
