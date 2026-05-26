# Specification — DEL-103-01 Scope of Work (Pipe Rack Modules)

> Normative requirements for the EPC Integrator Scope of Work artifact for package PKG-103. Requirements are grounded in PROJECT_DECOMP Gate-07 registers and DBM-Comp_and_Liquids; inferences are labelled ASSUMPTION.

## Scope

### In Scope (covers)

- A single, complete EPC Integrator Scope of Work for package PKG-103 "Pipe Rack Modules" (workbook tracking number 26020-03-36-003, WBS 03). [PACKAGE_REGISTER row 104; DELIVERABLE_REGISTER row 584]
- Statement of the workbook-defined package function: carry 'Pipe Rack Modules' as a distinct flat project package for WBS 03. [SCOPE_LEDGER SOW-0259]
- Identification of all interface types attached to PKG-103: Process Piping; Utility Piping; Relief / Flare / Vent; Electrical Power; EHT; I&C / Control Cabling; Communications / Network; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. [PACKAGE_REGISTER row 104; INTERFACE_REGISTER rows 909-917]
- Identification of the EPC Integrator as the design owner for pipe racks and pipe rack modules. [INTERFACE_REGISTER rows 909-917 Gate 6 disposition note]
- Tagged-equipment / package identity list, package function and integration narrative, and responsibility assignment record (the four anticipated artifacts). [DELIVERABLE_REGISTER row 584]

### Out of Scope (excludes)

- Detailed design, calculations, drawings, and bills of material for the rack modules themselves (carried separately under DEL-103-04 and the Package Datasheet DEL-103-02). [DELIVERABLE_REGISTER rows 585, 587]
- Construction work-package details (carried under DEL-103-03). [DELIVERABLE_REGISTER row 586]
- Process and utility piping commodity design carried on the racks (separate piping packages). ASSUMPTION based on package-name boundary; rack-supported commodities to be confirmed against plot plan/model. [PACKAGE_REGISTER row 104 note]
- Package-specific exclusions beyond the above are `TBD; no package-specific exclusions stated in source materials`. [PACKAGE_REGISTER row 104]

## Requirements

| ReqID | Requirement | Source |
|---|---|---|
| SPEC-103-01-R01 | The Scope of Work SHALL identify the package as PKG-103 "Pipe Rack Modules", workbook tracking number 26020-03-36-003, WBS 03, Structural discipline. | PACKAGE_REGISTER row 104 |
| SPEC-103-01-R02 | The Scope of Work SHALL state the workbook-defined package function: workbook-defined Structural package for 'Pipe Rack Modules' under WBS 03 with recorded physical interfaces. | PACKAGE_REGISTER row 104; SCOPE_LEDGER SOW-0259 |
| SPEC-103-01-R03 | The Scope of Work SHALL assign design ownership of pipe racks and pipe rack modules exclusively to the EPC Integrator, citing the Gate 6 disposition. | INTERFACE_REGISTER rows 909-917 (Gate 6 note) |
| SPEC-103-01-R04 | The Scope of Work SHALL enumerate every interface type attached to PKG-103 in the interface register: Process Piping; Utility Piping; Relief / Flare / Vent; Electrical Power; EHT; I&C / Control Cabling; Communications / Network; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. | INTERFACE_REGISTER rows 909-917; PACKAGE_REGISTER row 104 |
| SPEC-103-01-R05 | The Scope of Work SHALL include a whole-facility integration narrative for the rack modules (relationship to compressor station, liquids hub, electrical buildings, utilities, and site grading). | `_CONTEXT.md` Scope; DBM-Comp_and_Liquids line 38 |
| SPEC-103-01-R06 | The Scope of Work SHALL declare the four anticipated artifacts: (a) package scope of work, (b) tagged equipment and package identity list, (c) package function and integration narrative, (d) responsibility assignment record. | DELIVERABLE_REGISTER row 584; `_CONTEXT.md` |
| SPEC-103-01-R07 | The Scope of Work SHALL record traceability to scope item SOW-0259 and to objectives OBJ-002, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010. | SCOPE_LEDGER row 260; DELIVERABLE_REGISTER row 584 |
| SPEC-103-01-R08 | The Scope of Work SHALL note that rack-supported commodities are to be confirmed against the plot plan and 3D model, and SHALL mark unresolved commodity lists as TBD until confirmed. | PACKAGE_REGISTER row 104 note |
| SPEC-103-01-R09 | The Scope of Work SHALL surface DEC-001 as an attached open decision/issue against SOW-0259 and SHALL state it is unresolved at this revision. | SCOPE_LEDGER row 260 |
| SPEC-103-01-R10 | The Scope of Work SHALL identify the final geotechnical report as a required upstream input for rack-foundation design closure. | DBM-Comp_and_Liquids line 688 |
| SPEC-103-01-R11 | The Scope of Work SHALL state that outdoor pipe racks are treated as general purpose non-hazardous areas unless detailed classification drawings identify otherwise. | DBM-Comp_and_Liquids line 722 |
| SPEC-103-01-R12 | The Scope of Work SHALL state foundation design considerations to be carried into rack foundation/support specification: equipment loads, snow/wind/seismic, frost protection, vibration, settlement, and maintenance access (equipment-specific foundation and anchorage checks for pipe racks). | DBM-Comp_and_Liquids line 700 |
| SPEC-103-01-R13 | Tagged-equipment list completeness SHALL be marked TBD where the underlying plot plan/model has not yet been issued; values SHALL NOT be invented. ASSUMPTION: list will be closed when plot plan/model is available. | PACKAGE_REGISTER row 104 note; `_CONTEXT.md` |
| SPEC-103-01-R14 | The Scope of Work SHALL cross-reference its three sibling deliverables: DEL-103-02 (Package Datasheet), DEL-103-03 (Construction Work Package), DEL-103-04 (EPC/Structural Discipline Production Package). | SCOPE_LEDGER row 260; DELIVERABLE_REGISTER rows 585-587 |

