# Specification: DEL-039-03_construction-work-package

## Scope

This specification governs the EPC Integrator-authored Construction Work Package for `PKG-039`, the 600V ELECTRICAL BUILDING (850-1) package serving the Inlet/Sales Compressor electrical-distribution function. The Construction Work Package is the mandatory Gate 5 EPC anchor deliverable that describes how the prefabricated modular electrical building will be physically installed, built, inspected, turned over, and tied into the larger facility systems.

The package is a vendor-owned Electrical package under WBS 01 (CoA 26020-01-30-030). The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Field construction is assigned to Tourmaline Oil Corporation per the DBM Construction Responsibility table.

Exclusions:

- Vendor-owned package internal fabrication, factory acceptance testing, and shop assembly are not re-specified here; they are referenced as preconditions to site delivery.
- Coordinate-level building layout against plot plan CIV-235633-5002 is `TBD` because the plot plan drawing is not in the publication input package.
- Package-specific workface manpower loading, lift studies, scaffolding plans, and sequencing detail are `TBD` because no accessible PKG-039-specific vendor extraction is available in the deliverable folder.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-039-03-001 | The Construction Work Package shall identify `PKG-039`, workbook row 41, WBS 01, CoA tracking number 26020-01-30-030, discipline Electrical, and package name "600V ELECTRICAL BUILDING (850-1)." Source: Workbook Packages row 41; `PACKAGE_REGISTER.csv`. | Identity review against workbook row and Gate 7 registers. |
| REQ-039-03-002 | The Construction Work Package shall preserve the responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces; field construction is in Tourmaline scope per the DBM Construction Responsibility table. Source: `PACKAGE_REGISTER.csv` row `PKG-039`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Construction Responsibility". | Responsibility-statement review against Gate 7 register and DBM. |
| REQ-039-03-003 | The Construction Work Package shall include the twelve applicable interface facts for PKG-039 (Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports) and treat each as a construction tie-in/turnover scope item. Source: Workbook Packages row 41; `INTERFACE_REGISTER.csv`. | Interface-matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-039`. |
| REQ-039-03-004 | The Construction Work Package shall require the electrical building to be installed as a prefabricated, modular building elevated on piles with bottom cable entry, located in a general-purpose area, and shall provide for n + 1 HVAC operation. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Electrical Buildings" paragraph. | Construction-package review against DBM electrical-building basis. |
| REQ-039-03-005 | The Construction Work Package shall require building cable systems to use TECK and ACIC cables, EMT conduit between adjacent equipment, an outdoor GFI receptacle for exterior maintenance, and equipment doors sized for, or with removable transoms allowing, removal of the largest equipment. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings wiring paragraph. | Cable/conduit and door-opening verification against DBM. |
| REQ-039-03-006 | The Construction Work Package shall require major electrical equipment to be directly connected to the ground grid at two points and shall provide ground wells at the electrical building with bolted ground connections at test points for maintenance and operational testing. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding/bonding paragraph. | Grounding test/inspection record review. |
| REQ-039-03-007 | The Construction Work Package shall apply Tourmaline field construction scope per the DBM Construction Responsibility table to grading, piling, foundations, off-loading, setting modules on foundations, mechanical hookup, installation of shipped-loose items, structural supports, home-run cable installation, and electrical terminations. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Construction Responsibility". | Field construction scope review against DBM table. |
| REQ-039-03-008 | The Construction Work Package shall require joint planning for tie-ins to existing or related facilities and shall record tie-in timing as the project progresses. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, construction-responsibility paragraph. | Tie-in plan review. |
| REQ-039-03-009 | The Construction Work Package shall require installation, testing, and inspection of electrical equipment per the inspection authority designated by Tourmaline Oil Corp and applicable CSA C22.1 / project specifications, and shall require all installed electrical equipment to be new, of current design, and third-party certified by CSA, ULc, FM, ETL, or another acceptable NRTL. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical inspection/certification paragraphs. | Inspection authority and certification record review. |
| REQ-039-03-010 | The Construction Work Package shall produce a construction interface and turnover checklist covering the twelve PKG-039 interface facts. Source: `ARTIFACT_REGISTER.csv` `ART-17C0FB26AE`; Workbook Packages row 41. | Checklist completeness review against `INTERFACE_REGISTER.csv` rows for PKG-039. |
| REQ-039-03-011 | The Construction Work Package shall produce an installation and tie-in workface plan as construction tie-in evidence covering installing/building the package and connecting it to adjacent process, utility, electrical, controls, civil, structural, and safety systems as applicable. Source: `ARTIFACT_REGISTER.csv` `ART-93DCDB7068`. | Workface plan review against the artifact register description. |
| REQ-039-03-012 | The Construction Work Package shall identify source gaps for coordinate-level building location (plot plan CIV-235633-5002 not available), package-specific workface manpower loading, lift studies, scaffolding plans, sequencing, and turnover-checklist line items as `TBD` rather than invented values. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, plot-plan gap paragraph; `_REFERENCES.md` missing-references section. | Gap review before construction handoff. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| CSA C22.1-21 Canadian Electrical Code; applicable BC provincial and local electrical codes; requirements of the electrical inspection authority designated by Tourmaline Oil Corp | Governs installation, testing, and inspection of electrical equipment | Applicable as source-supported design/installation basis; clause locations TBD. |
| CSA A23.1/A23.2 | Concrete materials, construction, and testing for foundations supporting the elevated electrical building | Applicable to civil/structural construction supporting the package (DBM structural section); clause locations TBD. |
| Project electrical specifications (Propak/Tourmaline) | Voltage, MCC, grounding, cable, raceway, and inspection basis referenced by DBM electrical section | Applicable; document location TBD. |
| Third-party certification by CSA, ULc, FM, ETL, or another NRTL | All supplied electrical equipment shall be new, of current design, and certified by an acceptable NRTL | Applicable per DBM electrical paragraph. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, interface facts, and objective association | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare construction work package identity fields to workbook row 41 and Gate 7 registers | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare construction tie-in/turnover checklist coverage to `INTERFACE_REGISTER.csv` rows for `PKG-039` | All twelve interface facts addressed. |
| Building configuration | Compare building installation requirements (modular; elevated on piles; bottom cable entry; general-purpose area; n + 1 HVAC; TECK/ACIC cables; EMT between adjacent equipment; outdoor GFI; equipment-door sizing) to DBM electrical-buildings paragraph | All DBM electrical-building constructional requirements represented. |
| Grounding installation | Inspect ground-grid two-point connections and ground-well test points per DBM grounding/bonding paragraph | Two-point grounding and ground-well test connections in place. |
| Field construction scope | Compare field construction tasks to DBM "Construction Responsibility" table | Scope items appear in workface plan and turnover checklist. |
| Inspection and certification | Inspect equipment certification records (CSA/ULc/FM/ETL or other NRTL) and inspection-authority sign-off | Records complete per DBM electrical inspection paragraph. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices | Unsupported values are marked `TBD` or `ASSUMPTION`, not asserted. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package identity, interfaces, responsibilities, and `TBD` items | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Construction work package (per `ART-298F584585`).
- Installation and tie-in workface plan (per `ART-93DCDB7068`).
- Construction interface and turnover checklist (per `ART-17C0FB26AE`).
- Source-supported building installation, grounding, cable, inspection, and tie-in basis.
- Source-gap / `TBD` list for human or vendor resolution (coordinate-level location, workface detail, turnover-checklist line items).

The deliverable shall cite the Gate 7 snapshot, workbook row 41, applicable Gate 7 registers, and the DBM electrical and construction-responsibility source slices used for construction basis.
