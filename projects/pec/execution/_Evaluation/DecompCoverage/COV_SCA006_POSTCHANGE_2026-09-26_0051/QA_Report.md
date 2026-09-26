# QA Report — COV_SCA006_POSTCHANGE_2026-09-26_0051

## Scan coverage

Sections bound by heading text with no ambiguity: `Objectives` line 337,
`Packages` line 376, `Deliverables` line 402, `Scope Ledger` line 542
(`Decision_Log.md` D-1).

The run scanned:

- **Decomposition package:** `SOFTWARE_DECOMP.md` front matter, §2.1–2.3, §3,
  §4, §5, §7, §8, §9, §10, §11 DL-21, §12 and Companion Inventory; the four
  companion registers, bound as authoritative (paths and full hashes below).
- **Filesystem:**
  - 11 package folders and 66 deliverable folders (62 active, 4 retired); 2
    declared units without folders
  - 66 `_CONTEXT.md`, 66 `_STATUS.md` (current-state line), 66
    `_REFERENCES.md` (revision and PRD version), 66 `Dependencies.csv` (all
    rows) and 66 `_DEPENDENCIES.md` (EdgeID mentions and the two B3 quotes)
  - 32 `ScopeOfWork.md` (schema line only)
  - deliverable-local `artifacts/`
- **Paired read:** the only sibling memory file is DEL-01-03 `MEMORY.md`, read
  in full as non-authoritative context. It is consistent with DEL-01-03 at
  `IN_PROGRESS` and its v2 bytes outside the folder; no material caveat.
- **Handoff and snapshot surfaces:**
  - all three `_LATEST.md` pointers (read only)
  - the active SCA-005 snapshot (hashes) and the SCA-006 candidate snapshot
  - the SCA-006 group-2 snapshot and amendment 1
  - the `_AUTHORIZED` pointers
  - `_COORDINATION.md` item 14
  - the `D-PEC-95` ruling, register row and run root (listing, handoff, closure evidence)
  - the `D-PEC-96` amend-direction record
  - `v2/config/loops.json` (feed-profile presence only)
  - `docs/SPEC.md` §1 and §12.2

Census, supplementary checks and emitters ran as scratch Python scripts in the
session scratchpad (`cov_sca006/`), outside the repository. They wrote nothing
into the repository except this snapshot's files.

## Commands

cwd is the worktree root
`/Users/ryan/ai-env/projects/chirality/.claude/worktrees/agent-a2942849b8715f72c`
(REPO_ROOT) unless stated. Interpreter:
`/Library/Frameworks/Python.framework/Versions/3.13/bin/python3` (Python
3.13.7). `PYTHONDONTWRITEBYTECODE=1` was set for every Python run. Shell: zsh.
`SP` is the scratch folder `cov_sca006/`, and `SNAP` is this folder.

