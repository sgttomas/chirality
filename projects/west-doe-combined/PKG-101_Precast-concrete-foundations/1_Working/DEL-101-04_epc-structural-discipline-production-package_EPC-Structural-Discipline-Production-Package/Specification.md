# Specification: DEL-101-04 — EPC / Structural Discipline Production Package

## Scope

**In scope.** Production-unit work for the non-vendor portion of PKG-101 (Precast concrete foundations), discipline = Structural, WBS 01, CoA tracking 26020-01-36-001. The deliverable carries the workbook-defined Structural package scope conservatively from workbook row 102 and DBM support context. (Source: `PACKAGE_REGISTER.csv` row PKG-101; `_CONTEXT.md`.)

**Out of scope / excluded.** TBD — no package-specific exclusions are stated in source materials. (Source: `PACKAGE_REGISTER.csv` Exclusions.)

**Boundary with sibling deliverables.**
- DEL-101-01 (Scope of Work), DEL-101-02 (Package Datasheet), DEL-101-03 (Construction Work Package) are the EPC anchor deliverables for PKG-101 and remain the authoritative carriers of integrator-authored scope, datasheet, and construction work content. (Source: `DELIVERABLE_REGISTER.csv` rows DEL-101-01..03.)
- DEL-101-04 covers only the discipline-led production unit work that is not vendor-engineered. (Source: `DELIVERABLE_REGISTER.csv` row DEL-101-04 Description; `_CONTEXT.md` Scope.)

## Requirements

| Req ID | Requirement | Type | Source |
|---|---|---|---|
| R-101-04-01 | Produce a discipline production package basis artifact for PKG-101 grounded in workbook row 102 and DBM-supported context. | Artifact | ART-D61EA18810 (`ARTIFACT_REGISTER.csv`) |
| R-101-04-02 | Produce a source-limited requirements closure record that explicitly enumerates non-vendor structural requirements not present in the current source set, for Gate 5 disposition. | Artifact | ART-5FB1815B54; `DELIVERABLE_REGISTER.csv` Notes |
| R-101-04-03 | Produce a TBD discipline deliverable register listing the discipline deliverables the production unit will issue within source-supported scope. | Artifact | `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` AnticipatedArtifacts |
| R-101-04-04 | Preserve and reflect declared physical interfaces of PKG-101: Grading / Site Drainage / Spill Containment (IFC-26343B703C) and Structural / Foundations / Supports (IFC-BED3DE4194). | Interface | `INTERFACE_REGISTER.csv` rows for PKG-101 |
| R-101-04-05 | Ensure scope coverage of SOW-0257 ("Carry the workbook-defined Structural package 'Precast concrete foundations' as a distinct flat project package for WBS 01"). | Scope | `SCOPE_LEDGER.csv` row SOW-0257 |
| R-101-04-06 | Do not infer a separate vendor-package ownership model; responsibility assignment is source-dependent and must reflect the workbook basis. | Constraint | `PACKAGE_REGISTER.csv` ResponsibilityModel |
| R-101-04-07 | All non-trivial structural design values, materials, geometry, loadings, and construction criteria absent from the current source set MUST be recorded as TBD with provenance; they MUST NOT be invented. | Constraint (ASSUMPTION on application — derived from K-PROV-1 governance principle and source-limited scope statement) | `DELIVERABLE_REGISTER.csv` Notes; governance principle |
| R-101-04-08 | Responsible-party assignment (EPC Integrator vs discipline subcontractor) MUST be recorded in the responsibility assignment record before production commences. | Constraint | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` ResponsibleParty |

## Standards

| Standard / Reference | Applicability | Location |
|---|---|---|
| GATE-07 PROJECT_DECOMP snapshot (`PROJECT_DECOMP.md`, `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `SCOPE_LEDGER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_REGISTER.csv`) | Governing decomposition basis for this deliverable. | `_REFERENCES.md` |
| Workbook Packages row 102 (`26020-Packages_Interfaces_4_export.xlsx`) | Authoritative source row for PKG-101 identity, scope, interfaces. | location TBD (cell range within workbook not slice-extracted) |
| 26020 Package Requirements (`26020-Package_Requirements.docx`) | Possibly applicable package-requirements text; not opened as a source slice for this deliverable. | location TBD (ASSUMPTION: likely applicable) |
| DBM-Deepcut / DBM-Comp_and_Liquids — SEC-11 Civil/Structural basis | Cited by OBJ-008 as the civil/structural support basis; may inform structural production scope. | location TBD (not opened as a source slice for this deliverable) |
| Structural design codes (e.g., precast-concrete and foundation codes) | TBD — no specific structural code citations exist in the current source set for PKG-101. | TBD |

## Verification

| Req ID | Verification Approach |
|---|---|
| R-101-04-01 | Inspect the discipline production package basis artifact for presence of workbook-row-102 grounding and DBM context citations. |
| R-101-04-02 | Inspect the closure record for explicit enumeration of source-limited gaps; each gap must carry provenance and be flagged for Gate 5 ruling. |
| R-101-04-03 | Inspect the discipline deliverable register; confirm each listed deliverable is traceable to a source-supported scope statement or marked TBD. |
| R-101-04-04 | Cross-check production-package artifacts against `INTERFACE_REGISTER.csv` rows for PKG-101; both interface types must be reflected. |
| R-101-04-05 | Trace deliverable artifacts to SOW-0257 in `SCOPE_LEDGER.csv`. |
| R-101-04-06 | Review responsibility assignment record for absence of vendor-package ownership inferences not supported by sources. |
| R-101-04-07 | Spot-check artifacts for unsourced numeric values or design assertions; flag any not labeled TBD/ASSUMPTION. |
| R-101-04-08 | Confirm responsibility assignment record is present and signed by an authorized human (per K-AUTH-1). |

## Documentation

Required artifacts produced under this deliverable (per `ARTIFACT_REGISTER.csv` and `_CONTEXT.md`):

- Discipline production package basis (ART-D61EA18810)
- TBD discipline deliverable register
- Source-limited requirements closure record (ART-5FB1815B54)

Cross-referenced (carried by sibling DEL-101-01..03, not duplicated here):
- Package scope of work (DEL-101-01)
- Package technical datasheet, vendor handoff basis, interface requirements matrix, interface fact evidence (DEL-101-02)
- Construction work package, installation/tie-in workface plan, construction interface and turnover checklist (DEL-101-03)
