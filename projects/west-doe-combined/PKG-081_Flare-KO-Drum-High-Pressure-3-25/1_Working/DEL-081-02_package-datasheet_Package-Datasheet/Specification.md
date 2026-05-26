# Specification — DEL-081-02 Package Datasheet (Flare KO Drum (High Pressure) 3-25)

## Scope

### In Scope

The Package Datasheet shall declare the technical handoff data required for the Package Vendor to perform package engineering, design, vendor documentation, and physical equipment supply for `PKG-081` — Flare KO Drum (High Pressure) 3-25, consisting of:

- Two HP flare knock-out drums: `V-4100-2` (compressor area) and `V-4150-2` (tank farm). [DBM §"Flare and Blowdown"]
- Two HP flare KO drum transfer pumps: `P-4100-2` and `P-4150-2`, one per drum, configuration 1 x 100 percent. [DBM §"Flare and Blowdown"; §pump count table]
- Equipment design data, process conditions, mechanical/material requirements, interface requirements matrix, and source-supported design criteria.

### Out of Scope

- Construction/installation execution (covered by `DEL-081-03` Construction Work Package).
- Vendor package engineering deliverables themselves (covered by `DEL-081-04` Vendor Engineered Equipment Package).
- Vendor document turnover (covered by `DEL-081-05`).
- EPC vendor package review and acceptance (covered by `DEL-081-06`).
- LP flare KO drum scope (`PKG-082`, drum `V-3900-2`, pump `P-3900-2`). [DBM §"Flare and Blowdown"]

## Requirements

### R1 — Equipment Identity and Quantity

R1.1 The datasheet SHALL identify each KO drum by tag and area:
- `V-4100-2` — compressor area
- `V-4150-2` — tank farm

Source: DBM §"Flare and Blowdown".

R1.2 The datasheet SHALL identify each transfer pump by tag and provide redundancy basis:
- `P-4100-2` and `P-4150-2`, configuration "One per KO drum, 1 x 100 percent".

Source: DBM §"Pump Counts" (line 583).

### R2 — Process Conditions

R2.1 The datasheet SHALL state design pressure, design temperature, operating pressure, operating temperature, and relieving conditions for each drum. (Values: TBD — source slice with numeric values not locally accessible; ASSUMPTION: values reside in `Bid Docs/Budgetary/24292-02-PT-ENR-17-201_HP FKOD_R2.pdf` and `W242510-PRC-REP-000003-001`.)

R2.2 The datasheet SHALL state the HP relief inlet header connection size consistent with the project basis of 508 mm / 20 inch.

Source: DBM §"Flare and Blowdown" (line 499).

R2.3 The datasheet SHALL state the relief load and disposition basis (the package serves staggered blowdown to limit maximum relief).

Source: DBM §"Flare and Blowdown" (line 501).

### R3 — Materials and Service

R3.1 The datasheet SHALL identify service as HP flare relief liquid knockout and SHALL state whether sour-service (NACE MR0175 / ISO 15156) requirements apply. (ASSUMPTION: applicable based on facility isolation philosophy; confirm from process simulation, not locally accessible.)

Source: DBM §isolation philosophy (line 607).

### R4 — Mechanical Design Margins

R4.1 Vessel sizing margin SHALL use a starting basis of 10 percent on flow, validated against final process simulations and vendor package datasheets.

Source: DBM §"Equipment Design Margins".

R4.2 Pump sizing margin SHALL use a starting basis of 15 percent on flow unless package-specific design requires otherwise.

Source: DBM §"Equipment Design Margins".

### R5 — Liquid Disposition

R5.1 The datasheet SHALL specify pump discharge routing as "truck-out or transfer to slop".

Source: DBM §"Flare and Blowdown".

### R6 — Interfaces

R6.1 The datasheet SHALL declare the package interface requirements matrix covering: Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports.

Source: PACKAGE_REGISTER.csv row 54.

R6.2 The datasheet SHALL state that both KO drum outlets manifold to the HP flare side of the HP/Cryo and LP dual flare stack shared with 04-25.

Source: DBM §"Flare and Blowdown".

### R7 — Foundations / Structural

R7.1 The datasheet SHALL state that foundation and anchorage requirements are equipment-specific and SHALL list the inputs required for vendor foundation design (loads, geotechnical reference, wind/snow/seismic criteria, frost protection).

Source: DBM §"Foundations" (line 700).

### R8 — Responsibility Split

R8.1 The datasheet SHALL state that the Package Vendor owns package engineering, design, vendor documentation, and the physical equipment package; the EPC Integrator owns integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration).

Source: PACKAGE_REGISTER.csv row 54.

## Standards

| Standard | Applicability | Location |
|---|---|---|
| ASME BPVC Section VIII Div 1 (or Div 2) | Pressure vessel design for HP KO drums | location TBD (vendor basis; not declared in accessible DBM) |
| NACE MR0175 / ISO 15156 | Sour service (if confirmed) | location TBD |
| API 521 | Pressure-relieving and depressuring systems (flare KO drum sizing basis) | location TBD (ASSUMPTION: industry-standard reference; not cited in accessible DBM) |
| API 610 | Centrifugal pumps for transfer pumps (if applicable) | location TBD (ASSUMPTION) |
| Plant Shutdown and Blowdown Philosophy | `W242510-PRC-REP-000003-001` — required for final blowdown sequencing | DBM §"Flare and Blowdown" (line 501); document not locally accessible |

## Verification

| Requirement | Verification Approach |
|---|---|
| R1 | Cross-check vendor datasheet tag list vs PACKAGE_REGISTER.csv row 54 and DBM tag references |
| R2 | Reconcile against final flare studies and `W242510-PRC-REP-000003-001` when accessible |
| R3 | HAZOP/process review confirming sour-service applicability |
| R4 | Vendor calculation review vs DBM §"Equipment Design Margins" |
| R5 | Vendor P&ID review confirming slop/truck-out destination |
| R6 | Interface matrix walkdown against PACKAGE_REGISTER.csv row 54 interface list |
| R7 | Vendor foundation calculation review against equipment loads and project civil/geotechnical inputs |
| R8 | RACI review against PACKAGE_REGISTER.csv responsibility statement |

## Documentation

Required artifacts produced by this deliverable:

- Package technical datasheet (this deliverable's primary artifact)
- Vendor engineering handoff basis
- Package interface requirements matrix
- Source-supported equipment and design criteria

Source: `_CONTEXT.md` §"Anticipated Artifacts"; DELIVERABLE_REGISTER.csv row 289.
