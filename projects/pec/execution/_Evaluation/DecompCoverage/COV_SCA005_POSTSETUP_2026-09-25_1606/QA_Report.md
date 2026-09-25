# QA Report — COV_SCA005_POSTSETUP_2026-09-25_1606

## Scan coverage

Sections were bound by heading text with no ambiguity: `Objectives` at line
325, `Packages` at line 364, `Deliverables` at line 390 and `Scope Ledger` at
line 528 (`Decision_Log.md` D-1).

The run scanned:

- **Decomposition package:**
  - `SOFTWARE_DECOMP.md`: front matter, §2.1–2.3, §3, §4, §5, §7, §9, §10 and
    Companion Inventory
  - the four companion registers
- **Filesystem:**
  - 11 package folders
  - 66 deliverable folders (62 active, 4 retired)
  - 66 `_CONTEXT.md`, 66 `_STATUS.md`, 66 `_REFERENCES.md` (provenance
    revision only) and 66 `Dependencies.csv` (all rows)
  - 66 `_DEPENDENCIES.md`, EdgeID mentions only (supplementary mirror check)
  - 32 `ScopeOfWork.md`, contract schema line only
  - deliverable-local `artifacts/`
  - the one sibling `MEMORY.md` (DEL-01-03), presence only
- **Handoff and snapshot surfaces:**
  - the three `_LATEST.md` pointers
  - the active SCA-005 snapshot (all files listed in `Decision_Log.md`)
  - the group-3 checkpoint snapshot
  - the D-PEC-93 proposal, ruling and run root (read only)

The census, supplementary checks and emitters ran as scratch Python scripts in
the session scratchpad (`cov_postsetup/`), outside the repository. Their hashes
are in `Decision_Log.md`. They wrote nothing into the repository except this
snapshot's files.

## Commands

Commands ran with cwd = the worktree root
`/Users/ryan/ai-env/projects/chirality/.claude/worktrees/agent-adb8a84864c6fa862`
(REPO_ROOT), using `/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`
(Python 3.13.7). `PYTHONDONTWRITEBYTECODE=1` was set for every repository
script. `SP` below is the session scratchpad folder `cov_postsetup/`.

