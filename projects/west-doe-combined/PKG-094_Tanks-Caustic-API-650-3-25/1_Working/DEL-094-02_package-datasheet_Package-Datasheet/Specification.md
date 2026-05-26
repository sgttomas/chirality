# Specification — Package Datasheet (PKG-094 Tanks, Caustic API 650 3-25)

> Status: INITIALIZED. Requirements are source-grounded to the 3-25 DBM (locally accessible)
> and to the PROJECT_DECOMP GATE-07 registers. Items not anchored in accessible source are
> labeled `TBD` or `ASSUMPTION`.

## Scope

This specification governs the EPC Integrator-issued Package Datasheet for PKG-094 — Tanks,
Caustic (API 650), supporting the 03-25 West Doe Compressor Station and Liquids Hub.

In scope:
- One (1) Fresh Caustic Tank and one (1) Spent Caustic Tank, atmospheric, API 650.
- Storage service for 50 wt% NaOH/H₂O caustic solution feeding/returning from the
  non-regenerative caustic mercaptan treating package.
- The facility-side data, interface basis, and design conditions required for the Package
  Vendor to engineer and fabricate the tank package.

Excluded from this deliverable (carried in PKG-094 sibling deliverables):
- Scope of Work narrative (DEL-094-01).
- Construction Work Package (DEL-094-03).
- Vendor engineering output (DEL-094-04) and turnover docs (DEL-094-05).
- EPC review/acceptance evidence (DEL-094-06).

Excluded from the package scope itself:
- Caustic regeneration equipment (not part of 03-25 basis; DBM line 389).
- LACT or condensate stabilization equipment (not part of PKG-094).

## Requirements

### R1 — Equipment Count and Service
- R1.1 The package SHALL include one (1) Fresh Caustic Tank and one (1) Spent Caustic Tank.
  Source: PACKAGE_REGISTER.csv Notes (PKG-094).
- R1.2 The Fresh Caustic Tank SHALL store and supply fresh caustic solution to the caustic
  treatment unit. Source: PACKAGE_REGISTER.csv Notes.
- R1.3 The Spent Caustic Tank SHALL receive and safely store spent caustic from the
  pressurized caustic drain drum. Source: PACKAGE_REGISTER.csv Notes.

### R2 — Code and Capacity
- R2.1 Tanks SHALL be designed and fabricated to API 650. Source: PACKAGE_REGISTER.csv title
  ("Tanks, Caustic (API 650) 3-25"); decomposition package title.
- R2.2 Nominal tank capacity SHALL be 400 bbl (each). Source: DBM §Scope Inclusions
  (`3-25_Comp_and_Liquids_DBM.md` line 40).
- R2.3 Tanks SHALL be atmospheric, with vapor-space design suited to a 32 oz/in² blanket
  basis. Source: DBM §Condensate Mercaptan Treating (line 402).

### R3 — Stored Fluid Basis
- R3.1 Design fluid SHALL be 50 wt% NaOH/H₂O caustic solution. Source: DBM line 402.
- R3.2 Design specific gravity basis is 1.75 (DBM source: TBC). ASSUMPTION until confirmed
  by detailed design. Source: DBM line 402.

### R4 — Blanket, Heating, Insulation
- R4.1 Tanks SHALL be provided with an LP fuel-gas blanket. Source: DBM line 402.
- R4.2 Tanks SHALL be heated and insulated. Source: DBM line 402.
- R4.3 The Fresh Caustic Tank SHALL NOT be connected to the VRU. Source: DBM line 402.
- R4.4 The Spent Caustic Tank vent SHALL be routed via flame arrestor to the incinerator
  header and SHALL support truck-out. Source: DBM line 402.

### R5 — Materials
- R5.1 Aluminum SHALL NOT be used in the caustic building (or in any caustic-wetted or
  caustic-vapor-exposed component within the package). Source: DBM line 402.
- R5.2 Tank material of construction and coating/lining are TBC at decomposition; the
  Package Vendor SHALL propose materials suitable for 50 wt% NaOH service consistent with
  API 650 and submit for EPC review. Source: DBM line 402.
- R5.3 Caustic drain service piping material selection SHALL address caustic embrittlement.
  Source: DBM §Drains (line 493).

