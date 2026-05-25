# Specification: DEL-020-04_vendor-engineered-equipment-package

## Scope

This specification governs the Package Vendor-owned engineering, design, fabrication/supply, and physical equipment package for `PKG-020`, the 13.8kV SWITCHGEAR EQUIPMENT package. It is a Gate 5 vendor production unit anchored by the EPC Scope of Work (`DEL-020-01`) and Package Datasheet (`DEL-020-02`), and is subject to EPC Integrator integration review through `DEL-020-06_epc-vendor-package-review-and-acceptance`.

The package is a vendor-owned Electrical package under WBS 01. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Construction installation, on-site tie-ins, and field turnover activities are excluded (covered by `DEL-020-03_construction-work-package` and the EPC Integrator's facility integration scope).
- The vendor document register, submittals, and turnover records are excluded from this deliverable and are covered by `DEL-020-05_vendor-document-turnover-package`.
- EPC vendor package review and acceptance evidence is excluded and is covered by `DEL-020-06_epc-vendor-package-review-and-acceptance`.
- The upstream utility-supplied 25 kV/13.8 kV transformer is outside this package; the vendor package interface terminates at the 13.8 kV incoming line side of the switchgear.
- Downstream step-down transformers (e.g., 13.8 kV/4.16 kV, 13.8 kV/600 V) are outside this package; the vendor package interface terminates at the 13.8 kV outgoing feeders.
- Package-specific bus continuous current, short-circuit ratings, breaker quantities/ratings, protective-relay schemes, arc-flash boundaries, installation building assignment, and final foundation/support details remain `TBD` where the accessible source set does not provide confirmed package-specific values; the vendor shall resolve these in vendor data during package engineering.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-020-04-001 | The vendor package shall be developed from the accepted EPC Scope of Work (`DEL-020-01`) and Package Datasheet (`DEL-020-02`); the vendor shall not invent scope outside those inputs. Source: `_CONTEXT.md`, Scope; `DELIVERABLE_REGISTER.csv` rows `DEL-020-01`, `DEL-020-02`, `DEL-020-04`. | Cross-reference vendor design basis/datasheet against the accepted EPC inputs. |
| REQ-020-04-002 | The vendor package shall preserve the accepted responsibility split: Package Vendor owns engineering, design, vendor documentation, and physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-020`. | Responsibility statement review against Gate 7 package register. |
| REQ-020-04-003 | The vendor package shall be engineered to the six applicable package interfaces: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. Source: Workbook Packages row 22; `INTERFACE_REGISTER.csv`. | Vendor interface design review against `INTERFACE_REGISTER.csv` rows for `PKG-020`. |
| REQ-020-04-004 | The vendor package shall be engineered for 13.8 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded service consistent with the facility medium-voltage backbone basis. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, medium-voltage services table. | Vendor design basis check against the DBM electrical service basis. |
| REQ-020-04-005 | The 13.8 kV switchgear bus shall be sized for the full facility scope; specific continuous current and short-circuit duty ratings shall be confirmed by detailed electrical studies and reflected in vendor data. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 13.8 kV switchgear design basis. | Vendor design basis review against the facility electrical studies and the EPC Package Datasheet. |
| REQ-020-04-006 | The vendor package shall support radial distribution through step-down transformers from the 13.8 kV bus to facility electrical buildings (e.g., 13.8 kV/4.16 kV, 13.8 kV/600 V), and shall provide a 13.8 kV primary feeder interface for the 04-25 → 03-25 cross-facility sub-feed. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 13.8 kV switchgear distribution paragraph; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, sub-feeder list. | Vendor single-line diagram and feeder schedule review against accepted facility distribution basis. |
| REQ-020-04-007 | The vendor package shall not include a 13.8 kV-level emergency generator interface; standby power is provided at the 600 V MCC level via low-voltage standby generators with transfer switches. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, standby power paragraph. | Vendor design review confirms no 13.8 kV emergency-generator tie-in is engineered. |
| REQ-020-04-008 | The vendor package shall meet grounding/bonding requirements applicable to medium-voltage switchgear without overstating package-specific grounding detail not present in source. Major equipment grounding (two-point ground grid connection) and separate copper grounding conductors per CEC for distribution transformers, panelboards, and three-phase motors larger than 100 hp apply where applicable. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs. | Vendor grounding design review. |
| REQ-020-04-009 | Vendor-supplied internal cable tray and conduit routing shall preserve maintenance access, and shall maintain separation of 13.8 kV power circuits from control and instrument circuits by distance, shielding, or routing. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical buildings paragraph; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs. | Vendor layout review against the Maintenance Access and I&C / Control Cabling interfaces. |
| REQ-020-04-010 | Medium-voltage cabling associated with switchgear feeders shall be three-conductor copper TECK cable rated 15 kV with 133 percent insulation, shielded, where the vendor package supplies or terminates such cable. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, MV cable paragraph. | Vendor cable specification review. |
| REQ-020-04-011 | The vendor package shall produce, as artifacts, the vendor engineered physical equipment package and the vendor package design basis and datasheet set. Source: `_CONTEXT.md`, Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row `DEL-020-04`. | Artifact register check against vendor delivery. |
| REQ-020-04-012 | Source gaps for bus continuous current, short-circuit duty, breaker quantities/ratings, protective-relay scheme, arc-flash boundaries, installation building assignment, and foundation/support details shall be resolved by vendor data during package engineering; values shall not be invented in advance of vendor design. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` not extracted into deliverable-local truth set. | Vendor data review at EPC vendor package acceptance (`DEL-020-06`). |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding, conduit support, and electrical installation basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards | Applicable where the switchgear electrical building or external cable routes encounter hazardous-area classification. | Applicable; package location/classification TBD. |
| Industry medium-voltage switchgear standards (e.g., IEEE/CSA metal-clad switchgear) | Likely applicable to vendor switchgear design, type-test, and arc-flash performance. ASSUMPTION: standard family applies; specific edition/clause TBD pending source confirmation. | ASSUMPTION; not extracted from accessible sources. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |
| EPC Scope of Work (`DEL-020-01`) and EPC Package Datasheet (`DEL-020-02`) | Accepted EPC inputs to vendor package engineering. | Authoritative upstream EPC inputs; status governed by sibling deliverables. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Vendor inputs traceability | Compare vendor design basis to `DEL-020-01` Scope of Work and `DEL-020-02` Package Datasheet. | Vendor scope and parameters trace back to accepted EPC inputs without invented additions. |
| Identity completeness | Compare vendor package identity fields to workbook row 22 and Gate 7 registers. | Package name, IDs, discipline, WBS (01), and CoA tracking number (26020-01-30-011) match. |
| Interface completeness | Compare vendor design interface treatment to `INTERFACE_REGISTER.csv` rows for `PKG-020`. | All six applicable interfaces (Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports) are addressed. |
| Service basis fidelity | Compare vendor design voltage/grounding to DBM medium-voltage services. | 13.8 kV, 3 phase, 3 wire, 60 Hz, LRG basis is preserved. |
| Distribution topology | Compare vendor single-line diagram to DBM 13.8 kV distribution paragraph and 03-25 sub-feed paragraph. | Radial feeders to step-down transformers and the 04-25 → 03-25 sub-feed are represented as interfaces, not redefined. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as vendor commitments. |
| Responsibility split | Compare vendor scope language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated; integration items remain EPC. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |
| Integration handoff readiness | Confirm vendor package outputs are available to `DEL-020-05` (turnover) and `DEL-020-06` (acceptance) workflows. | Outputs identified and listed for EPC review. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Vendor engineered physical equipment package (13.8 kV switchgear lineup, including incoming and outgoing breakers/cells, protective relays, control wiring, and enclosure).
- Vendor package design basis.
- Vendor package datasheet set (bus rating, short-circuit duty, breaker schedule, protection scheme, control diagrams, enclosure/environmental ratings).
- Source-gap / `TBD` list to be closed by vendor data during package engineering.

The deliverable shall cite the Gate 7 snapshot, workbook row 22, applicable Gate 7 registers, and the DBM electrical source slices used for the 13.8 kV switchgear design basis, and shall reference the EPC Scope of Work and Package Datasheet as vendor engineering inputs.
