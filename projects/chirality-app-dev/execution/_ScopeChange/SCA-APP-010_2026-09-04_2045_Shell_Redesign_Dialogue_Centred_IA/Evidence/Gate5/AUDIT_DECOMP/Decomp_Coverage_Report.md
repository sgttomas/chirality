# Decomposition Coverage Report — SCA-APP-010 Gate-5 Post-change Candidate Audit

**Overall:** `WARNINGS`
**Closure readiness:** `FAIL`
**Basis:** `11b47882f7e8726a42829cd26db5ecd8383f43b5`
**Timestamp:** `2026-09-04T22:04:00-06:00`
**Object audited:** the SCA-APP-010 Gate-3 candidate post-images against the unchanged live filesystem. SCA-APP-010 is the candidate under audit, not the active snapshot.

Authoritative inputs: candidate decomposition SHA-256
`c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61`;
candidate companion SHA-256
`63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`;
both equal the approved Gate-3 hashes (G3-CONFIRM). The live pre-images are
unchanged (`e46084ab...`, `e47fced6...`) and `_LATEST.md` is byte-identical
to Gate 1 (`f235ced4...`), pointing uniquely to
`execution/_ScopeChange/SCA-APP-009_2026-09-04_0944_App_V3_Pathway_Seating/`
(`OPEN_PENDING_DERIVATIVE_CLOSURE`). Section binding by normalized heading
text on the candidate: Objectives line 258, Packages line 275, Deliverables
line 292, Scope Ledger line 398, Coverage and Telemetry line 491, Open Issues
line 591 (one hit each).

| Check | Verdict | Fresh result |
|---|---|---|
| 1 Package forward coverage | PASS | 10/10 declared packages (`PKG-01`..`PKG-10`, lines 279-288) resolve to exactly one immediate `execution/PKG-XX_*` folder each. |
| 2 Deliverable forward coverage | PASS | 52/52 declared deliverables (lines 298-394) resolve to exactly one `PKG-XX_*/1_Working/DEL-XX-YY_*` folder each; no folder is added or removed by the amendment. |
| 3 Reverse folder coverage | WARNING | `PKG-00_DAG_Closure_and_Project_Control` and `DEL-00-01`, `DEL-00-02` exist with no declaration; 52/54 immediate deliverable folders and 10/11 package folders are declared (96.3 percent). Carried. |
| 4 ID consistency | PASS | No duplicate declared deliverable or scope-item ID, duplicate folder prefix, parentless declaration, or folder-prefix mismatch; every `DEL-XX-YY` is coupled to `PKG-XX`. `DEL-02-02` keeps its ID, package, and folder prefix through the rename. |
| 5 Context fidelity | WARNING | 52/52 `_CONTEXT.md` present. 35 MATCH, 17 PARTIAL (67.3 percent): the thirteen amended carriers lag the candidate rows (expected, routed to WORKING_ITEMS), and the four carried rows `DEL-04-01`, `DEL-05-01`, `DEL-08-05`, `DEL-09-05` are unchanged. `DEL-02-02` additionally carries a folder-name and DeliverableName lag. |
| 6 Artifact presence | WARNING | 12/202 anticipated artifacts resolve by the Gate-1 deterministic folder-local filename rule (5.9 percent); `DEL-01-01` is 5/5. The same fifty IN_PROGRESS rows are warning-level; OPEN `DEL-09-07` is informational. All 51 `ScopeOfWork.md` validate as `SOW_V1`. |
| 7 Objective mapping | PASS | 10/10 ledger objectives have live supporting deliverables (6 to 12 each) and ledger rows (6 to 24 each); no declared deliverable or IN ledger row lacks an objective. Telemetry (lines 493-508) agrees: 84/10/52/10, `UnmappedObjectives 0`. All eight `OpenIssueAffectedScopeCounts` equal the Open Issues rows; OI-008 lists SOW-010, SOW-081, SOW-082, SOW-083 (4) and telemetry says `SHELL_LADDER_BOUNDARY=4`. One INFO on the summary `MappedScopeItems` column. |
| 8 Ledger integrity | PASS | 84 rows: 79 IN, 4 OUT, 1 TBD. Every IN row references an existing package, existing deliverables, and existing objectives; Section 8 `CoversScopeItems` equals the ledger reverse view on all 52 deliverables (0 missing / 0 extra), including the four new rows SOW-081..084 (lines 484-487). |
| 9 Derivative parity | SKIPPED | Not SOFTWARE-variant-owned. |
| 9b Package shape | WARNING | Companion inventory table present (Section 2.2, lines 62-70). Candidate companion is exact: 18 columns, 83 unique IDs, 50 families, 83/83 `AppDecompositionBasis` cite `c7c05169...`, every deliverable and package reference resolves, and only `K-PATH-2` changes beyond the pin (gains `DEL-07-03` and the SOW-081 anchor). Prose at lines 70, 525, 542, 581 still says 81 IDs / 48 families and line 74 still says 10-package / 51-deliverable. Carried; explicitly excluded from this amendment. |
| 10 Active snapshot / handoff | WARNING | `_LATEST.md` resolves uniquely to SCA-APP-009 (42 files, `MANIFEST.sha256` 41/41 OK, unchanged since Gate 1). Two carried warnings: SCA-APP-008 historical residue and SCA-APP-009 state-field vocabulary. SCA-APP-010 is reported as the candidate under audit: its `Handoff_State.md` records phase Gate 4 and `ReadyForNextPhase = NO`; no later-phase or cleaner-closure claim exists (INFO). |
| 11 Lifecycle | PASS | 51 IN_PROGRESS, 1 OPEN (`DEL-09-07`); 52 statuses read, 51 paired `MEMORY.md` read; `DEL-09-07` has none by its five-file scaffold contract. Unchanged. |
| 12 Baseline comparison | PASS | No new blocker or major versus the Gate-1 pre-change audit. Eleven net-new warning occurrences (ten newly PARTIAL amended carriers plus the DEL-02-02 name lag) and two new informational rows, all explained below. |

