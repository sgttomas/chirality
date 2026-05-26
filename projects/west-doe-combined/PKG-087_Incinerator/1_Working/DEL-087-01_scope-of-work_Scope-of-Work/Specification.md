# Specification — DEL-087-01 Scope of Work (PKG-087 Incinerator)

> Pass: P1_P2. Source-grounded EPC Scope of Work for the Incinerator package. Requirements are derived from locally accessible source slices; unsupported requirements are marked `TBD` or `ASSUMPTION`.

## Scope

This document specifies the EPC Integrator's Scope of Work for `PKG-087 Incinerator`. It defines:

- the tagged equipment and package identity that constitute the incinerator package supplied by the Package Vendor,
- the package function and integration narrative relative to the facility,
- the boundaries between Package Vendor scope and EPC Integrator scope,
- the responsibility assignment record for package-to-facility interfaces.

In scope:
- Whole-package definition for the Incinerator at `PKG-087` (`PACKAGE_REGISTER.csv` row 64).
- Identification of vendor-supplied tagged equipment (Datasheet §Attributes).
- Integration narrative covering the inbound spent-caustic-tank and DSO off-gas vapour routing, knockout, and stack discharge (`DBM-Deepcut` line 1570).
- Interface inventory (twelve applicable interface types per `PACKAGE_REGISTER.csv` row 64).
- Responsibility split between Package Vendor and EPC Integrator (`PACKAGE_REGISTER.csv` row 64).

Out of scope:
- Vendor package engineering and design content (delivered under `DEL-087-04`).
- Vendor document register and turnover records (delivered under `DEL-087-05`).
- Construction installation and tie-in detail (delivered under `DEL-087-03`).
- Vendor package review and acceptance evidence (delivered under `DEL-087-06`).
- Package technical datasheet content for vendor handoff (delivered under `DEL-087-02`).
- Package exclusions are not asserted; `PACKAGE_REGISTER.csv` row 64 states "TBD; no package-specific exclusions stated in source materials."

## Requirements

R-01. The Scope of Work shall identify all tagged equipment in `PKG-087` as listed in `PACKAGE_REGISTER.csv` row 64 and `DBM-Deepcut` Tag-Detail row 32. Source: as cited.

R-02. The Scope of Work shall record the package process function: vapours from the spent caustic storage tank and DSO off-gas flow to the incinerator; a knockout drum upstream separates free liquids before the stack. Source: `DBM-Deepcut` line 1570.

R-03. The Scope of Work shall preserve the EPC/Vendor responsibility split exactly as stated in `PACKAGE_REGISTER.csv` row 64: Package Vendor owns package engineering, design, vendor documentation, and the physical equipment package; EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

R-04. The Scope of Work shall enumerate the applicable interface types (twelve, per `PACKAGE_REGISTER.csv` row 64 "Applicable Interface Types"): Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports.

R-05. The Scope of Work shall cite the source basis (`Workbook Packages row 64`; `26020-Package_Requirements.docx` package heading 40; `Bid Docs/Budgetary/26020-01-PT-RFQ-25-003_Incinerator.docx`; `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`; `DBM-Deepcut/4-25_Deepcut_DBM.md`) per `PACKAGE_REGISTER.csv` row 64. Section locations within `26020-Package_Requirements.docx` and the RFQ remain `location TBD` (sources not locally accessible in markdown form for this run).

R-06. The Scope of Work shall propagate the open-item flag for the cross-facility service split between facilities 03-25 and 04-25 (`DBM-Comp_and_Liquids` line 56; `DBM-Deepcut` line 1572). The current service-allocation rule is unresolved and is carried as a `CONFLICT` (see `Guidance.md` Conflict Table).

R-07. The Scope of Work shall not impose design values not supported by accessible sources. Where the source records `TBD` or `TBC`, the Scope of Work shall mirror that status, not invent values. Sources: `DBM-Deepcut` lines 1572, 1890; `DBM-Comp_and_Liquids` line 555.

R-08. The Scope of Work shall be associated with scope items `SOW-0111`, `SOW-0112`, `SOW-0113`, `SOW-0114` and with objectives `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010`. Source: `DELIVERABLE_REGISTER.csv` row 348; `OBJECTIVE_SCOPE_MAP.csv` PKG-087 rows.

R-09. The Scope of Work shall include the spacing-related boundary expectations that affect integrator layout: 25 m (82 ft) minimum from any flare/incinerator to nearest plant equipment, and 25 m (82 ft) between fired heaters and the incinerator. Source: `DBM-Deepcut` lines 280, 296 (citing OGAOM Sec. 9.6.15).

R-10. The Scope of Work shall include backflash-protection facts that bound the package's upstream interface: the spent caustic and DSO tanks vent through flame arrestors to the incinerator header. Source: `DBM-Comp_and_Liquids` line 402; `DBM-Deepcut` lines 1562, 1564.

## Standards

| Standard / governing reference | Use | Source | Local access |
|---|---|---|---|
| OGAOM (Oil and Gas Above-ground Mechanical), Sec. 9.6.15 | Minimum spacing between flare/incinerator and plant equipment / fired heaters | `DBM-Deepcut` lines 280, 296 | OGAOM full text not locally accessible — `location TBD`; DBM-Deepcut citation is the working basis |
| `26020-Package_Requirements.docx` package heading 40 | Vendor package requirements basis | `_REFERENCES.md`; `PACKAGE_REGISTER.csv` row 64 | `.docx` not locally accessible in markdown form — `location TBD` |
| `26020-01-PT-RFQ-25-003_Incinerator.docx` | Word source basis (vendor RFQ) | `PACKAGE_REGISTER.csv` row 64 | not locally accessible — `location TBD` |

Code stamps (e.g., ASME, API), pressure-vessel codes, electrical area-classification codes: `TBD` — not stated in locally accessible source slices.

## Verification

| Requirement | Verification approach |
|---|---|
| R-01 | Tag-list cross-check against `PACKAGE_REGISTER.csv` row 64 and `DBM-Deepcut` Tag-Detail row 32. |
| R-02 | Narrative review against `DBM-Deepcut` lines 1568-1572. |
| R-03 | Responsibility-text exact-match check against `PACKAGE_REGISTER.csv` row 64 EPC/Vendor split. |
| R-04 | Interface-type list exact-match check against `PACKAGE_REGISTER.csv` row 64. |
| R-05 | Reference-list completeness check against `PACKAGE_REGISTER.csv` row 64 Source Basis column. |
| R-06 | Open-items registry contains the 03-25/04-25 cross-facility allocation item and links to this deliverable. |
| R-07 | Document scan: no design value not traceable to an accessible source. |
| R-08 | Cross-check `_CONTEXT.md` (Covers Scope Items, Supports Objectives) against `DELIVERABLE_REGISTER.csv` row 348 and `OBJECTIVE_SCOPE_MAP.csv` PKG-087 rows. |
| R-09 | Spacing values match OGAOM Sec. 9.6.15 as cited in `DBM-Deepcut`. |
| R-10 | Backflash-protection statement matches DBM lines 402, 1562, 1564 verbatim or by faithful summary. |

## Documentation (anticipated artifacts under this deliverable)

Per `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv` row 348:

- Package scope of work (this deliverable's primary artifact).
- Tagged equipment and package identity list (Datasheet §Attributes).
- Package function and integration narrative (Guidance §Purpose, §Principles).
- Responsibility assignment record (Guidance §Considerations and Specification R-03/R-04).
