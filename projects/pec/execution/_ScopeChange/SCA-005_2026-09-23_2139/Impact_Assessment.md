---
amendment_id: SCA-005
doc_kind: scope_change.impact_assessment
decomp_variant: SOFTWARE
checkpoint_group: 1
created: 2026-09-23
status: awaiting_checkpoint_1_acceptance
authority: D-PEC-86 §3 I-1..I-3 (owner direction 2026-09-23 opened Gate 1); checkpoint group 1 NOT accepted
workflow: chirality-root:bundled:workflow:scope-change
---

# SCA-005 — Checkpoint-group-1 Impact Assessment

> **Status: PROPOSED, awaiting owner acceptance.** This document proposes a
> change set and states its impact. It changes no decomposition byte,
> register, pointer, PRD, Scope of Work, `_CONTEXT.md`, `_STATUS.md`,
> `v2/**` or foreign surface. The owner accepts it, if at all, by the exact
> SHA-256 of this file as quoted in `Decision_Log.md` and the run return (a
> file cannot quote its own hash). Nothing here is a ruling.

Abbreviations: **DN** = `SCA-005_PREP_2026-09-23/FEED_MODEL_V2_DESIGN_NOTE.md`
(A4); **A1** = `SURVEY_SISTER_LOOP_FILE_TRUTH.md`; **A2** / **INV-###** =
`IMPACT_INVENTORY_PEC_BASIS.{md,csv}`; **Seq n** = row n of
`Amendment_Actions.csv` in this snapshot; **SB-PENDING** = a supersession
binding against PRD v2.2 will be required at checkpoint 2 unless the PRD
successor lands first (CP1-D79).

## 1. Impact verdict

SCA-005 is a **contract-affecting but topology-preserving** amendment. It
re-bases PEC's feed model on the 2026-09-22 shared development-loop method
(Markdown work graphs, central per-undertaking receipts, MEMORY run index,
retired `## Remaining`/workplans, evergreen `LOOP_INIT`) and on the D-GOV-43
A2 Runtime topology (no per-user daemon; one private Runtime per application).
In the recommended set (**O-B2 + P-β/R1 + ADD-new-DEL + Q6 re-express**) it:

- keeps all 11 packages and all 6 objectives, and preserves every existing
  stable ID (`ALLOW_RENUMBERING = false`);
- adds 2 scope items (`SOW-095`, `SOW-096`) and 2 deliverables
  (`DEL-02-08`, `DEL-02-09`) in PKG-02, both parser slices of the existing
  artifact kind;
- moves 3 IN scope items (`SOW-029`, `SOW-035`, `SOW-087`) to Deferred OUT
  behind an explicit trigger and retires their 3 OPEN, SOW-less deliverables
  (`DEL-06-04`, `DEL-07-02`, `DEL-07-05`) non-destructively;
- modifies statements/notes of 19 other scope items (one, SOW-058, conditional on Q9), 13 deliverable rows, 4
  packages, 2 constraints, 4 open issues, 3 objective views and 2 vocabulary
  terms, and adds 4 vocabulary terms;
- carries the nine TM-PEC-023 objective blanks as owner-selectable candidate
  MODIFYs with **no option pre-selected**;
- records the PRD successor candidate and the adopted-not-applied D-PEC-79
  §16.3 postimage as **product-authority inputs outside the decomposition**,
  whose application needs the owner's checkpoint-2 acceptance.

Its main cost is derivative currency: 24 of 32 Scope of Work contracts,
the accepted DEL-00-01 ADRs and DEL-00-03 SPEC, every `_REFERENCES.md` and
`_CONTEXT.md` provenance block, several dependency registers, the PRD, and
a later D-PEC source packet for the registry schema. None of that is
executed or authorized here.

Checkpoint group 1 is **not accepted** by this document.

## 2. Evidence basis

| Evidence | SHA-256 / result |
|---|---|
| Brief B1 (with both addenda) | `126f8c951307c49a84d4e8811f67364aa52e403c2ebf3418950f0c0ff139819e` |
| D-PEC-86 packet | `7cc4dd0f9065f9a79e554aae6ddad5dfdb631a28556585e8d04a7e6a6bdb682b` |
| `SUPPLIED_BASIS.json` | `d59821be6a0e3f3ccecb375344307c4d151a50ca7be7b84a18c68118a9b14354` |
| SOFTWARE_DECOMP revision 1.4 | `7cca5cdbb1ba4bd866391abf00998bc80f587a23505a6f5b6bceb8df48b65c81` (matches supplied basis and `_Decomposition/_LATEST.md`) |
| `ScopeLedger.csv` | `2103afa279bc7df8e75f830326462d7575cf69a403ee7ef07880e0e9fe969e25` (match) |
| `Deliverables.csv` | `49f904488a7402e2124359b59b2fc0df9103bef39ee53a5ce8b74f7dc6cc6b72` (match) |
| `ContextBudgetQA.csv` / `Companion_Inventory.csv` | `5c8d3099…2bef` / `18793e15…ec23` (unchanged since SCA-004) |
| PRD v2.2 live | `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba` (match; equals D-PEC-79 preimage) |
| D-PEC-79 postimage | `92627ee1d384dd8ef0f2db5d63362ec54eee9da30794b9c2d776bd46fb20f5b0` (match) |
| TM-PEC-023 `DECISION_SURFACE.md` | `3a61a24db9a0c5019302588831e5245e5c9436ef03b9e4595ea70615941071ef` (match) |
| A1 survey / manifest | `ec3301c4…2ddb` / `4f84cde1…521c` (recomputed; match addendum 2) |
| A2 inventory CSV (201 rows) / MD | `f0bba13a…e3bc` / `b0ff8359…0484` (recomputed; match) |
| DN (A4) | `4b9ccb9f3e96e66a9566479858deac42f5616315045542ba1b5663fef30d12da` (recomputed; match) |
| D-PEC-78 | `3f91ea6a18360d950f3cecce755ee929cdc78c53651d0b2774a3c93aa290a565` |
| Pre-change audit | `_Evaluation/DecompCoverage/COV_SCA005_PRECHANGE_2026-09-23_2139/`, `coverage_summary.json` `61163c96924e6dfb1f3fa6d1449b523c7280e808c92005cc77d64096858b5d9f` = this snapshot's `Pre_Change_Coverage.json` (byte-identical, `cmp`) |
| Audit result | `WARNINGS`: 0 blockers / 3 warnings / 69 info; 11/11 packages, 64/64 deliverables and contexts; 94 ledger rows (72/14/8); lifecycle 32 OPEN / 26 INITIALIZED / 4 CHECKING / 2 IN_PROGRESS; contracts 32 SOW_V1 / 32 none |
| Strict register validator (before) | 64 registers / 255 dependency rows (136 ANCHOR + 119 EXECUTION) / 0 errors / 0 warnings, exit 0 |
| Reliance-hold preflight | `ALLOW` for `SOFTWARE_DECOMP.md`, `ScopeLedger.csv`, `Deliverables.csv`, `docs/PRD.md` and this snapshot, operation `exact-correction-preparation`; register has no rows |

The three audit warnings are lifecycle-driven artifact-location findings
(DEL-01-03 and DEL-01-05 now `IN_PROGRESS` with bytes under `projects/pec/v2/`;
DEL-08-02 unchanged). None arises from decomposition drift: the package bytes
equal the SCA-004 postimage. The audit also reports that both `_LATEST.md`
pointers still say metadata alignment `NOT_STARTED` although provenance is on
revision 1.4 for all 64 contexts (conservative, not overclaiming).

## 3. Parsed change set and part-A validation

`Amendment_Actions.csv` holds **76 PROPOSED actions** (every Description is
prefixed `PROPOSED`; `SupersessionBindingPresent = NO` for all rows because
no `Supersession_Delta.csv` exists before checkpoint 2 — candidate bindings
are listed in §8.3).

| By ActionType | Count | | By EntityType | Count |
|---|---:|---|---|---:|
| ADD | 8 | | DELIVERABLE | 27 |
| MODIFY | 65 | | OTHER (scope items, constraints, OIs, sections, PRD inputs) | 36 |
| REMOVE | 3 | | VOCAB_TERM | 6 |
| RECLASSIFY / MERGE / SPLIT | 0 | | PACKAGE | 4 |
| | | | OBJECTIVE | 3 |

Cross-tab: ADD 2 DELIVERABLE / 2 OTHER (SOW) / 4 VOCAB_TERM; MODIFY 22
DELIVERABLE (13 description/notes rows + 9 TM-PEC-023 carry-ins) / 34 OTHER /
4 PACKAGE / 3 OBJECTIVE / 2 VOCAB_TERM; REMOVE 3 DELIVERABLE.

| Group | Seq | Content | Driving owner question |
|---|---|---|---|
| F — feed model | 1–25 | entity model, orientation, SOW-013..017, new SOW-095/096 and DEL-02-08/09, registry feed profiles (SOW-077/094, DEL-01-06), parser DEL rows, DEL-03-03, DEL-04-01, PKG-02, §1.2, R4 | Q1, Q2, Q4, Q7, Q8, CP1-X, CP1-V |
| P — presence/streams | 26–45 | C13, C5, SOW-026/029/034/035/049/087/074/092, three REMOVEs, DEL-06-01/09-05/00-02/08-01, PKG-00/06/07 | Q3, CP1-R |
| Q6 — §16 TBDs | 46–53 | SOW-076/080/082/083 and OI-002/006/008/009 re-expressed, still open | Q6 |
| V — vocabulary | 54–59 | `loop`, `harness` MODIFY; `work graph`, `receipt`, `feed profile`, `declared activity` ADD | Q1, Q3 |
| O/T — objectives, carry-ins, traceability | 60–76 | OBJ-001/002/003 views; nine TM-PEC-023 rows; SOW-058 (conditional on Q9); telemetry; SCA-005 traceability; PRD successor candidate; D-PEC-79 | CP1-TM, Q9, CP1-D79 |

**Part-A validation** (deterministic script over live registers; per-action
table in Annex A): 76/76 PASS — every MODIFY/REMOVE target exists; ADD IDs
`SOW-095`, `SOW-096`, `DEL-02-08`, `DEL-02-09` are unused, well-formed and
append-only after `SOW-094`/`DEL-02-07`; their parent `PKG-02` exists and
each new scope item is co-added with its covering deliverable; the four new
vocabulary terms are absent from §9 and the two modified ones present; every
`AffectedFiles` path exists; every cited `INV-###` exists in A2; enums and
columns match the contract. `AMENDMENT_ID = SCA-005` is free in PEC's
`_ScopeChange/` (folders SCA-001..SCA-004 before this snapshot; the zsh
helper, run after the folder existed, reports `SCA-006` as next). A1 DR-18
applies: `SCA-005` also names Root and App/Piping amendments, so cross-loop
readers must qualify it as PEC's.

**Contract-type corrections to the inventory.** A2 labels SOW-076/080/082
and OI-002/006/008 `RECLASSIFY` (INV-061..063, 074..076, 095..097). The
contract reserves `RECLASSIFY` for a parent-partition change; TBD rows and
open issues have no parent, so the recommended re-expression is `MODIFY`
(Seq 46–52). Under the Q6 "retire as moot" alternative they would still be
`MODIFY` (status TBD→OUT, issue resolved), matching the SCA-004 precedent
that treated TBD→IN plus package assignment as `MODIFY`. Likewise the IN→OUT
Deferred moves (Seq 29–31) are `MODIFY` of the scope row, with the orphaned
deliverables handled by explicit `REMOVE` rows (Seq 34–36).

**Parent-closure and variant-local rules.**

- No package is removed, merged, split or reclassified. PKG-06 keeps 5 and
  PKG-07 keeps 3 active children after the retirements; no IN scope item is
  left without package or deliverable (SOW-029/035/087 leave IN in the same
  amendment as their deliverables retire).
- Package-discipline isolation (DL-3, DL-12): both new deliverables are
  read-side grammar slices in PKG-02 of type `BACKEND_FEATURE_SLICE`, write
  nothing and consume no other package's internals.
