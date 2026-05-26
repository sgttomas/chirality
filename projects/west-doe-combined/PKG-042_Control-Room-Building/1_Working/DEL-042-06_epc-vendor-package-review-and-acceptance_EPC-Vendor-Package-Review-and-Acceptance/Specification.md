# Specification — DEL-042-06 EPC Vendor Package Review and Acceptance

## Scope

### Covered

- EPC-Integrator-led review of the Package Vendor's deliverables for PKG-042 Control Room Building against the EPC-authored anchor deliverables (Scope of Work, Package Datasheet, Construction Work Package).
  - Source: `DELIVERABLE_REGISTER.csv` row DEL-042-06 description; `_CONTEXT.md` Scope.
- Integration acceptance covering facility-level interfaces assigned to PKG-042 (Utility Piping; Drain/Containment; Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Communications/Network; Building HVAC/Services; Fire & Gas/Safety Systems; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports).
  - Source: `INTERFACE_REGISTER.csv` rows for PKG-042; `PACKAGE_REGISTER.csv` row PKG-042.
- Handoff-readiness acceptance: confirmation that vendor turnover evidence and document register satisfy the project handoff conditions (OBJ-010).
  - Source: `OBJECTIVE_REGISTER.csv` row OBJ-010.

### Excluded

- Authoring the EPC Scope of Work, Package Datasheet, or Construction Work Package (those are DEL-042-01/02/03).
- Performing the Package Vendor's engineering, package design, fabrication/supply, or vendor document authoring (those are DEL-042-04 and DEL-042-05).
  - Source: `PACKAGE_REGISTER.csv` row PKG-042 (Responsibility text); OBJ-004.
- Facility-wide design basis decisions outside the Control Room Building package boundary.

## Requirements

| ID | Requirement | Source / Basis |
|---|---|---|
| REQ-DEL-042-06-01 | The EPC Integrator SHALL review every Package Vendor deliverable identified in `DEL-042-04` and `DEL-042-05` and record the disposition (accept / accept-with-comment / reject / hold) in the vendor document review log. | `DELIVERABLE_REGISTER.csv` row DEL-042-06 (anticipated artifacts: vendor document review log); OBJ-004 (vendor/EPC split). |
| REQ-DEL-042-06-02 | The acceptance evaluation SHALL verify that the vendor package conforms to the EPC-issued Scope of Work (`DEL-042-01`), Package Datasheet (`DEL-042-02`), and Construction Work Package (`DEL-042-03`). | `DELIVERABLE_REGISTER.csv` row DEL-042-06 (description). |
| REQ-DEL-042-06-03 | The acceptance evaluation SHALL confirm interface compliance for each interface type tagged to PKG-042 (see Datasheet attribute "Applicable interface types"). | `INTERFACE_REGISTER.csv` PKG-042 rows; `PACKAGE_REGISTER.csv` row PKG-042. |
| REQ-DEL-042-06-04 | A package acceptance checklist SHALL be produced and signed by the EPC Integrator (with Package Vendor input) as evidence of integration acceptance. | `_CONTEXT.md` Anticipated Artifacts; ResponsibleParty. |
| REQ-DEL-042-06-05 | Test and inspection evidence SHALL be retained and indexed to specific vendor scope items and interfaces. | `_CONTEXT.md` Anticipated Artifacts; OBJ-010 (commissioning/turnover and open-item closure). |
| REQ-DEL-042-06-06 | Turnover evidence SHALL demonstrate that operability, maintainability, sparing, isolation, winterization, vendor-documentation, commissioning, and open-item closure conditions are met for handoff. | OBJ-010 (verbatim closure conditions). |
| REQ-DEL-042-06-07 | Electrical-discipline acceptance SHALL verify power, grounding/bonding, lighting, EHT, and electrical interfaces consistent with the facility electrical basis. | OBJ-005; `INTERFACE_REGISTER.csv` PKG-042 Electrical Power / Grounding / Lighting rows. ASSUMPTION: EHT/cathodic-protection applicability to this specific package is TBD until vendor scope is fixed. |
| REQ-DEL-042-06-08 | Controls/I&C acceptance SHALL verify package control interfaces, communications/network connectivity, alarm/shutdown integration, and fire & gas detection interfaces. | OBJ-006; `INTERFACE_REGISTER.csv` PKG-042 I&C/Communications/Fire & Gas rows. |
| REQ-DEL-042-06-09 | Safety/regulatory acceptance SHALL verify drain/containment, fire & gas, shutdown, and applicable code/standards conformance for the package and its interfaces. | OBJ-009; `INTERFACE_REGISTER.csv` PKG-042 Drain/Containment, Fire & Gas rows. |
| REQ-DEL-042-06-10 | Civil/structural acceptance SHALL verify foundations, supports, grading, site drainage, and access provisions associated with the Control Room Building installation. | OBJ-008; `INTERFACE_REGISTER.csv` PKG-042 Structural / Grading rows. |
| REQ-DEL-042-06-11 | Open items identified during review SHALL be tracked to closure with a documented closure record before final acceptance is granted. | OBJ-010 ("controlled open-item closure evidence"). |
| REQ-DEL-042-06-12 | The deliverable SHALL not author or modify upstream EPC anchor deliverables or vendor production deliverables; it SHALL only record review, acceptance, and integration findings. | Scope (Excluded); `PACKAGE_REGISTER.csv` Responsibility text. |

