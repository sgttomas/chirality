# Guidance — DEL-075-03 Construction Work Package (PKG-075 Cryogenic Unit "Deepcut")

## Purpose

The Construction Work Package translates the PKG-075 cryogenic deep-cut propane-plus recovery package — owned in engineering by the Package Vendor — into a buildable, inspectable, and turnover-ready field-execution plan owned by the EPC Integrator. It is the mandatory Gate 5 EPC anchor deliverable for "how the package will be physically installed, built, inspected, turned over, and tied into the larger facility systems" (`_CONTEXT.md` Scope; DELIVERABLE_REGISTER.csv row 278).

## Principles

- **Split of authority is fixed by the package register.** Package Vendor owns package engineering, design, vendor documentation, and physical equipment package. EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination. (PACKAGE_REGISTER.csv row 52) The CWP must not silently absorb vendor scope.
- **Field-construction owner is Tourmaline.** Construction management, civils, module setting, mechanical hookup, instrument/valve installation, structural supports, cabling, terminations, area lighting, fencing, and demolition where required are all Tourmaline field-construction scope per DBM lines 107–125. The CWP coordinates this work; it does not replace the construction contract.
- **Tie-ins are first-class artifacts.** Every interface in the PKG-075 interface set (Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports — PACKAGE_REGISTER.csv row 52) needs a per-tie-in responsibility entry. DBM line 117 flags "Interconnecting piping to ISBL/OSBL tie-in points" as an external-interface responsibility to confirm per tie-in.
- **Joint tie-in planning is required and progressive.** Tie-in timing is established as the project progresses (DBM line 127); CWP planning should be revisited at each construction milestone.
- **Shared-utility coordination crosses facility boundaries.** Power, fuel gas, and instrument air interfaces are shared between 03-25 and 04-25 (DBM lines 93–95); CWP must reference the shared-utility interface basis.
- **Layout basis governs site sequencing.** Modular installation, access routes, maintainability envelopes, hazardous-area separation, and emergency response must be coordinated with the plot plan as the layout matures (DBM line 233; §2.6).

## Considerations

- **Modular delivery vs. field hookup.** The package arrives largely modular; field scope is "set, hook up, and terminate," not "build from raw materials." Sequence transport, off-load windows, crane plans, and laydown around the layout basis (DBM §2).
- **Cryogenic service introduces material, cleanliness, and dry-out requirements.** Specific cleanliness, dry-out, leak-test, and material verification requirements are not enumerated in the locally accessible DBM slice and are TBD (likely defined in 26020-Package_Requirements.docx heading 29 — location TBD).
- **Interface count is large.** Twelve interface families per PACKAGE_REGISTER.csv row 52 raise constructability risk; an integrated tie-in/isolation matrix is recommended.
- **Joint-planning lead time.** Because tie-in timing is set progressively (DBM line 127), the CWP should treat the tie-in workface plan as a living document with explicit revision triggers (e.g., layout maturation, P&ID issue, vendor drawing release).

## Trade-offs

- **Pre-fabrication completeness vs. transport/setting constraints.** More vendor-side completion shortens field work but raises module weight/size and transport risk. No DBM-level guidance fixes this trade-off; resolve per package design and route study (location TBD).
- **Shared-utility integration vs. independent metering.** DBM requires independent metering and mass-balance accountability between 03-25 and 04-25 even where utilities are shared (DBM lines 42, 97). Construction tie-ins must preserve this separation.
- **External tie-in responsibility.** "Interconnecting piping to ISBL/OSBL tie-in points" is flagged as an external interface (DBM line 117); over-assigning this to Tourmaline field scope risks scope conflicts, under-assigning risks orphaned tie-ins.

## Examples

- DBM "Construction Responsibility" table (lines 107–125) provides the field-scope example list to use as the construction work-breakdown skeleton.
- DBM line 174 explicitly carries "Interconnecting piping to ISBL/OSBL tie-ins" forward as "External interface responsibility to be confirmed per tie-in" — use this as the template entry in the tie-in register.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short) | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-1 | Per-tie-in responsibility for "Interconnecting piping to ISBL/OSBL tie-in points" is unresolved. | DBM line 117 (external interface, confirm per tie-in) | _CONTEXT.md ResponsibleParty = EPC Integrator (deliverable-level) | Specification R-1, R-3; Datasheet Conditions; Procedure Step 2 | Treat as EPC-Integrator-coordinated but per-tie-in confirmed by joint planning (DBM line 127). | TBD |
| C-2 | Package-specific construction-execution requirements (NDE, hydrotest, dry-out, cleanliness, records set) are not in the locally accessible DBM slice. | DBM (silent) | 26020-Package_Requirements.docx heading 29 (location TBD) | Specification R-8, R-9; Datasheet Construction; Procedure Step 4, 6 | Open and slice the package-requirements docx; until then, mark TBD with ASSUMPTION labels. | TBD |
| C-3 | Objective-to-deliverable association uses PACKAGE_HEURISTIC. | _CONTEXT.md Supports Objectives (OBJ-001, OBJ-003..OBJ-010) | DELIVERABLE_REGISTER.csv row 278 ObjectiveAssociation | All four documents | Treat as ASSUMPTION pending human confirmation. | TBD |