- Artifact-kind granularity: one parser + fixtures per deliverable, as for
  DEL-02-01..07.
- DL-4 one-feed-kind-per-item: work graphs and MEMORY run index are new feed
  kinds (new SOW IDs); the central `RECEIPT.md` is a second grammar of the
  existing Receipt feed kind and stays in SOW-013 (as per-loop ledger
  grammars already do). The alternative is priced in §12.
- Context envelopes: no deliverable reaches XL; L stays at 2 (DEL-01-01,
  DEL-02-03) with named split lines; see §8.2.

## 4. Impact summary by action

| Seq | Action | Entity | Decomposition sections | Variant-local metadata (propagation) | Downstream reruns |
|---:|---|---|---|---|---|
| 1 | MODIFY OTHER | `SOW-001` | §2 SSOW row + `ScopeLedger.csv` row | — | AUDIT_DECOMP, WORKING_ITEMS, PROJECT_SETUP |
| 2 | MODIFY OTHER | `SOW-004` | §2 SSOW row + `ScopeLedger.csv` row | — | AUDIT_DECOMP, WORKING_ITEMS, PROJECT_SETUP |
| 3 | MODIFY OTHER | `SOW-013` | §2 SSOW row + `ScopeLedger.csv` row | — | AUDIT_DECOMP, WORKING_ITEMS, PROJECT_SETUP |
| 4 | MODIFY OTHER | `SOW-014` | §2 SSOW row + `ScopeLedger.csv` row | — | AUDIT_DECOMP, WORKING_ITEMS, PROJECT_SETUP |
| 5 | MODIFY OTHER | `SOW-015` | §2 SSOW row + `ScopeLedger.csv` row | — | AUDIT_DECOMP, WORKING_ITEMS, PROJECT_SETUP |
| 6 | MODIFY OTHER | `SOW-016` | §2 SSOW row + `ScopeLedger.csv` row | — | AUDIT_DECOMP, WORKING_ITEMS, PROJECT_SETUP |
| 7 | MODIFY OTHER | `SOW-017` | §2 SSOW row + `ScopeLedger.csv` row | — | AUDIT_DECOMP, WORKING_ITEMS, PROJECT_SETUP |
| 8 | ADD OTHER | `SOW-095` | §2 SSOW row + `ScopeLedger.csv` row | — | AUDIT_DECOMP, PROJECT_SETUP, WORKING_ITEMS, dependency-extract |
| 9 | ADD OTHER | `SOW-096` | §2 SSOW row + `ScopeLedger.csv` row | — | AUDIT_DECOMP, PROJECT_SETUP, WORKING_ITEMS, dependency-extract |
| 10 | MODIFY OTHER | `SOW-077` | §2 SSOW row + `ScopeLedger.csv` row | — | AUDIT_DECOMP, WORKING_ITEMS, PROJECT_SETUP |
| 11 | MODIFY OTHER | `SOW-094` | §2 SSOW row + `ScopeLedger.csv` row | — | AUDIT_DECOMP, WORKING_ITEMS |
| 12 | MODIFY DELIVERABLE | `DEL-01-01` | §5 table + `Deliverables.csv` row + `ContextBudgetQA.csv` | `DEL-01-01/_CONTEXT.md` | AUDIT_DECOMP, PROJECT_SETUP, WORKING_ITEMS |
| 13 | MODIFY DELIVERABLE | `DEL-01-06` | §5 table + `Deliverables.csv` row | `DEL-01-06/_CONTEXT.md` | AUDIT_DECOMP, PROJECT_SETUP, WORKING_ITEMS |
| 14 | MODIFY DELIVERABLE | `DEL-02-03` | §5 table + `Deliverables.csv` row + `ContextBudgetQA.csv` | `DEL-02-03/_CONTEXT.md` | AUDIT_DECOMP, PROJECT_SETUP, WORKING_ITEMS |
| 15 | MODIFY DELIVERABLE | `DEL-02-04` | §5 table + `Deliverables.csv` row | `DEL-02-04/_CONTEXT.md` | AUDIT_DECOMP, PROJECT_SETUP, WORKING_ITEMS |
| 16 | MODIFY DELIVERABLE | `DEL-02-05` | §5 table + `Deliverables.csv` row | `DEL-02-05/_CONTEXT.md` | AUDIT_DECOMP, PROJECT_SETUP, WORKING_ITEMS |
| 17 | MODIFY DELIVERABLE | `DEL-02-06` | §5 table + `Deliverables.csv` row + `ContextBudgetQA.csv` | `DEL-02-06/_CONTEXT.md` | AUDIT_DECOMP, PROJECT_SETUP, WORKING_ITEMS |
| 18 | MODIFY DELIVERABLE | `DEL-02-07` | §5 table + `Deliverables.csv` row | `DEL-02-07/_CONTEXT.md` | AUDIT_DECOMP, PROJECT_SETUP, WORKING_ITEMS, dependency-extract |
| 19 | ADD DELIVERABLE | `DEL-02-08` | §5 table + `Deliverables.csv` row + `ContextBudgetQA.csv` | — | AUDIT_DECOMP, PROJECT_SETUP, dependency-extract, WORKING_ITEMS |
| 20 | ADD DELIVERABLE | `DEL-02-09` | §5 table + `Deliverables.csv` row + `ContextBudgetQA.csv` | — | AUDIT_DECOMP, PROJECT_SETUP, dependency-extract, WORKING_ITEMS |
| 21 | MODIFY DELIVERABLE | `DEL-03-03` | §5 table + `Deliverables.csv` row | `DEL-03-03/_CONTEXT.md` | AUDIT_DECOMP, PROJECT_SETUP, WORKING_ITEMS |
| 22 | MODIFY DELIVERABLE | `DEL-04-01` | §5 table + `Deliverables.csv` row | `DEL-04-01/_CONTEXT.md` | AUDIT_DECOMP, PROJECT_SETUP, WORKING_ITEMS |
| 23 | MODIFY PACKAGE | `PKG-02` | §4 Packages row | — | AUDIT_DECOMP, WORKING_ITEMS |
| 24 | MODIFY OTHER | `S1.2-intake-summary` | §1.2 Intake summary | — | AUDIT_DECOMP |
| 25 | MODIFY OTHER | `R4` | §1.5 References | — | AUDIT_DECOMP |
| 26 | MODIFY OTHER | `C13` | §1.3 Hard constraints | — | AUDIT_DECOMP, WORKING_ITEMS |
| 27 | MODIFY OTHER | `C5` | §1.3 Hard constraints | — | AUDIT_DECOMP |
| 28 | MODIFY OTHER | `SOW-026` | §2 SSOW row + `ScopeLedger.csv` row | — | AUDIT_DECOMP, WORKING_ITEMS |
| 29 | MODIFY OTHER | `SOW-029` | §2 SSOW row + `ScopeLedger.csv` row | — | AUDIT_DECOMP, WORKING_ITEMS |
| 30 | MODIFY OTHER | `SOW-035` | §2 SSOW row + `ScopeLedger.csv` row | — | AUDIT_DECOMP, WORKING_ITEMS |
| 31 | MODIFY OTHER | `SOW-087` | §2 SSOW row + `ScopeLedger.csv` row | — | AUDIT_DECOMP, WORKING_ITEMS |
| 32 | MODIFY OTHER | `SOW-034` | §2 SSOW row + `ScopeLedger.csv` row | — | AUDIT_DECOMP, WORKING_ITEMS |
| 33 | MODIFY OTHER | `SOW-049` | §2 SSOW row + `ScopeLedger.csv` row | — | AUDIT_DECOMP, WORKING_ITEMS |
| 34 | REMOVE DELIVERABLE | `DEL-06-04` | §5 table + `Deliverables.csv` row + `ContextBudgetQA.csv` | `DEL-06-04/_STATUS.md` | AUDIT_DECOMP, PROJECT_SETUP, dependency-extract — **surviving dependant: DEL-09-05 `DEP-09-05-005` (EXECUTION / UPSTREAM / PREREQUISITE → DEL-06-04, ACTIVE) must be retired with this action (§8.1)**; own outgoing rows DEP-06-04-003..006 retire with the register |
| 35 | REMOVE DELIVERABLE | `DEL-07-02` | §5 table + `Deliverables.csv` row + `ContextBudgetQA.csv` | `DEL-07-02/_STATUS.md` | AUDIT_DECOMP, PROJECT_SETUP, dependency-extract — only incoming row is DEP-06-04-005 from the also-retired DEL-06-04; own outgoing DEP-07-02-003/004 retire with the register |
| 36 | REMOVE DELIVERABLE | `DEL-07-05` | §5 table + `Deliverables.csv` row + `ContextBudgetQA.csv` | `DEL-07-05/_STATUS.md` | AUDIT_DECOMP, PROJECT_SETUP, dependency-extract — no incoming row; own outgoing DEP-07-05-003/005 retire with the register |
| 37 | MODIFY DELIVERABLE | `DEL-06-01` | §5 table + `Deliverables.csv` row | `DEL-06-01/_CONTEXT.md` | AUDIT_DECOMP, PROJECT_SETUP |
| 38 | MODIFY DELIVERABLE | `DEL-09-05` | §5 table + `Deliverables.csv` row | `DEL-09-05/_CONTEXT.md` | AUDIT_DECOMP, PROJECT_SETUP, dependency-extract (retire `DEP-09-05-005`; refresh `_DEPENDENCIES.md` E-N02 row) |
| 39 | MODIFY DELIVERABLE | `DEL-00-02` | §5 table + `Deliverables.csv` row + `ContextBudgetQA.csv` | `DEL-00-02/_CONTEXT.md` | AUDIT_DECOMP, PROJECT_SETUP |
| 40 | MODIFY DELIVERABLE | `DEL-08-01` | §5 table + `Deliverables.csv` row + `ContextBudgetQA.csv` | `DEL-08-01/_CONTEXT.md` | AUDIT_DECOMP, PROJECT_SETUP, WORKING_ITEMS |
| 41 | MODIFY PACKAGE | `PKG-00` | §4 Packages row | — | AUDIT_DECOMP |
| 42 | MODIFY PACKAGE | `PKG-06` | §4 Packages row | — | AUDIT_DECOMP |
| 43 | MODIFY PACKAGE | `PKG-07` | §4 Packages row | — | AUDIT_DECOMP |
| 44 | MODIFY OTHER | `SOW-074` | §2 SSOW row + `ScopeLedger.csv` row | — | AUDIT_DECOMP |
| 45 | MODIFY OTHER | `SOW-092` | §2 SSOW row + `ScopeLedger.csv` row | — | AUDIT_DECOMP |
| 46 | MODIFY OTHER | `SOW-076` | §2 SSOW row + `ScopeLedger.csv` row | — | AUDIT_DECOMP |
| 47 | MODIFY OTHER | `SOW-080` | §2 SSOW row + `ScopeLedger.csv` row | — | AUDIT_DECOMP |
| 48 | MODIFY OTHER | `SOW-082` | §2 SSOW row + `ScopeLedger.csv` row | — | AUDIT_DECOMP |
| 49 | MODIFY OTHER | `SOW-083` | §2 SSOW row + `ScopeLedger.csv` row | — | AUDIT_DECOMP |
| 50 | MODIFY OTHER | `OI-002` | §10 Open Issues | — | AUDIT_DECOMP |
| 51 | MODIFY OTHER | `OI-006` | §10 Open Issues | — | AUDIT_DECOMP |
| 52 | MODIFY OTHER | `OI-008` | §10 Open Issues | — | AUDIT_DECOMP |
| 53 | MODIFY OTHER | `OI-009` | §10 Open Issues | — | AUDIT_DECOMP |
| 54 | MODIFY VOCAB_TERM | `loop` | §9 Vocabulary Map | — | AUDIT_DECOMP |
| 55 | MODIFY VOCAB_TERM | `harness` | §9 Vocabulary Map | — | AUDIT_DECOMP |
| 56 | ADD VOCAB_TERM | `work graph` | §9 Vocabulary Map | — | AUDIT_DECOMP |
| 57 | ADD VOCAB_TERM | `receipt` | §9 Vocabulary Map | — | AUDIT_DECOMP |
| 58 | ADD VOCAB_TERM | `feed profile` | §9 Vocabulary Map | — | AUDIT_DECOMP |
| 59 | ADD VOCAB_TERM | `declared activity` | §9 Vocabulary Map | — | AUDIT_DECOMP |
| 60 | MODIFY OBJECTIVE | `OBJ-001` | §3 Objectives view | — | AUDIT_DECOMP |
| 61 | MODIFY OBJECTIVE | `OBJ-002` | §3 Objectives view | — | AUDIT_DECOMP |
| 62 | MODIFY OBJECTIVE | `OBJ-003` | §3 Objectives view | — | AUDIT_DECOMP |
| 63 | MODIFY DELIVERABLE | `DEL-00-02` | §5 table + `Deliverables.csv` row | `DEL-00-02/_CONTEXT.md` | AUDIT_DECOMP, PROJECT_SETUP, task-management |
| 64 | MODIFY DELIVERABLE | `DEL-03-05` | §5 table + `Deliverables.csv` row | `DEL-03-05/_CONTEXT.md` | AUDIT_DECOMP, PROJECT_SETUP, task-management |
| 65 | MODIFY DELIVERABLE | `DEL-05-01` | §5 table + `Deliverables.csv` row | `DEL-05-01/_CONTEXT.md` | AUDIT_DECOMP, PROJECT_SETUP, task-management |
| 66 | MODIFY DELIVERABLE | `DEL-07-02` | §5 table + `Deliverables.csv` row | `DEL-07-02/_CONTEXT.md` | AUDIT_DECOMP, PROJECT_SETUP, task-management |
| 67 | MODIFY DELIVERABLE | `DEL-07-03` | §5 table + `Deliverables.csv` row | `DEL-07-03/_CONTEXT.md` | AUDIT_DECOMP, PROJECT_SETUP, task-management |
| 68 | MODIFY DELIVERABLE | `DEL-07-04` | §5 table + `Deliverables.csv` row | `DEL-07-04/_CONTEXT.md` | AUDIT_DECOMP, PROJECT_SETUP, task-management |
| 69 | MODIFY DELIVERABLE | `DEL-07-05` | §5 table + `Deliverables.csv` row | `DEL-07-05/_CONTEXT.md` | AUDIT_DECOMP, PROJECT_SETUP, task-management |
| 70 | MODIFY DELIVERABLE | `DEL-08-05` | §5 table + `Deliverables.csv` row | `DEL-08-05/_CONTEXT.md` | AUDIT_DECOMP, PROJECT_SETUP, task-management |
| 71 | MODIFY DELIVERABLE | `DEL-10-08` | §5 table + `Deliverables.csv` row | `DEL-10-08/_CONTEXT.md` | AUDIT_DECOMP, PROJECT_SETUP, task-management |
| 72 | MODIFY OTHER | `SOW-058` | §2 SSOW row + `ScopeLedger.csv` row | — | AUDIT_DECOMP, WORKING_ITEMS |
| 73 | MODIFY OTHER | `S7-S8-telemetry` | §3 notes, §7, §8 + `ContextBudgetQA.csv` | — | AUDIT_DECOMP |
| 74 | MODIFY OTHER | `SCA-005` | Gate/Decision Log, §12, front matter, pointers | — | AUDIT_DECOMP, HELP_HUMAN |
| 75 | MODIFY OTHER | `PRD-successor-candidate` | outside decomposition: `docs/PRD.md` | — | PRD amendment, HELP_HUMAN |
| 76 | MODIFY OTHER | `D-PEC-79` | outside decomposition: `docs/PRD.md` | — | PRD amendment, HELP_HUMAN |

