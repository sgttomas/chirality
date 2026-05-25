# Specification: DEL-030-04_vendor-engineered-equipment-package

## Scope

This specification governs the Vendor Engineered Equipment Package for `PKG-030`, "Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V." The deliverable is the Package Vendor production unit covering engineering, design, fabrication/supply, and the physical equipment package developed from the EPC Package Scope of Work (`DEL-030-01`) and Package Datasheet (`DEL-030-02`), with EPC Integrator integration review.

The package is a vendor-owned Electrical package under WBS 01 (CoA tracking number 26020-01-30-021). The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- The EPC Scope of Work, EPC Package Datasheet, EPC Construction Work Package, EPC review/acceptance, and Vendor Document Turnover content are produced under sibling deliverables `DEL-030-01`, `DEL-030-02`, `DEL-030-03`, `DEL-030-05`, and `DEL-030-06`, not under this deliverable.
- Detailed vendor design calculations, certified drawings, and final equipment selections are produced by the Package Vendor and are not pre-specified here beyond the source-supported facility basis.
- Package-specific values for transformer nameplate impedance, BIL, tap configuration, cooling class, secondary 4-wire neutral provisioning (347 V derivation), oil type, monitoring/protection signal list, exterior lighting layout, and installation location are `TBD` because the accessible source set does not establish confirmed package-specific values.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-030-04-001 | The vendor package shall implement a 13.8 kV → 600 V step-down distribution transformer consistent with the package name "Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V" recorded in Workbook Packages row 32 and `PACKAGE_REGISTER.csv` row `PKG-030`. | Identity check against workbook row 32 and `PACKAGE_REGISTER.csv`. |
| REQ-030-04-002 | The vendor package shall conform to the facility electrical voltage and service basis: 13.8 kV, 3-phase, 3-wire, 60 Hz, low-resistance grounded on the primary; 600 V, 3-phase, 3-wire, 60 Hz, high-resistance grounded with 5 A continuous resistor on the plant low-voltage system that the secondary feeds. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical voltages and services. | Compare vendor specification voltages, phasing, frequency, and grounding to DBM basis. |
| REQ-030-04-003 | The vendor package shall be developed from the EPC Package Scope of Work (`DEL-030-01`) and EPC Package Datasheet (`DEL-030-02`) and shall implement the EPC-defined battery limits, interfaces, and integration boundaries. Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-030-04`. | EPC integration review against `DEL-030-01` and `DEL-030-02` content. |
| REQ-030-04-004 | The vendor package shall conform to all seven applicable `PKG-030` interfaces in `INTERFACE_REGISTER.csv`: Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. Source: Workbook Packages row 32; `INTERFACE_REGISTER.csv`. | Interface conformance check against the EPC package interface requirements matrix. |
| REQ-030-04-005 | If oil-filled construction is selected, the package shall comply with CEC spacing requirements and shall minimize secondary containment requirements where practical. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers paragraph. | CEC-spacing layout review; containment review against site arrangement. |
| REQ-030-04-006 | Grounding/bonding shall comply with the facility basis: major electrical equipment connected to the ground grid at two points; a separate copper ground conductor sized per CEC connected directly to ground for distribution transformers, in addition to the grounding conductor run with power wiring. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs. | Grounding/bonding review against vendor drawings and CEC sizing. |
| REQ-030-04-007 | The 13.8 kV primary feeder interface shall accept three-conductor copper TECK cable rated 15 kV with 133 % insulation, shielded. The 600 V secondary to plant 600 V MCC shall be ACWU; single-conductor cables shall be avoided. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable types table. | Termination/bushing arrangement review against facility cable basis. |
| REQ-030-04-008 | Maintenance access (including bushing, tap-changer, oil/level, and protective device access where applicable) shall not be obstructed by cable tray or conduit routing. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray/conduit paragraphs; `INTERFACE_REGISTER.csv` `IFC-345609CB34`. | Layout review against package interface matrix. |
| REQ-030-04-009 | The vendor package shall provide the vendor package design basis and datasheet set artifact (`ART-0A27405282`) and the vendor engineered physical equipment package artifact (`ART-69E26F40CD`). Source: `ARTIFACT_REGISTER.csv` rows for `DEL-030-04`. | Artifact completeness check against `ARTIFACT_REGISTER.csv`. |
| REQ-030-04-010 | Package-specific values for impedance, BIL, tap configuration, cooling class, secondary 4-wire neutral provisioning (347 V derivation), oil type, monitoring/protection signal list, and installation location shall be either source-supported or held as `TBD`; the vendor shall not introduce facility-level requirements not present in the EPC Package Datasheet without EPC concurrence. | Source-grounding review; `TBD` items tracked as open items in the run record. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Transformer spacing, distribution-transformer grounding, ground-conductor sizing, and electrical installation basis referenced by the DBM electrical section. | Applicable as source-supported design basis; clause locations `TBD`. |
| Project electrical specifications | Voltage, distribution, grounding, cable, raceway, and 600 V MCC basis referenced by the DBM electrical section. | Applicable; specification document location `TBD`. |
| Area classification standards | Applicable to transformer installation classification where hazardous/non-hazardous areas are defined. | Applicable; package-specific area classification `TBD`. |
| IEEE/CSA distribution transformer standards | Likely applicable to a 2.5 MVA 13.8 kV / 600 V distribution transformer (e.g., for ratings, tests, and bushings). | ASSUMPTION (likely applicable); specific standard editions not stated in accessible source — `TBD`. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare vendor package identity (name, MVA, voltage class) to Workbook Packages row 32 and `PACKAGE_REGISTER.csv` row `PKG-030`. | All identity fields align with the workbook and Gate 7 register. |
| Interface conformance | Compare vendor package interface coverage to the seven `INTERFACE_REGISTER.csv` rows for `PKG-030`. | All seven interfaces are addressed or explicitly carried as `TBD` with EPC concurrence. |
| Source fidelity | Check every non-trivial requirement and value against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not asserted as requirements. |
| Responsibility split | Compare responsibility statements to `PACKAGE_REGISTER.csv` row `PKG-030` and `DELIVERABLE_REGISTER.csv` row `DEL-030-04`. | Vendor scope (engineering/design/fabrication/supply/physical package) and EPC scope (integration review, facility integration, interfaces, tie-ins) are not conflated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, voltages, and `TBD` items. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Vendor engineered physical equipment package (`ART-69E26F40CD`).
- Vendor package design basis and datasheet set (`ART-0A27405282`).
- Vendor-side test, inspection, and certification evidence prepared for EPC acceptance under `DEL-030-06` (specific list `TBD`).
- Source-gap / `TBD` list captured against vendor data resolution.

The deliverable shall cite the Gate 7 snapshot, Workbook Packages row 32, applicable Gate 7 registers, the EPC Package Scope of Work and Package Datasheet (`DEL-030-01`, `DEL-030-02`), and the DBM electrical source slices used as facility basis.
