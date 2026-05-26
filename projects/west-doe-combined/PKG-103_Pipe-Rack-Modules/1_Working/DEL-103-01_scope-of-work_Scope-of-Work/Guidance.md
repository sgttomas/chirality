# Guidance — DEL-103-01 Scope of Work (Pipe Rack Modules)

> Directional guidance, principles, considerations, and trade-offs for drafting the EPC Integrator Scope of Work for PKG-103. Includes the Conflict Table (for human ruling) per Pass 2.

## Purpose

The Scope of Work establishes the contractual and engineering envelope for PKG-103 "Pipe Rack Modules". It anchors all downstream deliverables in the package (Datasheet, Construction Work Package, Discipline Production Package) and is the Gate 5 EPC anchor record per user instruction. [`_CONTEXT.md`; DELIVERABLE_REGISTER row 584]

Pipe racks are a cross-cutting structural backbone that carries process, utility, relief, electrical, EHT, I&C, and communications commodities across the facility. The Scope of Work must therefore both bound the package (so commodity-design responsibility stays with the originating discipline) and assert the EPC Integrator's exclusive design ownership of the rack modules themselves (per Gate 6 disposition). [INTERFACE_REGISTER rows 909-917; PACKAGE_REGISTER row 104]

## Principles

1. **Workbook-authoritative.** The workbook Packages row 104 (mirrored in PACKAGE_REGISTER row 104) is the authoritative package definition. Do not redefine the package or its boundaries from narrative convention. [PACKAGE_REGISTER row 104; SCOPE_LEDGER row 260 note: "Workbook package row is authoritative"]
2. **Gate 6 design ownership is non-negotiable.** Pipe racks and pipe rack modules are designed exclusively by the EPC Integrator. Any vendor or discipline subcontractor narrative must be reconciled against this disposition. [INTERFACE_REGISTER rows 909-917]
3. **Interface-complete.** All nine interface types attached to PKG-103 must be visible in the SoW; omitting any masks an integration responsibility. [INTERFACE_REGISTER rows 909-917]
4. **TBD over invention.** Where rack-supported commodity lists or detailed equipment tags are not yet confirmed against the plot plan/model, mark TBD. [PACKAGE_REGISTER row 104 note]
5. **Cite the workbook row, not derivative prose.** The decomposition narrative summarises the workbook; the workbook row is the authority.

## Considerations

- **Sour-service and safety.** OBJ-009 (sour-service safety, relief, flare, blowdown, drain/containment, fire/gas, shutdown, environmental, regulatory, codes, standards) flows through the rack package because relief / flare / vent piping is one of the recorded interfaces. The SoW should flag that commodity-level sour-service handling is owned by the originating piping/safety package, while rack support, anchorage, and clearances must accommodate those commodities. [OBJECTIVE_REGISTER row 10 (OBJ-009); INTERFACE_REGISTER row 911]
- **Hazardous-area treatment.** Outdoor racks default to general-purpose non-hazardous, but classification drawings can override; the SoW should not assert a final classification. [DBM-Comp_and_Liquids line 722]
- **Foundation/geotechnical.** The final geotechnical report is required upstream of foundation design closure. The SoW should declare this dependency without consuming it. [DBM-Comp_and_Liquids lines 688, 700]
- **Modular fabrication boundary.** The package name "Pipe Rack Modules" implies modular shop fabrication. The exact modular split, weights, and transport envelopes are not stated in accessible sources — leave as TBD/ASSUMPTION rather than assert a fabrication strategy.
- **Tagged equipment list.** Pipe racks themselves carry few tagged process items but may carry tagged support steel modules, EHT panels, and walkway/access elements. Confirm against plot plan/model before populating. [PACKAGE_REGISTER row 104 note]
- **Companion deliverables.** Avoid duplicating Package Datasheet (DEL-103-02), Construction Work Package (DEL-103-03), and Discipline Production Package (DEL-103-04) content; the SoW should reference, not subsume. [DELIVERABLE_REGISTER rows 585-587]

## Trade-offs

