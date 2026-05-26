# Guidance — DEL-105-02 Package Datasheet (PKG-105 Platforms)

> Directional rationale for producing the Platforms package datasheet. Guidance is not a substitute for source; where source material is silent, this document flags `TBD` rather than fabricating direction.

## Purpose

The Package Datasheet is the EPC Integrator's mandatory Gate 5 anchor deliverable for the Structural "Platforms" package. Its job is to package the workbook-defined identity, governing structural basis, interface obligations, and design conditions into a single source-grounded record that the third-party vendor or discipline engineering team can use to engineer and design platforms for the WBS 01 facility (`_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`; `SCOPE_LEDGER.csv` SOW-0261).

This package is unusual in that interface facts are intentionally carried as datasheet evidence rather than spun off as standalone deliverables (`_CONTEXT.md` Notes). That choice puts an above-average burden on the datasheet to preserve interface fidelity.

## Principles

1. **Source fidelity first.** Every non-trivial entry traces to a register row, scope-ledger row, interface-register row, DBM section, or workbook row. If the source is silent, use `TBD`.
2. **Decomposition routes; it does not design.** The decomposition tells you what artifact this is and where it sits; the DBM and workbook tell you what the platforms must satisfy. Do not promote decomposition prose into design values (`SKILL.md` Authority Hierarchy).
3. **Interface evidence is part of the datasheet.** The three workbook interface types (Lighting, Grading/Drainage/Containment, Structural/Foundations/Supports) and their Gate 6 dispositions belong in the datasheet, not in a separate interface deliverable.
4. **Pile-default with caveats.** The DBM defaults to driven steel piles for "buildings, equipment, towers, tanks, modules, pipe racks, and similar structures." Platforms fall within that generic class; treat pile foundation as default basis but flag that platform-specific verification is part of detailed engineering.
5. **EPC Integrator owns the model-level reconciliation.** Per Gate 6 disposition recorded in `ARTIFACT_REGISTER.csv` and `INTERFACE_REGISTER.csv`, platform-to-equipment tie-ins are resolved via the overall 3D model and integrated P&ID set — not in this datasheet.

## Considerations

- **Tagged equipment is not enumerated in the accessible source slice** for PKG-105. The register Notes describe the package class and interface scope but not specific platform IDs, counts, or geometries. The Major Equipment List is therefore `TBD`.
- **Loading basis is borrowed from project buildings clause** of DBM SEC-11. This is a reasonable structural-engineering default but should be reviewed by the responsible structural engineer; flagged as **ASSUMPTION**.
- **Geotechnical inputs are upstream-blocking**: bearing capacity, LPILE curves, and dynamic design criteria are TBD pending the geotechnical report (DBM SEC-11 §Geotechnical and Topographical Assumptions). Platform foundation sizing cannot close without these.
- **Grading interface coupling**: per DBM SEC-11 §Site Grading and Surface Water Management, pad slopes 1.5% (or 1.0% where required) from main pipe racks. Platform top-of-pile-cap elevations interact with this slope envelope; coordinate via the IFC-07C472C58B (Grading / Site Drainage / Spill Containment) interface fact.
- **Vendor handoff completeness**: per `ARTIFACT_REGISTER.csv` ART-EA98D39386, the handoff must cover technical basis, battery limits, design expectations, and source-supported requirements. Where requirements are not source-supported, mark TBD rather than carrying them as definite.
- **Objective association is heuristic.** OBJ-001/005/008/010 are associated via PACKAGE_HEURISTIC at the package row in `OBJECTIVE_DELIVERABLE_MAP.csv`. OBJ-008 (civil/structural/site support) is the strongest semantic fit; OBJ-005 (electrical) reflects the lighting interface; OBJ-001 (facility scope) and OBJ-010 (handoff readiness) are package-grouping inferences. Label as ASSUMPTION (best-effort mapping).

## Trade-offs

| Trade-off | Direction | Rationale |
|---|---|---|
| Specificity vs. source fidelity | Prefer TBD over inferred value | Skill non-negotiable; downstream design depends on accurate inputs |
| Carrying interface facts inline vs. separate deliverable | Carry inline | `_CONTEXT.md` Notes explicitly direct this; consistent with workbook row 106 grouping |
| Default driven-pile foundation vs. alternate (e.g., bearing/precast) | Default piles | DBM SEC-11 §Piles and Foundations; alternates require justification |
| Adding generic platform design conventions vs. waiting for source | Wait | Decomposition narrative + DBM do not define platform-specific clauses; convention is not authority |
| Loading-clause borrow from buildings to platforms | Use with **ASSUMPTION** label | Loading regime is plausibly common but not stated for platforms specifically in source |

## Examples

The accessible source slices do not contain worked platform examples. None are reproduced here. If/when the workbook row 106 raw text or DBM platform-specific clauses become accessible, examples should be added at that time and cited.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short) | Source A | Source B | Impacted Sections | Proposed Authority (PROPOSAL) | Human Ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-01 | Platform structural loading basis is not explicitly stated for platforms; DBM SEC-11 §Buildings clause applies loading to "project buildings" not platforms. Datasheet borrows the buildings loading regime as ASSUMPTION. | `DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-11 §Buildings and Miscellaneous Facilities | (no explicit platforms loading clause in accessible source) | Datasheet §Conditions; Specification R-3 | Treat NBC Canada loading as applicable to platforms by default until structural engineering states otherwise. | TBD |
| CT-02 | Major equipment list and tagged platform identifiers are absent from the accessible register slice for PKG-105; downstream vendor handoff expects this content. | `PACKAGE_REGISTER.csv` row 106 (no equipment list) | `DELIVERABLE_REGISTER.csv` AnticipatedArtifacts (lists "source-supported equipment and design criteria") | Datasheet §Attributes; Specification R-2, R-12 | Hold as TBD; resolve by re-opening workbook row 106 raw source or a downstream tagged-equipment register. | TBD |
| CT-03 | Objective association OBJ-001/005/008/010 derives from package-heuristic mapping, not deliverable-level mapping. | `OBJECTIVE_DELIVERABLE_MAP.csv` (package-grouped rows) | `_CONTEXT.md` Supports Objectives | Datasheet §Identification; Guidance §Considerations | Carry as ASSUMPTION (best-effort) until human confirms. | TBD |
| CT-04 | Gate 6 disposition delegates platform-to-equipment tie-ins to EPC Integrator's 3D model / integrated P&ID set; this is recorded in artifact notes rather than a normative interface clause. | `ARTIFACT_REGISTER.csv` Notes (ART-39021CDFB3, etc.) | `INTERFACE_REGISTER.csv` Notes (same rows) | Datasheet §Interface Facts; Specification R-7 | Treat Gate 6 disposition as normative for this datasheet; reference both register rows. | TBD |
