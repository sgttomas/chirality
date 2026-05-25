# Datasheet: DEL-026-06_epc-vendor-package-review-and-acceptance — EPC Vendor Package Review and Acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-026-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| DeliverableName | EPC Vendor Package Review and Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| ParentPackageID | `PKG-026` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| ParentWorkbookRow | 28 | `PACKAGE_REGISTER.csv` (row 28) |
| PackageName | Transformer TXP-8300-2 - STEP DOWN DISTRIBUTION TRANSFORMER - 20/26MVA 13.8kV/6.9kV/0.4kV | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| WBS | 02 | `PACKAGE_REGISTER.csv` |
| CoA Tracking Number | 26020-02-30-017 | `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable Type | EPC Vendor Package Acceptance | `_CONTEXT.md` |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Covers Scope Items | `SOW-0027` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supports Objectives | `OBJ-002; OBJ-004; OBJ-005; OBJ-006; OBJ-008; OBJ-009; OBJ-010` | `_CONTEXT.md` (ASSUMPTION — `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Tagged Unit | TXP-8300-2 | `_CONTEXT.md`; package name in `PACKAGE_REGISTER.csv` |
| Service Function | Step-down distribution transformer providing 13.8 kV / 6.9 kV / 0.4 kV transformation at 20/26 MVA | `PACKAGE_REGISTER.csv` package name (interpretation; technical service basis TBD) |
| Vendor Scope | Package engineering, package design, vendor documentation, and the physical equipment package | `PACKAGE_REGISTER.csv` |
| EPC Integration Scope | Facility integration including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration | `PACKAGE_REGISTER.csv` |
| Acceptance Object | The vendor-engineered transformer package (DEL-026-04) and the vendor document/turnover package (DEL-026-05) | `DELIVERABLE_REGISTER.csv` (PKG-026 deliverables) |
| Acceptance Basis | EPC Scope of Work (DEL-026-01), Package Datasheet (DEL-026-02), and Construction Work Package (DEL-026-03) | `DELIVERABLE_REGISTER.csv` (PKG-026 deliverables) |
| Anticipated Artifacts | Vendor document review and comment log; vendor package acceptance and turnover checklist; factory/shop test and inspection evidence | `ARTIFACT_REGISTER.csv` rows for `DEL-026-06` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Plant Location | Comp_and_Liquids facility (03-25) | `PACKAGE_REGISTER.csv` source reference `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| Primary Voltage (package name) | 13.8 kV | `PACKAGE_REGISTER.csv` package name |
| Secondary Voltage (package name) | 6.9 kV | `PACKAGE_REGISTER.csv` package name |
| Tertiary / Low-Voltage (package name) | 0.4 kV | `PACKAGE_REGISTER.csv` package name |
| Rated Capacity (package name) | 20/26 MVA | `PACKAGE_REGISTER.csv` package name |
| Frequency | 60 Hz (ASSUMPTION — facility standard, see `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical voltage table) | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| Neutral Grounding | TBD — package-specific grounding scheme not located in accessible sources | location TBD |
| Insulation / Cooling Class | TBD — vendor-defined | location TBD |
| Hazardous Area Classification | TBD — package-specific classification not located in accessible sources | location TBD |
| Ambient / Environmental | TBD — package-specific environmental envelope not located in accessible sources | location TBD |

## Construction

| Element | Description | Source |
|---|---|---|
| Acceptance Evidence Pack | Compiled vendor review log, acceptance/turnover checklist, and test/inspection evidence assembled by the EPC Integrator | `ARTIFACT_REGISTER.csv` rows for `DEL-026-06` |
| Vendor Document Review Log | EPC review evidence for vendor documentation and integration requirements | `ARTIFACT_REGISTER.csv` row `ART-AF00FF6B63` |
| Acceptance and Turnover Checklist | Acceptance and turnover evidence for integration into the facility | `ARTIFACT_REGISTER.csv` row `ART-28805E8681` |
| Factory/Shop Test and Inspection Evidence | Expected package test/inspection evidence; detailed requirements are source-specific where available | `ARTIFACT_REGISTER.csv` row `ART-063BACA4E7` |
| Applicable Interfaces (reviewed for acceptance) | Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports | `INTERFACE_REGISTER.csv` rows for `PKG-026` |
| Test Plan Detail (FAT/SAT/site) | TBD — package-specific test list and acceptance thresholds not located in accessible sources | location TBD |

## References

- `_CONTEXT.md` (this deliverable)
- `_REFERENCES.md` (this deliverable)
- Gate 7 Final Published PROJECT_DECOMP snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `DELIVERABLE_REGISTER.csv` (row `DEL-026-06`)
  - `PACKAGE_REGISTER.csv` (row `PKG-026`)
  - `INTERFACE_REGISTER.csv` (rows for `PKG-026`)
  - `ARTIFACT_REGISTER.csv` (rows for `DEL-026-06`)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (03-25 design basis — accessed; no PKG-026-specific transformer slice located)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (accessed for cross-facility context; no TXP-8300-2 / 13.8-6.9-0.4 kV 20/26 MVA slice located)
- Companion deliverables (PKG-026): `DEL-026-01` Scope of Work, `DEL-026-02` Package Datasheet, `DEL-026-03` Construction Work Package, `DEL-026-04` Vendor Engineered Equipment Package, `DEL-026-05` Vendor Document Turnover Package

## TBD / Open Items

- TBD: package-specific transformer ratings, impedance, vector group, taps, cooling class, BIL, partial-discharge limits, sound level, oil/dry type, and bushings — not present in accessible sources.
- TBD: factory acceptance test list and acceptance criteria for the transformer package.
- TBD: site acceptance test / energization checklist content for facility integration.
- TBD: vendor document register and submittal index used by the review log (depends on `DEL-026-05`).
