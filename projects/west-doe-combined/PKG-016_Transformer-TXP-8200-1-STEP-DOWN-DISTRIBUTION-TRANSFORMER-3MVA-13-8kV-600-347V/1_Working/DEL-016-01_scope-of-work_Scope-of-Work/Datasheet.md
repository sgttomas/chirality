# Datasheet — DEL-016-01 Scope of Work (PKG-016 Transformer TXP-8200-1)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-016-01_scope-of-work` | DELIVERABLE_REGISTER.csv (Gate 7) |
| Deliverable Name | Scope of Work | DELIVERABLE_REGISTER.csv |
| Deliverable Type | EPC Scope of Work | DELIVERABLE_REGISTER.csv |
| Responsible Party | EPC Integrator | DELIVERABLE_REGISTER.csv |
| ParentPackageID | `PKG-016` | PACKAGE_REGISTER.csv row PKG-016 |
| Package Name | Transformer TXP-8200-1 — STEP DOWN DISTRIBUTION TRANSFORMER — 3MVA 13.8kV/600/347V | PACKAGE_REGISTER.csv row PKG-016 |
| Workbook Row | 18 | PACKAGE_REGISTER.csv |
| WBS | 02 | PACKAGE_REGISTER.csv |
| CoA Tracking Number | 26020-02-30-007 | PACKAGE_REGISTER.csv |
| Discipline | Electrical | PACKAGE_REGISTER.csv |
| Covers Scope Items | `SOW-0017` | SCOPE_LEDGER.csv |
| Supports Objectives | OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 | OBJECTIVE_DELIVERABLE_MAP.csv |

## Attributes (Package Identity carried by this SoW)

| Attribute | Value | Source |
|---|---|---|
| Equipment Tag | TXP-8200-1 | PACKAGE_REGISTER.csv (package name) |
| Equipment Function | Step-down distribution transformer | PACKAGE_REGISTER.csv (package name) |
| Rated Capacity | 3 MVA | PACKAGE_REGISTER.csv; DBM SEC-12 row "13.8 kV to 600V, 3 MVA transformer" |
| Primary Voltage | 13.8 kV, 3-phase, 3-wire, 60 Hz, LRG (cross-facility incoming basis) | DBM SEC-12 System Voltages table |
| Secondary Voltage (line-to-line / line-to-neutral notation) | 600 V / 347 V (from package name) | PACKAGE_REGISTER.csv (package name) |
| Low-Voltage System Basis | 600 V, 3-phase, 3-wire, 60 Hz, HRG with 5 A continuous resistor | DBM SEC-12 System Voltages table |
| Downstream Service | 600 V MCC for LV loads | DBM SEC-12 Incoming Power and Transformers table |
| Package Vendor Scope Ownership | Package engineering, package design, vendor documentation, physical equipment package | PACKAGE_REGISTER.csv RACI text |
| EPC Integrator Scope Ownership | Facility integration: interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration | PACKAGE_REGISTER.csv RACI text |

## Conditions (Service Environment and Applicability)

| Condition | Value | Source |
|---|---|---|
| Facility Location | 03-25 facility, sub-fed from 04-25 Main Switchgear Electrical Building | DBM SEC-12 |
| Area Classification (general basis) | Class I Zone 2, Gas Groups IIA and IIB unless detailed drawings indicate otherwise | DBM SEC-12 Area Classification |
| Building Context | 600 V electrical building (known building/interface) | DBM SEC-08 Buildings (row noting "600V electrical building") |
| Foundation / Civil Basis | Equipment-specific foundation and anchorage design per geotechnical, loads, snow/wind/seismic, frost, vibration, settlement, and maintenance access | DBM SEC-08 |
| Cable Separation Basis | 13.8 kV, 4,160 V, and 600 V power circuits separated from control and instrument circuits by distance, shielding, or routing | DBM SEC-12 Electrical Buildings, Raceways, Lighting, and Heat Tracing |
| Site / Environmental Conditions (ambient, altitude, seismic specifics) | TBD — not specified in accessible source slices for this package | — |
| Hazardous-Area Drawing Reference | location TBD | DBM SEC-12 |

## Construction (Package Identity and Boundary)

| Item | Value | Source |
|---|---|---|
| Major Equipment | One step-down distribution transformer TXP-8200-1, 3 MVA, 13.8 kV / 600 V (347 V neutral implied by package name) | PACKAGE_REGISTER.csv; DBM SEC-12 |
| Applicable Interface Types | Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports | PACKAGE_REGISTER.csv; INTERFACE_REGISTER.csv (7 rows for PKG-016) |
| Package Form Factor (oil-filled vs dry-type, indoor/outdoor, primary/secondary termination type) | TBD — not specified in accessible source slices | — |
| Tap-changer Configuration | TBD | — |
| Cooling Class | TBD | — |
| Impedance / BIL | TBD | — |
| Accessory Scope (RTUs, monitors, dehydrating breathers, surge arresters) | TBD | — |

## References

- Gate 7 PROJECT_DECOMP snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`
  - `DELIVERABLE_REGISTER.csv` — row `DEL-016-01_scope-of-work`
  - `PACKAGE_REGISTER.csv` — row `PKG-016`
  - `INTERFACE_REGISTER.csv` — rows for PKG-016 (7 interfaces)
  - `ARTIFACT_REGISTER.csv` — rows for DEL-016-01 (ART-9B23EFA6EE, ART-65C8336085, ART-4E2F8A9FDF, ART-F610CDF9EC)
  - `OBJECTIVE_DELIVERABLE_MAP.csv` — DEL-016-01 ↔ OBJ-002, 004, 005, 006, 008, 009, 010
  - `SCOPE_LEDGER.csv` — `SOW-0017`
- DBM source slice: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — SEC-12 (Electrical Basis), specifically:
  - System Voltages table (line 730–736)
  - Incoming Power and Transformers table (line 738–748) — row `13.8 kV to 600V, 3 MVA transformer | 600V MCC for LV loads`
  - Area Classification, Buildings, and Electrical Buildings/Raceways sections
- Workbook Packages row 18 (canonical decomposition source — referenced but not opened in this run; values consumed via Gate 7 registers).
