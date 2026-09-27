# QA Report — COV_D101_POSTSETUP_2026-09-26_1651

## Scan coverage

Sections were bound by heading text with no ambiguity: `Objectives` line 337,
`Packages` line 376, `Deliverables` line 402, `Scope Ledger` line 542
(`Decision_Log.md` D-1).

The run scanned:

- **Decomposition package:** `SOFTWARE_DECOMP.md` front matter, §2.1–2.3, §3,
  §4, §5, §7, §9, §10 and the Companion Inventory; the four companion
  registers, bound as authoritative (hashes below).
- **Filesystem:**
  - 11 package folders and 68 deliverable folders (64 active, 4 retired)
  - 68 `_CONTEXT.md` (every field), 68 `_STATUS.md` (current-state line)
  - 68 `_REFERENCES.md` (revision, PRD version, covers bullet)
  - 68 `Dependencies.csv` (all rows) and 68 `_DEPENDENCIES.md` (EdgeID rows and bullets)
  - 34 `ScopeOfWork.md` (schema line only)
  - deliverable-local `artifacts/`
  - the full contents of the two new folders
- **Paired reads:** DEL-01-03 `MEMORY.md` (byte-unchanged since the prior
  run's read) and DEL-01-06 `MEMORY.md` (read in full; header and an empty
  Runs table). Both are non-authoritative context (`Decision_Log.md` D-19).
- **Handoff and snapshot surfaces:**
  - the three `_LATEST.md` pointers (read only)
  - the active SCA-006 snapshot (file set, state fields) and the group-3 decision folder
  - the D-PEC-101 proposal and ruling, and the run root (listing, `closure/`, `VERIFIER_VERDICT_01.md` verdict lines, `checks/COMMANDS.txt`)
  - the register rows D-PEC-95 to D-PEC-101
  - the D-GOV-48 notice
  - `_COORDINATION.md` L220–227
  - `v2/config/loops.json` (feed profiles only)
  - the scope-change contract (snapshot layout and state fields)

Census, supplementary checks and emitters ran as scratch Python scripts in
`/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/d101act/audit/`
(`SP`), outside the repository. Nothing was written into the repository
except this snapshot's files.

## Commands

The working directory is the worktree root
`/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d101-act`
(`REPO_ROOT`) unless stated. Interpreter:
`/Library/Frameworks/Python.framework/Versions/3.13/bin/python3` (Python
3.13.7), with `PYTHONDONTWRITEBYTECODE=1` for every Python run. Shell: zsh,
with the one `bash` invocation the brief names. `SNAP` is this folder.

