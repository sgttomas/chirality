# Datasheet — Vendor Document Turnover Package (DEL-072-05)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-072-05_vendor-document-turnover-package | `_CONTEXT.md` |
| Name | Vendor Document Turnover Package | `_CONTEXT.md` |
| ParentPackageID | PKG-072 | `_CONTEXT.md` |
| Parent Package Name | Truck Product Loading Unit 4-25 | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 99 |
| Workbook Row | 99 | `DELIVERABLE_REGISTER.csv`; `PACKAGE_REGISTER.csv` |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable Type | Vendor Document Turnover | `_CONTEXT.md` |
| Responsible Party | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | `_CONTEXT.md` |
| Decomposition Snapshot | GATE-07 Final Published 2026-05-24 | `_REFERENCES.md` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Document scope | Vendor document register, submittals, source-required vendor documentation, and turnover records | `DELIVERABLE_REGISTER.csv` row 562 |
| Covered SOW items | SOW-0245; SOW-0246; SOW-0247; SOW-0248 | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supported objectives | OBJ-001; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 (ASSUMPTION — package-heuristic mapping) | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package equipment tag(s) | TBD (Truck Loading Ticket Shack 2 equipment tag listed as TBD in DBM) | DBM-Deepcut/4-25_Deepcut_DBM.md §near line 2630, 2645 (location TBD for full package equipment list) |
| Package WBS code | 01 | `PACKAGE_REGISTER.csv` row 99 |
| Package vendor identifier | 26020-01-23-001 | `PACKAGE_REGISTER.csv` row 99 |
| Applicable interface types | Process Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports; Product Loading | `PACKAGE_REGISTER.csv` row 99 |

## Conditions

| Item | Value | Source |
|---|---|---|
| Hand-over phase | Project turnover (post-installation / pre-commissioning through to final acceptance) | ASSUMPTION (standard EPC vendor-turnover convention); source `location TBD` in 26020-Package_Requirements.docx heading 26 |
| Document control medium | TBD (electronic register expected) | location TBD |
| Required submittal language / units | TBD | location TBD |
| Retention period | TBD | location TBD |

## Construction (Package Contents)

The package is the assembled collection of vendor-produced documentation, organized into a register and indexed submittal set. Anticipated artifacts (from `_CONTEXT.md`):

- Vendor document register (index of all vendor documents with metadata: doc number, title, revision, status, transmittal reference)
- Vendor document submittals (the individual documents themselves)
- Source vendor document table rows as artifacts where available (per-row evidence from upstream registers)
- Turnover records (transmittals, sign-offs, final acceptance evidence)

Per-document attributes (anticipated; specific list TBD pending access to 26020-Package_Requirements.docx heading 26):

- Vendor document number / title / revision / date
- Submittal stage (preliminary / for-approval / final / as-built)
- Review status and EPC Integrator disposition
- Linked SOW item(s) and interface(s)
- Transmittal reference

## References

- `_CONTEXT.md` (deliverable identity and scope)
- `_REFERENCES.md` (authoritative basis pointers)
- `DELIVERABLE_REGISTER.csv` GATE-07 row 562 (DEL-072-05)
- `PACKAGE_REGISTER.csv` GATE-07 row 99 (PKG-072)
- `26020-Package_Requirements.docx` package heading 26 (NOT LOCALLY READABLE — `.docx` binary; `location TBD` for clause-level slices)
- `Workbook Packages row 99` (`26020-Packages_Interfaces_4_export.xlsx`, NOT LOCALLY READABLE — `.xlsx` binary)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Deepcut Design Basis Memorandum — referenced for facility context)

## Notes

- CONFLICT: `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv` row 562 identify the parent package as "Truck Product Loading Unit 4-25"; `PACKAGE_REGISTER.csv` row 99 narrative also references "Low Pressure Fuel Gas Package" / "Condensate Truck Loading Stations" in different fields. Recorded in `Guidance.md` Conflict Table for human ruling.
- Individual source vendor document rows remain artifacts/evidence, not separate deliverables (per `_CONTEXT.md` Notes).
