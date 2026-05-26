# Specification — DEL-095-01 Scope of Work (PKG-095 Tanks, Slop (API 650))

## Scope

This Specification establishes the normative content requirements for the EPC Integrator's **Scope of Work** for `PKG-095` Tanks, Slop (API 650). It defines what the Scope of Work artifact must state regarding the package's tagged equipment, package function, source basis, package boundaries, responsibility split, and whole-facility integration narrative.

**Includes:**
- Package identity, workbook row, WBS, CoA tracking number, discipline (Mechanical).
- Package function and major equipment list as source-supported.
- Boundary definition: vendor-owned package vs. EPC-owned integration.
- Applicable interface types at the package boundary.
- Source references and traceability to upstream decomposition basis.

**Excludes:**
- Vendor package engineering and design content (covered by `DEL-095-04_vendor-engineered-equipment-package`).
- Technical datasheet content (covered by `DEL-095-02_package-datasheet`).
- Construction work package content (covered by `DEL-095-03_construction-work-package`).
- Vendor document register and turnover (covered by `DEL-095-05_vendor-document-turnover-package`).
- Acceptance / review evidence (covered by `DEL-095-06_epc-vendor-package-review-and-acceptance`).

Source: `DELIVERABLE_REGISTER.csv` (DEL-095-01 through DEL-095-06).

## Requirements

