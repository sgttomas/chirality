# Specification: DEL-035-03_construction-work-package

## Scope

This specification governs the EPC Integrator Construction Work Package for `PKG-035` (13.8kV SWITCHGEAR ELECTRICAL BUILDING (810-1)). It defines requirements for physically installing, tying in, inspecting, turning over, and integrating the vendor-supplied Electrical Building 810-1 and its 13.8 kV main switchgear into the West Doe Deepcut facility.

In scope:
- Receipt, transport, setting, and anchoring of the shop-built Electrical Building 810-1 on prepared pile foundations.
- Construction and tie-in of incoming utility feed from the 25 kV / 13.8 kV utility transformer to the 13.8 kV switchgear and outgoing radial 13.8 kV feeders to dependent electrical buildings.
- Grounding/bonding installation, cable tray and conduit installation, HVAC commissioning, and energization sequence within the EPC Integrator scope.
- Construction inspection, integration interface verification, and turnover documentation for PKG-035.

Out of scope:
- Package Vendor engineering, design, fabrication, and vendor documentation (covered by `DEL-035-04_vendor-engineered-equipment-package` and `DEL-035-05_vendor-document-turnover-package`).
- Detailed package datasheet content (covered by `DEL-035-02_package-datasheet`).
- EPC vendor package review and acceptance (covered by `DEL-035-06_epc-vendor-package-review-and-acceptance`).

## Requirements

| Req ID | Requirement | Status | Source |
|---|---|---|---|
| REQ-035-03-01 | The Construction Work Package shall implement the EPC Integrator share of facility integration, interfaces, tie-ins, constructability, and procurement/construction coordination for PKG-035. | NORMATIVE | `PACKAGE_REGISTER.csv` row `PKG-035` |
| REQ-035-03-02 | Electrical Building 810-1 shall be installed as a prefabricated modular building, elevated and installed on piles to provide bottom-entry space for cabling. | NORMATIVE | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraphs |
| REQ-035-03-03 | Building 810-1 shall be sited in a general-purpose area as a prefabricated electrical building per facility area classification. | NORMATIVE | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, area classification paragraph |
| REQ-035-03-04 | Incoming 25 kV / 13.8 kV utility supply to the 13.8 kV switchgear shall be installed such that the 13.8 kV bus serves as the plant main power distribution center sized for full facility scope. | NORMATIVE | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, facility electrical system paragraph |
| REQ-035-03-05 | Outgoing 13.8 kV feeders from the switchgear shall be installed for radial distribution through step-down transformers to the dependent electrical buildings (6.9 kV, 4.16 kV, 600 V buildings) per DBM. | NORMATIVE | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, radial distribution paragraph |
| REQ-035-03-06 | 13.8 kV medium-voltage cables shall be three-conductor copper TECK cable rated 15 kV with 133 percent insulation, shielded. | NORMATIVE | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable schedule |
| REQ-035-03-07 | All major electrical equipment in the building (switchgear, transformers if interfacing) shall be directly connected to the ground grid at two points; ground wells with bolted test points shall be installed at the electrical building. | NORMATIVE | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs |
| REQ-035-03-08 | Above-grade grounding conductors shall be green insulated ground wires in PVC conduit where mechanical protection is required; ground connections shall be compression type. | NORMATIVE | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs |
| REQ-035-03-09 | Cable tray and conduit routing shall not interfere with maintenance access; field-run cable tray is limited to field-constructed portions of the plant. | NORMATIVE | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray paragraphs |
| REQ-035-03-10 | Equipment doors of Building 810-1 shall be sized for, or include removable transom sections to allow, removal of the largest equipment housed in the building. | NORMATIVE | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraphs |
| REQ-035-03-11 | The building HVAC shall be commissioned as an n+1 system prior to energization so that failure or maintenance of one unit does not interrupt heating/cooling. | NORMATIVE | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings HVAC paragraph |
| REQ-035-03-12 | An outdoor GFI receptacle shall be provided for exterior maintenance at the building. | NORMATIVE | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph |
| REQ-035-03-13 | All twelve interface types asserted at PKG-035 in `INTERFACE_REGISTER.csv` (Utility Piping; Drain/Containment; Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Communications/Network; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports) shall be coordinated and have a documented construction tie-in plan and turnover record. | NORMATIVE | Workbook Packages row 37; `INTERFACE_REGISTER.csv` rows for `PKG-035` |
| REQ-035-03-14 | Energization of the 13.8 kV bus shall be planned as the gating tie-in for downstream electrical buildings; construction sequence shall reflect this dependency. | NORMATIVE | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, radial distribution paragraph |
| REQ-035-03-15 | The Construction Work Package shall deliver, at minimum, the anticipated artifacts: construction work package, installation and tie-in workface plan, and construction interface and turnover checklist. | NORMATIVE | `DELIVERABLE_REGISTER.csv` row `DEL-035-03_construction-work-package` |

