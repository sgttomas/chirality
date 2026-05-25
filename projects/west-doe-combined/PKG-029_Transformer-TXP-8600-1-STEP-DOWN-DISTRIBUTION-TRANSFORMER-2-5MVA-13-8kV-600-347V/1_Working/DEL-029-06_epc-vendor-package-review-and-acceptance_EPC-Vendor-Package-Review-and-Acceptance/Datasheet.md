# Datasheet: DEL-029-06_epc-vendor-package-review-and-acceptance — EPC Vendor Package Review and Acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-029-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Deliverable Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| ParentPackageID | `PKG-029` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package Name | Transformer TXP-8600-1 — STEP DOWN DISTRIBUTION TRANSFORMER — 2.5MVA 13.8kV/600/347V | `PACKAGE_REGISTER.csv` |
| Workbook Row | 31 | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` |
| CoA Tracking | 26020-01-30-020 | `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable Type | EPC Vendor Package Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Covers Scope Items | `SOW-0030` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supports Objectives | `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` (ASSUMPTION: best-effort package-grouping heuristic) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Deliverable purpose | EPC Integrator review and acceptance of the Package Vendor deliverable set for `PKG-029`, providing handoff readiness against the EPC Scope of Work, Package Datasheet, and Construction Work Package. | `DELIVERABLE_REGISTER.csv` |
| Primary recipient of acceptance evidence | Project Management / Gate 5 governance (EPC Integrator delivers; human approves). | ASSUMPTION based on Gate 5 anchor framing |
| Vendor responsibility | Package engineering, package design, vendor documentation, physical equipment package. | `PACKAGE_REGISTER.csv` |
| EPC Integrator responsibility | Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration. | `PACKAGE_REGISTER.csv` |
| Equipment basis | Step-down distribution transformer, tag TXP-8600-1, 2.5 MVA, primary 13.8 kV, secondary 600/347 V. | `PACKAGE_REGISTER.csv` (package name) |
| Service basis (facility) | 13.8 kV medium-voltage backbone steps down through distribution transformers to 600 V low-voltage services (3-phase, 3-wire, 60 Hz, high-resistance grounded with 5 A continuous resistor). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §System Voltages |
| Secondary 347 V context | 347 V is the phase-to-neutral derivative of a 600 V WYE secondary used for lighting and small loads. | ASSUMPTION; no explicit 347 V utilization clause located in accessible DBM slices — `location TBD`. |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site | West Doe Deepcut (04-25/03-25 facility complex). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §Electrical Power System |
| Primary supply | 13.8 kV switchgear bus distributed radially through step-down transformers. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §Electrical Power System |
| Spacing and installation | Large oil-filled transformers spaced per CEC; installed on structural steel transformer bases. Containment requirements to be reviewed; transformer selection to limit containment where practical. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §Transformers |
| Grounding (secondary 600 V) | Each 600 V transformer grounded by a 5 A continuous high-resistance grounding resistor; MCCs include power metering and ground/resistor fault detection. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §System Grounding |
| Standby/TOU | Standby power basis is TOU generators at the 600 V MCC level with transfer switches; sizing/transfer ratings TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §Standby Power |
| Oil/dry-type selection | Liquid- vs dry-type selection for TXP-8600-1 is not stated in accessible sources. | `TBD` |
| Foundation | Transformers generally supported on precast concrete bearing foundations. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` row "Transformers" in foundations table |

## Construction (Acceptance Construct)

The acceptance review consumes vendor-produced and EPC-produced inputs and yields the acceptance evidence set named in the deliverable register.

| Acceptance input | Origin | Source |
|---|---|---|
| Vendor document submittals | Package Vendor | `PACKAGE_REGISTER.csv` (vendor owns vendor documentation) |
| EPC Scope of Work for `PKG-029` | DEL-029-01_scope-of-work | `DELIVERABLE_REGISTER.csv` |
| Package Datasheet for `PKG-029` | DEL-029-02_package-datasheet (anticipated) | `DELIVERABLE_REGISTER.csv` family pattern |
| Construction Work Package for `PKG-029` | DEL-029 family (anticipated) | `DELIVERABLE_REGISTER.csv` family pattern |
| Interface basis | `INTERFACE_REGISTER.csv` rows for `PKG-029`: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. | `INTERFACE_REGISTER.csv` |

| Acceptance output (Anticipated Artifact) | Description |
|---|---|
| Vendor document review log | Documented review of each vendor submittal with disposition and comments. |
| Package acceptance checklist | Checklist mapping EPC SOW, Package Datasheet, and Construction Work Package requirements to acceptance status. |
| Test/inspection evidence | Factory and/or site test reports, inspection records demonstrating compliance. |
| Turnover evidence | Records demonstrating package readiness for handoff to operations/commissioning. |

## References

- `_CONTEXT.md` (deliverable identity, scope, objectives mapping).
- `_REFERENCES.md` (decomposition basis, source root).
- Gate 7 PROJECT_DECOMP snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (PACKAGE_REGISTER.csv, DELIVERABLE_REGISTER.csv, INTERFACE_REGISTER.csv, ARTIFACT_REGISTER.csv, OBJECTIVE_DELIVERABLE_MAP.csv).
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Electrical Power System; System Voltages; Standby Power; Transformers; System Grounding).
- Workbook Packages row 31 (cited in `PACKAGE_REGISTER.csv`).
- `_Sources/26020-Package_Requirements.docx` — package-specific requirements file present at source root; targeted package slice for `PKG-029` not extracted during PREPARATION (`location TBD`).