| Req ID | Requirement | Source |
|---|---|---|
| SPEC-095-01-R01 | The Scope of Work SHALL identify the package by `PKG-095`, workbook row 91, WBS 03, CoA tracking number 26020-03-19-004, discipline Mechanical, and package name "Tanks, Slop (API 650)". | `PACKAGE_REGISTER.csv` PKG-095 |
| SPEC-095-01-R02 | The Scope of Work SHALL describe the package's basic function as: supply one slop storage tank for off-spec condensate or contaminated hydrocarbon liquids requiring segregation from on-spec condensate product. | `SCOPE_LEDGER.csv` SOW-0214 |
| SPEC-095-01-R03 | The Scope of Work SHALL list the major included equipment: one API 650 modified atmospheric slop storage tank (preliminary tag `TK-9130-2`, ASSUMPTION); tank appurtenances; connections to relevant drain/recycle/truck-out systems; standard tank instrumentation. | `SCOPE_LEDGER.csv` SOW-0215 |
| SPEC-095-01-R04 | The Scope of Work SHALL document the integration scope notes from SOW-0216: definition of slop as off-spec condensate or contaminated hydrocarbon liquid; expected slop sources (off-spec condensate, tank drains, KO drum pump-out, VRU/scrubber liquids, treating-unit drains, other contaminated hydrocarbon liquids); and the open requirement for process confirmation of final source list, disposition path, and tank design basis. | `SCOPE_LEDGER.csv` SOW-0216 |
| SPEC-095-01-R05 | The Scope of Work SHALL assign package engineering, package design, vendor documentation, and the physical equipment package to the Package Vendor, and integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration) to the EPC Integrator. | `PACKAGE_REGISTER.csv` ResponsibilityModel |
| SPEC-095-01-R06 | The Scope of Work SHALL declare the applicable package-boundary interface types: Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. | `INTERFACE_REGISTER.csv` PKG-095 rows; `PACKAGE_REGISTER.csv` InterfaceTypes |
| SPEC-095-01-R07 | The Scope of Work SHALL cite source basis: Workbook Packages row 91; `26020-Package_Requirements.docx` package heading 47; the 3-25 Comp_and_Liquids DBM (`DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`). The SOW SHALL note that no package-folder brief.md, DOCX, or PDF scope source was found per `PACKAGE_REGISTER.csv`. | `PACKAGE_REGISTER.csv` SourceRefRaw |
| SPEC-095-01-R08 | The Scope of Work SHALL state the supported objectives `OBJ-002`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010`. | `OBJECTIVE_DELIVERABLE_MAP.csv`; `DELIVERABLE_REGISTER.csv` |
| SPEC-095-01-R09 | The Scope of Work SHALL identify the scope items it covers: `SOW-0213`, `SOW-0214`, `SOW-0215`, `SOW-0216`. | `SCOPE_LEDGER.csv` |
| SPEC-095-01-R10 | The Scope of Work SHALL produce the anticipated artifacts: package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record. | `DELIVERABLE_REGISTER.csv`; `ARTIFACT_REGISTER.csv` (ART-ECAD436B0E, ART-8EAFCB6105, ART-4DA4B85839, ART-10E6586D28, ART-C6A071D655) |
| SPEC-095-01-R11 | The Scope of Work SHALL mark unresolved/unsourced design values (tank capacity, dimensions, design pressure/temperature, materials, API 650 modification scope, instrument list) as `TBD` with `location TBD` where the source clause is not locally accessible. | `_REFERENCES.md`; SKILL four-documents source-grounding rule |
| SPEC-095-01-R12 | The Scope of Work SHALL flag the preliminary equipment tag `TK-9130-2` as ASSUMPTION pending vendor/process confirmation (source qualifies it as "likely"). | `SCOPE_LEDGER.csv` SOW-0215 |

## Standards

| Standard / Code | Applicability | Location |
|---|---|---|
| API 650 (modified) — Welded Tanks for Oil Storage | Applicable per package name "Tanks, Slop (API 650)" and SOW-0215 ("API 650 modified atmospheric slop storage tank"). Specific appendix selections (e.g., Appendix A small tanks, Appendix M elevated-temperature, Appendix S stainless) and "modified" basis TBD. | location TBD — `26020-Package_Requirements.docx` package heading 47 detail text |
| Sour-service / safety / relief / vent / drain-containment / fire-gas / shutdown / environmental / regulatory codes | ASSUMPTION: applicable to this slop tank package via `OBJ-009`. Specific code citations (e.g., API 2000 venting, NFPA 30 flammable/combustible liquids, AER/regulatory) are not enumerated in locally accessible source slices. | location TBD |
| Cathodic Protection standards | Applicable per `INTERFACE_REGISTER.csv` (Cathodic Protection interface declared). Specific standards (e.g., NACE SP0169, API 651) TBD. | location TBD |
| Grading / Site Drainage / Spill Containment standards | Applicable per `INTERFACE_REGISTER.csv`. Specific standards (e.g., SPCC, regional spill containment volume rules) TBD. | location TBD |

## Verification

| Req | Verification approach |
|---|---|
| R01 | Inspection: Scope of Work header contains every identity field, cross-checked against `PACKAGE_REGISTER.csv` PKG-095 row. |
| R02 | Inspection: package-function statement is textually consistent with SOW-0214. |
| R03 | Inspection: tagged-equipment list matches SOW-0215 (tank, appurtenances, drain/recycle/truck-out connections, standard instrumentation); tag `TK-9130-2` labeled ASSUMPTION. |
| R04 | Inspection: integration narrative reproduces SOW-0216 slop definition, expected sources, and process-confirmation open items. |
| R05 | Inspection + traceability: responsibility statements map to `PACKAGE_REGISTER.csv` ResponsibilityModel preserving the vendor/EPC split. |
| R06 | Cross-check: declared interface types equal the set in `INTERFACE_REGISTER.csv` for `PKG-095` (nine interfaces). |
| R07 | Inspection: source references section cites Workbook row 91, package requirements doc heading 47, and the 3-25 Comp_and_Liquids DBM; missing brief.md/DOCX/PDF noted. |
| R08 | Inspection: objective list equals `{OBJ-002, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010}`. |
| R09 | Inspection: scope-item list equals `{SOW-0213, SOW-0214, SOW-0215, SOW-0216}`. |
| R10 | Artifact inventory: each of the five anticipated artifacts (ART-ECAD436B0E, ART-8EAFCB6105, ART-4DA4B85839, ART-10E6586D28, ART-C6A071D655) has at least one section satisfying it. |
| R11 | QA review: every numeric/material value either has a cited source slice or is marked `TBD` with `location TBD`. |
| R12 | Inspection: equipment tag `TK-9130-2` is labeled ASSUMPTION in Datasheet and Scope-of-Work narrative. |

## Documentation

The deliverable SHALL produce, at minimum:

- Package scope of work narrative (covers R01–R09).
- Tagged equipment and package identity list (R01, R03).
- Package function and whole-facility integration narrative (R02, R04, R06).
- Responsibility assignment record (R05).
- Source basis / detailed mechanical scope extraction evidence (R07, R11).

Source: `ARTIFACT_REGISTER.csv` (ART-ECAD436B0E, ART-8EAFCB6105, ART-4DA4B85839, ART-10E6586D28, ART-C6A071D655).
