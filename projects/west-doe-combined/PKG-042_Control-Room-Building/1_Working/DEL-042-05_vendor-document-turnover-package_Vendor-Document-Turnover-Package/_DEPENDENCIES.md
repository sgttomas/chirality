# Dependencies: DEL-042-05_vendor-document-turnover-package — Vendor Document Turnover Package

**Coordination Mode:** DECLARED
**Dependency tracking mode:** DECLARED + EXTRACTED
**Default maturity threshold:** INITIALIZED
**Register convention:** Prefer `Dependencies.csv` (produced by `TASK + dependency-extract`); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Dependencies.csv produced by dependency-extract run on 2026-05-25 (MODE=UPDATE, STRICTNESS=CONSERVATIVE).

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetRefID / TargetDeliverableID | TargetName | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-042-05-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | WBS-03 | WBS 03 — Control Room Building (PKG-042) | ACTIVE |
| DEP-042-05-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0043 | SOW-0043 — Scope item | ACTIVE |
| DEP-042-05-003 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | GATE-07_Final_Published_2026-05-24 | Gate 7 PROJECT_DECOMP Snapshot | ACTIVE |
| DEP-042-05-004 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-042-04_vendor-engineered-equipment-package_Vendor-Engineered-Equipment-Package | Vendor Engineered Equipment Package (DEL-042-04) | ACTIVE |
| DEP-042-05-005 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-042-06_epc-vendor-package-review-and-acceptance_EPC-Vendor-Package-Review-and-Acceptance | EPC Vendor Package Review and Acceptance (DEL-042-06) | ACTIVE |
| DEP-042-05-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-BE3458FDB4 | Utility Piping interface fact (PKG-042) | ACTIVE |
| DEP-042-05-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-DC78111478 | Electrical Power interface fact (PKG-042) | ACTIVE |
| DEP-042-05-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-F360E6EC35 | I&C / Control Cabling interface fact (PKG-042) | ACTIVE |
| DEP-042-05-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-7F7D8698DC | Structural / Foundations / Supports interface fact (PKG-042) | ACTIVE |

**Total rows:** 9 | **ACTIVE:** 9 | **RETIRED:** 0

**ANCHOR rows:** 2 (1 IMPLEMENTS_NODE, 1 TRACES_TO_REQUIREMENT)
**EXECUTION rows:** 7 (2 UPSTREAM PREREQUISITE, 4 UPSTREAM INTERFACE, 1 DOWNSTREAM HANDOVER)

## Run Notes

- **Run date:** 2026-05-25
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned Datasheet.md, Specification.md, Guidance.md, Procedure.md, _CONTEXT.md
- **ANCHOR_DOC:** Datasheet.md (heuristic: contains identification and attribute tables providing anchor signals)
- **EXECUTION_DOC_ORDER:** Procedure.md (primary workflow), Specification.md (requirements/handoff), Guidance.md (principles/considerations)
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — path confirmed present; used to validate package and deliverable IDs.

**Interface fact rows (DEP-042-05-006 through -009):** The Datasheet Conditions table lists 11 PKG-042 interface facts with explicit vendor-document coverage statements. CONSERVATIVE extraction emits only the four interface facts that carry an explicit vendor-document coverage requirement statement in the Conditions table (Utility Piping, Electrical Power, I&C/Control Cabling, Structural/Foundations/Supports). The remaining seven interface facts (Drain/Containment, Grounding/Bonding, Area/Exterior Lighting, Communications/Network, Building HVAC/Services, Fire & Gas/Safety Systems, Grading/Site Drainage/Spill Containment) appear in the Conditions table with no explicit vendor-document content statement beyond "Interface fact applies to PKG-042" and are therefore not emitted as execution edges under CONSERVATIVE strictness; Specification REQ-042-05-005 requires coverage of all 11 and should drive content completeness at the work level.

**Assumptions and warnings:**
- ASSUMPTION (DEP-042-05-004): DEL-042-04 is treated as the source of vendor engineering design outputs. If vendor engineering originates from an external vendor system not tracked in this deliverable tree, this row should be reviewed and possibly re-typed as EXTERNAL.
- No source gap warnings on anchor extraction; WBS-03 and SOW-0043 both explicitly cited.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 9 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 9 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract run: MODE=UPDATE, STRICTNESS=CONSERVATIVE, DECOMPOSITION=GATE-07 confirmed, 9 ACTIVE rows written. Schema validated VALID.
