# Dependencies: DEL-066-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (Dependencies.csv v3.1 generated)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

---

## Extracted Dependency Register

**Schema version:** v3.1
**Total rows (ACTIVE):** 14
**ANCHOR rows (ACTIVE):** 5
**EXECUTION rows (ACTIVE):** 9
**RETIRED rows:** 0

### ANCHOR Rows (Pass 1 — Tree)

| DependencyID | AnchorType | Direction | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence |
|---|---|---|---|---|---|---|
| DEP-066-04-001 | IMPLEMENTS_NODE | UPSTREAM | PACKAGE | PKG-066 | Tanks, Condendate (API 650) 4-25 | HIGH |
| DEP-066-04-002 | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | SOW-0205 | SOW-0205 | HIGH |
| DEP-066-04-003 | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | SOW-0206 | SOW-0206 | HIGH |
| DEP-066-04-004 | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | SOW-0207 | SOW-0207 | HIGH |
| DEP-066-04-005 | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | SOW-0208 | SOW-0208 | HIGH |

### EXECUTION Rows (Pass 2 — DAG)

| DependencyID | Direction | DependencyType | TargetType | TargetDeliverableID / TargetRefID | TargetName | Confidence |
|---|---|---|---|---|---|---|
| DEP-066-04-006 | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-066-01_scope-of-work | Scope of Work | HIGH |
| DEP-066-04-007 | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-066-02_package-datasheet | Package Datasheet | HIGH |
| DEP-066-04-008 | UPSTREAM | INTERFACE | DELIVERABLE | DEL-066-03_construction-work-package | Construction Work Package | HIGH |
| DEP-066-04-009 | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-066-05_vendor-document-turnover-package | Vendor Document Turnover Package | HIGH |
| DEP-066-04-010 | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-066-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | HIGH |
| DEP-066-04-011 | UPSTREAM | INTERFACE | EXTERNAL | P-9210-1 / P-9220-1 | Condensate Transfer Pumps | HIGH |
| DEP-066-04-012 | DOWNSTREAM | INTERFACE | EXTERNAL | Module-930-VRU | VRU Suction Header — Module 930 | MEDIUM |
| DEP-066-04-013 | UPSTREAM | PREREQUISITE | EXTERNAL | CIV-235633-5002 | Plot Plan Drawing CIV-235633-5002 | MEDIUM |
| DEP-066-04-014 | UPSTREAM | PREREQUISITE | EXTERNAL | 26020-PKG-REQ-HDG-21 | 26020-Package_Requirements.docx Package Heading 21 | MEDIUM |

---

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 14 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 14 |

---

## Run Notes

- **Run date:** 2026-05-25
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; candidate source documents: `Datasheet.md`, `Guidance.md`, `Procedure.md`, `Specification.md`, `_CONTEXT.md`, `_REFERENCES.md`.
- **DOC_ROLE_MAP:** DEFAULT — ANCHOR_DOC: `Datasheet.md` (contains "datasheet" keyword; explicit identification, parentage, and SOW items). EXECUTION_DOCS: `Procedure.md` (contains "procedure"), `Specification.md` (contains "spec"), `Guidance.md`, `_CONTEXT.md`.
- **ANCHOR_DOC:** `Datasheet.md` (highest-confidence anchor per DOC_ROLE_MAP heuristic).
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — used to validate PKG-066 parentage and resolve sibling deliverable IDs (DEL-066-01 through DEL-066-06). All six sibling IDs confirmed in DELIVERABLE_REGISTER.csv.

**Parent anchor check:** 1 IMPLEMENTS_NODE row (DEP-066-04-001, targeting PKG-066 as PACKAGE). Note: IMPLEMENTS_NODE points to the parent PACKAGE node rather than a WBS_NODE because the decomposition structure is package-based and PKG-066 is the canonical parent identifier. This is consistent with the project decomposition model.

**Warnings:**
- [WARNING] `26020-Package_Requirements.docx` (package heading 21) is referenced in Specification and _CONTEXT.md but is not text-readable in this run (.docx format). CONFLICT C-03 documented in Guidance.md. Row DEP-066-04-014 created with `location TBD`; requirement clause content not resolved.
- [WARNING] Plot plan drawing CIV-235633-5002 is flagged as TBD/outside accessible sources in the DBM. Row DEP-066-04-013 created with `location TBD`.
- [WARNING] VRU/Module 930 deliverable ID not resolved from accessible decomposition scope (VRU is identified as a separate package but its PKG/DEL IDs are not present in the visible portion of DELIVERABLE_REGISTER.csv). Row DEP-066-04-012 uses TargetType=EXTERNAL and TargetRefID=Module-930-VRU.
- [WARNING] Condensate transfer pumps P-9210-1 / P-9220-1 are identified as a separate package per Specification but their PKG/DEL IDs are not resolved from accessible decomposition. Row DEP-066-04-011 uses TargetType=EXTERNAL.

---

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full two-pass extraction (dependency-extract skill, UPDATE/CONSERVATIVE). Dependencies.csv v3.1 created. 14 ACTIVE rows: 5 ANCHOR (1 IMPLEMENTS_NODE, 4 TRACES_TO_REQUIREMENT), 9 EXECUTION (3 UPSTREAM/DELIVERABLE, 2 DOWNSTREAM/DELIVERABLE, 2 EXTERNAL/UPSTREAM, 1 EXTERNAL/DOWNSTREAM, 1 EXTERNAL/UPSTREAM/plot-plan). Decomposition path confirmed at GATE-07_Final_Published_2026-05-24. Warnings recorded above.