## Standards

| Standard | Applicability | Location | Source |
|---|---|---|---|
| API RP 505 | Hazardous-area classification basis for process modules/buildings; cited as the basis for fugitive-emission-driven Zone 2 designations. Applicability to outdoor pipe racks: general-purpose non-hazardous unless classification drawings indicate otherwise. | DBM-Comp_and_Liquids line 722 | DBM-Comp_and_Liquids |
| Geotechnical report (project-specific) | Required upstream of foundation design closure (rack supports). | DBM-Comp_and_Liquids line 688 | DBM-Comp_and_Liquids |
| Snow/wind/seismic design criteria | Foundation/anchorage design basis. Specific code editions and load values: `location TBD`. ASSUMPTION: provincial building code applies. | DBM-Comp_and_Liquids line 700 | DBM-Comp_and_Liquids |
| Workbook Packages row 104 (`26020-Packages_Interfaces_4_export.xlsx`) | Authoritative package definition. Source is binary; content mirrored in PACKAGE_REGISTER row 104. | row 104 | PACKAGE_REGISTER row 104 |
| `26020-Package_Requirements.docx` package heading for PKG-103 | Potentially applicable; `location TBD` — no PKG-103 heading located in accessible derivative sources. | TBD | TBD |

## Verification

| ReqID | Verification approach |
|---|---|
| R01-R02 | Inspection of Scope of Work header and identity section against PACKAGE_REGISTER row 104. |
| R03 | Inspection of responsibility-assignment record against INTERFACE_REGISTER Gate 6 disposition. |
| R04 | Checklist comparison of enumerated interface types against the nine interface rows (IFC-1B5D83EC66 through IFC-BC9813EE49). |
| R05 | Human review of integration-narrative section for facility-level coverage. |
| R06 | Section-presence inspection for the four anticipated artifacts. |
| R07 | Traceability table review against SCOPE_LEDGER and OBJECTIVE_REGISTER. |
| R08, R13 | Inspection that commodity/tag lists carry TBD markers and reference to plot plan/model confirmation. |
| R09 | Inspection of open-issue section for DEC-001. |
| R10-R12 | Inspection that geotechnical-input, hazardous-area treatment, and foundation-design considerations are stated. |
| R14 | Cross-reference table inspection. |

## Documentation

Required artifacts produced by this deliverable (per `_CONTEXT.md` / DELIVERABLE_REGISTER row 584):

1. Package scope of work (this deliverable's primary artifact).
2. Tagged equipment and package identity list (may be TBD-marked where plot plan/model is pending).
3. Package function and integration narrative.
4. Responsibility assignment record (RACI or equivalent), naming the EPC Integrator as design owner for the rack modules per Gate 6.

Supporting record: this Specification, the Datasheet, Guidance, and Procedure within `{DELIVERABLE_PATH}` constitute the production record for Gate 5 review.
