# Decomposition Coverage Report — SCA-APP-010 Post-D-APP-109 Fresh Full Audit

**Overall:** `WARNINGS`
**Closure readiness:** `FAIL`
**Basis:** `f38f1448675b8e9f40f33932a11b7ffa4126fe69` plus the working tree (N8 context alignment and N9 emission, uncommitted)
**Timestamp:** `2026-09-05T08:33:00-06:00`
**Object audited:** the live applied SCA-APP-010 decomposition and companion register against the live filesystem after owner ruling D-APP-109: the fifteen held dependency edges emitted as nineteen cycle-participating non-gating register rows (N9) and the thirteen carriers' `_CONTEXT.md` aligned to the applied rows (N8). SCA-APP-010 is the active snapshot.

Authoritative inputs: decomposition SHA-256
`c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` (content commit
`dbd812a52d5ed0cb3ed173f3aaaa68703a914291`); companion SHA-256
`63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`; both byte-identical to the
0518 run's inputs. `_ScopeChange/_LATEST.md`
(`b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0`) points uniquely to
`execution/_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/`
(`OPEN_PENDING_DERIVATIVE_CLOSURE`). Section binding by normalized heading
text: Objectives line 258, Packages line 275, Deliverables line 292, Scope
Ledger line 398, Coverage and Telemetry line 491, Open Issues line 591 (one
hit each). Comparison basis: the 0518 run `SCA_APP_010_POST_ALIGNMENT` at
`projects/chirality-app-dev/execution/_Evaluation/DecompCoverage/COV_SCA_APP_010_POST_ALIGNMENT_2026-09-05_0518/`
(0 / 72 / 10).

| Check | Verdict | Fresh result |
|---|---|---|
| 1 Package forward coverage | PASS | 10/10 declared packages (`PKG-01`..`PKG-10`, lines 279-288) resolve to exactly one immediate `execution/PKG-XX_*` folder each. |
| 2 Deliverable forward coverage | PASS | 52/52 declared deliverables (rows 298-394) resolve to exactly one `PKG-XX_*/1_Working/DEL-XX-YY_*` folder each; no folder added, removed, or renamed since 0518. |
| 3 Reverse folder coverage | WARNING | `PKG-00_DAG_Closure_and_Project_Control` and `DEL-00-01`, `DEL-00-02` exist with no declaration; 52/54 deliverable folders and 10/11 package folders are declared (96.3 percent). Carried. |
| 4 ID consistency | PASS | No duplicate declared deliverable or scope-item ID, duplicate folder prefix, parentless declaration, or folder-prefix mismatch; every `DEL-XX-YY` is coupled to `PKG-XX`. `DEL-02-02` keeps its ID, package, and folder prefix; its context and register labels equal the applied name. |
| 5 Context fidelity | WARNING | 52/52 `_CONTEXT.md` present. 48 MATCH, 4 PARTIAL (92.3 percent; 0518 was 35 / 17). The thirteen D-APP-109 carriers are MATCH on every field this audit compares: identity table, Package Scope, Deliverable Scope (overlap 1.0), Traceability `CoversScopeItems` and `SupportsObjectives` (equal to the applied row on 13/13), and Anticipated Artifacts (exactly equal to the applied artifacts column on 13/13). PA-010-COV-004 is RESOLVED with no residual. The four carried rows `DEL-04-01`, `DEL-05-01`, `DEL-08-05`, `DEL-09-05` are unchanged. |
| 6 Artifact presence | WARNING | 12/202 anticipated artifacts resolve by the deterministic folder-local filename rule (5.9 percent), identical per row to 0518 and Gate 5; `DEL-01-01` is 5/5. The same fifty IN_PROGRESS rows are warning-level; OPEN `DEL-09-07` is informational. 54/54 `ScopeOfWork.md` validate as `SOW_V1`. One INFO records the pre-existing DEL-05-01 / DEL-05-05 register enum nonconformance (50/52 registers VALID under the full validator), correcting the 0518 statement. |
| 7 Objective mapping | PASS | 10/10 ledger objectives have supporting deliverables with folders (6 to 12 each) and ledger rows (6 to 24 each); no declared deliverable or IN ledger row lacks an objective. Telemetry (lines 493-508) agrees: 84/10/52/10, `UnmappedObjectives 0`. All eight `OpenIssueAffectedScopeCounts` equal the Open Issues rows; OI-008 lists SOW-010, SOW-081, SOW-082, SOW-083 (4) and telemetry says `SHELL_LADDER_BOUNDARY=4`. One INFO on the summary `MappedScopeItems` column (carried). |
| 8 Ledger integrity | PASS | 84 rows: 79 IN, 4 OUT, 1 TBD. Every IN row references an existing package, existing deliverables, and existing objectives; Section 8 `CoversScopeItems` equals the ledger reverse view on all 52 deliverables (0 missing / 0 extra), including SOW-081..084 (lines 484-487). |
| 9 Derivative parity | SKIPPED | Not SOFTWARE-variant-owned. |
| 9b Package shape | WARNING | Companion inventory table present (Section 2.2, lines 62-70). Companion is exact: 18 columns, 83 unique IDs, 50 families, 83/83 `AppDecompositionBasis` cite the live hash, every deliverable and package reference resolves. Prose at lines 70, 525, 542, 581 still says 81 IDs / 48 families and lines 13 and 74 still say 51 deliverables. Carried; byte-identical authority. |
| 10 Active snapshot / handoff | WARNING | `_LATEST.md` resolves uniquely to SCA-APP-010 (60 files, `MANIFEST.sha256` 59/59 OK, required root set complete, `Post_Change_Coverage.json` byte-identical to its audit summary, `Handoff_State.md` byte-identical to the 0518 read). `Handoff_State.md` exposes all seven state fields by name and `ReadyForNextPhase = NO`; no over-claim (handoff-state PASS). The one warning is the carried SCA-APP-008 historical residue; SCA-APP-009's vocabulary and pre-pointer wording are historical INFO; SCA-APP-010's own pre-pointer `RUN_SUMMARY.md` wording and trailing derivative fields are INFO, the under-claim now wider after D-APP-109. |
| 11 Lifecycle | PASS | 51 IN_PROGRESS, 1 OPEN (`DEL-09-07`); 52 statuses read, 51 paired `MEMORY.md` read; `DEL-09-07` has none. The thirteen carriers' `Current State`, `Checking Approval SHA`, and `Remaining` are byte-identical to HEAD; each gained exactly one D-APP-109 history line. Unchanged distribution. |
| 12 Baseline comparison | PASS | No new blocker or major versus the 0518 run. Zero new warning occurrences; one warning row of thirteen occurrences resolved (PA-010-COV-004); one informational row added for a pre-existing condition the 0518 run misstated (register enum, 2 occurrences). Occurrence-weighted 0 / 72 / 10 to 0 / 59 / 25. |

