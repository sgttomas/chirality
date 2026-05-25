# Guidance: DEL-001-01 Scope of Work

## Purpose

This document guides preparation of the PKG-001 Scope of Work. The deliverable exists to anchor the Civil package "Earthworks for foundations" for WBS 01, identify its source-supported interfaces, state its package function and boundaries, and provide an integration narrative for downstream package datasheet, construction work package, and civil discipline production package work.

Source basis: Gate 7 `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `SCOPE_LEDGER.csv`, and workbook Packages row 2.

## Principles

- Keep PKG-001 distinct from PKG-002 even though both rows share the same normalized tracking number. Gate 7 states duplicate tracking numbers are not merged for SOW-0001.
- Treat workbook Packages row 2 and Gate 7 registers as the package identity authority.
- Treat accessible DBM civil sections as source basis for civil, grading, drainage, foundation, geotechnical, survey, and external-input requirements.
- Use `TBD` for package-specific quantities, coordinates, final geotechnical parameters, final survey data, final drainage sizing, and final construction sequencing until authoritative inputs are available.
- Do not invent tagged equipment for this civil package. The accepted deliverable requires a tagged equipment and package identity list, but the accessible row does not identify package-specific tags.

## Considerations

The accepted package row identifies two interface types: Grading / Site Drainage / Spill Containment and Structural / Foundations / Supports. These interfaces should drive the scope boundary and integration narrative for the Scope of Work.

The DBM civil basis requires geotechnical and topographical inputs before final civil and structural design closure. The Scope of Work can require those inputs to be tracked and incorporated, but should not state final values that are marked `TBD` in the DBM.

Field construction responsibility is not the same as EPC scope definition responsibility. The DBM assigns field construction activities, including grading, piling, and foundation work, to Tourmaline field construction scope, while Gate 7 assigns this Scope of Work deliverable to the EPC Integrator.

## Trade-offs

| Topic | Conservative treatment |
|---|---|
| Package breadth | Include the source-supported civil interfaces and DBM civil basis, but avoid expanding into site grading, retention pond, road, or foundation packages unless directly needed for PKG-001 boundaries. |
| Design detail | State current design basis and external inputs, not final design values. |
| Responsibility | Separate EPC Integrator deliverable ownership from Tourmaline field construction execution. |
| Standards | List DBM governing standards as basis items; do not create clause-level requirements without source text. |

## Examples

- Supported: "PKG-001 carries Grading / Site Drainage / Spill Containment and Structural / Foundations / Supports interfaces." Source: Gate 7 `INTERFACE_REGISTER.csv`, PKG-001; workbook Packages row 2.
- Supported: "Final geotechnical parameters are TBD pending completion and review of the geotechnical assessment." Source: DBM-Deepcut SEC-11.
- Unsupported unless later sourced: "PKG-001 requires a specific excavation volume, pile count, or cut/fill balance."

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| None identified | No direct source conflict found during Pass 1+2 drafting | N/A | N/A | N/A | N/A | N/A |

## Open Items

- TBD: package-specific earthwork quantities.
- TBD: final geotechnical design parameters.
- TBD: final topographical survey and grade surface file content.
- TBD: final plot-plan coordinates and retention pond location impacts.
- TBD: package-specific tagged equipment list, if any.
- TBD: detailed civil discipline deliverable register for the related discipline production package.
