# Decomposition Coverage Report — SCA-APP-010 Post-alignment Fresh Full Audit

**Overall:** `WARNINGS`
**Closure readiness:** `FAIL`
**Basis:** `d66395d101143df68d956984f7ab93f5027418ec` plus the working tree (thirteen refreshed registers, uncommitted)
**Timestamp:** `2026-09-05T05:35:53-06:00`
**Object audited:** the live applied SCA-APP-010 decomposition and companion register against the live filesystem after owner seating (D-APP-108), WORKING_ITEMS alignment (PR #713), and the N3 reviewed dependency-register writes. SCA-APP-010 is the active snapshot.

Authoritative inputs: decomposition SHA-256
`c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` (content commit
`dbd812a52d5ed0cb3ed173f3aaaa68703a914291`); companion SHA-256
`63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`; both equal the approved Gate-3
candidates the Gate-5 post-change audit judged. `_ScopeChange/_LATEST.md`
(`b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0`) points uniquely to
`execution/_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/`
(`OPEN_PENDING_DERIVATIVE_CLOSURE`) under the G5-POINTER ruling. Section
binding by normalized heading text: Objectives line 258, Packages line 275,
Deliverables line 292, Scope Ledger line 398, Coverage and Telemetry line
491, Open Issues line 591 (one hit each). Comparison basis: the Gate-5
post-change audit `SCA_APP_010_GATE5_POSTCHANGE` at
`projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/Evidence/Gate5/AUDIT_DECOMP/` (0 / 74 / 8).

| Check | Verdict | Fresh result |
|---|---|---|
| 1 Package forward coverage | PASS | 10/10 declared packages (`PKG-01`..`PKG-10`, lines 279-288) resolve to exactly one immediate `execution/PKG-XX_*` folder each. |
| 2 Deliverable forward coverage | PASS | 52/52 declared deliverables (rows 298-394) resolve to exactly one `PKG-XX_*/1_Working/DEL-XX-YY_*` folder each; no folder added, removed, or renamed since Gate 5. |
| 3 Reverse folder coverage | WARNING | `PKG-00_DAG_Closure_and_Project_Control` and `DEL-00-01`, `DEL-00-02` exist with no declaration; 52/54 deliverable folders and 10/11 package folders are declared (96.3 percent). Carried. |
| 4 ID consistency | PASS | No duplicate declared deliverable or scope-item ID, duplicate folder prefix, parentless declaration, or folder-prefix mismatch; every `DEL-XX-YY` is coupled to `PKG-XX`. `DEL-02-02` keeps its ID, package, and folder prefix; its context and register labels now equal the applied name. |
| 5 Context fidelity | WARNING | 52/52 `_CONTEXT.md` present. 35 MATCH, 17 PARTIAL (67.3 percent, same count as Gate 5 but a different composition): the thirteen amended carriers are aligned on identity, DeliverableName, Package Scope, and Deliverable Scope (PR #713) and still lag on Traceability `CoversScopeItems` (nine) and the Anticipated Artifacts paragraph (ten), plus DEL-08-03's ownership-boundary section; the four carried rows `DEL-04-01`, `DEL-05-01`, `DEL-08-05`, `DEL-09-05` are unchanged. G5-010-COV-004 partially resolved; G5-010-COV-005 resolved at the context. |
| 6 Artifact presence | WARNING | 12/202 anticipated artifacts resolve by the deterministic folder-local filename rule (5.9 percent), identical per row to Gate 5; `DEL-01-01` is 5/5. The same fifty IN_PROGRESS rows are warning-level; OPEN `DEL-09-07` is informational and is no longer the five-file scaffold (PR #710, PR #712). 54/54 `ScopeOfWork.md` validate as `SOW_V1`. |
| 7 Objective mapping | PASS | 10/10 ledger objectives have supporting deliverables with folders (6 to 12 each) and ledger rows (10 to 24 each); no declared deliverable or IN ledger row lacks an objective. Telemetry (lines 493-508) agrees: 84/10/52/10, `UnmappedObjectives 0`. All eight `OpenIssueAffectedScopeCounts` equal the Open Issues rows; OI-008 lists SOW-010, SOW-081, SOW-082, SOW-083 (4) and telemetry says `SHELL_LADDER_BOUNDARY=4`. One INFO on the summary `MappedScopeItems` column (carried). |
| 8 Ledger integrity | PASS | 84 rows: 79 IN, 4 OUT, 1 TBD. Every IN row references an existing package, existing deliverables, and existing objectives; Section 8 `CoversScopeItems` equals the ledger reverse view on all 52 deliverables (0 missing / 0 extra), including SOW-081..084 (lines 484-487). |
| 9 Derivative parity | SKIPPED | Not SOFTWARE-variant-owned. |
| 9b Package shape | WARNING | Companion inventory table present (Section 2.2, lines 62-70). Companion is exact: 18 columns, 83 unique IDs, 50 families, 83/83 `AppDecompositionBasis` cite the live hash, every deliverable and package reference resolves. Prose at lines 70, 525, 542, 581 still says 81 IDs / 48 families and lines 13 and 74 still say 51 deliverables. Carried; explicitly excluded from SCA-APP-010. |
| 10 Active snapshot / handoff | WARNING | `_LATEST.md` resolves uniquely to SCA-APP-010 (60 files, `MANIFEST.sha256` 59/59 OK, required root set complete, `Post_Change_Coverage.json` byte-identical to its audit summary). `Handoff_State.md` exposes all seven state fields by name, records phase Gate 5 applied and merged with the pointer moved, and `ReadyForNextPhase = NO`; no over-claim (handoff-state PASS). The one warning is the carried SCA-APP-008 historical residue; SCA-APP-009's state-field vocabulary and pre-pointer wording are historical INFO; SCA-APP-010's own pre-pointer `RUN_SUMMARY.md` wording and trailing derivative fields are INFO. |
| 11 Lifecycle | PASS | 51 IN_PROGRESS, 1 OPEN (`DEL-09-07`); 52 statuses read, 51 paired `MEMORY.md` read; `DEL-09-07` has none. Unchanged. |
| 12 Baseline comparison | PASS | No new blocker or major versus the Gate-5 post-change audit. Zero new warning occurrences; two warning rows resolved or reclassified (DEL-02-02 name lag; SCA-APP-009 vocabulary); two informational rows added by those reclassifications. Occurrence-weighted 0 / 74 / 8 to 0 / 72 / 10. |

## Topology and authority

The applied decomposition is exactly 10 packages, 52 deliverables, 10
objectives, and 84 scope-ledger rows (79 IN / 4 OUT / 1 TBD), with context
envelopes S=9, M=41, L=2, XL=0 and 8 open issues, all equal to the Coverage
and Telemetry table (lines 493-508), the Context Budget QA table, the 10B
topology row (line 577), and the Gate-5 audit. The four new rows SOW-081
(PKG-07; DEL-07-03, DEL-02-02, DEL-04-04), SOW-082 (PKG-06; DEL-06-03,
DEL-05-02, DEL-02-02, DEL-08-01), SOW-083 (PKG-08; DEL-08-04, DEL-03-02),
and SOW-084 (PKG-07; DEL-07-01, DEL-08-01, DEL-04-04) resolve and every
reverse view agrees. DEC-025 (line 634) and OI-008 (line 602) are present
exactly once. The companion changes since the pre-image are the 83 pin
rebinds plus the `K-PATH-2` row, unchanged from Gate 5. The authority corpus
is v20 with every member `MATCH` and `no drift`.

## Filesystem

All 54 immediate deliverable folders carry `_CONTEXT.md` and `_STATUS.md`.
Since the Gate-5 basis (`11b47882`) the tracked delta is PR #708 (application
and snapshot completion), PR #709/#710 (DEL-09-07 Scope of Work), PR #711
(pointer to SCA-APP-010), PR #712 (DEL-09-07 dependency and semantic setup),
and PR #713 (owner seating under D-APP-108, WORKING_ITEMS alignment of the
thirteen carriers, routed Root notice). The working tree adds the thirteen
N3 reviewed register writes (`Dependencies.csv`, `_DEPENDENCIES.md`, 26
files, every hash equal to the sealed brief) and thirteen untracked TASK run
records. `PKG-00` and `DEL-00-01/02` remain undeclared control-plane folders
(IN_PROGRESS, with context, status, MEMORY, and valid SOW_V1).

## Check 5 detail

The seventeen PARTIAL rows split into two groups.

Thirteen amended carriers (PA-010-COV-004; G5-010-COV-004 partially
resolved). PR #713 executed the WI permitted effect exactly: on every carrier
the `_CONTEXT.md` title, `DeliverableName`, `PackageName`, Package Scope,
and Deliverable Scope now equal the applied row (Description overlap 1.0 on
all thirteen; Gate 5 ranged 0.09 to 1.0), and `DEL-02-02` carries its
applied name. Two surfaces the write set did not name still lag. First, the
Traceability table on nine carriers: `DEL-02-02` lists SOW-006, SOW-007
against SOW-006, SOW-081, SOW-082; `DEL-03-02` lacks SOW-083; `DEL-04-04`
lacks SOW-081 and SOW-084; `DEL-05-02` lacks SOW-082; `DEL-06-03` lacks
SOW-082; `DEL-07-01` lacks SOW-084; `DEL-07-03` lacks SOW-081; `DEL-08-01`
lacks SOW-082 and SOW-084; `DEL-08-04` lacks SOW-083, while the same
carriers' `ScopeOfWork.md` `project_scope_refs` and the refreshed
`Dependencies.csv` anchors already carry the applied items. Second, the
Anticipated Artifacts paragraph on ten carriers (`DEL-02-01`, `DEL-02-02`,
`DEL-02-04`, `DEL-02-05`, `DEL-04-04`, `DEL-06-03`, `DEL-07-01`,
`DEL-07-03`, `DEL-08-01`, `DEL-08-04`) predates the amended artifact lists;
`DEL-02-02`'s still reads "Workbench/Pipeline views" and omits the Who is
working view, Workflows view, proposal card, role-entry controls, and
posture labels. `DEL-08-03` matches on identity, Traceability, Description,
and artifacts, but its SCA-APP-004 Ownership Boundary section (line 53)
still names `DEL-02-02` as owner of re-hosted Workbench/Pipeline and
contextual Run presentation, which the applied row L370 Notes retire. Under
the Gate-5 PARTIAL rule all thirteen remain PARTIAL; the residual lag is
outside the executed WI permitted effect ("Align DeliverableName,
Deliverable Scope, and Package Scope prose") and belongs to the owner as a
further WORKING_ITEMS authorization or a `FUTURE_WRITE_SET.csv` amendment.

`DEL-02-02` (PA-010-COV-005; G5-010-COV-005 resolved at the context). The
applied name is now carried by `_CONTEXT.md`, `ScopeOfWork.md`, the
`_STATUS.md` history line, and every `Dependencies.csv` row. The physical
folder `DEL-02-02_Workbench_and_Pipeline_Selection_UX` keeps its prior label
by design (A015, no relocation), which has no ID effect; the Task Management
register cites `DEL-02-02` by ID only and carries no stale name string.

Four carried rows (PA-010-COV-003) are unchanged since Gate 5 (empty git
diff against `11b47882`): `DEL-04-01` (Traceability still SOW-018, SOW-044,
SOW-046 / OBJ-004), `DEL-05-01`, `DEL-08-05`, `DEL-09-05`. The two label
observations (`DEL-02-03` PackageName, `DEL-09-07` Discipline) remain INFO.

## Thirteen refreshed dependency registers

Every `Dependencies.csv` and `_DEPENDENCIES.md` hashes exactly to the sealed
brief; `validate_dependencies_schema.py` returns VALID for all 52 declared
registers (195 rows across the thirteen); `RegisterSchemaVersion` v3.1 and
`FromDeliverableID` equal to the carrier on every row; `FromDeliverableName`
equals the applied row name on every row. Every applied `CoversScopeItems`
and `SupportsObjectives` value, including SOW-081..084 on every carrier the
ledger maps them to, is anchored by an ACTIVE anchor row citing the applied
decomposition file, and `DEL-02-02`'s SOW-007 anchor is RETIRED 2026-09-05.
Root-owned targets are `EXTERNAL`/`TBD`; the pre-existing `DEL-08-01`
`DEP-08-01-013` absolute Root path is byte-identical to the pre-image and is
AUDIT_DEP_CLOSURE's finding. Graph closure and SCC parity are N4's verdict,
not this audit's.

## Check 10 detail

SCA-APP-010 is the active snapshot: root complete, manifest 59/59 OK,
`Handoff_State.md` truthful and field-complete, `ReadyForNextPhase = NO`.
`RUN_SUMMARY.md` retains pre-pointer wording (`APPLIED_PRE_POINTER`;
"SCA-APP-009 (not moved)"; `POINTER_SUBGATE_READY`) superseded by the
G5-POINTER decision and the handoff state, and `DerivativePackageState =
INCOMPLETE` / `MetadataAlignmentState = NOT_STARTED` now trail the working
tree (an under-claim; the frozen snapshot is not mutated by later evidence).
SCA-APP-009 is complete and historical (INFO); SCA-APP-008 still lacks six
required artifacts (WARNING, carried). The evaluation-root
`_Evaluation/DecompCoverage/_LATEST.md` still names the SCA-APP-006 run and
is not moved by this run (INFO).

## Comparison with the Gate-5 post-change audit

| Measure | Gate-5 post-change (11b47882, candidate pair) | This run (d66395d1 + working tree, live pair) |
|---|---|---|
| Topology | 10 / 52 / 84 (79/4/1), S9 M41 L2 XL0, 8 OI | identical |
| Companion | 83 / 50 / 18, pins `c7c05169` | identical (pins now cite the live file) |
| Forward / reverse coverage | 100 / 96.3 | identical |
| Reverse-view parity, duplicate IDs, dangling refs | 0 / 0 / 0 | 0 / 0 / 0 |
| Context fidelity | 35 MATCH, 17 PARTIAL (67.3) | 35 MATCH, 17 PARTIAL (67.3); thirteen carriers aligned on identity and scope prose, still lagging on Traceability and artifacts |
| DEL-02-02 name lag | WARNING | resolved at the context; folder label INFO |
| Artifact presence | 12/202 (5.9) | identical per row |
| Lifecycle / SOW / MEMORY | 51+1, 51/51 SOW_V1, 51 MEMORY | 51+1, 52/52 SOW_V1 (DEL-09-07 added), 51 MEMORY |
| Refreshed registers | not audited (STALE_REBUILD_REQUIRED) | 13/13 hash-exact, v3.1 VALID, anchored to the applied rows |
| Active snapshot / pointer | SCA-APP-009, `f235ced4` | SCA-APP-010, `b297f43e`; handoff-state fields complete |
| Blocker / warning / info | 0 / 74 / 8 | 0 / 72 / 10 |
| Overall / closure | WARNINGS / FAIL | WARNINGS / FAIL |

Occurrence-weighted movement: no new warning occurrence and no new blocker
or major. Two warning rows leave the warning class: G5-010-COV-005 (DEL-02-02
name lag) is resolved at the context and its folder-label residual is INFO;
G5-010-COV-013 (SCA-APP-009 state-field vocabulary) is reclassified to INFO
because SCA-APP-009 is no longer the active snapshot, a pointer effect and
not a repair. G5-010-COV-004 stays a 13-occurrence WARNING with its identity
and scope-prose portion resolved and its Traceability and Anticipated
Artifacts portion open. Every other row is carried unchanged in class and
count; PA-010-COV-008 and PA-010-COV-015 carry updated content (DEL-09-07
folder state; SCA-APP-010 now active).

## What to fix for a cleaner rerun

- Authorize WORKING_ITEMS to align the thirteen carriers' `_CONTEXT.md`
  Traceability tables and Anticipated Artifacts paragraphs, and DEL-08-03's
  ownership-boundary section, to the applied rows (a further sealed brief or
  an amendment of `FUTURE_WRITE_SET.csv` WI permitted effect); the
  `ScopeOfWork.md` refs and register anchors already carry the applied items.
- Align the four carried PARTIAL contexts and the `DEL-04-01` Traceability
  table through the same owning workflow; refresh the `DEL-02-03`
  PackageName and `DEL-09-07` Discipline labels.
- Reconcile the 81/48 and 10/51 prose (lines 13, 70, 74, 525, 542, 581) with
  the exact 83/50 companion and 10/52/84 topology only through a governed
  authority amendment; consider whether the Objectives `MappedScopeItems`
  column should be regenerated or labelled as a summary.
- On owner disposition, update SCA-APP-010 `Handoff_State.md` derivative
  fields, disposition SCA-APP-009's own closure, and decide whether this
  snapshot becomes the pointed `_Evaluation/DecompCoverage/_LATEST.md`.

This audit authorizes no application, amendment, repair, pointer movement,
commit, SOW creation, dependency acceptance, implementation, product,
release, or severity change.
