# Dependencies: DEL-07-03 Deliverable Metadata and Document Kit Contracts

> **Current-source note (2026-09-23):** References below to the former App `Remaining` section and its Depends text record dated extraction evidence. The live status section was retired in the finite App Task Management account. For current work and dependency gating, read `Dependencies.csv`, governing Scope of Work, accepted decisions and the selected work graph. The historical Depends text adds no prerequisite; this note does not change the accepted register rows.


## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows: `DEP-07-03-001`, `DEP-07-03-002`, `DEP-07-03-003`, `DEP-07-03-004`, `DEP-07-03-005`, `DEP-07-03-006`, `DEP-07-03-007`, `DEP-07-03-008`, `DEP-07-03-009`, `DEP-07-03-010`, `DEP-07-03-011`, `DEP-07-03-014`. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Declared Downstream

Current extracted downstream rows: `DEP-07-03-012`, `DEP-07-03-013`. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Extracted Dependency Register

| Metric | Count |
|---|---:|
| Total rows | 14 |
| ACTIVE rows | 14 |
| RETIRED rows | 0 |
| ANCHOR rows | 3 |
| EXECUTION rows | 11 |
| UPSTREAM rows | 12 |
| DOWNSTREAM rows | 2 |

| DependencyID | Class | Type | Target | Status | Evidence |
|---|---|---|---|---|---|
| DEP-07-03-001 | ANCHOR | OTHER | UPSTREAM | SOW-026 | ACTIVE | TBD |
| DEP-07-03-002 | ANCHOR | OTHER | UPSTREAM | OBJ-006 | ACTIVE | TBD |
| DEP-07-03-003 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-07-03 decomposition entry | ACTIVE | TBD |
| DEP-07-03-004 | EXECUTION | PREREQUISITE | UPSTREAM | REF-003 | ACTIVE | TBD |
| DEP-07-03-005 | EXECUTION | PREREQUISITE | UPSTREAM | REF-006 | ACTIVE | TBD |
| DEP-07-03-006 | EXECUTION | PREREQUISITE | UPSTREAM | REF-004 | ACTIVE | TBD |
| DEP-07-03-007 | EXECUTION | PREREQUISITE | UPSTREAM | REF-001 | ACTIVE | TBD |
| DEP-07-03-008 | EXECUTION | PREREQUISITE | UPSTREAM | REF-002 | ACTIVE | TBD |
| DEP-07-03-009 | EXECUTION | CONSTRAINT | UPSTREAM | DEL-07-04 | ACTIVE | TBD |
| DEP-07-03-010 | EXECUTION | CONSTRAINT | UPSTREAM | DEL-07-05 | ACTIVE | TBD |
| DEP-07-03-011 | ANCHOR | OTHER | UPSTREAM | SOW-081 | ACTIVE | TBD |
| DEP-07-03-012 | EXECUTION | INTERFACE | DOWNSTREAM | DEL-02-02 | ACTIVE | PENDING |
| DEP-07-03-013 | EXECUTION | INTERFACE | DOWNSTREAM | DEL-04-04 | ACTIVE | PENDING |
| DEP-07-03-014 | EXECUTION | CONSTRAINT | UPSTREAM | K-PATH-2 | ACTIVE | PENDING |

## Run Notes

