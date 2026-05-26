# Specification — DEL-063-01 Scope of Work (PKG-063 Tanks, DSO (API 650))

## Scope

This Specification establishes the normative content requirements for the EPC Integrator's **Scope of Work** for `PKG-063` Tanks, DSO (API 650). It defines what the Scope of Work artifact MUST state regarding the package's tagged equipment, package function, source basis, package boundaries, responsibility split, and whole-facility integration narrative for the 400 bbl atmospheric disulphide oil storage tank within the West Doe Deepcut (04-25) NGL caustic treating / DSO disposition system.

**Includes:**
- Package identity, workbook row, WBS, CoA tracking number, discipline (Mechanical).
- Package function (DSO storage from the DSO separator within the caustic regeneration system).
- Major equipment description (modified API 650 atmospheric tank, 400 bbl, internal coating, heater, insulation) as source-supported.
- Boundary definition: vendor-owned package vs. EPC-owned integration; explicit by-others carve-out (foundations, site mounting, E&I, platforms, staircase).
- Applicable interface types at the package boundary.
- Source references and traceability to the upstream decomposition basis and the 04-25 DBM disulphide-oil disposition context.

**Excludes:**
- Vendor package engineering and design content (covered by `DEL-063-04_vendor-engineered-equipment-package`).
- Technical datasheet content for handoff to the package vendor (covered by `DEL-063-02_package-datasheet`).
- Construction work package content for installation, tie-in, and turnover (covered by `DEL-063-03_construction-work-package`).
- Vendor document register and turnover (covered by `DEL-063-05_vendor-document-turnover-package`).
- EPC vendor-package review and acceptance evidence (covered by `DEL-063-06_epc-vendor-package-review-and-acceptance`).

Source: `DELIVERABLE_REGISTER.csv` (DEL-063-01 through DEL-063-06).

## Requirements

| Req ID | Requirement | Source |
|---|---|---|
| SPEC-063-01-R01 | The Scope of Work SHALL identify the package by `PKG-063`, workbook row 90, WBS 01, CoA tracking number 26020-01-19-001, discipline Mechanical, and package name "Tanks, DSO (API 650)". | `PACKAGE_REGISTER.csv` PKG-063 |
| SPEC-063-01-R02 | The Scope of Work SHALL describe the package's basic function: supply one (1) atmospheric DSO storage tank that receives separated DSO from the DSO separator (level-controlled) within the caustic regeneration system. | `SCOPE_LEDGER.csv` SOW-0210 |
| SPEC-063-01-R03 | The Scope of Work SHALL describe the major included equipment: DSO Storage Tank — modified API 650; 400 bbl nominal; atmospheric (design pressure 32 oz, 1.0 oz vacuum); vendor-designed heater sized for 32.2 °C (90 °F) minimum; internally coated (floor, walls, roof); insulated to maintain DSO above pour point for truck-out and handling (minimum temperature TBD). | `SCOPE_LEDGER.csv` SOW-0211 |
| SPEC-063-01-R04 | The Scope of Work SHALL document the by-others / boundary carve-out: foundations, on-site mounting, electrical/instrumentation, platforms, and staircase are by others (EPC Integrator / facility scope), not the Package Vendor. | `SCOPE_LEDGER.csv` SOW-0212 |
| SPEC-063-01-R05 | The Scope of Work SHALL assign package engineering, package design, vendor documentation, and the physical equipment package to the Package Vendor, and integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration) to the EPC Integrator. | `PACKAGE_REGISTER.csv` PKG-063 ResponsibilityModel |
| SPEC-063-01-R06 | The Scope of Work SHALL declare the applicable package-boundary interface types: Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. | `INTERFACE_REGISTER.csv` PKG-063 (nine rows); `PACKAGE_REGISTER.csv` InterfaceTypes |
| SPEC-063-01-R07 | The Scope of Work SHALL place the package in process context: DSO is a by-product of the NGL non-regenerative caustic treating process; the tank stores recovered DSO for truck-out and disposal; alternate mixing into C5+ product is identified as an open detailed-engineering review item, not a current-scope disposal path. | `DBM-Deepcut/4-25_Deepcut_DBM.md` (Disulphide oil disposition paragraph; DSO disposal open issue) |
| SPEC-063-01-R08 | The Scope of Work SHALL cite source basis: Workbook Packages row 90; `26020-Package_Requirements.docx` package heading 18; `DBM-Deepcut/4-25_Deepcut_DBM.md`. ASSUMPTION: budgetary go-by `Bid Docs/_Budgetary/26020-01-PT-RFQ-19-001_Tanks_DSO_R0.docx` is informational only and SHALL be labeled as such. | `PACKAGE_REGISTER.csv` SourceRefRaw |
| SPEC-063-01-R09 | The Scope of Work SHALL state the supported objectives `OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010`. | `OBJECTIVE_DELIVERABLE_MAP.csv`; `DELIVERABLE_REGISTER.csv` |
| SPEC-063-01-R10 | The Scope of Work SHALL identify the scope items it covers: `SOW-0209`, `SOW-0210`, `SOW-0211`, `SOW-0212`. | `SCOPE_LEDGER.csv` |
| SPEC-063-01-R11 | The Scope of Work SHALL produce the anticipated artifacts: package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record; detailed mechanical package scope extraction evidence. | `DELIVERABLE_REGISTER.csv`; `ARTIFACT_REGISTER.csv` (ART-8D38072F13, ART-469823FD54, ART-B502E838FB, ART-42CDF63E00, ART-A0E63EAD7C) |
| SPEC-063-01-R12 | The Scope of Work SHALL mark unresolved or unsourced design values (minimum pour-point temperature, capacity/throughput, operating conditions, materials/coating product, maximum fill, equipment tag number, alternate disposal-path commitment) as `TBD` with `location TBD` where the source clause is not locally accessible. | `_REFERENCES.md`; SKILL `four-documents` source-grounding rule |
| SPEC-063-01-R13 | The Scope of Work SHALL identify the DSO storage tank by an `Item No.` placeholder consistent with the 04-25 facility tagging convention; the explicit tag is TBD (the source slice in `26020-Package_Requirements.docx` heading 18 lists the equipment as "Item No. DSO Storage Tank:" with the tag itself not enumerated in the locally accessible slice). | `SCOPE_LEDGER.csv` SOW-0211; location TBD for tag number |