## Topology and authority

The candidate is exactly 10 packages, 52 deliverables, 10 objectives, and 84
scope-ledger rows (79 IN / 4 OUT / 1 TBD), with context envelopes S=9,
M=41, L=2, XL=0 and 8 open issues, all equal to the Coverage and Telemetry
table (lines 493-508), the Context Budget QA table (the nine S rows and two L
rows match the declared envelopes exactly), the 10B topology row (line 577,
"SCA-APP-010 expressly authorizes 84 scope items"), and Propagation_Plan
section 1. The four new rows are SOW-081 (PKG-07; DEL-07-03, DEL-02-02,
DEL-04-04), SOW-082 (PKG-06; DEL-06-03, DEL-05-02, DEL-02-02, DEL-08-01),
SOW-083 (PKG-08; DEL-08-04, DEL-03-02), and SOW-084 (PKG-07; DEL-07-01,
DEL-08-01, DEL-04-04); every mapping resolves and every reverse view agrees.
SOW-007's mapping shrinks to DEL-08-03 alone, and DEL-02-02 now covers
SOW-006, SOW-081, SOW-082. DEC-025 (line 634) and OI-008 (line 602) are
present exactly once; the collision scan finds no SOW-081..084, DEC-025, or
OI-008 in the live decomposition.

`git diff --no-index -U0` from each live pre-image to its candidate is
identical (after the path header) to the frozen `Gate3/DECOMP_DIFF.patch`
and `Gate3/COMPANION_DIFF.patch`. The companion changes are 83 pin rebinds
plus the `K-PATH-2` row; coverage-status distribution is unchanged (MAPPED
33, MAPPED_WITH_OPEN_ISSUE 36, UNRESOLVED_SEMANTIC_OWNER 10, FUTURE_BOUNDARY
4); three rows cite `DEL-09-07`. The authority corpus is v20 with every
member `MATCH` and `no drift`; the decomposition is not a corpus member.

## Filesystem

