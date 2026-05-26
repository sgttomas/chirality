# Datasheet — DEL-079-01 Scope of Work: Instrument Air Building (PKG-079)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-079-01_scope-of-work | _CONTEXT.md |
| Deliverable Name | Scope of Work | _CONTEXT.md |
| Deliverable Type | EPC Scope of Work | _CONTEXT.md |
| Parent Package | PKG-079 — Instrument Air Building | _CONTEXT.md; PACKAGE_REGISTER.csv row PKG-079 |
| Workbook Row | 69 | PACKAGE_REGISTER.csv (workbook_row=69) |
| Discipline | Mechanical | PACKAGE_REGISTER.csv |
| WBS | 01 | PACKAGE_REGISTER.csv |
| Tag (package identity) | 26020-01-PT-39-001 — Instrument Air Building | PACKAGE_REGISTER.csv (Tag) |
| Tracking Number | 26020-01-39-001 | PACKAGE_REGISTER.csv |
| Responsible Party | EPC Integrator | _CONTEXT.md; PACKAGE_REGISTER.csv (responsibility model) |
| Covers Scope Items | SOW-0131, SOW-0132, SOW-0133, SOW-0134 | _CONTEXT.md; SCOPE_LEDGER.csv |
| Supports Objectives | OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | _CONTEXT.md; OBJECTIVE_REGISTER.csv |

## Attributes — Package Identity and Function

| Attribute | Value | Source |
|---|---|---|
| Package function | Instrument air supply package for the facility | SOW-0131 (Workbook Packages row 69) |
| Package basic scope | Two motor-driven oil-injected rotary screw air compressors, one wet air receiver, two dryer pre-filters, one regenerative desiccant air dryer, one after-filter, and one dry air receiver (or two 50% capacity receivers) | SOW-0132 (26020-Package_Requirements.docx package heading 32 — Basic scope) |
| Ownership split | Package Vendor: package engineering, package design, vendor documentation, physical equipment package. EPC Integrator: facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | PACKAGE_REGISTER.csv responsibility model |

## Attributes — Tagged Equipment List (from source basis)

| Item | Quantity / Identity | Key Attributes | Source |
|---|---|---|---|
| Instrument air compressor | 2 x oil-injected rotary screw, air-cooled | 1113 SCFM at 861 kPag (125 psig) discharge each; electric motor driven | SOW-0133 (26020-Package_Requirements.docx Major included equipment) |
| Compressor motor | 2 x electric, 250 HP | Soft starter or VFD ready; anti-condensation space heaters | SOW-0133 |
| Compressor motor (operating envelope) | 200-250 HP, 600V/3PH/60Hz, TEFC, non-classified, speed TBD by vendor | TBD speed | SOW-0134 |
| Wet air receiver | 1; size by vendor | TBD by vendor | SOW-0133 |
| Dryer pre-filter | 2; size by vendor | TBD by vendor | SOW-0133 |
| Air dryer | 1 x regenerative desiccant, 100% capacity, 2 tanks/towers (one operating, one regenerating) | Size and capacity TBD by vendor; sized for 2 compressors and leave | SOW-0132; SOW-0133 |
| Common after-filter | 1; downstream of combined dryer outlets | TBD | SOW-0133 |
| Dry air receiver | 1 (or 2 x 50% capacity) | TBD by vendor | SOW-0132 |

## Conditions — Design and Operating Basis (from source basis)

| Parameter | Value | Source |
|---|---|---|
| Delivered air dewpoint | Maximum water dewpoint -73.3 °C at 1000 kPag | SOW-0133; SOW-0134 |
| PSV set pressure (all PSVs in system) | 948 kPag (137.5 psig) | SOW-0133 |
| Compressor rated discharge | 861 kPag (125 psig) | SOW-0133 |
| Compressor max discharge / shutdown | 1000 kPag | SOW-0134 |
| Maximum system design pressure | 1034 kPag (150 psig) | SOW-0134 |
| Minimum system pressure | 551 kPag (80 psig) | SOW-0134 |
| Facility shutdown pressure | 482 kPag (70 psig) | SOW-0134 |
| Capacity / design throughput | 1113 SCFM at 861 kPag (125 psig) | SOW-0134 |
| Design temperature range | -40 °C to 38 °C | SOW-0134 |

## Construction — Boundary, Interfaces, and Responsibility Split

| Element | Statement | Source |
|---|---|---|
| Battery limit principle | Package Vendor delivers the engineered/designed equipment package; EPC Integrator performs all facility-level integration | PACKAGE_REGISTER.csv responsibility model; OBJ-004 |
| By Others (explicit) | Shipping of compressor packages to site; installation on piles; tie-in piping; electrical connections; mounting platform and stairs | SOW-0134 (Scope notes — By others) |
| Applicable interface types | Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports | INTERFACE_REGISTER.csv (10 rows for PKG-079); PACKAGE_REGISTER.csv |
| Package-specific exclusions | TBD; no package-specific exclusions stated in source materials | PACKAGE_REGISTER.csv (Exclusions field) |

## Anticipated Artifacts (this deliverable)

- Package scope of work (this deliverable narrative)
- Tagged equipment and package identity list (see Attributes above)
- Package function and integration narrative (see Specification.md Scope)
- Responsibility assignment record (see Specification.md Requirements + Guidance.md)

Source: _CONTEXT.md anticipated artifacts; DELIVERABLE_REGISTER.csv anticipated_artifacts.

## References

- Workbook Packages row 69 (PACKAGE_REGISTER.csv; SCOPE_LEDGER.csv; INTERFACE_REGISTER.csv).
- 26020-Package_Requirements.docx package heading 32 — Basic scope; Major included equipment; Scope notes and open items (extracted into SCOPE_LEDGER.csv rows SOW-0131..SOW-0134).
- Word Source Basis (per PACKAGE_REGISTER.csv): Bid Docs/Budgetary/26020-01-PT-RFQ-39-001_Instr_Air_Bldg_R1.docx — location TBD locally.
- DBM reference: DBM-Deepcut/4-25_Deepcut_DBM.md (cited in PACKAGE_REGISTER.csv; locally accessible per _Sources listing — full slice not consulted in this pass).
- Objective register entries OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 — OBJECTIVE_REGISTER.csv. Association recorded as ASSUMPTION (best-effort, package-grouping heuristic) per skill Step 1.3.

## Notes

- All numeric values transcribed from SOW-0133/SOW-0134 which are direct extractions of 26020-Package_Requirements.docx package heading 32; the original .docx was not re-opened in this pass (located at _Sources/26020-Package_Requirements.docx; opening it for verification is a candidate Pass 3 reread).
- TBD items intentionally preserved where source defers sizing to the vendor.
