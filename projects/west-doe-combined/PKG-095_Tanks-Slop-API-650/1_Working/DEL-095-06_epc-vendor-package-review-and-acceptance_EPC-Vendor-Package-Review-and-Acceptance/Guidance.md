# Guidance — DEL-095-06 EPC Vendor Package Review and Acceptance (PKG-095)

> **Directional guidance** for the EPC Integrator performing PKG-095 vendor package review and acceptance. This document is not normative; the Specification is. Use this to interpret intent, weigh trade-offs, and surface conflicts requiring human ruling.

## Purpose

PKG-095 is the Tanks, Slop (API 650) package for the 03-25 / Tanks, Slop facility scope. The vendor delivers package engineering, package design, vendor documentation, and the physical equipment package; the EPC Integrator is responsible for integrating that package into the whole process facility (interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration). This deliverable produces the EPC Integrator's documentary acceptance evidence that the vendor package meets the EPC Scope of Work, Package Datasheet, and Construction Work Package, and is ready for handoff. (Sources: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv DEL-095-06; PACKAGE_REGISTER.csv PKG-095.)

## Principles

1. **Source-grounded acceptance.** Acceptance criteria trace to the Package Datasheet (DEL-095-02) and Scope of Work (DEL-095-01). Where the Datasheet is silent, mark the item `TBD` and route to human ruling; do not invent acceptance values.
2. **Interface completeness.** Every interface type declared for PKG-095 must have an acceptance entry: Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. (Source: PACKAGE_REGISTER.csv PKG-095.)
3. **Slop as a receiver, not just a tank.** Slop service in the 3-25 basis receives liquids from LP fuel-gas scrubber V-3210-2 (to TK-9130-2), LP KO drum V-3900-2 via P-3900-2, and HP KO drum pumps P-4100-2 / P-4150-2. Acceptance must confirm the vendor package can accommodate these routings, not just the static tank scope. (Sources: `3-25_Comp_and_Liquids_DBM.md` lines 463, 497, 499.)
4. **Winterization is a first-class constraint.** Site basis -40 deg C minimum ambient governs winterization, heat tracing, tank heating, drainage protection. The slop tank lives under this basis. (Source: `3-25_Comp_and_Liquids_DBM.md` lines 145, 770.)
5. **No agent-issued approvals.** Only humans sign acceptance. The artifacts produced here record evidence; binding approvals are human acts.

## Considerations

- **3-25 vs PKG-095 mapping.** The PKG-095 package narrative is rooted in Workbook row 91 and 26020-Package_Requirements.docx heading 47; the locally accessible source is the 3-25 DBM (Comp and Liquids). Treat the 3-25 DBM as the closest evidence and explicitly mark anything derived from it that is not echoed by the PKG-095 record as ASSUMPTION until the package-specific source slice is opened.
- **Vendor document register coupling.** This deliverable is downstream of DEL-095-04 (Vendor Engineered Equipment Package) and DEL-095-05 (Vendor Document Turnover Package). Acceptance entries should reference DEL-095-05 register rows where possible.
- **Atmospheric tank class.** The 3-25 DBM defines API-650 Modified atmospheric tanks with external insulation and heating and Devchem 253 internal coating for produced-water tanks. Slop-specific coating and insulation values are not explicitly given in the available slice and should be confirmed against the Package Datasheet.
- **Capacity ambiguity.** The 3-25 DBM enumerates "one slop tank" within the 3,800 bbl condensate-tank class but does not separately state a slop-tank volume. The PKG-095 Package Datasheet is the authoritative source for this value and must be confirmed at acceptance.

## Trade-offs

- **Strict source grounding vs schedule.** Where the Datasheet or vendor submittals are incomplete, `TBD` plus an HRR entry is preferred over a permissive acceptance entry. This protects downstream consumers (commissioning, turnover, regulator audit) at the cost of acceptance velocity.
- **Coating selection (Devchem 253 analog vs slop-specific selection).** Adopting the produced-water tank coating as a default is fast but unsupported by the slop-service slice. The vendor's submittal and the Package Datasheet must explicitly select the coating.
- **Sour-service treatment.** Conservatively scoping slop tank to sour-service rules (NACE MR0175 / ISO 15156) costs material/coating effort; not scoping it risks embrittlement / corrosion failures. The applicable position must be ruled and recorded.

