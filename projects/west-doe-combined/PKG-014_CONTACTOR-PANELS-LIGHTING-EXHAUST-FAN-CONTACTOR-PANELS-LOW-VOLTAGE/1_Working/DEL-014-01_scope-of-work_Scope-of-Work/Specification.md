# Specification: DEL-014-01 Scope of Work

## Scope

This deliverable defines the EPC Integrator scope of work for PKG-014, the workbook-defined Electrical package named `CONTACTOR PANELS - LIGHTING / EXHAUST FAN CONTACTOR PANELS - LOW VOLTAGE`, WBS 02, tracking number `26020-02-30-005`.

The Scope of Work shall cover:

- package identity, source basis, and workbook row traceability;
- package function and whole-facility integration narrative (low-voltage contactor panels for lighting and exhaust-fan control);
- tagged equipment where source-supported;
- responsibility split between Package Vendor and EPC Integrator;
- applicable package interfaces: Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports;
- scope boundaries, assumptions, TBDs, and open items required for downstream package datasheet (DEL-014-02), construction work package (DEL-014-03), vendor package production (DEL-014-04), vendor document turnover (DEL-014-05), and EPC vendor package review and acceptance (DEL-014-06).

The Scope of Work shall not assign package engineering, package design, vendor documentation production, or physical equipment package supply to the EPC Integrator. Gate 7 assigns those responsibilities to the Package Vendor and assigns facility-level integration/interface responsibilities to the EPC Integrator.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| SOW-014-01 | The Scope of Work shall identify PKG-014, workbook ID 14, workbook row 16, WBS 02, tracking number `26020-02-30-005`, package name `CONTACTOR PANELS - LIGHTING / EXHAUST FAN CONTACTOR PANELS - LOW VOLTAGE`, and discipline Electrical. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-014 and workbook Packages row 16. |
| SOW-014-02 | The Scope of Work shall state that the package is vendor-owned for package engineering, package design, vendor documentation, and physical equipment package supply. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-014. |
| SOW-014-03 | The Scope of Work shall state that the EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-014. |
| SOW-014-04 | The Scope of Work shall include the seven source-supported interface categories: Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. | Compare against Gate 7 `INTERFACE_REGISTER.csv` PKG-014 rows and workbook Packages row 16. |
| SOW-014-05 | The Scope of Work shall describe facility-level low-voltage and lighting/utility electrical context using DBM-derived values (600 V LV HRG; 120/208 V lighting/utility 60 Hz solid grounded) without converting them into package-specific design values. | Compare against `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Electrical Power Distribution table. |
| SOW-014-06 | The Scope of Work shall recognize that 208/120 V AC service is the facility power basis for building exhaust fans and that Remote I/O nodes may carry exhaust-fan and heater controls, without assigning specific load lists to PKG-014. | Compare against `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (208/120 V loads) and `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Remote I/O note). |
| SOW-014-07 | The Scope of Work shall mark unsupported package-specific design values as `TBD`, including contactor-panel counts, ratings, lineup, enclosure type, environmental rating, load schedules, lighting branch circuit details, and exhaust-fan control wiring counts. | Review against accessible sources and confirm no unsupported values are introduced. |
| SOW-014-08 | The Scope of Work shall preserve anticipated artifacts: package scope of work, tagged equipment and package identity list, package function and integration narrative, and responsibility assignment record. | Compare against `_CONTEXT.md` Anticipated Artifacts and Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-014-01_scope-of-work. |
| SOW-014-09 | The Scope of Work shall identify no declared critical upstream or downstream dependencies unless `_DEPENDENCIES.md` is later updated. | Compare against `_DEPENDENCIES.md` declared lists. |
| SOW-014-10 | The Scope of Work shall preserve the source spelling of the package name (`CONTACTOR PANELS - LIGHTING / EXHAUST FAN CONTACTOR PANELS - LOW VOLTAGE`) without normalization or rewording. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-014. |

## Standards

| Standard / basis | Status |
|---|---|
| Gate 7 PROJECT_DECOMP snapshot | Authoritative accepted decomposition basis for package, deliverable, objective, artifact, scope, and interface registers. |
| Workbook Packages row 16 | Authoritative source row for package identity and interface flags. |
| DBM Comp and Liquids electrical basis | Accessible facility-level source for LV (600 V) and lighting/utility (120/208 V) service context, and Remote I/O exhaust-fan/heater control note. |
| DBM Deepcut electrical basis | Accessible facility-level source for contactor-panel housing context and 208/120 V AC loads. |
| Canadian Electrical Code (CEC) | Cited in DBM Deepcut as governing conduit/wiring; `location TBD` at the package level. |
| Package-specific contactor-panel and lighting-control standards and vendor specifications | TBD; not present in accessible source slices for this deliverable. |

## Verification

- Verify identity fields against Gate 7 `PACKAGE_REGISTER.csv` row PKG-014 and workbook Packages row 16.
- Verify deliverable role against Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis.
- Verify responsibility split against Gate 7 `PACKAGE_REGISTER.csv` row PKG-014.
- Verify interface list against Gate 7 `INTERFACE_REGISTER.csv` rows for PKG-014 (seven flagged YES) and workbook row 16.
- Verify LV and lighting/utility service context statements against the DBM Comp and Liquids Electrical Power Distribution table.
- Verify contactor-panel housing and 208/120 V AC load statements against DBM Deepcut.
- Confirm each package-specific technical value is either source-supported or marked `TBD`.
- Confirm cross-document terminology uses the source-spelling package name.

## Documentation

The Scope of Work package shall produce or preserve:

- package scope of work;
- tagged equipment and package identity list, with tag values marked `TBD` when unavailable;
- package function and integration narrative for low-voltage lighting and exhaust-fan contactor panels;
- responsibility assignment record;
- interface basis covering the seven Gate 7 flagged categories;
- list of source limitations, TBDs, assumptions, and human ruling items.
