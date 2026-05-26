# Guidance — DEL-042-02 Package Datasheet (PKG-042 Control Room Building)

> Directional document. Captures rationale, considerations, and trade-offs. Not a substitute for the Specification.

## Purpose

The Package Datasheet is the EPC Integrator's technical handoff for the Control Room Building. Its job is to give a third-party vendor or a discipline package engineer the **data they need to engineer, design, fabricate, and integrate** the building without having to reconstruct the facility design basis. Per the decomposition note, "interface facts are intentionally carried here as evidence rather than standalone deliverables" (`_CONTEXT.md`).

## Principles

1. **Source-anchored content over narrative.** A datasheet exists to carry values a downstream party can act on. Decomposition prose and convention do not substitute for source text; if the source is not locally accessible, the value is `TBD` and the source is cited with `location TBD`.
2. **Carry interface facts here.** PKG-042 is the EPC anchor for control-room interfaces (controls network, alarms, secondary server siting, packaged-equipment monitoring). Do not push these into separate deliverables.
3. **Discipline label is shorthand.** `_CONTEXT.md` labels Discipline = Electrical, but the building is a coordination unit: controls/IT, civil/structural, HVAC, F&G, and electrical all converge. Treat the Electrical label as the lead discipline and explicitly route the other interfaces in the Interface Requirements Matrix.
4. **Two-facility ambiguity is real.** The accessible DBMs describe two facilities (Deepcut 04-25 and Comp_and_Liquids 03-25) that each reference a control room. Decomposition does not bind PKG-042 to one. Use the Conflict Table.

## Considerations

- **Server siting.** Primary controls hosts in the control room, secondary host in the MCC area. This drives floor-load, UPS, HVAC redundancy, cable routing, and access control requirements that the datasheet should surface even when exact load values are TBD. [DBM-Deepcut §3165; DBM-Comp_and_Liquids §796]
- **Operator workstation footprint.** Three workstation sets with 4 monitors each (initial design basis) drives furniture layout, lighting, sightlines, and HVAC heat-load assumptions. [DBM-Deepcut §3184]
- **Alarm beaconing.** Control room exterior beacons mean the building envelope carries facility-wide visibility; siting matters. [DBM-Deepcut §3262, §3293]
- **Spacing minima are hard constraints.** 50 ft from pressurized bullets, 82 ft from fired heaters. These constrain plot plan revisions and any future expansion. [DBM-Deepcut §254, §298]
- **Construction mode.** Package list designates 800-1 Office/Control Building as "Shop", and the DBM tells installers to "install on site or modify if already existing". This means the vendor delivers a building, not a stick-built. Trade-off: transport limits set the maximum module dimensions. [DBM-Deepcut §2810, §2759]
- **Wiring method.** EMT is permitted in the control room as a non-process location; this is a cost/maintenance lever the vendor should know up front. [DBM-Deepcut §3025]

## Trade-offs

| Trade-off | Pros | Cons | Where decided |
|---|---|---|---|
| Single building vs. control room + separate IT room | Lower footprint; simpler interfaces | All eggs in one envelope; HVAC and fire risk concentrated | Facility design basis (TBD) |
| Primary servers in control room vs. dedicated server room | Operator proximity; lower cable distances | Heat load and noise in operator space | DBM specifies primary in control room [§3165] |
| Thin-client vs. thick-client operator workstations | Centralized management vs. local resilience | TBD | Detailed design [§3184] |
| Shop-fabricated module vs. stick-built | Schedule certainty; quality control | Transport constraints; tie-in complexity | Package list designation "Shop" [§2810] |

## Examples

- The Deepcut DBM enumerates beacon group locations as: "outdoors at strategic points on the piperacks", "control room exterior", "building containing the main balance of plant control system PLCs", "near the NGL Storage Area", and "near the atmospheric storage tank area" [§3262]. The datasheet need only carry the row that names the control room.
- Conduit sizing minimum of 21 mm (3/4 in) is project-wide [§3025]; carrying it in the datasheet ensures the vendor does not propose smaller building-internal runs.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted Sections | Proposed Authority | Human Ruling |
|---|---|---|---|---|---|---|
| C-001 | Which facility (Deepcut 04-25 vs. Comp_and_Liquids 03-25) is the PKG-042 control room? Both DBMs describe a central control room with overlapping content. | DBM-Deepcut `4-25_Deepcut_DBM.md` §3119, §3141, §3165 | DBM-Comp_and_Liquids `3-25_Comp_and_Liquids_DBM.md` §75, §658, §796 | Datasheet Identification, Hosted Equipment, Construction; Specification R-2..R-12 | PROPOSAL: Both — treat PKG-042 datasheet content as facility-agnostic where DBMs agree; flag facility-specific deviations (e.g., secondary server in "MCC" vs. "low-voltage MCC room") as separate rows | TBD |
| C-002 | Source primary text for API 2510, OGAOM §9.6.15, and CEC clauses cited via DBM is not locally accessible. | DBM-Deepcut §254, §298, §3025 | (no second source) | Specification R-8, R-9; Datasheet Spacing/Construction | PROPOSAL: Carry DBM-cited values verbatim; mark standard text "location TBD". | TBD |
| C-003 | `26020-Package_Requirements.docx` and `26020-Packages_Interfaces_4_export.xlsx` are present in `_Sources/` but not text-readable in this environment. They likely contain authoritative package-row data (Workbook Packages row 44). | `_Sources/26020-Package_Requirements.docx` | `_Sources/26020-Packages_Interfaces_4_export.xlsx` | All four documents | PROPOSAL: Re-run with extraction tool (docx2md, xlsx2csv) to extract row 44 and re-anchor datasheet values; current values that depend on these sources are TBD. | TBD |
| C-004 | Discipline = Electrical (per `_CONTEXT.md`) understates the multi-discipline coordination scope evident in the DBMs (controls/IT, civil/structural, HVAC, F&G, electrical). | `_CONTEXT.md` (Discipline=Electrical) | DBM-Comp_and_Liquids §704 (coordination items) | Datasheet Identification; Specification R-14 | PROPOSAL: Keep Discipline=Electrical as lead; explicitly enumerate co-discipline interfaces in matrix. | TBD |