All authoritative decomposition writes land only after checkpoint-group-2
acceptance of the exact text and propagation plan. "Variant-local metadata"
names `_CONTEXT.md`/`_STATUS.md` files inside the SOFTWARE default
propagation scope; everything else in the last column is handoff work for its
owner.

## 5. Expected decomposition-state delta (recommended set)

| Metric | Pre-change (audit) | Expected post-change | Explanation |
|---|---:|---:|---|
| Scope items | 94 | 96 | +SOW-095, +SOW-096 (append-only) |
| IN / OUT / TBD | 72 / 14 / 8 | 71 / 17 / 8 | +2 IN; SOW-029/035/087 IN→OUT Deferred; TBDs re-expressed, not closed (Q6) |
| Packages | 11 | 11 | no partition change |
| Deliverable rows (active / RETIRED) | 64 (64 / 0) | 66 (63 / 3) | +DEL-02-08/09; DEL-06-04, DEL-07-02, DEL-07-05 retired |
| Objectives | 6 | 6 | views only |
| PKG-02 / PKG-06 / PKG-07 assigned scope | 7 / 7 / 6 | 9 / 6 / 4 | follows the ADD and Deferred-OUT rows |
| IN rows without package / deliverable | 0 / 0 | 0 / 0 | same-amendment assignment and retirement |
| IN rows without objective mapping | 11 | 9 (before TM-PEC-023 selection) | SOW-035 and SOW-087 leave IN; SOW-095/096 enter mapped to OBJ-001;OBJ-002 |
| Active deliverables without SupportsObjectives | 9 | 7 (before selection) | DEL-07-02, DEL-07-05 retire; TM-PEC-023 selection may reduce further |
| Open / resolved issues | 10 / 3 | 10 / 3 | OI-002/006/008/009 re-expressed, still open |
| Context envelopes (active) | S 28 / M 34 / L 2 / XL 0 | S 28 / M 33 / L 2 / XL 0 | +M (DEL-02-08), +S (DEL-02-09), −S (DEL-06-04), −M×2 (DEL-07-02/05) |
| Vocabulary terms | 22 | 26 | +4 ADD, 2 MODIFY |
| Hard constraints | C1–C16 | C1–C16 | C5 citation refresh; C13 owner restated |
| Execution dependency edges / SCCs | 119 / 0 (`analyze_dep_closure.py`: 64 nodes, 0 SCCs, 0 bidirectional pairs) | 110 before new edges; final UNKNOWN until dependency-extract runs | −9 edges touching retired DELs (§8.1); new DEL-02-08/09 edges and DEL-03-01 `[E-P25]` re-point are downstream (§7) |

## 6. Package-role and derivative-surface classification

| Surface | Package role | Classification | Expected state after amendment | Authority / required action |
|---|---|---|---|---|
| `_Decomposition/SOFTWARE_DECOMP.md` | working surface | `DIRECT_EDIT` | `CURRENT` after checkpoint 3 | exact checkpoint-2 text only; revision 1.5, DL-20 |
| `_Decomposition/ScopeLedger.csv` | authoritative companion register | `DIRECT_EDIT` | `CURRENT` after checkpoint 3 | rows for Seq 1–11, 28–33, 44–49 and 72; TM-PEC-023 selections (Seq 63–71); 2 appended rows |
| `_Decomposition/Deliverables.csv` | authoritative companion register | `DIRECT_EDIT` | `CURRENT` after checkpoint 3 | 13 description rows, 2 appended rows, 3 retirement annotations, TM-PEC-023 selections |
| `_Decomposition/ContextBudgetQA.csv` | authoritative companion register | `DIRECT_EDIT` | `CURRENT` after checkpoint 3 | notes for DEL-01-01/02-03/02-06/08-01/00-02; rows for DEL-02-08/09; retired-row annotation |
| `_Decomposition/Companion_Inventory.csv` | authoritative companion register | `RECOMPUTE` | `CURRENT` | row-count descriptions (94→96 scope items; 64→66 deliverable rows) |
| `_Decomposition/_LATEST.md` | snapshot / handoff artifact | `RECOMPUTE` | revision 1.5 only after checkpoint-3 acceptance | never moved at checkpoint 1 or 2 |
| `_ScopeChange/_LATEST.md` | snapshot / handoff artifact | `RECOMPUTE` | names SCA-005 only after checkpoint-3 acceptance | unchanged now (still SCA-004) |
| `_ScopeChange/checkpoint_snapshots/` | snapshot / handoff artifact | `RECOMPUTE` | group-1 decision snapshot created only after owner acceptance | not created by this run |
| this snapshot `SCA-005_2026-09-23_2139/` | snapshot / handoff artifact | `RECOMPUTE` | interim checkpoint-1 package, not active | this run |
| `_Evaluation/DecompCoverage/COV_SCA005_PRECHANGE_…` | derived publication artifact (audit evidence) | `RECOMPUTE` | current pre-change baseline | produced; `_LATEST.md` of DecompCoverage unchanged |
| `_CONTEXT.md` of 13 described deliverables + 9 carry-in rows' deliverables + 3 retired deliverables (union 22 folders; list in §7.2) | variant-local derived metadata | `DIRECT_EDIT` (SOFTWARE default propagation scope) | `CURRENT` after checkpoint 3 | semantic fields + provenance only |
| other `_CONTEXT.md` provenance blocks | variant-local derived metadata | `NO_CHANGE` in SCA pass | `STALE_REPIN_REQUIRED` | PROJECT_SETUP re-pin to revision 1.5 |
| three retired deliverables' `_STATUS.md` | variant-local lifecycle | `DIRECT_EDIT` | `RETIRED` after checkpoint 3 via `tools/scaffolding/write_status.sh … RETIRED WORKING_ITEMS` | folders never deleted; no MEMORY present |
| all other `_STATUS.md` | lifecycle truth | `NO_CHANGE` | `CURRENT_UNCHANGED` | no lifecycle act inferred |
| all `_REFERENCES.md` (64 + 2 new) | derived reference packets | `NO_CHANGE` in SCA pass | `STALE_REPIN_REQUIRED` | PROJECT_SETUP re-pin; 2 new created by preparation |
| `Dependencies.csv` / `_DEPENDENCIES.md` (DEL-03-01, DEL-02-07, DEL-01-06, DEL-09-05 `DEP-09-05-005`, retired DELs and the 8 surviving consumer mirrors named in §8.1, new DELs) | downstream structured dependency truth | `NO_CHANGE` in SCA pass | `STALE_REBUILD_REQUIRED` | dependency-extract / PROJECT_SETUP; rerun strict validator and closure |
| 32 `ScopeOfWork.md` | derived production contracts | `NO_CHANGE` in SCA pass | 24 `STALE_REVIEW_REQUIRED` or `STALE_REBUILD_REQUIRED` (one conditional on Q9); 5 housekeeping-only; 3 current (§7.1) | WORKING_ITEMS SOW currency + REVIEW/owner artifact gates |
| DEL-00-01 `artifacts/v2/ADRs.md` (CHECKING) | accepted derivative artifact | `NO_CHANGE` | `STALE_REVIEW_REQUIRED` (INV-178 carried posture 3) | DEL-00-01 owning workflow + exact-byte gate |
| DEL-00-03 `artifacts/v2/SPEC.md` (CHECKING) | accepted derivative artifact | `NO_CHANGE` | `STALE_REVIEW_REQUIRED` (§4, §6 PKG-07 row, §8) | DEL-00-03 owning workflow + exact-byte gate |
| `docs/PRD.md` v2.2 | upstream product authority (outside decomposition) | `NO_CHANGE` now | successor candidate prepared at checkpoint 2 | PRD amendment workflow; owner acceptance (CP1-D79) |
| `v2/config/loops.json`, `loops.schema.json`, `v2/src/pec_v2/core/ports/loop_registry.py` | source / configuration | `NO_CHANGE` | `STALE_SOURCE_PACKET_REQUIRED` under O-B/O-B2 | later D-PEC source packet naming exact paths (D-PEC-86 §4 opens no `v2/**`) |
| TM-PEC-023 register row | Task Management authority for concern disposition | `NO_CHANGE` | closes `RESOLVED_BY_DECISION` after checkpoint 3 per owner ruling 2026-08-03 1c | task-management workflow |
| `_DomainEngines/profiles/pec.yaml`; sister `adapter.yaml`; `projects/pec/AGENTS.md` §Shared Runtime Boundary | foreign / tier-0 / instruction surfaces | `NO_CHANGE` | route only (§7.4) | owners named in §7.4 |
| Decisions, receipts, prior SCA and audit snapshots, frozen corpus | authority / history / evidence | `NO_CHANGE` | `HISTORICAL_CURRENT` | never rewritten |

