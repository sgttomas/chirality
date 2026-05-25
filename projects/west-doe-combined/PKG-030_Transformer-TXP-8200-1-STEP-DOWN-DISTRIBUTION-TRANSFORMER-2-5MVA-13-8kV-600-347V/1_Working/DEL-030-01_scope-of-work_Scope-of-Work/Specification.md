# Specification: DEL-030-01 Scope of Work

## Scope

This deliverable defines the EPC Integrator Scope of Work for PKG-030, the workbook-defined Electrical package named `Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V`, WBS 01, tracking number `26020-01-30-021`.

The Scope of Work shall cover:

- package identity, source basis, and workbook row traceability;
- package function and whole-facility integration narrative (13.8 kV to 600 V step-down distribution transformer feeding a 600 V electrical building / MCC bus on the Deepcut facility per the DBM electrical basis);
- tagged equipment where source-supported (transformer tag `TXP-8200-1`);
- responsibility split between Package Vendor and EPC Integrator;
- applicable package interfaces: Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports;
- scope boundaries, assumptions, TBDs, and open items required for downstream package datasheet, construction work package, vendor package production, vendor document turnover, and EPC acceptance.

The Scope of Work shall not assign package engineering, package design, vendor documentation production, or physical equipment package supply to the EPC Integrator. Gate 7 assigns those responsibilities to the Package Vendor and assigns facility-level integration / interface responsibilities to the EPC Integrator.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| SOW-030-01 | The Scope of Work shall identify PKG-030, workbook ID 30, workbook row 32, WBS 01, tracking number `26020-01-30-021`, package name `Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V`, and discipline Electrical. | Compare against workbook Packages row 32 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-030. |
| SOW-030-02 | The Scope of Work shall state that the package is vendor-owned for package engineering, package design, vendor documentation, and physical equipment package supply. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-030. |
| SOW-030-03 | The Scope of Work shall state that the EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement / construction coordination, and facility-level integration. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-030. |
| SOW-030-04 | The Scope of Work shall include the seven source-supported interface categories: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. | Compare against workbook Packages row 32 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-030. |
| SOW-030-05 | The Scope of Work shall reference facility electrical context (BC Hydro 25 kV utility supply via 25 kV / 13.8 kV / 50 MVA transformer, 13.8 kV switchgear as plant main power distribution center, radial step-down distribution to 600 V electrical buildings) only as facility context and shall not convert it into package-specific transformer design values. | Compare against DBM Deepcut Electrical System section and System Voltages table. |
| SOW-030-06 | The Scope of Work shall mark unsupported package-specific design values as `TBD`, including (but not limited to) winding vector group, insulation type (oil or dry), impedance, taps, BIL, temperature rise, cooling class, enclosure type, area classification, dimensions, weight, and footprint. | Review against accessible sources and confirm no unsupported values are introduced. |
| SOW-030-07 | The Scope of Work shall preserve the secondary-side grounding basis: each 600 V transformer shall be grounded by a 5 A continuous high-resistance grounding resistor, consistent with the facility 600 V system high-resistance grounded basis. | Compare against DBM Deepcut Grounding and Bonding section and System Voltages table. |
| SOW-030-08 | The Scope of Work shall identify the downstream 600 V destination (600 V Electrical Building / 600 V MCC) as `TBD-which-EB`, surfacing the open item that the specific destination among the three DBM 600 V electrical buildings (Acid Gas Compressor EB, Sales / Overheads Compressor EB, General Area / Tank Farm / Process EB) is not stated in accessible sources. | Compare against DBM Deepcut Electrical System section (13.8 kV switchgear distribution list) and 0_References / workbook tagged-equipment data; confirm Conflict Table HR-030-01-01 is carried. |
| SOW-030-09 | The Scope of Work shall preserve anticipated artifacts: package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record. | Compare against `_CONTEXT.md` Anticipated Artifacts. |
| SOW-030-10 | The Scope of Work shall identify no declared critical upstream or downstream dependencies unless `_DEPENDENCIES.md` is later updated. | Compare against `_DEPENDENCIES.md` declared lists. |
| SOW-030-11 | The Scope of Work shall, when the transformer is of oil-filled construction, invoke the DBM requirement that large oil-filled transformers be spaced per CEC requirements, installed on structural steel transformer bases, and that secondary containment requirements be reviewed with transformer selection avoiding or limiting containment where practical. Insulation type itself shall remain `TBD` until vendor / engineering selection. | Compare against DBM Deepcut Transformers section. |
| SOW-030-12 | The Scope of Work shall surface that the package name nameplate "600/347 V" three-phase secondary nomenclature is the workbook-stated package identity, while the DBM facility 600 V services are stated as 600 V, 3 phase, 3 wire (not 4 wire / 347 V neutral). The Scope of Work shall not silently reconcile the two; the apparent secondary-system nomenclature discrepancy shall be carried as a human-ruling item. | Compare against package name (workbook row 32) and DBM Deepcut System Voltages table; confirm Conflict Table HR-030-01-02 is carried. |

## Standards

| Standard / basis | Status |
|---|---|
| Gate 7 PROJECT_DECOMP snapshot | Authoritative accepted decomposition basis for package, deliverable, objective, artifact, scope, and interface registers. |
| Workbook Packages row 32 | Authoritative source row for package identity and interface flags. |
| DBM Deepcut electrical sections | Accessible facility-level source for utility supply, 13.8 kV distribution, transformer installation basis, 600 V system voltages, and secondary-side grounding. |
| CEC (Canadian Electrical Code) | Invoked by the DBM for transformer spacing and installation; specific clause locations TBD. |
| CSA enclosure types (Type 12, Type 4X, hazardous-location-approved methods) | Referenced by DBM for general indoor / outdoor / hazardous-area enclosure selection; package-specific enclosure type TBD. |
| Transformer design standards (e.g., IEEE C57, IEC 60076) | Not cited in accessible sources at the package level; location of governing project specifications is TBD. |

## Verification

- Verify identity fields against workbook Packages row 32 and Gate 7 `PACKAGE_REGISTER.csv`.
- Verify deliverable role against Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis.
- Verify responsibility split against Gate 7 `PACKAGE_REGISTER.csv` row PKG-030.
- Verify interface list against workbook row 32 and Gate 7 `PACKAGE_REGISTER.csv` PKG-030 interface columns.
- Verify facility electrical context against DBM Deepcut Electrical System, System Voltages, Transformers, and Grounding and Bonding sections; confirm facility-context language has not been promoted to package design values.
- Confirm each package-specific technical value is source-supported or marked `TBD`.
- Confirm the 600 V destination-EB ambiguity is carried as a human-ruling item (HR-030-01-01).
- Confirm the secondary-system "600/347 V" vs DBM 600 V 3-wire discrepancy is carried as a human-ruling item (HR-030-01-02).
- Confirm cross-document terminology preserves the source package name spelling and tag value `TXP-8200-1`.

## Documentation

The Scope of Work package shall produce or preserve:

- package scope of work;
- tagged equipment and package identity list (with `TXP-8200-1` as the transformer tag from the package name; additional equipment tags `TBD`);
- package function and integration narrative (13.8 kV to 600 V step-down distribution transformer on the West Doe Deepcut facility);
- responsibility assignment record;
- interface basis for Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports;
- list of source limitations, TBDs, assumptions, and human ruling items.
