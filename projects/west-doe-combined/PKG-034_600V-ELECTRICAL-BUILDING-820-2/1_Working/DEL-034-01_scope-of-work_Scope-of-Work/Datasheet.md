# Datasheet: DEL-034-01 — Scope of Work (PKG-034 600V Electrical Building (820-2))

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-034-01_scope-of-work` | `_CONTEXT.md` |
| Deliverable Name | Scope of Work | `_CONTEXT.md` |
| ParentPackageID | `PKG-034` | `_CONTEXT.md` |
| ParentWorkbookID | 34 | `_CONTEXT.md` |
| Package Name | 600V ELECTRICAL BUILDING (820-2) | Gate 7 `PACKAGE_REGISTER.csv` row PKG-034 |
| CoA Tracking Number | 26020-02-30-025 | Gate 7 `PACKAGE_REGISTER.csv` row PKG-034 |
| WBS | 02 (03-25 Compressor Station and Liquids Hub) | Gate 7 `PACKAGE_REGISTER.csv` row PKG-034 |
| Discipline | Electrical | `_CONTEXT.md`; Gate 7 `PACKAGE_REGISTER.csv` |
| Deliverable Type | EPC Scope of Work | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Covers Scope Items | `SOW-0035` | `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` |
| Supports Objectives | `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION: package-grouping heuristic) | Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-034-01; `OBJECTIVE_ASSOCIATION_MODE = PACKAGE_HEURISTIC` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package Function | Vendor-engineered modular electrical building (820-2) housing 600V MCC, distribution equipment, and associated HVAC/ventilation for the 03-25 Compressor Station and Liquids Hub | DBM 3-25 SEC-12 "Electrical Buildings, Raceways, Lighting, and Heat Tracing" (location TBD line ref) |
| Voltage Class (housed equipment) | 600 V LV (per package designation "820-2") | Gate 7 `PACKAGE_REGISTER.csv`; DBM 3-25 SEC-12 "600V MCC and Standby Power" |
| Building Construction Basis | Pre-fabricated modularized building | DBM/Trace_Appendix SUB-12-05-02 citing DBM §12.5.2 (W242510-PRC-DBM-000001-001) |
| Siting Basis | Located for convenient power distribution in general-purpose areas | DBM/Trace_Appendix SUB-12-05-01 citing DBM §12.5.1 |
| Upstream Power Source | Sub-fed from 04-25 13.8 kV Main Switchgear Electrical Building via 13.8 kV / 600V, 3 MVA transformer feeding the 600V MCC | DBM 3-25 SEC-12 "Incoming Power and Transformers" |
| Standby Power | 600V-MCC-level LV standby natural-gas generator with transfer switch (transfer-switch type, bus configuration, generator count/rating TBD) | DBM 3-25 SEC-12 "600V MCC and Standby Power" |
| Building HVAC | Associated HVAC/ventilation systems coordinated with hazardous-area classification and controls architecture | DBM 3-25 SEC-12 "Electrical Buildings, Raceways, Lighting, and Heat Tracing" |
| Major Equipment List (tagged) | TBD (workbook row 36 source slice does not provide a tagged-equipment list at this register row; detailed major equipment to be developed in DEL-034-02 Package Datasheet) | Workbook Packages row 36; not present in accessible slice |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Facility / WBS Context | 03-25 Compressor Station and Liquids Hub (WBS 02) | Gate 7 `PACKAGE_REGISTER.csv`; DBM 3-25 Facility Overview |
| Service Environment | Industrial process plant; hazardous-area classification coordinated per project area-classification basis | DBM 3-25 SEC-12 "Electrical Buildings, Raceways, Lighting, and Heat Tracing" |
| Climate / Foundation Basis | Foundations designed for final geotechnical report, equipment loads, snow/wind/seismic, frost protection, vibration, settlement, and maintenance access | DBM 3-25 SEC-11 (Civil/Structural) "Foundations" paragraph |
| Co-located Buildings (context) | 4.16 kV inlet/overheads compressor electrical building, 600V electrical building, package buildings, and shared utility buildings at 04-25 | DBM 3-25 SEC-11 "Buildings include ..." paragraph |

## Construction

| Item | Value | Source |
|---|---|---|
| Building Type | Pre-fabricated modularized electrical building | DBM/Trace_Appendix SUB-12-05-02 |
| Housed Equipment Classes | 600V MCC, distribution equipment, building HVAC/ventilation, lighting, receptacles | DBM 3-25 SEC-12 |
| Power Circuit Separation | 13.8 kV / 4,160 V / 600 V power circuits separated from control and instrument circuits by distance, shielding, or routing | DBM 3-25 SEC-12 "Electrical Buildings, Raceways, Lighting, and Heat Tracing" |
| Lighting / Heat Tracing / Cathodic Protection | Within electrical design scope; building heaters normally fed from LV system | DBM 3-25 SEC-12 |
| Package Vendor Scope | Package engineering, package design, vendor documentation, physical equipment package | Gate 7 `PACKAGE_REGISTER.csv` row PKG-034 Responsibility column |
| EPC Integrator Scope | Integration into the functional process facility — interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration | Gate 7 `PACKAGE_REGISTER.csv` row PKG-034 Responsibility column |
| Applicable Interface Types | Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports | Gate 7 `PACKAGE_REGISTER.csv` row PKG-034 Interfaces column |

## References

- `_CONTEXT.md`
- Gate 7 snapshot `DELIVERABLE_REGISTER.csv` (row DEL-034-01)
- Gate 7 snapshot `PACKAGE_REGISTER.csv` (row PKG-034)
- Gate 7 snapshot `ARTIFACT_REGISTER.csv` (artifacts ART-690D20A019, ART-9012A670A0, ART-CF613FE6B3, ART-D799B59828)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-12 "Electrical Buildings, Raceways, Lighting, and Heat Tracing"; SEC-12 "Incoming Power and Transformers"; SEC-12 "600V MCC and Standby Power"; SEC-11 buildings/foundations paragraphs
- `_Sources/DBM-Comp_and_Liquids/Trace_Appendix.md` rows SUB-12-05-01 and SUB-12-05-02 (KTY-12-05 Electrical-Buildings)
- Workbook Packages row 36 (location TBD — source slice not copied into deliverable)
