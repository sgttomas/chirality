# Datasheet: DEL-106-05 — Vendor Document Turnover Package

Pass: P1 (initial draft) — Source-grounded against GATE-07 Final Published PROJECT_DECOMP snapshot.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-106-05_vendor-document-turnover-package` | `_CONTEXT.md` / DELIVERABLE_REGISTER.csv (PKG-106 row) |
| Name | Vendor Document Turnover Package | DELIVERABLE_REGISTER.csv |
| Parent Package | `PKG-106` Yard Lighting (Workbook row 12) | PACKAGE_REGISTER.csv |
| Discipline | Electrical | PACKAGE_REGISTER.csv |
| Type | Vendor Document Turnover | DELIVERABLE_REGISTER.csv |
| Responsible Party | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | DELIVERABLE_REGISTER.csv |
| Covers Scope Items | `SOW-0011` | DELIVERABLE_REGISTER.csv |
| Supports Objectives | `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-009`, `OBJ-010` (ASSUMPTION — package-grouping heuristic from `_CONTEXT.md`) | `_CONTEXT.md`; OBJECTIVE_DELIVERABLE_MAP |
| Authoritative Source Row | Workbook Packages row 12 | DELIVERABLE_REGISTER.csv |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package CoA Tracking Number | `26020-01-30-001` | PACKAGE_REGISTER.csv (PKG-106) |
| Package WBS | TBD (not stated in source) | PACKAGE_REGISTER.csv |
| Applicable Interface Types | Electrical Power; Grounding / Bonding; Area / Exterior Lighting | PACKAGE_REGISTER.csv; INTERFACE_REGISTER.csv (IFC-6FCF1B30D6, IFC-DA0D60681B, IFC-ED86F51087) |
| Vendor Document Register Content | TBD — detailed vendor-document requirements are not present in current source material for this package | ARTIFACT_REGISTER.csv (ART-182773E33C: "TBD vendor document register") |
| Vendor Submittals List | TBD (not enumerated in source) | ARTIFACT_REGISTER.csv |
| Source-Required Vendor Documents Table Rows | TBD — no package-specific source vendor-document rows captured in current decomposition | ARTIFACT_REGISTER.csv (ART-182773E33C, Vendor Documentation Gap Evidence) |
| Turnover Records | TBD list; framed as evidence carried to DEL-106-06 review/acceptance | DELIVERABLE_REGISTER.csv; ARTIFACT_REGISTER.csv (ART-DE7811332B, ART-6A9AFD2292) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Package Boundary | Workbook-defined vendor-owned Electrical package for Yard Lighting; vendor owns package engineering, design, vendor documentation, and physical equipment; EPC Integrator owns facility-level integration and interfaces | PACKAGE_REGISTER.csv |
| Exclusions | TBD; no package-specific exclusions stated in source materials | PACKAGE_REGISTER.csv |
| Review Interface | EPC Integrator interface/integration review of vendor documentation (delegated downstream to DEL-106-06 EPC Vendor Package Review and Acceptance) | DELIVERABLE_REGISTER.csv |

## Construction (Contents of the Turnover Package)

ASSUMPTION — the following are the expected component categories for a Vendor Document Turnover Package, derived from the anticipated artifacts in `_CONTEXT.md` and DELIVERABLE_REGISTER.csv. Specific document titles and revisions are TBD pending vendor submission and source enumeration.

| Component | Description | Source |
|---|---|---|
| Vendor Document Register | Master index of all documents the vendor is contractually obligated to submit for the package; entries TBD | `_CONTEXT.md` anticipated artifacts; DELIVERABLE_REGISTER.csv |
| Vendor Document Submittals | The actual submitted vendor documents (drawings, calculations, manuals, certificates, test reports, etc.); titles TBD | `_CONTEXT.md` anticipated artifacts |
| Source-Required Vendor Document Table Rows (artifacts) | Where the source workbook lists specific vendor documents as rows, those rows are carried as artifacts; none enumerated in current snapshot | `_CONTEXT.md` Notes; ART-182773E33C |
| Turnover Records | Records evidencing handoff of the document package to EPC Integrator/Owner; format TBD | `_CONTEXT.md` anticipated artifacts |

## References

- `_CONTEXT.md` — deliverable identity and scope
- `_REFERENCES.md` — authoritative source pointers
- DELIVERABLE_REGISTER.csv (GATE-07 Final Published snapshot) — DEL-106-05 row
- PACKAGE_REGISTER.csv (GATE-07) — PKG-106 row
- ARTIFACT_REGISTER.csv (GATE-07) — ART-182773E33C "TBD vendor document register" for PKG-106
- INTERFACE_REGISTER.csv (GATE-07) — PKG-106 interface rows
- OBJECTIVE_DELIVERABLE_MAP.csv (GATE-07)
- Workbook Packages row 12 (cited by decomposition; underlying xlsx not opened as text — location TBD for clause-level slices)