| # | Command | Exit | Key output |
|---|---|---|---|
| 1 | `shasum -a 256` of the brief; `git status --short`; `git log --oneline -3` (start) | 0 | Brief `d9e3f4e7…4194` matches. HEAD `43b60687b` (brief commit) on `fcc1cd26b`. Dirty: run-root `checks/COMMANDS.txt` (M) and `checks/40_preflight_dispatch_V.out` (??) only |
| 2 | `shasum -a 256` of root/PEC `AGENTS.md`, `AGENT_TASK.md`, the three workflow files, the decomposition, the four registers, the PRD, the D-PEC-101 proposal and ruling, `_ScopeChange/_LATEST.md`, the snapshot tool and the two prior-run files | 0 | Every brief-supplied hash matches |
| 3 | `git diff --name-only 62230fa46 HEAD` (filtered for paths outside the run root) | 0 | Empty: after K4 only run-root files changed |
| 4 | from `projects/pec`: `python3 execution/_Scripts/pec_reliance_hold.py --register execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv --target <T> --operation candidate-validation` for T = the decomposition, the four registers, `execution`, `execution/_Evaluation/DecompCoverage` and the two new folders | 0 ×9 | `{"operation": "candidate-validation", "status": "ALLOW"}` each time; register header-only. Run before any write |
| 5 | `bash tools/scaffolding/create_snapshot_folder.sh projects/pec/execution/_Evaluation/DecompCoverage COV D101_POSTSETUP` | 0 | Printed `projects/pec/execution/_Evaluation/DecompCoverage/COV_D101_POSTSETUP_2026-09-26_1651` (16:51 MDT) |
| 6 | cwd SP: `python3 census.py REPO_ROOT > census.json` with `PYTHONHASHSEED=0`, then `=1` to `census2.json`; `cmp` | 0 / 0 / 0 | Identical (`d920640f…7cf3`) |
| 7 | cwd SP: `python3 mkinventory.py REPO_ROOT census.json > SNAP/inventory.json` | 0 | 68 units, all live paths |
| 8 | `python3 tools/evaluation/audit_structure.py --root projects/pec/execution --variant SOFTWARE --output SNAP/structure.json --inventory SNAP/inventory.json` | 0 | `run_status COMPLETE`, `subject_status FAIL` (workspace issues only). **68 units: 68 PASS, 0 FAIL.** Lifecycle 28 I / 30 O / 4 C / 2 IP / 4 R. Formats `SOW_V1` 34 (valid), `INVALID` 34 (30 `OPEN` + 4 `RETIRED` without a contract; no unit-level issue). Tool issues: "partition directory contract is incomplete", "required tool roots are missing" |
| 9 | cwd SP: `python3 deps4.py REPO_ROOT > deps4.json` | 0 | See "Dependency registers" |
| 10 | cwd SP: `python3 anchorcheck.py REPO_ROOT > anchorcheck.out` | 0 | 138 ACTIVE anchor assertions true (64 `PackageID`, 74 `DeliverableIDs include`); 0 false; 0 unrecognized |
| 11 | `python3 tools/validation/validate_decomposition_registers.py projects/pec/execution --strict` (> SP/validator.out); the same with `--json SP/validator.json` | **1** / 1 | 68 registers, 285 rows, 68 deliverables declared. `ERROR findings: 0`, `WARNING findings: 26`, all XRG-013 (OUT/TBD without PackageID). **0 DRB-008.** Exit 1 is `--strict` treating warnings as failing |
| 12 | `python3 tools/coordination/analyze_dep_closure.py projects/pec/execution --output-dir SP/depclosure` (> SP/closure.out) | 0 | `run_status COMPLETE`, `subject_status PASS`; 127 edges, 68 nodes, 0 SCC, 0 bidirectional, 0 orphans, 0 declared disagreements, `declared_only_rows` 127, `declared_unread_count` 136, isolated 6 (DEL-00-03, DEL-01-05, DEL-06-04, DEL-07-02, DEL-07-04, DEL-07-05), hub DEL-03-01 (13/12/25), `implements_node_present` 68. `closure_summary.json` `7ed1553a…6fdd` equals the run root's `closure/closure_summary.json` |
| 13 | cwd SP: `python3 supp.py REPO_ROOT/projects/pec/execution/_Decomposition` | 0 | §2.1/2.2/2.3 = 74/18/8, all equal to the ledger; 29 vocabulary rows; 13 OI rows, 3 resolved; no prefix mismatch; no duplicate IDs; inventory lists the same 6 files as the CSV. Output byte-identical to the prior run's `supp.out` |
| 14 | cwd SP: `python3 postcheck.py REPO_ROOT <D-PEC-101 proposal>` | 0 | **161 rows (K4 129, K1 MODIFY 20, CREATE 12): 161 equal the tabled postimage (add-on C column where given); 0 mismatch** |
| 15 | cwd SP: `python3 refcheck.py REPO_ROOT > refcheck.json` | 0 | 64/64 active covers bullets equal the register (4 retired in add-on-R form); 68 references with `(revision 1.6, accepted current_basis; SCA-006 successor)` and PRD v2.4; 0 with revision 1.5 or v2.3; 68/68 context provenance tails at revision 1.6 SCA-006 |
| 16 | `git diff --name-status $(git merge-base HEAD origin/main) HEAD` (merge base `f392294b5`), excluding the run root | 0 | 12 A (the two new folders) + 1 A (K14A brief copy) + M 63 `_CONTEXT.md`, 66 `_REFERENCES.md`, 16 `_DEPENDENCIES.md`, 4 `Dependencies.csv`: exactly the granted 161 product paths |
| 17 | `git diff --name-status 5e0169f5e HEAD` over the package trees; `git log` over `_STATUS.md` and `ScopeOfWork.md` | 0 | Since the prior run: 57 `_STATUS.md` (D-PEC-99 `5066f895c`, Remaining sections), 2 `_STATUS.md` + 2 `ScopeOfWork.md` (D-PEC-98), DEL-01-06 `MEMORY.md` and `_run_records/` (D-PEC-96), and the D-PEC-101 paths. Lifecycle lines changed only for DEL-02-08/09 (OPEN → INITIALIZED) and the two new OPEN files |
| 18 | `git log` / historical `git show` of `workflows/scope-change/resources/contract.md` with `grep -c AdjustedAuditState` | 0 | Editions `f023e5e2`, `4453a719` (SCA-006's bound edition) and `0bd3533d` lack the field; `d9cdd650` (`0d7d5da61`) and later carry it |
| 19 | `git fetch -q origin` | 0 | **Side effect disclosed:** `refs/remotes/origin/main` fast-forwarded from `bdae9d66b` to `efe938506`; no local branch, index or working-tree change. `git diff --name-only d36c1a55f origin/main` over `projects/pec`, the audit tools and the method touches only `_Coordination/` records (D-PEC-100 ruling and register row, PR #971 reviews, the HELP_HUMAN graph, a D-GOV-50 notice) and `docs/STATUS.md`; no audited input |
| 20 | cwd SP: `python3 emit2.py REPO_ROOT SNAP 2026-09-26T17:02:24-06:00 "43b60687b… (…)"` | 0 | Wrote `Decomp_Coverage_IssueLog.csv` (78 rows), `Decomp_Coverage_Matrix.csv` (68 rows) and `coverage_summary.json`; `{"BLOCKER": 0, "WARNING": 3, "INFO": 73, "EXPECTED_CONSEQUENCE": 2}`. Two earlier emissions in the same minute were superseded; they differed only in the attribution labels of COV-001/002, COV-006 (DEL-01-03 text restored to the prior wording), COV-009, COV-017/018 and the `prior_dispositions` map |
| 21 | cwd SP: `python3 deltatable2.py <prior IssueLog> SNAP/Decomp_Coverage_IssueLog.csv issue_index.json > delta.md`; `cat prepost_head.md delta.md > SNAP/PrePost_Comparison.md` | 0 / 0 | 64 carried, 8 changed, 14 resolved, 6 new |
| 22 | Output validation: parse the issue log (10 columns × 78; sequential IDs), matrix (11 × 68) and JSON. Assert `DecisionRef` is non-empty exactly for `EXPECTED_CONSEQUENCE`, `CheckNumber` is in the allowed set, every BLOCKER/WARNING/EC row has both references, the counts equal the JSON, and there are 12 check verdicts | 0 | All true |
| 23 | `grep` of `VERIFIER_VERDICT_01.md` for its verdict lines | 0 | "PASS WITH NOTES"; "K1 passes: YES" |
| 24 | Re-hash every audited input and instruction file after emission; `git status --short --untracked-files=all` | 0 | All hashes equal those in `Decision_Log.md`. Working tree: the two pre-existing run-root entries and this folder only |

Exploratory read-only commands (`sed`, `grep`, `cat`, `ls`, inline Python
readers of the JSON outputs) are not listed individually.

## Parse and comparison results

- **Registers.** Ledger: 100 rows (74 IN / 18 OUT / 8 TBD). Deliverables: 68
  rows, 64 active and 4 retired. `ContextBudgetQA.csv`: 68 rows; envelope and
  package match 68/68. Active envelopes S 28 / M 34 / L 2 / XL 0.
- **§5 compact view** matches `Deliverables.csv` for 68/68 rows. **§7
  telemetry** equals the registers on every metric (counts, envelopes, open
  and resolved issues, single-package membership).
- **Ledger integrity.** All 74 IN rows resolve to declared packages and to
  declared, non-retired, folder-backed deliverables with matching prefixes.
  Non-IN rows carry no mapping. Reciprocity 68/68; union rule 64/64.
  Per-package IN equals §4 for 11/11.
- **Objectives** (ledger column): six. Ledger IN set, `SupportsObjectives`
  set, ledger-reached deliverables and §3 view are equal for each. IN items /
  supporters: OBJ-001 31/27, OBJ-002 15/14, OBJ-003 16/14, OBJ-004 13/11,
  OBJ-005 9/7, OBJ-006 9/9. Every supporter is folder-backed.
- **Filesystem.** 11/11 package folders, each with only `1_Working/`. 68
  `DEL-*` folders, all declared; no reverse-only or non-`DEL` entry.
- **Contexts.** 68/68 match every compared field. Provenance tails: 68 at
  revision 1.6 (`current_basis`, SCA-006 successor).
- **Reference packets.** 68 name revision 1.6 `current_basis` and PRD v2.4;
  every active covers bullet equals its register cell.
- **Lifecycle** (`**Current State:**` at `_STATUS.md:3`): 28 `INITIALIZED`,
  30 `OPEN`, 4 `CHECKING` (DEL-00-01, DEL-00-03, DEL-08-02, DEL-10-01), 2
  `IN_PROGRESS` (DEL-01-03, DEL-01-05), 4 `RETIRED`. `audit_structure.py`
  agrees.
- **Contracts.** 34 `SOW_V1` and 34 `NONE` (30 `OPEN` + 4 `RETIRED`).
- **Artifacts.** The same three deliverable-local sets (DEL-00-01,
  DEL-00-03, DEL-10-01). 65 absences: 3 WARNING, 62 INFO.
- **Dependency registers** (`deps4.py`):
  - 68 registers, 285 rows: ANCHOR 146 (138 ACTIVE, 8 RETIRED), EXECUTION
    139 (127 ACTIVE, 12 RETIRED).
  - The same 20 RETIRED rows. 0 ACTIVE rows in retired registers or
    targeting a retired deliverable. ACTIVE `IMPLEMENTS_NODE` is missing
    only for the four retired deliverables.
  - Uniqueness: no duplicate `DependencyID`, ACTIVE `EdgeID` or ACTIVE
    source–target pair.
  - 24 rows note D-PEC-101: the 22 added rows plus DEP-09-06-003 and
    DEP-10-03-003.
  - Quote currency: 127/127 ACTIVE EXECUTION quotes verbatim; the 19
    D-PEC-95 rows and 11 SOW-cited rows still verbatim.
  - Trace coverage: 74/74 IN items traced by an ACTIVE
    `TRACES_TO_REQUIREMENT` row in each deliverable they name; no trace
    anchor points outside the ledger mapping.
  - Mirror invariant: 127/127 ACTIVE EXECUTION edges have exactly one
    `| … | E |` row in the source `_DEPENDENCIES.md` and one `[E]` bullet in
    the target's. E-P84..E-P99 are mentioned twice each; E-P83 is unused. The
    12 fully retired EdgeIDs have no unstruck mention; no ACTIVE EdgeID is
    struck.
- **Pointers.** `_Decomposition/_LATEST.md` names revision 1.6 with basis
  hashes equal to the live bytes. `_ScopeChange/_LATEST.md` names SCA-006,
  `CLOSED_FOR_SCOPE_CHANGE_ONLY`. `DecompCoverage/_LATEST.md` names
  `COV_SCA006_POSTCHANGE_2026-09-26_0051` (read only; not updated).
- **Active SCA-006 snapshot.** Present: `Brief.md`, `Impact_Assessment.md`,
  `Amendment_Preview.md`, `Propagation_Plan.md`, `Amendment_Actions.csv`,
  `Amendment_Actions_CP2.csv`, `Pre_Change_Coverage.json`,
  `Post_Change_Coverage.json` (= prior run summary), `Decision_Log.md`,
  `Handoff_State.md`, `RUN_SUMMARY.md`, `Supersession_Delta.csv`,
  `Supersession_Map.csv`, `PRD_V2_4_SUCCESSOR_DIFF.md`, the two AGENTS diffs,
  `CP2_CANDIDATE/`, `CP3_EVIDENCE/`. Checkpoint folders for groups 1, 2,
  2-amendment-1 and 3 exist.

## Bound companion registers (full SHA-256)

| Register | SHA-256 |
|---|---|
| `projects/pec/execution/_Decomposition/ScopeLedger.csv` | `1d24a4b86f05dc6fd57028c08e202d33f9f317b148821f9c61246c6e91ee916e` |
| `projects/pec/execution/_Decomposition/Deliverables.csv` | `94ee5d182ae99092324505a72bf2f3b0581f85c0bae6c693214cfef709179805` |
| `projects/pec/execution/_Decomposition/ContextBudgetQA.csv` | `93b0bb075a0e83d3219e6293303c3feaa432e693e7255569d4e522ea42434c7c` |
| `projects/pec/execution/_Decomposition/Companion_Inventory.csv` | `1597ceec7af45f33fe348d46429cc3f82042db5dbd6a083903ae04c7bf908662` |

## Scratch artifacts (SP, outside the repository)

| File | SHA-256 |
|---|---|
| `census.py` (unchanged from the prior run) | `63c33850979387425a5376a8a9bbd144e1d08c1bfc1a37a414cf96e250f4f283` |
| `census.json` (= `census2.json`) | `d920640f75cbff39dbc2e97a8694fd097cc84368c69042ec40707696afbe7cf3` |
| `mkinventory.py` (docstring only changed) | `e7d8881057b67a9b6a0053758a33a995b00ad36b6b2f4802a9c0bfa9c9c44155` |
| `deps4.py` / `deps4.json` | `f3f43acb6f3074853bf6377d5a24aa24058b329061d1ac73b22687818eff16e0` / `98e3db262c18600bf85b335263cd20b0ab5c4ba8ecf0aa175d8e1c48367405e3` |
| `supp.py` (unchanged) / `supp.out` | `cb6ad2fac1a7ae451025ee59909f2357efd00b3b25f6275d824fe570cee4c674` / `138569dc2077cfe03f88f9f3f822a53e8ade586f0db4220809d62be458d12a30` |
| `anchorcheck.py` (unchanged) / `anchorcheck.out` | `bd586053b93f3497480f819d96dd9ceb24ff17308a1528e27d9a7acab4abd82d` / `bc5d02dd6d8fa4a1bbab89dc16b8546da602c06eae2d5793d66b607cf3548dbb` |
| `refcheck.py` / `refcheck.json` | `4c00f32a9129abb71de364b3d04f6c6fad0ce0789c1e8778464b67fdac220406` / `da7c3ee01d646c4ea9ecccee5c6c2dc6c6df3b7d5fcb9ba70fde8523a298a31f` |
| `postcheck.py` / `postcheck.out` | `8dad7cc92bcbe4459ed1d3eca0bcd77b6ca8325570a127d1a4107bdd0be01371` / `a5cf08a70f9026e73dbbbdf5ae3c2fc5135f583dd89ad72c825cbffcc946adb4` |
| `emit2.py` | `9d3ed8b3f8e309a7f284664e92e85f00548fec3d26f5d1264f2b45372abc2363` |
| `deltatable2.py` | `3859780f96d7a3529c22bc3f22c2b3db833d25cdeb38a6aebf1a0f9fa5ba1dde` |
| `issue_index.json` | `51901dfbe6127ccc89afd1208f727c97a4c525390df6320330deb8f6922c0b68` |
| `validator.out` / `validator.json` | `b44e34df0e6bfa9cbf1676dd3617df8801831109b1409562055e0d317b2d5a08` / `65fff023086a115f4596a7215eb6ac21d6c104131d1fbcf0165c0e1de4eb06f9` |
| `depclosure/closure_summary.json` (= `closure.out`) | `7ed1553aa1cb2314ac2df1d9bde45c53e2b64d3e8a46a46e1dea3cfedbec6fdd` |
| `prepost_head.md` / `delta.md` | `f6d95baabde5082c97600f79ae418ee60a759d47671d924ee34d803f22c0d000` / `fba58318956c8814f069192de92f9a270a8df0457a8d4074606bc225a787c97c` |

## Limits

- `AnticipatedArtifacts` holds descriptive classes, not filenames, so Check 6
  matches conservatively inside the deliverable folder. Source-tree bytes
  under `projects/pec/v2/` are cited but never counted; their fitness and
  acceptance were not judged.
- Quote currency was tested by exact substring. This run did not re-judge
  the semantic warrant of each new edge. That is the independent verifier's
  item 4, which it reports passed.
- SOW text, `_run_records/`, `_SEMANTIC.md`, `docs/STATUS.md` and the PRD
  body were not audited. The PRD and the decomposition were compared by hash
  only.
- The mirror check reads EdgeID rows and bullets only.
- The run did not reproduce the generators; the verifier did that. It
  compared the live bytes with the proposal's postimage tables instead.
- The audited tree is an unpublished branch (`claude/pec-d101-act`). Nothing
  here is observed on `origin/main`.
- Command 19 moved a remote-tracking ref (disclosed above). No other
  repository state was changed outside this folder.
- No independent review of this snapshot was performed.
- This derivative audit validates structural coverage and handoff honesty.
  It accepts nothing, changes no governed state, authorizes nothing, makes no
  lifecycle or readiness claim, and does not replace decomposition or SCA
  truth. `_Evaluation/DecompCoverage/_LATEST.md` was intentionally not
  updated.
