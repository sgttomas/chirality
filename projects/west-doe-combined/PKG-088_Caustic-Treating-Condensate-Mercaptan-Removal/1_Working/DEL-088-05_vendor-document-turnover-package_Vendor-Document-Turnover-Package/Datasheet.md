# Datasheet — DEL-088-05 Vendor Document Turnover Package

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-088-05_vendor-document-turnover-package |
| Name | Vendor Document Turnover Package |
| ParentPackageID | PKG-088 |
| ParentWorkbook | 88 — Caustic Treating (Condensate Mercaptan Removal) |
| Discipline | Mechanical |
| Type | Vendor Document Turnover |
| ResponsibleParty | Package Vendor (authoring); EPC Integrator (interface/integration review) |
| Source Reference | Workbook Packages row 50; 26020-Package_Requirements.docx package heading 41 (location TBD — locally inaccessible) |
| Decomposition Basis | GATE-07 Final Published PROJECT_DECOMP snapshot (2026-05-24) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package subject equipment | Non-regenerative caustic mercaptan treating unit for C5+ condensate | DBM-Comp_and_Liquids §"Condensate Mercaptan Treating" (line 387) |
| Treating technology | Non-regenerative caustic mercaptan treating (Merichem or equivalent) | DBM-Comp_and_Liquids §"Condensate Mercaptan Treating" (line 389) |
| Treating capacity | 20,000 bbl/d C5+ condensate | DBM-Comp_and_Liquids §"Condensate Mercaptan Treating" (line 389) |
| Vendor document register requirement | Mechanical package deliverables shall include vendor document registers | DBM-Comp_and_Liquids §"Mechanical Package Structure" (line 617) |
| Covered SOW items | SOW-0055, SOW-0056, SOW-0057, SOW-0058 | _CONTEXT.md |
| Supported objectives | OBJ-002, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (ASSUMPTION: package-grouping heuristic) | _CONTEXT.md; OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Turnover destination | EPC Integrator (interface/integration review) then Owner | _CONTEXT.md; ASSUMPTION on Owner final receipt |
| Turnover sequencing trigger | Vendor package readiness milestones (FAT, shipment, site acceptance) | TBD — not explicitly stated in accessible sources |
| Required submittal language | English | TBD (location TBD — 26020-Package_Requirements.docx inaccessible) |
| Document classification | Source-required vendor documentation vs. registered submittals | _CONTEXT.md Anticipated Artifacts |

## Construction

| Component | Description | Source |
|---|---|---|
| Vendor Document Register | Index of all vendor documents produced for the package, with revision and status columns | DBM-Comp_and_Liquids line 617; _CONTEXT.md |
| Vendor Document Submittals | The submitted vendor documents themselves (datasheets, drawings, manuals, certificates) | _CONTEXT.md |
| Source-required documentation | Documents explicitly required by 26020-Package_Requirements.docx package heading 41 | _REFERENCES.md (location TBD — inaccessible) |
| Turnover Records | Acceptance/sign-off records evidencing receipt by EPC Integrator | _CONTEXT.md; details TBD |

## References

- DBM-Comp_and_Liquids — `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (accessible)
- 26020-Package_Requirements.docx package heading 41 (referenced by decomposition; locally inaccessible — content TBD)
- Workbook Packages row 50 (referenced by decomposition; locally inaccessible — content TBD)
- GATE-07 snapshot — DELIVERABLE_REGISTER.csv, PACKAGE_REGISTER.csv, OBJECTIVE_DELIVERABLE_MAP.csv
