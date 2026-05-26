# Specification: DEL-057-02_package-datasheet — Package Datasheet (PKG-057 Stabilizers)

> Normative document. Requirements derive from accessible decomposition source slices. Where exact source location is not opened in this pass, the source is cited and the slice marked `location TBD`. Inferences are labeled `ASSUMPTION`.

## Scope

### Covers
- The EPC Integrator's Package Datasheet for `PKG-057` Stabilizers — the technical handoff record that consolidates package data required for third-party vendor or discipline package engineering and design. (`_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-057-02)
- The package data, design conditions, equipment list, and interface requirements for three (3) Inlet Stabilizer Packages serving the 04-25 Deepcut facility. (SOW-0178; SOW-0179; PACKAGE_REGISTER.csv PKG-057)

### Excludes
- Package vendor's internal package engineering and design execution (vendor-owned per SOW-0177).
- Items defined by SOW-0180 as `By others`: interconnecting piping at skid edge, DCS integration, foundations, electrical power supply from plant MCC, installation/erection.
- Package-specific exclusions beyond those above: TBD — none stated in source (PACKAGE_REGISTER.csv PKG-057 records `TBD; no package-specific exclusions stated in source materials`).

## Requirements

### R-DS-01 — Identification of the package
The datasheet SHALL identify the package by `PKG-057`, name `Stabilizers`, WBS 01, workbook tracking `26020-01-17-005`, discipline Mechanical, and responsible party EPC Integrator. (Source: PACKAGE_REGISTER.csv PKG-057; `_CONTEXT.md`.)

### R-DS-02 — Equipment count and configuration
The datasheet SHALL record three (3) Inlet Stabilizer Packages configured as 3 x 40%. (Source: SOW-0178, SOW-0179.)

### R-DS-03 — Design throughput
The datasheet SHALL record a design rate of 1,272 m3/d (8,000 bbl/d) per package and a turndown ratio of 3:1. (Source: SOW-0179, SOW-0180.)

### R-DS-04 — Operating conditions
The datasheet SHALL record operating conditions, including: Flash Feed Separator pressure 345 kPag, temperature 30.6 °C, retention time ~15 min; Feed/Bottoms Exchanger pre-heat to 71 °C; Stabilizer Column inlet temperature 71 °C. (Source: SOW-0180.)

### R-DS-05 — Design conditions
The datasheet SHALL record design conditions, including: Flash Feed Separator design inlet pressure 1724 kPag and design inlet temperature 60 °C; Feed/Bottoms Exchanger minimum approach 16.7 °C (30 °F); Stabilizer Column minimum pressure 793 kPag; turndown ratio 3:1; Stabilizer Product Cooler sized to 130%. (Source: SOW-0180.)

### R-DS-06 — Driver/motor configuration
The datasheet SHALL record that Feed Pumps and Product Cooler Fans use electric motor drivers that are VFD-compatible. (Source: SOW-0180.)

### R-DS-07 — Major equipment list
The datasheet SHALL list, at minimum, the major included equipment named in SOW-0179: trayed reboiled distillation columns; 20 floating valve trays; one LIT; one TIT — and the equipment named in SOW-0178: stabilizer flash feed separator, basket strainers, stabilizer feed pumps, feed/bottoms exchanger; plus the stabilizer product cooler implied by SOW-0180 sizing. Additional vendor BOM entries: TBD (full BOM not enumerated in accessible source extracts; location TBD in 26020-Package_Requirements.docx package heading 12).

### R-DS-08 — Ownership split
The datasheet SHALL record the ownership split: Package Vendor owns package engineering, design, vendor documentation, and physical equipment package; EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination. (Source: PACKAGE_REGISTER.csv PKG-057; SOW-0177.)

### R-DS-09 — Interface requirements matrix
The datasheet SHALL include a package interface requirements matrix enumerating all required interface types for PKG-057: Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports. Each interface is `Required = YES`. (Source: INTERFACE_REGISTER.csv rows scoped to PKG-057; PACKAGE_REGISTER.csv PKG-057.)

### R-DS-10 — Source traceability
Every non-trivial value in the datasheet SHALL cite its source (workbook row, SOW item, register row, or document heading) or be marked `TBD` with the source location flagged. (Authority: deliverable governance; `_REFERENCES.md`.)

### R-DS-11 — By-others exclusions
The datasheet SHALL explicitly call out the `By others` scope from SOW-0180 so that vendor and EPC scopes are unambiguous at the package-edge.

## Standards

The following standards/specifications are referenced by the source materials and govern this datasheet's content. Direct standards-clause extracts are `location TBD` until source slices are opened.

| Reference | Role | Location |
|---|---|---|
| Workbook Packages row 82 (`26020-Packages_Interfaces_4_export.xlsx`) | Authoritative package row | location TBD (binary not directly read; extracts promoted via Gate-07 ledgers are authoritative for items reproduced) |
| `26020-Package_Requirements.docx` package heading 12 | Authoritative package requirements text | location TBD (binary not opened; SCOPE_LEDGER extracts authoritative for cited items) |
| `Bid Docs/Budgetary/26020-01-PT-RFQ-17-005_Inlet Stabilizers_R0.docx` | RFQ basis (Word source basis for PACKAGE_REGISTER) | location TBD |
| `DBM-Deepcut/4-25_Deepcut_DBM.md` | Design basis memorandum (Deepcut 04-25) | location TBD in this pass |
| Process-mechanical industry codes (e.g., ASME, API for distillation columns/exchangers/pumps) | ASSUMPTION: typically applicable to Mechanical Process Piping packages; specific code list not enumerated in source extracts. | TBD |

## Verification

| Requirement | Verification Approach |
|---|---|
| R-DS-01 | Cross-check datasheet identity fields against PACKAGE_REGISTER.csv PKG-057 and `_CONTEXT.md` identity table. |
| R-DS-02 | Confirm "three (3) packages, 3 x 40%" text present and consistent with SOW-0178/0179. |
| R-DS-03 | Numeric check: 1,272 m3/d / 8,000 bbl/d / 3:1 turndown all present and unit-consistent. |
| R-DS-04, R-DS-05 | Operating and design condition tables compared against SOW-0180 line-by-line. |
| R-DS-06 | Confirm driver text matches SOW-0180. |
| R-DS-07 | Verify equipment list completeness vs. SOW-0178/0179; flag any non-listed BOM items as `TBD` with source location. |
| R-DS-08 | Confirm ownership-split paragraph matches PACKAGE_REGISTER.csv PKG-057 description verbatim or by equivalence. |
| R-DS-09 | Validate the interface matrix exactly enumerates the 13 interfaces in INTERFACE_REGISTER.csv for PKG-057 with `Required = YES`. |
| R-DS-10 | Editorial review: every numeric value or normative claim has a source citation or `TBD` marker. |
| R-DS-11 | Confirm a `By others` callout reproducing SOW-0180 list is present. |

## Documentation

Anticipated artifacts that this deliverable produces (from `_CONTEXT.md`):

- Package technical datasheet
- Vendor engineering handoff basis
- Package interface requirements matrix
- Source-supported equipment and design criteria

Companion deliverable-local documents:
- `Datasheet.md` (this deliverable's primary artifact view)
- `Specification.md` (this file)
- `Guidance.md`
- `Procedure.md`
