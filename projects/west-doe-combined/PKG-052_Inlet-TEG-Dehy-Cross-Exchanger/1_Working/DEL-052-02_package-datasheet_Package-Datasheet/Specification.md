# Specification — DEL-052-02 Package Datasheet (PKG-052 Inlet / TEG Dehy Cross Exchanger)

## Scope

### Covers
- The normative requirements for the EPC Integrator-owned Package Datasheet artifact for PKG-052 — Inlet / TEG Dehy Cross Exchanger (E-5718-1).
- Required data fields, source-grounding, completeness rules, and acceptance criteria for the Package Datasheet such that it can serve as the technical handoff basis for third-party vendor or discipline package engineering and design.
- The package interface requirements matrix scope for the declared interface types in PACKAGE_REGISTER.csv row 62.

### Excludes
- Detailed vendor-engineered datasheets (TEMA datasheet body, mechanical drawings) — produced under DEL-052-04 Vendor Engineered Equipment Package.
- Construction work-package installation specifics — DEL-052-03.
- Vendor document register and turnover — DEL-052-05.
- EPC vendor package review and acceptance evidence — DEL-052-06.
- Package scope of work narrative — DEL-052-01.

Source: DELIVERABLE_REGISTER.csv rows 336-341; `_CONTEXT.md`.

## Requirements

### R-1 Identity and traceability (FACT)
The Package Datasheet SHALL identify: deliverable ID, parent package ID, package name, WBS, lead equipment tag (26020-01-PT-16-001), tagged equipment list (E-5718-1), responsibility split between Package Vendor and EPC Integrator, and pointers to the upstream source basis.
Source: `_CONTEXT.md`; PACKAGE_REGISTER.csv row 62.

### R-2 Tagged equipment (FACT)
The datasheet SHALL list at minimum E-5718-1 Inlet / TEG Dehy Cross Exchanger (1 ea., shell-and-tube, TEMA "R" BEM).
Source: PACKAGE_REGISTER.csv row 62 (Description); DBM-Deepcut/4-25_Deepcut_DBM.md §"Inlet / TEG Dehy Cross Exchanger".

### R-3 Process function statement (FACT)
The datasheet SHALL state the process function: cold sour inlet-separator overhead gas is heated against a warm-side process gas stream; sour gas thereafter flows to inlet compression and downstream gas treating; the warm-side stream is cooled before flowing to process-gas molecular-sieve inlet filter/coalescers.
Source: PACKAGE_REGISTER.csv row 62; DBM §"Inlet / TEG Dehy Cross Exchanger" (line 606).

### R-4 Design conditions (FACT where available)
The datasheet SHALL record at minimum:
- Duty: 5,514.3 kW (18.82 MMBTU/hr). Source: PACKAGE_REGISTER.csv row 62.
- Design pressure: 9,756 kPag (1,415 psig). Source: DBM table.
- Design temperature: 66 °C. Source: DBM table.
Process-side operating conditions (flows, T, P, ΔP) SHALL be marked `TBD` where not stated in accessible source slices, with the gap explicitly listed for resolution before vendor RFQ issue.

### R-5 Warm-side stream identity (CONFLICT)
The datasheet SHALL flag the warm-side stream identity as an unresolved conflict (dehydrated TEG-contactor overhead vs. amine-sweetened warm gas) and SHALL NOT prescribe a single identity until a human ruling is recorded in Guidance.md.
Source: DBM line 606; line 836; line 1193.

### R-6 Interface requirements matrix (FACT — scope; TBD — content)
The datasheet SHALL include a Package Interface Requirements Matrix covering exactly the interface types declared in PACKAGE_REGISTER.csv row 62 for PKG-052:
Process Piping; Utility Piping; Drain / Containment; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports.
Each row SHALL declare EPC Integrator responsibility, Package Vendor responsibility, tie-in/boundary, and notes; missing tie-in coordinates SHALL be marked `TBD`.

