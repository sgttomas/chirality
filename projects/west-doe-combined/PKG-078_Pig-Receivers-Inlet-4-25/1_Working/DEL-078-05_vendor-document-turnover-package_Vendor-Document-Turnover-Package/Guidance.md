# Guidance — DEL-078-05 Vendor Document Turnover Package

## Purpose

The Vendor Document Turnover Package converts an as-engineered, as-fabricated, as-supplied vendor package (`DEL-078-04`) into the documentary record EPC Integrator and the Owner need to (a) accept the package, (b) install it under `DEL-078-03`, and (c) operate and maintain it through life. It exists because physical hardware is opaque without its document trail; without a controlled register, vendor documents arrive ad-hoc, revisions desynchronize, and turnover stalls. Source: `_CONTEXT.md`; DELIVERABLE_REGISTER row 436.

## Principles

1. **The register is the contract.** The vendor document register, not the file folder, is authoritative for what has been transmitted and what is in force.
2. **Turnover is per-revision, not per-file.** Each document carries a revision; turnover acceptance is granted per revision.
3. **Source-required documents are mandatory, not negotiable.** Document classes named in `_Sources/26020-Package_Requirements.docx` (`Vendor Engineering Deliverables` for `26020-01-PT-35-001`) form the floor; the vendor's standard package list may add to it but may not subtract.
4. **Safety-related documentation is non-substitutable.** HIPPS SIL, sour-service materials, pressure-vessel code stamps, and proof-test records cannot be deferred to "as-built" if they are prerequisites to commissioning.
5. **Traceability over volume.** A small register that cleanly links each transmittal to acceptance evidence is preferred to a large dump of files.

## Considerations

- The accessible source slice for `26020-01-PT-35-001` shows a `Vendor Engineering Deliverables` heading whose body is empty. Treat the canonical list as `TBD` and surface a conflict (see Conflict Table) rather than inferring it silently.
- The package uses HIPPS as the primary overpressure protection of the inlet separator. Documentation that fails to substantiate the SIL claim is a turnover blocker, regardless of equipment readiness.
- Sour-service basis is stated as 1.0 mol% in the source without specifying H2S; assume H2S until corrected, but flag the assumption.
- Interface documentation depends on `26020-Packages_Interfaces_4_export.xlsx`; mismatches between vendor drawings and that register are the most common source of late discoveries.
- EPC review (`DEL-078-06`) consumes this turnover package. Anything ambiguous here surfaces there.

## Trade-offs

| Trade-off | Considerations |
|---|---|
| Early partial turnover vs. complete turnover | Partial turnover accelerates downstream activities but increases revision-control overhead and risk of stale information being used. |
| Vendor-standard document set vs. project-specific list | Vendor standard is faster but may omit project-required artifacts; project-specific list slows submittal but ensures fit. |
| Native vendor numbering vs. EPC document numbering | Native numbering preserves vendor traceability; EPC numbering simplifies EPC-side control. A mapping table is usually the right compromise. ASSUMPTION (project standard not accessible). |

## Examples

Examples are deferred (`TBD`) until the source `Vendor Engineering Deliverables` list is populated or a project documentation standard is added to `_REFERENCES.md`.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-01 | Required vendor document classes for this package are unspecified. The source heading `Vendor Engineering Deliverables` for `26020-01-PT-35-001` exists but its body is empty. | `_Sources/26020-Package_Requirements.docx` heading `26020-01-PT-35-001 / Vendor Engineering Deliverables` (empty) | `_CONTEXT.md` Anticipated Artifacts (generic: "vendor document register; submittals; turnover records") | Datasheet "Mandatory document classes"; Specification R-02; Procedure steps | PROPOSAL: Adopt a conventional vendor turnover document set (see Datasheet) until source is amended. | TBD |
| C-02 | Sour-service basis "1.0 mol%" does not name the species. | `_Sources/26020-Package_Requirements.docx` Major Included Equipment | No alternate source in accessible references | Datasheet Attributes; Specification R-05 | PROPOSAL: Interpret as 1.0 mol% H2S until corrected. | TBD |
| C-03 | Governing standards (ASME, NACE, IEC 61511) are not cited in the accessible source slice. | `_Sources/26020-Package_Requirements.docx` 26020-01-PT-35-001 (no standards cited) | None | Specification Standards table | PROPOSAL: Flag as ASSUMPTION; require project-level standard reference to be added to `_REFERENCES.md`. | TBD |
| C-04 | Acceptance code scheme (e.g., Code 1/2/3) and document numbering standard are not in accessible references. | n/a | n/a | Specification R-08, R-09; Procedure | PROPOSAL: Use project EPC documentation standard once identified; mark TBD until then. | TBD |
| C-05 | Two `Pig Receivers (Inlet)` sections exist in the source (`26020-01-PT-35-001` and `26020-02-PT-35-001`). `PKG-078` "4-25" is interpreted as Train 4 / item 25, mapping to `26020-01-PT-35-001` (the 3-receiver, HIPPS-equipped train). | `_Sources/26020-Package_Requirements.docx` heading `26020-01-PT-35-001` (3x, HIPPS) | `_Sources/26020-Package_Requirements.docx` heading `26020-02-PT-35-001` (2x, ESDV) | All four documents | PROPOSAL: Treat `26020-01-PT-35-001` as authoritative for this deliverable based on Major Included Equipment matching anticipated three-receiver HIPPS scope. | TBD |
