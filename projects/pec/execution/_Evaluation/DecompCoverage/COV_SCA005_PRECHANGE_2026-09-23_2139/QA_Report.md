# QA Report — COV_SCA005_PRECHANGE_2026-09-23

## Scan coverage

Heading-text binding resolved `Packages` (line 351), `Deliverables` (line
377), `Scope Ledger` (line 511), and `Objectives` (line 312) with no
ambiguity. The run scanned:

- `SOFTWARE_DECOMP.md` and the four companion registers
- 11 package folders and 64 exact deliverable folders
- 64 `_CONTEXT.md` and 64 `_STATUS.md` files
- the one sibling `MEMORY.md` (`DEL-01-03`), read as non-authoritative context
- 32 `ScopeOfWork.md` contracts
- the deliverable-local artifact locations
- the three decomposition, scope-change and audit `_LATEST.md` pointers
- the complete active SCA-004 snapshot, the empty SCA-005 candidate folder, and
  the D-PEC-86 intake record
- the PROJECT_SETUP SCA-004 metadata-alignment handoff (SHA-256
  `93a3337b3c1f4ebee5ccee48a191e8a67ea4b080dedf88a82b6bcc7af6b58b1f`)

The deterministic census ran as a scratch Python script outside the
repository. It wrote nothing into the repository except this snapshot's files.

The working tree was at basis commit
`d61981ee2b9e36c82c6cdd28d4f3c12d3d32a69b`. `git diff --quiet d61981ee2 --
projects/pec/execution/_Decomposition projects/pec/execution/_ScopeChange
'projects/pec/execution/PKG-*'` exited 0, so the tracked audited bytes equal
the basis commit. The untracked paths observed were the D-PEC-86 record, the
`_REGISTER.md` row (uncommitted), `SCA-005_PREP_2026-09-23/`, the AgentRuns
record, the notice triage, the three `REMAINING_EVIDENCE_DEL-01-03-REM-00{1,2,3}/`
folders, and the empty `_ScopeChange/SCA-005_2026-09-23_2139/`. These are
external in-flight state. They were read or observed only, and they are not
audited as accepted truth.

## Commands

| # | Command (cwd = REPO_ROOT; interpreter `/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`, Python 3.13.7) | Exit | Key output |
|---|---|---|---|
| 1 | `PYTHONDONTWRITEBYTECODE=1 python3 projects/pec/execution/_Scripts/pec_reliance_hold.py --register projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv --target execution/_Decomposition/SOFTWARE_DECOMP.md --operation consume` | 0 | `{"operation": "consume", "status": "ALLOW"}`. The register (SHA-256 `f877d931…1cbc`) is header-only |
| 2 | `PYTHONDONTWRITEBYTECODE=1 python3 tools/validation/validate_decomposition_registers.py projects/pec/execution --strict` (script SHA-256 `590d9aa3…8818`) | 0 | Families SCH, EVQ, XRG, DRB. 64 registers scanned. 255 dependency rows (ANCHOR 136, EXECUTION 119). 64 deliverables declared. `ERROR findings: 0`, `WARNING findings: 0` |
| 3 | `shasum -a 256` over the method files, the decomposition package, the pointers and the SCA-004 snapshot | 0 | All values are recorded in `Brief.md` and below. All three brief-supplied hashes match |

The brief wrote the interpreter as `python3`. The absolute interpreter path
above was used, and `PYTHONDONTWRITEBYTECODE=1` was added so that no bytecode
was written into the repository.

## Parse and comparison results

- The audited decomposition SHA-256 is
  `7cca5cdbb1ba4bd866391abf00998bc80f587a23505a6f5b6bceb8df48b65c81`, matching
  the brief and both pointers.
- `ScopeLedger.csv` is `2103afa2…9e25` and `Deliverables.csv` is
  `49f90448…6b72`, both matching the brief. `ContextBudgetQA.csv` is
  `5c8d3099…2bef` and `Companion_Inventory.csv` is `18793e15…ec23`, both
  unchanged since SCA-004.
- 11/11 package folders and 64/64 deliverable folders were found. There is no
  reverse-only folder, and every package contains only `1_Working/`.