### R-7 Source-grounding and provenance (FACT)
Every non-trivial value or claim in the datasheet SHALL cite either (a) PACKAGE_REGISTER.csv row 62, (b) a specific DBM-Deepcut section, (c) `_CONTEXT.md`, or (d) a labeled `ASSUMPTION` with rationale. Unsupported values SHALL be `TBD`, not invented.

### R-8 Responsibility split (FACT)
The datasheet SHALL clearly assign: Package Vendor — package engineering, package design, vendor documentation, physical equipment package; EPC Integrator — facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration.
Source: PACKAGE_REGISTER.csv row 62 (Responsibility).

### R-9 Stable structure (FACT)
The Datasheet SHALL retain the default sections (Identification, Attributes, Conditions, Construction, References). Additional sections (e.g., Tagged Equipment, Interface Matrix) MAY be added.

### R-10 Coverage of SOW scope items (FACT)
The datasheet SHALL preserve traceability to SOW-0103, SOW-0104, SOW-0105, SOW-0106.
Source: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row 337.

## Standards

| Standard / Code | Applicability | Local accessibility |
|---|---|---|
| TEMA Standards (Heat Exchanger) | Cited indirectly via "TEMA 'R' BEM" classification | Not locally accessible; location TBD |
| ASME BPVC Section VIII Div. 1 | ASSUMPTION: standard for pressure-vessel design at 1,415 psig/66 °C in Canadian/EPC scope | Not locally accessible; location TBD; not cited in available source slices |
| CSA B51 / provincial pressure-equipment code | ASSUMPTION: jurisdictional registration likely required | Not locally accessible; location TBD |
| Project specifications referenced by 26020-Package_Requirements.docx heading 7 | Source-cited but heading not converted to local markdown | location TBD |

Verification of standards SHALL be completed when 26020-Package_Requirements.docx package heading 7 and the RFQ document are converted to locally accessible markdown.

## Verification

| Req ID | Verification approach | Evidence |
|---|---|---|
| R-1 | Inspection of datasheet against `_CONTEXT.md` and PACKAGE_REGISTER row 62 | Datasheet Identification table |
| R-2 | Inspection of Tagged Equipment table | Datasheet Tagged Equipment table |
| R-3 | Inspection of Process Function section | Datasheet Process Function |
| R-4 | Cross-check against DBM-Deepcut §"Inlet / TEG Dehy Cross Exchanger" and PACKAGE_REGISTER row 62 | Datasheet Design Attributes |
| R-5 | Inspection that warm-side identity is not unilaterally fixed; Conflict Table entry exists in Guidance.md | Guidance Conflict Table |
| R-6 | Coverage check: each declared interface type in PACKAGE_REGISTER row 62 appears as a row in the interface matrix | Datasheet Interface Matrix |
| R-7 | Provenance audit: each value cites a source or is labeled TBD/ASSUMPTION | Spot-check |
| R-8 | Inspection of responsibility statements | Datasheet Identification / Construction |
| R-9 | Section-heading audit (Identification, Attributes, Conditions, Construction, References present) | Datasheet headings |
| R-10 | Inspection that SOW-0103..0106 are recoverable from `_CONTEXT.md` linkage | `_CONTEXT.md` Covers Scope Items |

## Documentation

The Package Datasheet artifact set under this deliverable comprises:
- `Datasheet.md` — package technical datasheet (this deliverable's primary artifact)
- `Specification.md` — this normative requirements document
- `Guidance.md` — directional guidance and conflict register
- `Procedure.md` — operational procedure to produce and accept the datasheet

Additional anticipated artifacts per `_CONTEXT.md`:
- Package technical datasheet (Datasheet.md is the canonical EPC handoff form within this repo)
- Vendor engineering handoff basis (Datasheet.md + Specification.md)
- Package interface requirements matrix (Datasheet.md Interface Matrix section)
- Source-supported equipment and design criteria (Datasheet.md Tagged Equipment + Design Attributes)
