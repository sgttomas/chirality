# Specification — DEL-106-01 Scope of Work (PKG-106 Yard Lighting)

## Scope

This Specification establishes the normative content requirements for the EPC Integrator's **Scope of Work** for `PKG-106` Yard Lighting. It defines what the Scope of Work artifact must state regarding package identity, function, source basis, package boundaries, responsibility split, applicable interfaces, and whole-facility integration narrative for yard (exterior/area) lighting.

**Includes:**
- Package identity, workbook row, WBS (TBD), CoA tracking number, discipline (Electrical).
- Package function and equipment list as source-supported (LED yard/area lighting fixtures, poles/masts, control, supply circuits).
- Outdoor/site conditions as source-supported (LED technology, hazardous-area suitability, light-pollution controls, ambient temperature).
- Boundary definition: vendor-owned package vs. EPC-owned integration.
- Applicable interface types at the package boundary (Electrical Power; Grounding / Bonding; Area / Exterior Lighting).
- Source references and traceability to upstream decomposition basis.

**Excludes:**
- Technical datasheet content (covered by `DEL-106-02_package-datasheet`).
- Construction work package content (covered by `DEL-106-03_construction-work-package`).
- Vendor package engineering and design content (covered by `DEL-106-04_vendor-engineered-equipment-package`).
- Vendor document register and turnover (covered by `DEL-106-05_vendor-document-turnover-package`).
- Acceptance/review evidence (covered by `DEL-106-06_epc-vendor-package-review-and-acceptance`).

Source: `DELIVERABLE_REGISTER.csv` (DEL-106-01 through DEL-106-06).

## Requirements

