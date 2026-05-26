# Specification — DEL-066-01 Scope of Work (PKG-066 Tanks, Condendate (API 650) 4-25)

## Scope

This Specification establishes the normative content requirements for the EPC Integrator's **Scope of Work** for `PKG-066` Tanks, Condendate (API 650) 4-25. It defines what the Scope of Work artifact must state regarding the package's tagged equipment, package function, source basis, package boundaries, responsibility split, and whole-facility integration narrative.

**Includes:**
- Package identity, workbook row, WBS, CoA tracking number, discipline (Mechanical).
- Package function and major equipment list as source-supported.
- Boundary definition: vendor-owned package vs. EPC-owned integration.
- Applicable interface types at the package boundary.
- Source references and traceability to upstream decomposition basis.

**Excludes:**
- Vendor package engineering and design content (covered by `DEL-066-04_vendor-engineered-equipment-package`).
- Technical datasheet content (covered by `DEL-066-02_package-datasheet`).
- Construction work package content (covered by `DEL-066-03_construction-work-package`).
- Vendor document register and turnover (covered by `DEL-066-05_vendor-document-turnover-package`).
- Acceptance/review evidence (covered by `DEL-066-06_epc-vendor-package-review-and-acceptance`).

Source: `DELIVERABLE_REGISTER.csv` (DEL-066-01 through DEL-066-06).

## Requirements

| Req ID | Requirement | Source |
|---|---|---|
| SPEC-066-01-R01 | The Scope of Work SHALL identify the package by `PKG-066`, workbook row 89, WBS 01, CoA tracking number 26020-01-19-004, discipline Mechanical, and package name "Tanks, Condendate (API 650) 4-25". | `PACKAGE_REGISTER.csv` PKG-066 |
| SPEC-066-01-R02 | The Scope of Work SHALL describe the package's basic function as: supply condensate product storage tanks for 4-25 on-spec C5+ condensate product storage, using the 3-25 condensate tank package as the nearest analog. | `SCOPE_LEDGER.csv` SOW-0206 |
| SPEC-066-01-R03 | The Scope of Work SHALL list the major included equipment: API 650 modified atmospheric condensate product storage tanks with blanket gas; PVRV/EPRV protection; VRU header connection; grounding/cathodic protection provisions; tank instrumentation; standard tank appurtenances. Final tank count, tags, capacity, and dimensions SHALL be carried as TBD pending confirmation, with the Deepcut roster (five condensate tanks) and the 3-25 analog (four 3,800 bbl tanks) cited as candidate bases. | `SCOPE_LEDGER.csv` SOW-0207 |
| SPEC-066-01-R04 | The Scope of Work SHALL document the integration scope note that the analog 3-25 condensate service is on-spec C5+ condensate product storage downstream of treating or bypass paths before condensate export, and that for 4-25 the tank count, tags, capacity, inlet/outlet sources, mercaptan treating bypass/recycle paths, VRU/blanket gas configuration, and design-condition alignment with the 3-25 3,800 bbl tank basis remain to be confirmed. | `SCOPE_LEDGER.csv` SOW-0208 |
| SPEC-066-01-R05 | The Scope of Work SHALL assign package engineering, package design, vendor documentation, and the physical equipment package to the Package Vendor, and integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration) to the EPC Integrator. | `PACKAGE_REGISTER.csv` ResponsibilityModel |
| SPEC-066-01-R06 | The Scope of Work SHALL declare the applicable package-boundary interface types: Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. | `INTERFACE_REGISTER.csv` PKG-066 rows; `PACKAGE_REGISTER.csv` InterfaceTypes |
| SPEC-066-01-R07 | The Scope of Work SHALL cite source basis: Workbook Packages row 89; `26020-Package_Requirements.docx` package heading 21; `DBM-Deepcut/4-25_Deepcut_DBM.md`. ASSUMPTION: analog basis `26020-03-PT-RFQ-19-006 - Conde Tanks.docx` is informational only and SHALL be labeled as such. No direct package-folder brief.md/DOCX/PDF scope source exists for 4-25 (per `PACKAGE_REGISTER.csv` SourceRefRaw). | `PACKAGE_REGISTER.csv` SourceRefRaw |
| SPEC-066-01-R08 | The Scope of Work SHALL state the supported objectives `OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010`. | `OBJECTIVE_DELIVERABLE_MAP.csv`; `DELIVERABLE_REGISTER.csv` |
| SPEC-066-01-R09 | The Scope of Work SHALL identify the scope items it covers: `SOW-0205`, `SOW-0206`, `SOW-0207`, `SOW-0208`. | `SCOPE_LEDGER.csv` |
| SPEC-066-01-R10 | The Scope of Work SHALL produce the anticipated artifacts: package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record; detailed mechanical package scope extraction evidence. | `DELIVERABLE_REGISTER.csv`; `ARTIFACT_REGISTER.csv` (ART-141DADF026, ART-912CBD28E2, ART-E9AAAC9DD8, ART-E0DD04C3E9, ART-BA8C17DE60) |
| SPEC-066-01-R11 | The Scope of Work SHALL mark unresolved/unsourced design values (tank count/tags/capacity, pressures, temperatures, materials, code/standard clauses) as `TBD` with `location TBD` where the source clause is not locally accessible. | `_REFERENCES.md`; SKILL four-documents source-grounding rule |
| SPEC-066-01-R12 | The Scope of Work SHALL state the commercial product disposition context: C5+ condensate is delivered to the NorthRiver Midstream NEBC Connector via LACT, with cross-facility transfer between 04-25 and the 03-25 Liquids Hub. | `DBM-Deepcut/4-25_Deepcut_DBM.md` Process and Commercial Basis; `OBJ-003` |

