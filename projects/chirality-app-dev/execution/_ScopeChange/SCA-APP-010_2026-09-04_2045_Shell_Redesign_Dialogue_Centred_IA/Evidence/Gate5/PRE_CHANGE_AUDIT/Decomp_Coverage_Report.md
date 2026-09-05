# Decomposition Coverage Report — SCA-APP-010 Gate-5 Pre-change Baseline

**Overall:** `WARNINGS`
**Closure readiness:** `FAIL`
**Basis:** `11b47882f7e8726a42829cd26db5ecd8383f43b5` (fast-forward descendant of Gate-1 basis `95b5687a7c9a4c6fe6e655f628495dec08ce04d8`)
**Timestamp:** `2026-09-04T21:56:56-06:00`

Authoritative inputs: decomposition SHA-256
`e46084abc0f85970dbe4ed49d1366a99e9930bbb9d9bd87b86f998f98155ab97`;
companion SHA-256
`e47fced6f0bea32b1d18f987a7e33af0432271c4ff49bb196cdad6fb91742b70`;
`_LATEST.md` SHA-256
`f235ced4526aac51c4e7f5307ac619f3500e824c3549960b106bb80b67a6e17c`,
pointing uniquely to
`execution/_ScopeChange/SCA-APP-009_2026-09-04_0944_App_V3_Pathway_Seating/`
(`OPEN_PENDING_DERIVATIVE_CLOSURE`; git tree
`1c5b9e68049460c3a9a6c1abadc1b8a64e2bc085` at both the Gate-1 basis and
HEAD). All match the brief's expected values. Section binding by normalized
heading text: Objectives line 246, Packages line 263, Deliverables line 280,
Scope Ledger line 386 (one hit each).

| Check | Verdict | Fresh result |
|---|---|---|
| 1 Package forward coverage | PASS | 10/10 declared packages (`PKG-01`..`PKG-10`, lines 265-274) resolve to exactly one immediate `execution/PKG-XX_*` folder each. |
| 2 Deliverable forward coverage | PASS | 52/52 declared deliverables (lines 286-382) resolve to exactly one `PKG-XX_*/1_Working/DEL-XX-YY_*` folder each, including `DEL-09-07` (line 372). |
| 3 Reverse folder coverage | WARNING | `PKG-00_DAG_Closure_and_Project_Control` and `DEL-00-01`, `DEL-00-02` exist with no declaration; 52/54 immediate deliverable folders and 10/11 package folders are declared (96.3 percent). Carried. |
| 4 ID consistency | PASS | No duplicate declared ID, duplicate folder prefix, parentless declaration, or folder-prefix mismatch; every `DEL-XX-YY` is coupled to `PKG-XX`. |
| 5 Context fidelity | WARNING | 52/52 `_CONTEXT.md` present and byte-identical to the Gate-1 basis. Identity fields (PackageID, DeliverableID, Type, ContextEnvelope, CoversScopeItems, SupportsObjectives) match on 51 rows; `DEL-04-01` Traceability lacks `SOW-079` / `OBJ-002`. Seven Deliverable Scope paragraphs remain PARTIAL (carried set). 86.5 percent. |
| 6 Artifact presence | WARNING | 12/191 anticipated artifacts resolve by the Gate-1 deterministic folder-local filename rule (6.3 percent); `DEL-01-01` is 5/5; per-row distribution identical to Gate 1. Fifty IN_PROGRESS rows are warning-level; OPEN `DEL-09-07` is informational. All 51 `ScopeOfWork.md` validate as `SOW_V1`. |
| 7 Objective mapping | PASS | 10/10 objectives have live supporting deliverables (6 to 12 each) and ledger rows (6 to 24 each); no declared deliverable or IN ledger row lacks an objective. Telemetry (lines 475-490) agrees: 80/10/52/10, `UnmappedObjectives 0`. |
| 8 Ledger integrity | PASS | 80 rows: 75 IN, 4 OUT, 1 TBD. Every IN row references an existing package and existing deliverables; Section 8 `CoversScopeItems` equals the ledger reverse view on all 52 deliverables (including OUT/TBD boundary traces). |
| 9 Derivative parity | SKIPPED | Not SOFTWARE-variant-owned. |
| 9b Package shape | WARNING | Companion inventory table present (Section 2.2, lines 62-70) and companion register is exact (18 columns, 83 unique IDs, 50 families, every `AppDecompositionBasis` cites `e46084ab...`). Prose at lines 70, 509, 526, 565 still says 81 IDs / 48 families. Carried. |
| 10 Active snapshot / handoff | WARNING | `_LATEST.md` resolves uniquely to SCA-APP-009, which exists and carries all nine required non-DOMAIN root artifacts plus `Supersession_Delta.csv`, `Supersession_Map.csv`, and `Evidence/`; 42 files; `MANIFEST.sha256` verifies 41/41. Pointer bytes equal the approved literal postimage. Two carried warnings: SCA-APP-008 historical residue (six absent root artifacts, non-current) and SCA-APP-009 state-field vocabulary (five of seven contract field names absent). New INFO: SCA-APP-010 is a non-active in-progress SCA folder (not an error). No later-phase or cleaner-closure claim. |
| 11 Lifecycle | PASS | 51 IN_PROGRESS, 1 OPEN (`DEL-09-07`); 52 statuses read, 51 paired `MEMORY.md` read; `DEL-09-07` has none by its five-file scaffold contract. |
| 12 Baseline comparison | PASS | No new blocker, major, or warning versus the Gate-1 pre-change audit. Every audited surface is byte-identical; the only new issue row is the informational SCA-APP-010 folder note. |

