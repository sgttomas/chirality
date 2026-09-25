# QA Report — COV_SCA005_POSTCHANGE_2026-09-25_1344

## Scan coverage

Sections were bound by heading text with no ambiguity: `Objectives` at line
325, `Packages` at line 364, `Deliverables` at line 390 and `Scope Ledger` at
line 528 (`Decision_Log.md` D-1).

The run scanned:

- **Decomposition package:**
  - `SOFTWARE_DECOMP.md`: §2.1–2.3, §3, §4, §5, §7, §9, §10 and Companion
    Inventory
  - the four companion registers
- **Filesystem:**
  - 11 package folders
  - 64 deliverable folders (60 active, 4 retired)
  - 64 `_CONTEXT.md` and 64 `_STATUS.md`
  - 64 `_REFERENCES.md`, provenance revision only
  - 64 `Dependencies.csv`
  - 32 `ScopeOfWork.md`, contract schema line only
  - deliverable-local `artifacts/`
  - the one sibling `MEMORY.md` (`DEL-01-03`), read as non-authoritative
    context; it is consistent with `IN_PROGRESS`
- **Handoff and snapshot surfaces:**
  - the three `_LATEST.md` pointers
  - the complete active SCA-004 snapshot
  - the non-active SCA-005 snapshot
  - the group-2 checkpoint snapshot and `SCA-005_GROUP-2_AUTHORIZED.md`
  - the D-PEC-92 register row
  - the 2026-08-03 PROJECT_SETUP metadata-alignment handoff
    (`93a3337b…b58b1f`) and the 2026-08-09 currency-repair closeout handoff
    (`8a9957b4…0d24f`)

The census, supplementary checks and emitters ran as scratch Python scripts in
the session scratchpad, outside the repository. They wrote nothing into the
repository except this snapshot's files.

| Script (scratchpad `cov_postchange/`) | SHA-256 |
|---|---|
| `census.py` | `adf18d9318558cccc94f79a6afd0e2fe9e4f791bc40a80297637181767a83425` |
| `supp.py` (SSOW tables, vocabulary, OIs, inventory) | `cb6ad2fac1a7ae451025ee59909f2357efd00b3b25f6275d824fe570cee4c674` |
| `deps.py` (rows touching retired DELs) | `9fa18cd8c7a0f044d0c88603d3b87595a0f9c2d15a8f877b02cde08014dd6233` |
| `census.json` (output; identical under `PYTHONHASHSEED=0` and `=1`) | `1049b21e66ca2c2c86b5acf4fd9907c670f32c36fb33318e8750aaefe73c9732` |

## Commands

Commands ran with cwd = REPO_ROOT, the worktree
`/Users/ryan/ai-env/projects/chirality/.claude/worktrees/agent-a05f45a57936b1abf`,
using `/Library/Frameworks/Python.framework/Versions/3.13/bin/python3` (Python
3.13.7). `PYTHONDONTWRITEBYTECODE=1` was set for every repository script.