### R6 — Connections and Drain Interface
- R6.1 The spent-caustic tank caustic-drain inlet connection SHALL terminate at a 300# ANSI
  flange minimum (caustic drain header rating). Source: DBM line 493.
- R6.2 Caustic drain max design temperature is 121 °C / 250 °F (TBC); min 80 °F. Source:
  DBM line 493.

### R7 — Facility Interfaces (PKG-094)
The Package Datasheet SHALL document the package's tie-in points for each applicable PKG-094
interface. Source: INTERFACE_REGISTER.csv (all marked YES):

- R7.1 Process Piping (IFC-12C92E9A0A).
- R7.2 Relief / Flare / Vent (IFC-AFD520D296) — including incinerator-header vent path.
- R7.3 Drain / Containment (IFC-DA053E0FE2) — including caustic drain header.
- R7.4 Grounding / Bonding (IFC-35E994F2DE).
- R7.5 Area / Exterior Lighting (IFC-946F48A91C).
- R7.6 Cathodic Protection (IFC-7EBC5D8325).
- R7.7 I&C / Control Cabling (IFC-15D9C87C0A).
- R7.8 Grading / Site Drainage / Spill Containment (IFC-61D7941475).
- R7.9 Structural / Foundations / Supports (IFC-94BBAEE00A).

### R8 — Site and Environmental Basis
- R8.1 The Package Datasheet SHALL reference the 03-25 ambient, wind, snow, precipitation,
  geotechnical, and seismic design basis from the 3-25 DBM. Specific clause-level values:
  `location TBD` (DBM sections referenced; numeric values not extracted in this draft).
  Source: DBM §§Ambient Design Conditions; Wind, Snow, Precipitation; Geotechnical and
  Seismic Basis.

### R9 — Documentation Outputs
- R9.1 The deliverable SHALL include a package technical datasheet covering the equipment
  in R1, design conditions in R2-R6, and the interface tie-in summary in R7. Source:
  DELIVERABLE_REGISTER.csv anticipated artifacts (DEL-094-02).
- R9.2 The deliverable SHALL include a package interface requirements matrix covering R7.1
  through R7.9. Source: DELIVERABLE_REGISTER.csv.
- R9.3 The deliverable SHALL include the vendor engineering handoff basis (boundary,
  battery limits, terminal points) suitable for vendor RFQ. Source: DELIVERABLE_REGISTER.csv.

## Standards

| Standard | Use | Locally Accessible? |
|---|---|---|
| API 650 — Welded Tanks for Oil Storage | Tank construction code | `location TBD` (referenced by package title and decomposition; clause text not in `_Sources/`) |
| 3-25 DBM (`W242510-PRC-DBM-000001-001`) | Process, material, drain basis | Yes (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`) |
| 26020-Package_Requirements.docx (package heading 46) | Vendor RFQ basis | Source present but not parsed in this run; `location TBD` for clause text |
| Provincial/CSA pressure & lifecycle code references | TBD | TBD |

## Verification

| Requirement | Verification Approach |
|---|---|
| R1.1-R1.3 | Document review of vendor scope sheet vs. PACKAGE_REGISTER.csv |
| R2.1 | Vendor API 650 design report and U-stamp/manufacturer data report review |
| R2.2 | Vendor calculation/datasheet review (capacity ≥ 400 bbl each) |
| R2.3, R4.1, R4.4 | P&ID review and vendor mechanical datasheet review |
| R3.1, R3.2 | Vendor material-of-construction selection report citing 50 wt% NaOH service; design SG confirmation |
| R4.2, R4.3 | P&ID and tie-in matrix review |
| R5.1, R5.2, R5.3 | Vendor MOC submittal; coating spec; piping class for caustic service |
| R6.1, R6.2 | Piping class review; tie-in datasheet; HAZOP review of caustic drain |
| R7.* | Package interface requirements matrix sign-off (EPC + Vendor) |
| R8.1 | Cross-check vendor design conditions against DBM clause references |
| R9.* | Deliverable artifact register check at Gate 5 |

## Documentation

Required artifacts produced by this deliverable (per DELIVERABLE_REGISTER.csv):

- Package technical datasheet (Datasheet.md plus any vendor-style tabular sheet).
- Vendor engineering handoff basis statement.
- Package interface requirements matrix.
- Source-supported equipment and design criteria summary.
