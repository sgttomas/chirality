# Guidance — DEL-096-03 Construction Work Package (PKG-096 Tanks, Sour Condensate API 650)

> Directional document. Captures rationale, principles, considerations, trade-offs, and conflicts for human ruling.

## Purpose

This deliverable is the EPC Integrator's mandatory Gate 5 anchor for PKG-096. Its purpose is to translate the vendor-supplied modified-API-650 sour-condensate tank package into a constructable, inspectable, and turnover-ready facility asset. It addresses scope items SOW-0217 through SOW-0220 and supports project objectives OBJ-002 through OBJ-010 (per `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv`).

The package vendor owns the engineered tank package; the EPC Integrator owns everything that turns the package into an operating facility component — foundations, mounting, electrical/instrumentation, platforms, staircase, tie-ins, and the nine applicable physical interfaces (Process Piping; Relief/Flare/Vent; Drain/Containment; Grounding/Bonding; Area/Exterior Lighting; Cathodic Protection; I&C/Control Cabling; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports) — source: `26020-Package_Requirements.docx` H1 #48.

## Principles

1. **Source authority.** Vendor and package source materials (in particular the `26020-Package_Requirements.docx` package section) define what the construction work package must respect. Decomposition prose routes; the source determines content. (See SKILL authority hierarchy.)
2. **Sour service discipline.** Once the package leaves the shop, every field decision (welding, bolting, gasket selection, coating touch-up) must preserve NACE compliance. Field non-conformities in sour service are high-consequence.
3. **Vendor interface integrity.** Treat the vendor "By Others" list as a contractual boundary, not a suggestion. Foundations, site mounting, electrical/instrumentation, platforms, and staircase are EPC scope and must be planned before tanks arrive on site.
4. **Interface completeness.** Each of the nine applicable interface types is a documented turnover obligation. Absence of one signed interface ticket blocks turnover.
5. **Test before turnover.** Hydrotests, relief device function, blanket-gas leak test, loop checks, holiday test, and high-level shutdown must be evidenced before signing turnover.

## Considerations

- **Pressure and venting.** The tanks are essentially atmospheric (32 oz test pressure). Construction handling of nozzles, hatches, and the blanket-gas / VRU header tie-in must avoid over-pressurizing or vacuum-collapsing during commissioning. API 2000 governs venting; field commissioning sequencing should be coordinated with relief/flare system readiness.
- **Coating preservation.** Devchem 253 internal coating is specified by the vendor. Any heat work near coated surfaces (welds, hot taps for late tie-ins) risks coating damage. Plan field welding completion before coating, or accept vendor-approved touch-up.
- **Temperature envelope.** Design temperature -40 °C to 60 °C is wide; cold-weather construction must not impose temperatures or thermal gradients outside that range during hydrotest or commissioning.
- **Two-tank coordination.** With two tanks (TK-9110-2 and TK-9120-2) and design flows requiring that plant capacity can fill a single tank, the workface plan should sequence so that at least one tank is testable while the other supports vendor field-completion work.
- **Spill containment.** Containment grading and drainage around sour-condensate service must respect the spill volume of both tanks. Final volume calculation is `TBD` pending civil/site design slice.

## Trade-offs

| Trade-off | Discussion |
|---|---|
| Erect tanks first vs. complete underground tie-ins first | Erecting first speeds vertical schedule but constrains foundation-period piping/grounding/CP work. Project conditions typically favor completing buried interfaces (CP anodes, drains, grounding grid) before tanks block access. **Decision: TBD pending civil/sitework sequence.** |
| Field-erected vs. shop-fabricated mounting | Source notes "mounting tanks at site" is By Others. Whether the EPC mounts modular tank components or accepts a partially shop-assembled package affects rigging and lifting study. **Decision: TBD pending vendor MEC-018 Lifting/Handling Study.** |
| Vendor-managed coating touch-up vs. EPC-managed | NACE coating systems on sour service are typically vendor-warranted. Pulling touch-up into EPC scope risks warranty disputes. Default position: vendor-managed touch-up, EPC supports access. |
| Lighting / I&C interface — vendor-supplied vs. facility-supplied | Source marks Electrical Power = No, but Area/Exterior Lighting = Yes and I&C/Control Cabling = Yes. The EPC must supply lighting and control cabling but not bulk power; the dividing terminal box / panel must be specified. **Specifics: TBD.** |

## Examples

- (omitted: no concrete prior-package examples in accessible source slices)

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFL-096-03-01 | "Electrical Power = No" but "Area / Exterior Lighting = Yes" and "I&C / Control Cabling = Yes" — power must come from somewhere to feed lighting and I&C panels at the tank pad. | `26020-Package_Requirements.docx` H1 #48, Physical Interface Summary (Electrical Power = No) | Same source: same table (Area Lighting = Yes, I&C = Yes) | Specification R-096-03-10, R-096-03-12 | PROPOSAL: "Electrical Power = No" refers to bulk-power interface to the package equipment (none); lighting and I&C have their own facility-level power feeds. | TBD |
| CFL-096-03-02 | "Mounting tanks at site" listed as By Others (vendor scope notes), but vendor also lists MEC-018 Lifting / Handling Study as a vendor deliverable. | `26020-Package_Requirements.docx` H1 #48, Scope Notes (By Others list) | `26020-Package_Requirements.docx` H1 #48, Vendor Engineering Deliverables (MEC-018) | Procedure prerequisites; Specification R-096-03-04 | PROPOSAL: Vendor provides the lifting study; EPC executes the lift / mounting per that study. | TBD |
| CFL-096-03-03 | `_DEPENDENCIES.md` declares no upstream/downstream dependencies, yet the package register identifies many physical interfaces requiring upstream interface partners (e.g. CP, grounding grid, flare header). | `_DEPENDENCIES.md` (no declared upstream/downstream) | `26020-Package_Requirements.docx` H1 #48, Physical Interface Summary; `PACKAGE_REGISTER.csv` PKG-096 Applicable Interface Types | Procedure prerequisites | PROPOSAL: Run `TASK + dependency-extract` to formalize the nine interface dependencies before construction execution. | TBD |
| CFL-096-03-04 | Source mentions `26020-Packages_Interfaces.3.xlsx` for row 92 interface details, but the workspace `_Sources` carries `26020-Packages_Interfaces_4_export.xlsx`. | `26020-Package_Requirements.docx` H1 #48, Physical Interface Summary (mentions ".3.xlsx") | `_Sources/26020-Packages_Interfaces_4_export.xlsx` (filename in repo) | All interface references | PROPOSAL: `_4_export.xlsx` is the current revision; treat as authoritative and update text references. | TBD |
| CFL-096-03-05 | Internal coating Devchem 253 is vendor-applied, but field work (welds, late tie-ins, mounting) may damage coating; source does not state field touch-up authority. | `26020-Package_Requirements.docx` H1 #48, Major Included Equipment (coating) | Source silent on field touch-up authority | Specification R-096-03-03; Guidance Considerations | PROPOSAL: Default to vendor-managed touch-up under warranty; explicit ruling required. | TBD |