| # | Command | Exit | Key output |
|---|---|---|---|
| 1 | `shasum -a 256` over the instruction, method and input files | 0 | All nine brief-supplied hashes match (`Brief.md`) |
| 2 | `python3 projects/pec/execution/_Scripts/pec_reliance_hold.py --register projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv --target projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA005_POSTCHANGE_2026-09-25_1344/ --operation dispatch-for-production` (script `b1712e4b…cd0e`), run before any write | 0 | `{"operation": "dispatch-for-production", "status": "ALLOW"}`. The register (`f877d931…1cbc`) is header-only |
| 3 | `python3 tools/validation/validate_decomposition_registers.py projects/pec/execution --strict` (script `590d9aa3…8818`) | 1 | Families SCH, EVQ, XRG, DRB. 64 registers, 255 dependency rows (ANCHOR 136, EXECUTION 119), 66 deliverables declared. `ERROR findings: 0`. `WARNING findings: 2`, both DRB-008 (DEL-02-08, DEL-02-09). Exit 1 is strict mode failing on warnings |
| 4 | `python3 tools/coordination/analyze_dep_closure.py projects/pec/execution --output-dir <scratchpad>/depclosure` (script `fe546d0f…8ccd`) | 0 | `run_status COMPLETE`, `subject_status PASS`. 64 files and 255 rows. 119 graph edges over 64 nodes. 0 SCCs, 0 bidirectional pairs, 0 orphans, 0 outside scope. Isolated: DEL-00-03, DEL-01-05. One hub, DEL-03-01 (in 13, out 11, total 24; the tool marks `hubs WARNING`). Schema valid 64/64; `IMPLEMENTS_NODE` present 64/64. `closure_summary.json` `9fb8cc44…c1a7` |
| 5 | `python3 <scratchpad>/cov_postchange/census.py <REPO_ROOT>`, run twice (before and after the caller's commit) | 0 | Identical content. The only byte difference came from set ordering in one key, which is now sorted. The second run confirmed determinism under two hash seeds |
| 6 | `python3 <scratchpad>/cov_postchange/supp.py <decomposition dir>` | 0 | §2.1/2.2/2.3 = 70 IN / 18 OUT / 8 TBD. All 96 IDs equal the ledger's IDs and status. 26 vocabulary terms. 13 OI rows, of which 3 are resolved. No package-prefix mismatch. No duplicate IDs. The main-document inventory lists the same 6 files as `Companion_Inventory.csv` |
| 7 | `python3 <scratchpad>/cov_postchange/deps.py projects/pec/execution` | 0 | The retired registers own 18 ACTIVE rows (10 EXECUTION, 8 ANCHOR). The only inbound row to a retired DEL is `DEP-09-05-005` (DEL-09-05 → DEL-06-04, EXECUTION, ACTIVE) |
| 8 | Python check of the 26 A2/A3 planned postimage hashes parsed from `Propagation_Plan.md` against live bytes | 0 | 26/26 MATCH (22 `_CONTEXT.md`, 4 `_STATUS.md`) |
| 9 | `diff CP2_CANDIDATE/_Decomposition/SOFTWARE_DECOMP.md _Decomposition/SOFTWARE_DECOMP.md` | 1 | Only lines 5 (`status`) and 8 (`accepted`) differ |
| 10 | `git show 2b0572fe0:…/SOFTWARE_DECOMP.md \| shasum -a 256` and the same for `DEL-01-06/_CONTEXT.md` | 0 | `7cca5cdb…5c81` and `24f357cc…94b2`. The revision-1.4 basis cited by the pointers and SCA-004 is exactly recoverable |
| 11 | `git status --short`; `git log --oneline -5`; `git show --stat 5d2770350 7e8374ae2` | 0 | See the note on concurrent state below |
| 12 | `git diff --quiet HEAD --` over every `Dependencies.csv`, `_REFERENCES.md`, `ScopeOfWork.md` and `_DEPENDENCIES.md`, and over `_ScopeChange/SCA-005_2026-09-23_2139` | 0 / 0 | No change against HEAD |
| 13 | `python3 <scratchpad>/cov_postchange/emit.py …` and `delta.py …` | 0 | Wrote the issue log, matrix and `coverage_summary.json`, and computed the per-finding delta |

**Concurrent state.** At the first scan the Lane A1–A3 writes (33 paths) were
uncommitted in this worktree. The caller committed them during the run as
`5d2770350` (13:47:38 -0600), then `7e8374ae2` (13:48:43 -0600). The second
commit adds only
`_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/returns/B3_SCA005_CHECKPOINT3.md`.
This run read that return as context only. It does not audit it, and it
states that this audit's result had not yet been received. After the commits
the working tree was clean, and the census over the committed state matched.
This run made no git write.

A scratch folder, `<scratchpad>/depclosure/` (dated 2026-09-23), already
existed in the session scratchpad. Command 4 overwrote its files. It is scratch
state outside the repository.

## Parse and comparison results

- **Registers.**
  - Ledger: 96 rows, 70 IN / 18 OUT / 8 TBD.
  - Deliverables: 66 rows, 62 active and 4 retired. Retirement is identified
    by the `[RETIRED — SCA-005]` description prefix, blank
    `CoversScopeItems`/`SupportsObjectives`, the §5 `— [RETIRED — SCA-005]`
    Covers cell, and the `ContextBudgetQA.csv` RecommendedAction marker.
  - `ContextBudgetQA.csv`: 66 rows. Envelope and package match the
    deliverable register 66/66.
- **§5 compact view** matches `Deliverables.csv` for 66/66 rows (name, type,
  envelope, phase, covers).
- **Ledger integrity.**
  - All 70 IN rows resolve to declared packages and to declared, non-retired
    deliverables with matching package prefixes.
  - No IN row lacks a deliverable or an objective. No OUT/TBD row carries a
    mapping.
  - `CoversScopeItems` and ledger `DeliverableIDs` are reciprocal for 66/66.
  - The union rule (a deliverable's `SupportsObjectives` equals the union of
    its covered IN rows' objectives) holds for all 62 active rows.
- **Per-package IN counts** equal §4 "Assigned (count)" for 11/11:
  3/8/9/7/6/3/6/3/6/7/12.
- **Envelopes.** Active: S 28 / M 32 / L 2 / XL 0, which equals §5, §7 and
  C3. All rows: S 29 / M 35 / L 2.
- **Objectives** resolved from the ledger `ObjectiveIDs` column: six. For each
  objective, the ledger IN-item set equals the §3 "Mapped Scope Items" set,
  with ranges and instruments expanded. The `SupportsObjectives` set equals
  both §3 "MappedDeliverables" and the ledger-reached deliverables.
  - Counts, as IN items / supporting deliverables: OBJ-001 27/25, OBJ-002
    14/14, OBJ-003 16/14, OBJ-004 13/11, OBJ-005 9/7, OBJ-006 9/9.
  - IN rows without an objective: 0. Active deliverables without an
    objective: 0.
- **§7 metrics** equal the registers: 96 (70/18/8); 11; 66 rows (62/4); 6;
  0/0/0/0; S28/M32/L2/XL0; issues 10 open / 3 resolved; 66/66 single-package
  membership.
- **Companion inventory.** The main-document section and
  `Companion_Inventory.csv` list the same six files. The CSV row descriptions
  ("96-row", "66-row") agree with the registers.
- **Filesystem.** 11/11 package folders, each containing only `1_Working/`.
  64 `DEL-*` folders, all declared. There is no reverse-only or non-`DEL`
  folder. DEL-02-08 and DEL-02-09 are absent.
- **Contexts.** 64/64 match their register rows on DeliverableID, name,
  package, type, `ContextEnvelope`, `PhaseHint`, covered items (ID set),
  supported objectives (ID set), responsible party, description, anticipated
  artifacts and envelope notes.
- **Context provenance.**
  - The 22 A2 mirrors end at "revision 1.5 (`current_basis`, SCA-005
    successor)": DEL-00-02, DEL-01-01, DEL-01-06, DEL-02-03, DEL-02-04,
    DEL-02-05, DEL-02-06, DEL-02-07, DEL-03-03, DEL-03-05, DEL-04-01,
    DEL-05-01, DEL-06-01, DEL-06-04, DEL-07-02, DEL-07-03, DEL-07-04,
    DEL-07-05, DEL-08-01, DEL-08-05, DEL-09-05, DEL-10-08.
  - 42 end at revision 1.4: DEL-00-01, DEL-00-03, DEL-01-02, DEL-01-03,
    DEL-01-04, DEL-01-05, DEL-02-01, DEL-02-02, DEL-03-01, DEL-03-02,
    DEL-03-04, DEL-03-06, DEL-04-02, DEL-04-03, DEL-04-04, DEL-04-05,
    DEL-05-02, DEL-06-02, DEL-06-03, DEL-06-05, DEL-06-06, DEL-07-01,
    DEL-08-02, DEL-08-03, DEL-08-04, DEL-09-01, DEL-09-02, DEL-09-03,
    DEL-09-04, DEL-09-06, DEL-09-07, DEL-10-01, DEL-10-02, DEL-10-03,
    DEL-10-04, DEL-10-05, DEL-10-06, DEL-10-07, DEL-10-09, DEL-10-10,
    DEL-10-11, DEL-10-12.
- **Reference packets.** All 64 `_REFERENCES.md` end at revision 1.4.
- **Lifecycle,** each read from the `**Current State:**` line at
  `_STATUS.md:3`: 26 `INITIALIZED`, 28 `OPEN`, 4 `CHECKING` (DEL-00-01,
  DEL-00-03, DEL-08-02, DEL-10-01), 2 `IN_PROGRESS` (DEL-01-03, DEL-01-05) and
  4 `RETIRED`. No unrecognized state.
- **Contracts.** 32 valid `SOW_V1` (4 `CHECKING`, 26 `INITIALIZED`,
  2 `IN_PROGRESS`) and 32 `NONE` (28 `OPEN`, 4 `RETIRED`). No legacy, dual or
  invalid contract.
- **Artifacts.** Three deliverable-local anticipated sets are present:
  DEL-00-01 `artifacts/v2/ADRs.md`, DEL-00-03 `artifacts/v2/SPEC.md`, and
  DEL-10-01 `artifacts/STEP0_COST_BASELINE{,_METHOD}.md`. The other 61
  matched folders have no anticipated set. The absences are 3 `WARNING`
  (DEL-01-03, DEL-01-05, DEL-08-02) and 58 `INFO`.
  `artifact_presence_pct` is 4.5455 (3/66 declared) or 4.6875 (3/64
  folder-matched).
- **Retired folders** are retained with all their files: `Dependencies.csv`,
  `_CONTEXT.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, `_SEMANTIC.md`,
  `_STATUS.md` and `_run_records/`. Live hashes:

  | DEL | `_STATUS.md` | `_CONTEXT.md` |
  |---|---|---|
  | DEL-06-04 | `eeae22fb…724bc` | `a0aee56b…7fc30` |
  | DEL-07-02 | `8eda30e1…93b8a` | `0bb820de…af3f0` |
  | DEL-07-04 | `2aaec8fd…2de5e` | `5ac0787f…81b43` |
  | DEL-07-05 | `19123cf8…83ded` | `1adc79cd…8de12e` |

  The `_STATUS.md` values equal the planned A3 postimages. No sibling memory
  file exists in these folders.
- **Active SCA-004 snapshot.** It is complete: `Brief`, `Impact_Assessment`,
  `Propagation_Plan`, `Amendment_Actions.csv`, `Amendment_Preview`,
  `Pre_Change_Coverage.json`/`Post_Change_Coverage.json`, `Decision_Log`,
  `Handoff_State`, `RUN_SUMMARY`, `Supersession_Map.csv` (header only) and the
  Gate 2–4 records. The following hashes are unchanged since PRECHANGE:

  | File | SHA-256 |
  |---|---|
  | `Handoff_State.md` | `919d40bb…e970` |
  | `RUN_SUMMARY.md` | `db0ca735…75bc` |
  | `Post_Change_Coverage.json` | `0d3ec0a8…d9ec` |
  | `Supersession_Map.csv` | `9b62e987…fcb9` |

  `ReadyForNextPhase` is `NO`.
- **Non-active SCA-005 snapshot.**
  - Present: `Amendment_Actions.csv`, `Amendment_Actions_CP2.csv`,
    `Amendment_Preview.md`, `Brief.md`, `CP2_CANDIDATE/`, `Decision_Log.md`,
    `Handoff_State.md`, `Impact_Assessment.md`, `PRD_V2_3_SUCCESSOR_DIFF.md`,
    `Pre_Change_Coverage.json`, `Propagation_Plan.md`,
    `Supersession_Delta.csv` and `Supersession_Map.csv` (30 lines, 29 rows).
  - Absent: `Post_Change_Coverage.json` and `RUN_SUMMARY.md`.
  - Its Handoff_State claims neither application nor closure. Its latest
    state-field table (checkpoint-2 preparation) says `AuditState` is
    post-change `NOT_RUN`, which is true at this run's start.

## Limits

- `AnticipatedArtifacts` holds descriptive artifact classes, not filenames.
  Check 6 therefore matches conservatively inside the deliverable folder.
  Source-tree bytes under `projects/pec/v2/` are cited in the warnings but
  never counted. Their fitness and acceptance were not judged.
- This run did not audit the content of the `_run_records/` folders, the
  retired folders' `_DEPENDENCIES.md` mirrors, or the SOW text. Their
  currency is as declared in the plan's B3/B4 tables and is UNKNOWN beyond
  byte-unchanged status.
- C1 exact-write containment, C3 successor assertions and C5 snapshot
  completeness are Lane C items owned by the caller. This run checked parts
  of them (the 26 postimage hashes, the C3 counts, and the SCA-005 file
  presence) as audit evidence only. It does not replace those lanes.
- No independent review of this snapshot was performed. The plan's C4 calls
  for a separate review instance, and that is outside this run.
- This derivative audit validates structural coverage and snapshot honesty.
  It does not accept checkpoint 3 or any artifact, change governed state,
  authorize amendment or implementation, or replace decomposition or SCA
  truth. The audit `_LATEST.md` (`0084d218…7432`, naming
  `COV_SCA004_POSTCHANGE_2026-08-03_1442`) was intentionally not updated.
