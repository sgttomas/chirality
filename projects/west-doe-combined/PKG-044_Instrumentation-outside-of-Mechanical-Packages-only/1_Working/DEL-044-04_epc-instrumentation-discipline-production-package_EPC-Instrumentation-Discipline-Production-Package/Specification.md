# Specification — DEL-044-04 EPC / Instrumentation Discipline Production Package

> Pass 1/2 draft. Requirements are conservatively carried from decomposition narrative because deliverable-specific source slices are not locally accessible (`_REFERENCES.md` Missing/Deferred References). Items derived without a source slice are labelled ASSUMPTION or TBD; substantive engineering requirements remain `TBD` pending Gate 5 disposition.

## Scope

**In scope.** Discipline-led production unit producing the instrumentation deliverables for `PKG-044` (Instrumentation outside of Mechanical Packages only), excluding the EPC-anchor deliverables already separated out as DEL-044-01 (Scope of Work), DEL-044-02 (Package Datasheet), and DEL-044-03 (Construction Work Package). The deliverable is a "production unit for the non-vendor package scope, carried conservatively from workbook and DBM support" (DELIVERABLE_REGISTER row DEL-044-04 Description).

**Out of scope.**
- Vendor-engineered equipment package and vendor document turnover — `PKG-044` is not vendor-owned (PACKAGE_REGISTER PKG-044 ResponsibilityNote: "no separate vendor-package ownership model is inferred").
- Mechanical-package-embedded instrumentation — explicitly excluded by package name "Instrumentation (outside of Mechanical Packages only)".
- Package-level scope of work, datasheet, and construction work package authorship (owned by DEL-044-01..03).

## Requirements

Note: requirements below are derived from `_CONTEXT.md`, the GATE-07 DELIVERABLE_REGISTER and PACKAGE_REGISTER rows, and the ARTIFACT_REGISTER. Where no source slice supports a specific value the entry is `TBD`.

| ID | Requirement | Source / Basis |
|---|---|---|
| R-044-04-01 | Produce a discipline production package basis documenting the non-vendor instrumentation scope for `PKG-044`. | DELIVERABLE_REGISTER DEL-044-04 AnticipatedArtifacts ("Discipline production package basis") |
| R-044-04-02 | Produce a discipline deliverable register enumerating the discipline-level work items for `PKG-044`. | DELIVERABLE_REGISTER DEL-044-04 AnticipatedArtifacts ("TBD discipline deliverable register") |
| R-044-04-03 | Produce a source-limited requirements closure record explicitly identifying source gaps and Gate 5 disposition items. | DELIVERABLE_REGISTER DEL-044-04 AnticipatedArtifacts |
| R-044-04-04 | Cover scope-of-work item `SOW-0045` (Instrumentation, outside of Mechanical Packages only). | `_CONTEXT.md` Covers Scope Items; DELIVERABLE_REGISTER DEL-044-04 SowReferenceIDs |
| R-044-04-05 | Support associated objectives `OBJ-002; OBJ-003; OBJ-005; OBJ-006; OBJ-007; OBJ-010` (ASSUMPTION: package-grouping heuristic). | OBJECTIVE_DELIVERABLE_MAP rows for `DEL-044-04` |
| R-044-04-06 | Address the package's applicable interface types (Process Piping; Utility Piping; Electrical Power; I&C/Control Cabling; Communications/Network) within the discipline production unit. | PACKAGE_REGISTER PKG-044 ApplicableInterfaceTypes |
| R-044-04-07 | Carry forward the Gate 6 disposition that instrumentation field supports, power, and communications are included in each package scope as appropriate under the plug-n-play package philosophy. | ARTIFACT_REGISTER ART-05F89F3B5C / ART-7114CBB6AD / ART-C0C9C4ADC7 (interface fact rows for DEL-044-02) |
| R-044-04-08 | Detailed engineering, performance, materials, and qualification requirements — TBD pending Gate 5 disposition and source slice resolution. | DELIVERABLE_REGISTER DEL-044-04 Notes ("source-limited and remain open for Gate 5 disposition") |
| R-044-04-09 | Responsibility assignment (EPC Integrator vs. discipline subcontractor) — TBD; source-dependent. | PACKAGE_REGISTER PKG-044 ResponsibilityNote |

## Standards

| Standard / Code | Applicability | Source |
|---|---|---|
| Project-wide instrumentation standards (ISA-5, ISA-18, IEC 61511, IEC 60079, NEC/CEC, project specs) | ASSUMPTION: likely applicable for instrumentation production work; location TBD; clauses not derived without source access | ASSUMPTION; no source slice locally accessible |
| Workbook Packages row 46 conventions | Applicable as decomposition basis | `_REFERENCES.md` |
| `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` provisions | Applicable as DBM support per PACKAGE_REGISTER row | PACKAGE_REGISTER PKG-044 SourceReference; location TBD relative to `_REFERENCES.md` Shared Source Root |

## Verification

| Requirement | Verification approach |
|---|---|
| R-044-04-01..03 | Document inspection — verify the three anticipated artifacts exist and are internally consistent with `PKG-044` scope. |
| R-044-04-04 | Trace matrix back to `SOW-0045`. |
| R-044-04-05 | Trace matrix back to each listed objective (mark ASSUMPTION lineage explicitly). |
| R-044-04-06 | Cross-check interface coverage against PACKAGE_REGISTER PKG-044 ApplicableInterfaceTypes and DEL-044-02 interface-fact artifacts. |
| R-044-04-07 | Confirm Gate 6 disposition language is retained or explicitly resolved. |
| R-044-04-08 | Gate 5 review (deferred); record open items in the source-limited requirements closure record. |
| R-044-04-09 | Human ruling at responsibility assignment; record decision in `_DEPENDENCIES.md` or successor responsibility evidence artifact. |

## Documentation

Required artifacts (from `_CONTEXT.md` Anticipated Artifacts):

1. Discipline production package basis.
2. Discipline deliverable register (currently TBD).
3. Source-limited requirements closure record.

Cross-references:

- DEL-044-01 (Scope of Work) — package-level scope and tagged equipment basis.
- DEL-044-02 (Package Datasheet) — interface facts and vendor-handoff evidence.
- DEL-044-03 (Construction Work Package) — installation, turnover, and tie-in plan.
