# Specification: DEL-036-03_construction-work-package

## Scope

This deliverable specifies the EPC Integrator-authored Construction Work Package for `PKG-036` — the 6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1). The Construction Work Package defines how the vendor-engineered package will be physically installed, built, inspected, turned over, and tied into the larger facility systems. It covers integration, tie-ins, constructability, and facility-level integration owned by the EPC Integrator. It does NOT cover vendor package engineering, package design, vendor documentation, or the physical equipment package itself (Package Vendor scope; see `DEL-036-04`).

- Covers scope item: `SOW-0037` (`DELIVERABLE_REGISTER.csv`).
- Mandatory artifacts: construction work package, installation and tie-in workface plan, construction interface and turnover checklist (`ARTIFACT_REGISTER.csv`).

## Requirements

| ID | Requirement | Source | Status |
|---|---|---|---|
| REQ-036-03-001 | The Construction Work Package shall be authored by the EPC Integrator. | `PACKAGE_REGISTER.csv` row `PKG-036`; `DELIVERABLE_REGISTER.csv` | FACT |
| REQ-036-03-002 | The Construction Work Package shall include a construction work package narrative, an installation and tie-in workface plan, and a construction interface and turnover checklist. | `ARTIFACT_REGISTER.csv` `ART-5AF99634D9`, `ART-0CFB00EEF8`, `ART-A5CFBCEAB9` | FACT |
| REQ-036-03-003 | Construction installation shall reflect that this is a shop-prefabricated modular electrical building. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-building-type table | FACT |
| REQ-036-03-004 | The construction approach shall provide for bottom entry of incoming and outgoing power cables; the building shall be installed on piles, elevated to provide space beneath the building for incoming cable trays. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph | FACT |
| REQ-036-03-005 | The construction approach shall result in an n+1 HVAC system installed and commissioned. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph | FACT |
| REQ-036-03-006 | Field wiring shall use TECK and ACIC cables; EMT conduit shall be used between adjacent equipment; an outdoor GFI receptacle shall be installed; equipment doors shall be sized or include removable transom sections to permit removal of the largest equipment. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph | FACT |
| REQ-036-03-007 | All major electrical equipment within the building shall be directly connected to the ground grid at two points; ground wells shall be provided at the electrical building with bolted ground test points; above-grade grounding conductors shall be green insulated ground wires in PVC conduit where mechanical protection is required; ground connections shall be compression type. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Grounding paragraph | FACT |
| REQ-036-03-008 | The Construction Work Package shall include workface planning evidence for tie-in to each applicable facility system: utility piping; drain/containment; electrical power; grounding/bonding; area/exterior lighting; I&C/control cabling; communications/network; building HVAC/services; fire & gas/safety systems; maintenance access; grading/site drainage/spill containment; structural/foundations/supports. | `INTERFACE_REGISTER.csv` (12 rows for `PKG-036`); `PACKAGE_REGISTER.csv` row `PKG-036` | FACT |
| REQ-036-03-009 | The Construction Work Package shall include a turnover checklist that records construction-interface acceptance and handoff to commissioning. | `ARTIFACT_REGISTER.csv` `ART-A5CFBCEAB9` | FACT |
| REQ-036-03-010 | Detailed inspection, test, and acceptance criteria for installed equipment shall be defined consistent with detailed electrical design. | Source gap | ASSUMPTION — derived from interpretation rule; specifics TBD |

## Standards

| Standard / governing document | Applicability | Source / location |
|---|---|---|
| Project Design Basis Memorandum (Deepcut) — Electrical design basis sections | Electrical building configuration, grounding, cable systems, power distribution | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| West Doe Project workbook Packages row 38 | Package identity, scope, and interface facts | `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 38 |
| `26020-Package_Requirements.docx` | Project-wide package requirements; package-specific slice for `PKG-036` not located in accessible source | `_Sources/26020-Package_Requirements.docx` — location TBD |
| Canadian Electrical Code (CEC) | Sizing/grounding referenced by DBM | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (referenced by DBM); clause location TBD |
| TOU electrical standards | Referenced by DBM for standby power and TOU-typical bases | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (referenced by DBM); standard location TBD |

## Verification

| Requirement | Verification approach | Evidence |
|---|---|---|
| REQ-036-03-001 / REQ-036-03-002 | Document review of completed Construction Work Package, workface plan, and turnover checklist by EPC Integrator. | Artifact set per `ARTIFACT_REGISTER.csv` rows for `DEL-036-03`. |
| REQ-036-03-003 / REQ-036-03-004 | Construction inspection: confirm shop-prefabricated module set on piled foundation with bottom-entry cable space below. | Inspection record; turnover checklist line item. |
| REQ-036-03-005 | HVAC commissioning test confirming n+1 capability. | Commissioning record. |
| REQ-036-03-006 | Field walkdown confirming cable types, EMT routing, GFI receptacle, door/transom sizing. | Walkdown checklist. |
| REQ-036-03-007 | Ground continuity / resistance test; visual confirmation of two-point ground connection and ground-well bolted test points. | Ground test record. |
| REQ-036-03-008 | Interface tie-in walkdowns per interface type; each interface row from `INTERFACE_REGISTER.csv` mapped to a workface plan section. | Workface plan section index and tie-in walkdown record. |
| REQ-036-03-009 | Turnover checklist signed by EPC Integrator and accepted by commissioning. | Signed checklist `ART-A5CFBCEAB9`. |
| REQ-036-03-010 | Inspection and test plan referenced from detailed design. | TBD pending detailed-design ITP. |

## Documentation

- Construction work package narrative — `ART-5AF99634D9`.
- Installation and tie-in workface plan — `ART-0CFB00EEF8`.
- Construction interface and turnover checklist — `ART-A5CFBCEAB9`.
- Construction inspection, test, and walkdown records (per verification above).
- Ground test record; HVAC commissioning record.
