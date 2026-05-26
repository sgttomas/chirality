# Specification — DEL-044-02 Package Datasheet (PKG-044 Instrumentation)

## Scope

This specification governs the EPC Package Datasheet produced for PKG-044, "Instrumentation (outside of Mechanical Packages only)" (Workbook Packages row 46, WBS 02, CoA 26020-01-32-002). The datasheet provides the technical handoff data required for third-party vendor or discipline-package engineering and design and the package interface requirements matrix.

**In scope:** package identity; design conditions; tagged equipment summary (when source-supported); declared physical interfaces (Process Piping, Utility Piping, Electrical Power, I&C / Control Cabling, Communications / Network); EPC-Integrator boundary statements; references to authoritative DBM and workbook sources.

**Excluded:** Mechanical-Package-internal instrumentation (carried inside the owning mechanical package per the package taxonomy implied by the package title); vendor-internal design details produced downstream of handoff.

Source: `_CONTEXT.md`; PACKAGE_REGISTER.csv (PKG-044); DELIVERABLE_REGISTER.csv (DEL-044-02).

## Requirements

| Req ID | Requirement | Source | Type |
|---|---|---|---|
| R-044-02-01 | The datasheet shall identify the package by PackageID, Workbook row, WBS, CoA tracking number, and discipline. | PACKAGE_REGISTER.csv | FACT |
| R-044-02-02 | The datasheet shall declare the five package interface types as recorded in source: Process Piping, Utility Piping, Electrical Power, I&C / Control Cabling, Communications / Network. | INTERFACE_REGISTER.csv (PKG-044 rows) | FACT |
| R-044-02-03 | The datasheet shall state the package responsibility model exactly as carried in the package register: "EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred from current sources." | PACKAGE_REGISTER.csv | FACT |
| R-044-02-04 | The datasheet shall record the Gate 6 disposition that instrumentation field supports, power, and communications are included in each package scope as appropriate under the plug-n-play package philosophy. | INTERFACE_REGISTER.csv (PKG-044 interface notes) | FACT |
| R-044-02-05 | The minimum design ambient temperature for exposed equipment, package buildings, control panels, instrumentation, and field devices shall be -40 deg C unless a more severe process or vendor condition applies. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, line 145 | FACT |
| R-044-02-06 | Analyzer-quality air, when required by the equipment list, shall meet: hydrocarbon content < 1 ppm and dew point < -40 deg C. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, line 509 | FACT |
| R-044-02-07 | The datasheet shall identify exclusions explicitly; if no package-specific exclusions are stated in source, the datasheet shall record "TBD; no package-specific exclusions stated in source materials." | PACKAGE_REGISTER.csv | FACT |
| R-044-02-08 | The datasheet shall enumerate the equipment tag list and associated I/O / loop list for PKG-044. | ASSUMPTION (typical EPC Package Datasheet content) — location TBD; specific list not present in locally accessible sources | ASSUMPTION |
| R-044-02-09 | Project electrical and instrumentation specifications listed in the governing DBM Table 12-1 shall govern electrical distribution design and equipment procurement basis for items implemented by this package. | DBM-Deepcut/4-25_Deepcut_DBM.md, lines 2870, 2887-2891 (referenced for instrumentation specification set) | FACT (cross-DBM reference) |

## Standards

| Standard / Spec | Reference | Status |
|---|---|---|
| Project Instrumentation Specifications (Instrumentation General; Instrumentation for Packaged Equipment; Vibration Instrumentation) | ELC-QAS-000014-001; ELC-QAS-000015-001; ELC-QAS-000018-001 | Cited in DBM-Deepcut/4-25_Deepcut_DBM.md (lines 2887-2891); applicable per project specification index — location TBD for this package's binding subset |
| Project area classification, F&G, ESD specifications | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (lines 704, 826-830) | ASSUMPTION: applicable; binding subset TBD |
| Final project standards register | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, line 888 | TBD: shall be verified against the latest project specification index |

## Verification

| Req ID | Verification Approach | Procedure Hook |
|---|---|---|
| R-044-02-01 | Cross-check datasheet identity block against PACKAGE_REGISTER.csv row for PKG-044. | Procedure.md Step 1 |
| R-044-02-02 | Cross-check declared interface list against INTERFACE_REGISTER.csv rows for PKG-044 (expect 5 rows). | Procedure.md Step 2 |
| R-044-02-03 | Verbatim string check against package register `ResponsibilityModel` field. | Procedure.md Step 3 |
| R-044-02-04 | Verbatim presence check of Gate 6 disposition sentence in datasheet Construction or Interfaces section. | Procedure.md Step 3 |
| R-044-02-05 | Datasheet Conditions table includes -40 deg C statement with DBM citation. | Procedure.md Step 4 |
| R-044-02-06 | Datasheet Conditions table includes analyzer-quality air spec with DBM citation. | Procedure.md Step 4 |
| R-044-02-07 | Datasheet Attributes table includes Exclusions row matching source convention. | Procedure.md Step 3 |
| R-044-02-08 | Equipment tag list present OR explicitly marked TBD with location TBD reference. | Procedure.md Step 5 |
| R-044-02-09 | Standards section cites the three identified instrumentation specifications. | Procedure.md Step 6 |

## Documentation

The following artifacts (from `_CONTEXT.md` Anticipated Artifacts) are produced by or anchored in this deliverable:

- Package technical datasheet (`Datasheet.md`).
- Vendor engineering handoff basis (Datasheet + Specification together).
- Package interface requirements matrix (Datasheet "Interfaces" table, sourced from INTERFACE_REGISTER.csv).
- Source-supported equipment and design criteria (Datasheet "Conditions" + "Attributes" with citations).

Downstream consumers: vendor / discipline-package engineering and design teams; DEL-044-03 (Construction Work Package); DEL-044-04 (EPC / Instrumentation Discipline Production Package).
