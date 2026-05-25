# Package Datasheet Guidance

## Purpose

This guidance explains how to interpret and use the `PKG-001 - Earthworks for foundations` package datasheet. The datasheet is an EPC Integrator technical handoff record for civil earthworks and foundation package engineering/design. It is grounded in Workbook Packages row 2, Gate 7 decomposition registers, and the DBM-Deepcut civil basis.

## Principles

- Use source hierarchy conservatively. Workbook row 2 and the Gate 7 registers establish the package identity and physical interface flags; the DBM-Deepcut civil section supplies civil/structural design-basis content.
- Treat the datasheet as a handoff basis, not a final detailed-design calculation package.
- Preserve open design inputs as `TBD` where the DBM ties final values to geotechnical assessment, topographical survey, plot plan, drainage design, or dynamic analysis.
- Do not infer vendor ownership for this civil package. Gate 7 records the responsibility model as EPC Integrator or discipline subcontractor responsibility, source-dependent.
- Keep interface language aligned to the source terms: `Grading / Site Drainage / Spill Containment` and `Structural / Foundations / Supports`.

## Considerations

The current source set supports a civil package datasheet with strong identity/interface definition but limited final design values. The highest-risk open inputs are:

- geotechnical design parameters, including bearing capacity, LPILE curves, dynamic design criteria, pavement design parameters, pavement layer thicknesses, and geotextile need;
- topographical survey and grade surface file details;
- plot-plan coordination for retention pond location;
- detailed drainage design for final IDF duration, ditch/culvert sizing, retention pond capacity, and final pond location;
- compressor dynamic analysis and compressor support verification where the foundation basis affects this package.

The DBM provides preliminary design criteria for site grading, roads, drainage, and foundation concepts. These are appropriate for handoff unless later authoritative project sources supersede them.

## Trade-offs

| Topic | Conservative treatment | Reason |
|---|---|---|
| Preliminary civil criteria | Include stated DBM criteria, but keep final dependent values TBD. | The DBM states several final values depend on later engineering inputs. |
| Interface facts | Carry only the two workbook-supported interface types. | Additional interface types are not marked applicable for PKG-001 in the accessible workbook/register basis. |
| Responsibility | State source-dependent EPC Integrator or discipline subcontractor responsibility. | No separate vendor-package ownership model is supported by current sources. |
| Standards | List civil/structural standards stated by the DBM; avoid clause-level requirements unless source text is available. | The task requires source-grounded drafting and avoids unsupported detail. |

## Examples

TBD. The accessible source set does not provide a completed example package datasheet for this civil package.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| None identified in Pass 1/2 | No direct source conflict was identified between workbook row 2, Gate 7 registers, and the DBM-Deepcut civil source slices. | N/A | N/A | N/A | N/A | N/A |

## Assumptions and TBDs

- ASSUMPTION: `OBJ-001` and `OBJ-008` are directionally relevant because `_CONTEXT.md` and Gate 7 package/deliverable mappings list them for this package/deliverable; they are not treated as additional design requirements without objective text being applied to a specific datasheet requirement.
- TBD: Package-specific exclusions.
- TBD: Final geotechnical and topographical inputs.
- TBD: Final retention pond location and capacity.
- TBD: Final drainage sizing and IDF duration confirmation.
- TBD: Detailed tagged equipment list for the earthworks/foundations datasheet, if required by later source material.
