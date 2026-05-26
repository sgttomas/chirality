# Dependencies: DEL-072-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Total rows: 15 | ACTIVE: 15 | RETIRED: 0

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-072-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-072 | Truck Product Loading Unit 4-25 | HIGH | ACTIVE |
| DEP-072-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | Provide the 04-25 Deepcut facility scope | HIGH | ACTIVE |
| DEP-072-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-003 | Preserve commercial stream disposition and metering accountability | HIGH | ACTIVE |
| DEP-072-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Execute each electrical and mechanical equipment package as a vendor-owned package | HIGH | ACTIVE |
| DEP-072-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Provide and integrate facility electrical power basis and interfaces | HIGH | ACTIVE |
| DEP-072-01-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Provide and integrate controls instrumentation and package control interfaces | HIGH | ACTIVE |
| DEP-072-01-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | Provide and integrate shared utilities and ancillary support systems | HIGH | ACTIVE |
| DEP-072-01-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Provide civil structural site buildings foundations grading containment and construction-support scope | HIGH | ACTIVE |
| DEP-072-01-009 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Carry sour-service safety relief shutdown environmental and regulatory requirements into package scopes | HIGH | ACTIVE |
| DEP-072-01-010 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Maintain operability maintainability vendor-documentation commissioning turnover and controlled open-item closure evidence | HIGH | ACTIVE |
| DEP-072-01-011 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-072-02_package-datasheet | Package Datasheet | HIGH | ACTIVE |
| DEP-072-01-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-072-03_construction-work-package | Construction Work Package | HIGH | ACTIVE |
| DEP-072-01-013 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-072-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package | HIGH | ACTIVE |
| DEP-072-01-014 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-072-05_vendor-document-turnover-package | Vendor Document Turnover Package | HIGH | ACTIVE |
| DEP-072-01-015 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-072-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | HIGH | ACTIVE |

## Run Notes

**Run date:** 2026-05-25
**Mode:** UPDATE
**Strictness:** CONSERVATIVE
**Consumer context:** NONE

**Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
- Note: The `DECOMPOSITION_PATH` parameter referenced `GATE-07_Final_Published_2026-05-24` at a different parent path (`projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/`), which does not exist. The correct canonical location under `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` was used instead. Recorded per skill run-note requirement.

**Source documents scanned (AUTO):**
- `_CONTEXT.md` — ANCHOR_DOC (contains identity, parent package, objective list)
- `Specification.md` — primary source for scope, requirements, documentation section
- `Guidance.md` — execution flow context, OBJ-004/OBJ-009/OBJ-010 citations, downstream consumers
- `Procedure.md` — explicit downstream consumer handoff steps
- `Datasheet.md` — conditions and interface types (no additional unique dependency signals beyond Specification.md)

**ANCHOR_DOC:** `_CONTEXT.md` (identity + parent + objective list — highest-confidence anchor signals per DEFAULT heuristic)

**Pass 1 (ANCHOR) result:**
- 1 IMPLEMENTS_NODE parent anchor emitted for PKG-072. No AMBIGUOUS_ANCHOR.
- 9 TRACES_TO_REQUIREMENT anchors emitted for OBJ-001 and OBJ-003 through OBJ-010 (note: OBJ-002 is not in the supported-objectives list for this deliverable per DELIVERABLE_REGISTER.csv row 558).

**Pass 2 (EXECUTION) result:**
- 5 DOWNSTREAM HANDOVER edges emitted for sibling deliverables DEL-072-02 through DEL-072-06.
- No UPSTREAM execution edges found: Procedure.md states "no declared upstream dependencies" and sources (PACKAGE_REGISTER.csv, SCOPE_LEDGER.csv, etc.) are decomposition/source inputs, not execution deliverable dependencies.

**Warnings:** None. No FLOATING_NODE. No AMBIGUOUS_ANCHOR. Decomposition snapshot resolved successfully.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 15 |
| RETIRED | 0 |
| **Total** | **15** |

| SatisfactionStatus | Count |
|---|---|
| TBD | 15 |

| DependencyClass | ACTIVE Count |
|---|---|
| ANCHOR | 10 |
| EXECUTION | 5 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full two-pass extraction (MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE). Created Dependencies.csv v3.1 with 15 rows (10 ANCHOR, 5 EXECUTION). All ACTIVE. Decomposition: GATE-07_Final_Published_2026-05-24. No warnings.