## Topology and authority

The applied decomposition is exactly 10 packages, 52 deliverables, 10
objectives, and 84 scope-ledger rows (79 IN / 4 OUT / 1 TBD), with context
envelopes S=9, M=41, L=2, XL=0 and 8 open issues, all equal to the Coverage
and Telemetry table (lines 493-508), the Context Budget QA table, the 10B
topology row (line 577), the Gate-5 audit, and the 0518 run. Neither the
decomposition nor the companion changed a byte between the 0518 run and this
one; D-APP-109 authorizes no authority write and none occurred. The authority
corpus is v20 with every member `MATCH` and `no drift`.

## Filesystem

All 54 immediate deliverable folders carry `_CONTEXT.md` and `_STATUS.md`.
Since the 0518 basis (`d66395d1` plus the N3 register writes, since committed
as `f38f1448`) the working tree adds exactly the D-APP-109 writes: the
thirteen carriers' `_CONTEXT.md`, `_STATUS.md`, and `MEMORY.md` (N8; 39
files whose pre-images equal the `f38f1448` blobs and whose post-images equal
`Evidence/context_fix/post_images.json`, 39/39 each), the nine holding
carriers' `Dependencies.csv` and `_DEPENDENCIES.md` (N9; 18 files), nine
untracked TASK run records, the D-APP-109 ruling and its register row, and
run-packet evidence. No `ScopeOfWork.md`, `_REFERENCES.md`, product, kit, or
Root byte changed. `PKG-00` and `DEL-00-01/02` remain undeclared control-plane
folders (IN_PROGRESS, with context, status, MEMORY, and valid SOW_V1).

## Check 5 detail

The thirteen D-APP-109 carriers (PD-010-COV-004; PA-010-COV-004 resolved).
Each of the five surfaces the 0518 run found lagging is now equal to the
applied row, mechanically and by reading:

- Traceability `CoversScopeItems` equals the applied row's scope refs on
  13/13. The nine tables named as stale at 0518 now carry the amended items:
  `DEL-02-02` reads SOW-006, SOW-081, SOW-082; `DEL-03-02` carries SOW-083;
  `DEL-04-04` SOW-081 and SOW-084; `DEL-05-02` SOW-082; `DEL-06-03` SOW-082;
  `DEL-07-01` SOW-084; `DEL-07-03` SOW-081; `DEL-08-01` SOW-082 and SOW-084;
  `DEL-08-04` SOW-083. `SupportsObjectives` equals the applied objectives on
  13/13.
