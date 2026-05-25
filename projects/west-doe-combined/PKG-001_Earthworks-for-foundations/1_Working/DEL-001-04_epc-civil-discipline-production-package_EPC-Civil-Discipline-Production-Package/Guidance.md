# Guidance: DEL-001-04_epc-civil-discipline-production-package

## Purpose

This guidance supports preparation and review of the EPC / Civil Discipline Production Package for PKG-001, Earthworks for foundations. The deliverable exists to carry the Civil production basis for a non-vendor package while preserving source limits from the accepted Gate 7 decomposition.

The useful posture for this deliverable is conservative: workbook row 2 establishes package identity and interface flags; Gate 7 establishes downstream decomposition truth; DBM SEC-11 supplies the civil basis. Values that depend on missing geotechnical, topographical, plot-plan, hydrology, or detailed engineering inputs should stay open.

## Principles

- Preserve workbook facts exactly: WBS 01, CoA tracking number 26020-01-42-001, package name Earthworks for foundations, Civil discipline, and the two workbook interface flags.
- Treat Gate 7 registers as accepted decomposition truth for package identity, deliverable identity, anticipated artifacts, objectives, and source-limited notes.
- Use DBM civil sections for governing civil design basis, not generic civil practice.
- Distinguish basis requirements from closure gaps. The DBM intentionally leaves several civil values open pending later inputs.
- Do not convert decomposition narrative into final construction criteria unless supported by an accessible source slice.

## Considerations

| Topic | Guidance | Source |
|---|---|---|
| Objective alignment | OBJ-001 is broad facility-scope context; OBJ-008 is the more directly relevant civil/structural/site/construction-support context. Treat both as context, not as detailed construction requirements. | Gate 7 `OBJECTIVE_REGISTER.csv`; `OBJECTIVE_DELIVERABLE_MAP.csv` |
| Package responsibility | The responsible party remains TBD between EPC Integrator and discipline subcontractor. Draft work products should identify the accountable organization once assigned rather than assuming one. | `_CONTEXT.md`; Gate 7 `PACKAGE_REGISTER.csv` |
| DBM civil basis | SEC-11 defines the civil, structural, site-grading, drainage, road, foundation, building, and miscellaneous-facility basis for the Deepcut expansion. Use it as the governing civil source slice for this package. | `DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Civil Scope |
| Open inputs | Geotechnical assessment, topographical survey/grade surface, plot plan, detailed drainage design, and compressor dynamic analysis are external inputs. Their absence should drive `TBD` entries, not assumed values. | `DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 External Dependencies |
| Plot plan dependency | Coordinate-level layout, final road/access geometry, and drawing conflict checks remain TBD pending CIV-235633-5002. Avoid layout-final language before that drawing is accepted. | `DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-02 Plot Plan Status |

## Trade-offs

- A concise discipline production basis is preferable to an over-detailed package that invents unsupported values. The current source set supports package identity, interface categories, civil basis criteria, and open input tracking.
- Some DBM criteria are sufficiently explicit for basis use, such as grading/drainage principles and default driven-steel-pile foundation basis. Other items, such as bearing capacity, pavement thicknesses, retention pond capacity, and final IDF duration, remain unsuitable for closure.
- The package name is Earthworks for foundations, but the accepted DBM source slice covers broader civil basis. Keep the package focused on earthworks/foundations while referencing broader civil criteria only where they constrain that package.

## Examples

| Use | Acceptable Wording |
|---|---|
| Supported value | "Facility pad grading shall use the DBM basis of slopes down from pipe racks at 1.5% to each side, with reduction to 1.0% where required to maintain reasonable top-of-pile-cap elevations." |
| Open value | "Bearing capacity: TBD pending geotechnical assessment report." |
| Unsupported detail | "Final retention pond capacity: TBD pending plot plan coordination and detailed engineering." |
| Assumption | "ASSUMPTION: PKG-001 production package will use DBM SEC-11 civil basis as the initial civil criteria until project-specific civil design deliverables supersede it." |

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| None identified | No direct source conflict identified during Pass 1+2. Remaining gaps are missing inputs/TBDs rather than contradictory evidence. | N/A | N/A | N/A | N/A | N/A |