## Standards

| Standard / Authority | Applicability | Location |
|---|---|---|
| Project codes & standards basis (OBJ-009: sour-service safety, relief/flare, drain/containment, fire/gas, shutdown, environmental, emissions, regulatory) | Carried into acceptance criteria where applicable to this electrical package. | `location TBD` — DBM SEC-15 slices not parsed locally. |
| Facility electrical basis (OBJ-005) | Governs electrical interface acceptance. | `location TBD` — DBM SEC-12 slices not parsed locally. |
| Controls/I&C basis (OBJ-006) | Governs controls and instrumentation interface acceptance. | `location TBD` — DBM SEC-13/SEC-14 slices not parsed locally. |
| 26020-Package_Requirements.docx vendor-document tables | Governs the vendor document set expected for review. | `location TBD` — not parsed locally; cited by OBJ-004 and OBJ-010. |

## Verification

| Requirement | Verification Approach | Evidence |
|---|---|---|
| REQ-DEL-042-06-01 | Review of vendor document review log for completeness vs. vendor submittal index. | Vendor document review log. |
| REQ-DEL-042-06-02 | Traceability matrix between SoW/Datasheet/CWP items and vendor deliverables. | Package acceptance checklist. |
| REQ-DEL-042-06-03 | Interface compliance review per interface type. | Acceptance checklist; interface review records. |
| REQ-DEL-042-06-04 | Signature presence on acceptance checklist. | Signed acceptance checklist. |
| REQ-DEL-042-06-05 | Index of test/inspection records vs. requirements. | Test/inspection evidence package. |
| REQ-DEL-042-06-06 | Turnover record review against OBJ-010 closure conditions. | Turnover evidence package. |
| REQ-DEL-042-06-07..10 | Discipline-specific review walkdown / document review. | Discipline review notes; acceptance checklist sections. |
| REQ-DEL-042-06-11 | Open-item register closure status review. | Open-item closure log. |
| REQ-DEL-042-06-12 | Scope-bounds review of this deliverable's outputs. | Run record / scope audit. |

## Documentation

The deliverable SHALL produce, at minimum, the artifacts listed in `_CONTEXT.md` (Anticipated Artifacts):

- Vendor document review log
- Package acceptance checklist
- Test/inspection evidence
- Turnover evidence

Additional sub-artifacts (e.g., discipline review notes, open-item closure log, signed acceptance certificate) MAY be produced as supporting evidence; they SHALL be referenced from the package acceptance checklist.