- The §5 compact control view matches `Deliverables.csv` for 64/64 rows.
  `ContextBudgetQA.csv` matches for 64/64.
- 64/64 contexts parsed and matched on all compared fields, including
  `ContextEnvelope`. 64/64 provenance blocks name revision 1.4.
- 94 ledger rows parsed: 72 `IN`, 14 `OUT`, 8 `TBD`.
  - Every `IN` package and deliverable reference resolves.
  - No `IN` row lacks a deliverable, and no `OUT`/`TBD` row carries a mapping.
  - `DeliverableIDs` in the ledger and `CoversScopeItems` in the register are
    reciprocal for 64/64.
  - The per-package `IN` counts equal the §4 "Assigned (count)" column for
    11/11.
- Objective scope-item counts are OBJ-001 22, OBJ-002 12, OBJ-003 13,
  OBJ-004 11, OBJ-005 9 and OBJ-006 9. Supporting-deliverable counts are
  20/12/12/10/7/9. Both sets equal §3 lines 322–327.
- Mapping residue is 9 deliverables and 11 `IN` rows (SOW-022, 023, 033–038,
  044, 063, 087), which equals §7 line 539.
- Envelope counts are S 28 / M 34 / L 2 / XL 0, which equals §5 and §7.
- Lifecycle is 26 `INITIALIZED`, 32 `OPEN`, 4 `CHECKING` and 2
  `IN_PROGRESS`, each read from the `**Current State:**` line at
  `_STATUS.md:3`.
- Contracts are 32 valid `SOW_V1` (4 `CHECKING`, 26 `INITIALIZED`,
  2 `IN_PROGRESS`) and 32 `NONE` at `OPEN`. There are 0 legacy, dual or
  invalid contracts.
- Deliverable-local anticipated artifact sets: 3 present and 61 absent. The
  absences for `DEL-01-03` (`IN_PROGRESS`), `DEL-01-05` (`IN_PROGRESS`) and
  `DEL-08-02` (`CHECKING`) are warnings.
- The active SCA-004 snapshot has all core SOFTWARE artifacts, and the seven
  fixed state fields appear in both `RUN_SUMMARY.md` and `Handoff_State.md`.
  These hashes match the live bytes:

  | File | SHA-256 |
  |---|---|
  | `Handoff_State.md` | `919d40bb…e970` |
  | `RUN_SUMMARY.md` | `db0ca735…75bc` |
  | `Post_Change_Coverage.json` (equal to the COV_SCA004_POSTCHANGE `coverage_summary.json`) | `0d3ec0a8…d9ec` |
  | `Pre_Change_Coverage.json` (equal to the COV_SCA004_PRECHANGE `coverage_summary.json`) | `183c6d94…2813` |
  | `Supersession_Map.csv` | `9b62e987…fcb9` |
  | `DEL-01-06/_CONTEXT.md` | `24f357cc…94b2` |

## Limits

`AnticipatedArtifacts` holds descriptive classes of artifact, not filenames.
Check 6 therefore uses conservative, deliverable-folder-local matching and
does not treat source-tree bytes under `projects/pec/v2/` as matches. The
source-tree locations are cited in the warnings. Their fitness, acceptance and
completeness were not judged.

The `REMAINING_EVIDENCE_*` folders under `DEL-01-03` were in flight and
untracked at scan time. They were observed but not evaluated, and their
completeness is UNKNOWN to this audit.

Whether the four SOW contracts, the `DEL-00-03` SPEC and the orientation maps
named stale in the SCA-004 handoff have since been repaired was not
determined, except as recorded in the cited 2026-08-03 PROJECT_SETUP and
WORKING_ITEMS handoffs. That status is UNKNOWN beyond those records.

This derivative audit validates structural coverage and active-snapshot
honesty. It does not accept SCA-005 checkpoint group 1 or any artifact, change
any governed state, authorize amendment or implementation, or replace the
accepted decomposition or SCA truth. Per the sealed brief, the audit
`_LATEST.md` pointer (SHA-256 `0084d218…7432`, naming
`COV_SCA004_POSTCHANGE_2026-08-03_1442`) was intentionally not updated.
