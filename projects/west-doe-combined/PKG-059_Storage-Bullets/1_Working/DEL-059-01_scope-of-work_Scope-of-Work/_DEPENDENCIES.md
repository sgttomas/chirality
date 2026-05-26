# Dependencies: DEL-059-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill, UPDATE run)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1, 19 rows); this file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Run date: 2026-05-25 | Mode: UPDATE | Strictness: CONSERVATIVE | Rows: 19 ACTIVE

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-059-01-A-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-059 | Storage Bullets (PKG-059) | HIGH | ACTIVE |
| DEP-059-01-A-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0181 | Scope Ledger SOW-0181 — Vendor/EPC responsibility split | HIGH | ACTIVE |
| DEP-059-01-A-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0182 | Scope Ledger SOW-0182 — Basic scope | HIGH | ACTIVE |
| DEP-059-01-A-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0183 | Scope Ledger SOW-0183 — Major included equipment | HIGH | ACTIVE |
| DEP-059-01-A-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0184 | Scope Ledger SOW-0184 — Scope notes / by-others | HIGH | ACTIVE |
| DEP-059-01-A-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | Objective OBJ-001 | MEDIUM | ACTIVE |
| DEP-059-01-A-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-003 | Objective OBJ-003 | MEDIUM | ACTIVE |
| DEP-059-01-A-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Objective OBJ-004 — Vendor/EPC responsibility | HIGH | ACTIVE |
| DEP-059-01-A-009 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Objective OBJ-009 — Safety / sour-service / regulatory | HIGH | ACTIVE |
| DEP-059-01-A-010 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Objective OBJ-010 — Operability / commissioning / turnover | HIGH | ACTIVE |
| DEP-059-01-E-001 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | GATE-07-DECOMP | GATE-07 Final Published PROJECT_DECOMP Snapshot | HIGH | ACTIVE |
| DEP-059-01-E-002 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DBM-Deepcut | 4-25 Deepcut Design Basis Memorandum | HIGH | ACTIVE |
| DEP-059-01-E-003 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | PKG-REQ-DOC | 26020-Package_Requirements.docx package heading 14 | MEDIUM | ACTIVE |
| DEP-059-01-E-004 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-059-02_package-datasheet | Package Datasheet (DEL-059-02) | HIGH | ACTIVE |
| DEP-059-01-E-005 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-059-03_construction-work-package | Construction Work Package (DEL-059-03) | HIGH | ACTIVE |
| DEP-059-01-E-006 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-059-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package (DEL-059-04) | HIGH | ACTIVE |
| DEP-059-01-E-007 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-059-05_vendor-document-turnover-package | Vendor Document Turnover Package (DEL-059-05) | HIGH | ACTIVE |
| DEP-059-01-E-008 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-059-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance (DEL-059-06) | HIGH | ACTIVE |
| DEP-059-01-E-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | INTERFACE-REG-PKG-059 | INTERFACE_REGISTER PKG-059 (10 rows) | HIGH | ACTIVE |

**Counts:** ANCHOR = 10 (1 IMPLEMENTS_NODE + 9 TRACES_TO_REQUIREMENT) | EXECUTION = 9 (3 UPSTREAM + 1 INTERFACE UPSTREAM + 5 DOWNSTREAM HANDOVER) | Total ACTIVE = 19 | RETIRED = 0

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Source docs scanned (AUTO):** Datasheet.md, Specification.md, Guidance.md, Procedure.md
- **ANCHOR_DOC (AUTO):** Datasheet.md (contains DeliverableID, ParentPackageID, scope item traceability)
- **EXECUTION_DOC_ORDER (AUTO):** Procedure.md (prerequisites / steps), Specification.md (verification section), Guidance.md (purpose / downstream reference)
- **Decomposition path:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — FOUND; used to validate PKG-059 anchor and resolve deliverable IDs DEL-059-02..06.
- **_REFERENCES.md:** Present and read; used to resolve document pointer paths (GATE-07 snapshot CSVs; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; `_Sources/26020-Package_Requirements.docx`).
- **Objectives OBJ-005..OBJ-008:** Present in Datasheet "Supported Objectives" but not individually cited in Specification source text. CONSERVATIVE posture: not emitting separate trace rows for OBJ-005..OBJ-008 because no explicit per-objective citation appears in the source docs beyond the heuristic block in Datasheet. OBJ-001, OBJ-003, OBJ-004, OBJ-009, OBJ-010 are individually cited or block-cited with explicit source reference; emitted.
- **GATE-07 DECOMPOSITION_PATH supplied as `GATE-07_Final_Published_2026-05-24/` (from _REFERENCES.md):** confirmed directory exists.
- **No warnings:**
  - Parent anchor count = 1 (DEP-059-01-A-001): OK.
  - All ACTIVE rows carry EvidenceFile + SourceRef.
  - No legacy INBOUND/OUTBOUND values present.
  - All DependencyIDs unique.

## Lifecycle Summary

| Dimension | Count |
|---|---|
| ACTIVE | 19 |
| RETIRED | 0 |
| Total rows | 19 |
| ANCHOR / IMPLEMENTS_NODE | 1 |
| ANCHOR / TRACES_TO_REQUIREMENT | 9 |
| EXECUTION / UPSTREAM | 4 |
| EXECUTION / DOWNSTREAM | 5 |
| SatisfactionStatus = TBD | 19 |
| SatisfactionStatus = SATISFIED | 0 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full two-pass extraction (ANCHOR + EXECUTION); dependency-extract skill UPDATE run; CONSERVATIVE strictness; CONSUMER_CONTEXT=NONE. 19 ACTIVE rows written to Dependencies.csv v3.1. Schema validated VALID.