## Topology and authority

The decomposition at this basis is exactly 10 packages, 52 deliverables, 10
objectives, and 80 scope-ledger rows (75 IN / 4 OUT / 1 TBD), with context
envelopes S=9, M=41, L=2, XL=0, all equal to the Coverage and Telemetry
table (lines 477-487) and the 10B acceptance-checklist topology row (line
561). The decomposition and companion register are byte-identical to the
Gate-1 audit inputs and to the SCA-APP-009 approved postimages. The
authority corpus is v20 with every member `MATCH` and `no drift`.

The companion register cross-references only declared packages and
deliverables; three rows cite `DEL-09-07`. Coverage status distribution:
MAPPED 33, MAPPED_WITH_OPEN_ISSUE 36, UNRESOLVED_SEMANTIC_OWNER 10,
FUTURE_BOUNDARY 4.

## Filesystem

All 54 immediate deliverable folders carry `_CONTEXT.md` and `_STATUS.md`.
The `DEL-09-07` folder contains exactly `_CONTEXT.md`, `_STATUS.md`,
`_REFERENCES.md`, `_DEPENDENCIES.md`, and zero-byte `_SEMANTIC.md`, all
regular files, with no `ScopeOfWork.md`, `MEMORY.md`, or `Dependencies.csv`;
its scaffold-format context binds PKG-09 / MIGRATION_SCRIPT / TBD / M /
SOW-080 / OBJ-008 exactly. `PKG-00` and `DEL-00-01/02` remain undeclared
control-plane folders (IN_PROGRESS, with context, status, and MEMORY).
`git diff --name-only 95b5687a -- 'execution/PKG-*'` is empty: no deliverable
byte differs from the Gate-1 basis.

## Check 5 detail

The seven PARTIAL rows are unchanged from Gate 1: `DEL-02-02` (line 296)
omits the SCA-APP-009 Agent 0/1/2 role-entry duty; `DEL-04-01` (line 314)
omits App Server observation duties and its Traceability table still lists
`SOW-018, SOW-044, SOW-046` / `OBJ-004` against the authoritative
`SOW-018, SOW-044, SOW-046, SOW-079` / `OBJ-002, OBJ-004`; `DEL-05-01`
(line 324) omits backup-before-write, rollback, source-byte, and
`legacySource` duties; `DEL-02-05` (299), `DEL-08-04` (359), `DEL-08-05`
(360), and `DEL-09-05` (370) carry their accepted divergences. The two
informational label observations re-derive mechanically: `DEL-02-03`
`_CONTEXT.md` line 11 carries the pre-SCA-APP-004 PackageName, and
`DEL-09-07` `_CONTEXT.md` line 5 carries
`Discipline: NOT_PRESENT_IN_ACCEPTED_DECOMPOSITION`. `ResponsibleParty`
assignments on `DEL-01-01` and `DEL-10-04` are permitted by the TBD rule.

## Check 10 detail

