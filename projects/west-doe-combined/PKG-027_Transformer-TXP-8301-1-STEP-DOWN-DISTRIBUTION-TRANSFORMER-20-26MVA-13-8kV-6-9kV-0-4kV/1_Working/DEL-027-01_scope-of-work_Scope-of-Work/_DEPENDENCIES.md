# Dependencies: DEL-027-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

**Total ACTIVE rows:** 17
**ANCHOR rows (ACTIVE):** 9 (1 IMPLEMENTS_NODE + 8 TRACES_TO_REQUIREMENT)
**EXECUTION rows (ACTIVE):** 8

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-027-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-027 | Transformer TXP-8301-1 — PKG-027 package node | HIGH | ACTIVE |
| DEP-027-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | Objective OBJ-001 (integrated facility scope) | MEDIUM | ACTIVE |
| DEP-027-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Objective OBJ-004 | MEDIUM | ACTIVE |
| DEP-027-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Objective OBJ-005 | MEDIUM | ACTIVE |
| DEP-027-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Objective OBJ-006 | MEDIUM | ACTIVE |
| DEP-027-01-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Objective OBJ-008 | MEDIUM | ACTIVE |
| DEP-027-01-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Objective OBJ-009 | MEDIUM | ACTIVE |
| DEP-027-01-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Objective OBJ-010 | MEDIUM | ACTIVE |
| DEP-027-01-009 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0028 | CoA scope reference SOW-0028 | HIGH | ACTIVE |
| DEP-027-01-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-027-02_package-datasheet | Package Datasheet | HIGH | ACTIVE |
| DEP-027-01-011 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-027-03_construction-work-package | Construction Work Package | HIGH | ACTIVE |
| DEP-027-01-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-027-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package | HIGH | ACTIVE |
| DEP-027-01-013 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-027-05_vendor-document-turnover-package | Vendor Document Turnover Package | MEDIUM | ACTIVE |
| DEP-027-01-014 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-027-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | HIGH | ACTIVE |
| DEP-027-01-015 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-7FDEAE3A5F | Interface: Electrical Power | HIGH | ACTIVE |
| DEP-027-01-016 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-868150D715 | Interface: Grounding / Bonding | HIGH | ACTIVE |
| DEP-027-01-017 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | DOCUMENT | — | DBM-Deepcut Electrical Design Basis | HIGH | ACTIVE |

## Run Notes

**Run timestamp:** 2026-05-25
**Mode:** UPDATE
**Strictness:** CONSERVATIVE
**Source docs scanned (AUTO):** Datasheet.md (ANCHOR_DOC — matches `datasheet`); Specification.md, Guidance.md, Procedure.md (EXECUTION_DOC_ORDER)
**Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
**Consumer context:** NONE

**Defaults applied:**
- SOURCE_DOCS: AUTO — all four files in deliverable folder scanned (excluding _* artifacts).
- ANCHOR_DOC: Datasheet.md (highest-confidence anchor match by filename heuristic `datasheet`).
- EXECUTION_DOC_ORDER: Specification.md, Guidance.md, Procedure.md.
- DECOMPOSITION_PATH: Gate-07 snapshot located under `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` per `_REFERENCES.md` pointer. Anchors validated against DELIVERABLE_REGISTER.csv, PACKAGE_REGISTER.csv, and OBJECTIVE_DELIVERABLE_MAP.csv.

**Decisions and assumptions:**
- IMPLEMENTS_NODE anchor DEP-027-01-001 assigned to PKG-027 (confirmed in DELIVERABLE_REGISTER.csv, PACKAGE_REGISTER.csv). TargetType=WBS_NODE used as PKG-027 is the parent package/decomposition node. FACT.
- TRACES_TO_REQUIREMENT rows DEP-027-01-002 through DEP-027-01-008 use OBJ-001, OBJ-004–OBJ-010 from OBJECTIVE_DELIVERABLE_MAP.csv. Carried as ASSUMPTION (PACKAGE_HEURISTIC mode, per REQ-027-01-009 and DELIVERABLE_REGISTER.csv note). Confidence=MEDIUM.
- DEP-027-01-009: SOW-0028 appears as the CoA/scope tracking reference in DELIVERABLE_REGISTER.csv for all PKG-027 deliverables. Recorded as TRACES_TO_REQUIREMENT with Confidence=HIGH. FACT.
- DOWNSTREAM HANDOVER rows DEP-027-01-010 through DEP-027-01-014 are drawn from explicit Procedure.md Prerequisites statement ("downstream consumers include DEL-027-02 … DEL-027-06"). FACT.
- INTERFACE rows DEP-027-01-015 and DEP-027-01-016 drawn from Datasheet.md Conditions table citing INTERFACE_REGISTER.csv rows IFC-7FDEAE3A5F and IFC-868150D715 explicitly. TargetType=DOCUMENT used since IFC IDs are not DELIVERABLE or PACKAGE type. FACT.
- CONSTRAINT row DEP-027-01-017 drawn from DBM electrical design basis cited explicitly across all four source documents as the authoritative constraint for 6.9 kV NGR grounding, CEC spacing, and foundation/containment requirements. FACT.
- No rows were emitted for the remaining five interface types (Area/Exterior Lighting, I&C/Control Cabling, Communications/Network, Maintenance Access, Structural/Foundations/Supports) in the INTERFACE_REGISTER.csv list — these are listed in Datasheet.md and Specification.md as applicable interface facts but without explicit IFC IDs cited in the Conditions table. CONSERVATIVE: these are captured in the Scope of Work content but did not meet the bar for separate EXECUTION rows under CONSERVATIVE strictness (no IFC reference ID given).

**Integrity check — parent anchor:** 1 IMPLEMENTS_NODE row (DEP-027-01-001). OK.
**Integrity check — no AMBIGUOUS_ANCHOR:** confirmed single parent anchor.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 17 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 17 |

All rows are open / TBD — no closure has been assessed on this first extraction run.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First extraction run. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition: Gate-07 snapshot. Source docs: Datasheet.md (anchor), Specification.md, Guidance.md, Procedure.md (execution). Produced 17 ACTIVE rows (9 ANCHOR, 8 EXECUTION). Schema: VALID (29 columns, v3.1). No warnings.