## Standards

| Standard / Basis | Applicability | Location |
|---|---|---|
| Canadian Electrical Code (CEC), spacing and installation requirements | Cited by DBM for electrical equipment installation. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, CEC references; clause location TBD in CEC itself |
| OGAOM (Oil and Gas Activities Operations Manual) Sec. 9.6.15 | Separation distance between fired heaters and control room/electrical buildings (25 m / 82 ft) — applicable to siting of Building 810-1 relative to fired equipment. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 298 |
| West Doe Deepcut Design Basis Memorandum (DBM), electrical design basis | Authoritative project basis for electrical installation, grounding, cable, and building construction. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Section "Electrical" and Electrical Buildings paragraphs |
| Package Vendor documentation (FAT/SAT, settings, drawings) | Required for installation, tie-in, and turnover; specific documents TBD pending Package Vendor submittals. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, vendor document references; location TBD |

## Verification

| Req ID | Verification approach |
|---|---|
| REQ-035-03-01 | Documentation review confirming EPC Integrator construction scope coverage against `PACKAGE_REGISTER.csv` responsibility model. |
| REQ-035-03-02, REQ-035-03-10 | Installation inspection of building setting on piles, bottom-entry provisions, and door/transom sizing. |
| REQ-035-03-03 | Area classification verification at Building 810-1 site. |
| REQ-035-03-04, REQ-035-03-05, REQ-035-03-14 | Pre-energization checks, protection coordination review, sequenced energization test, and witness of incoming/outgoing feeder integrity. |
| REQ-035-03-06 | Cable acceptance test (insulation/megger and high-pot per project test plan); confirmation of TECK type and rating. |
| REQ-035-03-07, REQ-035-03-08 | Ground continuity test, two-point connection verification, ground well inspection. |
| REQ-035-03-09 | Walk-down inspection of cable tray/conduit routing against maintenance-access criteria. |
| REQ-035-03-11 | HVAC commissioning test demonstrating n+1 redundancy. |
| REQ-035-03-12 | Inspection of outdoor GFI receptacle and GFI trip test. |
| REQ-035-03-13 | Construction interface and turnover checklist completed for each of the twelve PKG-035 interfaces. |
| REQ-035-03-15 | Verification that all three anticipated artifacts exist and are accepted. |

## Documentation

The following artifacts shall be produced and retained for this deliverable:

- Construction work package (master document).
- Installation and tie-in workface plan.
- Construction interface and turnover checklist (per PKG-035 interface type).
- Energization sequence and pre-energization checklist record.
- Grounding/bonding installation and test records.
- Cable installation and acceptance test records.
- HVAC commissioning record.
- Inspection records and non-conformance reports (NCRs) and resolutions.
- Turnover package to operations.

Source references:
- `DELIVERABLE_REGISTER.csv` row `DEL-035-03_construction-work-package` (anticipated artifacts).
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis sections.