## 7. Derivative packages and owning reruns

### 7.1 Scope of Work currency list (WORKING_ITEMS, per deliverable)

Lifecycles are from the pre-change audit and each `_STATUS.md` (sibling
`MEMORY.md` read where present: only DEL-01-03 has one). "Pin" = the
unresolvable `@3623b958b` basis pin (INV-176); "Ref" = the false
"`_REFERENCES.md` still names revision 1.1" claim (INV-177). Both are
**non-scope housekeeping corrections**, listed so they ride the same currency
pass (steer 8).

| DEL | Lifecycle | Inventory rows | SCA-005 cause (recommended set) | Currency class | Pin | Ref |
|---|---|---|---|---|:-:|:-:|
| DEL-00-01 | CHECKING | INV-130, INV-178..181 | C13/D-GOV-43 runtime-ownership premise (CLM-005; ADR carried posture 3) | `STALE_REVIEW_REQUIRED` (SOW and ADR bytes) | | |
| DEL-00-03 | CHECKING | INV-131, INV-132, INV-182..184 | quotations of §1.4/§4 charter; SPEC §4/§6/§8 | `STALE_REVIEW_REQUIRED` (SOW quotations; SPEC) | | |
| DEL-01-01 | INITIALIZED | INV-133..136 | entity model re-sourced (Seq 1, 12) | `STALE_REBUILD_REQUIRED` | ✓ | ✓ |
| DEL-01-03 | IN_PROGRESS | INV-137 | CON-001 quotes stale "pec ledger prose-structured"; content-minimal boundary applies to Markdown feeds | `STALE_REVIEW_REQUIRED` (quotation) | ✓ | |
| DEL-01-04 | INITIALIZED | — | none | housekeeping only | ✓ | |
| DEL-01-05 | IN_PROGRESS | INV-138 | PEC-API-001 citation (D-GOV-20→43) | `STALE_REVIEW_REQUIRED` (quotation) | | |
| DEL-01-06 | INITIALIZED | INV-139, INV-140 | feed-profile declarations, schema v2 obligation, five-loop CLMs (Seq 10, 11, 13) | `STALE_REBUILD_REQUIRED` — a **new** currency obligation; RF-002 stays RESOLVED | | |
| DEL-02-01 | INITIALIZED | INV-141, INV-142 | per-loop optional "remaining items"; PEC-RCN-002 quotation | `STALE_REVIEW_REQUIRED` | ✓ | ✓ |
| DEL-02-02 | INITIALIZED | INV-143 | PEC-RCN-002 quotation only | `STALE_REVIEW_REQUIRED` (quotation) | ✓ | ✓ |
| DEL-02-03 | INITIALIZED | INV-144..148 | central RECEIPT.md grammar; OI-008 re-expressed; six ledgers (Seq 3, 14) | `STALE_REBUILD_REQUIRED` | ✓ | ✓ |
| DEL-02-04 | INITIALIZED | INV-149..151 | historical JSON grammar; daemon referent; CON-003 "no STATUS.json in PEC" false (13 exist) | `STALE_REBUILD_REQUIRED` | ✓ | ✓ |
| DEL-02-05 | INITIALIZED | INV-152..154 | WORK_GRAPH.json historical; `.md` to DEL-02-08 | `STALE_REBUILD_REQUIRED` | ✓ | ✓ |
| DEL-02-06 | INITIALIZED | INV-155..158 | LOOP_INIT identity only; workplans historical; CON-005 false (PEC has LOOP_INIT) | `STALE_REBUILD_REQUIRED` | ✓ | ✓ |
| DEL-02-07 | INITIALIZED | INV-159, INV-160 | re-purposed to parity-peer reader (Q2 b) | `STALE_REBUILD_REQUIRED` | | |
| DEL-03-01 | INITIALIZED | INV-161 | ingest boundary follows feed list; `[E-P25]` manifest edge re-points DEL-02-07→DEL-01-06 | `STALE_REVIEW_REQUIRED` | | |
| DEL-03-02 | INITIALIZED | — | none | housekeeping only | ✓ | ✓ |
| DEL-03-03 | INITIALIZED | — | new lag classes (Seq 21) | `STALE_REVIEW_REQUIRED` (new content) | ✓ | ✓ |
| DEL-03-04 | INITIALIZED | INV-162..164 | stale P1 quotation; TBD-003 parity set (Q10) | `STALE_REVIEW_REQUIRED` | ✓ | ✓ |
| DEL-03-06 | INITIALIZED | — | none | current | | |
| DEL-04-01 | INITIALIZED | INV-165, INV-166 | orientation re-sourced; "newest applicable receipt" ordering (Seq 2, 22) | `STALE_REBUILD_REQUIRED` | | |
| DEL-04-02 | INITIALIZED | — | none | current | | |
| DEL-04-03 | INITIALIZED | INV-167 | feed set for per-feed freshness | `STALE_REVIEW_REQUIRED` | | |
| DEL-04-05 | INITIALIZED | INV-168 | absent/historical ledger becomes normal case | `STALE_REVIEW_REQUIRED` | ✓ | ✓ |
| DEL-08-01 | INITIALIZED | INV-169, INV-170 | OI-006 re-expressed; D-GOV-20 citation | `STALE_REVIEW_REQUIRED` | | |
| DEL-08-02 | CHECKING | — | none | housekeeping only | ✓ | |
| DEL-08-03 | INITIALIZED | INV-171 | SOW-083 quotation | `STALE_REVIEW_REQUIRED` (quotation) | | |
| DEL-08-04 | INITIALIZED | INV-172 | inherits DEL-04-01/08-01 refresh | `STALE_REVIEW_REQUIRED` (quotation) | | |
| DEL-10-01 | CHECKING | INV-173 | Step-0 measured condition; Q9 (conditional Seq 72) | `STALE_REVIEW_REQUIRED` only if Q9 (a) or (c) | | |
| DEL-10-02 | INITIALIZED | — | none | housekeeping only | ✓ | ✓ |
| DEL-10-03 | INITIALIZED | — | none | housekeeping only | ✓ | ✓ |
| DEL-10-10 | INITIALIZED | INV-174, INV-175 | TBD-005 "structurally different loop" (Q5); DEL-02-05 dependency premise | `STALE_REVIEW_REQUIRED` | | |
| DEL-10-11 | INITIALIZED | — | none | current | | |

Totals: 24 SOWs need currency review — the A2 inventory's 23 touched
contracts plus DEL-03-03 (new content, no stale claim); DEL-10-01's review is
conditional on Q9. Five more need only the housekeeping fixes (DEL-01-04,
03-02, 08-02, 10-02, 10-03) and three are current (DEL-03-06, 04-02, 10-11).
Housekeeping totals: 16 pins and 13 reference claims. The two new deliverables receive first SOWs through the
ordinary preparation → Scope of Work path; the three retired deliverables
have none.

### 7.2 Other derivative packages

| Package / exact population | Owner | State after accepted amendment | Required rerun / closure action |
|---|---|---|---|
| `_CONTEXT.md`, 22 semantic folders: DEL-00-02, 01-01, 01-06, 02-03..07, 03-03, 03-05, 04-01, 05-01, 06-01, 06-04, 07-02, 07-03, 07-04, 07-05, 08-01, 08-05, 09-05, 10-08 | SCOPE_CHANGE direct propagation (checkpoint-2 plan) | `DIRECT_EDIT` | mirror the accepted register fields; TM-PEC-023 rows only after selection; retired rows annotated |
| remaining `_CONTEXT.md` provenance blocks (42) + 2 new | PROJECT_SETUP (metadata re-pin; preparation for new) | `STALE_REPIN_REQUIRED` | re-pin to revision 1.5; semantic fields unchanged |
| 66 `_REFERENCES.md` | PROJECT_SETUP / reference owner | `STALE_REPIN_REQUIRED` | re-pin; 2 created for DEL-02-08/09 |
| New folders `PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_*`, `DEL-02-09_*` | PROJECT_SETUP with the source-qualified `preparation` skill | `NOT_CREATED` | `_CONTEXT.md`, `_STATUS.md` (OPEN), `_REFERENCES.md`, `_DEPENDENCIES.md` |
| Dependency registers | dependency-extract / PROJECT_SETUP | `STALE_REBUILD_REQUIRED` | DEL-03-01 `[E-P25]` re-point to DEL-01-06; edges into DEL-02-08/09 (consumers DEL-03-01, DEL-04-01, DEL-01-01 schema); retire non-destructively the surviving dependant row `DEP-09-05-005` (DEL-09-05 → DEL-06-04) and the 8 EXECUTION rows owned by DEL-06-04/07-02/07-05 (§8.1), and refresh 8 consumer mirrors; rerun strict validator and `analyze_dep_closure.py` (expect 0 SCCs) |
| DEL-00-01 ADRs, DEL-00-03 SPEC | owning deliverable workflows + REVIEW/owner exact-byte gates | `STALE_REVIEW_REQUIRED` | amend only the stale premises; accepted bytes remain history |
| PRD v2.2 → successor candidate | PRD amendment workflow; owner | `CANDIDATE_REQUIRED` at checkpoint 2 | Annex B rows; D-PEC-79 path per CP1-D79 |
| Registry source (`loops.schema.json` v2, `loops.json`, `RegisteredLoop`) | later D-PEC source packet; DEL-01-06 | `STALE_SOURCE_PACKET_REQUIRED` (O-B only) | exact paths, VER-001/VER-003 re-run, rollback |
| P1 fixture suites | DEL-02-08/09/03 production under their SOWs | `NOT_STARTED` | pinned golden-by-reference fixtures at `d61981ee2` (§9.3) |
| Post-change audit | TASK `audit-decomp` | `NOT_RUN` | compare with `COV_SCA005_PRECHANGE_2026-09-23_2139` |
| README / docs/STATUS / `_COORDINATION.md` orientation prose | HELP_HUMAN (D-PEC-86 I-5 for present-current refresh) | `STALE_POINTER_OR_MAP_NOTE` after checkpoint 3 | assert no acceptance that did not occur |

### 7.3 Downstream sequence (recommended, none authorized here)

1. Owner accepts or modifies checkpoint group 1; the group-1 decision
   snapshot is written under `_ScopeChange/checkpoint_snapshots/`.
2. Checkpoint-2 package: exact decomposition diff, `Propagation_Plan.md`,
   `Supersession_Delta.csv` (or none if the PRD successor lands first), the
   PRD successor candidate text (D-PEC-79 per CP1-D79), TM-PEC-023 row-by-row
   selections (rows 1/4/7 after Q3).
3. After checkpoint-2 acceptance: apply decomposition + registers + direct
   `_CONTEXT.md`/`_STATUS.md` writes; PRD successor applied under its own
   accepted act; post-change `audit-decomp`; independent review;
   checkpoint 3.
4. After checkpoint-3 acceptance: pointers move; then separately gated
   downstream: PROJECT_SETUP metadata re-pin (contexts, references) and
   preparation of DEL-02-08/09; dependency-extract; WORKING_ITEMS Scope of
   Work currency per DEL (§7.1, including the housekeeping fixes); DEL-00-01
   ADR and DEL-00-03 SPEC amendments; the registry D-PEC source packet; P1
   fixture-suite strategy inside DEL-02-08/09/03 SOWs; TM-PEC-023 closure.
5. PEC loop migration to the shared method stays deferred (D-PEC-86 I-7);
   under O-B2 it later becomes one owner-gated registry row change (Q8).