| # | Command | Exit | Key output |
|---|---|---|---|
| 1 | `git status --short`; `git log --oneline -3` (start) | 0 | Clean; HEAD `39a9768c8` (A4 tranche) on `fb1debf2f` (A1/A2) |
| 2 | `shasum -a 256` over root/PEC `AGENTS.md`, `AGENT_TASK.md`, the three workflow files, the decomposition, four registers and PRD | 0 | Every brief-supplied hash matches |
| 3 | from `projects/pec`: `python3 execution/_Scripts/pec_reliance_hold.py --register execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv --target <T> --operation candidate-validation` for T = `SOFTWARE_DECOMP.md`, the four registers, `execution/_Evaluation/DecompCoverage/COV_SCA006_POSTCHANGE_2026-09-26_0051`, `execution` | 0 ×7 | `{"operation": "candidate-validation", "status": "ALLOW"}` each time; register header-only. Run before any reliance or write |
| 4 | `shasum -a 256` baseline `coverage_summary.json` and SCA-006 `Pre_Change_Coverage.json` | 0 | Both `b7b432a2…128d`: byte-identical |
| 5 | `mkdir …/COV_SCA006_POSTCHANGE_2026-09-26_0051` | 0 | Created; did not exist before (D-3) |
| 6 | cwd SP: `python3 census.py REPO_ROOT > census.json` with `PYTHONHASHSEED=0`, then `=1` to `census2.json`; `cmp` | 0 / 0 / 0 | Identical (`85a4fbc7…b719`) |
| 7 | cwd SP: `python3 mkinventory.py REPO_ROOT census.json > SNAP/inventory.json` | 0 | 68 units (66 live paths + 2 plan-§B1 expected paths) |
| 8 | `python3 tools/evaluation/audit_structure.py --root projects/pec/execution --variant SOFTWARE --output SNAP/structure.json --inventory SNAP/inventory.json` | 0 | `run_status COMPLETE`, `subject_status FAIL`. 68 units: 66 PASS, 2 FAIL (DEL-08-06, DEL-10-13: directory missing). Lifecycle 26/30/4/2/4 + 2 UNKNOWN. Formats SOW_V1 32 (valid), INVALID 36 (34 no-contract `OPEN`/`RETIRED` folders with no issue raised, plus the 2 missing). Tool issues: "partition directory contract is incomplete", "required tool roots are missing" |
| 9 | cwd SP: `python3 deps3.py REPO_ROOT > deps3.json` | 0 | See "Dependency registers" |
| 10 | cwd SP: `python3 anchorcheck.py REPO_ROOT > anchorcheck.out` | 0 | 132 ACTIVE anchor assertions true (62 `PackageID`, 70 `DeliverableIDs include`); 0 false; 0 unrecognized |
| 11 | `python3 tools/validation/validate_decomposition_registers.py projects/pec/execution --strict` | **1** | Families SCH, EVQ, XRG, DRB. 66 registers, 263 rows, 68 deliverables declared; evidence well-formed 263/263. `ERROR findings: 0`, `WARNING findings: 2`, both DRB-008 (DEL-08-06, DEL-10-13). Exit 1 is `--strict` treating warnings as failing, as plan §C2 predicts |
| 12 | `python3 tools/coordination/analyze_dep_closure.py projects/pec/execution --output-dir SP/depclosure` | 0 | `run_status COMPLETE`, `subject_status PASS`; 111 edges, 66 nodes, 0 SCC, 0 bidirectional, 0 orphans, 0 invalid IDs; isolated 6; hub DEL-03-01 (13/12/25); `implements_node_present` 66. `closure_summary.json` `bd73806c…187a` = baseline = D-PEC-95 `checks/closure_post.out` |
| 13 | cwd SP: `python3 supp.py projects/pec/execution/_Decomposition` (absolute path) | 0 | §2.1/2.2/2.3 = 74/18/8, all equal to the ledger; 29 vocabulary rows; 13 OI rows, 3 resolved; no prefix mismatch; no duplicate IDs; inventory lists the same 6 files as the CSV |
| 14 | `git merge-base --is-ancestor abfd0897b HEAD`; `git diff --name-only abfd0897b^1 abfd0897b` (by basename) | 0 / 0 | D-PEC-95 merge is an ancestor; it changed 42 `_CONTEXT.md`, 64 `_REFERENCES.md`, 10 `Dependencies.csv`, 2 `_LATEST.md` (plus run-root and closure evidence) |
| 15 | `git diff --name-only abfd0897b HEAD -- projects/pec/execution projects/pec/docs projects/pec/AGENTS.md` | 0 | Product paths since D-PEC-95: the decomposition, four registers, PRD, `docs/STATUS.md`, `projects/pec/AGENTS.md`, the three A2 contexts, SCA-006 snapshot files. No `_REFERENCES.md`, `Dependencies.csv`, `_STATUS.md` or SOW |
| 16 | `git diff --name-only 995af4f36 HEAD` over `_STATUS.md`, `ScopeOfWork.md`, `artifacts/*` and the SCA-005 snapshot | 0 | Empty |
| 17 | `diff` CP2 candidate vs live `SOFTWARE_DECOMP.md`; `cmp` the four registers and PRD with their CP2 candidates | 1 / 0 ×5 | Decomposition differs only at lines 5, 7–8 (front matter), 574 (§7 revision date) and 700 (DL-21 date); registers and PRD identical |
| 18 | `git show 94e9255b6:<path> \| shasum -a 256` for the decomposition, ScopeLedger, Deliverables, PRD | 0 | `dc2b8479…9660`, `83152a94…d9df`, `b8628fc4…d65a`, `fff27a66…dc32`: the pointer's basis hashes are recoverable |
| 19 | `git diff -U0 abfd0897b HEAD` over the three decomposition CSVs | 0 | Rows changed: SOW-003, SOW-060, SOW-080 modified; SOW-097..100 added; DEL-04-03, DEL-08-01, DEL-08-03 modified; DEL-08-06, DEL-10-13 added (and their ContextBudgetQA rows). SOW-094 and DEL-01-06 unchanged |
| 20 | `git log --oneline -3` (mid-run) | 0 | HEAD moved to `5e0169f5e` (manager: A5 `Supersession_Map.csv`, C3 evidence) during the run |
| 21 | cwd SP: `python3 emit.py REPO_ROOT SNAP 2026-09-26T01:12:45-06:00 "5e0169f5e …"` | 0 | Wrote `Decomp_Coverage_IssueLog.csv` (86 rows), `Decomp_Coverage_Matrix.csv` (68 rows), `coverage_summary.json`; `{"BLOCKER": 0, "WARNING": 3, "INFO": 71, "EXPECTED_CONSEQUENCE": 12}`. Earlier emissions at 01:06 were superseded by this one (only the timestamp and one DecisionRef string differed) |
| 22 | cwd SP: `python3 deltatable.py <baseline IssueLog> SNAP/Decomp_Coverage_IssueLog.csv issue_index.json > delta.md`; `cat prepost_head.md delta.md > SNAP/PrePost_Comparison.md` | 0 / 0 | 68 carried, 2 changed, 3 resolved, 16 new |
| 23 | Output validation: parse the issue log (10 columns × 86), matrix (11 × 68) and JSON; assert `DecisionRef` non-empty exactly for `EXPECTED_CONSEQUENCE`; `CheckNumber` in the allowed set | 0 | All true |
| 24 | Re-hash of every audited input and instruction file after emission; `git diff --stat HEAD` over the 11 package trees; `git status --short --untracked-files=all` | 0 | All hashes equal the values in `Decision_Log.md`; package trees clean; only this folder untracked |

