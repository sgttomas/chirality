# Dependencies: DEL-037-05_vendor-document-turnover-package — Vendor Document Turnover Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1); this file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

15 rows extracted (15 ACTIVE, 0 RETIRED).

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-037-05-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | WBS-01 | WBS 01 — 5kV SWITCHGEAR ELECTRICAL BUILDING (880-1) | HIGH | ACTIVE |
| DEP-037-05-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0038 | Scope of Work item SOW-0038 | HIGH | ACTIVE |
| DEP-037-05-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | OBJ-001 — Provide the 04-25 Deepcut facility scope | HIGH | ACTIVE |
| DEP-037-05-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | OBJ-004 — Execute each electrical and mechanical equipment package as vendor-owned | HIGH | ACTIVE |
| DEP-037-05-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | OBJ-005 — Provide and integrate the facility electrical power basis | HIGH | ACTIVE |
| DEP-037-05-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | OBJ-006 — Provide and integrate controls instrumentation communications | HIGH | ACTIVE |
| DEP-037-05-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | OBJ-007 — Provide and integrate shared utilities and ancillary support systems | HIGH | ACTIVE |
| DEP-037-05-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | OBJ-008 — Provide civil structural site buildings foundations scope | HIGH | ACTIVE |
| DEP-037-05-009 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | OBJ-009 — Carry sour-service safety relief flare and regulatory requirements | HIGH | ACTIVE |
| DEP-037-05-010 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | OBJ-010 — Maintain operability maintainability vendor-documentation commissioning turnover | HIGH | ACTIVE |
| DEP-037-05-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-037-01_scope-of-work | Scope of Work | HIGH | ACTIVE |
| DEP-037-05-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-037-02_package-datasheet | Package Datasheet | HIGH | ACTIVE |
| DEP-037-05-013 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-037-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | HIGH | ACTIVE |
| DEP-037-05-014 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | PRQ-009 | Vendor Document Index (PRQ-009) | MEDIUM | ACTIVE |
| DEP-037-05-015 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DOC-008 | Vendor Document Control Procedure (DOC-008) | MEDIUM | ACTIVE |

## Run Notes

- **Run date:** 2026-05-25
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; used Datasheet.md (ANCHOR_DOC), Specification.md, Procedure.md, _CONTEXT.md as primary sources.
- **ANCHOR_DOC:** Datasheet.md (matched heuristic: `datasheet` in filename).
- **EXECUTION_DOC_ORDER:** Specification.md, Procedure.md (matched heuristic: `spec`, `procedure` in filename).
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — resolved from `_CONTEXT.md` Decomposition Reference. GATE-07 DELIVERABLE_REGISTER.csv used to confirm PKG-037 / DEL-037 family IDs and resolve canonical deliverable names.
- **Parent anchor:** DEP-037-05-001 — WBS-01 resolved from Datasheet.md Identification table and Workbook Packages row 39.
- **Trace anchors:** SOW-0038 and OBJ-001 through OBJ-010 — all explicitly listed in _CONTEXT.md and confirmed in GATE-07 DELIVERABLE_REGISTER.csv row DEL-037-05.
- **Execution edges:** DEL-037-01 and DEL-037-02 as upstream prerequisites (vendor documentation develops from the EPC SOW and Package Datasheet, stated explicitly in Specification.md Scope); DEL-037-06 as downstream handover (explicitly named in Specification.md and Datasheet.md Construction table as the EPC acceptance deliverable that receives this package); PRQ-009 and DOC-008 as upstream document prerequisites (explicitly cited in _Sources/26020-Package_Requirements.docx Core vendor documents table, referenced in Datasheet.md Attributes).
- **Interfaces not extracted as dependencies:** The twelve PKG-037 interface facts (Utility Piping, Drain/Containment, Electrical Power, etc.) are noted in Datasheet.md Conditions but are interface obligations carried within the vendor documentation content, not explicit information-transfer dependencies between deliverables. They are not extracted as EXECUTION edges under CONSERVATIVE strictness.
- **[WARNING] MISSING_DECOMPOSITION_FOLDER:** The BRIEF specified `DECOMPOSITION_PATH: /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/` which does not exist as a top-level folder. Resolved to canonical location `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` via `_CONTEXT.md` Decomposition Reference. No anchor validation gap — all IDs confirmed against GATE-07 DELIVERABLE_REGISTER.csv.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 15 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 15 |

| DependencyClass | ACTIVE count |
|---|---|
| ANCHOR | 10 |
| EXECUTION | 5 |

Parent anchor (IMPLEMENTS_NODE): 1 — DEP-037-05-001 (WBS-01). No floating node warning.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract skill run; MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE; 15 rows extracted (10 ANCHOR + 5 EXECUTION); all ACTIVE; schema valid.