### 7.4 Surfaces PEC cannot write (route only; steer 7)

| Surface | Stale premise | Owning authority | Route | SCA-005 writes it? |
|---|---|---|---|---|
| `_DomainEngines/profiles/pec.yaml` | header "Candidate only … awaiting owner ruling" vs body `ADOPTED` (INV-200); any runtime client/bridge needs a profile amendment first (INV-201) | tier-0 register (`_DomainEngines/_DECISIONS/`), D-T0-27 owner | tier-0 notice / Task Management row (header housekeeping now; profile amendment only if T-RT ever fires) | No |
| App and Piping `_harness/adapter.yaml` | declare no WorkGraphs, RECEIPT.md, MEMORY or TM surface (A1 DR-07) | App and Piping loops (harness configuration authority) | informational notice only; under O-B2 PEC needs nothing from them | No |
| `projects/pec/AGENTS.md` §Shared Runtime Boundary | "D-GOV-20 … root-owned shared runtime … daemon sole owner" (A2 §9) | PEC instruction surface; instruction change needs its own authorized scope and tranche manifest (Root `AGENTS.md`) | separate instruction-change tranche after checkpoint 3 | No |

## 8. Orphan, invariant and telemetry risk

### 8.1 Structural and register invariants

| Risk | Pre-change evidence | Post-change exposure | Required control |
|---|---|---|---|
| Package orphan | 11/11 found | none: PKG-06 keeps 5, PKG-07 keeps 3 active children | preserve package rows; enumerate child sets in checkpoint-2 diff |
| IN item without package/deliverable | 0 / 0 | 0 if Seq 29–31 and 34–36 land atomically | same-amendment status change + retirement |
| Union invariant `Deliverables.SupportsObjectives = union(ScopeLedger.ObjectiveIDs)` (XRG-005) | holds for all 64 (strict validator 0 findings) | DEL-02-08/09 = OBJ-001;OBJ-002 = union of SOW-095/096 ✓; retired rows must clear SupportsObjectives; each TM-PEC-023 selection must set both registers in lockstep | re-run strict validator on the candidate; checkpoint-2 diff shows both columns per row |
| Reciprocity (XRG-003) / OUT naming deliverables (XRG-007) | 0 findings | retired DELs must clear `CoversScopeItems`; Deferred-OUT rows must clear `DeliverableIDs` | explicit cells in the checkpoint-2 diff |
| Blank PhaseHint (XRG-008) | 0 | retired rows must keep a PhaseHint; new rows need one | keep original PhaseHint; DEL-02-08/09 = P1 (Q5 a) |
| ContextBudgetQA coverage | 64/64 rows | 66 rows needed | append DEL-02-08/09; annotate retired rows |
| Objective supported only by RETIRED units (audit BLOCKER rule) | none | OBJ-003 loses DEL-06-04 only; 10 active supporters remain | none further |
| Validator has no RETIRED concept | — | a retired row is still a register row | UNKNOWN whether `audit-decomp` reverse-coverage flags a zero-coverage retired row; the post-change audit must report it and the checkpoint-2 plan must state the representation (`[RETIRED — SCA-005]` annotation per method) |
| Dependency cycle | 119 edges / 0 SCCs | UNKNOWN until re-extraction | `analyze_dep_closure.py` after dependency-extract |
| **Surviving dependant on a retired deliverable** (method part B REMOVE trace; `analyze_dep_closure.py` + scan of all 64 `Dependencies.csv`) | `DEP-09-05-005`: DEL-09-05 (Presence board, P3) → DEL-06-04 (Live hierarchy edges, P4), EXECUTION / UPSTREAM / PREREQUISITE, `ACTIVE`, evidence ScopeLedger SOW-049, mirrored as `E-N02` (PHASE_TENSION) in DEL-09-05 `_DEPENDENCIES.md`. No surviving register row targets DEL-07-02 or DEL-07-05 | **R1:** a surviving P3 deliverable would keep an ACTIVE prerequisite on a RETIRED node (never satisfiable). **R2:** the edge would point at a deferred (T-RT) node, blocking DEL-09-05 indefinitely | **R1:** dependency-extract retires `DEP-09-05-005` non-destructively (Status RETIRED, note SCA-005) in the same propagation as Seq 34, consistent with Seq 33/38 dropping live hierarchy from the presence board; refresh the `E-N02` mirror. **R2:** with Seq 33/38 as proposed the same retirement applies; only if the owner kept live hierarchy on the board would the row survive, and then it must be reclassified non-blocking or DEL-09-05 re-phased — an owner choice at checkpoint 2 |
| Edges owned by retired registers | DEP-06-04-003..006 (→ DEL-01-02, DEL-06-01, DEL-07-02, DEL-07-03), DEP-07-02-003/004 (→ DEL-00-02, DEL-07-01), DEP-07-05-003/005 (→ DEL-00-02, DEL-01-01): 8 EXECUTION rows plus ANCHOR rows; DEP-06-04-005 is retired→retired | retire with their registers; 119 − 8 − 1 (`DEP-09-05-005`) = 110 edges | consumer mirrors in 8 surviving `_DEPENDENCIES.md` go stale: DEL-00-02 (E-A03, E-N01), DEL-01-01 (E-P14), DEL-01-02 (E-N09), DEL-06-01 (E-N10), DEL-07-01 (E-P48), DEL-07-03 (E-P47), DEL-08-02 (E-N13, already struck through), DEL-09-05 (E-N02); dependency-extract / PROJECT_SETUP refresh them; rerun strict validator and closure (expect 0 SCCs) |
| Package-discipline isolation | PASS (audit) | new DELs are PKG-02 read-side grammars | explicit check recorded at checkpoint 3 |
| Stable identity | all IDs stable | no renumbering; names/paths retained (CP1-N); 4 ADD IDs append-only; retired IDs reserved | confirm at checkpoint 1 |

### 8.2 Context-envelope risk

| Deliverable | Now | Proposed | Risk note |
|---|---|---|---|
| DEL-02-03 | L, MEDIUM | L, MEDIUM | adds the central-receipt grammar; OI-008 variance shrinks (3 ledgers share receipt-contract-v2; App/Piping ledgers historical). Split line: central-receipt grammar → a new deliverable (priced in §12.5) |
| DEL-01-01 | L, MEDIUM | L, MEDIUM | entity set changes shape (−Workplan/Step/Gate as live, +WorkGraph/WorkNode); count stays near 14 |
| DEL-02-06 | M, LOW | M or S (re-assess) | scope narrows to LOOP_INIT identity |
| DEL-02-08 (new) | — | M, LOW–MEDIUM | new grammar, discovery, PR→merge join inputs, three fixture classes |
| DEL-02-09 (new) | — | S, LOW | three observed MEMORY forms |
| DEL-02-04 / DEL-02-05 | S | S | narrowed (historical grammar labels) |

No XL arises; no split-or-accept decision is required.

### 8.3 Supersession and authority-conflict risk

Candidate `Supersession_Delta.csv` rows for checkpoint 2 (none exists now):

| Candidate binding | Superseded authority fact | OverrideType if the PRD successor does **not** land first |
|---|---|---|
| SOW-013/014/015/016/017, SOW-095/096 | PRD v2.2 §9.2 PEC-RCN-002 feed list and manifest clause; §7.1 rows | `SUPERSESSION` |
| SOW-001, SOW-004 | PRD §7.1 entity rows; PEC-ORI-001 | `SUPERSESSION` |
| SOW-026, SOW-029, SOW-035, SOW-049, SOW-087 | PEC-PRS-001/-004, PEC-STR-003, PEC-DSH-005, §13 client-seam row, §12 P4 | `SUPERSESSION` |
| SOW-034, SOW-074, SOW-083 | PEC-STR-002 and §16.9 `runtime/` paths | `SUPERSESSION` (paths) |
| SOW-077 under O-B2 | D-PEC-78 O-A "Schema version 1 remains strict and versioned"; D-PEC-79 §16.3 "strict-version-1" | `SUPPLEMENTARY_EXTENSION` if the owner confirms CP1-V; otherwise `SUPERSESSION` needing an owner ruling |

If the owner adopts the PRD successor before or with checkpoint-2
application, the PRD rows cease to be conflicting authority and only the
D-PEC-78/79 version clause remains to bind.

### 8.4 Observed-fact risks (carried from DN, A1 and the brief addenda)

