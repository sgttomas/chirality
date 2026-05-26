# Guidance — DEL-056-03 Construction Work Package (PKG-056)

## Purpose

This Guidance document explains the intent, principles, and judgement areas behind the PKG-056 Construction Work Package. The CWP is the mandatory Gate 5 EPC Integrator anchor deliverable that describes how the inlet separators package will be physically installed, built, inspected, turned over, and tied into the 04-25 facility (`_CONTEXT.md`; DELIVERABLE_REGISTER row DEL-056-03). Where the Specification is binding, this document supplies rationale, considerations, and trade-offs.

## Principles

- **Vendor/EPC interface integrity.** Package Vendor owns equipment package engineering, design, and vendor documentation; EPC Integrator owns facility-level integration including interfaces, tie-ins, constructability, and procurement/construction coordination (PACKAGE_REGISTER.csv PKG-056). The CWP must respect this split and not duplicate or override vendor engineering.
- **Construction responsibility per DBM SEC-01.** Field construction execution is assigned to Tourmaline Oil Corporation per the explicit construction responsibility table in DBM SEC-01. The CWP plans around that scope split rather than reassigning activities.
- **Source-grounded values, conservative when ambiguous.** Operating, design, and equipment values reproduced in the kit are taken from accessible sources; conflicts (e.g., installed quantity, slug capacity) are surfaced not resolved.
- **Symmetrical inlet distribution.** The two installed separators rely on piping symmetry for balanced gas/liquid distribution (DBM SEC-04). Construction sequencing and red-line discipline must preserve that symmetry.
- **Two-phase inlet tolerance.** Inlet gas can arrive two-phase in winter or after cool-down (DBM SEC-04). Construction acceptance must include integrity of methanol injection, liquid outlet heating, and downstream MPFF/stabilizer interfaces.

## Considerations

- **Future plot provision.** Plot space for a third inlet separator is retained (PACKAGE_REGISTER.csv PKG-056; DBM SEC-04). Construction layout, tie-in stub configuration, and lifting access should avoid foreclosing that future provision.
- **Modular setting and lifts.** The package vendor delivers shop-assembled equipment. Lift plans, crane access, and rigging studies should be developed early and integrated with site logistics; specific lift weights and pick points are TBD pending vendor general arrangement drawings.
- **Heat medium identity.** Liquid outlet heater medium is unresolved between warm glycol and process-stream cross-exchange (DBM SEC-04). Construction sequence and tie-in routing must remain compatible with either selection until detailed engineering closes that.
- **Hot work and live-plant tie-ins.** Several PKG-056 tie-ins (flare, drains, utilities, EHT, F&G) may need to be made into a live or partially commissioned 04-25 facility. Sequencing and permit-to-work practices are not specified in deliverable-local sources reviewed; the CWP must obtain and reference the governing site standard (location TBD).
- **Hydrotest and cleanliness.** Vessel internal coating (Devchem 253, DBM SEC-04) constrains hydrotest chemistry and flushing strategy. Coating integrity must be confirmed before and after hydrotest.
- **Inspection of internals.** The mist eliminator type is "subject to operations review" per DBM SEC-04. Construction acceptance should include a documented internals inspection prior to closing manways.

## Trade-offs

- **Pre-fabricate vs field-erect tie-in spools.** Pre-fabrication shortens field schedule but risks dimensional rework if vendor GA changes; field-fit reduces rework risk but extends field hours.
- **Single vs phased turnover.** Turning over both separators together simplifies operator acceptance but lengthens critical path; sequential turnover allows earlier feed-in but doubles turnover effort.
- **Hydrostatic vs pneumatic testing.** Pneumatic test reduces dry-out time on sour service but introduces stored-energy risk; final selection is TBD pending governing piping code reference.

## Examples

(Examples available only where local source content supports them.)

- **Construction responsibility example (DBM SEC-01):** "Mechanical hookup of modules, equipment, and interconnecting piping — Tourmaline field construction scope."
- **Inlet PCV example (DBM SEC-04):** Two parallel balanced-globe inlet PCVs per separator, hardened trim recommended, design dP <=5 psid; outlet manual isolation permits PCV maintenance without full separator blowdown.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-056-03-1 | Installed inlet separator quantity: two (2) installed + future plot vs four (4) packages legacy | PACKAGE_REGISTER.csv PKG-056 / Equipment description; DBM SEC-04 "Inlet Separation" (current body basis) | DBM SEC-04 narrative referencing legacy four-package basis; MPFF source table legacy "4 vessels" reference | Datasheet Attributes; Specification R-2.1; Procedure (modular setting and tie-in count) | Adopt current governed package basis: two installed + future-plot provision | TBD |
| C-056-03-2 | Per-separator slug capacity: 31.8 m3 vs 33.9 m3 | DBM SEC-04 Inlet Separation narrative | DBM SEC-04 Inlet Separator Design Parameters table | Datasheet Attributes | Hold both; defer to vendor data sheet at detailed engineering | TBD |
| C-056-03-3 | Governing piping code/class for tie-in welds and pressure tests | Not explicitly named in local DBM sections reviewed | — | Specification R-6.2, R-8.1; Verification | Adopt project-standard piping code once provided; ASME B31.3 ASSUMPTION pending confirmation | TBD |
| C-056-03-4 | Liquid outlet heater medium (warm glycol vs process-stream cross-exchange) | DBM SEC-04 Inlet Separator Design Parameters | DBM SEC-04 narrative | Datasheet Attributes (heat medium); Specification R-5.3; Procedure (heat medium tie-ins) | Construction-compatible with either; defer to detailed engineering | TBD |