| Trade-off | Discussion |
|---|---|
| Breadth vs. clarity of integration narrative | The SoW must show how PKG-103 integrates across nine interface types without becoming the integration register. Cite the interface register rather than re-listing every interface fact. |
| Commodity ownership boundary | The SoW should be explicit that rack-supported piping/electrical/I&C commodities are owned by their originating packages, while module structure, anchorage, and the rack support system itself are EPC Integrator scope. The workbook does not give a line-item commodity split — keep boundary statements principle-based, not commodity-by-commodity. |
| Open-issue treatment (DEC-001) | DEC-001 is attached to SOW-0259. The SoW should surface and describe DEC-001, but resolving it is not within this deliverable's authority. ASSUMPTION: DEC-001 narrative is in the Open Issues / Decisions register; if not locally accessible, mark `location TBD`. |
| Conservatism on standards | Accessible sources name API RP 505 and a generic snow/wind/seismic criterion set. Do not name specific code editions or load values that the sources do not contain. |

## Examples

No worked SoW example for PKG-103 exists in accessible sources. ASSUMPTION: the structural-style SoW pattern used for adjacent Structural packages (e.g., PKG-102 "Monolithic concrete foundations", PACKAGE_REGISTER row 103) is a reasonable structural-template basis, but it must not be substituted for PKG-103-specific content.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CONF-103-01-01 | Responsibility model: PACKAGE_REGISTER row 104 says EPC Integrator or discipline subcontractor responsibility is "source-dependent" and "no separate vendor-package ownership model is inferred"; INTERFACE_REGISTER Gate 6 disposition states "pipe racks and pipe rack modules are designed exclusively by the EPC Integrator". | `PACKAGE_REGISTER.csv` row 104 (PKG-103 responsibility column) | `INTERFACE_REGISTER.csv` rows 909-917 (Gate 6 disposition note) | Datasheet › Identification (Responsible Party); Specification › SPEC-103-01-R03; SoW › Responsibility assignment record | PROPOSAL: Gate 6 disposition supersedes the workbook-stage responsibility note (Gate 6 > Gate 0). Treat EPC Integrator as exclusive design owner. | TBD |
| CONF-103-01-02 | Hazardous-area classification: DBM-Comp_and_Liquids line 722 says outdoor pipe racks are general purpose non-hazardous "unless detailed classification drawings identify otherwise"; classification drawings are not locally accessible. | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 722 | Classification drawings (not in `_Sources`; location TBD) | Datasheet › Conditions; Specification › SPEC-103-01-R11 | PROPOSAL: state the DBM default and flag classification drawings as TBD upstream input; do not assert a final classification in the SoW. | TBD |
| CONF-103-01-03 | Tagged-equipment list completeness: `_CONTEXT.md` lists "tagged equipment and package identity list" as an anticipated artifact; PACKAGE_REGISTER row 104 says rack-supported commodities should be confirmed against plot plan/model. The plot plan/model is not locally accessible. | `_CONTEXT.md` Anticipated Artifacts | `PACKAGE_REGISTER.csv` row 104 note | Datasheet › Construction; Specification › SPEC-103-01-R13 | PROPOSAL: include the artifact as a placeholder marked TBD pending plot plan/model. | TBD |
| CONF-103-01-04 | Workbook source readability: `26020-Packages_Interfaces_4_export.xlsx` row 104 is the cited authoritative source but is a binary file not directly readable as text. Content is mirrored in PACKAGE_REGISTER row 104. | Workbook (binary) | PACKAGE_REGISTER row 104 (derivative) | Specification › Standards table | PROPOSAL: continue to cite PACKAGE_REGISTER row 104 as the readable mirror; flag that any divergence between workbook and register must be resolved in the register's favor only after re-validation. | TBD |
| CONF-103-01-05 | `26020-Package_Requirements.docx` PKG-103 heading not located: no PKG-103 / 26020-03-36-003 entry was located in accessible derivative material (Trace_Appendix.md and DBM). | `26020-Package_Requirements.docx` (binary) | derivative `Trace_Appendix.md` | Specification › Standards table; SoW › Requirements narrative | PROPOSAL: mark `location TBD`; do not derive requirement text from the package-requirements document until a readable extract is available. | TBD |
