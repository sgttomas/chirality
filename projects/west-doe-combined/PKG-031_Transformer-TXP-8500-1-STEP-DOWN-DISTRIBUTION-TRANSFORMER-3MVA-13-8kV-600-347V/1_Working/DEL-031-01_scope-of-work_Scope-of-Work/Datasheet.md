# Datasheet — DEL-031-01 Scope of Work (PKG-031 Transformer TXP-8500-1)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-031-01_scope-of-work` | DELIVERABLE_REGISTER.csv (Gate 7) |
| Deliverable Name | Scope of Work | DELIVERABLE_REGISTER.csv |
| Deliverable Type | EPC Scope of Work | DELIVERABLE_REGISTER.csv |
| Responsible Party | EPC Integrator | DELIVERABLE_REGISTER.csv |
| ParentPackageID | `PKG-031` | PACKAGE_REGISTER.csv row PKG-031 |
| Package Name | Transformer TXP-8500-1 — STEP DOWN DISTRIBUTION TRANSFORMER — 3MVA 13.8kV/600/347V | PACKAGE_REGISTER.csv row PKG-031 |
| Workbook Row | 33 | PACKAGE_REGISTER.csv |
| WBS | 01 | PACKAGE_REGISTER.csv |
| CoA Tracking Number | 26020-01-30-022 | PACKAGE_REGISTER.csv |
| Discipline | Electrical | PACKAGE_REGISTER.csv |
| Covers Scope Items | `SOW-0032` | SCOPE_LEDGER.csv |
| Supports Objectives | OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 | OBJECTIVE_DELIVERABLE_MAP.csv |

## Attributes (Package Identity carried by this SoW)

| Attribute | Value | Source |
|---|---|---|
| Equipment Tag | TXP-8500-1 | PACKAGE_REGISTER.csv (package name) |
| Equipment Function | Step-down distribution transformer | PACKAGE_REGISTER.csv (package name) |
| Rated Capacity | 3 MVA | PACKAGE_REGISTER.csv (package name) |
| Primary Voltage | 13.8 kV, 3-phase, 60 Hz (cross-facility incoming basis) | DBM-Deepcut SEC "System Voltages" / Power Distribution narrative |
| Secondary Voltage (line-to-line / line-to-neutral notation) | 600 V / 347 V (from package name) | PACKAGE_REGISTER.csv (package name) |
| Low-Voltage System Basis | 600 V, 3-phase, 3-wire, 60 Hz, high-resistance grounded with 5 A continuous resistor | DBM-Deepcut System Voltages table (line 2937) |
| Downstream Service | 600 V MCC for LV loads (Deepcut 04-25 facility) | DBM-Deepcut Power Distribution narrative (lines 2917–2929, 2959) |
| Package Vendor Scope Ownership | Package engineering, package design, vendor documentation, physical equipment package | PACKAGE_REGISTER.csv RACI text |
| EPC Integrator Scope Ownership | Facility integration: interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration | PACKAGE_REGISTER.csv RACI text |

## Conditions (Service Environment and Applicability)

| Condition | Value | Source |
|---|---|---|
| Facility Location | West Doe Deepcut expansion (04-25 facility), fed from the 13.8 kV main switchgear | DBM-Deepcut lines 2917–2919 |
| Area Classification (general basis) | Class I Zone 2, Gas Groups IIA and IIB unless detailed area-classification drawings indicate otherwise | DBM-Deepcut "Area Classification" (line 2907) |
| Building Context | Prefabricated modular electrical building housing 600 V MCCs and 600-to-208/120 V distribution transformers and panelboards | DBM-Deepcut Electrical Buildings narrative (lines 2973, 2977) |
| Foundation / Civil Basis | Electrical buildings are elevated and pile-supported with bottom cable entry; package-specific foundation/anchorage per geotechnical, loads, snow/wind/seismic, frost, vibration, and maintenance access | DBM-Deepcut Electrical Buildings (line 2977); general facility civil basis |
| Cable Separation Basis | Power circuits separated from control and instrument circuits by distance, shielding, or routing | DBM-Deepcut Raceways narrative |
| Site / Environmental Conditions (ambient, altitude, seismic specifics) | TBD — not specified in accessible source slices for this package | — |
| Hazardous-Area Drawing Reference | location TBD | DBM-Deepcut "Area Classification" |

## Construction (Package Identity and Boundary)

| Item | Value | Source |
|---|---|---|
| Major Equipment | One step-down distribution transformer TXP-8500-1, 3 MVA, 13.8 kV / 600 V (347 V neutral implied by package name) | PACKAGE_REGISTER.csv; DBM-Deepcut Power Distribution |
| Applicable Interface Types | Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports | PACKAGE_REGISTER.csv; INTERFACE_REGISTER.csv (7 rows for PKG-031) |
| Package Form Factor (oil-filled vs dry-type, indoor/outdoor, primary/secondary termination type) | TBD — not specified in accessible source slices | — |
| Tap-changer Configuration | TBD | — |
| Cooling Class | TBD | — |
| Impedance / BIL | TBD | — |
| Accessory Scope (RTUs, monitors, dehydrating breathers, surge arresters) | TBD | — |
| Grounding Basis (secondary) | Each 600 V transformer grounded by a 5 A continuous high-resistance grounding resistor; 600 V MCCs include power metering and ground/resistor fault detection; ground-fault protection on 600 V is alarm-only | DBM-Deepcut Grounding narrative (line 2985) |

## References

- Gate 7 PROJECT_DECOMP snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`
  - `DELIVERABLE_REGISTER.csv` — row `DEL-031-01_scope-of-work`
  - `PACKAGE_REGISTER.csv` — row `PKG-031`
  - `INTERFACE_REGISTER.csv` — rows for PKG-031 (7 interfaces)
  - `ARTIFACT_REGISTER.csv` — rows for DEL-031-01 (ART-38263068FC, ART-C52F26582F, ART-F816DB4F10, ART-23AA8A388B)
  - `OBJECTIVE_DELIVERABLE_MAP.csv` — DEL-031-01 ↔ OBJ-001, 004, 005, 006, 008, 009, 010
  - `SCOPE_LEDGER.csv` — `SOW-0032`
- DBM source slice: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — Electrical Basis sections, specifically:
  - Power Distribution narrative (lines 2917–2929) — 25 kV → 13.8 kV utility supply, 13.8 kV switchgear radial step-down to facility loads
  - System Voltages table (line 2937) — `Low-voltage services | 600 V, 3 phase, 3 wire, 60 Hz HRG with 5 A continuous resistor`
  - 600 V MCC narrative (line 2959)
  - Electrical Buildings narrative (lines 2973, 2977)
  - Area Classification (lines 2905–2913)
  - Grounding narrative (lines 2985, 2991)
- Workbook Packages row 33 (canonical decomposition source — referenced but not opened in this run; values consumed via Gate 7 registers).
