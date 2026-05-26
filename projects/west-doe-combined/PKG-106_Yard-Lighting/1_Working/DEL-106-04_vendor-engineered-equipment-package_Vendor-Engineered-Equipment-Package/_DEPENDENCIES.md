# Dependencies: DEL-106-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** EXTRACTED
**Dependency tracking mode:** EXTRACTED (Dependencies.csv v3.1)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the authoritative structured register; this file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

13 rows extracted and registered in `Dependencies.csv` (all ACTIVE).

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetID / Name | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-106-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0011 | HIGH | ACTIVE |
| DEP-106-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | HIGH | ACTIVE |
| DEP-106-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | HIGH | ACTIVE |
| DEP-106-04-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | HIGH | ACTIVE |
| DEP-106-04-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | HIGH | ACTIVE |
| DEP-106-04-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | HIGH | ACTIVE |
| DEP-106-04-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-106-01_scope-of-work | HIGH | ACTIVE |
| DEP-106-04-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-106-02_package-datasheet | HIGH | ACTIVE |
| DEP-106-04-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | Facility hazardous area drawings | HIGH | ACTIVE |
| DEP-106-04-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | Geotechnical basis for mast pole foundations | MEDIUM | ACTIVE |
| DEP-106-04-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | Electrical distribution layout — nearest RDC | HIGH | ACTIVE |
| DEP-106-04-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-106-05_vendor-document-turnover-package | HIGH | ACTIVE |
| DEP-106-04-013 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-106-06_epc-vendor-package-review-and-acceptance | HIGH | ACTIVE |

**ANCHOR rows:** 6 (1 IMPLEMENTS_NODE + 5 TRACES_TO_REQUIREMENT)
**EXECUTION rows:** 7 (4 UPSTREAM: 2 PREREQUISITE + 2 INTERFACE [document]; 1 UPSTREAM INTERFACE [document]; 2 DOWNSTREAM: 2 HANDOVER)

## Run Notes

- **Run date:** 2026-05-26
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Source docs (AUTO):** Datasheet.md (ANCHOR_DOC — matched by `datasheet`), Specification.md, Guidance.md, Procedure.md (EXECUTION_DOC candidates)
- **ANCHOR_DOC chosen:** Datasheet.md (highest-confidence ANCHOR_DOC match by filename heuristic; confirmed by Identification table mapping to decomposition rows)
- **EXECUTION_DOC order:** Specification.md, Procedure.md, Guidance.md (Specification.md carries explicit requirement IDs; Procedure.md carries explicit prerequisite list; Guidance.md carries supporting context)
- **Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` (from `_REFERENCES.md` and confirmed by directory presence)
- **DECOMPOSITION_PATH from invocation:** `GATE-07_Final_Published_2026-05-24/` — path not found as absolute; resolved to snapshot under `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` from `_REFERENCES.md`.
- **Anchor validation:** SOW-0011 confirmed in `SCOPE_LEDGER.csv`; OBJ-001/004/005/009/010 confirmed in `OBJECTIVE_REGISTER.csv` and `DELIVERABLE_REGISTER.csv` objectives column for DEL-106-04.
- **Parent anchor count:** 1 (DEP-106-04-001 — IMPLEMENTS_NODE → SOW-0011). Tree integrity: OK.
- **CONSERVATIVE extraction note:** Procedure.md explicitly labels logical inputs (DEL-106-01, DEL-106-02, hazardous area drawings, geotechnical basis, electrical distribution layout) as `ASSUMPTION, not declared edges`. Under CONSERVATIVE strictness, these are extracted as EXECUTION edges because the source text names them as explicit required inputs for vendor execution (Specification.md VEEP-REQ-002, VEEP-REQ-005, VEEP-REQ-006, VEEP-REQ-008; Procedure.md Prerequisites). The Procedure.md label "ASSUMPTION, not declared edges" reflects the pre-extraction DECLARED state, not a basis to suppress extraction.
- **TargetLocation for DOCUMENT rows:** All three document prerequisites carry `location TBD` — facility hazardous area drawings, geotechnical basis, and electrical distribution layout are not yet in `_Sources` for this deliverable.
- **`26020-Package_Requirements.docx` PKG-106 slice:** Not extracted during PREPARATION (per `_REFERENCES.md` and Guidance.md HRR-106-04-004). No rows created from that source. Quantities (lux levels, pole specs, foundation loads) remain TBD.
- **No writes outside dependency artifacts.** Source documents, `_REFERENCES.md`, and decomposition files are unchanged.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 13 |
| RETIRED | 0 |
| **Total** | **13** |

**SatisfactionStatus breakdown (ACTIVE rows):**

| SatisfactionStatus | Count |
|---|---|
| TBD | 6 (all ANCHOR rows) |
| PENDING | 7 (all EXECUTION rows) |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — First extraction run. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition: GATE-07_Final_Published_2026-05-24 snapshot. 13 rows extracted (6 ANCHOR + 7 EXECUTION). 0 retired. No warnings.
