# Guidance: DEL-005-02_package-datasheet - Package Datasheet

## Purpose

The PKG-005 Site Grading package datasheet exists to carry the technical handoff basis for Civil discipline engineering and design. Its most important function is to preserve the accepted package identity, the workbook interface facts, and the DBM civil/site constraints without converting source-limited or preliminary basis items into closed design requirements.

## Principles

- Treat Gate 7 registers as the accepted decomposition truth for package and deliverable identity.
- Treat workbook Packages row 6 as the authoritative row-level source for WBS, CoA tracking number, discipline, package name, and interface applicability.
- Treat the 03-25 DBM as source authority for civil/site/drainage constraints, while preserving its stated uncertainties.
- Keep package-specific grading elevations, drainage flow values, retention volumes, and geotechnical closure as `TBD` unless a later accepted source provides them.
- Keep interface facts as datasheet evidence, not separate deliverables, consistent with the Gate 5 accepted basis in `PROJECT_DECOMP.md`.

## Considerations

The DBM makes surface-water management a civil design concern tied to offsite discharge prevention, process-area protection, and construction/operations access. For this deliverable, that supports inclusion of drainage and containment criteria in the datasheet, but it does not provide final drainage sizing or grading geometry.

The workbook row marks both Drain / Containment and Grading / Site Drainage / Spill Containment as applicable. Those two facts should be visible in the datasheet and interface matrix because they are source-supported row facts.

The DBM states that hydrology and geotechnical inputs remain preliminary or pending confirmation. The datasheet should therefore function as a controlled handoff record with explicit open fields, not as final issued-for-construction design criteria.

## Trade-offs

| Topic | Conservative treatment | Reason |
|---|---|---|
| Detailed grading geometry | Mark `TBD`. | No package-specific elevations, slopes, or grading plans were found in accessible source slices. |
| Drainage sizing | Mark `TBD`. | DBM preserves rainfall/hydrology uncertainty pending site-specific update. |
| Geotechnical closure | Mark `TBD`; require final geotechnical report. | DBM treats current geotechnical values as design placeholders. |
| Interface scope | Include only the two row-6 applicable interfaces. | Workbook row 6 and Gate 7 INTERFACE_REGISTER support those two interface facts. |
| Responsibility model | State EPC Integrator or discipline subcontractor responsibility is source-dependent. | Gate 7 PACKAGE_REGISTER does not infer separate vendor-package ownership for this Civil package. |

## Examples

Example datasheet entry pattern:

| Field | Entry |
|---|---|
| Interface type | Drain / Containment |
| Applicability | Applicable |
| Source | Workbook Packages row 6; Gate 7 INTERFACE_REGISTER IFC-590C44EF2F |
| Design value | TBD unless supplied by accepted civil/drainage design source |

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-005-02-001 | Final package-specific grading, drainage sizing, and geotechnical values are required for a complete engineering handoff but are not present in the accessible source slices. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, SEC-02 and SEC-11 | 26020-Packages_Interfaces_4_export.xlsx, Packages row 6 | Datasheet Conditions/Construction; Specification Requirements; Procedure Verification | Preserve workbook and DBM basis; keep final values `TBD` until civil/hydrology/geotechnical sources are accepted. | TBD |
