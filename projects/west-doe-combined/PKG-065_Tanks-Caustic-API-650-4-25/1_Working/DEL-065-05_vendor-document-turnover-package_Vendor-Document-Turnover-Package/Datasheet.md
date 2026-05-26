# Datasheet — DEL-065-05 Vendor Document Turnover Package — Tanks, Caustic (API 650) 4-25 (PKG-065)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-065-05_vendor-document-turnover-package` | `_CONTEXT.md` |
| Deliverable Name | Vendor Document Turnover Package | `_CONTEXT.md` |
| ParentPackageID | `PKG-065` | `_CONTEXT.md` |
| Package Name | Tanks, Caustic (API 650) 4-25 | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row DEL-065-05 |
| Workbook Row | 87 | `_CONTEXT.md`; PACKAGE_REGISTER.csv row PKG-065 |
| Discipline | Mechanical | `_CONTEXT.md` |
| Deliverable Type | Vendor Document Turnover | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row DEL-065-05 |
| Responsible Party | Package Vendor (vendor documentation); EPC Integrator (interface/integration review) | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row DEL-065-05 |

## Attributes — Document Set Identity

| Attribute | Value | Source |
|---|---|---|
| Document Class | Vendor Document Turnover Package | DELIVERABLE_REGISTER.csv row DEL-065-05 |
| Submission Owner | Package Vendor | `_CONTEXT.md` Responsibility |
| Review Owner | EPC Integrator | `_CONTEXT.md` Responsibility |
| Anticipated Artifacts (per `_CONTEXT.md`) | Vendor document register; vendor document submittals; source-required vendor document table rows as artifacts where available; turnover records | `_CONTEXT.md` Anticipated Artifacts; DELIVERABLE_REGISTER.csv row DEL-065-05 |
| Decomposition Note | Additional Gate 5 deliverable; individual source-document rows remain artifacts/evidence, not separate deliverables | `_CONTEXT.md` Notes; DELIVERABLE_REGISTER.csv row DEL-065-05 |

## Conditions — Applicable Scope of Equipment Covered

The vendor document turnover package covers documentation for the equipment supplied by the Package Vendor under PKG-065. Equipment identity (from sibling DEL-065-01/02/04 sources):

| Tag | Description | Quantity | Source |
|---|---|---|---|
| `TK-6780-1` | Spent Caustic Storage Tank | 1 | SCOPE_LEDGER SOW-0199 |
| (TBD tag) | Fresh Caustic Storage Tank | 1 | SCOPE_LEDGER SOW-0198 (tag not asserted in available source slice — `TBD`) |

## Construction — Document Categories Anticipated

The categories below reflect the anticipated artifact set named in `_CONTEXT.md` and DELIVERABLE_REGISTER.csv. Specific document line items for PKG-065 are not enumerated in any locally accessible source slice (`26020-Package_Requirements.docx` package heading 20 is a binary `.docx` not directly read in this run).

| Category | Contents | Source |
|---|---|---|
| Vendor document register | Master index of all vendor-issued documents for PKG-065 (drawings, datasheets, calculations, MTRs, NDE records, test records, manuals, spare parts lists). Specific line items `TBD`. | `_CONTEXT.md` Anticipated Artifacts; ASSUMPTION on contents (industry-typical for API 650 vendor package) |
| Vendor document submittals | The actual issued documents per the register, with revision codes and submittal status. Submittal categories and revision-control conventions `TBD` (no explicit source). | `_CONTEXT.md` Anticipated Artifacts |
| Source vendor document table rows | Where workbook/package-requirements rows directly enumerate a vendor document, that row is preserved as evidence. Available rows `TBD` pending readable source slice. | `_CONTEXT.md` Notes; DELIVERABLE_REGISTER.csv row DEL-065-05 |
| Turnover records | Mechanical completion, inspection, hydrotest, NDE, calibration, and packing records required for handover to EPC Integrator. Specific record set `TBD`. | `_CONTEXT.md` Anticipated Artifacts; ASSUMPTION (typical API 650 / atmospheric tank turnover) |

## Scope Items Covered

| SOW Item | Summary |
|---|---|
| `SOW-0197` | Carry the workbook-defined vendor-responsible Mechanical package as a distinct flat project package for WBS 01; Package Vendor owns engineering/design/equipment/documentation; EPC Integrator owns facility integration. |
| `SOW-0198` | Supply (1) spent caustic tank and (1) fresh caustic tank. |
| `SOW-0199` | Major included equipment — Spent Caustic Storage Tank TK-6780-1 detail. |
| `SOW-0200` | Scope notes and open items (by-others list; design condition placeholders). |

## Objectives Supported

`OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION: package-grouping heuristic via `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`; mapping copied from `_CONTEXT.md`).

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- Gate 7 PROJECT_DECOMP snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `DELIVERABLE_REGISTER.csv` row DEL-065-05_vendor-document-turnover-package
  - `PACKAGE_REGISTER.csv` row PKG-065
  - `SCOPE_LEDGER.csv` rows SOW-0197, SOW-0198, SOW-0199, SOW-0200
- `_Sources/26020-Package_Requirements.docx` package heading 20 (binary `.docx` — not directly read; values relayed via SCOPE_LEDGER / DELIVERABLE_REGISTER extraction; vendor-document-specific contents `location TBD`)
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 87 (binary `.xlsx` — not directly read; values relayed via PACKAGE_REGISTER extraction)
