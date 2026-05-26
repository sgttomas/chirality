# Datasheet — Vendor Engineered Equipment Package (DEL-100-04)

> Descriptive datasheet for the Package Vendor's engineered Hydrogen Peroxide Sweetening Unit
> equipment package. Values are drawn from the locally accessible source slice for
> `26020-03-PT-27-001 - Hydrogen Peroxide Sweetening Unit` in
> `_Sources/26020-Package_Requirements.docx` (package heading 52). Items not stated in source
> are marked `TBD`; inferred items are labeled `ASSUMPTION`.

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-100-04_vendor-engineered-equipment-package` |
| Name | Vendor Engineered Equipment Package |
| ParentPackageID | `PKG-100` |
| Package Name | Hydrogen Peroxide Sweetening Unit |
| Package Tag (source) | `26020-03-PT-27-001` (source: `_Sources/26020-Package_Requirements.docx`, package heading 52) |
| Discipline | Mechanical |
| Type | Vendor Package Production Unit |
| Responsible Party | Package Vendor (engineering/design/equipment); EPC Integrator integration review |
| Source Basis (RFQ) | `Bid Docs/Budgetary/26020-03-PT-RFQ-27-001-H202_Sweet_Unit.docx` (referenced by package heading 52; not locally accessible — `location TBD`) |
| Site / Location Status | "3-25 West Doe Liquids Hub; vetted package scope basis" (source: package heading 52) |

## Attributes — Basic Scope (as-engineered)

The package supplies one (1) sour-water hydrogen peroxide treatment package consisting of
the following equipment items (source: package heading 52, "Basic Scope" and "Major
Included Equipment"):

| Item | Description | Source Note |
|---|---|---|
| Hydrogen Peroxide Storage Tank | 400 BBL | Major Included Equipment |
| Hydrogen Peroxide Pumps | Chemical injection pumps — Vendor to design | Major Included Equipment; "Vendor to design" |
| Static Mixer | Vendor to design | Major Included Equipment |
| Hydrogen Peroxide Reactor(s) | Vendor to design (quantity per attached PFD) | Major Included Equipment; PFD referenced but not locally accessible — `location TBD` |
| Additional equipment | "Additional equipment shown in PFD" | PFD `location TBD` |
| Building | Self-framing building, erected at site | Major Included Equipment |

### Process Function (descriptive)

Sour water is routed through the static mixer and then to the Hydrogen Peroxide Reactors
for treatment. Hydrogen peroxide is pumped in from the Hydrogen Peroxide Storage Tank by
the chemical injection pumps. Treated water is sent to produced water storage tanks.
(Source: package heading 52, "Process function".)

## Conditions

### Operating Conditions (source: package heading 52, "Operating conditions")

| Parameter | Value | Units |
|---|---|---|
| Sour water temperature | 9 | °C |
| Sour water pressure | 340.54 | kPag |
| Sour water flow rate | 160 (24,154) | m³/h (BBL/D) |

### Capacity / Design Throughput (source: package heading 52, "Capacity/design throughput")

| Parameter | Value |
|---|---|
| Package treatment capacity | 24,154 BBL/D |
| H₂O₂ Storage Tank capacity | 400 BBL |
| H₂O₂ Pump capacity | TBC — Vendor to design |

### Design Conditions (source: package heading 52, "Design conditions")

| Parameter | Value |
|---|---|
| Design conditions (process) | TBC (per source: "Design conditions TBC") |
| Ambient temperature — minimum | −40 °C |
| Ambient temperature — maximum | +35 °C |
| H₂O₂ supply | From onsite tank(s) |

### Drivers / Electrical (source: package heading 52, "Driver")

| Parameter | Value |
|---|---|
| Pump motor supply | 575 V / 3 PH / 60 Hz |
| Starting method | DOL or VFD |
| Local control | H-O-A or On-Off switch |
| Feeder source | 600 V MCC |

## Construction

| Item | Statement | Source Note |
|---|---|---|
| Building | Self-framing building erected at site | Major Included Equipment |
| Mounting / foundations | "By others" (foundations) | Scope Notes / Open Items |
| Interconnecting piping | "By others" | Scope Notes / Open Items |
| Electrical supply to MCC | "By others" | Scope Notes / Open Items |
| DCS integration | "By others" | Scope Notes / Open Items |
| Material specifications | `TBD` (not stated in source slice) | |
| Code/registration scope | `TBD` (vendor deliverable list includes Pressure Equipment Registration `REG-022`) | Vendor Engineering Deliverables list |

## Physical Interface Summary

Applicability of physical interfaces — source: package heading 52, "Physical Interface
Summary" (interface source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`; specific
deliverable row 63 referenced by `_CONTEXT.md`).

