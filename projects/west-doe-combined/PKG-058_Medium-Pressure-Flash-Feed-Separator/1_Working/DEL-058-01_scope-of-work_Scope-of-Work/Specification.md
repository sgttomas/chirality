# Specification — DEL-058-01 Scope of Work (PKG-058 Medium Pressure Flash Feed Separator)

## Scope

This Specification establishes the normative content requirements for the EPC Integrator's **Scope of Work** for `PKG-058` Medium Pressure Flash Feed Separator (MPFF). It defines what the Scope of Work artifact must state regarding the package's tagged equipment, package function, source basis, package boundaries, responsibility split, and whole-facility integration narrative.

**Includes:**
- Package identity, workbook row, WBS, CoA tracking number, discipline (Mechanical).
- Package function and major equipment list as source-supported.
- Operating and design conditions explicitly given in `SCOPE_LEDGER.csv` SOW-0142.
- Boundary definition: vendor-owned package vs. EPC-owned integration; by-others items.
- Applicable interface types at the package boundary (nine types per `INTERFACE_REGISTER.csv`).
- Source references and traceability to upstream decomposition basis.

**Excludes:**
- Vendor package engineering and design content (covered by `DEL-058-04_vendor-engineered-equipment-package`).
- Technical datasheet content (covered by `DEL-058-02_package-datasheet`).
- Construction work package content (covered by `DEL-058-03_construction-work-package`).
- Vendor document register and turnover (covered by `DEL-058-05_vendor-document-turnover-package`).
- Acceptance/review evidence (covered by `DEL-058-06_epc-vendor-package-review-and-acceptance`).

Source: `DELIVERABLE_REGISTER.csv` (DEL-058-01 through DEL-058-06).

## Requirements

| Req ID | Requirement | Source |
|---|---|---|
| SPEC-058-01-R01 | The Scope of Work SHALL identify the package by `PKG-058`, workbook row 71, WBS 01, CoA tracking number 26020-01-17-006, discipline Mechanical, and package name "Medium Pressure Flash Feed Separator". | `PACKAGE_REGISTER.csv` PKG-058 |
| SPEC-058-01-R02 | The Scope of Work SHALL describe the package's basic function as: supply one (1) MPFF Separator — Two Phase, flashing light hydrocarbon vapours from inlet separator raw condensate, with flashed overhead vapours pressure-controlled to the SOC 3rd-stage suction and bottoms condensate level-controlled. | `SCOPE_LEDGER.csv` SOW-0140 |
| SPEC-058-01-R03 | The Scope of Work SHALL list the major included equipment: one (1) MPFF Separator — Two Phase; mistex mist extractor; heated self-framing building module enclosing instrumentation and one vessel end; two (2) PITs; one (1) TIT; one (1) LT for condensate level; one (1) LT for produced water level; one (1) inlet LCV. | `SCOPE_LEDGER.csv` SOW-0141 |
| SPEC-058-01-R04 | The Scope of Work SHALL document the by-others scope: interconnecting piping at skid edge; DCS integration; foundations; electrical power supply from plant MCC; installation and erection. | `SCOPE_LEDGER.csv` SOW-0142 (By others) |
| SPEC-058-01-R05 | The Scope of Work SHALL state the source-supported capacity and operating/design conditions: Normal Throughput 7,883 m³/h; Maximum Throughput 15,223 m³/h; Operating Pressure 1,724 kPag; Operating Inlet Flow 7,883 m³/h; Operating Inlet Temperature −9.55 °C; Design Pressure TBD; Flange Rating ASME Class 300; Design Inlet Flow Rate 15,223 m³/h; Design Temperature −40 °C. | `SCOPE_LEDGER.csv` SOW-0142 |
| SPEC-058-01-R06 | The Scope of Work SHALL assign package engineering, package design, vendor documentation, and the physical equipment package to the Package Vendor, and integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration) to the EPC Integrator. | `PACKAGE_REGISTER.csv` ResponsibilityModel |
| SPEC-058-01-R07 | The Scope of Work SHALL declare the applicable package-boundary interface types: Process Piping; Drain / Containment; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports. | `INTERFACE_REGISTER.csv` PKG-058 rows; `PACKAGE_REGISTER.csv` InterfaceTypes |
| SPEC-058-01-R08 | The Scope of Work SHALL cite source basis: Workbook Packages row 71; `26020-Package_Requirements.docx` package heading 13; `DBM-Deepcut/4-25_Deepcut_DBM.md`. ASSUMPTION: budgetary Word source `Bid Docs/Budgetary/26020-01-PT-RFQ-17-006_MPFF Separator_R0.docx` is informational only and SHALL be labeled as such. | `PACKAGE_REGISTER.csv` SourceRefRaw |
| SPEC-058-01-R09 | The Scope of Work SHALL state the supported objectives `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010`. | `OBJECTIVE_DELIVERABLE_MAP.csv`; `DELIVERABLE_REGISTER.csv` |
| SPEC-058-01-R10 | The Scope of Work SHALL identify the scope items it covers: `SOW-0139`, `SOW-0140`, `SOW-0141`, `SOW-0142`. | `SCOPE_LEDGER.csv` |
| SPEC-058-01-R11 | The Scope of Work SHALL produce the anticipated artifacts: package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record; detailed mechanical package scope extraction evidence. | `DELIVERABLE_REGISTER.csv`; `ARTIFACT_REGISTER.csv` (ART-060CD62000, ART-D3168A53CC, ART-5F228F6180, ART-2F011685B1, ART-4F926E1593) |
| SPEC-058-01-R12 | The Scope of Work SHALL describe the MPFF's whole-facility integration narrative: inlet liquid from upstream inlet-separator liquid outlet heaters; overhead vapour pressure-regulated to SOC 3rd-stage suction; bottoms condensate level-controlled to the downstream stabilizer flash/feed separator; LP fuel gas purge; automated blowdown to HP flare; one-MPFF-per-stabilizer train pairing (2 x 100% normal operating sparing). | `DBM-Deepcut/4-25_Deepcut_DBM.md` (MPFF section; MPFF and Stabilizer Train Relationship); `SCOPE_LEDGER.csv` SOW-0140 |
| SPEC-058-01-R13 | The Scope of Work SHALL mark unresolved/unsourced design values (e.g., Design Pressure, materials of construction, vessel geometry, code citations) as `TBD` with `location TBD` where the source clause is not locally accessible. | `_REFERENCES.md`; SKILL four-documents source-grounding rule |