- Run timestamp: 2026-05-20T19:54:16-0600.
- Mode: UPDATE.
- Strictness: CONSERVATIVE.
- Consumer context: NONE.
- Scope: DEL-07-03.
- Decomposition path: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; status: located and used for anchor/target validation.
- Source documents read for extraction: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- Human ruling honored: semantic lensing and P3 enrichment are skipped; `_SEMANTIC.md` was not read or consumed as dependency evidence.
- Anchor document selected: `Datasheet.md`.
- Execution document order selected: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`.
- Existing `Dependencies.csv`: absent before this run; created with v3.1 schema.
- [RESOLVED 2026-07-12] REF-006 docs/PRD.md is MATCH under D-APP-38; the mismatch warning remains only in dated 2026-05-20 run history.
- Implementation location remains TBD in source procedure; no dependency edge was inferred from that unknown.
- Scanner output schema remains TBD in source procedure; no dependency edge was inferred from that unknown.

## Run Notes - 2026-09-05 SCA-APP-010 dependency closure (UPDATE)

- Run timestamp: 2026-09-05T00:37:52-0600. Produced as report-only preview `N1-TASK-DEL-07-03` under run `execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/`; applied to this folder only by the reviewed write step (SCA-APP-010 `FUTURE_WRITE_SET.csv` DEP-019, DEP-020).
- Runtime overrides: `SCOPE=DEL-07-03_Deliverable_Metadata_and_Document_Kit_Contracts`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; `SOURCE_DOCS=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`; `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`. No default was left to auto-discovery.
- Decomposition: found at the pinned identity, SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61`, content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291` (matches `ScopeOfWork.md` front matter `decomposition_basis`); companion register `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`; pointer `_ScopeChange/_LATEST.md` `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0` naming SCA-APP-010. Applied row L359; amended Scope Ledger row SOW-081 L251; reverse view L429 (SOW-026) and L484 (SOW-081); OI-008 L602; DEC-025 L634.
- Sources: `ScopeOfWork.md` (anchor and execution), `_CONTEXT.md`, `_STATUS.md` `## Remaining` only (`Depends`, `Write locus`, gate lines); `_REFERENCES.md` for pointer resolution. Excluded as evidence: `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`, `MEMORY.md`, `Assessment_*`, `Evidence*`, `_run_records/**`. Source documents were read-only.
- Legacy four-document kit: `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` no longer exist in this folder. Every pre-existing row that cited them (DEP-07-03-001 to DEP-07-03-010) is restated in live `ScopeOfWork.md` bytes and was re-evidenced with `LastSeen=2026-09-05`; no row was retired.
- Pass 1 - ANCHOR: parent anchor DEP-07-03-001 (SOW-026, `IMPLEMENTS_NODE`) preserved; objective trace anchor DEP-07-03-002 (OBJ-006) preserved with `TargetType=REQUIREMENT` as this register's existing convention; new trace anchor DEP-07-03-011 for SOW-081, which SCA-APP-010 added to applied row L359 (DEC-025). No scope ref left the applied row, so no anchor was retired.
- Pass 2 - EXECUTION: three new rows from SOW-081. DEP-07-03-012 (DOWNSTREAM INTERFACE to DEL-02-02: the Workflows view, roadmap, forms, library, and bind act over the file contract this carrier owns; L484, L308). DEP-07-03-013 (DOWNSTREAM INTERFACE to DEL-04-04: the delimited roadmap-injection block consumes the roadmap grammar, `roadmapSource`, and hash; L484, L329, L251). DEP-07-03-014 (UPSTREAM CONSTRAINT, `TargetType=EXTERNAL`, `TargetLocation=TBD`: "Writes obey K-PATH-2 containment", L251, L329, REQ-008).
- Considered and not emitted (CONSERVATIVE; F3 permitted effect): SOW-026 co-carrier DEL-08-03 (structural adjacency; unchanged by SCA-APP-010); DEL-08-01 skill-declared workflow templates and the app-scoped known-folder set behind the library (not stated for this carrier); the workflow file's front-matter delegation-policy declaration as a consumer of the Root DEL-02-11 session-record field (not stated for this carrier; the seated item records `Depends: none`); the `plans/shell-redesign_2026-09-04/` design-basis pins in the seated item (cited "only for what the tranche means when complete, never as a queue"; not on the applied or amended rows); the seated item's gates and checks (schedule/verification, not information flow).
- Fences: F1 NONE (DEL-07-03 is not an SCC-001 member; DEL-02-02 and DEL-04-04 are not SCC-001 members; no SCC-001 member holds an active row back to DEL-07-03). F2 NONE (every `TargetLocation` is under `execution/**`, a `_REFERENCES.md`-pinned `docs/*.md`, or `TBD`; no Root path). F3 NONE (new rows derive only from SOW-081 L251/L484 and applied row L359 prose).
- NEEDS_HUMAN_GRAPH_DECISION: none.
- CONFLICT: decomposition L251 and OI-008 L602 state that Q16 (shared-folder position advance) remains an OI-008 owner question, while `_STATUS.md` `## Remaining` DEL-07-03-V3-01 and `ScopeOfWork.md` Current acceptance obligations record Q16 as ruled under D-APP-108 (2026-09-04). No graph edge hinges on it; surfaced for RECONCILIATION and the OI-008 register, not resolved here.
- [WARNING] PROJECT_ID_FORMAT_PROFILE: the generic `validate_id_format.sh` expects `PKG-NNN`, `DEL-NNN-NN`, `DEP-NNN-NN-NNN`, and `SOW-NNNN`; this accepted App decomposition uses `PKG-NN`, `DEL-NN-NN`, `DEP-NN-NN-NNN`, and `SOW-NNN`. The helper reports those IDs invalid by its generic profile (OBJ-006 validates). No accepted ID was rewritten or invented.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` anchor is present.
- Schema validation: `validate_dependencies_schema.py` VALID, 29 columns, 14 data rows; all 23 distinct emitted enum values VALID; `DependencyID` unique; `FromDeliverableID=DEL-07-03` on every row; `Status=CANDIDATE` absent.

## Run History

| Timestamp | Mode | Strictness | Decomposition status | Warnings | ACTIVE rows |
|---|---|---|---|---|---:|
| 2026-05-20T19:54:16-0600 | UPDATE | CONSERVATIVE | located: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | SOURCE_HASH_MISMATCH REF-006 | 10 |
| 2026-09-05T00:37:52-0600 | UPDATE | CONSERVATIVE | located at pinned identity: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SHA-256 `c7c05169…771e61` at `dbd812a52d5ed0cb3ed173f3aaaa68703a914291` | PROJECT_ID_FORMAT_PROFILE; CONFLICT Q16 (L251/L602 vs D-APP-108 seating) | 14 |

## Lifecycle Summary

Current descriptive counts from unchanged `Dependencies.csv` (2026-09-22); this projection does not change satisfaction or maturity.

| Field | Count |
|---|---:|
| ACTIVE | 14 |
| RequiredMaturity=SEMANTIC_READY | 14 |
| ProposedMaturity=TBD | 14 |
| SatisfactionStatus=PENDING | 3 |
| SatisfactionStatus=TBD | 11 |

## Downstream Handoff Notes

- Consumer: `RECONCILIATION`.
- Reconcile one parent anchor (SOW-026), two trace anchors (OBJ-006, SOW-081), eight retained UPSTREAM prerequisite/constraint rows re-evidenced to `ScopeOfWork.md`, two new DOWNSTREAM interface rows (DEL-02-02, DEL-04-04) that correspond to the SOW-081 ownership split on L484, and one new EXTERNAL constraint row (K-PATH-2) whose owning document is unresolved.
- Expect reciprocal UPSTREAM rows in the DEL-02-02 and DEL-04-04 registers from their own SCA-APP-010 extraction passes; this register does not assert them.
- Carry the Q16 CONFLICT (decomposition L251/L602 versus D-APP-108 seating) to the OI-008 register owner; it is documentary, not a graph edge.
- DEP-07-03-012, DEP-07-03-013, and DEP-07-03-014 remain PENDING until DEL-07-03-V3-01 lands the workflow file contract and validator; no lifecycle, dependency-acceptance, or Root act is implied.

## D-APP-56 R5 P40 register annotation (2026-07-12)

REF-006 is MATCH under D-APP-38. Any HASH_MISMATCH token retained in the dated Run History is extraction provenance, not current dependency state. Structured-row status and summary counts above reflect Dependencies.csv after UPD-077..079.

---

**Addendum (2026-07-18 — D-APP-62 scoped interpretation):** Under the
D-APP-62 ruling (O-A, 2026-07-18), the assertion above that `_SEMANTIC.md`
is invalid evidence / was not read or consumed is scoped to
dependency-extraction evidence: it bars `_SEMANTIC.md` from serving as
evidence for dependency rows. Its recorded consumption as the primary input
to `_SEMANTIC_LENSING.md` is a different act, outside that scope and
consistent with it. See
`execution/_Coordination/_DECISIONS/D-APP-62_PACKET_SEMANTIC_ADMISSIBILITY_SCOPE_2026-07-18.md`.

## Current record interpretation — 2026-09-22

Earlier extraction notes, counts, source states and file citations retain their dated basis. Current production claims live in `ScopeOfWork.md`; removed four-document files are historical evidence. D-GOV-43/D-APP-127 make the App-owned Runtime/Codex path current; SDK MCP/hooks and daemon proofs are compatibility history. Formal row mutations require the owning dependency pass; this descriptive update grants none.

## Current evidence-locator refresh — 2026-09-22

2 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=14; RETIRED=0; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.

## Current evidence-locator refresh — 2026-09-22

7 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.
