# Specification: DEL-014-02_package-datasheet

## Scope

This specification governs the EPC Integrator-authored Package Datasheet for `PKG-014`, the CONTACTOR PANELS - LIGHTING / EXHAUST FAN CONTACTOR PANELS - LOW VOLTAGE package. The datasheet is a mandatory Gate 5 EPC anchor deliverable and shall provide the technical handoff basis required for third-party vendor or discipline package engineering and design.

The package is a vendor-owned Electrical package under WBS 02. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design calculations, certified drawings, contactor selections, and final per-circuit schedules are excluded from this EPC datasheet unless later provided as vendor data.
- Package-specific panel quantities, contactor ratings, circuit-by-circuit schedules, feeder sizing, in-building mounting layout, and per-building assignment are `TBD` because the accessible source set does not provide confirmed package-specific values.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-014-02-001 | The Package Datasheet shall identify `PKG-014`, workbook row 16, WBS 02, CoA tracking number 26020-02-30-005, discipline Electrical, and the full package name "CONTACTOR PANELS - LIGHTING / EXHAUST FAN CONTACTOR PANELS - LOW VOLTAGE." Source: Workbook Packages row 16; `PACKAGE_REGISTER.csv`. | Datasheet identification review against workbook row and Gate 7 registers. |
| REQ-014-02-002 | The Package Datasheet shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-014`. | Responsibility statement review against Gate 7 package register. |
| REQ-014-02-003 | The Package Datasheet shall include the seven applicable interface facts: Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. Source: Workbook Packages row 16; `INTERFACE_REGISTER.csv` rows for `PKG-014`. | Interface matrix check against `INTERFACE_REGISTER.csv`. |
| REQ-014-02-004 | The Package Datasheet shall identify the 208/120 V, 3 phase, 4 wire, 60 Hz, solidly grounded lighting and utility service as the upstream supply basis for the contactor panels, sourced from 600 V to 208/120 V distribution transformers feeding dedicated 208/120 V distribution panelboards. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` "208/120 V Systems and SCR Heater Controls" and "Voltage Levels and Services". | Source citation review. |
| REQ-014-02-005 | The Package Datasheet shall require contactor panels to control loads supported by the 208/120 V system, including lighting and receptacles, building exhaust fans, building heater blower fans, electric heat tracing (where assigned), and packaged equipment requiring 208/120 V power. Source: DBM "208/120 V Systems and SCR Heater Controls"; "Lighting and Receptacles". | Load-list review against source. |
| REQ-014-02-006 | The Package Datasheet shall require contactor panels housed within prefabricated modular electrical buildings to be coordinated with the building scope: bottom cable entry, pile-supported elevated building, n + 1 HVAC, EMT permitted between adjacent panels and contactor panels, and equipment door sizing/removable transoms for largest-equipment removal. Source: DBM "Electrical Buildings". | Building-coordination review. |
| REQ-014-02-007 | The Package Datasheet shall require grounding and bonding consistent with the project basis: distribution transformers and panelboards have a separate copper ground conductor sized per CEC in addition to the grounding conductor with power wiring; building uses driven piles as ground electrodes interconnected by a #2/0 green insulated grounding conductor; transformer neutral solidly grounded. Source: DBM "Grounding and Bonding"; "208/120 V Systems and SCR Heater Controls". | Grounding/bonding review. |
| REQ-014-02-008 | The Package Datasheet shall require the contactor panels for exhaust-fan and heater control to coordinate with the plant control system, including Allen-Bradley Flex5000 Remote I/O nodes at RDCs that may support building exhaust-fan and heater control. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Remote I/O paragraph; DBM Control Systems sections. | Control-interface review. |
| REQ-014-02-009 | The Package Datasheet shall require that where forced-ventilation modules or buildings rely on ventilation to maintain area classification, exhaust-fan control and monitoring shall include an interlock initiated in the plant control system. Source: DBM "Area Classification and Hazardous Locations" (forced-ventilation paragraph). | Hazard/interlock review. |
| REQ-014-02-010 | The Package Datasheet shall require lighting served via lighting contactor panels to be LED type, with fixtures suitable for the area classification, MCC-room flat-panel LED fixtures, process-area and outdoor LED fixtures, post lighting for the overall area where required, exit lights with battery backup per building code, and at least two emergency lighting fixtures per building for outage conditions. Source: DBM "Lighting and Receptacles". | Lighting-load review. |
| REQ-014-02-011 | The Package Datasheet shall not assign panel count, contactor ratings, per-circuit schedules, feeder sizing, in-building mounting locations, or per-building assignment beyond what accessible source slices support; unsupported values shall remain `TBD`. Source: `_REFERENCES.md`; absence of PKG-014 match in `26020-Package_Requirements.docx`. | Gap review before vendor handoff. |
| REQ-014-02-012 | The Package Datasheet shall require cable tray and conduit routing supplying or interconnecting contactor panels to not interfere with maintenance access; rigid conduit shall be used for building lighting, exhaust fans, receptacles, and switches in shop-fabricated/erected buildings; EMT may be used in non-process locations. Source: DBM "Cable, Wire, and Raceways". | Raceway/maintenance-access review. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Conduit installation, grounding-conductor sizing, area-classification compliance, and electrical installation basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway/lighting/receptacle basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards | Applicable to contactor-panel housing, lighting, receptacles, conduit sealing, and exhaust-fan interlock for ventilation-dependent area classification. | Applicable; package location/classification TBD. |
| Building codes (exit / emergency lighting) | Exit-light battery backup and emergency-lighting provisions are required as per building code. | Applicable; specific code reference TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare datasheet identity fields to workbook row 16 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare datasheet matrix to `INTERFACE_REGISTER.csv` rows for `PKG-014`. | All seven interface facts (Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) are present. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, voltage class, interfaces, and `TBD` items. | No unresolved internal inconsistency. |
| Forced-ventilation interlock | Confirm the requirement for exhaust-fan control/monitoring with plant-control-system interlock is preserved wherever exhaust-fan-related sections appear. | Requirement consistently expressed across documents. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Package technical datasheet.
- Vendor engineering handoff basis.
- Package interface requirements matrix (seven interfaces).
- Source-supported equipment and design criteria.
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 16, applicable Gate 7 registers, and the DBM electrical source slices used for 208/120 V system basis, electrical buildings, grounding/bonding, raceways, lighting, and exhaust-fan/area-classification interlock.
