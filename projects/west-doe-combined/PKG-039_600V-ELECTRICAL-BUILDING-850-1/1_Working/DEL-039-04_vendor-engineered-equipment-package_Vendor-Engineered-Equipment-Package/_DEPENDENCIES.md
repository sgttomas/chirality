# Dependencies: DEL-039-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1 schema). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` generated 2026-05-25. 17 rows total; 17 ACTIVE, 0 RETIRED.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-039-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0040 | SOW-0040 | ACTIVE |
| DEP-039-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | OBJ-001 | ACTIVE |
| DEP-039-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | OBJ-004 | ACTIVE |
| DEP-039-04-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | OBJ-005 | ACTIVE |
| DEP-039-04-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | OBJ-006 | ACTIVE |
| DEP-039-04-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | OBJ-007 | ACTIVE |
| DEP-039-04-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | OBJ-008 | ACTIVE |
| DEP-039-04-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | OBJ-009 | ACTIVE |
| DEP-039-04-009 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | OBJ-010 | ACTIVE |
| DEP-039-04-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-039-01_scope-of-work | Scope of Work | ACTIVE |
| DEP-039-04-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-039-02_package-datasheet | Package Datasheet | ACTIVE |
| DEP-039-04-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-039-05_vendor-document-turnover-package | Vendor Document Turnover Package | ACTIVE |
| DEP-039-04-013 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-039-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | ACTIVE |
| DEP-039-04-014 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-C1DF6B8DD9 | Electrical Power Interface | ACTIVE |
| DEP-039-04-015 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-9653B84E14 | Grounding / Bonding Interface | ACTIVE |
| DEP-039-04-016 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-E3D0A5A836 | Structural / Foundations / Supports Interface | ACTIVE |
| DEP-039-04-017 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-3F18DB0D3A | I&C / Control Cabling Interface | ACTIVE |

**Anchor rows:** 9 (1 IMPLEMENTS_NODE + 8 TRACES_TO_REQUIREMENT)
**Execution rows:** 8 (2 UPSTREAM PREREQUISITE + 2 DOWNSTREAM HANDOVER + 4 UPSTREAM INTERFACE)

Note: The Datasheet `Conditions` table lists 12 applicable interface rows from `INTERFACE_REGISTER.csv`. Four representative interfaces with high design-critical signal are extracted here (Electrical Power, Grounding/Bonding, Structural/Foundations/Supports, I&C/Control Cabling). The remaining eight interfaces (Utility Piping `IFC-A257E2C89C`, Drain/Containment `IFC-5C80D8C3EC`, Area/Exterior Lighting `IFC-4BC9BD20C1`, Communications/Network `IFC-B95212AB85`, Building HVAC/Services `IFC-D8A8F7FEBC`, Fire & Gas/Safety Systems `IFC-9C0AFE36A2`, Maintenance Access `IFC-D971A17948`, Grading/Site Drainage/Spill Containment `IFC-50A5B3F280`) are explicitly required per REQ-039-04-003 and Specification.md; they may be added in a future refresh run if downstream consumers require individual edge resolution.

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **DECOMPOSITION_PATH used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
- **SOURCE_DOCS scanned:** `_CONTEXT.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`
- **ANCHOR_DOC:** `_CONTEXT.md` (contains explicit SOW reference and objective list)
- **EXECUTION_DOC_ORDER:** `Procedure.md` (primary), `Specification.md`, `Datasheet.md`
- Decomposition confirmed: `SOW-0040` confirmed in `SCOPE_LEDGER.csv`; `DEL-039-04` confirmed in `DELIVERABLE_REGISTER.csv`; all objective IDs confirmed in `OBJECTIVE_REGISTER.csv`.
- Only 4 of 12 applicable interface edges extracted (CONSERVATIVE mode, highest-signal interfaces only). All 12 are explicitly required per REQ-039-04-003 and are noted above for downstream refresh.
- No `_REFERENCES.md` entries pointed to external document paths resolvable to a different TargetLocation beyond the INTERFACE_REGISTER.csv path used.

## Lifecycle Summary

| Class | Count | ACTIVE | RETIRED | SATISFIED | PENDING | TBD |
|---|---|---|---|---|---|---|
| ANCHOR | 9 | 9 | 0 | 0 | 0 | 9 |
| EXECUTION | 8 | 8 | 0 | 0 | 0 | 8 |
| **Total** | **17** | **17** | **0** | **0** | **0** | **17** |

SatisfactionStatus is `TBD` for all rows (first extraction; no closure evidence available).

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract skill run; UPDATE mode; CONSERVATIVE strictness; decomposition GATE-07_Final_Published_2026-05-24 used; 17 rows extracted (9 ANCHOR + 8 EXECUTION); no pre-existing rows; schema validation VALID.