## Standards

| Standard / Code | Applicability | Location |
|---|---|---|
| API 650 (modified) | Tank design and fabrication standard explicitly cited by source for the DSO storage tank ("Design & fabrication to modified API 650"). The nature and extent of the modification is not stated in the locally accessible source slice. | `SCOPE_LEDGER.csv` SOW-0211; modification scope: location TBD |
| Sour-service / safety / relief / flare / blowdown / drain-containment / fire-gas / shutdown / environmental / regulatory codes | ASSUMPTION: applicable via `OBJ-009`. Specific code citations (e.g., API 620, API 2510, NFPA 30, AER OGAOM, ASME, CSA) are not enumerated in the locally accessible PKG-063 source slice. The 04-25 DBM Site/Spacing table cites API 2510, NFPA 30, and OGAOM Sec. 9.6.15 for atmospheric tank spacing, which apply to siting/integration. | location TBD — `26020-Package_Requirements.docx` package heading 18 and `DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-09, SEC-14, SEC-15 |
| Internal coating / lining standards (DSO service) | Internal coating is required (floor, walls, roof) per SOW-0211; coating system specification and standard are not stated in the locally accessible source slice. | location TBD |
| Insulation and heat-tracing standards | Insulation required for pour-point maintenance per SOW-0211; heater is vendor-designed at 32.2 °C (90 °F) minimum. Whether heating uses internal coil, external EHT, or both — not stated. | location TBD |
| Grounding / bonding, cathodic protection, area lighting, I&C / control cabling, grading / site drainage / spill containment, structural foundations standards | Applicable per `INTERFACE_REGISTER.csv` PKG-063 rows. Specific standards TBD. | location TBD |

## Verification

| Req | Verification approach |
|---|---|
| R01 | Inspection: Scope of Work header contains every identity field, cross-checked against `PACKAGE_REGISTER.csv` PKG-063. |
| R02 | Inspection: package-function statement is textually consistent with SOW-0210 (DSO storage from DSO separator under level control in caustic regeneration system). |
| R03 | Inspection: major-equipment paragraph reproduces SOW-0211 (modified API 650, 400 bbl, atmospheric, 32 oz / 1.0 oz vacuum, heater at 32.2 °C / 90 °F minimum, internal coating, insulation). |
| R04 | Inspection: by-others list explicitly names foundations, mounting, E&I, platforms, and staircase per SOW-0212. |
| R05 | Inspection + traceability: responsibility statements map verbatim or as faithful paraphrase to `PACKAGE_REGISTER.csv` ResponsibilityModel preserving vendor/EPC split. |
| R06 | Cross-check: declared interface types equal the nine-row set in `INTERFACE_REGISTER.csv` for `PKG-063`. |
| R07 | Inspection: process-integration narrative cites the 04-25 DBM disulphide-oil paragraph and flags DSO-disposal as an open item. |
| R08 | Inspection: source-basis section cites Workbook row 90, package requirements doc heading 18, and the 04-25 DBM; budgetary RFQ go-by labeled informational. |
| R09 | Inspection: objective list equals `{OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010}`. |
| R10 | Inspection: scope-item list equals `{SOW-0209, SOW-0210, SOW-0211, SOW-0212}`. |
| R11 | Artifact inventory: each ART-* row above has at least one corresponding section or sub-artifact within the deliverable. |
| R12 | QA review: every numeric/material value either has a cited source slice or is marked `TBD` with `location TBD`. |
| R13 | Inspection: equipment tag carrier present with explicit `TBD` for the tag number and pointer to the source heading where the tag should reside. |

## Documentation

The deliverable SHALL produce, at minimum:

- Package scope of work narrative (covers R01–R10).
- Tagged equipment and package identity list (R01, R03, R13).
- Package function and whole-facility integration narrative (R02, R06, R07).
- Responsibility assignment record (R04, R05).
- Detailed mechanical package scope extraction evidence (R08, R12).

Source: `ARTIFACT_REGISTER.csv` (ART-8D38072F13, ART-469823FD54, ART-B502E838FB, ART-42CDF63E00, ART-A0E63EAD7C).
