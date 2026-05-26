# Specification — DEL-043-03 Construction Work Package

## Scope

**In scope.** The Construction Work Package (CWP) for `PKG-043 Instrumentation (outside of Mechanical Packages only)` describes how the instrumentation package will be physically installed, built, inspected, turned over, and tied into the larger facility systems (`DELIVERABLE_REGISTER.csv` row 242). It covers the workbook-defined Instrumentation package under WBS 01 (`PACKAGE_REGISTER.csv` row 45) and addresses the package's recorded physical interfaces: Process Piping, Utility Piping, Electrical Power, I&C / Control Cabling, and Communications / Network (`PACKAGE_REGISTER.csv` row 45).

**Covers scope item:** `SOW-0044` — Carry the workbook-defined Instrumentation package as a distinct flat project package for WBS 01 (`SCOPE_LEDGER.csv` row 45).

**Exclusions.** Instrumentation that lies inside vendor mechanical packages is excluded by the package name "Instrumentation (outside of Mechanical Packages only)" (`PACKAGE_REGISTER.csv` row 45; `_CONTEXT.md`). Field supports, power, and communications are not included unless confirmed by package scope (`PACKAGE_REGISTER.csv` row 45). No other package-specific exclusions are stated in accessible source materials (`PACKAGE_REGISTER.csv` row 45 — `TBD; no package-specific exclusions stated in source materials`).

## Requirements

Requirements are derived strictly from accessible decomposition rows and `_CONTEXT.md`. Where construction-detail standards or site procedures would be required to set quantitative criteria, the row is marked `TBD` with the dependency named.

| # | Requirement | Basis | Status |
|---|---|---|---|
| R-01 | The CWP shall describe physical installation, construction build, inspection, turnover, and tie-in to larger facility systems for `PKG-043`. | `DELIVERABLE_REGISTER.csv` row 242 (description) | FACT |
| R-02 | The CWP shall produce three artifact classes: (a) Construction work package document, (b) Installation and tie-in workface plan, (c) Construction interface and turnover checklist. | `DELIVERABLE_REGISTER.csv` row 242 (artifacts); `_CONTEXT.md` | FACT |
| R-03 | The CWP shall address every package physical interface type recorded for `PKG-043`: Process Piping; Utility Piping; Electrical Power; I&C / Control Cabling; Communications / Network. | `PACKAGE_REGISTER.csv` row 45 | FACT |
| R-04 | The CWP shall treat field supports, power, and communications as out-of-scope unless explicitly confirmed by package scope. | `PACKAGE_REGISTER.csv` row 45 | FACT |
| R-05 | The CWP shall be owned and produced by the EPC Integrator. | `DELIVERABLE_REGISTER.csv` row 242; `_CONTEXT.md` | FACT |
| R-06 | The CWP shall demonstrate support for the associated objectives: OBJ-001, OBJ-003, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-010. | `DELIVERABLE_REGISTER.csv` row 242 (objectives column) | FACT |
| R-07 | The CWP shall reference the tagged-equipment list and package datasheet upstream deliverables (`DEL-043-01`, `DEL-043-02`) for instrument identity and design data. | ASSUMPTION (typical EPC sequencing inside `PKG-043` register rows 240, 241, 242); cross-deliverable consistency | ASSUMPTION |
| R-08 | Construction sequencing shall be expressed as a workface plan suitable for WBS 01 execution. | `PACKAGE_REGISTER.csv` row 45 (WBS 01); ASSUMPTION on workface plan structure | ASSUMPTION |
| R-09 | Inspection and test plan (ITP) acceptance criteria for instrumentation construction shall conform to project specifications and applicable codes. | TBD — applicable instrumentation construction standards not enumerated in accessible source slices | TBD |
| R-10 | Hazardous-area installation requirements shall conform to the facility area classification basis. | TBD — area classification not in accessible source slices | TBD |
| R-11 | Turnover documentation shall align with the facility commissioning and turnover system. | ASSUMPTION; turnover checklist is an anticipated artifact (`_CONTEXT.md`) | ASSUMPTION |

## Standards

Accessible source slices do not enumerate clause-level standards for instrumentation construction. Likely-applicable bodies of practice are listed conservatively and remain `location TBD`:

| Standard / Body of Practice | Applicability | Source / Location |
|---|---|---|
| Project-issued construction specifications for instrumentation | Governs ITP, installation tolerances, and material control | location TBD |
| Facility area-classification and electrical installation basis | Governs hazardous-area installation, sealing, and grounding for I&C / power tie-ins | location TBD |
| ISA / IEC instrumentation installation practice | ASSUMPTION: typically applicable to instrument mounting, tubing, calibration, loop checking | location TBD |
| Site QA/QC and inspection procedures | Governs witness/hold points and ITP execution | location TBD |
| Site turnover and commissioning procedures | Governs handover checklists and system boundary acceptance | location TBD |

## Verification

| Requirement | Verification Approach | Records |
|---|---|---|
| R-01 | Review of CWP document content for the full installation→tie-in lifecycle. | CWP document; review record |
| R-02 | Document inventory check confirming the three artifact classes exist and are internally consistent. | Artifact register entry; review record |
| R-03 | Interface coverage matrix mapping each PKG-043 interface type to CWP sections, workface activities, and turnover items. | Interface coverage matrix |
| R-04 | Scope-boundary statement reviewed against `PACKAGE_REGISTER.csv` row 45. | Boundary review note |
| R-05 | Responsible-party attestation captured in CWP front matter. | Attestation record |
| R-06 | Objective-traceability matrix linking CWP sections to each listed objective. | Traceability matrix |
| R-07 | Cross-references to `DEL-043-01` and `DEL-043-02` present and resolvable. | Cross-reference list |
| R-08 | Workface plan reviewed against WBS 01 deliverable boundary. | Workface plan |
| R-09 | ITP review against governing project specifications and codes (post-source resolution). | ITP review record (TBD until R-09 closed) |
| R-10 | Hazardous-area conformance review (post-source resolution). | Hazardous-area review record (TBD) |
| R-11 | Turnover checklist mapped to commissioning system entries. | Turnover checklist |

## Documentation

Required artifacts (from `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row 242 artifacts column):

- Construction work package (master CWP document).
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.

Supporting records produced during execution:

- Interface coverage matrix (R-03 verification).
- Objective-traceability matrix (R-06 verification).
- ITP and inspection records (R-09 verification — `TBD` until governing standards resolved).
- Turnover acceptance records (R-11 verification).
