# Specification: DEL-021-01_scope-of-work

## Scope

This specification governs the EPC Integrator-authored Scope of Work for `PKG-021`, the 6.9kV SWITCHGEAR EQUIPMENT package. The Scope of Work is a mandatory Gate 5 EPC anchor deliverable that defines the full package scope, including tagged equipment, package function, source basis, boundaries, and the whole-facility integration narrative used to scope vendor engineering, procurement, and construction.

The package is a vendor-owned Electrical package under WBS 01 (CoA tracking 26020-01-30-012). The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration: interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. This Scope of Work establishes the EPC-side scope statement that anchors the downstream Package Datasheet (`DEL-021-02`), Construction Work Package (`DEL-021-03`), Vendor Engineered Equipment Package (`DEL-021-04`), Vendor Document Turnover Package (`DEL-021-05`), and EPC Vendor Package Review and Acceptance (`DEL-021-06`).

Exclusions:

- Vendor detailed design calculations, certified drawings, equipment ratings selection, and final lineup configuration are excluded from this EPC Scope of Work and are produced under `DEL-021-04`.
- Construction workface execution detail is excluded; it is produced under `DEL-021-03`.
- Lineup-level ratings (bus, interrupting capacity, section count), breaker counts, and protective relay settings are `TBD` here because accessible source slices do not contain confirmed package-specific values; they are deferred to the short-circuit study and vendor engineering.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-021-01-001 | The Scope of Work shall identify `PKG-021`, workbook row 23, WBS 01, CoA tracking 26020-01-30-012, discipline Electrical, and package name "6.9kV SWITCHGEAR EQUIPMENT". Source: Workbook Packages row 23; `PACKAGE_REGISTER.csv`. | Identity field review against Gate 7 registers. |
| REQ-021-01-002 | The Scope of Work shall state the responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-021`. | Responsibility statement review against `PACKAGE_REGISTER.csv`. |
| REQ-021-01-003 | The Scope of Work shall state the package function: 6.9 kV switchgear/MCC equipment supporting medium-voltage distribution to facility process inverter-drive motors rated 5,500 hp and above. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, medium-voltage services table. | Source citation review against DBM electrical section. |
| REQ-021-01-004 | The Scope of Work shall identify the upstream tie-in: radial step-down from the 13.8 kV plant main switchgear via a 13.8 kV / 6.9 kV step-down transformer to the 6.9 kV electrical building. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, plant distribution paragraph. | Tie-in narrative review. |
| REQ-021-01-005 | The Scope of Work shall identify the package-associated electrical building as 820-1 6.9kV Inlet/Sales Compressor Electrical Building (shop-fabricated, prefab). Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings list. | Building reference review. |
| REQ-021-01-006 | The Scope of Work shall represent the medium-voltage service basis: 6.9 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded, with each 6.9 kV transformer grounded by a 100 A, 10 s neutral grounding resistor operating as a tripping system. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, medium-voltage services and grounding paragraphs. | Source citation review. |
| REQ-021-01-007 | The Scope of Work shall include the six applicable interface facts: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. Source: Workbook Packages row 23; `INTERFACE_REGISTER.csv` rows for `PKG-021`. | Interface list cross-check against `INTERFACE_REGISTER.csv`. |
| REQ-021-01-008 | The Scope of Work shall identify the governing project electrical specifications: ELC-QAS-000007-001 Medium Voltage Switchgear and ELC-QAS-000008-001 Medium Voltage Motor Control Centers (with CEC and other project electrical specifications as broader basis). Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical and instrumentation specifications table. | Standards list review. |
| REQ-021-01-009 | The Scope of Work shall state that power-factor-correction capacitor banks shall not be installed on the MCC-8200 synchronous-transfer bus, and that Starting VFDs are used on the KM-2150/2250 Inlet/Sales Gas Compressor motors with synchronous transfer to a normal-service bus. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 6.9 kV MCC paragraph. | Statement-of-design review against DBM. |
| REQ-021-01-010 | The Scope of Work shall mark lineup ratings, breaker counts, interrupting capacity, and protective relay settings as `TBD` pending the project short-circuit study and vendor data; the Scope of Work shall not assign invented values. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, short-circuit study row; `_REFERENCES.md`. | TBD / open-item review. |
| REQ-021-01-011 | The Scope of Work shall preserve cable, grounding, and conduit basis: 6.9 kV cables are three-conductor copper TECK rated 8 kV, 100% insulation, shielded; cable tray and conduit routing shall not interfere with maintenance access. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable table and cable/conduit paragraphs. | Source citation review. |
| REQ-021-01-012 | The Scope of Work shall declare downstream EPC handoffs: `DEL-021-02` Package Datasheet (handoff basis), `DEL-021-03` Construction Work Package (installation/tie-in), `DEL-021-04` Vendor Engineered Equipment Package, `DEL-021-05` Vendor Document Turnover Package, `DEL-021-06` EPC Vendor Package Review and Acceptance. Source: `DELIVERABLE_REGISTER.csv` rows for `PKG-021`. | Cross-deliverable narrative consistency review. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| ELC-QAS-000007-001 Medium Voltage Switchgear (project specification) | Governs medium-voltage switchgear procurement basis. | Applicable; document location TBD; clause-level requirements not derivable from accessible source. |
| ELC-QAS-000008-001 Medium Voltage Motor Control Centers (project specification) | Governs medium-voltage MCC procurement basis (MCC-8200). | Applicable; document location TBD. |
| ELC-QAS-000005-001 Medium Voltage Induction Motors (project specification) | Adjacent; governs the driven-motor side of the 6.9 kV system. | Applicable as adjacent reference; not the switchgear specification itself. |
| Canadian Electrical Code (CEC) | Electrical installation, grounding, conduit support, spacing (MCC to process equipment 7.5 m / 25 ft). | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications (Table 12-1) | Govern facility electrical distribution design and equipment procurement basis. | Applicable; clause locations TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare Scope of Work identity to workbook row 23 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare Scope of Work interface list to `INTERFACE_REGISTER.csv` rows for `PKG-021`. | Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports are all present. |
| Responsibility split | Compare responsibility narrative to `PACKAGE_REGISTER.csv` row `PKG-021`. | Package Vendor and EPC Integrator scopes are not conflated. |
| Source fidelity | Check every non-trivial value, statement-of-design, and requirement against cited DBM section or Gate 7 register row. | Unsupported values are marked `TBD` or `ASSUMPTION`, not asserted as requirements. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, function, interfaces, and TBDs. | No unresolved internal inconsistency. |
| Downstream handoff coverage | Confirm Scope of Work explicitly names downstream deliverables `DEL-021-02` through `DEL-021-06`. | All five downstream deliverables referenced. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Package scope of work narrative.
- Tagged equipment and package identity list (workbook row 23; MCC-8200; 820-1 6.9 kV Inlet/Sales Compressor Electrical Building).
- Package function and integration narrative (medium-voltage feed to inverter-drive process motors rated 5,500 hp and above; KM-2150/2250 inlet/sales compressor motor support).
- Responsibility assignment record (Package Vendor vs. EPC Integrator).
- Source-supported interface list and TBD/open-item list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 23, applicable Gate 7 registers (`PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`), and the DBM electrical source slices used.
