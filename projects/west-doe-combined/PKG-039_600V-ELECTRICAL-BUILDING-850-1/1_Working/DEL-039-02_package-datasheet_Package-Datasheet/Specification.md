# Specification: DEL-039-02_package-datasheet

## Scope

This specification governs the EPC Integrator-authored Package Datasheet for `PKG-039`, the 600V ELECTRICAL BUILDING (850-1) package. The datasheet is a mandatory Gate 5 EPC anchor deliverable and shall provide the technical handoff basis required for third-party vendor or discipline package engineering and design of the prefabricated modular electrical building serving the 600 V Inlet / Sales Compressor area.

The package is a vendor-owned Electrical package under WBS 01. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design calculations, certified drawings, final equipment selections, and final internal lineup configuration are excluded from this EPC datasheet unless later provided as vendor data.
- Package-specific 600 V MCC bus rating, UPS sizing, distribution-transformer kVA, panelboard schedules, HVAC capacity, lighting layout, exact foundation/pile basis, and specific siting on the plot plan are `TBD` because the accessible source set does not provide confirmed package-specific values for building 850-1.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-039-02-001 | The Package Datasheet shall identify `PKG-039`, workbook row 41, WBS 01, CoA tracking number 26020-01-30-030, discipline Electrical, and package name "600V ELECTRICAL BUILDING (850-1)". Source: Workbook Packages row 41; `PACKAGE_REGISTER.csv`. | Identification review against workbook row and Gate 7 registers. |
| REQ-039-02-002 | The Package Datasheet shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-039`. | Responsibility statement review against Gate 7 package register. |
| REQ-039-02-003 | The Package Datasheet shall include the twelve applicable interface facts: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. Source: Workbook Packages row 41; `INTERFACE_REGISTER.csv` rows for `PKG-039`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-039`. |
| REQ-039-02-004 | The Package Datasheet shall identify the low-voltage service basis as 600 V, 3-phase, 3-wire, 60 Hz, high-resistance grounded with 5 A continuous resistor, applied to motors 3/4 hp through 250 hp with direct-on-line starting, lighting/utility distribution transformers, building heaters, and UPS systems larger than 10 kVA. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage and service table. | Source citation review. |
| REQ-039-02-005 | The Package Datasheet shall identify the building 850-1 function as the 600 V Inlet / Sales Compressor Electrical Building, fed from the 13.8 kV main switchgear via step-down transformers. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, building list row 850-1; 13.8 kV switchgear paragraph. | Building-list and switchgear paragraph cross-check. |
| REQ-039-02-006 | The Package Datasheet shall identify the building as a prefabricated modular electrical building with bottom-entry incoming and outgoing cables, elevated on piles, with n + 1 HVAC sizing. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraphs. | DBM citation review. |
| REQ-039-02-007 | The Package Datasheet shall preserve the standby-power basis (TOU LV standby generators at the 600 V MCC level via transfer switches) and shall mark generator sizing, transfer-switch ratings, automatic vs manual transfer, paralleling, and load-shedding/sequencing as `TBD` pending electrical studies and TOU standard confirmation. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Standby Power. | TBD/open-item review. |
| REQ-039-02-008 | The Package Datasheet shall capture grounding and bonding requirements: ground-grid interconnection via driven-pile electrodes with a main #2/0 green insulated conductor; two-point ground connection for major equipment; ground wells at electrical buildings; separate copper ground conductor for distribution transformers, panelboards, and three-phase motors larger than 100 hp per CEC. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Grounding and Bonding. | Grounding interface review. |
| REQ-039-02-009 | The Package Datasheet shall require that cable tray and conduit routing not interfere with maintenance access, and that equipment doors be sized for, or include removable transoms for, removal of the largest equipment. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cable, Wire, and Raceways; Electrical Buildings. | Layout/interface review. |
| REQ-039-02-010 | The Package Datasheet shall require LED interior and exterior lighting per DBM, including flat-panel LED for MCC-room lighting and at least two emergency LED fixtures with battery backup per building. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Lighting and Receptacles. | Lighting basis review. |
| REQ-039-02-011 | The Package Datasheet shall require that 120 VAC receptacles fed from UPS sources be identified in orange and that outdoor receptacles use GFI protection; an outdoor GFI receptacle shall be provided for exterior maintenance. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings; Lighting and Receptacles. | Receptacle schedule review. |
| REQ-039-02-012 | The Package Datasheet shall identify source gaps for 600 V MCC bus rating, UPS quantity/sizing, distribution-transformer kVA, panelboard schedules, exact HVAC capacity, building footprint, foundation/pile design, fire-and-gas device population, and plot-plan siting as `TBD` instead of invented values. Source: `_REFERENCES.md`; package-specific source slice not located. | Gap review before vendor handoff. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical installation basis for grounding, conduit support, conductor sizing, and transformer spacing referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway/UPS basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards | Applicable to electrical equipment, conduit sealing, lighting, and receptacle classification at building entry and adjacent areas. | Applicable; package-specific area classification TBD. |
| NEMA VE2 | Cable tray support where a specific support detail is not included in the drawing package. | Applicable per DBM. |
| Building code (emergency lighting / exit lighting) | Emergency and exit lighting battery-backup provisions. | Applicable per DBM Lighting and Receptacles. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare datasheet identity fields to workbook row 41 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare datasheet matrix to `INTERFACE_REGISTER.csv` rows for `PKG-039`. | All twelve applicable interfaces are present. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices in DBM electrical section. | Unsupported values are marked `TBD` or `ASSUMPTION`. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated. |
| Standby-power interface | Confirm standby power is captured as an interface with `TBD` parameters per DBM Standby Power. | TOU LV-MCC basis cited; sizing/transfer scheme remains TBD. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Package technical datasheet for the 600 V electrical building (850-1).
- Vendor engineering handoff basis.
- Package interface requirements matrix covering the twelve applicable interfaces.
- Source-supported equipment and design criteria (low-voltage service basis, UPS service basis, standby power interface, grounding, HVAC, lighting, raceway, building construction).
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 41, applicable Gate 7 registers, and the DBM electrical source slices used for the building 850-1 basis.