Exploratory read-only commands (`sed`, `grep`, `cat`, `ls`, `awk`, the viewers
`show.py` and `showstruct.py`, inline Python readers of `deps3.json`) are not
listed individually.

## Parse and comparison results

- **Registers.** Ledger 100 rows (74 IN / 18 OUT / 8 TBD). Deliverables 68
  rows: 64 active and 4 retired (`[RETIRED — SCA-005]` prefix, blank coverage
  and objective cells). `ContextBudgetQA.csv` has 68 rows; envelope and package
  match 68/68, and the four retired rows are marked. Active envelopes are
  S 28 / M 34 / L 2 / XL 0; across all rows S 29 / M 37 / L 2.
- **§5 compact view** matches `Deliverables.csv` for 68/68 rows (name, type,
  envelope, phase, covers or retired marker).
- **Ledger integrity.** All 74 IN rows resolve to declared packages and
  declared, non-retired deliverables with matching prefixes; 72 resolve to
  folders (not SOW-099 → DEL-08-06, SOW-100 → DEL-10-13). Non-IN rows carry no
  mapping. Reciprocity 68/68; union rule 64/64. Per-package IN equals §4 for
  11/11 (3/8/9/7/7/3/6/3/8/7/13).
- **Objectives** (from the ledger column): six. For each, the ledger IN set,
  the `SupportsObjectives` set, the ledger-reached deliverables and the §3
  view are equal. IN items / supporters: OBJ-001 31/27, OBJ-002 15/14,
  OBJ-003 16/14, OBJ-004 13/11, OBJ-005 9/7, OBJ-006 9/9. IN rows without an
  objective: 0. Active deliverables without an objective: 0.
- **Filesystem.** 11/11 package folders, each with only `1_Working/`. 66
  `DEL-*` folders, all declared; no reverse-only or non-`DEL` entry.
- **Contexts.** 66/66 match every compared field. Provenance: 63 end at
  revision 1.5 (`current_basis`, SCA-005 successor), and 3 (DEL-04-03,
  DEL-08-01, DEL-08-03) at revision 1.6 (`current_basis`, SCA-006 successor).
  The A2 mirrors hash to their plan postimages.
- **Reference packets.** All 66 name revision 1.5 as accepted
  `current_basis` and `docs/PRD.md` v2.3.
