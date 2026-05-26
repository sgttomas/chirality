# Datasheet — Vendor Engineered Equipment Package (DEL-087-04)

> Descriptive datasheet for the Package Vendor production unit that delivers the engineered, designed, and supplied incinerator equipment package for PKG-087.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-087-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Name | Vendor Engineered Equipment Package | `_CONTEXT.md` |
| ParentPackageID | `PKG-087` | `_CONTEXT.md` |
| Package Name | Incinerator | `_CONTEXT.md` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | Vendor Package Production Unit | `_CONTEXT.md` |
| Responsible Party | Package Vendor (engineering / design / equipment) with EPC Integrator integration review | `_CONTEXT.md` |
| Facility Anchor | 03-25 Compressor Station and Liquids Hub (`OBJ-002`) | `OBJECTIVE_REGISTER.csv` (OBJ-002) |
| Source Basis | Workbook Packages row 64; 26020-Package_Requirements.docx package heading 40 | `_CONTEXT.md`, `PACKAGE_REGISTER.csv` |
| Bid Document Reference | `26020-01-PT-RFQ-25-003_Incinerator.docx` (Bid Docs/Budgetary) | `PACKAGE_REGISTER.csv` (Word Source Basis) — location TBD (slice not locally accessible) |
| Vendor Identity | TBD (Package Vendor selection not in source set) | TBD |

## Attributes

### Package Function and Service

| Attribute | Value | Source |
|---|---|---|
| Process function | Receives vapours from the spent caustic storage tank and the caustic regeneration column overheads; oxidises/incinerates the vapour stream and discharges through a low pressure flare stack | `PACKAGE_REGISTER.csv` (Description) |
| Shared interface status | Shared-interface system across 03-25 / 04-25; exact service-split and owner interface carried as open interface items | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 56; line 547 |
| Caustic regeneration in 03-25 basis | Caustic regeneration is NOT part of the current 03-25 basis (non-regenerative treating). The decomposition mention of "caustic regeneration column overheads" comes from the package row description; reconcile with DBM (CONFLICT — see Guidance) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 389; `PACKAGE_REGISTER.csv` |
| Spent caustic vent path | Spent caustic tank vents through a flame arrestor to the incinerator header; supports truck-out | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 402 |
| Caustic treating contributor | C5+ caustic treating package overhead/dilution/enrichment-gas interfaces feed the incinerator | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 400 |
| Caustic oxidation demand | 214 SCFM TBC | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 477 |

### Equipment Constituents (supplied as one vendor package)