| # | Fact (evidence) | Risk | Control in the proposed set |
|---|---|---|---|
| R-01 | All three 2026-09-23 trial graphs show `F1 ACTIVE` after their final PRs merged (#868 `10b672cae`, #876 `0b276a7f`, #873 `c56ae4a2`); the method forbids write-back (DN §3.1; A1 DR-04) | reading completion from the cell reports finished undertakings as active | SOW-004 (Q4 a) derives terminal completion from local Git; DEL-03-03 classifies terminal lag as "trailing by method design" |
| R-02 | Run IDs differ from graph folder names in two of three trials (A1 §5.1, §5.3) | path-based joins mis-attribute | SOW-095 joins on the declared run-identity token |
| R-03 | Two of three trials have no `RECEIPT.md`; the DEC-025 run has `EVIDENCE.md`, the App run no AgentRuns record (A1 DR-13; the assessment's overstatement is corrected by HELP_HUMAN's appended note) | fixtures assuming the full shape are wrong; absence misreported as nonconformance | three fixture classes (§9.3); absence is a stated coverage limit (I-15) |
| R-04 | The practitioner harness classifies `RECEIPT.md` as UNCLASSIFIED and does not observe `projects/pec` (DN §4 O-A, §7 item 2) | P1 parity has no counterpart for new surfaces and no census over PEC | Q10 (c): census parity leg moves to P2 with P1 exit wording stating it explained |
| R-05 | PEC's own P1 self-ingest corpus stays old-shape (57 `## Remaining`, ledger, 64 `Dependencies.csv`) for the whole SCA-005 horizon (DN I-16) | P1 exercises almost none of the new feeds | fixtures carry the new grammars; `remaining-loop` profile covers PEC (Q8 a) |
| R-06 | D-PEC-78 "Schema version 1 remains strict" and D-PEC-79 "strict-version-1" (D-PEC-78 L80; postimage L509) | O-B2 needs schema v2 | CP1-V owner confirmation; PRD successor rewording |
| R-07 | DEL-10-01 is CHECKING with an accepted pre-P1 baseline; its SOW requires every capture before the first P1 node (REQ-005, AC-003); P1 nodes are now IN_PROGRESS | DN Q9 (a) would displace an accepted baseline with a post-start measurement | manager recommends Q9 (c): supplementary, separately labelled comparison |
| R-08 | MEMORY `## Runs` has 0 template tables; bullet and dated-heading forms observed (A1 DR-12) | a table-only grammar misses all current data | SOW-096 covers all three forms |
| R-09 | Name-based discovery over-selects (53 `WORK_GRAPH.md`, 3 canonical; A1 DR-16) | false undertakings | discovery by declared feed profile and canonical path |
| R-10 | Content-minimality of extracting PR numbers and state tokens from graph cells (A1 open question 1) | PEC-K-10 breach if prose leaks | SOW-095 extracts only identifiers and closed-vocabulary tokens (DN §3.2); golden tests assert no source-text runs (DN §6 item 3) |
| R-11 | Bridge has had no receipt since 2026-08-02; Runtime is a sixth loop (A1 DR-10) | "five loops" and census scope drift | registry-relative wording (Seq 54; PRD candidate); owner decides rows separately |

## 9. Estimate, schedule and fixture staleness

### 9.1 Estimate/schedule

No estimate or schedule register exists for the PEC decomposition (none is
named in the Companion Inventory), so no `estimate-snapshot` rerun is
required by SCA-005 itself. Effort shifts qualitatively: PKG-02 grows by one
M and one S slice; PKG-06/07 shrink by one S and two M slices; DEL-02-03 and
DEL-01-01 stay L. The P1 critical path gains DEL-02-08/09 only under Q5 (a).

### 9.2 Phase effects

P1: DEL-02-08/09 (fixture-suite parsers), DEL-02-03 central grammar,
DEL-03-03 lag classes, DEL-04-01 re-sourcing, DEL-01-06 feed profiles (after
its source packet). P2: census parity leg (Q10 c). P3: presence narrowed to
Git + hooks. P4: daemon bridge and live hierarchy removed; stream-loss and TTL
tests keep their meaning for the hooks stream only.

### 9.3 P1 fixture strategy (steer 3; DN §6; Q5)

| Fixture class | Trial (pinned at `d61981ee2`) | Shape | Exercises |
|---|---|---|---|
| FC-1 receipt present | Piping `PIPING_LINTER_SCOPE_20260923` (graph blob `ae942d99…`, `RECEIPT.md` blob `23623e2c…`) | full shared shape | receipt fields, Examined-Through ancestry, run ID = folder |
| FC-2 evidence-only | Piping `PIP-DEC025-BASELINE-2026-09-23` (graph `e471421c…`, `EVIDENCE.md` `76e618a5…`) | AgentRuns evidence, no receipt | run ID ≠ folder; dated-heading MEMORY; partial coverage |
| FC-3 no AgentRuns record | App `APP-REPLAY-BOUNDARY-2026-09-23` (graph `d25cae61…`) | evidence colocated in WorkGraphs folder | run ID ≠ folder; bullet `## Runs`; em-dash node suffixes |
| FX-PEC-0 | PEC self-ingest (`remaining-loop`) | old shape | dual-generation reading on the loop PEC builds |
| synthetic | authored fresh under a v2 packet | grammar edges | missing run identity, unknown state token, unresolved PR, seeded two-graph overlap (SOW-061) |

Negative and partial classes are deliberate (steer 3). Fixtures are
golden-by-reference `(commit, path, blob)` triples with content-minimal
goldens; nothing is copied into PEC's tree.

## 10. Active snapshot and handoff impact

- `_Decomposition/_LATEST.md` stays revision 1.4 and `_ScopeChange/_LATEST.md`
  stays SCA-004 through checkpoints 1 and 2 and during checkpoint-3
  preparation (posture `ACCEPTED_PREDECESSOR`).
- `SCA-005_2026-09-23_2139/` is the interim checkpoint-1 package; it is not an
  active snapshot and not decomposition truth.
- The group-1 decision snapshot (`DECISION.md`, `ACCEPTED_MANIFEST.csv`,
  `Handoff_State.md`) is written only after owner acceptance.
- SCA-004's downstream obligations remain as its `Handoff_State.md` states;
  the pre-change audit reports provenance already on revision 1.4 for all 64
  contexts, but this assessment does not verify which SCA-004 SOW/SPEC
  repairs have occurred. SCA-005's currency list (§7.1) supersedes none of
  them silently.

## 11. Recommended downstream reruns

| Rerun | Owner | Trigger | Scope |
|---|---|---|---|
| PROJECT_SETUP metadata re-pin | PROJECT_SETUP | checkpoint 3 | all `_CONTEXT.md` provenance and `_REFERENCES.md` to revision 1.5; preparation of DEL-02-08/09 folders |
| WORKING_ITEMS Scope of Work currency per DEL | WORKING_ITEMS + REVIEW/owner artifact gates | checkpoint 3 | §7.1 list incl. pins and reference claims; DEL-01-06 as a new obligation |
| PRD amendment | PRD amendment workflow; owner | checkpoint 2 | successor candidate (Annex B), D-PEC-79 per CP1-D79 |
| DEL-00-03 SPEC (and DEL-00-01 ADRs) | owning deliverable workflows | after PRD successor and checkpoint 3 | §4 information model, §6 PKG-07 row, §8 open decisions; ADR carried posture 3 |
| P1 fixture strategy | DEL-02-08/09/03 SOWs | SOW currency pass | §9.3 classes, pinned basis, content-minimal goldens |
| dependency-extract + strict validator + closure | dependency-extract / PROJECT_SETUP | after preparation | §7.2 |
| audit-decomp post-change | TASK | checkpoint-3 preparation | compare with the pre-change baseline |
| Registry source packet | later D-PEC packet | after checkpoint 3 (O-B only) | `loops.schema.json` v2, `loops.json`, `RegisteredLoop` |
| TM-PEC-023 closure | task-management | after checkpoint 3 | `RESOLVED_BY_DECISION` citing SCA-005 |

## 12. Option deltas (so the owner can switch at checkpoint 1 without a re-run)

Each table states what changes **relative to the recommended set** in
`Amendment_Actions.csv`. Seq numbers refer to that file.

### 12.1 Feed model (Q1)

| Option | Actions dropped | Actions changed | Actions added | Consequence |
|---|---|---|---|---|
| **O-B2 (recommended)** | — | — | — | registry declares closed feed profiles; P1 self-ingest manifest gap closes; D-PEC-78/79 version clause needs CP1-V |
| O-B1 free declarations | — | Seq 10, 11, 13, 58: rows carry feed kinds with path globs and grammar IDs instead of profile IDs; `feed profile` term becomes `feed declaration` | — | configuration becomes a second description of each foreign loop's layout; every foreign-method change needs an owner-gated PEC config edit; same schema-v2 packet and CP1-V issue |
| O-A convention | Seq 10, 11, 13 (registry feed profiles), 58 (`feed profile` term), 7 and 18 (SOW-017/DEL-02-07 stay the manifest, NOTE only) | Seq 8 (discovery by convention, not profile), Seq 75 (no §16.3 feed-profile clause) | — | 70 actions; P1 self-ingest keeps an implicit manifest (PEC has no `adapter.yaml`); no schema v2, no CP1-V; later PEC migration needs parser/heuristic revisit |
| O-C minimal re-point | Seq 1, 2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22, 56–58, 60, 61 | Seq 3 (SOW-013: "`LOOP_RECEIPTS.md` or `AgentRuns/<RunID>/RECEIPT.md`"), Seq 5 (SOW-015: `WORK_GRAPH.md` replaces `.json`), Seq 14/16 wording only, Seq 23 (charter minimal), Seq 75 (PEC-RCN-002 only) | — | smallest SCA; entity model, JSON RunRecord sources, workplan parsing and the adapter manifest stay as written and contradict file truth; DN judges this converts known model drift into silent parser work (PRD §12) |

Presence (group P) and §16 (group Q6) actions are independent of Q1.

### 12.2 Presence and streams (Q3) and the deferral representation (CP1-R)

| Option | Actions dropped | Actions changed | Actions added | Consequence |
|---|---|---|---|---|
| **P-β / R1 (recommended)** | — | — | — | Git + hooks presence; graph-declared activity record tier; SOW-029/035/087 Deferred OUT with trigger T-RT; DEL-06-04/07-02/07-05 retired; TM rows 4/7 disposed without mapping |
| P-β / R2 keep IN, re-phase | Seq 34–36 (REMOVE) | Seq 29–31: stay IN, `OpenIssue = TRUE`; DEL-06-04/07-02/07-05 PhaseHint → `deferred (T-RT)`; Seq 42/43 keep assignments; Seq 60–62 OBJ-003 unchanged; `DEP-09-05-005` (DEL-09-05 → DEL-06-04) still retired with Seq 33/38, or reclassified non-blocking if the owner keeps live hierarchy on the board (§8.1); the 8 outgoing edges of the three deferred DELs stay ACTIVE | ADD OTHER `OI-014` (T-RT trigger) | smaller structural change; IN scope then contains work the PRD successor calls deferred; TM rows 4/7 stay live for mapping; envelopes and counts unchanged (IN 74 / OUT 14) |
| P-α PEC-owned Runtime instance | Seq 29–31 status moves, Seq 34–36 | SOW-035 → "PEC-owned Runtime instance SSE client"; SOW-087 → per-application client instance; SOW-029 hierarchy from that instance; C13 and SOW-067 (permanent OUT) would need a **contract-level** change | a `pec.yaml` profile amendment (foreign tier-0) before invocation | DN: yields no cross-application presence (tokens private per application) and makes PEC an execution host, conflicting with I-10/C13/SOW-067; not recommended |
| P-δ drop presence tier | all group-P MODIFYs become retirements | SOW-002, 026–032, 033, 035–037, 039, 049, 061, 062, 084 → OUT; SOW-044 → deltas only; PRD §3.3 outcome 3 retired | REMOVE PKG-06 and PKG-07 with every child (DEL-06-01..06, DEL-07-01..05), REMOVE DEL-01-02, DEL-09-05, DEL-10-06, 10-07, 10-08, 10-09; REMOVE or restate OBJ-003 (otherwise orphaned); SOW-038/DEL-03-05 disposition UNKNOWN | largest change; exact child-closure set must be computed at checkpoint 2; gives up the Git-based half of outcome 3 |
| keep rows as written | all group-P MODIFY/REMOVE except citation refreshes | — | — | PRD and decomposition keep naming a daemon that does not exist (A1 DR-08) |

### 12.3 New feed items (CP1-X; steer 5)

| Variant | Actions | Envelope consequence | Package discipline |
|---|---|---|---|
| **ADD-new (recommended)** | Seq 8, 9 (SOW-095/096), 19, 20 (DEL-02-08 M, DEL-02-09 S) | no existing envelope rises; PKG-02 active S/M/L = 4/4/1 | one grammar per deliverable (DL-4, DL-13) |
| Extend-existing | drop Seq 8, 9, 19, 20, 60, 61; Seq 5 SOW-015 adds `WORK_GRAPH.md` (+discovery, PR→merge inputs); Seq 4 SOW-014 adds MEMORY run index; Seq 15/16 re-envelope | DEL-02-05 S→M, plausibly L once discovery and the completion-join inputs are included; DEL-02-04 S→M; three L deliverables in PKG-01/02 | breaks DL-4 one-feed-kind-per-item; flagged as a decomposition-convention change |
| Receipts as a new item (applies to either) | Seq 3 narrows to ledgers; ADD `SOW-097` + `DEL-02-10` (S) for central `RECEIPT.md` | DEL-02-03 stays L on ledgers only | cleaner split; +1 SOW, +1 DEL |

### 12.4 Other owner questions that change the action set

| Question / option | Delta from recommended |
|---|---|
| Q2 (a) adapter.yaml stays manifest | Seq 7, 18 dropped (NOTE only); only coherent with O-A/O-C |
| Q2 (c) removed from PEC scope | Seq 7 → SOW-017 IN→OUT; Seq 18 → REMOVE DEL-02-07; DEL-03-01 `[E-P25]` edge retires |
| Q4 (b) node states verbatim | Seq 2 drops derived completion; Seq 21 dropped; every finished undertaking shows `ACTIVE` (R-01) |
| Q4 (c) keep ORI-001 wording | Seq 2, 22 dropped; parsers approximate |
| Q5 (b) P1 live App/Piping ingest | ADD a SOW-064/DEL-10-10 MODIFY naming a second P1 loop (beyond OI-010) and owner-gated `loops.json` rows |
| Q5 (c) P2 only | DEL-02-08/09 PhaseHint P2; P1 fixture suites dropped |
| Q6 retire as moot | Seq 46–52 become status changes: SOW-076/080/082 TBD→OUT (closed moot), OI-002/006/008 resolved; telemetry TBD 8→5, OUT 17→20, open/resolved OIs 10/3→7/6; OI-009 stays open |
| Q6 leave untouched | Seq 46–53 dropped; the TBD statements keep naming a daemon |
| Q7 (a) / (c) | Seq 8 wording only |
| Q8 (b) declare both generations / (c) defer PEC's row | Seq 11 wording only / Seq 11 dropped |
| Q9 (a) DN recommendation | Seq 72 replaces rather than supplements the pre-P1 baseline — conflicts with DEL-10-01 REQ-005/AC-003 and its CHECKING state (R-07) |
| Q9 (b) | Seq 72 dropped |
| Q10 (a) / (b) | PRD P1 exit wording unchanged / cross-loop harness change outside PEC fences (not an SCA-005 act) |
| CP1-N rename DEL-02-03/04/06/07 | four Name changes plus PROJECT_SETUP folder-path acts; DEL-07-02 is retired under R1 so its rename is moot |

## 13. Recorded disagreements between inputs (inventory locators govern)

| # | Inputs | Disagreement | Resolution in this package |
|---|---|---|---|
| X-1 | A2 M-6 vs live DEL-01-06 `Review_Findings.csv` (`f114d52b…`) and `_REVIEW.md`; brief steer 6 | A2 says RF-002 "already authorizes a revision"; the live record shows RF-002 RESOLVED with the successor SOW accepted at `5fdcfd96…a2fa8` on 2026-08-03 | live record governs; Seq 13 records a **new** currency obligation and a later source packet; RF-002 not reopened |
| X-2 | A2 (INV-061..063, 074..076, 095..097) vs contract Action Types | A2 uses `RECLASSIFY` for TBD/OI rows with no parent | `MODIFY` (§3) |
| X-3 | DN §5.4 vs A2 | DN names DEL-06-03 correlation as degrading; A2 finds no stale DEL-06-03 claim | no DEL-06-03 action; SOW-currency note only when its SOW is written |
| X-4 | DN §4 O-A vs A2 | DN lists DEL-03-03 "trailing by design" as a change; A2 finds no touching claim | carried as new content (Seq 21), not as drift |
| X-5 | DN §5.4 / §7 vs A2 | DN changes the presence board (DEL-09-05/SOW-049); A2 has no row | carried as a P-β consequence (Seq 33, 38) with live register locators |
| X-6 | DN §4 O-A ("SOW-013 MODIFY") vs A2 INV-080 (candidate ADD) | receipt parser as MODIFY vs ADD | MODIFY recommended (DL-4 feed-kind reading), ADD priced in §12.3 |
| X-7 | DN §7 "2 ADD SOWs, ≤2 DEL" vs A2 C-1..C-4 (up to four candidates) | C-2 (discovery) and C-13 (completion join) folded | folded into SOW-095; C-3 into SOW-013 |
| X-8 | A2 C-6 (per-application Runtime client instance) vs DN P-β | candidate ADD vs deferral | P-β recommended; C-6 is P-α in §12.2 |
| X-9 | DN §5.3 / Q9 (a) vs DEL-10-01 contract | DN's recommendation would replace a pre-P1 baseline after P1 started | manager recommends Q9 (c) (R-07) |
| X-10 | D-PEC-78 / D-PEC-79 "strict version 1" vs DN O-B2 ("home and shape unchanged, only the version advances") | whether schema v2 is within the ruling | CP1-V owner question |
| X-11 | Brief ("32 OPEN / 26 INITIALIZED / 4 CHECKING / 2 IN_PROGRESS") vs audit | none — the audit found exactly that census | recorded |
| X-12 | A2 §4 lists DEL-01-06 without housekeeping pin; A2 INV-176 membership | consistent | recorded |

## 14. Candidates and findings not carried into the action set

| Item | Why not carried | Where it lives |
|---|---|---|
| A2 C-14 / A1 DR-15 Task Management register feed | not in DN's recommended set; CandidateBrief re-sourcing (Q4) covers the need at P1 | later SCA if the owner wants it |
| A2 C-9 per-loop optional `## Remaining` | carried inside SOW-001 (Seq 1), not a separate action | DEL-02-01 SOW currency |
| A2 C-10 external fixtures | Q5; no decomposition change under Q5 (a) | §9.3, DEL-02-08/09/03 SOWs |
| A2 C-11 loop-set wording | Seq 54 + PRD candidate; registry rows are owner-gated config, not SCA edits | Q9 loop set, CP1 notes |
| A2 C-12 event-contract home | Seq 32, 44, 49, 53 | — |
| A1 DR-14 decision-register header variance | informational; DEL-02-02 grammar work | DEL-02-02 SOW currency |
| A1 DR-17 Root LOOP_INIT still lists historical ledgers | Root surface | informational notice to Root, not an SCA-005 act |
| A1 DR-18 `SCA-005` ID collision across loops | naming | qualify as PEC's SCA-005 in any cross-loop reference |
| INV-116 ContextBudgetQA DEL-01-01 RecommendedAction repeats DEL-02-03's split line | pre-existing register defect, not drift | may ride Seq 12 at checkpoint 2 if the owner wishes |

## 15. Checkpoint-group-1 owner question set

The owner answers these as one package. "Rec." is the note's recommended
option unless marked **manager**.

| # | Decision | Options | Rec. |
|---|---|---|---|
| CP1-A | Confirm or modify the parsed SCA-005 change set (76 PROPOSED actions: 8 ADD / 65 MODIFY / 3 REMOVE) | confirm / modify named rows | confirm |
| CP1-B | Accept this Impact Assessment at its exact SHA-256 (quoted in `Decision_Log.md` and the run return) | accept / return | accept |
| Q1 | Feed model | O-A / **O-B2** / O-B1 / O-C | O-B2 |
| Q2 | `adapter.yaml`, SOW-017, DEL-02-07 | (a) manifest / **(b) parity-peer input only, DEL-02-07 re-purposed** / (c) removed from scope | (b) |
| Q3 | Presence and streams under A2 | **P-β** / P-α / P-δ / keep as written | P-β |
| CP1-R | Representation of the P-β deferral | **R1 Deferred OUT + retire DEL-06-04/07-02/07-05** / R2 keep IN, re-phase, add OI-014 | R1 (manager) |
| Q4 | Orientation over graph node states | **(a) re-source to READY/ACTIVE/BLOCKED nodes with Git-derived terminal completion** / (b) verbatim states / (c) keep ORI-001 wording | (a) |
| Q5 | When the external trials enter | **(a) P1 pinned parser fixture suites only, three fixture classes (receipt present; evidence-only; no AgentRuns record)** / (b) P1 live ingest / (c) P2 only | (a) |
| Q6 | A2 effects on PRD §16.2/16.6/16.8/16.9 | **re-express as factual premise, decision still open** / retire as moot / leave untouched | re-express |
| Q7 | Ref scope for in-flight graphs | (a) integration ref only / **(b) integration ref default, local branches opt-in labelled unintegrated** / (c) all refs | (b) |
| Q8 | PEC's own registry row | **(a) declare `remaining-loop` now; migration later as one row change under its own ruling** / (b) both generations / (c) defer | (a) |
| Q9 | Step-0 baseline loops (SOW-058, DEL-10-01) | (a) shared-method loops as the "before" / (b) PEC's own loop / (c) both, reported separately | DN: (a); **manager: (c)** — DEL-10-01 is CHECKING with an accepted pre-P1 baseline (R-07) |
| Q10 | P1 parity comparable set given the harness does not observe PEC | (a) self-check facts + explained census absence / (b) seek harness observability (cross-loop) / **(c) census leg to P2 over App/Piping, stated in the P1 exit** | (c) |
| CP1-D79 | D-PEC-79 path | (a) apply the adopted six-hunk postimage, then amend on top / **(b) carry its six hunks into one successor candidate, adopted bytes preserved as historical exact input** | (b) — either needs checkpoint-2 acceptance |
| CP1-TM | TM-PEC-023 | **confirm the nine rows as candidate MODIFYs with no option selected, selected row by row at checkpoint 2; rows 1, 4, 7 sequenced behind Q3** / other handling | confirm |
| CP1-X | New feed items | **ADD SOW-095/096 + DEL-02-08/09; central receipts in SOW-013/DEL-02-03** / extend DEL-02-04/05 / receipts as SOW-097/DEL-02-10 | ADD-new (manager, steer 5) |
| CP1-N | Stable names and paths of DEL-02-03/04/06/07 | **retain, flag label drift** / rename (PROJECT_SETUP path act) | retain (manager) |
| CP1-V | D-PEC-78 O-A "Schema version 1 remains strict" / D-PEC-79 "strict-version-1" under O-B2 | **confirm a strict, versioned schema v2 via a later D-PEC packet is a supplementary extension, with the PRD successor saying "strict, versioned"** / rule a supersession / choose O-A | confirm (manager) |
| CP1-O | Objectives for SOW-095/096 and DEL-02-08/09 | **OBJ-001;OBJ-002 (DL-17 parser precedent)** / other | OBJ-001;OBJ-002 (manager) |

Accepting CP1-A/CP1-B authorizes preparation of the checkpoint-2 package
only. It applies no decomposition, register, PRD, SOW, metadata, source or
foreign change.

## Annex A — Part-A validation per action

Produced by a deterministic check of `Amendment_Actions.csv` against live `ScopeLedger.csv`, `Deliverables.csv`, `SOFTWARE_DECOMP.md` §3/§4/§1.3/§9/§10 and the A2 inventory (command and exit code in `Handoff_State.md`).

| Seq | ActionType | EntityType | EntityID | Validation | Result |
|---:|---|---|---|---|---|
| 1 | MODIFY | OTHER | SOW-001 | MODIFY: SOW-001 exists (IN) | PASS |
| 2 | MODIFY | OTHER | SOW-004 | MODIFY: SOW-004 exists (IN) | PASS |
| 3 | MODIFY | OTHER | SOW-013 | MODIFY: SOW-013 exists (IN) | PASS |
| 4 | MODIFY | OTHER | SOW-014 | MODIFY: SOW-014 exists (IN) | PASS |
| 5 | MODIFY | OTHER | SOW-015 | MODIFY: SOW-015 exists (IN) | PASS |
| 6 | MODIFY | OTHER | SOW-016 | MODIFY: SOW-016 exists (IN) | PASS |
| 7 | MODIFY | OTHER | SOW-017 | MODIFY: SOW-017 exists (IN) | PASS |
| 8 | ADD | OTHER | SOW-095 | ADD: ID free (append-only after SOW-094); parent PKG-02 + new DEL co-added | PASS |
| 9 | ADD | OTHER | SOW-096 | ADD: ID free (append-only after SOW-094); parent PKG-02 + new DEL co-added | PASS |
| 10 | MODIFY | OTHER | SOW-077 | MODIFY: SOW-077 exists (IN) | PASS |
| 11 | MODIFY | OTHER | SOW-094 | MODIFY: SOW-094 exists (IN) | PASS |
| 12 | MODIFY | DELIVERABLE | DEL-01-01 | MODIFY: DEL-01-01 exists (PKG PKG-01) | PASS |
| 13 | MODIFY | DELIVERABLE | DEL-01-06 | MODIFY: DEL-01-06 exists (PKG PKG-01) | PASS |
| 14 | MODIFY | DELIVERABLE | DEL-02-03 | MODIFY: DEL-02-03 exists (PKG PKG-02) | PASS |
| 15 | MODIFY | DELIVERABLE | DEL-02-04 | MODIFY: DEL-02-04 exists (PKG PKG-02) | PASS |
| 16 | MODIFY | DELIVERABLE | DEL-02-05 | MODIFY: DEL-02-05 exists (PKG PKG-02) | PASS |
| 17 | MODIFY | DELIVERABLE | DEL-02-06 | MODIFY: DEL-02-06 exists (PKG PKG-02) | PASS |
| 18 | MODIFY | DELIVERABLE | DEL-02-07 | MODIFY: DEL-02-07 exists (PKG PKG-02) | PASS |
| 19 | ADD | DELIVERABLE | DEL-02-08 | ADD: ID free, format DEL-XX-YY, parent PKG-02 exists | PASS |
| 20 | ADD | DELIVERABLE | DEL-02-09 | ADD: ID free, format DEL-XX-YY, parent PKG-02 exists | PASS |
| 21 | MODIFY | DELIVERABLE | DEL-03-03 | MODIFY: DEL-03-03 exists (PKG PKG-03) | PASS |
| 22 | MODIFY | DELIVERABLE | DEL-04-01 | MODIFY: DEL-04-01 exists (PKG PKG-04) | PASS |
| 23 | MODIFY | PACKAGE | PKG-02 | MODIFY: PKG-02 exists | PASS |
| 24 | MODIFY | OTHER | S1.2-intake-summary | MODIFY: section/record 'S1.2-intake-summary' (non-register surface) | PASS |
| 25 | MODIFY | OTHER | R4 | MODIFY: section/record 'R4' (non-register surface) | PASS |
| 26 | MODIFY | OTHER | C13 | MODIFY: constraint C13 exists | PASS |
| 27 | MODIFY | OTHER | C5 | MODIFY: constraint C5 exists | PASS |
| 28 | MODIFY | OTHER | SOW-026 | MODIFY: SOW-026 exists (IN) | PASS |
| 29 | MODIFY | OTHER | SOW-029 | MODIFY: SOW-029 exists (IN) | PASS |
| 30 | MODIFY | OTHER | SOW-035 | MODIFY: SOW-035 exists (IN) | PASS |
| 31 | MODIFY | OTHER | SOW-087 | MODIFY: SOW-087 exists (IN) | PASS |
| 32 | MODIFY | OTHER | SOW-034 | MODIFY: SOW-034 exists (IN) | PASS |
| 33 | MODIFY | OTHER | SOW-049 | MODIFY: SOW-049 exists (IN) | PASS |
| 34 | REMOVE | DELIVERABLE | DEL-06-04 | REMOVE: DEL-06-04 exists (PKG PKG-06) | PASS |
| 35 | REMOVE | DELIVERABLE | DEL-07-02 | REMOVE: DEL-07-02 exists (PKG PKG-07) | PASS |
| 36 | REMOVE | DELIVERABLE | DEL-07-05 | REMOVE: DEL-07-05 exists (PKG PKG-07) | PASS |
| 37 | MODIFY | DELIVERABLE | DEL-06-01 | MODIFY: DEL-06-01 exists (PKG PKG-06) | PASS |
| 38 | MODIFY | DELIVERABLE | DEL-09-05 | MODIFY: DEL-09-05 exists (PKG PKG-09) | PASS |
| 39 | MODIFY | DELIVERABLE | DEL-00-02 | MODIFY: DEL-00-02 exists (PKG PKG-00) | PASS |
| 40 | MODIFY | DELIVERABLE | DEL-08-01 | MODIFY: DEL-08-01 exists (PKG PKG-08) | PASS |
| 41 | MODIFY | PACKAGE | PKG-00 | MODIFY: PKG-00 exists | PASS |
| 42 | MODIFY | PACKAGE | PKG-06 | MODIFY: PKG-06 exists | PASS |
| 43 | MODIFY | PACKAGE | PKG-07 | MODIFY: PKG-07 exists | PASS |
| 44 | MODIFY | OTHER | SOW-074 | MODIFY: SOW-074 exists (OUT) | PASS |
| 45 | MODIFY | OTHER | SOW-092 | MODIFY: SOW-092 exists (OUT) | PASS |
| 46 | MODIFY | OTHER | SOW-076 | MODIFY: SOW-076 exists (TBD) | PASS |
| 47 | MODIFY | OTHER | SOW-080 | MODIFY: SOW-080 exists (TBD) | PASS |
| 48 | MODIFY | OTHER | SOW-082 | MODIFY: SOW-082 exists (TBD) | PASS |
| 49 | MODIFY | OTHER | SOW-083 | MODIFY: SOW-083 exists (TBD) | PASS |
| 50 | MODIFY | OTHER | OI-002 | MODIFY: OI-002 exists | PASS |
| 51 | MODIFY | OTHER | OI-006 | MODIFY: OI-006 exists | PASS |
| 52 | MODIFY | OTHER | OI-008 | MODIFY: OI-008 exists | PASS |
| 53 | MODIFY | OTHER | OI-009 | MODIFY: OI-009 exists | PASS |
| 54 | MODIFY | VOCAB_TERM | loop | MODIFY: term 'loop' exists in §9 | PASS |
| 55 | MODIFY | VOCAB_TERM | harness | MODIFY: term 'harness' exists in §9 | PASS |
| 56 | ADD | VOCAB_TERM | work graph | ADD: term 'work graph' not yet in §9 | PASS |
| 57 | ADD | VOCAB_TERM | receipt | ADD: term 'receipt' not yet in §9 | PASS |
| 58 | ADD | VOCAB_TERM | feed profile | ADD: term 'feed profile' not yet in §9 | PASS |
| 59 | ADD | VOCAB_TERM | declared activity | ADD: term 'declared activity' not yet in §9 | PASS |
| 60 | MODIFY | OBJECTIVE | OBJ-001 | MODIFY: OBJ-001 exists | PASS |
| 61 | MODIFY | OBJECTIVE | OBJ-002 | MODIFY: OBJ-002 exists | PASS |
| 62 | MODIFY | OBJECTIVE | OBJ-003 | MODIFY: OBJ-003 exists | PASS |
| 63 | MODIFY | DELIVERABLE | DEL-00-02 | MODIFY: DEL-00-02 exists (PKG PKG-00) | PASS |
| 64 | MODIFY | DELIVERABLE | DEL-03-05 | MODIFY: DEL-03-05 exists (PKG PKG-03) | PASS |
| 65 | MODIFY | DELIVERABLE | DEL-05-01 | MODIFY: DEL-05-01 exists (PKG PKG-05) | PASS |
| 66 | MODIFY | DELIVERABLE | DEL-07-02 | MODIFY: DEL-07-02 exists (PKG PKG-07) | PASS |
| 67 | MODIFY | DELIVERABLE | DEL-07-03 | MODIFY: DEL-07-03 exists (PKG PKG-07) | PASS |
| 68 | MODIFY | DELIVERABLE | DEL-07-04 | MODIFY: DEL-07-04 exists (PKG PKG-07) | PASS |
| 69 | MODIFY | DELIVERABLE | DEL-07-05 | MODIFY: DEL-07-05 exists (PKG PKG-07) | PASS |
| 70 | MODIFY | DELIVERABLE | DEL-08-05 | MODIFY: DEL-08-05 exists (PKG PKG-08) | PASS |
| 71 | MODIFY | DELIVERABLE | DEL-10-08 | MODIFY: DEL-10-08 exists (PKG PKG-10) | PASS |
| 72 | MODIFY | OTHER | SOW-058 | MODIFY: SOW-058 exists (IN) | PASS |
| 73 | MODIFY | OTHER | S7-S8-telemetry | MODIFY: section/record 'S7-S8-telemetry' (non-register surface) | PASS |
| 74 | MODIFY | OTHER | SCA-005 | MODIFY: section/record 'SCA-005' (non-register surface) | PASS |
| 75 | MODIFY | OTHER | PRD-successor-candidate | MODIFY: section/record 'PRD-successor-candidate' (non-register surface) | PASS |
| 76 | MODIFY | OTHER | D-PEC-79 | MODIFY: section/record 'D-PEC-79' (non-register surface) | PASS |

Summary: 76 actions, 0 errors (ADD 8, MODIFY 65, REMOVE 3; DELIVERABLE 27, OTHER 36, VOCAB_TERM 6, PACKAGE 4, OBJECTIVE 3).

## Annex B — PRD v2.2 rows carried to the successor candidate (outside the decomposition)

Source: A2 INV-001..INV-036 (28 MODIFY, 8 NOTE-ONLY). Every row applies identically to the D-PEC-79 postimage except INV-033, which that postimage already resolves (A2 §6). Application requires the owner's checkpoint-2 acceptance.

| InvID | PRD locator (v2.2) | A2 action | Drift | Disposition in the recommended set |
|---|---|---|---|---|
| INV-001 | §2 Problem, bullet 1 (L74) | NOTE-ONLY | D2;D4 | No change required; optional refresh |
| INV-002 | §2 Problem, bullet 3 (L82) | MODIFY | D5;D1 | Refresh with the successor candidate |
| INV-003 | §2 Problem, closing paragraph (L90) | MODIFY | D8 | Registry-relative loop wording (Q-loop set; D8) |
| INV-004 | §4.2 Not an orchestrator (L130) | MODIFY | D5 | Refresh with the successor candidate |
| INV-005 | §7.1 Loop row (L203) | MODIFY | D4;D8 | Refresh with the successor candidate |
| INV-006 | §7.1 Workplan / Step / Gate row (L204) | MODIFY | D4 | Historical-grammar entity; gate state re-sourced |
| INV-007 | §7.1 Receipt row (L205) | MODIFY | D2 | Refresh with the successor candidate |
| INV-008 | §7.1 Package / Deliverable row (L208) | MODIFY | D3 | Refresh with the successor candidate |
| INV-009 | §7.1 DependencyEdge row (L209) | MODIFY | D1 | Refresh with the successor candidate |
| INV-010 | §7.1 RunRecord row (L210) | MODIFY | D1;D2;D5;D6 | RunRecord re-sourced |
| INV-011 | §7.1 CandidateBrief row (L211) | NOTE-ONLY | D3 | No change required; optional refresh |
| INV-012 | §7.2 Presence tier (whole table) (L219) | NOTE-ONLY | D5 | No change required; optional refresh |
| INV-013 | §8 Users and access, Harnesses (L237) | MODIFY | D5 | Refresh with the successor candidate |
| INV-014 | §9.1 PEC-ORI-001 (L257) | MODIFY | D2;D3;D4 | Q4 (a) re-sourcing |
| INV-015 | §9.2 PEC-RCN-002 (feed list) (L269) | MODIFY | D1;D2;D4;D6;D7 | Re-express feed kinds; manifest clause moves to registry feed profiles (Q1/Q2) |
| INV-016 | §9.3 PEC-GAT-001 (L279) | NOTE-ONLY | D2 | No change required; optional refresh |
| INV-017 | §9.4 PEC-PRS-001 (L288) | MODIFY | D5 | Re-express per P-β |
| INV-018 | §9.4 PEC-PRS-004 (L291) | MODIFY | D5 | Defer with trigger T-RT (P-β) |
| INV-019 | §9.5 PEC-STR-002 (L301) | MODIFY | D5;D9 | Refresh with the successor candidate |
| INV-020 | §9.5 PEC-STR-003 (L302) | MODIFY | D5 | Daemon bridge deferred; hooks/cmux stay |
| INV-021 | §9.6 PEC-API-001 (L310) | MODIFY | D5 | Refresh with the successor candidate |
| INV-022 | §9.7 PEC-DSH-001 (L320) | NOTE-ONLY | D2;D4 | No change required; optional refresh |
| INV-023 | §9.7 PEC-DSH-003 (L322) | NOTE-ONLY | D1;D2 | No change required; optional refresh |
| INV-024 | §12 P0 row (L373) | NOTE-ONLY | D4 | No change required; optional refresh |
| INV-025 | §12 P2 row (L375) | MODIFY | D8 | Registry-relative P2 wording |
| INV-026 | §12 P4 row (L377) | MODIFY | D5 | Narrow P4 (P-β) |
| INV-027 | §12 closing paragraph (L392) | NOTE-ONLY | D1;D2 | No change required; optional refresh |
| INV-028 | §13 Domain-engine registration row (L414) | MODIFY | D9 | Refresh with the successor candidate |
| INV-029 | §13 Shared-runtime client seam row (L417) | MODIFY | D5 | Refresh with the successor candidate |
| INV-030 | §13 chirality.project.json row (L418) | MODIFY | D5 | Refresh with the successor candidate |
| INV-031 | §15 D-GOV-20 bullet (L461) | MODIFY | D5 | Refresh with the successor candidate |
| INV-032 | §16.2 (L497) | MODIFY | D5 | Q6 re-express, still open |
| INV-033 | §16.3 (L499) | MODIFY | D8 | Already resolved by D-PEC-79 hunk 5; carried per CP1-D79; add feed-profile clause under O-B2 |
| INV-034 | §16.6 (L504) | MODIFY | D5 | Q6 re-express, still open |
| INV-035 | §16.8 (L507) | MODIFY | D2 | Q6 re-express, still open |
| INV-036 | §16.9 (L510) | MODIFY | D5;D9 | Q6 re-express + path refresh |
