# Guidance: DEL-060-02 — Package Datasheet (Tank Farm Pump Building 4-25)

## Purpose

This guidance explains *why* the Package Datasheet exists for `PKG-060` and how it should be developed to serve its downstream consumers — principally the third-party package vendor responding to `26020-01-PT-18-002` and the EPC Integrator coordinating package interfaces with the rest of the 04-25 Deepcut facility.

The datasheet is the **EPC Integrator's authoritative technical handoff** to the package vendor for the Tank Farm Pump Building 4-25. It carries forward the design basis already established in the DBM-Deepcut and in the PROJECT_DECOMP Gate 7 snapshot, and packages that basis in a form usable by a vendor whose responsibility starts at package engineering and ends at the physical equipment package.

Source: `_CONTEXT.md` (Scope); PACKAGE_REGISTER row 85 (responsibility boundary narrative).

## Principles

- **Source-grounded over inferred.** Every non-trivial value must be traceable to the DBM, PACKAGE_REGISTER, or another locally accessible source. Where the source is silent, prefer `TBD` over invention. (Authority hierarchy per `_REFERENCES.md`.)
- **Vendor scope is the package, EPC scope is the integration.** Anything *inside* the vendor's package boundary (skid layout, internal piping, equipment selection within performance envelope) is the vendor's responsibility; anything that crosses the package boundary (tie-ins, utilities, interfaces) is EPC scope. (PACKAGE_REGISTER row 85.)
- **Interfaces are first-class data.** The interface types listed in PACKAGE_REGISTER row 85 are the standard fourteen-interface model used across the EPC packages; the datasheet must address each.
- **Facility-level constraints are inherited.** Cold-startup motor sizing (-40 °C, JT-mode), sour-service expectations, and shared utility coordination (fuel gas, instrument air, EHT) are governed by the DBM and apply to this package even when the package vendor cannot be expected to derive them independently.

## Considerations

- **Pump configuration semantics.** The DBM (line 1675) explicitly requires `2 x 150%` sparing for condensate transfer so that both pumps may run simultaneously during upset pump-down. This is *not* a conventional `2 x 100%` sparing case and should be communicated unambiguously.
- **NPSHR ceiling.** The 0.75 m NPSHR ceiling at design flow (DBM line 1677) reflects an architectural decision: condensate tanks are not elevated. Exceeding this ceiling triggers a booster-pump scope change with cascading impact. The datasheet should foreground this as a hard ceiling, not a target.
- **Cold-start motor sizing.** Motor sizing based on -40 °C inlet-stabilizer composition density (DBM line 1679) is a worst-case driver case. Calling this out prevents the vendor from sizing on normal operating density.
- **Heat tracing / EHT.** The DBM (line 2014) notes dual redundant self-regulated EHT on separate circuits for hydrocarbon drains in the tank-farm area as a freeze-protection basis; the same heat-trace philosophy is likely applicable to exposed tank-farm pump piping. ASSUMPTION — confirm vendor interface scope vs. EPC scope at heat-trace boundary.
- **Module construction.** The tank farm pump module (`920-1`) is a shop module per DBM line 2817; shop-module fabrication implies finalized pipe routing and electrical pre-installation before site delivery. This shifts vendor documentation deadlines forward relative to a stick-built scope.

## Trade-offs

- **Specificity vs. vendor design space.** The more conditions the datasheet pins down, the less freedom the vendor has to optimize. The DBM-stated values (350 kPad differential, 0.75 m NPSHR, -40 °C motor sizing) are non-negotiable; secondary values (e.g., operating conditions for water/sour-water/process-water/fresh-caustic pumps) should be left to the vendor's data sheets to avoid overconstraining.
- **TBD vs. ASSUMPTION.** Where the source is silent but the value is genuinely required for vendor engineering (e.g., normal operating flows for the water-transfer service), prefer surfacing the gap as a `TBD` item in the datasheet rather than assuming a value. Assumptions create silent constraints that may not be caught at vendor review.

## Examples

- The condensate transfer service is the best-documented sub-scope: DBM line 1673 fully specifies pump tags, sparing logic, and differential pressure; line 1675 specifies the operability requirement; lines 1677-1679 specify the design ceilings. This is the model the rest of the datasheet sections should aspire to.
- The fresh-caustic transfer service (`P-6760-1`, `P-6765-1`) has *only* tag/quantity-level documentation in the accessible DBM slice. The datasheet should explicitly mark operating conditions as `TBD` and reference the 26020-Package_Requirements.docx package heading 15 (location TBD) as the place the missing values are expected to live.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C1 | "Condensate Recycle Pump" (PACKAGE_REGISTER row 85; 1 unit with strainer) vs. two `Tank farm pump module` pumps in the DBM: "Product recycle pump" (DBM line 1671) and "Condensate skim pump" (DBM line 1672), each 1 x 100%, each 20 m3/h at 80 m TDH (TBC). | PACKAGE_REGISTER row 85 ("(1x) Condensate recycle pump") | DBM-Deepcut lines 1671-1672 | Datasheet §Attributes; Specification R2 | The DBM-level decomposition shows two separate recycle/skim units; the PACKAGE_REGISTER narrative may consolidate them. Treat the package as carrying both units, and add an explicit note. | TBD |
| C2 | Package roster (DBM line 2555) names the package "Tank Farm Pump Building 2" with 10 total equipment items, while `_CONTEXT.md` and PACKAGE_REGISTER call the package "Tank Farm Pump Building 4-25". | DBM line 2555 ("Tank Farm Pump Building 2") | `_CONTEXT.md`; PACKAGE_REGISTER row 85 ("Tank Farm Pump Building 4-25") | Datasheet identification | The "2" suffix in the DBM appears to disambiguate the 4-25 tank-farm pump building from a 3-25 equivalent; the PROJECT_DECOMP / `_CONTEXT.md` name is authoritative for deliverable identity. | TBD |
| C3 | Condensate recycle pump tag is `TBD` in the DBM line-item table (line 2555 narrative + lines 2618-2622 line items omit the recycle unit explicitly with a tag). | DBM lines 1671-1672 (no tag stated) | PACKAGE_REGISTER row 85 (no explicit tag) | Datasheet §Attributes | Mark tag `TBD` pending vendor or detailed-engineering assignment. | TBD |
