# Specification — DEL-100-01 Scope of Work (PKG-100 Hydrogen Peroxide Sweetening Unit)

## Scope

This Specification establishes the normative content requirements for the EPC Integrator's **Scope of Work** for `PKG-100` Hydrogen Peroxide Sweetening Unit. It defines what the Scope of Work artifact must state regarding the package's tagged equipment, package function, source basis, package boundaries, responsibility split, applicable interfaces, and whole-facility integration narrative.

**Includes:**
- Package identity, workbook row, WBS, CoA tracking number, discipline (Mechanical).
- Package function and major equipment list as source-supported.
- Operating and ambient conditions as source-supported.
- Boundary definition: vendor-owned package vs. EPC-owned integration.
- Applicable interface types at the package boundary.
- Source references and traceability to upstream decomposition basis.

**Excludes:**
- Technical datasheet content (covered by `DEL-100-02_package-datasheet`).
- Construction work package content (covered by `DEL-100-03_construction-work-package`).
- Vendor package engineering and design content (covered by `DEL-100-04_vendor-engineered-equipment-package`).
- Vendor document register and turnover (covered by `DEL-100-05_vendor-document-turnover-package`).
- Acceptance/review evidence (covered by `DEL-100-06_epc-vendor-package-review-and-acceptance`).

Source: `DELIVERABLE_REGISTER.csv` (DEL-100-01 through DEL-100-06).

## Requirements

| Req ID | Requirement | Source |
|---|---|---|
| SPEC-100-01-R01 | The Scope of Work SHALL identify the package by `PKG-100`, workbook row 63, WBS 03, CoA tracking number 26020-03-27-001 (also reported as 26020-03-PT-27-001), discipline Mechanical, and package name "Hydrogen Peroxide Sweetening Unit". | `PACKAGE_REGISTER.csv` PKG-100 |
| SPEC-100-01-R02 | The Scope of Work SHALL describe the basic package function: supply one sour-water hydrogen peroxide treatment package consisting of Hydrogen Peroxide Pumps (chemical injection pumps), Hydrogen Peroxide Reactors, and a Static Mixer; sour water passes through the static mixer to the reactors, with H₂O₂ pumped from the hydrogen peroxide tank, and treated water routed to produced water storage tanks. | `SCOPE_LEDGER.csv` SOW-0108 |
| SPEC-100-01-R03 | The Scope of Work SHALL list the major included equipment: 400 BBL Hydrogen Peroxide Storage Tank; Hydrogen Peroxide Pumps (Vendor to design); Static Mixer (Vendor to design); Hydrogen Peroxide Reactors (Vendor to design); additional equipment per PFD; self-framing building to be erected at site. | `SCOPE_LEDGER.csv` SOW-0109 |
| SPEC-100-01-R04 | The Scope of Work SHALL document the scope notes / open items: capacity 24,154 BBL/D; tank 400 BBL; pump capacity TBC; drivers 575 V/3PH/60Hz motors with DOL or VFD starting, local H-O-A/On-Off control, fed from a 600 V MCC; sour-water T=9 °C, P=340.54 kPag, Q=160 m³/h; ambient −40 to +35 °C; H₂O₂ supplied from onsite tanks; "by others" list: interconnecting piping, DCS integration, foundations, electrical supply to MCC. | `SCOPE_LEDGER.csv` SOW-0110 |
| SPEC-100-01-R05 | The Scope of Work SHALL assign package engineering, package design, vendor documentation, and the physical equipment package to the Package Vendor, and integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration) to the EPC Integrator. | `PACKAGE_REGISTER.csv` ResponsibilityModel |
| SPEC-100-01-R06 | The Scope of Work SHALL declare the applicable package-boundary interface types: Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports (13 interface types). | `INTERFACE_REGISTER.csv` PKG-100 rows; `PACKAGE_REGISTER.csv` InterfaceTypes |
| SPEC-100-01-R07 | The Scope of Work SHALL cite source basis: Workbook Packages row 63; `26020-Package_Requirements.docx` package heading 52; `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`. ASSUMPTION: budgetary go-by `Bid Docs/Budgetary/26020-03-PT-RFQ-27-001-H202_Sweet_Unit.docx` is informational only and SHALL be labeled as such. | `PACKAGE_REGISTER.csv` SourceRefRaw |
| SPEC-100-01-R08 | The Scope of Work SHALL state the supported objectives `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010`. | `OBJECTIVE_DELIVERABLE_MAP.csv`; `DELIVERABLE_REGISTER.csv` |
| SPEC-100-01-R09 | The Scope of Work SHALL identify the scope items it covers: `SOW-0107`, `SOW-0108`, `SOW-0109`, `SOW-0110`. | `SCOPE_LEDGER.csv` |
| SPEC-100-01-R10 | The Scope of Work SHALL produce the anticipated artifacts: package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record. | `DELIVERABLE_REGISTER.csv`; `ARTIFACT_REGISTER.csv` (ART-CF28BC5992, ART-DEB15FAA69, ART-2ED2F833EB, ART-5BA6AFE0FD, ART-B77E9A5546) |
| SPEC-100-01-R11 | The Scope of Work SHALL mark unresolved/unsourced design values (final design pressures, design temperatures beyond ambient, pump capacity, materials of construction, reactor sizing, code citations) as `TBD` with `location TBD` where the source clause is not locally accessible. | `_REFERENCES.md`; SKILL `four-documents` source-grounding rule |

