# Dependencies: DEL-084-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill; UPDATE run 2026-05-26)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the authoritative register (v3.1 schema); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Extraction completed 2026-05-26. Total rows: 11 ACTIVE, 0 RETIRED.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-084-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-084 | Fuel Gas Skid 3-25 (PKG-084) | HIGH | ACTIVE |
| DEP-084-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0095 | Carry Fuel Gas Skid 3-25 as distinct package | HIGH | ACTIVE |
| DEP-084-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0096 | Basic scope — LP Fuel Gas Package | HIGH | ACTIVE |
| DEP-084-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0097 | Major included equipment | HIGH | ACTIVE |
| DEP-084-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0098 | Scope notes and design conditions | HIGH | ACTIVE |
| DEP-084-02-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | PACKAGE_REGISTER_PKG-084 | PACKAGE_REGISTER.csv row PKG-084 | HIGH | ACTIVE |
| DEP-084-02-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DELIVERABLE_REGISTER_DEL-084-02 | DELIVERABLE_REGISTER.csv row DEL-084-02 | HIGH | ACTIVE |
| DEP-084-02-008 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-084-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package | HIGH | ACTIVE |
| DEP-084-02-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DBM_COMP_LIQUIDS | 3-25_Comp_and_Liquids_DBM.md §Fuel Gas L454-465 | HIGH | ACTIVE |
| DEP-084-02-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DBM_DEEPCUT | 4-25_Deepcut_DBM.md §Fuel Gas Heating and Scrubbing L1872-1874 | HIGH | ACTIVE |
| DEP-084-02-011 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DOCUMENT | RFQ_26020-02-PT-RFQ-23-001 | 26020-02-PT-RFQ-23-001_FG_Skid_1.docx | HIGH | ACTIVE |

## Run Notes

- **Run date:** 2026-05-26
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; documents found: `Datasheet.md` (ANCHOR_DOC; filename contains `datasheet`), `Specification.md`, `Guidance.md`, `Procedure.md` (EXECUTION_DOCs).
- **ANCHOR_DOC:** AUTO → resolved to `Datasheet.md` (highest-confidence anchor doc per DOC_ROLE_MAP heuristic; filename contains `datasheet`).
- **EXECUTION_DOC_ORDER:** AUTO → `Procedure.md` (primary, contains explicit prerequisite and handover statements), `Specification.md`, `Guidance.md`, `Datasheet.md`.
- **DECOMPOSITION_PATH resolution:** DECOMPOSITION_PATH argument (`/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/`) did not exist at the given path. Resolved via `_REFERENCES.md` § Authoritative Decomposition Basis to: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PROJECT_DECOMP.md`. Confirmed PKG-084 and DEL-084-02_package-datasheet present in PACKAGE_REGISTER.csv and DELIVERABLE_REGISTER.csv respectively. Anchor validation performed against SCOPE_LEDGER.csv (SOW-0095 through SOW-0098) and DELIVERABLE_REGISTER.csv (DEL-084-04 confirmed).
- **Parent anchor:** One IMPLEMENTS_NODE row emitted (DEP-084-02-001) pointing to PKG-084.
- **Trace anchors:** Four TRACES_TO_REQUIREMENT rows emitted (DEP-084-02-002 through -005) for SOW-0095, SOW-0096, SOW-0097, SOW-0098 per `_CONTEXT.md` § Covers Scope Items.
- **Execution edges:** Six EXECUTION rows emitted: two upstream prerequisite documents (Gate 7 registers), two upstream source-slice prerequisites (DBM slices explicitly required by Procedure.md), one downstream handover to DEL-084-04 (explicitly named in Procedure.md § Purpose), one downstream handover to RFQ document (explicitly named in Procedure.md § Purpose).
- **No FLOATING_NODE warning:** One IMPLEMENTS_NODE row present (DEP-084-02-001).
- **No AMBIGUOUS_ANCHOR warning:** Exactly one IMPLEMENTS_NODE row.
- **CONSERVATIVE posture applied:** No implicit or structural-adjacency edges emitted. Objectives (OBJ-002 through OBJ-010) listed in `_CONTEXT.md` were not emitted as ANCHOR rows because the decomposition does not define objective-nodes as WBS tree parents; they are a separate dimension. Emitting them would be structural over-reach. Only explicit prerequisite/handover statements in source documents produced EXECUTION rows.
- **Accepted upstream decomposition snapshot:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`

## Lifecycle Summary

| Dimension | Count |
|---|---|
| ACTIVE rows | 11 |
| RETIRED rows | 0 |
| ANCHOR / IMPLEMENTS_NODE (ACTIVE) | 1 |
| ANCHOR / TRACES_TO_REQUIREMENT (ACTIVE) | 4 |
| EXECUTION / UPSTREAM (ACTIVE) | 4 |
| EXECUTION / DOWNSTREAM (ACTIVE) | 2 |
| SatisfactionStatus = TBD | 11 |
| SatisfactionStatus = SATISFIED | 0 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — First EXTRACTED run; MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. DECOMPOSITION_PATH resolved via `_REFERENCES.md` to Gate-07 snapshot. 11 rows emitted (5 ANCHOR, 6 EXECUTION); 0 RETIRED. No integrity warnings.