- The Anticipated Artifacts paragraph equals the applied artifacts column
  exactly (whitespace-normalized) on 13/13; the ten paragraphs named as stale
  at 0518 are replaced (`DEL-02-02` now lists the Who is working view,
  Workflows view, roadmap and forms, proposal card, role-entry controls, the
  exact posture labels, provenance labels, and the label and query
  compatibility tests; `DEL-08-03` no longer lists contextual-consumer tests).
- The three PKG-02 Source Authority paragraphs (`DEL-02-01`, `DEL-02-02`,
  `DEL-02-04`) state that SCA-APP-010 (applied at Gate 5, D-APP-108) controls
  the current presentation target through the applied row line and the
  `ScopeOfWork.md` Gate-5 section, with SCA-APP-004 and its amendment as dated
  history; the old "prospectively control" sentence is absent from all
  thirteen. `DEL-02-02`'s paragraph adds that the Who is working view, the
  Workflows view, and the proposal card present accepted state and never
  infer enforcement. `DEL-02-05` never carried the SCA-APP-004 sentence and
  is unchanged there.
- `DEL-08-03`'s section is retitled `Ownership Boundary (SCA-APP-004 as
  amended by SCA-APP-010)` and its `DEL-02-02` bullet names the right-panel
  views of applied row L308 and the DEC-025 retirement of the contextual
  Pipeline presentation; the old re-hosted Workbench/Pipeline sentence is
  gone.
- Identity tables, Package Scope, Deliverable Scope (overlap 1.0 on 13/13),
  and `ContextEnvelopeNotes` are byte-identical to PR #713. Each `_STATUS.md`
  gained exactly one D-APP-109 history line (Current State, Checking
  Approval SHA, and Remaining unchanged) and each `MEMORY.md` one appended
  line.

Under the Gate-5 PARTIAL rule (PD-010-006) all thirteen are MATCH. No
residual remains from PA-010-COV-004; nothing is routed to the owner from
these carriers by this audit.

`DEL-02-02` (PD-010-COV-005). The applied name is carried by `_CONTEXT.md`,
`ScopeOfWork.md`, the `_STATUS.md` history, and every register row. The
physical folder keeps its prior label by design (A015, no relocation), with
no ID effect; the Task Management registers cite `DEL-02-02` by ID only.

Four carried rows (PD-010-COV-003) are unchanged since Gate 5 (empty git diff
against `f38f1448`): `DEL-04-01` (Traceability still SOW-018, SOW-044,
SOW-046 / OBJ-004 against SOW-018, SOW-044, SOW-046, SOW-079 / OBJ-002,
OBJ-004), `DEL-05-01`, `DEL-08-05`, `DEL-09-05`. D-APP-109 did not name them.
The two label observations (`DEL-02-03` PackageName, `DEL-09-07`
Discipline) remain INFO.

## Thirteen registers after emission

Every `Dependencies.csv` and `_DEPENDENCIES.md` hashes exactly to the sealed
brief (26/26); the four carriers without held rows are byte-identical to
HEAD. `validate_dependencies_schema.py` returns VALID for all thirteen (206
rows: 187 at `f38f1448` plus the nineteen emitted rows) and for 50 of the 52
declared registers; `RegisterSchemaVersion` v3.1, `FromDeliverableID` equal
to the carrier, and `FromDeliverableName` equal to the applied row name on
every row; exactly one ACTIVE `IMPLEMENTS_NODE` per register. Every applied
`CoversScopeItems` and `SupportsObjectives` value, including SOW-081..084 on
every carrier the ledger maps them to, is anchored by an ACTIVE anchor row
citing the applied decomposition file, and every `#Lnnn` or `:nnn` anchor
pointer resolves to a line carrying the anchored ID; `DEL-02-02`'s SOW-007
anchor is RETIRED. The nineteen emitted rows (`DEP-02-01-010`;
`DEP-02-02-015/017/018/019/020/022`; `DEP-02-04-015..019`;
`DEP-02-05-014/015`; `DEP-03-02-013`; `DEP-05-02-016`; `DEP-06-03-014`;
`DEP-08-01-018`; `DEP-08-04-013`) are each present once, ACTIVE, equal as a
set to `HELD_EDGE_PROPOSALS.csv`, and carry the `EMITTED 2026-09-05 under
D-APP-109 (H-nnn)` and `CYCLE_PARTICIPATING` non-gating clause. The
pre-existing `DEL-08-01` `DEP-08-01-013` absolute Root path is unchanged and
is AUDIT_DEP_CLOSURE's finding. The post-emission graph picture (a
twenty-node SCC and a two-node SCC per `Evidence/fanin_simulation_v1/` and
`REVIEW_v1.2.md`) is recorded here as context only; N11-AUDIT-DEP-CLOSURE
owns that verdict.