| Tag / Item | Quantity | Key Data | Source |
|---|---|---|---|
| Incinerator Knock Out Drum `V-6900-1` | 1 | 2,896 mm (114") ID x 9,144 mm (30') S/S; 345 kPag @ -45.5 deg C / 260 deg C; 1.59 mm C.A. | `26020-Package_Requirements.docx` package heading 40 (Major included equipment, slice 510-515) |
| Incinerator KO Drum Transfer Pump `P-6900-1` | 1 | Vertical inline centrifugal; 70 USGPM; 5 hp, 575V/3Ph/60Hz; Class I Div 2 | `26020-Package_Requirements.docx` package heading 40 (slice 510-515) |
| Incinerator (low pressure flare stack) `FL-6920-1` | 1 | NPS 6 x 54,861 mm (180') tall; sized for max relief rate from tank farm and VRU (slice text truncated — confirm trailing clause) | `26020-Package_Requirements.docx` package heading 40 (slice 510-515) |
| Incinerator Blower `B-6920-1` | 1 | ARR-4 Disch.; TEFC, 405T frame; 74 kW (100 hp), 575V/3Ph/60Hz, 1800 rpm; Type VJ, Class II | `26020-Package_Requirements.docx` package heading 40 (slice 510-515) |
| Instrumentation reference | Per PFD | "See PFD for instrumentation" — PFD location TBD | `26020-Package_Requirements.docx` package heading 40 (slice 510-515) |
| Building | Self-framing building, erected at site | — | `26020-Package_Requirements.docx` package heading 40 (slice 510-515) |

### Design Conditions and Process Data

| Attribute | Value | Source |
|---|---|---|
| Site ambient design temperature | -40 deg C (winter operation, facility-wide basis); KO drum design min/max -45.5 deg C / 260 deg C | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 696; `26020-Package_Requirements.docx` package heading 40 (KO drum) |
| Inlet streams | Spent caustic tank vapours; caustic treating overhead/dilution/enrichment gas; potentially other vent/relief headers per shared-interface allocation | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 400, 402, 547; `26020-Package_Requirements.docx` package heading 40 (Basic Scope) |
| Inlet composition | TBD (governed by upstream caustic treating package and shared-interface allocation) | TBD |
| Design throughput | Incinerator stack `FL-6920-1` sized for max relief rate from tank farm and VRU; reconcile with caustic-oxidation demand 214 SCFM TBC and shared-interface allocation | `26020-Package_Requirements.docx` package heading 40 (Major included equipment); `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 477 |
| KO drum design pressure | 345 kPag | `26020-Package_Requirements.docx` package heading 40 (Major included equipment) |
| Transfer pump rated flow | 70 USGPM | `26020-Package_Requirements.docx` package heading 40 (Major included equipment) |
| Blower motor rating | 74 kW (100 hp), 575V/3Ph/60Hz, 1800 rpm | `26020-Package_Requirements.docx` package heading 40 (Major included equipment) |
| Combustion control | TBD (vendor design) | TBD |
| Stack discharge basis | Low pressure flare stack form factor; final emissions/stack height/permit data TBD | `PACKAGE_REGISTER.csv` (ScopeNotes); `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 555 |

### Materials and Construction

| Attribute | Value | Source |
|---|---|---|
| Caustic-service material constraints | Aluminum SHALL NOT be used in caustic service / caustic building; further caustic material/coating details TBC | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 402 |
| Caustic drain interface | Minimum drain header rating 300# ANSI; drain header terminates at 300# flange at the spent-caustic tank; max drain temperature 121 deg C / 250 deg F TBC | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 493 |
| Winterization | Required (site -40 deg C design); detail TBD (vendor design) | ASSUMPTION (site-wide DBM basis); `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 696 |
| Modularisation / skid limits | TBD (vendor design, coordinated with EPC Integrator) | TBD |

### Interface Envelope (Package Vendor scope boundary)

| Interface Type | Applicability | Source |
|---|---|---|
| Process Piping | YES | `INTERFACE_REGISTER.csv` IFC-3FF4A46502 |
| Utility Piping | YES | `INTERFACE_REGISTER.csv` IFC-B01B4DDC89 |
| Relief / Flare / Vent | YES | `INTERFACE_REGISTER.csv` IFC-DBC4027D02 |
| Drain / Containment | YES | `INTERFACE_REGISTER.csv` IFC-2BACDFA5F1 |
| Electrical Power | YES | `INTERFACE_REGISTER.csv` IFC-D8FC238CE8 |
| Grounding / Bonding | YES | `INTERFACE_REGISTER.csv` IFC-FD13F602FB |
| Area / Exterior Lighting | YES | `INTERFACE_REGISTER.csv` IFC-1892D97798 |
| I&C / Control Cabling | YES | `INTERFACE_REGISTER.csv` IFC-5ED2CD719C |
| Building HVAC / Services | YES | `INTERFACE_REGISTER.csv` IFC-588E647FEE |
| Fire & Gas / Safety Systems | YES | `INTERFACE_REGISTER.csv` IFC-F147F6DD86 |
| Maintenance Access | YES | `INTERFACE_REGISTER.csv` IFC-A18F15D335 |
| Structural / Foundations / Supports | YES | `INTERFACE_REGISTER.csv` IFC-23A65D01E5 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service classification | Sour service / vent destruction (oxidiser) | ASSUMPTION (from DBM context of sour streams and incinerator role) |
| Hazardous area classification | TBD (vendor / EPC interface) | TBD |
| Noise limits | TBD | TBD |
| Emissions limits | TBD (final emissions table requires confirmation of incinerator service split, flare/blowdown loads, and any regulatory permit values) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 555 |
| Detection coverage at package | LEL, H2S, methyl mercaptan, and fire detection devices apply per process hazards, ventilation, equipment spacing, flare/vent interfaces, caustic/DSO systems (detector quantity, tag list, set points, voting logic, placement, calibration TBD) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 838 |

## Construction

| Item | Value | Source |
|---|---|---|
| Fabrication / supply scope | Vendor-fabricated / supplied package (knockout drum, transfer pump, low-pressure flare stack, blower) plus piping, supports, controls, and ancillaries inside the vendor scope boundary | `PACKAGE_REGISTER.csv` (ScopeNotes) |
| Vendor responsibility | Package engineering, package design, vendor documentation, physical equipment package supply | `PACKAGE_REGISTER.csv` (Description); `OBJECTIVE_REGISTER.csv` (OBJ-004) |
| EPC Integrator responsibility | Integration into facility process, interfaces, tie-ins, constructability, procurement / construction coordination, facility-level integration | `PACKAGE_REGISTER.csv` (Description); `OBJECTIVE_REGISTER.csv` (OBJ-004) |
| Installation / tie-in plan owner | EPC Integrator via DEL-087-03 (Construction Work Package) | `DELIVERABLE_REGISTER.csv` (DEL-087-03) |
| Foundations / supports | EPC Integrator civil/structural scope (vendor provides loads, anchor patterns, and anchorage details) | ASSUMPTION (OBJ-004 / OBJ-008 division of responsibility) |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- Gate 7 PROJECT_DECOMP snapshot:
  - `DELIVERABLE_REGISTER.csv` (DEL-087-04 row)
  - `PACKAGE_REGISTER.csv` (PKG-087 row)
  - `INTERFACE_REGISTER.csv` (PKG-087 rows)
  - `OBJECTIVE_REGISTER.csv` (OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010)
- Accessible source slices:
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
  - `_Sources/26020-Package_Requirements.docx` package heading 40 ("26020-02-PT-25-003 - Incinerator", Basic Scope + Major Included Equipment, slice 510-515 in paragraph index)
- Inaccessible / location TBD: `26020-01-PT-RFQ-25-003_Incinerator.docx`; PFD referenced by source (`See PFD for instrumentation`)
