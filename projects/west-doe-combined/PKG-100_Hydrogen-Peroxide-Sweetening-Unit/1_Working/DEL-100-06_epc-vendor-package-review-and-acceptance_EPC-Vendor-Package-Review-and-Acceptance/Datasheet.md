# Datasheet — DEL-100-06 EPC Vendor Package Review and Acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-100-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md` Identity |
| Deliverable Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md` Identity |
| Parent Package | `PKG-100` — Hydrogen Peroxide Sweetening Unit | `_CONTEXT.md` Identity; `PACKAGE_REGISTER.csv` row PKG-100 |
| Workbook Row | 63 (WBS 03) | `PACKAGE_REGISTER.csv` row PKG-100 |
| Discipline | Mechanical | `_CONTEXT.md` Identity |
| Deliverable Type | EPC Vendor Package Acceptance | `_CONTEXT.md` Identity |
| Responsible Party | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md` Identity |
| Covers Scope Items | `SOW-0107`, `SOW-0108`, `SOW-0109`, `SOW-0110` | `_CONTEXT.md` Covers Scope Items; `SCOPE_LEDGER.csv` |
| Supports Objectives | `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` | `_CONTEXT.md` Supports Objectives |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Object Under Review | Vendor-supplied Hydrogen Peroxide Sweetening Unit package (Hydrogen Peroxide Pumps, Hydrogen Peroxide Reactors, Static Mixer, and ancillary equipment per PFD) | `SCOPE_LEDGER.csv` SOW-0108; `SCOPE_LEDGER.csv` SOW-0109 |
| Review Authority | EPC Integrator | `_CONTEXT.md` Identity; `PACKAGE_REGISTER.csv` row PKG-100 (responsibility model) |
| Acceptance Reference Documents | EPC Scope of Work (`DEL-100-01`); Package Datasheet (`DEL-100-02`); Construction Work Package (`DEL-100-03`); Vendor Engineered Equipment Package (`DEL-100-04`); Vendor Document Turnover Package (`DEL-100-05`) | `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` PKG-100 deliverable rows |
| Interface Surfaces Covered by Acceptance | Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports | `INTERFACE_REGISTER.csv` (PKG-100 rows); `PACKAGE_REGISTER.csv` PKG-100 |
| Anticipated Artifacts | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence | `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` DEL-100-06 |
| Turnover Destination | EPC Integrator facility integration / project handoff | ASSUMPTION (per OBJ-010 closure-condition framing in `OBJECTIVE_REGISTER.csv`) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Package Process Function (context for review) | Sour water → static mixer → Hydrogen Peroxide Reactors; H2O2 injected from H2O2 tank via H2O2 pumps; treated water routed to produced-water storage tanks | `PACKAGE_REGISTER.csv` PKG-100; `SCOPE_LEDGER.csv` SOW-0108 |
| Package Capacity (acceptance basis) | 24,154 BBL/D treatment capacity; 400 BBL hydrogen peroxide storage tank; pump capacity TBC (Vendor to design) | `SCOPE_LEDGER.csv` SOW-0110 |
| Package Operating Conditions (acceptance basis) | Sour water temperature 9 °C; sour water pressure 340.54 kPag; sour water flow 160 m3/h (24,154 BBL/D) | `SCOPE_LEDGER.csv` SOW-0110 |
| Package Design Ambient | Ambient temperature −40 °C min / +35 °C max; design conditions TBC | `SCOPE_LEDGER.csv` SOW-0110 |
| Electrical Driver Basis (acceptance basis) | All pumps driven by 575 V / 3 PH / 60 Hz motors; DOL or VFD starting; local control (H-O-A or On-Off); fed from 600 V MCC | `SCOPE_LEDGER.csv` SOW-0110 |
| EPC-Scope Tie-In Items "By Others" (interface acceptance basis) | Interconnecting piping; DCS integration; foundations; electrical supply to MCC | `SCOPE_LEDGER.csv` SOW-0110 |
| Review Window | TBD (project schedule not in accessible references) | TBD |
| Acceptance Sign-Off Authority | Human approver per K-AUTH-1; specific role TBD | TBD |

## Construction

| Item | Value | Source |
|---|---|---|
| Form of Deliverable | Review-and-acceptance evidence pack (logs, checklists, inspection/test evidence, turnover evidence) — not a physical artifact | `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` DEL-100-06 (Notes: "EPC-integrator review and acceptance evidence") |
| Storage Location | This deliverable folder (`DEL-100-06_...`); referenced upstream evidence remains in its owning deliverable folder | ASSUMPTION (filesystem-native convention; not stated in accessible references) |
| Evidence Indexing Convention | Each acceptance-checklist item references the underlying source artifact (`DEL-100-0n` deliverable + section) | ASSUMPTION |
| Format | Markdown logs/checklists and referenced source documents | ASSUMPTION |

## References

- `_CONTEXT.md` (this deliverable)
- `_REFERENCES.md` (this deliverable)
- `_DEPENDENCIES.md` (this deliverable)
- `DELIVERABLE_REGISTER.csv` row `DEL-100-06_epc-vendor-package-review-and-acceptance` — `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`
- `PACKAGE_REGISTER.csv` row `PKG-100` — same snapshot
- `SCOPE_LEDGER.csv` rows `SOW-0107`, `SOW-0108`, `SOW-0109`, `SOW-0110` — same snapshot
- `INTERFACE_REGISTER.csv` rows for `PKG-100` — same snapshot
- `OBJECTIVE_REGISTER.csv` rows `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` — same snapshot
- Source materials referenced by the decomposition row but not opened as deliverable-local source slices: `Workbook Packages row 63`; `26020-Package_Requirements.docx` package heading 52 — location TBD (not copied into deliverable; available under `_Sources/`)