## Standards

| Standard / Code | Applicability | Location |
|---|---|---|
| API 650 (Welded Tanks for Oil Storage) | Named in package title and SOW-0207 ("modified atmospheric" basis implies API 650 with modifications). Specific clause applicability TBD. | location TBD — `26020-Package_Requirements.docx` package heading 21 |
| API 2510 / NFPA 30 / OGAOM (atmospheric tank spacing) | Applicable to facility integration spacing for condensate tanks (per `DBM-Deepcut/4-25_Deepcut_DBM.md` Site/Spacing section): ≥30.48 m from pressurized bullets (API 2510); 2.35 m between atmospheric tanks (NFPA 30 Tbl 22.4.2.1); ≥50 m from flare (OGAOM Sec. 9.6.15). | `DBM-Deepcut/4-25_Deepcut_DBM.md` Site/Spacing |
| Sour-service / safety / relief / flare / blowdown / drain-containment / fire-gas / shutdown / environmental / regulatory codes | ASSUMPTION: applicable to this condensate tank package via `OBJ-009`. Specific code citations (e.g., API 521, API 620, ASME, NFPA, AER/regulatory) are not enumerated in locally accessible source slices. | location TBD — `26020-Package_Requirements.docx` package heading 21; `DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-09/SEC-14/SEC-15 |
| Cathodic protection / grounding standards | Applicable per SOW-0207 (grounding/cathodic protection provisions) and `INTERFACE_REGISTER.csv` PKG-066 (Grounding/Bonding; Cathodic Protection). Specific standards TBD. | location TBD |
| Blanket gas / PVRV-EPRV / VRU configuration standards | Applicable per SOW-0207 (PVRV/EPRV protection; VRU header connection; blanket gas). Specific standards TBD. | location TBD |
| Process Piping / Relief-Flare-Vent / Drain-Containment design standards | Applicable per `INTERFACE_REGISTER.csv` rows. Specific standards TBD. | location TBD |

## Verification

| Req | Verification approach |
|---|---|
| R01 | Inspection: Scope of Work header contains every identity field, cross-checked against `PACKAGE_REGISTER.csv`. |
| R02 | Inspection: package-function statement is textually consistent with SOW-0206 (basic scope wording preserved, including 3-25 analog reference). |
| R03 | Inspection: tagged-equipment list reproduces SOW-0207; final count/tags/capacity marked TBD; Deepcut roster (5 tanks) and 3-25 analog (4 × 3,800 bbl) cited. |
| R04 | Inspection: integration narrative reproduces SOW-0208 (open items list intact). |
| R05 | Inspection + traceability: responsibility statements map to `PACKAGE_REGISTER.csv` ResponsibilityModel verbatim or as paraphrase preserving the vendor/EPC split. |
| R06 | Cross-check: declared interface types equal the set in `INTERFACE_REGISTER.csv` for `PKG-066` (nine interface types). |
| R07 | Inspection: source references section cites Workbook row 89, package requirements doc heading 21, and DBM section(s); analog `Conde Tanks.docx` labeled informational. |
| R08 | Inspection: objective list equals `{OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010}`. |
| R09 | Inspection: scope-item list equals `{SOW-0205, SOW-0206, SOW-0207, SOW-0208}`. |
| R10 | Artifact inventory: each anticipated artifact (ART-141DADF026, ART-912CBD28E2, ART-E9AAAC9DD8, ART-E0DD04C3E9, ART-BA8C17DE60) has at least one section or attachment satisfying it. |
| R11 | QA review: every numeric/material value either has a cited source slice or is marked `TBD` with `location TBD`. |
| R12 | Inspection: commercial disposition statement names C5+ → NEBC Connector via LACT and the 03-25 cross-facility transfer. |

## Documentation

The deliverable SHALL produce, at minimum:

- Package scope of work narrative (covers R01–R09, R12).
- Tagged equipment and package identity list (R01, R03).
- Package function and whole-facility integration narrative (R02, R04, R06, R12).
- Responsibility assignment record (R05).
- Source basis / detailed mechanical scope extraction evidence (R07, R11).

Source: `ARTIFACT_REGISTER.csv` (ART-141DADF026, ART-912CBD28E2, ART-E9AAAC9DD8, ART-E0DD04C3E9, ART-BA8C17DE60).
