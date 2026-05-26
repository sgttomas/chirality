# Guidance — DEL-042-04 Vendor Engineered Equipment Package

Directional guidance for drafting, reviewing, and accepting the Package Vendor's engineered Control Room Building equipment package under PKG-042.

## Purpose

This deliverable carries the Package Vendor's engineering, design, and physical equipment scope for the Control Room Building. It exists as a distinct production unit (separate from EPC-Integrator anchor deliverables `DEL-042-01` and `DEL-042-02`) to make vendor ownership and the boundary between vendor scope and EPC integration explicit (Gate 7 `PACKAGE_REGISTER.csv` `PKG-042` ResponsibilityModel).

## Principles

- **Vendor produces, EPC integrates.** The Package Vendor owns the package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination, and acceptance review (`PKG-042` ResponsibilityModel).
- **Authority chain for content.** EPC Scope of Work (`DEL-042-01`) and Package Datasheet (`DEL-042-02`) are upstream inputs; the DBMs (`3-25_Comp_and_Liquids_DBM.md` and, where its provisions reach across the project, `4-25_Deepcut_DBM.md`) provide the design-basis source for control-room siting, building services, and interior wiring; workbook row 44 is the registration basis.
- **Building function anchors content.** The control room is the operations environment from which the facility is monitored and controlled (DBM §3119) and hosts the primary control-system server, operator/engineering workstations, and core network switches (DBM §796, §3141). The vendor package must support these functions even though BPCS controllers and RIO design are not in vendor scope.
- **Coordination is non-negotiable.** Building design must be coordinated with area classification, ventilation, heating, emergency egress, fire and gas detection, ESD pushbutton placement, RIO panel locations, power distribution, and maintenance access (DBM §704). These are coordination obligations, not deferrals.
- **Separation criteria are explicit.** Plot-plan placement must respect API 2510 (≥ 15.24 m / 50 ft from pressurized bullets) and OGAOM §9.6.15 (≥ 25 m / 82 ft from fired heaters) per DBM `4-25` §254, §298.

## Considerations

- **WBS / DBM cross-applicability.** PKG-042 is registered under WBS 03 (per Gate 7), and the principal source slices for control-room siting separations come from the DBM-Deepcut (4-25) document. Treat DBM `4-25` separation values as authoritative project-wide criteria for control-room siting unless `DEL-042-02` or a project-wide design basis ruling supersedes them. Where 4-25 references "install on site or modify if already existing" for office/control-room buildings (§2662, §2759), applicability to PKG-042 is `TBD` until the EPC anchor deliverables clarify.
- **Pre-assembly mode.** DBM `4-25` §3025 contemplates buildings fabricated and erected in the assembly shop before shipment to site. Vendor design should declare whether PKG-042 is shop-assembled or stick-built, because that determines the conduit-method requirement (rigid vs EMT).
- **Server hosting.** The primary control-system server host being in the control room (DBM §796) drives the building's environmental (HVAC), power-quality, fire-suppression, and physical-security requirements. The vendor package must size building services with the server-hosting load in scope, even though server hardware itself may be supplied separately.
- **Network-room boundary.** Core network switches are hosted in the control room (DBM §3141); the boundary between vendor-supplied building network infrastructure (racks, cabling, structured wiring) and EPC-supplied / BPCS-supplied active equipment must be made explicit in the vendor design basis.
- **Area classification.** The building interior is treated here as non-process / general-purpose based on DBM §3025's allowance of EMT inside control rooms. The actual area-classification drawing for PKG-042 is not in accessible source slices; this is recorded as an ASSUMPTION and a Conflict-Table item.

## Trade-offs

- **Shop-assembled module vs site-built building.** Shop-assembled modules reduce site labor and weather risk and benefit from rigid-conduit pre-fab (DBM §3025) but constrain building size to shipping envelope and may complicate later modification. Site-built construction loosens size constraints but increases site coordination with concurrent civil/electrical work packages. Decision is `TBD` and depends on EPC Package Datasheet (`DEL-042-02`) and plot-plan constraints.
- **Single-room vs subdivided interior.** A subdivided interior (operator room + server/network room + electrical/HVAC plant) can simplify fire/smoke compartmentation and acoustic isolation, but increases footprint and HVAC zoning complexity. Trade-off resolution depends on operator-count, server-thermal-load, and fire-and-gas detection design (`TBD`).
- **Fire-suppression strategy.** Sprinkler vs gaseous (e.g., clean-agent) suppression in the server / network areas affects equipment risk, building services, and code path. Not stated in accessible source slices; `TBD`.