All 54 immediate deliverable folders carry `_CONTEXT.md` and `_STATUS.md`.
The `DEL-09-07` folder remains the exact five-file OPEN scaffold with no
`ScopeOfWork.md`, `MEMORY.md`, or `Dependencies.csv`. `PKG-00` and
`DEL-00-01/02` remain undeclared control-plane folders (IN_PROGRESS, with
context, status, MEMORY, and valid SOW_V1). Since the Gate-1 basis
(`95b5687a`) the only tracked change outside the SCA-APP-010 snapshot is
`projects/chirality-app-dev/loop/LOOP_RECEIPTS.md`; no deliverable,
decomposition, companion, or pointer byte changed. The working tree carries
an uncommitted `Decision_Log.md` (G4-CONFIRM row) and this run's untracked
`Evidence/Gate5/` folder.

## Check 5 detail

The seventeen PARTIAL rows split into three groups.

Thirteen amended carriers (G5-010-COV-004) lag the candidate rows they will
be aligned to by WORKING_ITEMS after owner seating. Nine have a mechanical
Traceability gap: `DEL-02-02` lists SOW-006, SOW-007 against SOW-006,
SOW-081, SOW-082; `DEL-03-02` lacks SOW-083; `DEL-04-04` lacks SOW-081 and
SOW-084; `DEL-05-02` lacks SOW-082; `DEL-06-03` lacks SOW-082; `DEL-07-01`
lacks SOW-084; `DEL-07-03` lacks SOW-081; `DEL-08-01` lacks SOW-082 and
SOW-084; `DEL-08-04` lacks SOW-083. Three (`DEL-02-01`, `DEL-02-04`,
`DEL-02-05`) keep their coverage but their Deliverable Scope and Anticipated
Artifacts paragraphs predate the amended prose (composer context line, chat
navigator, account row host; per-view right-panel widths, activity strip,
chat annotations; app-wide account presentation, account row and popover).
`DEL-08-03`'s identity, description, artifacts, and coverage are unchanged,
but its context (lines 30 and 49) still names `DEL-02-02` as the contextual
Pipeline presentation consumer that the candidate Notes (line 370) retire
from the active shell. Ten of these rows were MATCH at Gate 1; `DEL-02-02`,
`DEL-02-05`, and `DEL-08-04` were already PARTIAL and now lag further.

`DEL-02-02` (G5-010-COV-005) is additionally renamed by the candidate to
"Right-Panel Coordination, Workflows, and Proposal UX" while its folder is
`DEL-02-02_Workbench_and_Pipeline_Selection_UX` and its `_CONTEXT.md`
DeliverableName reads "Work/Agents Coordination, Workbench, and Pipeline UX".
The ID and package binding are unchanged, so this is a name lag, not an ID
defect; the amendment retains the folder name and routes the label to
WORKING_ITEMS (context) and TASK_MANAGEMENT (register).

Four carried rows (G5-010-COV-003) are unchanged from Gate 1: `DEL-04-01`
(Traceability still SOW-018, SOW-044, SOW-046 / OBJ-004), `DEL-05-01`,
`DEL-08-05`, `DEL-09-05`. The two label observations (`DEL-02-03`
PackageName, `DEL-09-07` Discipline) remain INFO. `ResponsibleParty` on
`DEL-01-01` and `DEL-10-04` is permitted by the TBD rule.

## Check 7 detail

Check 7 resolves objectives from the ledger `ObjectiveID(s)` column and
passes. The Objectives table `MappedScopeItems` column is a summary that did
not equal the ledger reverse view for nine objectives before the amendment
and still does not; the candidate adds SOW-081-SOW-082 to OBJ-001 while the
ledger also maps SOW-082/083 to OBJ-005, SOW-081/084 to OBJ-006, and
SOW-081..084 to OBJ-007 (G5-010-COV-009, INFO). This is a pre-existing
pattern, not a candidate defect, and no telemetry surface depends on it.

## Check 10 detail

