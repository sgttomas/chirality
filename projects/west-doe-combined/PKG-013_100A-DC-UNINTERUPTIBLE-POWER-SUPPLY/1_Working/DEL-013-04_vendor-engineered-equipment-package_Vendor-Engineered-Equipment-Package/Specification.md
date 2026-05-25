# Specification: DEL-013-04_vendor-engineered-equipment-package

## Scope

This specification governs the Package Vendor-owned engineering, design, fabrication/supply, and physical equipment package for `PKG-013`, the 100A DC UNINTERUPTIBLE POWER SUPPLY package. It is a Gate 5 vendor production unit anchored by the EPC Scope of Work (`DEL-013-01`) and Package Datasheet (`DEL-013-02`), and is subject to EPC Integrator integration review through `DEL-013-06_epc-vendor-package-review-and-acceptance`.

The package is a vendor-owned Electrical package under WBS 02. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Construction installation, on-site tie-ins, and field turnover activities are excluded (covered by `DEL-013-03_construction-work-package` and the EPC Integrator's facility integration scope).
- The vendor document register, submittals, and turnover records are excluded from this deliverable and are covered by `DEL-013-05_vendor-document-turnover-package`.
- EPC vendor package review and acceptance evidence is excluded and is covered by `DEL-013-06_epc-vendor-package-review-and-acceptance`.
- Package-specific UPS ratings, autonomy, charger data, battery type, feeder sizing, distribution-panel assignments, and installation location remain `TBD` where the accessible source set does not provide confirmed package-specific values; the vendor shall resolve these in vendor data during package engineering.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-013-04-001 | The vendor package shall be developed from the accepted EPC Scope of Work (`DEL-013-01`) and Package Datasheet (`DEL-013-02`); the vendor shall not invent scope outside those inputs. Source: `_CONTEXT.md`, Scope; `DELIVERABLE_REGISTER.csv` rows `DEL-013-01`, `DEL-013-02`, `DEL-013-04`. | Cross-reference vendor design basis/datasheet against the accepted EPC inputs. |
| REQ-013-04-002 | The vendor package shall preserve the accepted responsibility split: Package Vendor owns engineering, design, vendor documentation, and physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-013`. | Responsibility statement review against Gate 7 package register. |
| REQ-013-04-003 | The vendor package shall be engineered to the four applicable package interfaces: Electrical Power, Grounding / Bonding, Maintenance Access, and Structural / Foundations / Supports. Source: Workbook Packages row 15; `INTERFACE_REGISTER.csv`. | Vendor interface design review against `INTERFACE_REGISTER.csv` rows for `PKG-013`. |
| REQ-013-04-004 | The vendor package design basis shall be consistent with the DBM electrical voltage/service basis (120 VAC / 125 VDC UPS services supporting control system, selected emergency or critical lighting, MV breaker control, and MV protective relays). Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage/service table. | Vendor design basis check against the DBM electrical service basis. |
| REQ-013-04-005 | The vendor package shall be engineered to be compatible with standby power coordination during outages and turnarounds; generator sizing, transfer-switch configuration, load shedding, sequencing, and TOU standard confirmation remain owned by EPC integration and are `TBD` for vendor design until resolved. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, standby power paragraph. | TBD/open-item review at integration acceptance. |
| REQ-013-04-006 | The vendor package shall meet grounding/bonding requirements applicable to electrical equipment without overstating package-specific grounding detail not present in source. Major equipment grounding (two-point ground grid connection) and separate copper grounding conductors per CEC for distribution transformers, panelboards, and three-phase motors larger than 100 hp apply where applicable. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs. | Vendor grounding design review. |
| REQ-013-04-007 | Vendor-supplied internal cable tray and conduit routing shall preserve maintenance access. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs. | Vendor layout review against the Maintenance Access interface. |
| REQ-013-04-008 | The vendor package shall produce, as artifacts, the vendor engineered physical equipment package and the vendor package design basis and datasheet set. Source: `_CONTEXT.md`, Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row `DEL-013-04`. | Artifact register check against vendor delivery. |
| REQ-013-04-009 | Source gaps for UPS count/rating, battery, charger, feeder, distribution, physical location, and support requirements shall be resolved by vendor data during package engineering; values shall not be invented in advance of vendor design. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` package search returned no PKG-013 match. | Vendor data review at EPC vendor package acceptance (`DEL-013-06`). |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding, conduit support, and electrical installation basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards | Applicable to electrical equipment, conduit sealing, and installation classification where hazardous/non-hazardous areas are defined. | Applicable; package location/classification TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |
| EPC Scope of Work (`DEL-013-01`) and EPC Package Datasheet (`DEL-013-02`) | Accepted EPC inputs to vendor package engineering. | Authoritative upstream EPC inputs; status governed by sibling deliverables. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Vendor inputs traceability | Compare vendor design basis to `DEL-013-01` Scope of Work and `DEL-013-02` Package Datasheet. | Vendor scope and parameters trace back to accepted EPC inputs without invented additions. |
| Identity completeness | Compare vendor package identity fields to workbook row 15 and Gate 7 registers. | Package name, IDs, discipline, WBS, and CoA tracking number match. |
| Interface completeness | Compare vendor design interface treatment to `INTERFACE_REGISTER.csv` rows for `PKG-013`. | Electrical Power, Grounding / Bonding, Maintenance Access, and Structural / Foundations / Supports are addressed. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as vendor commitments. |
| Responsibility split | Compare vendor scope language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated; integration items remain EPC. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |
| Integration handoff readiness | Confirm vendor package outputs are available to `DEL-013-05` (turnover) and `DEL-013-06` (acceptance) workflows. | Outputs identified and listed for EPC review. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Vendor engineered physical equipment package.
- Vendor package design basis.
- Vendor package datasheet set.
- Source-gap / `TBD` list to be closed by vendor data during package engineering.

The deliverable shall cite the Gate 7 snapshot, workbook row 15, applicable Gate 7 registers, and the DBM electrical source slices used for UPS/electrical design basis, and shall reference the EPC Scope of Work and Package Datasheet as vendor engineering inputs.