## Examples

Locally accessible source slices do not contain a worked control-room building example; this section is limited to source-grounded illustrations.

- *Function illustration (from DBM 4-25):* "The controls system is designed for operation from a central operations control room. The control room shall provide the environment for operations personnel to monitor and control the facility while limiting the need for physical interaction in the process facility." (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §3119)
- *Hosting illustration (from DBM 3-25):* "The primary host is located in the control room; the secondary host is located in the low-voltage MCC room." (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §796)
- *Interior wiring illustration (from DBM 4-25):* "EMT may be used in non-process locations such as MCC buildings, control rooms, offices, and warehouses. Conduit shall be sealed where it crosses a change in area classification ... Minimum conduit size shall be 21 mm (3/4 in)." (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §3025)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-042-04-001 | Cross-DBM applicability: the principal control-room siting separations and interior-wiring conventions are stated in DBM `4-25_Deepcut_DBM.md`, but PKG-042 is registered under WBS 03 / project basis 3-25. | Gate 7 `PACKAGE_REGISTER.csv` `PKG-042` (WBS 03; SourceRefs cite `DBM-Comp_and_Liquids/3-25`) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §254, §298, §3025, §3119, §3141 | `Datasheet.md` Separation criteria / Wiring method; `Specification.md` REQ-042-04-07, REQ-042-04-08, REQ-042-04-09 | Treat DBM 4-25 control-room provisions as authoritative project-wide criteria for control-room siting and interior wiring unless the EPC Package Datasheet (`DEL-042-02`) supersedes them. Record the ruling in `_MEMORY.md` and the package datasheet. | TBD |
| HRR-042-04-002 | Building configuration (shop-assembled module vs site-built; single-room vs subdivided interior) is not specified in accessible source slices for PKG-042. | Workbook Packages row 44 (no configuration stated) | DBM `4-25` §3025 (contemplates shop pre-assembly for non-process buildings) | `Datasheet.md` Construction (Fabrication / supply, Pre-existing-building option); `Specification.md` REQ-042-04-09; `Procedure.md` steps 5-6 | Record building configuration as `TBD` and resolve via `DEL-042-02` before vendor design freeze; default to shop-assembled module if no EPC direction is provided. | TBD |
| HRR-042-04-003 | Area classification of the building interior is not provided at deliverable scope; the assumption of "non-process / general-purpose" is inferred from DBM §3025's allowance of EMT. | DBM `4-25` §3025 (EMT in control rooms permitted) | Project area-classification drawing (not in accessible source slices) | `Datasheet.md` Conditions (Area classification); `Specification.md` REQ-042-04-05, REQ-042-04-08 | Accept the non-process / general-purpose assumption for vendor preliminary design; require formal confirmation by the EPC area-classification drawing prior to design freeze. | TBD |
| HRR-042-04-004 | Existing-building reuse option referenced in DBM 4-25 (§2662, §2759) is not declared in or out of scope for PKG-042. | DBM `4-25` §2662, §2759 | Gate 7 `PACKAGE_REGISTER.csv` `PKG-042` (silent on reuse) | `Datasheet.md` Construction (Pre-existing-building option) | Treat as `TBD`; the EPC Scope of Work (`DEL-042-01`) and Package Datasheet (`DEL-042-02`) are the authoritative places to resolve. | TBD |

## Cross-references

- `Datasheet.md` — identification, attributes, conditions, construction, references.
- `Specification.md` — scope, requirements, standards, verification, documentation.
- `Procedure.md` — prerequisites, steps, verification, records.
- Sibling deliverables: `DEL-042-01`, `DEL-042-02`, `DEL-042-03`, `DEL-042-05`, `DEL-042-06`.
