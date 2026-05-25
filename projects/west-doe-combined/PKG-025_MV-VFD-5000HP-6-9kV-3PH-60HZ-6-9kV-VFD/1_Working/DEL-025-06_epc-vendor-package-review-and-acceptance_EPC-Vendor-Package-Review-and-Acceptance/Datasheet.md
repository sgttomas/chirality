# Datasheet — EPC Vendor Package Review and Acceptance (DEL-025-06)

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-025-06_epc-vendor-package-review-and-acceptance` |
| Name | EPC Vendor Package Review and Acceptance |
| ParentPackageID | `PKG-025` |
| PackageName | MV VFD - 5000HP, 6.9kV, 3PH, 60HZ - 6.9kV VFD |
| Discipline | Electrical |
| Type | EPC Vendor Package Acceptance |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input |
| Covers Scope Items | `SOW-0026` |
| Supports Objectives | `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010` |

Sources: `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` row `DEL-025-06_epc-vendor-package-review-and-acceptance`; Gate 7 `PACKAGE_REGISTER.csv` row `PKG-025`.

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Subject package | MV VFD — 5000 HP, 6.9 kV, 3-phase, 60 Hz | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` (PKG-025) |
| Acceptance object | Vendor-engineered MV VFD equipment package and vendor turnover documentation | `DELIVERABLE_REGISTER.csv` (DEL-025-04, DEL-025-05) |
| Acceptance basis | EPC Scope of Work (DEL-025-01), Package Datasheet (DEL-025-02), Construction Work Package (DEL-025-03) | `DELIVERABLE_REGISTER.csv` (DEL-025-01..03); `_CONTEXT.md` Scope |
| Accepting party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Providing parties | Package Vendor (engineering, design, equipment, documentation) | `PACKAGE_REGISTER.csv` (PKG-025); `DELIVERABLE_REGISTER.csv` (DEL-025-04, DEL-025-05) |
| Applicable interface types | Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports | `PACKAGE_REGISTER.csv` (PKG-025) |
| Facility MV system context | 6.9 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded; serves AC inverter-drive motors rated 5,500 hp and above | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §Medium-voltage services (line 2935) |
| Housing context | MV VFDs installed in prefabricated MV electrical buildings together with MV switchgear, MV MCCs, RVSS, UPS, etc. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §Electrical buildings (line 2973) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Acceptance precondition: SOW issued | DEL-025-01 accepted | `DELIVERABLE_REGISTER.csv` DEL-025-01 |
| Acceptance precondition: Package Datasheet issued | DEL-025-02 accepted | `DELIVERABLE_REGISTER.csv` DEL-025-02 |
| Acceptance precondition: Construction Work Package issued | DEL-025-03 accepted | `DELIVERABLE_REGISTER.csv` DEL-025-03 |
| Acceptance object: Vendor Engineered Equipment Package received | DEL-025-04 delivered by Package Vendor | `DELIVERABLE_REGISTER.csv` DEL-025-04 |
| Acceptance object: Vendor Document Turnover Package received | DEL-025-05 delivered by Package Vendor | `DELIVERABLE_REGISTER.csv` DEL-025-05 |
| Coordination mode | DECLARED (no declared upstream/downstream edges at PREPARATION) | `_DEPENDENCIES.md` |
| Maturity threshold default | INITIALIZED | `_DEPENDENCIES.md` |
| Authoring scope | EPC Integrator-led; Package Vendor provides clarifications and corrected documents | `_CONTEXT.md` ResponsibleParty |

## Construction

The deliverable is a record set, not a physical artifact. Constituent artifacts (from `_CONTEXT.md` Anticipated Artifacts):

| Artifact | Form | Source |
|---|---|---|
| Vendor document review log | Tabular log mapping each vendor submittal to review status, reviewer, comments, and disposition | `_CONTEXT.md` Anticipated Artifacts |
| Package acceptance checklist | Checklist mapping SOW / Datasheet / CWP requirements to acceptance evidence and pass/fail status | `_CONTEXT.md` Anticipated Artifacts |
| Test / inspection evidence | Aggregated factory and site test reports, inspection records, non-conformance reports, and resolutions provided by the Package Vendor and verified by EPC | `_CONTEXT.md` Anticipated Artifacts |
| Turnover evidence | Turnover package receipt, completed CWP turnover checklist items (DEL-025-03), and integration readiness sign-off | `_CONTEXT.md` Anticipated Artifacts; DEL-025-03 narrative |

Detailed acceptance criteria values (witness/hold point lists, FAT/SAT pass thresholds, document-class checklists) are not enumerated in accessible sources. Mark `TBD` until referenced (see Specification §Standards and Guidance §Conflict Table).

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- Gate 7 PROJECT_DECOMP snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `DELIVERABLE_REGISTER.csv` (rows DEL-025-01..06)
  - `PACKAGE_REGISTER.csv` (row PKG-025)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (electrical-systems and electrical-buildings sections)

TBD: `_Sources/26020-Package_Requirements.docx` was not opened during this pass (binary). Re-read in Pass 3 if/when a markdown extract is referenced. `location TBD`.