## Standards

| Standard / Code | Applicability | Location |
|---|---|---|
| Sour-service / safety / relief / flare / blowdown / drain-containment / fire-gas / shutdown / environmental / regulatory codes | ASSUMPTION: applicable via `OBJ-009`. Specific code citations (e.g., API 521, API 12J, ASME Section VIII, NFPA, AER/regulatory) are not enumerated in locally accessible source slices. | location TBD — `26020-Package_Requirements.docx` package heading 13; `DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-09/SEC-14/SEC-15 |
| Pressure vessel design code (anticipated ASME Boiler & Pressure Vessel Code, Section VIII) | ASSUMPTION: applicable to a two-phase separator vessel; ASME Class 300 flange rating is explicitly stated by SOW-0142, implying ASME-derived pressure design basis. | location TBD |
| Electrical heat tracing (EHT) and insulation standards | Applicable per `INTERFACE_REGISTER.csv` (EHT) and facility DBM (winterization / hydrate-suppression). Specific standards TBD. | location TBD |
| Process Piping / Drain-Containment / Fire-Gas / Structural design standards | Applicable per `INTERFACE_REGISTER.csv` rows. Specific standards TBD. | location TBD |

## Verification

| Req | Verification approach |
|---|---|
| R01 | Inspection: Scope of Work header contains every identity field, cross-checked against `PACKAGE_REGISTER.csv` PKG-058. |
| R02 | Inspection: package-function statement is textually consistent with SOW-0140. |
| R03 | Inspection: tagged-equipment list matches SOW-0141 (mist extractor, building module, instrument count). |
| R04 | Inspection: by-others list reproduces SOW-0142 by-others enumeration. |
| R05 | Inspection: capacity / operating / design conditions block reproduces SOW-0142 values; Design Pressure shown as TBD per source. |
| R06 | Inspection + traceability: responsibility statements map to `PACKAGE_REGISTER.csv` ResponsibilityModel verbatim or as paraphrase preserving the vendor/EPC split. |
| R07 | Cross-check: declared interface types equal the set in `INTERFACE_REGISTER.csv` for `PKG-058` (nine rows). |
| R08 | Inspection: source references section cites Workbook row 71, package requirements doc heading 13, and DBM section(s); budgetary Word source labeled informational. |
| R09 | Inspection: objective list equals `{OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010}`. |
| R10 | Inspection: scope-item list equals `{SOW-0139, SOW-0140, SOW-0141, SOW-0142}`. |
| R11 | Artifact inventory: each anticipated artifact has at least one section or attachment satisfying it. |
| R12 | Inspection: integration narrative explicitly names upstream (inlet separator liquid outlet heaters), downstream (stabilizer flash/feed separator, SOC 3rd-stage suction), and ancillary (LP fuel gas purge, HP flare blowdown) flow paths. |
| R13 | QA review: every numeric/material value either has a cited source slice or is marked `TBD` with `location TBD`. |

## Documentation

The deliverable SHALL produce, at minimum:

- Package scope of work narrative (covers R01–R10, R12).
- Tagged equipment and package identity list (R01, R03).
- Package function and whole-facility integration narrative (R02, R07, R12).
- Responsibility assignment record (R06).
- Detailed mechanical package scope extraction evidence (R08, R13).

Source: `ARTIFACT_REGISTER.csv` (ART-060CD62000, ART-D3168A53CC, ART-5F228F6180, ART-2F011685B1, ART-4F926E1593).
