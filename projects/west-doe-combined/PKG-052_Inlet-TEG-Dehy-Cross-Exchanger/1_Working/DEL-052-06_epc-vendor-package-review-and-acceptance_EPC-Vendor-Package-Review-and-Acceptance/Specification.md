# Specification — DEL-052-06 EPC Vendor Package Review and Acceptance

## Scope

### In Scope

The EPC Integrator shall produce a review and acceptance record for the PKG-052 (Inlet / TEG Dehy Cross Exchanger E-5718-1) vendor package, evaluating it against:

- the EPC Scope of Work (`DEL-052-01`),
- the EPC Package Datasheet (`DEL-052-02`),
- the EPC Construction Work Package (`DEL-052-03`),

using as inputs:

- the Vendor Engineered Equipment Package (`DEL-052-04`), and
- the Vendor Document Turnover Package (`DEL-052-05`).

Source: `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` row DEL-052-06.

### Out of Scope

- Authoring vendor engineering, design, fabrication, or vendor documentation (owned by `DEL-052-04` / `DEL-052-05`).
- Modifying the EPC SOW, Package Datasheet, or CWP (those are upstream deliverables).
- Package-specific exclusions beyond those stated in source materials — TBD (`PACKAGE_REGISTER.csv` row PKG-052: "no package-specific exclusions stated in source materials").

## Requirements

| Req ID | Requirement | Verification Approach | Source |
|---|---|---|---|
| R-06-01 | A vendor document review and comment log shall be produced covering vendor submittals supplied under `DEL-052-05`. | Verification §V-06-01 | `ARTIFACT_REGISTER.csv` ART-F0F5332A58; `_CONTEXT.md` Anticipated Artifacts |
| R-06-02 | A package acceptance checklist shall be produced confirming integration acceptance against EPC SOW, Package Datasheet, and CWP. | Verification §V-06-02 | `ARTIFACT_REGISTER.csv` ART-21EEB708EC; `_CONTEXT.md` |
| R-06-03 | Factory/shop test and inspection evidence shall be captured from the vendor for the supplied equipment package (E-5718-1; TEMA 'R' BEM; duty 5514.3 kW / 18.82 MMBTU/hr) and accompanying piping/instrumentation and skid. | Verification §V-06-03 | `ARTIFACT_REGISTER.csv` ART-7F212499D9; `PACKAGE_REGISTER.csv` row PKG-052 |
| R-06-04 | Turnover evidence shall be assembled to substantiate handoff readiness from vendor to EPC Integrator and into the facility. | Verification §V-06-04 | `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` |
| R-06-05 | The acceptance record shall address each PKG-052 interface type with respect to integration readiness: Process Piping; Utility Piping; Drain / Containment; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports. | Verification §V-06-05 | `INTERFACE_REGISTER.csv` PKG-052 rows; `PACKAGE_REGISTER.csv` row PKG-052 |
| R-06-06 | Each review/acceptance entry shall trace to the originating requirement in DEL-052-01, DEL-052-02, or DEL-052-03 (or, where applicable, to the source row in `26020-Package_Requirements.docx` package heading 7). | Verification §V-06-06 | ASSUMPTION based on review/acceptance role stated in `_CONTEXT.md` Scope |
| R-06-07 | Detailed acceptance criteria for factory/shop tests and inspections shall be derived from `26020-Package_Requirements.docx` package heading 7 and from the vendor RFQ basis (`26020-01-PT-RFQ-16-001-Heat_Ex_ST.docx`). | Verification §V-06-07 | location TBD — sources not locally text-accessible |

## Standards

| Standard / Reference | Applicability | Location |
|---|---|---|
| 26020-Package_Requirements.docx — package heading 7 (Inlet / TEG Dehy Cross Exchanger) | Defines package-level technical and documentation requirements that the review shall verify | location TBD (binary source; not text-accessible) |
| 26020-Packages_Interfaces_4_export.xlsx — Packages row 62 | Authoritative interface inventory for PKG-052 (mirrored in `INTERFACE_REGISTER.csv`) | location TBD (binary source); accessible mirror: `INTERFACE_REGISTER.csv` |
| Vendor RFQ — `26020-01-PT-RFQ-16-001-Heat_Ex_ST.docx` | Word Source Basis cited in `PACKAGE_REGISTER.csv` row PKG-052 | location TBD; file not present under `_Sources/` |
| TEMA 'R' (heat-exchanger mechanical standard) | Mechanical-design class declared for E-5718-1 | ASSUMPTION: applies to vendor design verification; clause-level TBD |
| EPC Construction Work Package (DEL-052-03) | Construction/turnover acceptance basis | `DELIVERABLE_REGISTER.csv` row DEL-052-03 |

## Verification

| V ID | Verifies | Method |
|---|---|---|
| V-06-01 | R-06-01 | Inspect vendor document review log for coverage of every submittal in `DEL-052-05` and presence of EPC review disposition for each entry. |
| V-06-02 | R-06-02 | Inspect package acceptance checklist for closed-out entries against DEL-052-01, DEL-052-02, and DEL-052-03 line items. |
| V-06-03 | R-06-03 | Inspect factory/shop test reports and inspection evidence for the tagged equipment (E-5718-1) and accompanying piping/instrumentation and skid; confirm acceptance dispositions. Detailed pass/fail criteria — TBD pending source access. |
| V-06-04 | R-06-04 | Inspect turnover evidence for completeness of handoff records (custody transfer, punch list closure, residual-action register). Specific turnover-record set — TBD pending source access. |
| V-06-05 | R-06-05 | Walk each PKG-052 interface row from `INTERFACE_REGISTER.csv` and confirm an acceptance disposition exists. |
| V-06-06 | R-06-06 | Spot-check traceability from acceptance entries back to originating SOW/Datasheet/CWP requirements. |
| V-06-07 | R-06-07 | Once source clauses are locally accessible, regenerate acceptance criteria and re-verify R-06-03/R-06-04. |

## Documentation

The deliverable produces, at minimum:

- Vendor document review log (`ART-F0F5332A58`)
- Package acceptance and turnover checklist (`ART-21EEB708EC`)
- Factory/shop test and inspection evidence (`ART-7F212499D9`)
- Turnover evidence (per `_CONTEXT.md` Anticipated Artifacts)

Detailed submittal lists and per-document acceptance criteria are TBD pending access to `26020-Package_Requirements.docx` package heading 7 and to the vendor RFQ basis.
