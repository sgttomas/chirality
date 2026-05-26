# Guidance: DEL-105-01 — Scope of Work (PKG-105 Platforms)

## Purpose

This deliverable exists because PKG-105 ("Platforms") is a workbook-recognized Structural package (Workbook Packages row 106; CoA 26020-01-36-005) and the project's Gate 5 EPC convention requires an EPC Integrator-authored Scope of Work for each such package. The SoW exists to define what the package covers, what it does in the facility, who is responsible, and how it integrates with adjacent disciplines.

Source: `_CONTEXT.md` Scope and Notes; DELIVERABLE_REGISTER.csv row `DEL-105-01_scope-of-work`; PACKAGE_REGISTER.csv row PKG-105.

## Principles

1. **Source-anchored content.** The SoW restates and cites what the workbook and DBM say about the package. It does not introduce platform geometry, loads, or equipment lists not present in the source set. (`_REFERENCES.md`; skill authority hierarchy.)
2. **Single responsibility at SoW level.** EPC Integrator authors and owns the SoW. Discipline subcontractor split (if any) is deferred to the EPC / Structural Discipline Production Package (DEL-105-04). (DELIVERABLE_REGISTER.csv responsibility fields for DEL-105-01 vs DEL-105-04.)
3. **Interface honesty.** All three workbook-declared physical interfaces for PKG-105 must be carried forward; none may be dropped at SoW level. (INTERFACE_REGISTER.csv for PKG-105.)
4. **Boundary clarity.** Where boundaries or exclusions are not stated in source, mark `TBD` rather than infer. (PACKAGE_REGISTER.csv exclusions = "TBD; no package-specific exclusions stated in source materials".)
5. **Decomposition does not substitute for source.** Decomposition narrative routes the deliverable; it does not establish design facts. (Skill authority hierarchy.)

## Considerations

- **Tagged equipment list.** Workbook row 106 lists the package as "Platforms" without a transcribed per-tag equipment table in the currently accessible source slice. The detailed major-equipment text "where source-supported" (ARTIFACT_REGISTER.csv ART-21C90A2BB4) should be drawn from `26020-Package_Requirements.docx` package heading for row 106 when that slice is transcribed.
- **Integration narrative.** Platforms in a process facility provide access for operation, inspection, and maintenance of equipment and piping. The DBM does not enumerate platform-by-platform locations; the integration narrative should be expressed at the level the source supports (workbook-recognized package; interfaces with lighting, drainage/spill containment, and structural foundations/supports). Anything more specific is `TBD` until layout/3D-model evidence is available — consistent with the workbook note "Platform-to-equipment tie-ins should be confirmed by layout/model" (PACKAGE_REGISTER.csv row PKG-105).
- **Standards stack.** Platform steel design and fabrication follow the project's governing structural basis (CSA S16, CSA G40.20/G40.21, CSA W59) (DBM `4-25_Deepcut_DBM.md` §Governing Civil and Structural Basis). A walking-working-surface / occupational safety code (guardrails, stairs, ladders, grating) is almost certainly applicable to access platforms (ASSUMPTION: likely applicable) but the specific code text is not transcribed in the accessible sources.
- **Gate 6 disposition is binding.** Platform-to-equipment tie-ins are the EPC Integrator's responsibility through the overall 3D model and integrated P&ID set (INTERFACE_REGISTER.csv notes for PKG-105). The SoW must restate this and not propose an alternative split.
- **Geotechnical dependence.** Platform foundations (where free-standing) depend on the project geotechnical assessment (DBM line 2685). The SoW should flag that platform foundation design parameters are geotechnical-report-dependent.

## Trade-offs

- **Structure-mounted vs free-standing platforms.** Source materials do not specify which platforms in PKG-105 are equipment-mounted vs free-standing on dedicated foundations. The trade-off (foundation cost vs equipment vendor load envelope) cannot be resolved from the current source slice and is `TBD`.
- **Construction walkway vs permanent access.** The DBM distinguishes "construction walkway" (cable-tray modules; not for permanent lighting) (line 3023) from operational access (e.g., 1 m access walkway for the standby generator; line 2076). The SoW should keep these categories distinct and not conflate construction-only walkways with permanent access platforms.
- **Discipline subcontracting model.** Whether platforms are produced fully by the EPC Integrator or partly by a discipline subcontractor is "source-dependent; no separate vendor-package ownership model is inferred from the current sources" (PACKAGE_REGISTER.csv row PKG-105 responsibility note). The SoW must not pre-commit a subcontracting model.

## Examples

- DBM line 116 lists "Installation of miscellaneous structural supports" under Tourmaline field construction scope — directionally indicative of the kind of scope item that would appear in a platforms SoW (ASSUMPTION: directionally relevant).
- DBM line 2076 records "A 1 m access walkway shall be maintained" in the standby-generator context — an example of an explicit minimum-access dimension at the DBM level (not a platform-specific requirement).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-105-01-01 | Anticipated artifacts list differs slightly between `_CONTEXT.md` ("Package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record") and ARTIFACT_REGISTER.csv (4 artifacts with explicit ART-IDs and a "whole-facility integration narrative" wording for ART-1B624DB0B8). | `_CONTEXT.md` §Anticipated Artifacts | ARTIFACT_REGISTER.csv rows for DEL-105-01 | Specification §Documentation; Datasheet §Identification | ARTIFACT_REGISTER.csv (registered ART-IDs and exact titles) governs; `_CONTEXT.md` wording is a non-binding summary. | TBD |
| CT-105-01-02 | Source-availability conflict: `_REFERENCES.md` states "No deliverable-specific source slices copied during PREPARATION," and the binary `26020-Package_Requirements.docx` cannot be slice-read in this run. Downstream artifacts (tagged-equipment list, boundaries/exclusions, battery limits) therefore cannot be fully populated. | `_REFERENCES.md` §Missing / Deferred References | DELIVERABLE_REGISTER.csv anticipated artifacts (requires source-supported detail) | Datasheet §Attributes (Tagged equipment, Boundaries); Specification §Scope (out-of-scope); Procedure §Steps | Mark affected items `TBD` with a pointer to `26020-Package_Requirements.docx` package heading for row 106 until a source slice is transcribed; do not invent. | TBD |
| CT-105-01-03 | Walking-working-surface / occupational safety code (guardrails, stair geometry, grating loading) is not cited in accessible DBM slices, yet such a code is almost certainly applicable to platforms. | DBM §Governing Civil and Structural Basis (lines 2666-2685; 3411-3413) — no walking-working-surface code listed | General professional convention for access platforms | Specification §Standards; Guidance §Considerations | Carry as ASSUMPTION (likely applicable); ruling needed on which specific code (e.g., applicable provincial OH&S / NFPA / OSHA-equivalent) and where it is cited in the project basis. | TBD |
| CT-105-01-04 | Objective association at deliverable-ID level: `_CONTEXT.md` lists OBJ-001/005/008/010 as supported; OBJECTIVE_DELIVERABLE_MAP.csv associates objectives via the PACKAGE_HEURISTIC. Specific objective-to-platform linkage is not asserted by source. | `_CONTEXT.md` §Supports Objectives | OBJECTIVE_DELIVERABLE_MAP.csv (package-grouped) | Datasheet §Identification | Treat as ASSUMPTION (best-effort PACKAGE_HEURISTIC mapping) per skill Step 1.3. | TBD |