- **Lifecycle** (`**Current State:**` at `_STATUS.md:3`): 26 `INITIALIZED`,
  30 `OPEN`, 4 `CHECKING` (DEL-00-01, DEL-00-03, DEL-08-02, DEL-10-01), 2
  `IN_PROGRESS` (DEL-01-03, DEL-01-05), 4 `RETIRED`; no unrecognized state.
  `audit_structure.py` agrees.
- **Contracts.** 32 `SOW_V1` and 34 `NONE` (30 `OPEN` + 4 `RETIRED`); no
  legacy, dual or invalid contract.
- **Artifacts.** The same three deliverable-local sets (DEL-00-01, DEL-00-03,
  DEL-10-01). 63 absences among existing folders: 3 `WARNING`, 60 `INFO`.
- **Dependency registers** (`deps3.py`):
  - 66 registers, 263 rows: ANCHOR 140 (132 ACTIVE, 8 RETIRED), EXECUTION
    123 (111 ACTIVE, 12 RETIRED).
  - The same 20 RETIRED rows as the baseline. 0 ACTIVE rows in retired
    registers or targeting a retired deliverable.
  - ACTIVE `IMPLEMENTS_NODE` is missing only for the four retired
    deliverables.
  - Quote currency, over 243 ACTIVE rows with quotes: 2 EXECUTION rows not
    verbatim (DEP-09-06-003, DEP-10-03-003, both citing
    `Deliverables.csv` DEL-08-01 Description). The 132 ANCHOR structured
    quotes are checked semantically (132/132 true).
  - The 19 baseline rows all note D-PEC-95, carry `LastSeen` 2026-09-25 and
    are verbatim.
  - DEP-09-06-004 and DEP-10-12-004 are verbatim. The 11 SOW-cited ACTIVE
    rows are verbatim.
  - No row and no `_DEPENDENCIES.md` names DEL-08-06, DEL-10-13 or
    SOW-097..100. Neither broken quote appears in any `_DEPENDENCIES.md`.
- **Mirrors.** The 12 fully retired EdgeIDs have no unstruck row mention; no
  ACTIVE EdgeID is struck; E-P79 ×2, E-P80 ×2, E-P81 ×3, E-P82 ×3.
- **Pointers.** `_Decomposition/_LATEST.md` `626feaaf…12dd` and
  `_ScopeChange/_LATEST.md` `e92b3b16…7d24` equal the plan's checkpoint-3
  precondition hashes. `DecompCoverage/_LATEST.md` `2b43dc3b…1450` names
  `COV_SCA005_POSTSETUP_2026-09-25_1606` (read only; not updated).
- **Active SCA-005 snapshot.** All 14 files plus `CP2_CANDIDATE/` are
  present, byte-identical to the baseline's recorded hashes.
- **SCA-006 candidate snapshot.** Present: `Brief.md`, `Impact_Assessment.md`,
  `Amendment_Preview.md`, `Propagation_Plan.md`, `Amendment_Actions.csv`,
  `Amendment_Actions_CP2.csv`, `Supersession_Delta.csv`, `Supersession_Map.csv`
  (45 data rows), `Pre_Change_Coverage.json`, `Decision_Log.md`,
  `Handoff_State.md`, `PRD_V2_4_SUCCESSOR_DIFF.md`,
  `AGENTS_MD_CANDIDATE_DIFF.md`, `AGENTS_MD_AMENDMENT1_DIFF.md`,
  `CP2_CANDIDATE/`, `CP3_EVIDENCE/`. Absent: `Post_Change_Coverage.json`,
  `RUN_SUMMARY.md` (A5 pending).

## Bound companion registers (full SHA-256)

| Register | SHA-256 |
|---|---|
| `projects/pec/execution/_Decomposition/ScopeLedger.csv` | `1d24a4b86f05dc6fd57028c08e202d33f9f317b148821f9c61246c6e91ee916e` |
| `projects/pec/execution/_Decomposition/Deliverables.csv` | `94ee5d182ae99092324505a72bf2f3b0581f85c0bae6c693214cfef709179805` |
| `projects/pec/execution/_Decomposition/ContextBudgetQA.csv` | `93b0bb075a0e83d3219e6293303c3feaa432e693e7255569d4e522ea42434c7c` |
| `projects/pec/execution/_Decomposition/Companion_Inventory.csv` | `1597ceec7af45f33fe348d46429cc3f82042db5dbd6a083903ae04c7bf908662` |