| Req ID | Requirement | Source |
|---|---|---|
| SPEC-106-01-R01 | The Scope of Work SHALL identify the package by `PKG-106`, workbook row 12, WBS TBD, CoA tracking number 26020-01-30-001, discipline Electrical, and package name "Yard Lighting". | `PACKAGE_REGISTER.csv` PKG-106 |
| SPEC-106-01-R02 | The Scope of Work SHALL describe the basic package function: provide exterior/area lighting for the facility yard, integrating LED luminaires, poles/masts, and associated control/supply circuits such that exterior working areas are illuminated to project requirements while regulatory light-pollution controls are observed. | `PACKAGE_REGISTER.csv` PKG-106 Description; `SCOPE_LEDGER.csv` SOW-0011; DBM-Deepcut SEC-12 lines 3027-3035 |
| SPEC-106-01-R03 | The Scope of Work SHALL list the major included equipment categories: LED yard/area luminaires; lighting mast poles (located away from the pad edge where mast poles are required); downcast floodlights; photocell or switch controls; supply branch circuits and panel feeders; grounding and bonding to facility electrical earth grid. Specific fixture catalog, wattages, pole heights, mast counts, and quantities are vendor-design outputs and SHALL be marked `TBD`. | DBM-Deepcut SEC-12 lines 3029, 3031, 3035; `PACKAGE_REGISTER.csv` PKG-106 |
| SPEC-106-01-R04 | The Scope of Work SHALL document the conditions governing design: LED luminaire technology; suitability for the area classification in which fixtures are installed; downward illumination (downcast floodlights); prohibition of horizontally aimed floodlights; selective minimization of exterior lighting to working areas; photocell or switch control; mast pole placement away from pad edge; ambient temperature range governed by facility basis (-40 deg C minimum). Specific illuminance (lux) targets, photometric calculation basis, pole heights, and mast counts SHALL be marked `TBD` with `location TBD`. | DBM-Deepcut SEC-12 lines 3029-3035; DBM-Comp_and_Liquids SEC-04 line 145 |
| SPEC-106-01-R05 | The Scope of Work SHALL assign package engineering, package design, vendor documentation, and the physical equipment package to the Package Vendor, and integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration) to the EPC Integrator. | `PACKAGE_REGISTER.csv` ResponsibilityModel |
| SPEC-106-01-R06 | The Scope of Work SHALL declare the applicable package-boundary interface types for PKG-106: Electrical Power; Grounding / Bonding; Area / Exterior Lighting (3 interface types). | `INTERFACE_REGISTER.csv` PKG-106 rows (`IFC-6FCF1B30D6`, `IFC-DA0D60681B`, `IFC-ED86F51087`); `PACKAGE_REGISTER.csv` InterfaceTypes |
| SPEC-106-01-R07 | The Scope of Work SHALL cite source basis: Workbook Packages row 12; `DBM-Deepcut/4-25_Deepcut_DBM.md` (SEC-12 Lighting and Receptacles); `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (SEC-12 Electrical Buildings, Raceways, Lighting, and Heat Tracing). ASSUMPTION: `26020-Package_Requirements.docx` and `26020-Packages_Interfaces_4_export.xlsx` row 12 contain additional vendor-document/interface detail; `location TBD` until extracted. | `PACKAGE_REGISTER.csv` SourceRefRaw; `_REFERENCES.md` |
| SPEC-106-01-R08 | The Scope of Work SHALL state the supported objectives `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-009`, `OBJ-010`. | `OBJECTIVE_DELIVERABLE_MAP.csv`; `DELIVERABLE_REGISTER.csv` |
| SPEC-106-01-R09 | The Scope of Work SHALL identify the scope items it covers: `SOW-0011`. | `SCOPE_LEDGER.csv` |
| SPEC-106-01-R10 | The Scope of Work SHALL produce the anticipated artifacts: package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record. | `DELIVERABLE_REGISTER.csv`; `ARTIFACT_REGISTER.csv` (ART-1D00D7FAE6, ART-508A45C565, ART-C1764AFD92, ART-27C44AFC19) |
| SPEC-106-01-R11 | The Scope of Work SHALL mark unresolved/unsourced design values (fixture catalog, wattages, lux levels, pole heights, mast counts, photometric calculations, specific fixture/lighting standards beyond CEC) as `TBD` with `location TBD` where the source clause is not locally accessible. | `_REFERENCES.md`; SKILL `four-documents` source-grounding rule |
| SPEC-106-01-R12 | The Scope of Work SHALL explicitly surface the conflict between the workbook framing (vendor-owned package) and DBM-Deepcut SEC-04 (Area lighting listed within Tourmaline field construction scope) as an open item requiring human ruling; the SOW SHALL NOT silently reconcile this conflict. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 120; `PACKAGE_REGISTER.csv` PKG-106 |

## Standards

| Standard / Code | Applicability | Location |
|---|---|---|
| Canadian Electrical Code (CEC) | Applicable to all electrical installation (wiring methods, conduit sealing, area classification, GFI protection). | DBM-Deepcut SEC-12 line 3025; **location TBD** for specific CEC editions/clauses |
| Electrical safety, grounding/bonding, lighting fixture standards (CSA C22.2 fixture-family standards; IEEE 1100 grounding practice; IES RP- area/roadway lighting practice) | ASSUMPTION: applicable to yard-lighting design per industry practice; specific edition and clause TBD. | location TBD |
| Light-pollution / dark-sky regulatory requirements | Applicable per DBM-Deepcut SEC-12 line 3035 ("Regulatory light-pollution requirements shall be addressed by LED lighting…"). Specific regulatory citation (BCER condition, municipal bylaw, IDA guideline) TBD. | location TBD — DBM-Deepcut SEC-12 line 3035 |
| Hazardous-area classification standards (CSA C22.1 Section 18, IEC 60079 series) | Applicable where yard-lighting fixtures are installed within classified areas, per DBM-Deepcut SEC-12 line 3029 ("suitable for the area classification"). Specific area-classification drawings TBD. | location TBD |
| Sour-service safety / regulatory / codes carried by `OBJ-009` | ASSUMPTION: applicable to the extent that yard-lighting fixtures, controls, and emergency-lighting interact with fire/gas and emergency-egress requirements. | location TBD |

## Verification

| Req | Verification approach |
|---|---|
| R01 | Inspection: Scope of Work header contains every identity field, cross-checked against `PACKAGE_REGISTER.csv` PKG-106 (WBS marked TBD). |
| R02 | Inspection: package-function statement is textually consistent with the workbook description and DBM-Deepcut SEC-12 lighting narrative. |
| R03 | Inspection: major-equipment-category list reproduces LED fixtures, mast poles, downcast floodlights, photocell/switch controls, and supply circuits; vendor-design quantities marked `TBD`. |
| R04 | Inspection: conditions (LED; hazardous-area suitability; downward illumination; no horizontal floodlights; mast placement; -40 deg C ambient) appear verbatim or as exact paraphrase; lux/pole/photometric values marked `TBD`. |
| R05 | Inspection + traceability: responsibility text preserves the Package Vendor / EPC Integrator split per `PACKAGE_REGISTER.csv` ResponsibilityModel. |
| R06 | Cross-check: declared interface types equal the 3-element set in `INTERFACE_REGISTER.csv` for `PKG-106` (Electrical Power; Grounding / Bonding; Area / Exterior Lighting). |
| R07 | Inspection: source-references section cites Workbook row 12, DBM-Deepcut SEC-12, and DBM-Comp_and_Liquids SEC-12; package requirements doc and interface xlsx labeled `location TBD`. |
| R08 | Inspection: objective list equals `{OBJ-001, OBJ-004, OBJ-005, OBJ-009, OBJ-010}`. |
| R09 | Inspection: scope-item list equals `{SOW-0011}`. |
| R10 | Artifact inventory: each anticipated artifact has at least one section or attachment satisfying it. |
| R11 | QA review: every numeric/material value either has a cited source slice or is marked `TBD` with `location TBD`. |
| R12 | Inspection: Conflict Table entry CONF-106-01-01 (vendor-owned package vs. field construction scope) is present and unresolved. |

## Documentation

The deliverable SHALL produce, at minimum:

- Package scope of work narrative (covers R01–R09, R12).
- Tagged equipment and package identity list (R01, R03).
- Package function and whole-facility integration narrative (R02, R04, R06).
- Responsibility assignment record (R05).
- Source basis listing and TBD register (R07, R11).

Source: `ARTIFACT_REGISTER.csv` (ART-1D00D7FAE6, ART-508A45C565, ART-C1764AFD92, ART-27C44AFC19).
