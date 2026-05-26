# Datasheet — DEL-049-03 Construction Work Package (Sales Gas Booster Compressor)

> Descriptive datasheet for the Construction Work Package (CWP) deliverable. Values are sourced from the accessible package requirements slice for `26020-01-PT-12-004 - Sales Gas Booster Compressor` and the deliverable's `_CONTEXT.md`. Missing values are marked `TBD`; inferences are labelled `ASSUMPTION`.

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-049-03_construction-work-package` |
| Name | Construction Work Package |
| ParentPackageID | `PKG-049` |
| PackageName | Sales Gas Booster Compressor |
| Equipment Tag | `26020-01-PT-12-004` (SourcePath: `_Sources/26020-Package_Requirements.docx`, SectionRef: package heading 4 — Sales Gas Booster Compressor) |
| Discipline | Mechanical (lead) with Civil/Structural, Piping, Electrical, I&C, Fire & Gas interfaces |
| Type | EPC Construction Work Package |
| ResponsibleParty | EPC Integrator |
| Decomposition Snapshot | `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Construction object | Sales Gas Booster Compressor package — motor-driven separable reciprocating gas compressor with filter coalescer | `26020-Package_Requirements.docx`, SGBC Basic Scope |
| Major included equipment | Ariel KBX/X reciprocating compressor; 8-pole induction motor 4000 V / 3PH / 60 Hz / 891 RPM DOL with soft-start; per-stage forced-air intercoolers (API 661, horizontal, single-fan, automated louvers); per-stage suction scrubbers (two-phase, vertical mesh/vane); packing vent/drain pot; seal-pot waste-oil transfer pump; filter coalescer (0.3 µm @ 99.97 %, bandlock QOC, 100 MMSCFD design) | `26020-Package_Requirements.docx`, SGBC Major Included Equipment |
| Capacity (design) | 3,962 e3m3/day (140 MMSCFD); no turndown | `26020-Package_Requirements.docx`, SGBC Scope Notes |
| Driver | 1,000 kW (1,340 HP) induction motor, 4000 V / 3PH / 60 Hz, 891 RPM fixed speed, TEFC or WPII, non-sparking bidirectional fan, NEMA MG 1 | `26020-Package_Requirements.docx`, SGBC Scope Notes |
| Construction scope demarcation ("By others") | Shipping the compressor package to site; installation on piles; tie-in piping; electrical connections; mounting platform and stairs | `26020-Package_Requirements.docx`, SGBC Scope Notes — explicit "By others" list |

## Conditions (Construction-Relevant)

| Item | Value | Source |
|---|---|---|
| Suction design pressure | 6,137 kPag (890 psig) | SGBC Scope Notes |
| Discharge design pressure | 12,866 kPag (1,866 psig) | SGBC Scope Notes |
| Inlet operating temperature | 110 °F (43.3 °C) summer | SGBC Scope Notes |
| Suction scrubber inlet liquid density | 0.61 SG (assumption per source) | SGBC Scope Notes |
| Hydrotest / leak-test parameters | TBD (PIP-024 Hydrotest/Pressure Test Package not yet produced) | Anticipated artifact |
| Site/area classification, weather window, lay-down area | TBD (project execution plan slice not accessible in `_REFERENCES.md`) | TBD |

## Construction Scope Items Covered

The CWP discharges these decomposition scope items (Source: `DELIVERABLE_REGISTER.csv` row for `DEL-049-03`):

- `SOW-0169`
- `SOW-0170`
- `SOW-0171`
- `SOW-0172`

## Construction Interface Applicability

Sourced from the SGBC Physical Interface Summary table:

| Interface | Applicability |
|---|---|
| Process Piping | Yes |
| Utility Piping | Yes |
| Relief / Flare / Vent | Yes |
| Drain / Containment | Yes |
| Electrical Power | Yes |
| Area / Exterior Lighting | Yes (`26020-Packages_Interfaces.3.xlsx` col M, row 80) |
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

## Construction Artifacts (Anticipated)

Per `_CONTEXT.md` and the decomposition `Anticipated Artifacts` field:

- Construction work package (master document set)
- Installation and tie-in workface plan
- Construction interface and turnover checklist

## References

- `_Sources/26020-Package_Requirements.docx` — heading 4 (`26020-01-PT-12-004 - Sales Gas Booster Compressor`)
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — row 80 (interface summary)
- `_CONTEXT.md` (deliverable identity)
- `DELIVERABLE_REGISTER.csv` — GATE-07 snapshot row `DEL-049-03`
- `RFQ/Bid Docs/26020-01-PT-RFQ-12-004-Sales Booster Comp.docx` — RFQ basis cited by source (location TBD; not present under `_Sources/`)