The active snapshot is unchanged: SCA-APP-009's root still carries every
required non-DOMAIN artifact, and its two carried findings stand (SCA-APP-008
residue WARNING; five of seven contract state-field names not exposed by
name, WARNING; pre-pointer wording, INFO). The SCA-APP-010 snapshot root
currently carries `Brief.md`, `Impact_Assessment.md`, `Propagation_Plan.md`,
`Amendment_Actions.csv`, `Pre_Change_Coverage.json`, `Decision_Log.md`,
`Handoff_State.md`, `Supersession_Delta.csv`, `Supersession_Map.csv` (45
rows, SHA-256 `2045684e...`, the expected cumulative map), the four Gate-4
matrices, `Gate3/`, and `Evidence/Gate1`, `Gate3`, `Gate4` (independent
reviews PASS with 0 BLOCKER / 0 MAJOR). `RUN_SUMMARY.md`, `MANIFEST.sha256`,
and the remaining Gate-5 evidence are steps 4-9 of Propagation_Plan section
5 not yet reached; this run supplies step 4's `Post_Change_Coverage.json`.
`Handoff_State.md` records phase Gate 4, `DecompositionTruthState =
INCOMPLETE`, and `ReadyForNextPhase = NO`, which does not overclaim
(G5-010-COV-015, INFO).

## Comparison with the Gate-1 pre-change audit

| Measure | Gate-1 pre-change (95b5687a, live pair) | This run (11b47882, candidate pair) |
|---|---|---|
| Topology | 10 / 52 / 80 (75/4/1), S9 M41 L2 XL0, 7 OI | 10 / 52 / 84 (79/4/1), S9 M41 L2 XL0, 8 OI |
| Companion | 83 rows / 50 families / 18 columns, pins `e46084ab` | 83 / 50 / 18, pins `c7c05169`; only K-PATH-2 changed beyond the pin |
| Forward / reverse coverage | 100 / 96.3 | identical |
| Reverse-view parity, duplicate IDs, dangling refs | 0 / 0 / 0 | 0 / 0 / 0 |
| Context fidelity | 45 MATCH, 7 PARTIAL (86.5) | 35 MATCH, 17 PARTIAL (67.3) |
| Artifact presence | 12/191 (6.3) | 12/202 (5.9); same 50 warning rows |
| Lifecycle / SOW / MEMORY | 51+1, 51/51 SOW_V1, 51 MEMORY | identical |
| Active snapshot / pointer | SCA-APP-009, `f235ced4` | identical |
| Blocker / warning / info | 0 / 63 / 6 | 0 / 74 / 8 |
| Overall / closure | WARNINGS / FAIL | WARNINGS / FAIL |

Occurrence-weighted movement: the seven Gate-1 PARTIAL occurrences become
four carried (G5-010-COV-003) plus three counted inside the thirteen amended
carriers (G5-010-COV-004); ten amended carriers are newly PARTIAL and the
DEL-02-02 name lag (G5-010-COV-005) is new, so warnings rise by eleven
(63 to 74). Two informational rows are new: the `MappedScopeItems` method
note (G5-010-COV-009) and the SCA-APP-010 candidate-snapshot state
(G5-010-COV-015). Every other row is carried unchanged in class and count.
There is no new BLOCKER and no new MAJOR condition relative to pre-change;
every new warning is the expected consequence of amending authority before
its carrier surfaces are realigned, and each is already routed by
`Propagation_Plan.md` section 3 and `DOWNSTREAM_HANDOFFS.csv`.

## What to fix for a cleaner rerun

- After application and owner seating, align the thirteen amended carriers'
  `_CONTEXT.md` (identity, Traceability, scope prose, artifacts) and the
  DEL-02-02 DeliverableName only through WORKING_ITEMS under sealed briefs;
  refresh the Task Management register label through TASK_MANAGEMENT.
- Align the four carried PARTIAL contexts and the `DEL-04-01` Traceability
  table through the same owning workflow.
- Reconcile the 81/48 and 10/51 prose with the exact 83/50 companion and
  10/52 topology only through a governed authority amendment; consider
  whether the Objectives `MappedScopeItems` column should be regenerated or
  labelled as a summary.
- Expose the seven contract state fields by name in a future active
  snapshot; SCA-APP-008 and SCA-APP-009 bytes stay immutable history.

This audit authorizes no application, amendment, repair, pointer movement,
SOW creation, dependency extraction, implementation, product, release, or
severity change.
