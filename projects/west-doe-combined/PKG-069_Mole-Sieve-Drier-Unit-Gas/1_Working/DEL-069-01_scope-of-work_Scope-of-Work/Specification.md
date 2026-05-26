# Specification — DEL-069-01 Scope of Work (PKG-069 Mole Sieve Drier Unit (Gas))

## Scope

This Specification establishes the normative content requirements for the EPC Integrator's **Scope of Work** for `PKG-069` Mole Sieve Drier Unit (Gas). It defines what the Scope of Work artifact must state regarding the package's tagged equipment, package function, source basis, package boundaries, responsibility split, and whole-facility integration narrative.

**Includes:**
- Package identity, workbook row, WBS, CoA tracking number, discipline (Mechanical).
- Package function and major equipment list as source-supported by the 04-25 Deepcut DBM.
- Boundary definition: vendor-owned package vs. EPC-owned integration.
- Applicable interface types at the package boundary (12 types per `INTERFACE_REGISTER.csv`).
- Source references and traceability to upstream decomposition basis.

**Excludes:**
- Vendor package engineering and design content (covered by `DEL-069-04_vendor-engineered-equipment-package`).
- Technical datasheet content for vendor handoff (covered by `DEL-069-02_package-datasheet`).
- Construction work package content (covered by `DEL-069-03_construction-work-package`).
- Vendor document register and turnover (covered by `DEL-069-05_vendor-document-turnover-package`).
- EPC vendor-package review/acceptance evidence (covered by `DEL-069-06_epc-vendor-package-review-and-acceptance`).
- NGL Mole Sieve Drier Unit (a distinct workbook package per Gate-6 disposition).

Source: `DELIVERABLE_REGISTER.csv` (DEL-069-01 through DEL-069-06); `PACKAGE_REGISTER.csv` PKG-069 NotesRaw.

## Requirements

| Req ID | Requirement | Source |
|---|---|---|
| SPEC-069-01-R01 | The Scope of Work SHALL identify the package by `PKG-069`, workbook row 73, WBS 01, CoA tracking number 26020-01-22-002, discipline Mechanical, and package name "Mole Sieve Drier Unit (Gas)". | `PACKAGE_REGISTER.csv` PKG-069 |
| SPEC-069-01-R02 | The Scope of Work SHALL describe the package's basic function as: provide final dehydration of process gas upstream of cryogenic recovery via three molecular-sieve adsorber driers (two in adsorption, one in standby/regeneration/cooling), with two 100% inlet filter/coalescers upstream and dust filtration downstream. | `DBM-Deepcut/4-25_Deepcut_DBM.md` (line ~1243, ~1263, ~2362) |
| SPEC-069-01-R03 | The Scope of Work SHALL list the major included equipment by tag: `AC-6180-1`, `K-6190-1`, `K-6195-1`, `F-5910-1`, `F-5920-1`, `F-6151-1`, `F-6155-1`, `E-6170-1`, `V-6160-1`, `V-6130-1`, `V-6140-1`, `V-6150-1`, `V-6185-1`. | `DBM-Deepcut/4-25_Deepcut_DBM.md` equipment inventory row 56 (line ~2607) |
| SPEC-069-01-R04 | The Scope of Work SHALL document that mole sieve regeneration gas heating is supplied by a separate direct-fired heater and is NOT served by the unified heat medium loop. | `DBM-Deepcut/4-25_Deepcut_DBM.md` (line ~1947) |
| SPEC-069-01-R05 | The Scope of Work SHALL document the integration of the gas mole sieve into the wider process train: TEG dehydration upstream → inlet filter/coalescers → adsorber driers → mole-sieve dust filtration → mercury recovery unit → MRU dust filter → UltraTEF cryogenic unit. | `DBM-Deepcut/4-25_Deepcut_DBM.md` (line ~1243) |
| SPEC-069-01-R06 | The Scope of Work SHALL assign package engineering, package design, vendor documentation, and the physical equipment package to the Package Vendor, and integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration) to the EPC Integrator. | `PACKAGE_REGISTER.csv` ResponsibilityModel |
| SPEC-069-01-R07 | The Scope of Work SHALL declare the applicable package-boundary interface types: Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports. | `INTERFACE_REGISTER.csv` PKG-069 rows; `PACKAGE_REGISTER.csv` InterfaceTypes |
| SPEC-069-01-R08 | The Scope of Work SHALL cite source basis: Workbook Packages row 73; `26020-Package_Requirements.docx` package heading for row 73; `DBM-Deepcut/4-25_Deepcut_DBM.md` (mole sieve narrative, equipment inventory, sparing, regeneration heat, moisture analyzers, isolation philosophy). | `PACKAGE_REGISTER.csv` SourceRefRaw |
| SPEC-069-01-R09 | The Scope of Work SHALL state the supported objectives `OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010`. | `OBJECTIVE_DELIVERABLE_MAP.csv`; `DELIVERABLE_REGISTER.csv` |
| SPEC-069-01-R10 | The Scope of Work SHALL identify the scope items it covers: `SOW-0144`. | `SCOPE_LEDGER.csv` |
| SPEC-069-01-R11 | The Scope of Work SHALL produce the anticipated artifacts: package scope of work narrative; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record. | `DELIVERABLE_REGISTER.csv`; `ARTIFACT_REGISTER.csv` (ART-CA6ACF97B8, ART-E3BAD449B0, ART-ED8784A9C5, ART-875349E7C7) |
| SPEC-069-01-R12 | The Scope of Work SHALL record the Gate-6 disposition that gas mole sieve scope is referenced as included with the Cryogenic Unit package scope while `PKG-069` remains a discrete workbook package; the integration ruling SHALL be carried as a conflict pending human disposition. | `PACKAGE_REGISTER.csv` PKG-069 NotesRaw |
| SPEC-069-01-R13 | The Scope of Work SHALL mark unresolved/unsourced design values (pressures, temperatures, bed sizing, cycle time, regeneration heater duty, materials, codes) as `TBD` with `location TBD` where the source clause is not locally accessible. | `_REFERENCES.md`; SKILL `four-documents` source-grounding rule |
| SPEC-069-01-R14 | The Scope of Work SHALL include the moisture analysis basis (two moisture analyzers manifolded from common line and each of three driers) and the isolation philosophy (unit-level isolation for maintenance) where applicable to package boundary definition. | `DBM-Deepcut/4-25_Deepcut_DBM.md` (line ~2134, ~2408) |

