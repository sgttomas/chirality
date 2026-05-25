# Datasheet: DEL-031-05 — Vendor Document Turnover Package

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-031-05_vendor-document-turnover-package | `_CONTEXT.md` |
| Name | Vendor Document Turnover Package | `_CONTEXT.md` |
| ParentPackageID | PKG-031 | `_CONTEXT.md` |
| Package | Transformer TXP-8500-1 — Step Down Distribution Transformer, 3 MVA, 13.8 kV / 600/347 V | `_CONTEXT.md` |
| Discipline | Electrical | `_CONTEXT.md` |
| Deliverable Type | Vendor Document Turnover | `_CONTEXT.md` |
| Responsible Party | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | `_CONTEXT.md` |
| Covers Scope Items | SOW-0032 | DELIVERABLE_REGISTER.csv row DEL-031-05 |
| Supports Objectives | OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 | DELIVERABLE_REGISTER.csv row DEL-031-05 |
| Source Reference | Workbook Packages row 33 | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Subject equipment tag | TXP-8500-1 | Package name (workbook row 33) |
| Equipment class | Step-Down Distribution Transformer | Package name |
| Nameplate rating | 3 MVA | Package name (location TBD in vendor source) |
| Primary voltage | 13.8 kV | Package name (location TBD in vendor source) |
| Secondary voltage | 600 / 347 V | Package name (location TBD in vendor source) |
| Vendor document set scope | Vendor document register, submittals, source-required vendor documentation, turnover records | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv |
| Vendor-document grouping rule | Source vendor-document rows are carried as artifacts/evidence under this turnover package, not as standalone deliverables | PROJECT_DECOMP DEC-004; DEC-012 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Decomposition gate | Gate 5 approved 2026-05-24 (deliverable basis); Gate 7 final published 2026-05-24 (artifact set) | PROJECT_DECOMP gate matrix |
| Coordination mode | DECLARED | `_DEPENDENCIES.md` |
| Maturity threshold | INITIALIZED | `_DEPENDENCIES.md` |
| Source slice locality | No deliverable-specific source slices copied to `0_References` during PREPARATION | `_REFERENCES.md`; `0_References/` listing |
| Authoritative source root | `_Sources/` (shared) — `26020-Package_Requirements.docx`, `26020-Packages_Interfaces_4_export.xlsx`, DBM folders | `_REFERENCES.md`; PROJECT_DECOMP source register |

## Construction (Artifact Composition)

| Artifact | Description | Source |
|---|---|---|
| Vendor document register | Indexed list of all vendor-supplied documents for PKG-031 with status, revision, transmittal, and turnover state | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv |
| Vendor document submittals | Submitted vendor document files (drawings, datasheets, test reports, manuals) with revision history | `_CONTEXT.md` |
| Source vendor-document table rows (as artifacts) | Rows from the 26020 package requirements vendor-document tables matched to PKG-031 | DEC-004; DEC-012; `_Sources/26020-Package_Requirements.docx` (PKG-031 section — location TBD) |
| Turnover records | Final turnover transmittals, completeness sign-off, and acceptance evidence linked to EPC Vendor Package Acceptance | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv DEL-031-06 |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- Gate 7 snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `DELIVERABLE_REGISTER.csv` (row DEL-031-05)
  - `PACKAGE_REGISTER.csv` (row PKG-031)
  - `OBJECTIVE_DELIVERABLE_MAP.csv`
  - `ARTIFACT_REGISTER.csv`
  - `PROJECT_DECOMP.md` (DEC-004, DEC-006, DEC-012)
- `_Sources/26020-Package_Requirements.docx` — PKG-031 section and vendor-documentation tables (location TBD; not locally sliced)
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — Workbook Packages row 33