## Standards

| Standard / Code | Applicability | Location |
|---|---|---|
| Sour-service / safety / relief / fire-gas / shutdown / environmental / regulatory codes | ASSUMPTION: applicable to this sour-water treatment package via `OBJ-009`. Specific code citations (e.g., API/ASME pressure vessel, NFPA, AER/regulatory, ANSI/ISA for instrumentation) are not enumerated in locally accessible source slices. | location TBD — `26020-Package_Requirements.docx` package heading 52; `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| Hydrogen peroxide handling / chemical injection safety | ASSUMPTION: applicable due to the use of bulk H₂O₂ and chemical injection equipment (industry practice covers H₂O₂ compatibility, materials, separation, ventilation). Specific standards TBD; reference DBM and vendor specifications. | location TBD |
| Electrical equipment standards (motors, MCC, VFD starting, area classification) | Applicable per SOW-0110 (575 V/3PH/60Hz motors; 600 V MCC; DOL/VFD starting). Specific standards (CSA/CEC for AB jurisdiction implied) TBD. | location TBD — `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| Process Piping / Utility Piping / Relief-Flare-Vent / Drain-Containment design standards | Applicable per `INTERFACE_REGISTER.csv` PKG-100 rows. Specific standards TBD. | location TBD |
| Building / HVAC / Fire & Gas standards (self-framing building at site) | Applicable per SOW-0109 (self-framing building) and PKG-100 interface set (Building HVAC / Services; Fire & Gas / Safety Systems). Specific standards TBD. | location TBD |

## Verification

| Req | Verification approach |
|---|---|
| R01 | Inspection: Scope of Work header contains every identity field, cross-checked against `PACKAGE_REGISTER.csv` PKG-100. |
| R02 | Inspection: package-function statement is textually consistent with SOW-0108 (static mixer, reactors, peroxide pumps, treated water to produced water storage). |
| R03 | Inspection: major-equipment list reproduces SOW-0109 items, including the 400 BBL H₂O₂ storage tank and the self-framing site building. |
| R04 | Inspection: operating-condition values (24,154 BBL/D; 9 °C; 340.54 kPag; 160 m³/h; ambient −40/+35 °C; 575 V/3PH/60Hz; 600 V MCC) appear verbatim or as exact unit-converted equivalents. |
| R05 | Inspection + traceability: responsibility text preserves the Package Vendor / EPC Integrator split per `PACKAGE_REGISTER.csv` ResponsibilityModel. |
| R06 | Cross-check: declared interface types equal the 13-element set in `INTERFACE_REGISTER.csv` for `PKG-100`. |
| R07 | Inspection: source references section cites Workbook row 63, package requirements doc heading 52, and the 3-25 Comp_and_Liquids DBM; budgetary go-by labeled informational. |
| R08 | Inspection: objective list equals `{OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010}`. |
| R09 | Inspection: scope-item list equals `{SOW-0107, SOW-0108, SOW-0109, SOW-0110}`. |
| R10 | Artifact inventory: each anticipated artifact has at least one section or attachment satisfying it. |
| R11 | QA review: every numeric/material value either has a cited source slice or is marked `TBD` with `location TBD`. |

## Documentation

The deliverable SHALL produce, at minimum:

- Package scope of work narrative (covers R01–R09).
- Tagged equipment and package identity list (R01, R03).
- Package function and whole-facility integration narrative (R02, R04, R06).
- Responsibility assignment record (R05).
- Detailed mechanical package scope extraction evidence / source basis listing (R07, R11).

Source: `ARTIFACT_REGISTER.csv` (ART-CF28BC5992, ART-DEB15FAA69, ART-2ED2F833EB, ART-5BA6AFE0FD, ART-B77E9A5546).
