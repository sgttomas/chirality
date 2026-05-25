# Datasheet: DEL-038-05 — Vendor Document Turnover Package

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-038-05_vendor-document-turnover-package` | `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` |
| Name | Vendor Document Turnover Package | `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` |
| ParentPackageID | `PKG-038` | `_CONTEXT.md`; Gate 7 `PACKAGE_REGISTER.csv` |
| Package Name | 600V ELECTRICAL BUILDING (820-1) | Gate 7 `PACKAGE_REGISTER.csv` (workbook row 40) |
| Workbook Row | 40 | Gate 7 registers |
| Discipline | Electrical | Gate 7 `PACKAGE_REGISTER.csv` |
| Type | Vendor Document Turnover | `_CONTEXT.md` |
| ResponsibleParty | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | Gate 7 `DELIVERABLE_REGISTER.csv` |
| Covers ScopeItem | `SOW-0039` | Gate 7 `DELIVERABLE_REGISTER.csv` |
| Supports Objectives | `OBJ-001; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010` | Gate 7 `DELIVERABLE_REGISTER.csv` |
| Coordination Mode | DECLARED | `_DEPENDENCIES.md` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package WBS | 01 | Gate 7 `PACKAGE_REGISTER.csv` |
| Workbook Package ID | 26020-01-30-029 | Gate 7 `PACKAGE_REGISTER.csv` |
| Vendor scope category | Package Vendor production-unit documentation | Gate 7 `DELIVERABLE_REGISTER.csv` |
| EPC Integrator role | Interface/integration review of vendor documentation | Gate 7 `DELIVERABLE_REGISTER.csv` |
| Sibling deliverables (same package) | DEL-038-01 SOW; DEL-038-02 Package Datasheet; DEL-038-03 CWP; DEL-038-04 Vendor Engineered Equipment Package; DEL-038-06 EPC Vendor Package Review and Acceptance | Gate 7 `DELIVERABLE_REGISTER.csv` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Governing electrical design context | Facility electrical buildings shall be prefabricated, modular, HVAC-controlled, bottom-cable-entry buildings housing MV switchgear, MCCs, UPS, distribution transformers, panelboards, control panels, and network racks | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Sec. "Electrical Buildings" (around L2971-2999) |
| Governing codes/regulators (parent electrical scope) | CSA C22.1-21 Canadian Electrical Code; BC provincial/local electrical codes; electrical inspection authority designated by Tourmaline Oil Corp; applicable standards from CSA, API, IEEE, ISA, NEMA, WorkSafeBC, Technical Safety BC, BCER | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2866 |
| Detailed vendor documentation list (titles, revisions, due dates) | TBD — not enumerated in available source slices | location TBD |
| Submittal workflow (issue/review/approval cycles) | TBD — not specified in available source slices | location TBD |
| Turnover record set composition | TBD — not enumerated in available source slices | location TBD |

## Construction

| Component | Value | Source |
|---|---|---|
| Anticipated artifact: Vendor document register | Required | `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` |
| Anticipated artifact: Vendor document submittals | Required | `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` |
| Anticipated artifact: Source vendor document table rows (as artifacts where available) | Required where available | `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` |
| Anticipated artifact: Turnover records | Required | `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` |
| Individual source document rows | Carried as artifacts/evidence, not separate deliverables | Gate 7 `DELIVERABLE_REGISTER.csv` notes column |

## References

- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv`
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/OBJECTIVE_DELIVERABLE_MAP.csv`
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Electrical Buildings; Electrical design basis sections)
- Workbook: `_Sources/26020-Package_Requirements.docx` (package-specific row not located for PKG-038; ASSUMPTION: standard package-requirements document applies)
