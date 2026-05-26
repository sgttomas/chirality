# Specification: DEL-042-03 — Construction Work Package (Control Room Building)

## Scope

**In scope:** EPC Integrator-authored Construction Work Package (CWP) covering physical installation, on-site construction, inspection, system tie-in, and turnover of the PKG-042 Control Room Building into the larger process facility. The CWP must address all eleven applicable interface types listed in the Datasheet. (SourceRef: DELIVERABLE_REGISTER.csv DEL-042-03; INTERFACE_REGISTER.csv PKG-042 rows.)

**Excluded:** Package engineering, package design, vendor documentation, and the physical equipment package itself — these are Package Vendor responsibilities, not EPC Integrator construction work package scope. (SourceRef: PACKAGE_REGISTER.csv PKG-042 ResponsibilityModel.)

## Requirements

| ReqID | Requirement | Basis / SourceRef |
|---|---|---|
| R-042-03-01 | The CWP SHALL describe how the Control Room Building package is physically installed, built, inspected, turned over, and tied into the larger facility systems. | DELIVERABLE_REGISTER.csv DEL-042-03 (scope text) |
| R-042-03-02 | The CWP SHALL include a construction work package artifact (ART-6AD15AE851). | ARTIFACT_REGISTER.csv |
| R-042-03-03 | The CWP SHALL include an installation and tie-in workface plan (ART-9882790698). | ARTIFACT_REGISTER.csv; DELIVERABLE_REGISTER.csv anticipated artifacts |
| R-042-03-04 | The CWP SHALL include a construction interface and turnover checklist. | DELIVERABLE_REGISTER.csv anticipated artifacts |
| R-042-03-05 | The CWP SHALL address tie-in/installation for each of the eleven applicable interface types listed in INTERFACE_REGISTER.csv for PKG-042. | INTERFACE_REGISTER.csv (PKG-042) |
| R-042-03-06 | The CWP SHALL respect the responsibility split: EPC Integrator owns construction integration; Package Vendor owns engineered package supply. | PACKAGE_REGISTER.csv PKG-042 ResponsibilityModel |
| R-042-03-07 | The CWP SHALL demonstrate coverage of SOW-0043 and trace to objectives OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010. | SCOPE_LEDGER.csv SOW-0043; DELIVERABLE_REGISTER.csv DEL-042-03 |
| R-042-03-08 | ASSUMPTION: The CWP SHALL conform to project-level construction execution standards (HSE, QC, permit-to-work). Specific governing standards: location TBD — not present in accessible source registers. | ASSUMPTION |

## Standards

| Standard | Applicability | Location |
|---|---|---|
| Project-level EPC construction standards | Governs construction execution | location TBD (not present in accessible registers) |
| Discipline (Electrical) installation codes (e.g., NEC, IEEE, area classification practice) | Governs electrical installation and grounding tie-ins | location TBD — ASSUMPTION based on Discipline=Electrical in PACKAGE_REGISTER.csv |
| Site-specific permit-to-work and turnover procedures | Governs construction execution and handover | location TBD |

## Verification

| ReqID | Verification Approach |
|---|---|
| R-042-03-01 | Document review of CWP narrative against DELIVERABLE_REGISTER.csv scope text |
| R-042-03-02..04 | Artifact presence check (three named artifacts produced and stored in deliverable folder) |
| R-042-03-05 | Interface coverage matrix: each of the 11 PKG-042 InterfaceIDs mapped to a tie-in step and acceptance check |
| R-042-03-06 | Responsibility traceability table against PACKAGE_REGISTER.csv |
| R-042-03-07 | Trace matrix from CWP sections to SOW-0043 and listed OBJ-* IDs |
| R-042-03-08 | Standards-applicability review once governing standards are confirmed (TBD) |

## Documentation

Required documentation deliverables (anticipated artifacts; SourceRef: DELIVERABLE_REGISTER.csv):

- Construction work package (ART-6AD15AE851)
- Installation and tie-in workface plan (ART-9882790698)
- Construction interface and turnover checklist
- Interface coverage matrix (R-042-03-05 evidence)
- Responsibility traceability table (R-042-03-06 evidence)
- Scope/objective trace matrix (R-042-03-07 evidence)
