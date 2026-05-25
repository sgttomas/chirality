# Specification: DEL-029-01 Scope of Work

## Scope

This deliverable defines the EPC Integrator Scope of Work for PKG-029, the workbook-defined Electrical package named `Transformer TXP-8600-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V`, WBS 01, tracking number `26020-01-30-020`.

The Scope of Work shall cover:

- package identity, source basis, and workbook row 31 traceability;
- package function and whole-facility integration narrative (13.8 kV primary, 600/347 V secondary step-down service);
- tagged equipment where source-supported (transformer tag `TXP-8600-1`; auxiliary equipment TBD);
- the responsibility split between Package Vendor (engineering, design, documentation, physical equipment package) and EPC Integrator (facility integration, interfaces, tie-ins, constructability, procurement/construction coordination);
- the seven applicable package interfaces flagged in the workbook and `INTERFACE_REGISTER.csv`: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports;
- scope boundaries, assumptions, TBDs, and open items required for downstream Package Datasheet (DEL-029-02), Construction Work Package (DEL-029-03), Vendor Engineered Equipment Package (DEL-029-04), Vendor Document Turnover (DEL-029-05), and EPC Vendor Package Review and Acceptance (DEL-029-06).

The Scope of Work shall NOT assign package engineering, package design, vendor documentation, or physical equipment package supply to the EPC Integrator. Gate 7 assigns those responsibilities to the Package Vendor and assigns facility-level integration/interface responsibilities to the EPC Integrator.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| SOW-029-01 | The Scope of Work shall identify PKG-029, workbook ID 29, workbook row 31, WBS 01, tracking number `26020-01-30-020`, package name `Transformer TXP-8600-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V`, and discipline Electrical. | Compare against `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages sheet row 31 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-029. |
| SOW-029-02 | The Scope of Work shall state that the package is vendor-owned for package engineering, package design, vendor documentation, and physical equipment package supply. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-029. |
| SOW-029-03 | The Scope of Work shall state that the EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-029. |
| SOW-029-04 | The Scope of Work shall include all seven source-supported interface categories: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. | Compare against workbook row 31 and Gate 7 `INTERFACE_REGISTER.csv` PKG-029 rows. |
| SOW-029-05 | The Scope of Work shall identify the transformer's facility role as stepping down a 13.8 kV primary feed (from the plant 13.8 kV switchgear) to a 600/347 V secondary service, consistent with the DBM Power System and System Voltages tables. The mapping of TXP-8600-1 to a specific downstream electrical building, RDC, or yard service is to be marked `TBD` unless explicitly source-supported. | Compare against `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2917-2937. |
| SOW-029-06 | The Scope of Work shall require that the 600 V secondary be grounded with a 5 A continuous high-resistance grounding resistor in accordance with the facility 600 V grounding rule. | Compare against `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2985 ("Each 600 V transformer shall be grounded by a 5 A continuous high-resistance grounding resistor") and System Voltages table line 2937. |
| SOW-029-07 | The Scope of Work shall require that the package be installed in compliance with CEC spacing requirements for transformers and on a structural-steel transformer base on a precast concrete bearing foundation, unless an alternate basis is approved during detailed engineering. | Compare against `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2660, 2745, 2949. |
| SOW-029-08 | The Scope of Work shall require that secondary-containment requirements for the transformer be reviewed during detailed engineering and that transformer selection (oil-filled vs. dry-type, etc.) avoid or limit containment requirements where practical. | Compare against `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Transformers paragraph (line 2949). |
| SOW-029-09 | The Scope of Work shall require that major electrical equipment (including this transformer) be connected to the ground grid at two points and that ground wells be provided at the transformer for maintenance and operational testing. | Compare against `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Grounding paragraph (line 2989). |
| SOW-029-10 | The Scope of Work shall mark unsupported package-specific design values as `TBD`, including (but not limited to): insulating medium (oil-filled vs. dry-type), cooling class, tap changer configuration, BIL, impedance, vector group, noise level, weight, dimensions, fan/cooling controls, RTDs, temperature monitors, primary feeder routing, secondary distribution targets, and downstream electrical-building assignment. | Review against accessible sources and confirm no unsupported value is introduced as a fact. |
| SOW-029-11 | The Scope of Work shall preserve the anticipated artifacts: package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record. | Compare against `_CONTEXT.md` Anticipated Artifacts. |
| SOW-029-12 | The Scope of Work shall identify no declared critical upstream or downstream dependencies unless `_DEPENDENCIES.md` is later updated; coordination mode remains DECLARED. | Compare against `_DEPENDENCIES.md` declared lists. |

## Standards

| Standard / basis | Status |
|---|---|
| Gate 7 PROJECT_DECOMP snapshot (2026-05-24) | Authoritative accepted decomposition basis for package, deliverable, objective, artifact, scope, and interface registers. |
| Workbook Packages row 31 (`_Sources/26020-Packages_Interfaces_4_export.xlsx`) | Authoritative source row for package identity, WBS, tracking number, discipline, and interface flags. |
| `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` electrical design basis | Accessible facility-level source for power system architecture, 13.8 kV/600 V service basis, transformer general requirements, grounding, and foundation concepts. |
| Canadian Electrical Code (CEC) | Referenced by DBM for transformer spacing, ground conductor sizing, and installation. Specific clauses are `location TBD` (no local source slice). |
| CSA C9 / CSA C802 / IEEE C57 (transformer equipment standards) | TBD; not present in accessible source slices for this deliverable. To be confirmed by vendor package data. |
| Package-specific transformer specification (vendor-issued) | TBD; not present in accessible source slices. Expected as a downstream vendor deliverable. |

## Verification

- Verify identity fields against workbook Packages row 31 and Gate 7 `PACKAGE_REGISTER.csv`.
- Verify deliverable role against Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis.
- Verify responsibility split against Gate 7 `PACKAGE_REGISTER.csv` row PKG-029.
- Verify interface list against workbook row 31 and the seven Gate 7 `INTERFACE_REGISTER.csv` rows for PKG-029.
- Verify facility role and system-voltage statements against `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Power System and System Voltages tables.
- Verify grounding and foundation statements against the DBM grounding, foundation, and transformer paragraphs.
- Confirm each package-specific technical value (insulating medium, cooling class, tap changer, impedance, BIL, dimensions, weight, downstream allocation) is either source-supported or marked `TBD`.
- Confirm cross-document terminology consistently uses the source spellings `TXP-8600-1`, `STEP DOWN DISTRIBUTION TRANSFORMER`, `2.5 MVA`, and `13.8 kV / 600/347 V` (the workbook spelling is preserved verbatim where it appears as an identifier).

## Documentation

The Scope of Work shall produce or preserve:

- the package scope of work narrative (identity, function, source basis, integration role, boundaries);
- the tagged equipment and package identity list (`TXP-8600-1` with auxiliary equipment marked `TBD`);
- the package function and integration narrative;
- the responsibility assignment record (Package Vendor vs. EPC Integrator);
- the interface basis for all seven workbook-flagged interfaces;
- a list of source limitations, TBDs, ASSUMPTIONS, and human ruling items (see `Guidance.md` Conflict Table).
