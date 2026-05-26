# Guidance — DEL-085-04 Vendor Engineered Equipment Package (Flare Stack, High Pressure)

## Purpose

This deliverable exists because PKG-085 (Flare Stack, High Pressure) is built and delivered as a vendor-engineered equipment package rather than as discipline-built scope. The EPC Integrator defines what the package must do (`DEL-085-01` SOW; `DEL-085-02` Package Datasheet); the Package Vendor produces engineering, design, fabrication/supply, and the physical package itself; the EPC Integrator then reviews and accepts the result (`DEL-085-06`). This deliverable is the production unit on the vendor side of that handoff (source: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv).

## Principles

1. **EPC anchor governs.** The vendor package is a derivative of the EPC SOW and Package Datasheet. When vendor judgment and EPC anchor documents disagree, the EPC anchor governs unless the EPC Integrator issues a written change.
2. **Source-anchored values, not vendor convention.** Where the project Design Basis Memoranda (3-25 and 4-25 DBMs) state values for flare service, header sizing, KO drum arrangement, spacing, or thermal-radiation flux, the vendor design SHALL adopt those values until superseded by final flare studies and an accepted EPC change.
3. **Shared-system humility.** The HP/Cryo flare stack is a shared 03-25 / 04-25 system; vendor scope boundaries are not a unilateral decision (source: 3-25 DBM Utilities narrative).
4. **Final flare studies are pending.** Current source basis explicitly states blowdown and relief loads require final flare studies; vendor design accommodates revision (source: 3-25 DBM Plant Information Summary).
5. **No silent invention.** Where the EPC SOW and Package Datasheet do not yet resolve a value, the vendor records the gap as TBD or an interface item, not as a vendor-elected value.

## Considerations

- **Tributary services to HP flare** (source: 4-25 Deepcut DBM): the HP flare receives relief and blowdown from inlet separators, MPFF, stabilizer flash/feed separator, stabilizer tower, SOC, pig receiver vent (sweet-gas purge + HP flare vent), and contactor blowdown. Vendor package interfaces must accommodate this range of services.
- **KO drum locations** (source: 3-25 DBM): two HP KO drums upstream of the HP flare — one in the compressor area, one in the tank farm — manifolded to the HP flare. Vendor manifold design must respect both routes.
- **Thermal radiation and spacing** (source: 4-25 Deepcut DBM): both inside-boundary (≤ 9 kW/m²) and outside-boundary (≤ 5 kW/m²) flux limits apply, along with explicit spacing rules to plant equipment, public road/property line, condensate tanks, separators, pressurized bullets, vegetation/fire hazards, and fired heaters.
- **Stack physical envelope** (source: 3-25 DBM): the current sonic HP/Cryo stack is 660 mm OD x 60,957 mm tall; LP stack OD is TBD. Vendor lift, foundation, and transport planning depends on confirming these dimensions against final vendor selection.
- **Detection coverage** (source: 3-25 DBM): LEL, H2S, methyl mercaptan, fire detection at flare/vent interfaces should be assumed required; specific quantities and locations remain TBD.

## Trade-offs

- **Vendor-standard stack vs. project-specific configuration:** A vendor-standard sonic HP/Cryo stack offering may reduce delivery time but may not match the 660 mm OD x 60,957 mm tall envelope in the current source basis. Trade-off decisions should be documented and reconciled with final flare studies.
- **Centralized vs. split KO drum service:** The current basis splits HP KO service across V-4100-2 (compressor area) and V-4150-2 (tank farm). Vendor proposals to consolidate or rearrange must be screened against shared-system allocation with 04-25 and against tank-farm/compressor-area routing.
- **Layout flexibility vs. spacing minima:** Reducing stack-to-equipment distance below the cited minima is not an engineering economy: those distances are externally cited regulatory minimums (OGAOM, OGPFR, API 2510) carried in the project DBM (source: 4-25 Deepcut DBM).
- **Vendor scope creep:** Pulling civil, structural, or detection scope inside the vendor package may simplify interface management but increases the EPC Integrator's review burden and risks duplicating bulks. Resolve through the EPC SOW (`DEL-085-01`) and Package Datasheet (`DEL-085-02`), not by vendor election.

## Examples

- **Spacing example (source: 4-25 Deepcut DBM):** A vendor package layout that places the flare KO drum 8 m from a treeline does not satisfy the 10 m flare KO-to-vegetation/fire-hazard distance and SHALL be revised.
- **Stack example (source: 3-25 DBM):** The current HP/Cryo stack dimension (660 mm OD x 60,957 mm tall) drives crane planning, foundation reach, and transport segmentation; vendor proposals to alter the dimension must trigger a revisit of the project foundation/anchorage basis.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFL-01 | Vendor scope boundary (mechanical, instrumentation, civil, detection, insulation, painting, bulks) is not explicitly fixed for DEL-085-04 in accessible sources | `_CONTEXT.md` DEL-085-04 scope statement | DELIVERABLE_REGISTER.csv DEL-085-01 (EPC SOW) and DEL-085-02 (Package Datasheet) — anticipated to define scope split | Specification §REQ-085-04-11; Datasheet Construction; Guidance Trade-offs | Defer to EPC SOW (`DEL-085-01`) and Package Datasheet (`DEL-085-02`) when issued | TBD |
| CFL-02 | Final HP relief/blowdown loads are not yet established | 3-25 DBM Flare and Blowdown / Plant Information Summary ("blowdown and relief basis require final flare studies") | Vendor sizing assumptions (none yet) | Specification §REQ-085-04-03..05; Datasheet Attributes | Vendor sizes against current basis but holds re-issue until flare study is final | TBD |
| CFL-03 | HP/Cryo and LP flare stack service split between 03-25 and 04-25 is described as an open interface item | 3-25 DBM Utilities narrative | 4-25 Deepcut DBM HP-flare service interfaces | Specification §REQ-085-04-10; Guidance Considerations | EPC Integrator to issue ruling against current allocation before vendor design freeze | TBD |
| CFL-04 | External regulatory references (OGPFR, OGAOM, API 2510) cited by DBM are not locally accessible | 4-25 Deepcut DBM Flare and Incinerator Spacing (cites OGPFR, OGAOM, API 2510) | Source-document files | Specification §REQ-085-04-06, §REQ-085-04-07; Datasheet Conditions | Carry DBM-stated values as the working basis; reconcile against governing regulation during detailed design | TBD |