The full validator rejects `DEL-05-01` and `DEL-05-05` on legacy `TargetType`
values `CODE` and `DECISION` (four rows). Both files are byte-identical to the
basis, outside the thirteen carriers, already WARNING DC-007 / DC-008 in the
closure audit and repair-first candidates in the run `HANDOFF_STATE.md`. The
0518 run's "52/52 declared registers v3.1 VALID" matches only the closure
audit's shape-level count; this run records the correction as INFO
PD-010-COV-017 and raises no new blocker or major on it.

## Check 10 detail

SCA-APP-010 is the active snapshot: root complete, manifest 59/59 OK,
`Handoff_State.md` truthful, field-complete, and byte-identical to the 0518
read, `ReadyForNextPhase = NO`. `RUN_SUMMARY.md` retains pre-pointer wording
superseded by the G5-POINTER decision and the handoff state, and
`DerivativePackageState = INCOMPLETE` / `MetadataAlignmentState =
NOT_STARTED` now trail the working tree on every count (carriers aligned by
PR #713 and D-APP-109; registers refreshed and the held rows emitted); the
frozen snapshot is not mutated by later evidence and the owner updates the
fields on disposition (run `HANDOFF_STATE.md` slate item 7). SCA-APP-009 is
complete and historical (INFO); SCA-APP-008 still lacks six required
artifacts (WARNING, carried). `_Evaluation/DecompCoverage/_LATEST.md` still
names the SCA-APP-006 run and is not moved by this run (INFO).

## Comparison with the 0518 run

| Measure | 0518 (d66395d1 + N3 registers) | This run (f38f1448 + N8/N9 working tree) |
|---|---|---|
| Topology | 10 / 52 / 84 (79/4/1), S9 M41 L2 XL0, 8 OI | identical (authority byte-identical) |
| Companion | 83 / 50 / 18, pins `c7c05169` | identical |
| Forward / reverse coverage | 100 / 96.3 | identical |
| Reverse-view parity, duplicate IDs, dangling refs | 0 / 0 / 0 | 0 / 0 / 0 |
| Context fidelity | 35 MATCH, 17 PARTIAL (67.3) | 48 MATCH, 4 PARTIAL (92.3); thirteen carriers MATCH |
| PA-010-COV-004 | WARNING, 13 occurrences | RESOLVED; INFO resolution record |
| Artifact presence | 12/202 (5.9) | identical per row |
| Lifecycle / SOW / MEMORY | 51+1, 54/54 SOW_V1, 51 MEMORY | identical |
| Thirteen registers | 13/13 hash-exact, VALID, anchored; held rows not emitted | 13/13 hash-exact to the new identities, VALID, anchored; nineteen rows emitted and marked |
| All-register validity | stated 52/52 | 50/52 under the full validator (DEL-05-01, DEL-05-05 pre-existing; INFO) |
| Active snapshot / pointer | SCA-APP-010, `b297f43e` | identical; under-claim wider |
| Blocker / warning / info | 0 / 72 / 10 | 0 / 59 / 25 |
| Overall / closure | WARNINGS / FAIL | WARNINGS / FAIL |

Occurrence-weighted movement: no new warning occurrence and no new blocker
or major. Thirteen occurrences leave the warning class because PA-010-COV-004
is resolved by the D-APP-109 context alignment; they reappear as the
thirteen-occurrence INFO resolution record PD-010-COV-004. Two INFO
occurrences are added for the pre-existing DEL-05-01 / DEL-05-05 register
enum nonconformance (PD-010-COV-017), a correction of the 0518 statement, not
a change in the filesystem. Every other row is carried unchanged in class and
count; PD-010-COV-015 carries updated content (the SCA-APP-010 under-claim).

## What to fix for a cleaner rerun

- Align the four carried PARTIAL contexts and the `DEL-04-01` Traceability
  table through WORKING_ITEMS under an owner authorization; refresh the
  `DEL-02-03` PackageName and `DEL-09-07` Discipline labels.
- Repair the `DEL-05-01` and `DEL-05-05` legacy `TargetType` values under
  the repair-first path the run `HANDOFF_STATE.md` names (a register write,
  not a decomposition write).
- Reconcile the 81/48 and 10/51 prose (lines 13, 70, 74, 525, 542, 581) with
  the exact 83/50 companion and 10/52/84 topology only through a governed
  authority amendment; consider whether the Objectives `MappedScopeItems`
  column should be regenerated or labelled as a summary.
- On owner disposition, update SCA-APP-010 `Handoff_State.md` derivative
  fields, disposition SCA-APP-009's own closure, and decide whether this
  snapshot becomes the pointed `_Evaluation/DecompCoverage/_LATEST.md`.

This audit authorizes no application, amendment, repair, pointer movement,
commit, SOW creation, dependency acceptance, SCC resolution, implementation,
product, release, or severity change.