## Scratch artifacts (session scratchpad `cov_sca006/`, outside the repository)

| File | SHA-256 |
|---|---|
| `census.py` (adapted from baseline `7dd1f65a…1eb6`) | `63c33850979387425a5376a8a9bbd144e1d08c1bfc1a37a414cf96e250f4f283` |
| `census.json` (= `census2.json`) | `85a4fbc7dec2297820f87b95d05ac7eef704236baccdb01d4052527178abb719` |
| `deps3.py` (adapted from baseline `deps2.py` `80f3d369…1ef2`) | `70365549559331200b73a38ffb24c3b2a58ddf2001a8e29f3944ffa70a91bbdc` |
| `deps3.json` | `100e886d840acc6130204e5499d4201edba4917896ab7ef92f3d1db71b2c1c0a` |
| `supp.py` (unchanged from the baseline) / `supp.out` | `cb6ad2fac1a7ae451025ee59909f2357efd00b3b25f6275d824fe570cee4c674` / `138569dc2077cfe03f88f9f3f822a53e8ade586f0db4220809d62be458d12a30` |
| `anchorcheck.py` (unchanged) / `anchorcheck.out` | `bd586053b93f3497480f819d96dd9ceb24ff17308a1528e27d9a7acab4abd82d` / `0adf90265ab5b215cae1edffb51512a545553686f54a11a0dec41335fe696e1c` |
| `mkinventory.py` | `620bf403fca86aa252ce04d5be21b03c8a2385f689781c3492dd058cac8da4ee` |
| `emit.py` | `2d930d2de9a2d3a22b105024ee6f1b291f96c6ac19dadf76f9f2ec43fa787c22` |
| `deltatable.py` | `263b2c9116a418a5852df2069b3cebe3d2540f127696cdf3172cd9d4d072c075` |
| `show.py` / `showstruct.py` (viewers) | `7aa61f7b5079b91193ae88834b4f0b69b60b4dec268e914b04af27dff21a0f7d` / `eabcf5f7356d92f4cbdb4df2cb243926b8e47da1f39fa4bd77d51c9aed307d41` |
| `issue_index.json` | `aaef7ff6e648c4b3a0b6b66ed9378b2567a83bbe77259f9532220975654e8a52` |
| `validator.out` | `e8ccca4e36086364ea7a70eec005e7086b96428b6ab88dd1d5448d82e8b56e5c` |
| `depclosure/closure_summary.json` (= `closure.out`) | `bd73806c98e82455f6abfe66aeeee38623cd24f2e48ed102bb2689934bbc187a` |
| `prepost_head.md` / `delta.md` | `0550e8b87b5cc5cdeb3a0cc0114aca6c6104a47f68d4b06bbc56b4c7799e6bc9` / `29fbe247591a2f55a432ec84c9121f3dbef00f7498fd7e5eca8e52f879c7eb9c` |

## Limits

- `AnticipatedArtifacts` holds descriptive classes, not filenames, so Check 6
  matches conservatively inside the deliverable folder. Source-tree bytes
  under `projects/pec/v2/` are cited in the warnings but never counted; their
  fitness and acceptance were not judged.
- Quote currency was tested by exact substring. It does not judge whether a
  quote still supports its edge semantically.
- SOW text, `_run_records/`, `_SEMANTIC.md`, `docs/STATUS.md`, the tranche
  manifest and notices, and the DEL-00-03 SPEC were not audited. The PRD was
  compared byte-for-byte with its accepted candidate only; its requirement
  count (plan §C3: 49) was not recounted here.
- The mirror check reads EdgeID mentions only.
- Exact slot-rule verification of the pre-acceptance decomposition, and the
  plan's C1 write containment, are the manager's C1/C3. This run observed
  only that the differences sit on the slot lines.
- The live tree moved once during the run (`5e0169f5e`); no audited input
  changed (command 24).
- No independent review of this snapshot was performed. Plan §C4 item 3
  provides a separate review instance.
- This derivative audit validates structural coverage and handoff honesty.
  It accepts nothing, changes no governed state, authorizes nothing, makes no
  lifecycle or readiness claim, and does not replace decomposition or SCA
  truth. `_Evaluation/DecompCoverage/_LATEST.md` was intentionally not
  updated.
