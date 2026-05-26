# Specification — DEL-054-01 Scope of Work (PKG-054 Flare KO Drum (High Pressure) 4-25)

## Scope

This Specification establishes the normative content requirements for the EPC Integrator's **Scope of Work** for `PKG-054` Flare KO Drum (High Pressure) 4-25. It defines what the Scope of Work artifact must state regarding the package's tagged equipment, package function, source basis, package boundaries, responsibility split, and whole-facility integration narrative.

**Includes:**
- Package identity, workbook row, WBS, CoA tracking number, discipline (Mechanical).
- Package function and major equipment list as source-supported.
- Boundary definition: vendor-owned package vs. EPC-owned integration.
- Applicable interface types at the package boundary.
- Source references and traceability to upstream decomposition basis.

**Excludes:**
- Vendor package engineering and design content (covered by `DEL-054-04_vendor-engineered-equipment-package`).
- Technical datasheet content (covered by `DEL-054-02_package-datasheet`).
- Construction work package content (covered by `DEL-054-03_construction-work-package`).
- Vendor document register and turnover (covered by `DEL-054-05_vendor-document-turnover-package`).
- Acceptance/review evidence (covered by `DEL-054-06_epc-vendor-package-review-and-acceptance`).

Source: `DELIVERABLE_REGISTER.csv` (DEL-054-01 through DEL-054-06).

## Requirements

| Req ID | Requirement | Source |
|---|---|---|
| SPEC-054-01-R01 | The Scope of Work SHALL identify the package by `PKG-054`, workbook row 55, WBS 01, CoA tracking number 26020-01-17-002, discipline Mechanical, and package name "Flare KO Drum (High Pressure) 4-25". | `PACKAGE_REGISTER.csv` PKG-054 |
| SPEC-054-01-R02 | The Scope of Work SHALL describe the package's basic function as: supply one HP flare knock-out drum and one HP flare KO drum transfer pump. | `SCOPE_LEDGER.csv` SOW-0076 |
| SPEC-054-01-R03 | The Scope of Work SHALL list the major included equipment: HP flare KO drum `V-4100-1`; transfer pump `P-4100-1`; liquid handling to condensate slop tank; truck-out provision; related package connections. | `SCOPE_LEDGER.csv` SOW-0077 |
| SPEC-054-01-R04 | The Scope of Work SHALL document the integration scope note that the HP flare header ties into the cryogenic flare header downstream of the drum before the common HP/Cryo flare stack, and that outdoor HP flare headers are electrically heat traced and insulated. | `SCOPE_LEDGER.csv` SOW-0078 |
| SPEC-054-01-R05 | The Scope of Work SHALL assign package engineering, package design, vendor documentation, and the physical equipment package to the Package Vendor, and integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration) to the EPC Integrator. | `PACKAGE_REGISTER.csv` ResponsibilityModel |
| SPEC-054-01-R06 | The Scope of Work SHALL declare the applicable package-boundary interface types: Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports. | `INTERFACE_REGISTER.csv` PKG-054 rows; `PACKAGE_REGISTER.csv` InterfaceTypes |
| SPEC-054-01-R07 | The Scope of Work SHALL cite source basis: Workbook Packages row 55; `26020-Package_Requirements.docx` package heading 9; the 04-25 Deepcut DBM. ASSUMPTION: budgetary go-by `24292-02-PT-ENR-17-201_HP FKOD_R2.pdf` is informational only and SHALL be labeled as such. | `PACKAGE_REGISTER.csv` SourceRefRaw |
| SPEC-054-01-R08 | The Scope of Work SHALL state the supported objectives `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010`. | `OBJECTIVE_DELIVERABLE_MAP.csv`; `DELIVERABLE_REGISTER.csv` |
| SPEC-054-01-R09 | The Scope of Work SHALL identify the scope items it covers: `SOW-0075`, `SOW-0076`, `SOW-0077`, `SOW-0078`. | `SCOPE_LEDGER.csv` |
| SPEC-054-01-R10 | The Scope of Work SHALL produce the anticipated artifacts: package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record. | `DELIVERABLE_REGISTER.csv`; `ARTIFACT_REGISTER.csv` (ART-65A805B4B4, ART-7AAF16B96E, ART-71C6BDD9A9, ART-BBEC99B699, ART-F93D07F98B) |
| SPEC-054-01-R11 | The Scope of Work SHALL mark unresolved/unsourced design values (pressures, temperatures, capacity, materials) as `TBD` with `location TBD` where the source clause is not locally accessible. | `_REFERENCES.md`; SKILL four-documents source-grounding rule |

## Standards

| Standard / Code | Applicability | Location |
|---|---|---|
| Sour-service / safety / relief / flare / blowdown / drain-containment / fire-gas / shutdown / environmental / regulatory codes | ASSUMPTION: applicable to this HP flare KO drum package via `OBJ-009`. Specific code citations (e.g., API 521, API 650/620, ASME Section VIII, NFPA, AER/regulatory) are not enumerated in locally accessible source slices. | location TBD — `26020-Package_Requirements.docx` package heading 9; `DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-09/SEC-14/SEC-15 |
| Electrical heat tracing (EHT) and insulation standards | Applicable per SOW-0078 (outdoor HP flare headers EHT-traced and insulated). Specific standards TBD. | location TBD |
| Process Piping / Relief-Flare-Vent / Drain-Containment design standards | Applicable per `INTERFACE_REGISTER.csv` rows. Specific standards TBD. | location TBD |

## Verification

| Req | Verification approach |
|---|---|
| R01 | Inspection: Scope of Work header contains every identity field, cross-checked against `PACKAGE_REGISTER.csv`. |
| R02 | Inspection: package-function statement is textually consistent with SOW-0076. |
| R03 | Inspection: tagged-equipment list matches SOW-0077 verbatim or by tag enumeration (`V-4100-1`, `P-4100-1`). |
| R04 | Inspection: integration narrative reproduces SOW-0078 process notes. |
| R05 | Inspection + traceability: responsibility statements map to `PACKAGE_REGISTER.csv` ResponsibilityModel verbatim or as paraphrase preserving the vendor/EPC split. |
| R06 | Cross-check: declared interface types equal the set in `INTERFACE_REGISTER.csv` for `PKG-054`. |
| R07 | Inspection: source references section cites Workbook row 55, package requirements doc heading 9, and DBM section(s); budgetary go-by labeled informational. |
| R08 | Inspection: objective list equals `{OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010}`. |
| R09 | Inspection: scope-item list equals `{SOW-0075, SOW-0076, SOW-0077, SOW-0078}`. |
| R10 | Artifact inventory: each anticipated artifact has at least one section or attachment satisfying it. |
| R11 | QA review: every numeric/material value either has a cited source slice or is marked `TBD` with `location TBD`. |

## Documentation

The deliverable SHALL produce, at minimum:

- Package scope of work narrative (covers R01–R09).
- Tagged equipment and package identity list (R01, R03).
- Package function and whole-facility integration narrative (R02, R04, R06).
- Responsibility assignment record (R05).
- Source basis / detailed mechanical scope extraction evidence (R07, R11).

Source: `ARTIFACT_REGISTER.csv` (ART-65A805B4B4, ART-7AAF16B96E, ART-71C6BDD9A9, ART-BBEC99B699, ART-F93D07F98B).