## Standards

| Standard / Code | Applicability | Location |
|---|---|---|
| Adsorber pressure-vessel codes (e.g., ASME Section VIII) | ASSUMPTION: applicable to adsorber vessels `V-6130-1`, `V-6140-1`, `V-6150-1` and ancillary vessels. Specific code citations not enumerated in locally accessible source slices. | location TBD — `26020-Package_Requirements.docx` package row 73 heading; DBM mechanical sections |
| Sour-service / safety / relief / flare / blowdown / drain-containment / fire-gas / shutdown / environmental / regulatory codes | ASSUMPTION: applicable to this package via `OBJ-009`. Specific codes (e.g., NACE MR0175, API, NFPA, AER) not enumerated in locally accessible source slices. | location TBD |
| Direct-fired heater (regeneration gas) codes | Applicable per separate-direct-fired regeneration heater scope (DBM line ~1947). Specific code citations TBD. | location TBD |
| Process Piping / Relief-Flare-Vent / Drain-Containment / I&C design standards | Applicable per `INTERFACE_REGISTER.csv` PKG-069 rows. Specific standards TBD. | location TBD |
| Electrical Power / EHT / Grounding-Bonding / Area Lighting standards | Applicable per `INTERFACE_REGISTER.csv` PKG-069 rows. Specific standards TBD. | location TBD |

## Verification

| Req | Verification approach |
|---|---|
| R01 | Inspection: Scope of Work header contains every identity field, cross-checked against `PACKAGE_REGISTER.csv`. |
| R02 | Inspection: package-function statement is textually consistent with DBM mole-sieve narrative (line ~1243, ~1263). |
| R03 | Inspection: tagged-equipment list matches DBM equipment inventory row 56 (line ~2607) verbatim by tag. |
| R04 | Inspection: regeneration heating statement reproduces DBM heat-medium statement (line ~1947) preserving the separate-direct-fired-heater fact. |
| R05 | Inspection: integration narrative reproduces upstream/downstream process train per DBM (line ~1243). |
| R06 | Inspection + traceability: responsibility statements map to `PACKAGE_REGISTER.csv` ResponsibilityModel verbatim or paraphrase preserving vendor/EPC split. |
| R07 | Cross-check: declared interface types equal the set in `INTERFACE_REGISTER.csv` for `PKG-069` (12 types). |
| R08 | Inspection: source references section cites workbook row 73, package requirements doc heading, and DBM sections. |
| R09 | Inspection: objective list equals `{OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010}`. |
| R10 | Inspection: scope-item list equals `{SOW-0144}`. |
| R11 | Artifact inventory: each anticipated artifact has at least one section/attachment satisfying it. |
| R12 | Inspection: Gate-6 disposition note present; conflict captured in Guidance Conflict Table. |
| R13 | QA review: every numeric/material/code value either has a cited source slice or is marked `TBD` with `location TBD`. |
| R14 | Inspection: moisture-analysis and isolation statements present where they bear on package boundary. |

## Documentation

The deliverable SHALL produce, at minimum:

- Package scope of work narrative (covers R01–R10, R12, R14) — `ART-CA6ACF97B8`.
- Tagged equipment and package identity list (R01, R03) — `ART-E3BAD449B0`.
- Package function and whole-facility integration narrative (R02, R04, R05, R07) — `ART-ED8784A9C5`.
- Responsibility assignment record (R06) — `ART-875349E7C7`.
- Source-basis / extraction evidence (R08, R13) — supported by `_REFERENCES.md`.

Source: `ARTIFACT_REGISTER.csv` (PKG-069 / DEL-069-01 rows).
