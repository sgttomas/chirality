# Guidance: DEL-050-03 — Construction Work Package

## Purpose

The Construction Work Package is the Gate 5 EPC anchor deliverable that converts the package Scope of Work (DEL-050-01) and Package Datasheet (DEL-050-02) into an executable construction plan for the `PKG-050 Stabilizer Overheads Compressors`. It exists because the Package Vendor (DEL-050-04) supplies engineering, design, and physical equipment, but the EPC Integrator owns the facility integration boundary — and that boundary is where construction risk concentrates (PACKAGE_REGISTER row PKG-050, ResponsibilityModel).

## Principles

- **Responsibility-boundary discipline.** The construction work package describes EPC-side work and EPC/vendor interface management, not vendor-internal fabrication. (PACKAGE_REGISTER row PKG-050.)
- **Interface-first planning.** All 13 applicable interface types listed in PACKAGE_REGISTER row PKG-050 (Process Piping, Utility Piping, Relief/Flare/Vent, Drain/Containment, Electrical Power, EHT, Grounding/Bonding, Area/Exterior Lighting, I&C/Control Cabling, Building HVAC/Services, Fire & Gas/Safety Systems, Maintenance Access, Structural/Foundations/Supports) should be treated as first-class planning units.
- **Two-train symmetry.** Because the package is 2x100% (two identical compressor trains), construction sequencing should make the two trains substantially interchangeable to preserve operational redundancy through commissioning. (PACKAGE_REGISTER row PKG-050, ScopeDescription.)
- **Tie-in directionality.** Suction at 50 psig and discharge at 1100 psig route to/from defined facility points (amine inlet filter coalescer; first-stage recycle); tie-in design should respect this directionality and pressure step. (PACKAGE_REGISTER row PKG-050.)
- **Source-grounded specificity.** Where the accessible registers are silent (area classification, ambient envelope, seismic basis, noise limits), the work package should defer to project-level documents rather than invent values.

## Considerations

- **Equipment characteristics drive constructability.** Separable reciprocating compressors typically present pulsation, vibration, foundation-mass, and alignment considerations during installation. The work package should identify whether vendor analyses (pulsation study, mechanical analysis) gate any field activities. (ASSUMPTION grounded in equipment type; detailed gates TBD.)
- **Electrical classification.** Hydrocarbon compression duty typically implies a classified area; electrical installation methods (cables, glands, EHT) must conform. Specific classification not in accessible source slice — location TBD.
- **Turnover readiness.** DEL-050-06 (EPC Vendor Package Review and Acceptance) consumes the inspection/test/turnover evidence produced under this deliverable; the checklist structure should align to DEL-050-06's acceptance shape.

## Trade-offs

- **Modular vs. stick-built tie-ins.** Modular pre-fabrication of pipe spools reduces field exposure but increases vendor coordination burden. The work package should make the choice explicit per interface type. (No project preference is recorded in the accessible registers — TBD.)
- **Schedule for two trains.** Parallel construction of both trains compresses schedule but doubles peak crew loading; staggered construction protects schedule risk but extends overall duration. Project preference is TBD.
- **Commissioning windows.** Early energization of EHT/lighting may be required before mechanical completion; the workface plan should sequence enabling utility tie-ins ahead of process tie-ins.

## Examples

Concrete examples from project execution history are not available in the accessible source slices (no prior construction records in this deliverable folder). Mark as TBD; pull patterns from analogous PKG-xxx Construction Work Packages once produced.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-050-03-01 | Standards traceability (e.g., API 618, NEC/IEC 60079) is plausible but not derived from an accessible source slice. | This deliverable's Specification §Standards (ASSUMPTION) | `26020-Package_Requirements.docx` heading 5 (not parseable in this run) | Specification §Standards; Datasheet §Conditions | Resolve by extracting the .docx clauses; treat source-extracted standards as authoritative | TBD |
| C-050-03-02 | `_REFERENCES.md` notes "No deliverable-specific source slices copied during PREPARATION," yet PACKAGE_REGISTER row PKG-050 provides substantive process content. | `_REFERENCES.md` Missing/Deferred References | `PACKAGE_REGISTER.csv` PKG-050 | Datasheet §Attributes; Specification §Scope/Requirements | Treat PACKAGE_REGISTER row as locally accessible authoritative slice; copy source slices for .docx in a follow-on PREPARATION pass | TBD |