The active snapshot is SCA-APP-009, whose root carries every required
non-DOMAIN artifact (`AGENT_SCOPE_CHANGE.md` lines 655-676) and whose git
tree is unchanged since Gate 1. SCA-APP-008 remains historical residue
lacking `Propagation_Plan.md`, `Amendment_Actions.csv`,
`Pre_Change_Coverage.json`, `Post_Change_Coverage.json`, `Decision_Log.md`,
and `RUN_SUMMARY.md`; its defect stays a WARNING under the protocol's
non-current rule, and no SCA-APP-008 path appears in
`git diff --name-only 95b5687a..HEAD`.

SCA-APP-009 still exposes `ReadyForNextPhase = NO` and
`MetadataAlignmentState = NOT_STARTED` under the contract field names
(`Handoff_State.md` lines 5, 12) but carries `DecompositionTruthState`,
`DerivativePackageState`, `ContentRemediationState`, `DownstreamRerunState`,
and `AuditState` only under other names or not at all
(`AGENT_SCOPE_CHANGE.md` lines 678-690); the carried WARNING stands. Its
pre-pointer statements (`POINTER_APPROVAL_READY`, "live pointer remains
unchanged") are immutable history; the live pointer equals the literal
postimage recorded in `Evidence/Gate5/POINTER_CANDIDATE_VALIDATION.md` line
38. `Post_Change_Coverage.json` is byte-identical to
`Evidence/Gate5/AUDIT_DECOMP/coverage_summary.json`.

SCA-APP-010 is a non-active in-progress SCA folder. At the Gate-1 basis it
held four root files written concurrently by the intake; at HEAD it holds 35
tracked files (root artifacts through `Propagation_Plan.md`, the `Gate3/`
candidate package, and `Evidence/Gate1`, `Gate3`, `Gate4`), and the working
tree adds one uncommitted `Decision_Log.md` edit (the G4-CONFIRM row, read as
data). `_LATEST.md` does not reference it, its own `Handoff_State.md`
records `ReadyForNextPhase = NO` and no pointer movement, and it is not
evaluated against the active-snapshot contract. This is recorded as INFO
G5-010-COV-013, not as an error.

## Comparison with the Gate-1 pre-change audit

| Measure | Gate-1 pre-change (95b5687a) | This run (11b47882) |
|---|---|---|
| Topology | 10 / 52 / 80 (75/4/1), S9 M41 L2 XL0 | identical |
| Companion | 83 rows / 50 families / 18 columns | identical |
| Forward / reverse coverage | 100 / 96.3 | identical |
| Context fidelity | 45 MATCH, 7 PARTIAL | identical set |
| Artifact presence | 12/191 (stated rule) | 12/191, identical per-row distribution |
| Lifecycle | 51 IN_PROGRESS, 1 OPEN | identical |
| Active snapshot | SCA-APP-009 (PASS with warnings) | identical (tree `1c5b9e68...`) |
| Authority corpus | v20, no drift | identical |
| Blocker / warning / info | 0 / 63 / 6 | 0 / 63 / 7 |
| Overall / closure | WARNINGS / FAIL | WARNINGS / FAIL |

What changed versus Gate 1: nothing in the audited surfaces. The 63 warning
occurrences and the six Gate-1 informational rows carry unchanged (IDs
re-labelled `G5-010-COV-001..012` in the same order). The single delta is
the new informational row G5-010-COV-013 recording SCA-APP-010's growth as a
non-active in-progress SCA folder. The only tracked changes between the two
bases are 34 added paths under the SCA-APP-010 snapshot and 44 inserted
lines in `projects/chirality-app-dev/loop/LOOP_RECEIPTS.md`; neither is an
audited surface. No blocker, major, or warning was added or resolved.

## What to fix for a cleaner rerun

- Align the seven PARTIAL contexts, and the `DEL-04-01` Traceability table,
  only through their owning workflow (WORKING_ITEMS metadata alignment named
  open in SCA-APP-009 `Handoff_State.md`).
- Reconcile the 81/48 prose with the exact 83/50 companion only through a
  governed authority amendment (the approved SCA-APP-010 Gate-3 candidate is
  the pending carrier; this audit does not apply it).
- Expose the seven contract state fields by name in a future active
  snapshot; SCA-APP-008 and SCA-APP-009 bytes stay immutable history.
- Decide whether `_Evaluation/DecompCoverage/_LATEST.md` should be
  re-pointed or retired now that audits live inside SCA snapshots.

This audit authorizes no amendment, repair, pointer movement, SOW creation,
dependency extraction, implementation, product, release, or severity change.
