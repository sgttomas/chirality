# Guidance: DEL-041-02 — Package Datasheet (PKG-041)

> Directional guidance for authoring and using the Package Datasheet for the 13.8 kV, 3.0 MW Standby Generator Building (490-1). Rationale is grounded in the Gate-07 PROJECT_DECOMP snapshot; deeper engineering rationale is `TBD` until package-specific source slices are resolved.

## Purpose

The Package Datasheet exists so the EPC Integrator can hand a third-party package vendor (or discipline engineering team) the technical basis required to perform package engineering and design for PKG-041 (DELIVERABLE_REGISTER `DEL-041-02_package-datasheet`; `_CONTEXT.md` Scope). It is the single Gate-5 EPC anchor on which the vendor's engineered equipment package (`DEL-041-04`), vendor documentation (`DEL-041-05`), and EPC review/acceptance (`DEL-041-06`) all depend.

## Principles

- **Source authority over convention.** Per the four-documents skill authority hierarchy, when a workbook or design-basis source slice becomes accessible, it overrides any prose derived from decomposition summaries.
- **Carry interface facts as evidence, not as separate deliverables.** All twelve workbook X-column interface facts for PKG-041 are intentionally carried inside this datasheet (`_CONTEXT.md` Notes; ARTIFACT_REGISTER artifact rows tagged `Interface Fact Evidence`).
- **Vendor handoff completeness over speed.** A `TBD` with a source-location pointer is more useful to a vendor than a fabricated value. The datasheet is read by parties without project context.
- **Stay inside the EPC responsibility split.** Document what the EPC must hand off; do not pre-engineer what the Package Vendor owns (engineering, design, vendor documentation, physical equipment) — see PACKAGE_REGISTER `PKG-041` ResponsibilityModel.
- **One package, one datasheet.** PKG-041 has one Package Datasheet deliverable; sibling deliverables (`DEL-041-01`, `DEL-041-03..06`) cover the other anchor and acceptance roles.

## Considerations

- **Discipline.** Electrical; WBS 01. The package is in the "Deepcut" design-basis grouping (PACKAGE_REGISTER `PKG-041` SourceRefs reference `DBM-Deepcut/4-25_Deepcut_DBM.md`).
- **Twelve required interfaces.** The package crosses Utility Piping, Drain/Containment, Electrical Power, Grounding/Bonding, Area/Exterior Lighting, I&C/Control Cabling, Communications/Network, Building HVAC/Services, Fire & Gas/Safety Systems, Maintenance Access, Grading/Site Drainage/Spill Containment, Structural/Foundations/Supports (INTERFACE_REGISTER). Each must appear in the matrix.
- **Standby duty implies emergency-power conventions.** ASSUMPTION: NFPA 110 / ISO 8528 standby ratings apply; confirm and cite when sources accessible.
- **Hazardous-area classification.** Not source-stated. ASSUMPTION: balance-of-facility may have classified areas; the package boundary classification must be vendor-stated against the EPC area classification drawing (drawing reference TBD).
- **Building enclosure.** Source does not state whether the building is vendor-supplied skid/walk-in enclosure or EPC-built shelter. This is a primary vendor-handoff clarification (TBD).
- **Fuel system.** Not stated; tank sizing, autonomy, and supply-mode interface (`IFC-508C53EB72` Utility Piping) all depend on a vendor-stated genset selection.

## Trade-offs

- **Vendor-skid vs. EPC-built building.** Vendor skid simplifies engineering interfaces (single supplier owns enclosure, HVAC, fuel day-tank) but raises transport/foundation constraints; EPC-built building gives constructability and standardization control but pushes more interface design onto the EPC. Decision rationale `TBD`; surface for human ruling once source slice is accessible.
- **Diesel vs. gas-fueled standby.** Diesel typical for true standby autonomy; gas may be preferred where pipeline fuel is reliable. Choice cascades into NFPA 30 / NFPA 37 / NFPA 110 applicability. `TBD`.
- **Sound attenuation level.** Higher attenuation increases enclosure cost and HVAC load; lower attenuation may breach site noise limits. Site noise criterion `TBD`.

## Examples

Examples of vendor-handoff datasheet values from accessible sources are not present in the local decomposition registers. Omitted pending source-slice access; do not fabricate.

## Conflict Table (for human ruling)

No conflicts identified between locally accessible sources at this draft. New conflicts surfaced in Pass 3 (semantic lensing) will be added here.

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority | Human ruling |
|---|---|---|---|---|---|---|
| _none_ | — | — | — | — | — | TBD |
