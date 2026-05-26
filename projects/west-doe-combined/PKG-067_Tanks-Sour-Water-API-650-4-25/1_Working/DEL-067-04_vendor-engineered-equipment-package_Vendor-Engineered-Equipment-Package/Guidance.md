# Guidance — DEL-067-04 Vendor Engineered Equipment Package (Tanks, Sour Water — API 650, 4-25)

## Purpose

This deliverable exists to procure the physical sour-water (produced-water) tank package from a Package Vendor whose responsibility set covers package engineering, design, vendor documentation, and the physical equipment, while the EPC Integrator retains responsibility for facility integration, interfaces, tie-ins, constructability, and procurement/construction coordination. (Source: PACKAGE_REGISTER.csv row 94 — "Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility…"; DELIVERABLE_REGISTER.csv row 531.)

## Principles

- **Source first.** The DBM-Deepcut entry for produced-water storage (DBM §"Waste Streams and Disposition — Produced Water") is the governing technical basis until vendor data refines it. Do not let vendor preferences silently overwrite DBM design intent without a recorded change.
- **Atmospheric API 650 with sour-service awareness.** The DBM directs a modified API 650 atmospheric tank with internal coating, external insulation and heating, hydrocarbon skim, and PVRV venting; however, sour-service isolation is explicitly TBD. Engineering should treat sour vapour as credible during HAZOP and isolation philosophy review. (DBM §"Produced Water" prose; §"Assumptions and Unresolved Requirements".)
- **Conservative SG, validated later.** The DBM uses **1.18** as a conservative pump SG and **1.25** (TBC) as the tank design SG. Sizing should adopt 1.25 until detailed engineering confirms the actual produced-water density envelope. (DBM §"Produced Water" prose.)
- **Coating equivalence requires evidence.** Devchem 253 is the named internal coating. A vendor proposing an equivalent should provide chemical-compatibility, application, and service-life data, and have the substitution accepted by the EPC Integrator.
- **Vent system completeness.** PVRV per API 2000 covers normal in-/out-breathing; EPRV sizing must close before commissioning. Leaving EPRV as TBD into construction is a risk.

## Considerations

- **Trace contaminant list is incomplete.** Produced water "may contain trace lube oils, hydrocarbons, TEG, amine, H2S, caustic, and mercaptans. The list is not comprehensive and is to be confirmed." (DBM §"Produced Water" prose.) Materials, coating life, and vent sizing should be reviewed once the composition is closed.
- **Capacity/turnover.** 2 x 2,000 bbl at 380 bbl/d gives ~8.9 days storage at design throughput (DBM §"Product Storage and Distribution Summary"); operations expect ~60 m³/d continuous accumulation with ~240 m³/d batch pump-out to the 03-25 Liquids Hub (DBM §"Produced Water" prose). Tank-pair scheduling and outage tolerance should be discussed with the operator.
- **Truck-out paths.** A common envirobox truck-out connection is required (DBM §"Produced Water" table). Vacuum-truck assumption is 2.75 m³/min (TBC). Confirm the operator's preferred B-train basis (55 m³ / 20 min).
- **Spacing compliance is an EPC integration check.** API 2510, NFPA 30, and OGAOM-driven spacing live in DBM §2.5 and are enforced at the plot plan. The tank package must not assume a footprint that violates these distances. (DBM §"Atmospheric Tank and General Plant Spacing".)
- **Sibling deliverables provide the wrappers.** DEL-067-01 (Scope of Work) and DEL-067-02 (Package Datasheet) are the EPC-issued inputs; DEL-067-03 (CWP) governs construction; DEL-067-05 (Document Turnover) and DEL-067-06 (Acceptance) close out the package. (DELIVERABLE_REGISTER.csv rows 528–533.)

## Trade-offs

- **Heater type.** Steam coils, electric immersion, and external heat-traced jacket each carry different sour-service, maintenance, and electrical-area-classification impacts. The DBM does not pick one. Vendor proposal should justify selection against winter operability and produced-water composition.
- **PVRV count vs single-large device.** Multiple smaller PVRVs improve isolation availability during PM but increase nozzle count and weight; a single larger device simplifies maintenance scheduling. Either is consistent with "at least one PVRV" (DBM §"Produced Water" prose).
- **Internal coating substitution.** Equivalent epoxy systems may reduce cost but require qualification data; Devchem 253 is the named baseline. (DBM §"Produced Water" prose.)
- **EPRV deferral.** Deferring EPRV sizing to detailed engineering is permitted by the DBM but lengthens the late-cycle change window if sizing reveals upstream sources (e.g., relief routing) needing rework. (DBM §"Produced Water" prose.)

## Examples

- **Worked storage check (illustrative, from DBM table):** at the DBM design throughput of 380 bbl/d to 2 x 2,000 bbl tanks, residence is 4,000/380 ≈ 10.5 days; the DBM lists 8.9 days using its own accounting basis. The number to use for operational planning is the DBM-stated 8.9 days. (DBM §"Product Storage and Distribution Summary".)
- **Spacing constraint example:** two atmospheric tanks must be separated by at least 2.35 m (7.72 ft) per NFPA 30 Table 22.4.2.1 (DBM §2.5). For the 2-tank set TK-9010-1 / TK-9020-1, this is the controlling tank-to-tank distance.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short) | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-01 | Stored-fluid trace composition is "not comprehensive (TBC)" — material selection and coating-life require a closed list. | DBM §"Produced Water" prose: trace H2S, mercaptans, hydrocarbons, TEG, amine, caustic, lube oils (not comprehensive, TBC) | No closed composition list in `_REFERENCES.md` | Specification R2.3, R3.1; Datasheet Conditions | Use DBM-stated trace list as the design envelope; flag for confirmation before fabrication release. | TBD |
| CT-02 | Tank design SG is 1.25 (TBC) vs pump design SG 1.18 (conservative). | DBM §"Produced Water" prose | DBM §"Produced Water" prose | Specification R2.1; Datasheet Conditions | Use 1.25 for tank sizing; pump basis remains 1.18 — both are intentionally different. | TBD (confirm SG closure during detailed engineering.) |
| CT-03 | EPRV sizing and sour-service isolation philosophy explicitly TBD; risk if not closed before construction. | DBM §"Produced Water" prose; §"Assumptions and Unresolved Requirements" | n/a | Specification R5.3, R5.4; Datasheet "Sour-service isolation" | Open as a tracked TBD with a closure target before vendor IFC drawings. | TBD |
| CT-04 | Source `26020-Package_Requirements.docx` package heading 22 referenced as authority but is a binary DOCX not text-readable in this run. | `_CONTEXT.md` "Source Reference"; `_REFERENCES.md` | DBM-Deepcut (accessible) used as proxy | All sections | Convert DOCX to markdown during PREPARATION and re-issue source slices to this deliverable. | TBD |
| CT-05 | Objective associations (`OBJ-001`, `OBJ-003`–`OBJ-010`) are inherited via PACKAGE_HEURISTIC (ASSUMPTION). | `_CONTEXT.md` "Supports Objectives" | OBJECTIVE_DELIVERABLE_MAP.csv (not inspected at deliverable-ID granularity) | Datasheet Identification (Supports Objectives) | Keep as ASSUMPTION until decomposition publishes a deliverable-ID-level objective mapping. | TBD |
