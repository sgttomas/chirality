# Guidance: DEL-028-02_package-datasheet

## Purpose

The Package Datasheet exists to convert the accepted Gate 7 package basis for `PKG-028` into a source-supported technical handoff document. It should let the Package Vendor understand the EPC integration basis for the 7.5 MVA, 13.8 kV / 4160 / 2400 V step-down distribution transformer (tag TXP-8801-1) while keeping EPC-owned facility interfaces distinct from vendor-owned package design.

## Principles

- Preserve source spelling and identity. The package name is carried as "Transformer TXP-8801-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 7.5MVA 13.8kV/4160/2400V" because that is the workbook and Gate 7 register spelling.
- Treat workbook interface `X` facts as evidence under the Package Datasheet, not as separate deliverables.
- Keep vendor-owned design work (transformer construction, ratings, cooling, BIL, impedance, taps, monitoring, accessories) with the Package Vendor and facility-level integration (foundations, cabling, grounding, lighting, I&C/comms routing, maintenance access) with the EPC Integrator.
- Use the DBM electrical design basis only at the level it supports: 13.8 kV distribution backbone, medium-voltage cable type, grounding philosophy, foundations convention, oil-filled spacing, and standby-power context.
- Use `TBD` for all package-specific transformer construction values that are not present in the accessible source set.

## Considerations

The DBM establishes the facility electrical system as a BC Hydro 25 kV supply stepped down to 13.8 kV, with the 13.8 kV switchgear as the plant main distribution center feeding radial step-down transformers to electrical buildings and process loads. This positions PKG-028 as a downstream radial 13.8 kV-fed unit that produces 4160 V and 2400 V secondaries. The accessible DBM voltage table characterizes 13.8 kV and 600 V services in detail but does not characterize a 4160 V or 2400 V class secondary; therefore the secondary-side service-basis details (winding configuration, neutral treatment, fault duty, protective relay basis) remain TBD.

DBM grounding requires major electrical equipment to be connected to the ground grid at two points, with ground wells at power transformers and a separate CEC-sized copper ground conductor for distribution transformers. The Package Datasheet should propagate this expectation to PKG-028 without inventing conductor sizes that the accessible source does not specify.

The DBM Transformers subsection treats oil-filled transformers as a facility class subject to CEC spacing and to a documented containment review, but does not confirm that TXP-8801-1 is oil-filled. Construction class should be carried as `TBD`, and the containment requirement should be triggered only conditional on an oil-filled selection.

Foundations are noted in the DBM as "generally precast concrete bearing foundations" for transformers. Package-specific anchor pattern, dead/live loads, seismic class, and oil-containment foundation features are TBD.

Standby power is delivered at the 600 V MCC level via TOU standby generators with transfer switches; a centralized 13.8 kV emergency generator concept has been eliminated. PKG-028 should therefore not assume any standby power feed at 13.8 kV or 4160 V upstream of the transformer; standby coverage of downstream loads is provided at the 600 V level on different feeders.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Construction class (oil-filled vs dry-type) | Mark `TBD`; require containment review only if oil-filled is selected. | DBM allows oil-filled transformers facility-wide but does not specify this unit. |
| Neutral grounding for 4160/2400 V secondaries | Mark `TBD`; do not extrapolate from 6.9 kV (100 A NGR) or 600 V (5 A HRG) values. | DBM grounding paragraph specifies utility (25/13.8 kV), 6.9 kV, and 600 V transformer grounding only. |
| Secondary voltage interpretation (4160 V and 2400 V) | Treat both as nameplate values from the workbook title; do not assign loads, downstream switchgear, or winding configuration. | Accessible sources do not define the downstream loads served by either secondary. |
| Installation location | Identify as unconfirmed; require detailed engineering to assign location, area classification, and foundation context. | DBM does not locate PKG-028. |
| Standards | List CEC, area classification, and project electrical specifications as governing bases with clause/document locations TBD. | DBM references these but exact clauses are not available in the deliverable folder. |

## Examples

- Acceptable datasheet entry: "Applicable interfaces: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: Workbook Packages row 30 and `INTERFACE_REGISTER.csv`."
- Acceptable source-gap entry: "Impedance, cooling class, BIL, and vector group: TBD. No package-specific source slice available."
- Not acceptable without new source: "Transformer is ONAN/ONAF oil-filled with 5.75% impedance and Dyn1 vector group." The accessible source set does not establish these values.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-028-02-001 | The package title carries two secondary voltages (4160 V and 2400 V), but the accessible DBM voltage table characterizes only 13.8 kV and 600 V facility distribution voltages; downstream loads, winding configuration, and switchgear/MCC interfaces for the 4160 V and 2400 V secondaries are not source-confirmed. | Workbook Packages row 30 (title "13.8kV/4160/2400V") | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage and service table (line 2934) and electrical system overview | Datasheet Attributes/Construction; Specification Requirements; Procedure Steps | Carry "4160/2400 V" as title-derived nameplate values only; keep downstream load assignment, switchgear/MCC interfaces, and neutral grounding scheme `TBD` until vendor data or detailed electrical engineering is accepted. | TBD |
| HRR-028-02-002 | Construction class (oil-filled vs dry-type) for TXP-8801-1 is not confirmed by accessible source; DBM permits oil-filled transformers facility-wide and triggers CEC spacing and a containment review when oil-filled, but does not state which class applies to this unit. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Transformers subsection (lines 2947-2949) | Workbook Packages row 30; `PACKAGE_REGISTER.csv` row `PKG-028` | Datasheet Attributes/Construction; Specification REQ-028-02-007; Procedure Steps | Mark construction class `TBD`; require containment review only conditional on an oil-filled selection. | TBD |
| HRR-028-02-003 | Neutral grounding for the 4160/2400 V secondaries is not defined by accessible source; DBM specifies grounding for the BC Hydro utility transformer, each 6.9 kV transformer, and each 600 V transformer only. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraph (line 2985) | Workbook Packages row 30 | Datasheet Attributes; Specification Requirements | Do not assign NGR values to PKG-028; mark secondary grounding scheme `TBD` until protection coordination/electrical study results are accepted. | TBD |