| Interface Type | Applicability |
|---|---|
| Process Piping | Yes |
| Utility Piping | Yes |
| Relief / Flare / Vent | Yes |
| Drain / Containment | Yes |
| Electrical Power | Yes |
| Area / Exterior Lighting | Yes |
| EHT | Yes |
| Grounding / Bonding | Yes |
| Cathodic Protection | No |
| I&C / Control Cabling | Yes |
| Communications / Network | No |
| Building HVAC / Services | No |
| Fire & Gas / Safety Systems | Yes |
| Maintenance Access | Yes |
| Grading / Site Drainage / Spill Containment | No |
| Structural / Foundations / Supports | Yes |
| Product Loading | No |
| Pipeline / Pigging | No |

## Vendor Engineering Deliverables (anticipated artifact set)

The engineered package is expected to be accompanied by the vendor deliverable set
enumerated in package heading 52 "Vendor Engineering Deliverables". Categories and
deliverable IDs are reproduced for reference (full list reproduced in `Specification.md`,
§Documentation):

- Core vendor documents: `PRQ-009`, `DOC-008`, `QLT-006`, `QLT-003`, `QLT-013`, `QLT-020`, `QLT-021`, `PRQ-013`, `PRQ-015`, `PRQ-016`
- Core package engineering: `MEC-001`, `MEC-002`, `MEC-003`, `MEC-006`, `MEC-014`, `MEC-016`, `MEC-017`, `MEC-018`, `MEC-021`, `MEC-022`, `MEC-023`, `MEC-024`, `MEC-025`
- Rotating equipment / pumps: `MEC-004`, `MEC-007`, `MEC-019`, `PRO-013`, `ELE-011`
- Static pressure equipment: `MEC-005`, `MEC-009`, `REG-022`
- Storage tanks: `MEC-011`
- Process package design: `PRO-004`, `PRO-005`, `PRO-007`, `PRO-008`, `PRO-010`, `PRO-011`, `PRO-012`, `PRO-020`, `PRO-025`, `PRO-026`, `PRO-027`, `PRO-028`
- Relief / flare / vent design: `PRO-014`, `PRO-015`, `PRO-016`, `PRO-017`, `PRO-018`
- Process piping interfaces: `PIP-003`, `PIP-004`, `PIP-006`, `PIP-007`, `PIP-008`, `PIP-009`, `PIP-017`, `PIP-018`, `PIP-024`, `PIP-025`, `PIP-028`
- Drainage / containment: `PRO-023`, `CIV-014`
- Electrical, lighting, EHT, grounding: `ELE-002`, `ELE-003`, `ELE-014`, `ELE-015`, `ELE-016`, `ELE-020`, `ELE-027`, `ELE-028`, `ELE-029`, `ELE-030`, `ELE-017`, `ELE-018`, `PIP-020`, `PIP-021`, `ELE-012`, `ELE-019`
- Instrumentation and controls: `INS-002`, `INS-003`, `INS-005`, `INS-006`, `INS-008`, `INS-009`, `INS-010`, `INS-011`, `INS-016`, `INS-017`, `INS-018`, `INS-025`, `INS-029`, `CTL-003`, `CTL-005`, `CTL-006`, `CTL-026`
- Building / HVAC / code: `PRO-024`, `TSF-023`, `REG-021`, `STR-002`, `STR-012`
- Fire & gas / technical safety: `TSF-002`, `TSF-003`, `TSF-004`, `TSF-009`, `TSF-011`, `TSF-013`, `TSF-028`
- Structural / foundations / supports / access: `STR-001`, `STR-004`, `STR-005`, `STR-006`, `STR-011`, `STR-013`, `STR-014`, `STR-020`

Interface Coordination Notes from package heading 52: "TBD."

## References

- `_REFERENCES.md` (this deliverable)
- `_Sources/26020-Package_Requirements.docx` — package heading 52, "26020-03-PT-27-001 — Hydrogen Peroxide Sweetening Unit"
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — row 63 (column M referenced by source for Area/Exterior Lighting)
- Decomposition row reference: Workbook Packages row 63 (`DECOMPOSITION_REF` Gate 7 snapshot)
- RFQ basis: `Bid Docs/Budgetary/26020-03-PT-RFQ-27-001-H202_Sweet_Unit.docx` — `location TBD` (not locally accessible)
- Process Flow Diagram (PFD) referenced by source — `location TBD`
