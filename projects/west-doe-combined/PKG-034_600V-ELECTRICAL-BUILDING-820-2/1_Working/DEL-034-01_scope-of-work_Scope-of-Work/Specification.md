# Specification: DEL-034-01 — Scope of Work (PKG-034 600V Electrical Building (820-2))

## Scope

This Scope of Work defines the EPC Integrator's authorship of the full package scope for PKG-034 "600V ELECTRICAL BUILDING (820-2)" within the 03-25 Compressor Station and Liquids Hub (WBS 02). It establishes the package identity, tagged-equipment basis, package function, source basis, package boundaries, and the whole-facility integration narrative.

**Inclusions:**
- Package identity statement (PackageID, CoA tracking, WBS, discipline, source row).
- Tagged equipment and package identity list (to the extent supported by source).
- Package function statement and whole-facility integration narrative.
- Source basis (workbook row + DBM source slices).
- Package boundaries (battery limits) summarized at scope level; detailed interface facts are carried in DEL-034-02 Package Datasheet.
- Responsibility assignment record (Package Vendor vs EPC Integrator).

**Exclusions:**
- Detailed package engineering, package design, and vendor documentation (Package Vendor scope; see DEL-034-04, DEL-034-05).
- Package technical datasheet content and interface requirements matrix (DEL-034-02).
- Construction work package detail (DEL-034-03).
- EPC vendor package review and acceptance records (DEL-034-06).
- LACT units and third-party scope (per DBM 3-25 SEC-12 "Incoming Power and Transformers").
- Local 03-25 instrument-air compressor scope (per DBM 3-25 SCA-006; SEC-12 "Instrument Air and Electrical Interface").

## Requirements

| ReqID | Requirement | Source |
|---|---|---|
| REQ-034-01-001 | The Scope of Work shall state PackageID `PKG-034`, package name "600V ELECTRICAL BUILDING (820-2)", CoA tracking `26020-02-30-025`, WBS `02`, discipline `Electrical`, and workbook source row 36. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-034 |
| REQ-034-01-002 | The Scope of Work shall identify the package function as a pre-fabricated modular electrical building housing 600V MCC, distribution equipment, and associated HVAC/ventilation, serving the 03-25 facility. | DBM 3-25 SEC-12 "Electrical Buildings, Raceways, Lighting, and Heat Tracing"; Trace_Appendix SUB-12-05-02 |
| REQ-034-01-003 | The Scope of Work shall record the responsibility split: Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-034 Responsibility column |
| REQ-034-01-004 | The Scope of Work shall enumerate the applicable interface types listed in the workbook for this package: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-034 Interfaces column |
| REQ-034-01-005 | The Scope of Work shall state the upstream electrical source basis: the 600V MCC is fed from a 13.8 kV / 600V, 3 MVA transformer sub-fed from the 04-25 13.8 kV Main Switchgear Electrical Building. | DBM 3-25 SEC-12 "Incoming Power and Transformers" |
| REQ-034-01-006 | The Scope of Work shall record standby power as 600V-MCC-level LV standby natural-gas generator with transfer switch; transfer-switch type, bus configuration, generator count, and rating remain `TBD`. | DBM 3-25 SEC-12 "600V MCC and Standby Power" |
| REQ-034-01-007 | The Scope of Work shall acknowledge tagged major equipment as `TBD` at the SOW level; the tagged-equipment evidence list is consolidated in DEL-034-02 Package Datasheet (ART-9012A670A0; ART-F1D13765C8). | Gate 7 `ARTIFACT_REGISTER.csv` |
| REQ-034-01-008 | The Scope of Work shall cite the source basis as Workbook Packages row 36 and the DBM-Comp_and_Liquids 3-25 DBM. | Gate 7 `PACKAGE_REGISTER.csv`; `_REFERENCES.md` |
| REQ-034-01-009 | The Scope of Work shall associate the package with supporting objectives `OBJ-002`, `OBJ-004`–`OBJ-010` under the package-grouping heuristic (ASSUMPTION; not a hard requirement until human-confirmed). | Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-034-01; `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC` |
| REQ-034-01-010 | The Scope of Work shall identify exclusions: LACT units (third-party scope) and local 03-25 instrument-air compressors. | DBM 3-25 SEC-12 "Incoming Power and Transformers"; "Instrument Air and Electrical Interface" |

## Standards

| Standard / Basis | Applicability | Source |
|---|---|---|
| Project Electrical Specifications (cable tray, conduit, grounding, bonding) | Mandatory for power-circuit separation and raceway design | DBM 3-25 SEC-12 "Electrical Buildings, Raceways, Lighting, and Heat Tracing" (location TBD — specific spec IDs not in accessible slice) |
| Project Hazardous Area Classification basis | Drives building HVAC, area-classification coordination | DBM 3-25 SEC-12; Trace_Appendix SUB-12-05-01 |
| Geotechnical / Civil-Structural basis | Foundation design (loads, snow/wind/seismic, frost, vibration, settlement, maintenance access) | DBM 3-25 SEC-11 Foundations paragraph |
| DBM 3-25 W242510-PRC-DBM-000001-001 (March 2025) | Governing electrical-buildings design basis | Trace_Appendix rows SUB-12-05-01, SUB-12-05-02 |
| External codes (e.g., CSA/CEC/NEC, NFPA) | `TBD` — not enumerated in the accessible source slice | location TBD |

## Verification

| ReqID | Verification Approach |
|---|---|
| REQ-034-01-001 | Document review: confirm SOW header carries PackageID, CoA, WBS, discipline, source row matching Gate 7 `PACKAGE_REGISTER.csv`. |
| REQ-034-01-002 | Document review against DBM 3-25 SEC-12 and Trace_Appendix SUB-12-05-02. |
| REQ-034-01-003 | Document review: responsibility paragraph matches Gate 7 `PACKAGE_REGISTER.csv` wording. |
| REQ-034-01-004 | Cross-check interface-type list against Gate 7 `PACKAGE_REGISTER.csv` Interfaces column. |
| REQ-034-01-005 | Document review against DBM 3-25 SEC-12 "Incoming Power and Transformers". |
| REQ-034-01-006 | Document review against DBM 3-25 SEC-12 "600V MCC and Standby Power"; `TBD` items carried forward. |
| REQ-034-01-007 | Cross-reference to DEL-034-02 artifact register entries ART-9012A670A0 and ART-F1D13765C8. |
| REQ-034-01-008 | Confirm `_REFERENCES.md` and SOW cite Workbook Packages row 36 + 3-25 DBM. |
| REQ-034-01-009 | Confirm ASSUMPTION label is present; objective list matches Gate 7 register. |
| REQ-034-01-010 | Confirm exclusions are stated and trace back to SCA-006/SEC-12 wording. |

## Documentation

The following anticipated artifacts (per Gate 7 `ARTIFACT_REGISTER.csv` for DEL-034-01) are produced as part of this Scope of Work:

- ART-690D20A019 — Package scope of work (EPC Scope of Work).
- ART-9012A670A0 — Tagged equipment and package identity list (Tagged Equipment Evidence).
- ART-CF613FE6B3 — Package function and whole-facility integration narrative (EPC Integration Narrative).
- ART-D799B59828 — Package responsibility assignment record (Responsibility Evidence).

Companion deliverable artifacts (out of scope here; carried in DEL-034-02..DEL-034-06) are listed in Gate 7 `ARTIFACT_REGISTER.csv` for PKG-034.