| # | Command | Exit | Key output |
|---|---|---|---|
| 1 | `git status --short --untracked-files=all`; `git log --oneline -3` | 0 | HEAD `995af4f36` (D-PEC-93 act) on `04e04da00`. One untracked file, `projects/pec/execution/_Coordination/PROJECT_SETUP_SCA005_A4_B3_2026-09-25/checks/07_diff_check.out`, present before this run (not written by it; not an audited path) |
| 2 | `shasum -a 256` over the workflow, contract, method, snapshot tool, decomposition, D-PEC-93 proposal and ruling, and the prior run's files | 0 | Every brief-supplied hash matches (`Brief.md`, `Decision_Log.md`) |
| 3 | `python3 projects/pec/execution/_Scripts/pec_reliance_hold.py --register projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv --target projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA005_POSTSETUP --operation dispatch-for-production`, and the same with `--target projects/pec/execution`, run before any write | 0 / 0 | `{"operation": "dispatch-for-production", "status": "ALLOW"}` both times. The register is header-only |
| 4 | `bash tools/scaffolding/create_snapshot_folder.sh projects/pec/execution/_Evaluation/DecompCoverage COV SCA005_POSTSETUP` | 0 | Printed `projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA005_POSTSETUP_2026-09-25_1606` |
| 5 | `python3 SP/census.py REPO_ROOT > SP/census.json` with `PYTHONHASHSEED=0`, then `=1` to `SP/census2.json`; `cmp` | 0 / 0 / 0 | Identical output (`046afd1f…2056`) |
| 6 | `python3 tools/validation/validate_decomposition_registers.py projects/pec/execution --strict` | **0** | Families SCH, EVQ, XRG, DRB. 66 registers, 263 dependency rows (ANCHOR 140, EXECUTION 123), 66 deliverables declared. Evidence file populated and resolving 263/263. `ERROR findings: 0`, `WARNING findings: 0` |
| 7 | `python3 tools/coordination/analyze_dep_closure.py projects/pec/execution --output-dir SP/depclosure` | 0 | `run_status COMPLETE`, `subject_status PASS`. 66 files, 263 rows. 111 graph edges over 66 nodes. 0 SCCs, 0 bidirectional pairs, 0 orphans, 0 outside scope, 0 invalid IDs, 0 normalizations. Isolated (6): DEL-00-03, DEL-01-05, DEL-06-04, DEL-07-02, DEL-07-04, DEL-07-05. One hub: DEL-03-01 (in 13, out 12, total 25; threshold 20). Checks: `isolated_units` and `hubs` WARNING, all others PASS. Schema valid 66/66; `IMPLEMENTS_NODE` present 66/66. `closure_summary.json` `bd73806c…187a`, byte-identical to the D-PEC-93 run root's `closure/closure_summary.json` |
| 8 | `python3 SP/supp.py projects/pec/execution/_Decomposition` | 0 | §2.1/2.2/2.3 = 70 IN / 18 OUT / 8 TBD, all equal to the ledger. 26 vocabulary terms. 13 OI rows, 3 resolved. No package-prefix mismatch, no duplicate IDs. The main-document inventory lists the same 6 files as `Companion_Inventory.csv` |
| 9 | `python3 SP/deps2.py REPO_ROOT > SP/deps2.json` | 0 | See "Dependency registers" below |
| 10 | `python3 SP/anchorcheck.py REPO_ROOT` | 0 | 132 ACTIVE ANCHOR assertions true against the registers (62 `PackageID`, 70 `DeliverableIDs include`); 0 false; 0 unrecognized |
| 11 | `python3 SP/posthash.py REPO_ROOT` | 0 | 31 rows parsed from the proposal's option-A table; 31/31 live hashes equal the postimages; aggregate `c4525add…727a` equals the proposal's option-A aggregate |
| 12 | `git diff --stat 04e04da00 HEAD -- projects/pec/execution/_Decomposition projects/pec/docs projects/pec/execution/_ScopeChange projects/pec/execution/_Evaluation` | 0 | Empty: the act touched no decomposition, PRD, scope-change or evaluation path |
| 13 | `git diff -U0 04e04da00 HEAD --` DEL-03-01 and DEL-09-05 `Dependencies.csv` | 0 | Changed rows: `DEP-03-01-007`, `-014` (modified), `-015`, `-016` (added); `DEP-09-05-005` (modified). No row in the quote-currency set was touched |
| 14 | `git diff --name-status 5d2770350 HEAD --` the 11 package trees | 0 | Exactly the 31 D-PEC-93 product paths (12 added, 19 modified); no other deliverable file changed since the prior audited commit |
| 15 | `python3 SP/emit.py SP/census.json SP/deps2.json SP/depclosure/closure_summary.json <this folder> REPO_ROOT 2026-09-25T16:13:14-06:00` | 0 | Wrote `Decomp_Coverage_IssueLog.csv` (73 rows), `Decomp_Coverage_Matrix.csv` (66 rows) and `coverage_summary.json`; `{"BLOCKER": 0, "WARNING": 3, "INFO": 70}` |
| 16 | `python3 SP/mapcheck.py SP/issue_index.json <prior IssueLog> <this IssueLog>` | 0 | 68 prior findings mapped to new IDs with identical check, severity and entity (COV-078's entity label widened to "64 of 66"); 14 prior findings unmapped (resolved); 5 new rows |
| 17 | `python3 SP/deltatable.py SP/issue_index.json <prior IssueLog> <this IssueLog> > SP/delta.md`; `cat SP/prepost_head.md SP/delta.md > <this folder>/PrePost_Comparison.md` | 0 / 0 | 87-row per-finding delta table (82 prior rows + 5 new) |

Exploratory read-only commands (`sed`, `grep`, `cat`, `ls`, `SP/anchorq.py`) are
not listed individually.

## Parse and comparison results

- **Registers.**
  - Ledger: 96 rows, 70 IN / 18 OUT / 8 TBD.
  - Deliverables: 66 rows, 62 active and 4 retired (`[RETIRED — SCA-005]`
    prefix, blank coverage and objective cells).
  - `ContextBudgetQA.csv`: 66 rows; envelope and package match 66/66; the
    four retired rows are marked.
- **§5 compact view** matches `Deliverables.csv` for 66/66 rows.
- **Ledger integrity.** All 70 IN rows resolve to declared packages and to
  declared, non-retired deliverables with matching package prefixes, and now
  all 70 resolve to existing folders (including SOW-095 → DEL-02-08 and
  SOW-096 → DEL-02-09). Reciprocity holds for 66/66 and the union rule for
  62/62. Per-package IN counts equal §4 for 11/11
  (3/8/9/7/6/3/6/3/6/7/12).
- **Objectives** (from the ledger column): six. For each, the ledger IN set,
  `SupportsObjectives` set, ledger-reached deliverables and §3 view are equal.
  IN items / supporters, all folder-backed: OBJ-001 27/25, OBJ-002 14/14,
  OBJ-003 16/14, OBJ-004 13/11, OBJ-005 9/7, OBJ-006 9/9. IN rows without an
  objective: 0. Active deliverables without an objective: 0.
- **Filesystem.** 11/11 package folders, each containing only `1_Working/`.
  66 `DEL-*` folders, all declared; no reverse-only or non-`DEL` folder.
  Folder names for the new rows: `PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser`
  and `…/DEL-02-09_MEMORY_run_index_parser`.
- **Contexts.** 66/66 match their register rows on every compared field
  (DeliverableID, name, package, type, `ContextEnvelope`, `PhaseHint`,
  covered items, objectives, responsible party, description, anticipated
  artifacts, envelope notes). The new files hash to the proposal postimages:
  DEL-02-08 `721a9807…4d20`, DEL-02-09 `2413b5c0…0502`.
- **Context provenance.** 24 end at revision 1.5 (the 22 A2 mirrors plus
  DEL-02-08, DEL-02-09); 42 end at revision 1.4 (the same 42 listed in the
  prior QA report).
- **Reference packets.** 64 end at revision 1.4; 2 (DEL-02-08, DEL-02-09) at
  revision 1.5.
- **Lifecycle** (`**Current State:**` at `_STATUS.md:3`): 26 `INITIALIZED`,
  30 `OPEN`, 4 `CHECKING` (DEL-00-01, DEL-00-03, DEL-08-02, DEL-10-01), 2
  `IN_PROGRESS` (DEL-01-03, DEL-01-05), 4 `RETIRED`. No unrecognized state.
  The two new `_STATUS.md` read `OPEN` (history line `TASK+preparation`) and
  hash `d80800a4…0eef` and `3e14313c…d768`, the proposal postimages.
- **Contracts.** 32 `SOW_V1` and 34 `NONE` (30 `OPEN` + 4 `RETIRED`). No
  legacy, dual or invalid contract.
- **Artifacts.** The same three deliverable-local sets as before (DEL-00-01,
  DEL-00-03, DEL-10-01). 63 absences: 3 `WARNING` (DEL-01-03, DEL-01-05,
  DEL-08-02) and 60 `INFO`.
- **Dependency registers** (`deps2.py`):
  - 66 registers, 263 rows: ANCHOR 140 (132 ACTIVE, 8 RETIRED), EXECUTION 123
    (111 ACTIVE, 12 RETIRED).
  - 20 RETIRED rows, exactly the proposal's set: `DEP-03-01-014`,
    `DEP-06-04-001`..`006`, `DEP-07-02-001`..`004`, `DEP-07-04-001`..`004`,
    `DEP-07-05-001`/`002`/`003`/`005`, `DEP-09-05-005`.
  - 0 ACTIVE rows in the four retired registers; 0 ACTIVE rows targeting a
    retired deliverable.
  - 8 added rows (`DEP-02-08-001`..`003`, `DEP-02-09-001`..`003`,
    `DEP-03-01-015`, `-016`) and 1 refreshed row (`DEP-03-01-007`).
  - ACTIVE `IMPLEMENTS_NODE` missing only for the four retired deliverables
    (D-PEC-93 finding 3).
  - Quote currency: 19 ACTIVE EXECUTION rows not verbatim (COV-072); every
    new or refreshed quote is verbatim.
- **Mirrors (supplementary).** The 12 fully retired EdgeIDs (E-A03, E-A04,
  E-N01, E-N02, E-N09, E-N10, E-P14, E-P25, E-P46, E-P47, E-P48, E-P50) have
  no unstruck table-row or bullet mention in any `_DEPENDENCIES.md`; no ACTIVE
  EdgeID is struck; the new edges are mirrored (E-P79 ×2, E-P80 ×2, E-P81 ×3,
  E-P82 ×3).
- **Pointers.** `_Decomposition/_LATEST.md` names revision 1.5
  `current_basis` with the live hashes; `_ScopeChange/_LATEST.md` names
  exactly one snapshot, SCA-005, which exists; `DecompCoverage/_LATEST.md`
  names `COV_SCA004_POSTCHANGE_2026-08-03_1442` (read only; not updated).
- **Active SCA-005 snapshot.** All 15 C5 items are present (`Brief.md`,
  `Impact_Assessment.md`, `Amendment_Preview.md`, `Propagation_Plan.md`,
  `Amendment_Actions.csv`, `Amendment_Actions_CP2.csv`,
  `Supersession_Delta.csv`, `Supersession_Map.csv`, `Pre_Change_Coverage.json`,
  `Post_Change_Coverage.json`, `Decision_Log.md`, `Handoff_State.md`,
  `RUN_SUMMARY.md`, `PRD_V2_3_SUCCESSOR_DIFF.md`, `CP2_CANDIDATE/`). Every
  hash in its C5 table equals the live bytes except the `RUN_SUMMARY.md`
  (`e3480b78…196a`) and `Decision_Log.md` (`85676c53…4d7b`) rows, which
  record the checkpoint-3 preparation values; the file's checkpoint-3
  amendment paragraph states the live values (`e9a0224e…e518`,
  `09f99fb1…a6e`), and its top hash table carries the live `Decision_Log.md`
  value. Not raised as an issue (`Decision_Log.md` D-16). The snapshot and
  pointers state `ReadyForNextPhase = NO` and `AuditState BLOCKED`; they claim
  no cleaner state than the evidence.
- **D-PEC-93 run root.** It holds `gen_d93.py` (`cfae0052…d6c2`, the bound
  generator), its report and stderr, `checks/`, `closure/` and `probes/`. It
  does not yet hold `MANIFEST.md`, `VALIDATION.md`, `HANDOFF_STATE.md` or a
  verifier verdict; the proposal places those after this re-audit.

## Limits

- `AnticipatedArtifacts` holds descriptive classes, not filenames, so Check 6
  matches conservatively inside the deliverable folder. Source-tree bytes
  under `projects/pec/v2/` are cited in the warnings but never counted, and
  their fitness and acceptance were not judged.
- The mirror check reads EdgeID mentions only; it does not judge mirror prose.
  The byte-exact mirror content is covered by the 31/31 postimage match.
- Quote currency was tested by exact substring. It does not judge whether a
  non-verbatim quote still supports its edge semantically.
- This run did not audit `_run_records/` content, SOW text, or the
  `_Coordination/_COORDINATION.md` basis line that the new `_REFERENCES.md`
  files cite (D-PEC-93 finding 5 reports it still names revision 1.4; outside
  this audit's checks).
- No independent review of this snapshot was performed. The D-PEC-93
  proposal calls for a separate verifier, outside this run.
- This derivative audit validates structural coverage and handoff honesty.
  It accepts nothing, changes no governed state, authorizes nothing, makes no
  lifecycle or readiness claim, and does not replace decomposition or SCA
  truth. `_Evaluation/DecompCoverage/_LATEST.md` was intentionally not
  updated.