## Examples

- *Interface acceptance example.* A "Relief / Flare / Vent" acceptance row records: (a) vendor P&ID identifier, (b) which design-basis routing it satisfies (e.g., LP KO drum V-3900-2 / P-3900-2 to slop), (c) tie-in flange tag, (d) inspection result. (Pattern; source slice `3-25_Comp_and_Liquids_DBM.md` line 499.)
- *Foundation acceptance example.* A "Structural / Foundations / Supports" acceptance row records the vendor foundation drawing reference, the geotechnical report reference relied upon, and explicit closure of frost / snow / wind / seismic / settlement criteria. (Pattern; source slice `3-25_Comp_and_Liquids_DBM.md` lines 688, 700.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-095-06-01 | Slop-tank capacity not stated in available source slice; the 3-25 DBM enumerates "one slop tank" within the 3,800 bbl condensate-tank class but does not separately confirm slop-tank volume. | `3-25_Comp_and_Liquids_DBM.md` line 406 | PACKAGE_REGISTER.csv PKG-095 (no bbl value) | Datasheet Conditions; Specification R-095-06-12 | PROPOSAL: Confirm capacity from Package Datasheet (DEL-095-02); default to 3,800 bbl only if PKG-095 explicitly inherits the condensate-tank class. | TBD |
| HRR-095-06-02 | Internal coating selection for slop service not given. Produced-water tank class uses Devchem 253; slop service is not explicitly addressed. | `3-25_Comp_and_Liquids_DBM.md` line 421 | (none — slop-specific coating absent) | Datasheet Construction; Specification R-095-06-12 | PROPOSAL: Confirm coating from Package Datasheet; do not adopt Devchem 253 by default. | TBD |
| HRR-095-06-03 | Sour-service applicability to slop tank is not stated. Slop receives mixed off-spec hydrocarbon liquids and may receive sour streams via KO drum routings. | PACKAGE_REGISTER.csv PKG-095 description | `3-25_Comp_and_Liquids_DBM.md` lines 497, 499 (slop receives routed liquids) | Specification R-095-06-11; Procedure verification | PROPOSAL: Treat as sour-service applicable until ruled otherwise. | TBD |
| HRR-095-06-04 | Objective association uses PACKAGE_HEURISTIC: OBJ-002 through OBJ-010 are package-grouped, not deliverable-specific. | DELIVERABLE_REGISTER.csv DEL-095-06 | `OBJECTIVE_ASSOCIATION_MODE: PACKAGE_HEURISTIC` (this run) | Datasheet Identification (Supports Objectives) | PROPOSAL: Carry as ASSUMPTION (best-effort mapping); human confirms before acceptance signoff. | TBD |
| HRR-095-06-05 | "Slop-routing" requirement R-095-06-06 cites 3-25 DBM tag-specific routings (TK-9130-2, V-3900-2, P-3900-2, P-4100-2, P-4150-2). PKG-095 may or may not inherit identical tag scope. | `3-25_Comp_and_Liquids_DBM.md` lines 463, 497, 499 | PACKAGE_REGISTER.csv PKG-095 (tag 26020-03-PT-19-004) | Specification R-095-06-06 | PROPOSAL: Verify against PKG-095 vendor P&IDs at submittal review; treat 3-25 routings as expected pattern only. | TBD |
| HRR-095-06-06 | Package-specific exclusions field for PKG-095 reads "TBD; no package-specific exclusions stated in source materials." | PACKAGE_REGISTER.csv PKG-095 | (none) | Specification R-095-06-13; Procedure | PROPOSAL: Record "no exclusions" only after explicit confirmation by the EPC Integrator and Package Vendor. | TBD |
