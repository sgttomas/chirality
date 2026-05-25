# Specification: DEL-017-04_vendor-engineered-equipment-package

## Scope

This specification governs the Package Vendor-owned engineering, design, fabrication/supply, and physical equipment package for `PKG-017`, the MV VFD - 600HP, 4160V, 3PH, 60HZ - 4160V VFD package. It is a Gate 5 vendor production unit anchored by the EPC Scope of Work (`DEL-017-01`) and Package Datasheet (`DEL-017-02`), and is subject to EPC Integrator integration review through `DEL-017-06_epc-vendor-package-review-and-acceptance`.

The package is a vendor-owned Electrical package under WBS 02. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Construction installation, on-site tie-ins, and field turnover activities are excluded (covered by `DEL-017-03_construction-work-package` and the EPC Integrator's facility integration scope).
- The vendor document register, submittals, and turnover records are excluded from this deliverable and are covered by `DEL-017-05_vendor-document-turnover-package`.
- EPC vendor package review and acceptance evidence is excluded and is covered by `DEL-017-06_epc-vendor-package-review-and-acceptance`.
- Driven-motor identification, VFD topology selection, cooling method, harmonic filter sizing, reactive-power mitigation choices, area classification, and installation location remain `TBD` where the accessible source set does not provide confirmed package-specific values; the vendor shall resolve these from the EPC Package Datasheet (`DEL-017-02`) and vendor data during package engineering.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-017-04-001 | The vendor package shall be developed from the accepted EPC Scope of Work (`DEL-017-01`) and Package Datasheet (`DEL-017-02`); the vendor shall not invent scope outside those inputs. Source: `_CONTEXT.md`, Scope; `DELIVERABLE_REGISTER.csv` rows `DEL-017-01`, `DEL-017-02`, `DEL-017-04`. | Cross-reference vendor design basis/datasheet against the accepted EPC inputs. |
| REQ-017-04-002 | The vendor package shall preserve the accepted responsibility split: Package Vendor owns engineering, design, vendor documentation, and physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-017`. | Responsibility statement review against Gate 7 package register. |
| REQ-017-04-003 | The vendor package shall be engineered to the six applicable package interfaces: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: Workbook Packages row 19; `INTERFACE_REGISTER.csv` rows `IFC-5E50E5F700`, `IFC-1340C6D795`, `IFC-6ECD9C92A1`, `IFC-FB4034716A`, `IFC-A807F5E0B3`, `IFC-34EB597147`. | Vendor interface design review against `INTERFACE_REGISTER.csv` rows for `PKG-017`. |
| REQ-017-04-004 | The vendor package nameplate shall reflect the workbook-stated identity: 600 HP, 4160 V, 3-phase, 60 Hz, with 4160 V VFD output. Driven-motor identification and continuous-duty vs. start-only operating basis shall be taken from the accepted EPC Package Datasheet (`DEL-017-02`); ASSUMPTION outside that input is not permitted. Source: Workbook Packages row 19; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, motor basis paragraph. | Vendor nameplate review against workbook row 19 and `DEL-017-02`. |
| REQ-017-04-005 | The vendor package design shall be compatible with the DBM-stated 4160 V system context: 13.8 kV / 4.16 kV, 12 MVA source transformer feeding the 4160 V MCC, with EtherNet communication from the 4160 V MCC to the plant PLC central control panel for data acquisition. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160 V MCC paragraph. | Vendor electrical interface review against the DBM 4160 V system context. |
| REQ-017-04-006 | The vendor package harmonic and reactive-power treatment shall align with EPC-defined electrical studies. Capacitor banks are removed from the synchronous bus on MCC-8200 where VFDs are present (SCA-001 VE #37); the vendor design shall not assume capacitor-bank reactive support that the EPC has removed. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160 V MCC paragraph. | Vendor harmonic / power-quality design review at integration acceptance. |
| REQ-017-04-007 | The vendor package shall be engineered to the Grounding / Bonding interface; where applicable, major electrical equipment shall be connected to the ground grid at two points, and distribution transformers, panelboards, and three-phase motors larger than 100 HP shall be served by separate copper ground conductors sized per CEC. Applicability to this MV VFD package shall be confirmed by detailed design. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, grounding/bonding paragraphs (where present in the electrical section). | Vendor grounding design review. |
| REQ-017-04-008 | The vendor package shall provide an I&C / Control Cabling termination set and a Communications / Network interface sufficient for control, status, and protective interface, consistent with the DBM-stated EtherNet path from the 4160 V MCC to the plant PLC. Specific protocol, address, and signal lists shall be taken from `DEL-017-02`. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160 V MCC paragraph; Workbook Packages row 19; `INTERFACE_REGISTER.csv`. | Vendor I&C and Communications design review against `DEL-017-02`. |
| REQ-017-04-009 | Vendor-supplied internal cable tray, conduit routing, and access provisions shall preserve maintenance access to the VFD, control, and protection sections. Source: Workbook Packages row 19; `INTERFACE_REGISTER.csv` `IFC-A807F5E0B3`. | Vendor layout review against the Maintenance Access interface. |
| REQ-017-04-010 | The vendor package shall produce, as artifacts, the vendor engineered physical equipment package and the vendor package design basis and datasheet set. Source: `_CONTEXT.md`, Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row `DEL-017-04`. | Artifact register check against vendor delivery. |
| REQ-017-04-011 | Source gaps for driven-motor identification, topology, cooling, harmonic filter, area classification, and installation location shall be resolved by `DEL-017-02` and vendor data during package engineering; values shall not be invented in advance of vendor design. Source: `_REFERENCES.md`; `_Sources/26020-Package_Requirements.docx` package search returned no PKG-017 match. | Vendor data review at EPC vendor package acceptance (`DEL-017-06`). |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding, conduit support, and electrical installation basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| NEMA MG1 (motor basis context) | DBM identifies NEMA MG1 compliance for the 4000 V inlet compressor motors; applicability to a 600 HP / 4160 V driven motor is by vendor confirmation through `DEL-017-02`. | Applicable as context; package-specific applicability TBD. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards | Applicable where the installation location classifies the area; package location/classification TBD. | Applicable; package location/classification TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |
| EPC Scope of Work (`DEL-017-01`) and EPC Package Datasheet (`DEL-017-02`) | Accepted EPC inputs to vendor package engineering. | Authoritative upstream EPC inputs; status governed by sibling deliverables. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Vendor inputs traceability | Compare vendor design basis to `DEL-017-01` Scope of Work and `DEL-017-02` Package Datasheet. | Vendor scope and parameters trace back to accepted EPC inputs without invented additions. |
| Identity completeness | Compare vendor package identity fields to workbook row 19 and Gate 7 registers. | Package name, IDs, discipline, WBS, and CoA tracking number (26020-02-30-008) match. |
| Interface completeness | Compare vendor design interface treatment to `INTERFACE_REGISTER.csv` rows for `PKG-017`. | All six applicable interfaces (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) are addressed. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as vendor commitments. |
| Responsibility split | Compare vendor scope language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated; integration items remain EPC. |
| Power-quality basis | Confirm vendor harmonic / reactive-power approach does not assume capacitor-bank support removed by SCA-001 VE #37. | Vendor approach is consistent with the DBM 4160 V MCC paragraph and EPC-defined electrical studies. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |
| Integration handoff readiness | Confirm vendor package outputs are available to `DEL-017-05` (turnover) and `DEL-017-06` (acceptance) workflows. | Outputs identified and listed for EPC review. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Vendor engineered physical equipment package (MV VFD, 600 HP / 4160 V class).
- Vendor package design basis.
- Vendor package datasheet set.
- Source-gap / `TBD` list to be closed by vendor data and `DEL-017-02` during package engineering.

The deliverable shall cite the Gate 7 snapshot, workbook row 19, applicable Gate 7 registers (deliverable, package, artifact, interface, objective-deliverable), and the DBM-Comp_and_Liquids electrical source slices used for the 4160 V system context, and shall reference the EPC Scope of Work and Package Datasheet as vendor engineering inputs.
