# Dependencies: DEL-014-05_vendor-document-turnover-package — Vendor Document Turnover Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is canonical; this file is the human-readable view and index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Run 2026-05-25 — 13 rows extracted (8 ANCHOR, 5 EXECUTION); all ACTIVE.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-014-05-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0015 | Scope decision SOW-0015 — CONTACTOR PANELS - LIGHTING / EXHAUST FAN CONTACTOR PANELS - LOW VOLTAGE | HIGH | ACTIVE |
| DEP-014-05-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | Project Objective OBJ-002 — 03-25 compressor station and liquids hub scope | HIGH | ACTIVE |
| DEP-014-05-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Project Objective OBJ-004 — Vendor-owned package responsibility model | HIGH | ACTIVE |
| DEP-014-05-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 — Facility electrical power basis and electrical interfaces | HIGH | ACTIVE |
| DEP-014-05-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Project Objective OBJ-006 — Controls instrumentation and communications interfaces | HIGH | ACTIVE |
| DEP-014-05-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 — Civil structural site and construction-support scope | HIGH | ACTIVE |
| DEP-014-05-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 — Safety relief regulatory and codes requirements | HIGH | ACTIVE |
| DEP-014-05-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 — Operability maintainability vendor documentation and turnover handoff | HIGH | ACTIVE |
| DEP-014-05-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-014-01_scope-of-work | Scope of Work | HIGH | ACTIVE |
| DEP-014-05-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-014-02_package-datasheet | Package Datasheet | HIGH | ACTIVE |
| DEP-014-05-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-014-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package | HIGH | ACTIVE |
| DEP-014-05-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-014-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | HIGH | ACTIVE |
| DEP-014-05-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | (TargetLocation: _Sources/26020-Package_Requirements.docx) | 26020-Package_Requirements.docx — PKG-014 source slice | MEDIUM | ACTIVE |

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 13 |
| RETIRED | 0 |
| **Total** | **13** |

| SatisfactionStatus | Count |
|---|---|
| TBD | 4 |
| PENDING | 3 |
| IN_PROGRESS | 0 |
| SATISFIED | 0 |
| WAIVED | 0 |
| NOT_APPLICABLE | 0 |

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; source documents found: `Datasheet.md`, `Procedure.md`, `Specification.md`, `Guidance.md`, `_CONTEXT.md`.
- **ANCHOR_DOC:** `Datasheet.md` (highest-confidence anchor match; contains explicit SOW-0015 reference, objectives, and decomposition identifiers).
- **EXECUTION_DOC_ORDER:** `Procedure.md` (primary execution signals), `Specification.md` (requirements/constraints), `Guidance.md` (boundary/trade-off framing).
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — confirmed accessible; SOW-0015 and objective IDs resolved against SCOPE_LEDGER.csv, DELIVERABLE_REGISTER.csv, and OBJECTIVE_REGISTER.csv.
- **Parent anchor:** DEP-014-05-001 — SOW-0015 confirmed in SCOPE_LEDGER.csv and DELIVERABLE_REGISTER.csv. Single IMPLEMENTS_NODE row; no FLOATING_NODE or AMBIGUOUS_ANCHOR warning triggered.
- **26020-Package_Requirements.docx:** Named in Specification R-4 as the authority for source-required vendor documents; PKG-014-specific slice not yet extracted. DEP-014-05-013 emitted as PREREQUISITE/DOCUMENT with Confidence=MEDIUM and SatisfactionStatus=PENDING.
- **INTERFACE_REGISTER.csv signals:** Datasheet.md enumerates seven declared PKG-014 interfaces (IFC-78CF31138D, IFC-31C88BB424, IFC-EF784327FA, IFC-C715E9AA3E, IFC-2D60238809, IFC-52B07B0D36, IFC-53646D26A1). These are interface facts documented within DEL-014-05; no separate dependency rows were emitted per the information-flow-only rule (interfaces are structural adjacency within the package, not external artifact-transfer edges requiring separate rows).
- **Boundary DEL-014-05 / DEL-014-06:** Explicitly stated in Procedure Step 5 — vendor submits here; EPC review evidence lives in DEL-014-06. DEP-014-05-012 captures this as DOWNSTREAM/HANDOVER.
- **Boundary DEL-014-05 / DEL-014-04:** Explicitly stated in Procedure Step 4 — DEL-014-04 engineering output feeds submittals. DEP-014-05-011 captures this as UPSTREAM/PREREQUISITE.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract skill run; MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. 13 rows extracted (8 ANCHOR, 5 EXECUTION), all ACTIVE. Decomposition confirmed at GATE-07_Final_Published_2026-05-24. No FLOATING_NODE, AMBIGUOUS_ANCHOR, or MISSING_DECOMPOSITION warnings.
