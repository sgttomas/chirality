# Datasheet — DEL-091-02 Package Datasheet (Tank Farm Pump Building 3-25)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-091-02_package-datasheet | _CONTEXT.md |
| Deliverable Name | Package Datasheet | _CONTEXT.md |
| Parent Package | PKG-091 — Tank Farm Pump Building 3-25 | PACKAGE_REGISTER.csv row PKG-091 |
| Workbook Row | 84 | PACKAGE_REGISTER.csv row PKG-091 |
| WBS | 03 | PACKAGE_REGISTER.csv row PKG-091 |
| Tag Prefix | 26020-03-18-001 | PACKAGE_REGISTER.csv row PKG-091 |
| Discipline | Mechanical | _CONTEXT.md; PACKAGE_REGISTER.csv |
| Deliverable Type | EPC Package Datasheet | _CONTEXT.md |
| Responsible Party | EPC Integrator | _CONTEXT.md; DELIVERABLE_REGISTER.csv |
| Covers Scope Items | SOW-0185, SOW-0186, SOW-0187, SOW-0188 | DELIVERABLE_REGISTER.csv; SCOPE_LEDGER.csv |
| Supports Objectives | OBJ-002 … OBJ-010 | DELIVERABLE_REGISTER.csv |

## Attributes — Package Equipment Inventory

Tagged equipment carried into this datasheet from authoritative source (SCOPE_LEDGER SOW-0187 / 26020-Package_Requirements.docx heading 44, "Major included equipment"). Values shown verbatim where possible; "TBC" reproduces source language.

| Tag | Equipment | Type / Description | Power | Drive | Source |
|---|---|---|---|---|---|
| P-9295-2 | Building Drain Pump (1) | Graco 1050A Pneumatic Diaphragm; 11.34 m³/h @ 689 kPag | n/a (pneumatic) | Pneumatically Driven | SOW-0187 |
| P-9290-2 / P-9293-2 | Water Transfer Pumps (2) | Radial centrifugal; seal plan single mechanical | 150 kW (200 HP) | 575 V / 3 Ph / 60 Hz electric motor | SOW-0187 |
| P-9215-2 / P-9216-2 | Sour Condensate Booster Pumps (2) | Vertical inline centrifugal; seal plan API-682 Plan 14/52 | 18.5 kW (25 HP) | 575 V / 3 Ph / 60 Hz electric motor | SOW-0187 |
| P-9210-2 / P-9220-2 | Condensate Sweetening Feed Pumps (2) | Vertical inline centrifugal; seal plan API-682 Plan 14/52 | 55 kW (75 HP) @ 100% | 575 V / 3 Ph / 60 Hz (TBD — voltage explicit in source: "Powered by." truncated) | SOW-0187 |
| P-9200-2 | Condensate Skim Pump (1) | Diaphragm positive displacement; Hydracell, sealless | 11 kW (15 HP) | 575 V / 3 Ph / 60 Hz electric motor | SOW-0187 |
| P-9230-2 | Sour Condensate Recycle Pump (1) | Diaphragm positive displacement; Hydracell, sealless | 11 kW (15 HP) | 575 V / 3 Ph / 60 Hz electric motor | SOW-0187 |
| P-9211-2 / P-9221-2 | Condensate Booster Pumps (2) | Vertical inline centrifugal; seal plan API-682 Plan 14/52 | 18.5 kW (25 HP) | Electric motor (voltage TBD — source not explicit at this line) | SOW-0187 |
| P-9240-2 | Condensate Product Recycle Pump (1) | Diaphragm positive displacement; Hydracell, sealless; with inlet basket strainer (size TBC) | 11 kW (15 HP) | Electric motor (voltage TBD — source not explicit at this line) | SOW-0187 |

## Conditions — Capacity / Throughput

Source: SOW-0188 (26020-Package_Requirements.docx package heading 44, "Scope notes and open items").

