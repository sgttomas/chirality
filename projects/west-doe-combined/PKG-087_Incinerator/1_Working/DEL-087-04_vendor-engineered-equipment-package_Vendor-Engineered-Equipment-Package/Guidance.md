# Guidance — Vendor Engineered Equipment Package (DEL-087-04)

> Directional guidance to support engineering judgement when executing the Package Vendor production unit for the PKG-087 Incinerator. Source-anchored; rationale only — not normative requirements.

## Purpose

This deliverable is the Package Vendor production unit. It exists to translate the EPC Scope of Work (DEL-087-01) and the EPC Package Datasheet (DEL-087-02) into an engineered, designed, and supplied incinerator equipment package — distinct from the EPC integration scope so that vendor engineering, vendor documentation, equipment supply, and EPC integration review remain separately owned. [`PACKAGE_REGISTER.csv` Description; `OBJECTIVE_REGISTER.csv` OBJ-004; `_CONTEXT.md`]

The package itself destroys vent streams from spent-caustic storage and the caustic-treating overhead system within the 03-25 / 04-25 shared-interface envelope. Its design integrity is therefore intertwined with caustic-treating, flare-header, and shared-interface decisions made elsewhere in the facility. [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 56, 400, 402, 547]

## Principles

1. **Vendor owns engineering; EPC owns integration.** The Package Vendor is responsible for package engineering, package design, vendor documentation, and physical equipment package supply. The EPC Integrator is responsible for facility-level integration, interfaces, tie-ins, constructability, and procurement / construction coordination. Avoid silently absorbing integration work into the vendor package or vice versa. [`PACKAGE_REGISTER.csv` Description; `OBJECTIVE_REGISTER.csv` OBJ-004]
2. **EPC Datasheet is the design basis input.** The package design should be driven from the EPC Package Datasheet (DEL-087-02) and Scope of Work (DEL-087-01). Where vendor judgement is required, document the assumption and route it for EPC ruling rather than diverging silently. [`DELIVERABLE_REGISTER.csv` DEL-087-01, DEL-087-02]
3. **Treat the shared-interface as governing.** The HP/Cryo and LP dual flare stack and incinerator are shared-interface systems across 03-25 / 04-25. Service-split and ownership are open interface items. Vendor design should preserve flexibility (capacity, materials, controls) until the EPC Integrator confirms allocation. [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 56, 547]
4. **Caustic-service discipline.** Caustic systems impose strict material constraints (no aluminum), drain-rating constraints (300# ANSI minimum), and temperature constraints (TBC at 121 deg C / 250 deg F). These propagate to incinerator inlet headers, knockout-drum drains, and the spent-caustic vent route. [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 402, 493]
5. **Design for -40 deg C site.** Winterisation, freeze protection, and cold-start considerations are facility basis, not optional. [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 696]
6. **Documentation drives turnover.** Vendor documentation completeness is a closure condition under OBJ-010; missing vendor documents block DEL-087-05 (turnover) and DEL-087-06 (acceptance). [`OBJECTIVE_REGISTER.csv` OBJ-010; `DELIVERABLE_REGISTER.csv` DEL-087-05, DEL-087-06]

## Considerations

### Process and Capacity

- The caustic-oxidation demand carried in the DBM is 214 SCFM (TBC). This is one of several contributing loads and should not be treated as the full incinerator capacity basis without confirmation. [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 477]
- Final emissions / permit data are not yet established; vendor capacity sizing therefore needs to anticipate permit-driven turndown, combustion-efficiency, and stack-discharge constraints that may emerge during permit finalisation. [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 555]
- Inlet composition depends on the upstream caustic treating package (Merichem or equivalent), its DSO/spent-caustic handling, and any other vent contributors confirmed by the EPC Integrator. [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 389, 400]

### Materials and Mechanical

- Caustic-wetted components require coating/material reviews; aluminum is excluded. Embrittlement is a known concern for caustic drain service. [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 402, 493]
- Heat tracing on caustic drains is "under consideration" at 37.8 deg C / 100 deg F with redundant circuits in the DBM; coordinate with EPC for the final position. [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 493]
- Knockout-drum sizing, transfer-pump NPSH, and stack draft control are vendor engineering decisions — but they cascade into facility drain, slop, and flare-header design owned by the EPC.

### Interfaces

- Twelve interface categories are applicable to PKG-087. Each is a likely site of ambiguity between vendor and EPC scope; the vendor interface schedule should mirror the GATE-07 interface register row-for-row to surface gaps early. [`INTERFACE_REGISTER.csv` (PKG-087 rows)]
- Fire & Gas detection at the package boundary should anticipate H2S, methyl mercaptan, LEL, and fire-detection coverage; final detector placement is an EPC F&G design responsibility informed by vendor layout. [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 838]

### Trade-offs

- **Skid integration vs. site assembly.** A larger skid simplifies vendor responsibility but adds shipping, lift, and foundation complexity for the EPC. A lighter skid eases construction but expands site interface work and increases EPC engineering scope. [ASSUMPTION — general vendor-package trade-off]
- **Capacity headroom vs. emissions/permit risk.** Oversizing reduces re-work if shared-interface allocation grows; undersizing risks future capacity expansion. Until the 03-25/04-25 split is ruled, conservative capacity headroom is defensible. [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 56, 547, 555]
- **Vendor controls scope vs. EPC controls topology.** Self-contained vendor controls accelerate package supply but may complicate integration into the EPC cause-and-effect/shutdown framework under OBJ-006. [`OBJECTIVE_REGISTER.csv` OBJ-006]

## Examples

- **Spent caustic vent path** — the spent-caustic tank vents via a flame arrestor into the incinerator header. Vendor design must accept this configuration as an inlet boundary condition rather than redesigning the upstream relief path. [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 402]
- **Caustic-treating overhead/dilution/enrichment-gas interfaces** — the C5+ caustic treating package routes overhead/dilution/enrichment gas to the incinerator. These streams contribute to inlet composition and capacity. [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 400]

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-01 | Decomposition (`PACKAGE_REGISTER.csv` PKG-087 Description) says incinerator receives vapours from the **caustic regeneration column overheads**, but the 03-25 DBM states **caustic regeneration is not part of the current 03-25 basis** (non-regenerative treating). | `PACKAGE_REGISTER.csv` (PKG-087 Description) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 389 | Datasheet (process function, attributes), Specification R2 (process function and inlet streams), Guidance (Process and Capacity) | PROPOSAL: treat the DBM as authoritative on caustic-treating technology (non-regenerative); interpret the decomposition "regeneration column overheads" as a colloquial reference to caustic-treating overheads. Incinerator inlets = spent-caustic tank vapours + C5+ caustic treating overhead/dilution/enrichment-gas streams. | TBD |
| CONF-02 | Decomposition lists the incinerator package under PKG-087 (a 03-25-anchored package via OBJ-002), but the DBM notes the LP flare stack and incinerator are **shared-interface systems** with 04-25, and the 03-25/04-25 service split is unresolved. | `PACKAGE_REGISTER.csv` (PKG-087 row, OBJ-002 anchor) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 56, 547 | Datasheet (Identification — Facility Anchor; Conditions — emissions), Specification R2.2 (shared-interface allocation), Guidance (Principles, Considerations) | PROPOSAL: the vendor package is anchored at PKG-087 / 03-25 for ownership and decomposition tracking, while capacity, allocation, and ownership of any shared service to 04-25 are open interface items to be ruled by the EPC Integrator prior to package design freeze. | TBD |
| CONF-03 | `26020-Package_Requirements.docx` package heading 40 is now locally accessible (entry "26020-02-PT-25-003 - Incinerator", Basic Scope + Major Included Equipment, slice 510-515 in paragraph index). Equipment tags (V-6900-1, P-6900-1, FL-6920-1, B-6920-1) and primary design data are extracted into Datasheet/Specification. The Physical Interface Summary, Vendor Engineering Deliverables list, Interface Coordination Notes, and broader standards/vendor-document tables remain TBD at the same source ("Interface source: `26020-Packages_Interfaces.3.xlsx`"; "Interface Coordination Notes: TBD"). | `_REFERENCES.md` Source Materials Referenced By Decomposition Row | `26020-Package_Requirements.docx` package heading 40 (slice 510-521) — partially resolved | Specification (Standards, Documentation), Datasheet (Bid Document Reference, Equipment Constituents, Design Conditions), Procedure (Prerequisites) | PROPOSAL: mark CONF-03 partially resolved (equipment scope and tags resolved from source). Retain `location TBD` only for the Interface Schedule (referenced to `26020-Packages_Interfaces.3.xlsx`), Vendor Engineering Deliverables table, governing standards list, and Vendor Document tables that the source slice does not contain. | TBD |
