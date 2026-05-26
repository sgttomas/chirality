# Specification: DEL-079-02 — Package Datasheet (Instrument Air Building, PKG-079)

## Scope

This Package Datasheet is the EPC Integrator's normative technical handoff for the **Instrument Air Building** (`26020-01-PT-39-001`, CoA `26020-01-39-001`, Mechanical discipline). It defines the equipment, design conditions, interface scope, and vendor engineering deliverables required for a third-party vendor or discipline package to engineer, fabricate, and integrate the package.

**In scope of this datasheet (as the deliverable artifact):**
- Capturing source-supported equipment list, design and operating conditions, and PSV setting.
- Capturing the package-level interface matrix (per the Packages interface register, row 69).
- Capturing the vendor engineering deliverables list (handoff manifest).
- Declaring the source basis and the by-others boundary.

**Out of scope of this datasheet:**
- Detailed equipment data sheets (vendor-produced deliverables MEC-003, MEC-008, MEC-009, INS-003, etc., per the handoff manifest).
- Detailed building/HVAC, structural, electrical, fire & gas designs (interface scopes; produced under the cited deliverable IDs).
- Site installation, piling, tie-in piping, electrical connections, mounting platform, and stairs — explicitly **by others** per source.

## Requirements

All requirements below are source-traceable to `26020-Package_Requirements.docx` section `26020-01-PT-39-001` unless otherwise marked. `ASSUMPTION` and `TBD` labels are used where source is silent.

### R1 — Package architecture

- R1.1 The package SHALL consist of: 2 oil-injected rotary screw air compressors (motor-driven, air-cooled); 1 wet air receiver; 2 dryer pre-filters; 1 regenerative desiccant air dryer (100% capacity, 2 towers, one operating / one regenerating); 1 common after-filter; 1 dry air receiver (or 2 × 50% capacity receivers). *(Source: Basic Scope, Major Included Equipment.)*

### R2 — Capacity and rating

- R2.1 Each compressor SHALL be rated **1113 SCFM at 861 kPag (125 psig)** discharge pressure. *(Source: Major Included Equipment; scope-notes table.)*
- R2.2 The desiccant dryer SHALL be sized for two compressors **and leave**. *(Source: Major Included Equipment.)*

### R3 — Drivers (electrical)

- R3.1 Each compressor SHALL be driven by an electric motor, 200-250 HP (Major Included Equipment row states **250 HP**; scope-notes table states **200-250 HP** — CT-02 in Guidance Conflict Table).
- R3.2 Motors SHALL be **600 V / 3 PH / 60 Hz**, TEFC, **non-classified**, with **soft starter or VFD-ready** configuration and **anti-condensation space heaters**. *(Source: scope-notes table; Major Included Equipment.)*
- R3.3 Motor speed SHALL be determined by the vendor. *(Source: scope-notes table.)*

### R4 — Pressure design

- R4.1 Maximum system design pressure: **1034 kPag (150 psig)**.
- R4.2 Compressor maximum discharge / shutdown pressure: **1000 kPag**.
- R4.3 Minimum system pressure: **551 kPag (80 psig)**.
- R4.4 Facility shutdown pressure: **482 kPag (70 psig)**.
- R4.5 All PSVs in the package SHALL be set at **948 kPag (137.5 psig)**.
*(Source: scope-notes table; Major Included Equipment.)*

### R5 — Temperature design

- R5.1 Design temperature range: **-40 °C to 38 °C**. *(Source: scope-notes table.)*

### R6 — Delivered-air quality

- R6.1 Delivered instrument air SHALL have a **maximum water dew point of -73.3 °C at 1000 kPag**. *(Source: Major Included Equipment; scope-notes table.)*

### R7 — Interfaces

- R7.1 Applicable interfaces SHALL be engineered consistent with row 69 of `26020-Packages_Interfaces_4_export.xlsx` (sheet `Packages`) and the interface table in the Requirements doc. Applicable interface types: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports.
- R7.2 Process Piping, Relief / Flare / Vent, EHT, Cathodic Protection, Communications / Network, Grading / Site Drainage / Spill Containment, Product Loading, and Pipeline / Pigging interfaces are **not applicable**. *(Source: xlsx row 69; Requirements doc interface table.)*

### R8 — Vendor handoff manifest

- R8.1 The vendor SHALL produce the deliverables listed in **Datasheet.md § Vendor Engineering Deliverables**, grouped per source.

### R9 — By-others boundary

- R9.1 The following are **by others** (not within the vendor's package scope): shipping compressor packages to site; installation on piles; tie-in piping; electrical connections; mounting platform and stairs. *(Source: scope-notes table, "By others".)*

## Standards

Governing standards are not enumerated explicitly in the locally accessible source slices for this package. The following are referenced indirectly and require human confirmation (`location TBD`):

- `REG-021` Fire Code / Building Code Compliance Package — applicable fire/building codes `TBD` (handoff manifest deliverable).
- `REG-022` Pressure Equipment Registration Package — jurisdictional pressure-equipment registration `TBD`.
- `TSF-009` SIL Determination and `TSF-011` SRS imply functional-safety standards (commonly IEC 61511) — `ASSUMPTION: likely applicable`; not derivable from source at clause level.
- API/ISO standards for rotary screw air compressors and desiccant dryers — `TBD: standards not stated in available source slices`.

## Verification

| Req | Verification Approach | Verifying Deliverable(s) |
|---|---|---|
| R1, R2 | Vendor data sheet review + equipment list reconciliation | MEC-002, MEC-003, MEC-008, MEC-009 |
| R3 | Motor data sheets + motor starting study | ELE-011, ELE-020 |
| R4 (pressure design) | Mechanical calc package + PSV sizing review + hydrotest | MEC-014, PIP-024, REG-022 |
| R4.5 (PSV set) | PSV data sheets + ITP witness | INS-003 (or vendor PSV data sheet), QLT-003 |
| R5, R6 | Performance test (FAT) — dew point and temperature envelope | MEC-021, MEC-022 |
| R7 (interfaces) | Interface check against `26020-Packages_Interfaces_4_export.xlsx` row 69; interconnection diagrams; loop diagrams | ELE-028, INS-008, CTL-026 |
| R8 (handoff) | Vendor Document Index reconciliation | PRQ-009, PRQ-016 |
| R9 (by-others) | Battery-limit walkdown; scope split confirmation | MEC-017, STR-006 |

## Documentation

Documentation required from this deliverable and its downstream consumers:

- **This deliverable produces:** `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` for `DEL-079-02`.
- **Anticipated artifacts (from `_CONTEXT.md`):** package technical datasheet; vendor engineering handoff basis; package interface requirements matrix; source-supported equipment and design criteria. These are all satisfied within the four documents and the Datasheet's handoff manifest.
- **Vendor documentation:** as enumerated in Datasheet.md § Vendor Engineering Deliverables.