| Service | Design Throughput / Capacity | Source |
|---|---|---|
| Building Drain Pump | 11.34 m³/h @ 689 kPag | SOW-0188 |
| Water Transfer Pump | 218 m³/day @ 172 kPad (40 USGPM @ 25 psid) | SOW-0188 |
| Sour Condensate Booster Pump | TBC (source-stated "TBC") | SOW-0188 |
| Sweet Condensate Feed Pump | TBC (source-stated "TBC") | SOW-0188 |
| Condensate Skim Pump | 20 m³/hr | SOW-0188 |
| Sour Condensate Recycle Pump | 20 m³/hr | SOW-0188 |
| Condensate Booster Pump | TBC (source-stated "TBC") | SOW-0188 |
| Condensate Loading | TBD — source line truncated in SOW-0188 | SOW-0188 |

### Site / Driver Conditions

| Parameter | Value | Source |
|---|---|---|
| Motor electrical supply | 575 V / 3 Ph / 60 Hz | SOW-0188 |
| Starting method | DOL or VFD | SOW-0188 |
| Local control | H-O-A or On-Off switch | SOW-0188 |
| Power feed | Electric motors fed from 600 V MCC | SOW-0188 |
| Motor sizing basis | Sized for inlet stabilizer composition density at −40 °C start-up condition | SOW-0188 |
| Operating conditions | TBC (source-stated; see Throughput/Capacity) | SOW-0188 |
| Design conditions | TBC (source-stated; see Throughput/Capacity) | SOW-0188 |

## Construction — Package Process Function and Configuration

Verbatim from PACKAGE_REGISTER.csv (PKG-091 process function) and SCOPE_LEDGER SOW-0186:

- Package houses all pumps for the tank farm.
- Water Transfer Pumps configured in parallel, drawing water from produced water tanks through a bag filter, discharging to the produced water pipeline.
- Sour Condensate Pumps move sour condensate from sour condensate storage tanks to the condensate sweetening feed pumps.
- "Condensate." (Source sentence is truncated in workbook/Word extract — downstream detail TBD.)

### By Others (boundary clarifications)

- DCS integration — by others (SOW-0188)
- Foundations — by others (SOW-0188)
- Electrical supply to MCC — by others (SOW-0188)

### Package Interfaces (EPC Integrator Scope)

All interface types are applicable to this package per PACKAGE_REGISTER and INTERFACE_REGISTER (each `Applies = YES`, Workbook row 84):

| InterfaceID | Type |
|---|---|
| IFC-4A728F3420 | Process Piping |
| IFC-D7A04E5422 | Utility Piping |
| IFC-B085936AF4 | Relief / Flare / Vent |
| IFC-F4402C016A | Drain / Containment |
| IFC-D13319D61F | Electrical Power |
| IFC-7007935F4B | EHT |
| IFC-C58489EFA9 | Grounding / Bonding |
| IFC-EA6B9F1DED | Area / Exterior Lighting |
| IFC-8763413C44 | Cathodic Protection |
| IFC-4660D77FEA | I&C / Control Cabling |
| IFC-61A8B94465 | Building HVAC / Services |
| IFC-9D2C05504D | Fire & Gas / Safety Systems |
| IFC-D1580484FE | Maintenance Access |
| IFC-EA0CFB4263 | Grading / Site Drainage / Spill Containment |
| IFC-9847799665 | Structural / Foundations / Supports |

## References

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable-local)
- GATE-07 PROJECT_DECOMP snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `PACKAGE_REGISTER.csv` — row PKG-091
  - `DELIVERABLE_REGISTER.csv` — row DEL-091-02
  - `SCOPE_LEDGER.csv` — rows SOW-0185 .. SOW-0188
  - `INTERFACE_REGISTER.csv` — fifteen PKG-091 rows
  - `OBJECTIVE_DELIVERABLE_MAP.csv`
- Upstream source materials (referenced; full slice access TBD beyond what is carried into the snapshot rows): `_Sources/26020-Package_Requirements.docx` package heading 44; `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 84; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`; Bid Docs Budgetary `26020-03-PT-RFQ-18-002-Tank Farm Pumps.docx` (location TBD).
