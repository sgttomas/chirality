# Datasheet — DEL-079-06 EPC Vendor Package Review and Acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-079-06_epc-vendor-package-review-and-acceptance | `_CONTEXT.md` |
| Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md` |
| ParentPackageID | PKG-079 | `_CONTEXT.md` |
| Package Name | Instrument Air Building | `_CONTEXT.md` |
| Workbook ID | 79 (Packages row 69) | DELIVERABLE_REGISTER.csv |
| CoA Tracking Number | 26020-01-PT-39-001 | PACKAGE_REGISTER.csv |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Vendor Package Acceptance | `_CONTEXT.md` |
| Responsible Party | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Subject vendor package | Instrument Air Building (rotary screw compressors + receivers + dryer train) | SCOPE_LEDGER SOW-0131..SOW-0133 |
| Acceptance basis documents | EPC Scope of Work (DEL-079-01), EPC Package Datasheet (DEL-079-02), EPC Construction Work Package (DEL-079-03) | DELIVERABLE_REGISTER (PKG-079); `_CONTEXT.md` Scope |
| Vendor inputs reviewed | Vendor Engineered Equipment Package (DEL-079-04), Vendor Document Turnover Package (DEL-079-05) | DELIVERABLE_REGISTER (PKG-079) |
| Anticipated artifacts | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence | `_CONTEXT.md` Anticipated Artifacts |
| Scope items covered | SOW-0131, SOW-0132, SOW-0133, SOW-0134 | `_CONTEXT.md`; SCOPE_LEDGER |
| Objectives supported | OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (ASSUMPTION via PACKAGE_HEURISTIC) | `_CONTEXT.md`; OBJECTIVE_DELIVERABLE_MAP.csv |

## Conditions (Acceptance Context)

| Condition | Value | Source |
|---|---|---|
| Applicable interface types (must close before acceptance) | Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports | INTERFACE_REGISTER IFC-E7D3353482, IFC-FBA5A1ED78, IFC-47DC520AA2, IFC-CD84DBE736, IFC-3B18C99DFD, IFC-C4F92A698B, IFC-75F0F21CEA, IFC-E10830EA2F, IFC-5BB5161DC0, IFC-0EC9E5E722 |
| Excluded EPC-by-others items not within vendor scope (acceptance scope flagged accordingly) | Shipping compressor packages to site; installation on piles; tie-in piping; electrical connections; mounting platform and stairs | SCOPE_LEDGER SOW-0134 |
| Critical design conditions to confirm via vendor data | PSV set at 948 kPag (137.5 psig); delivered air max water dew point -73.3 °C at 1000 kPag; max system design 1034 kPag (150 psig); min system 551 kPag (80 psig); facility shutdown 482 kPag (70 psig); design temperature -40 °C to 38 °C | SCOPE_LEDGER SOW-0133, SOW-0134 |
| Equipment count to verify on receipt | 2 x rotary screw IA compressors (1113 SCFM @ 861 kPag each, 250 HP electric, soft-start/VFD ready); 1 wet receiver; 2 dryer pre-filters; 1 regenerative desiccant dryer (2 towers); 1 after-filter; 1 dry receiver (or 2 x 50%) | SCOPE_LEDGER SOW-0132, SOW-0133 |

## Construction (Artifact Set)

| Artifact | Description | Source |
|---|---|---|
| Vendor document review log | Per-document review status against the EPC Package Datasheet and EPC Scope of Work; covers vendor document categories produced under DEL-079-05 | `_CONTEXT.md`; ARTIFACT_REGISTER DEL-079-05 entries (ART-95A888C02E, ART-33E3E7FE46, ART-F8BF3DB9AA, ART-D103DDD65D, ART-CACD5074F8, …) |
| Package acceptance checklist | Itemized acceptance gates traceable to SOW-0131..SOW-0134 and to the ten PKG-079 interface facts | SCOPE_LEDGER; INTERFACE_REGISTER PKG-079 |
| Test / inspection evidence | Factory and site test records, PSV verification, dew-point verification, motor / soft-start commissioning records — `location TBD` until vendor turnover received | SCOPE_LEDGER SOW-0133 (PSV, dew point); TBD source slice |
| Turnover evidence | Construction turnover handoff records aligned to DEL-079-03 Construction Interface and turnover checklist (ART-10C3D82526) | ARTIFACT_REGISTER DEL-079-03 |

## References

- `_CONTEXT.md` (deliverable-local).
- `_REFERENCES.md` (deliverable-local) — Gate 7 PROJECT_DECOMP snapshot pointers.
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (row `DEL-079-06_epc-vendor-package-review-and-acceptance`).
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` (row `PKG-079`).
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/SCOPE_LEDGER.csv` (SOW-0131..SOW-0134).
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv` (10 PKG-079 interface rows).
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/ARTIFACT_REGISTER.csv` (PKG-079 artifacts).
- Source basis (per `_REFERENCES.md`): Workbook Packages row 69; `26020-Package_Requirements.docx` package heading 32; `Bid Docs/Budgetary/26020-01-PT-RFQ-39-001_Instr_Air_Bldg_R1.docx`; `DBM-Deepcut/4-25_Deepcut_DBM.md` — `location TBD` (raw slices not copied into the deliverable folder during PREPARATION).
