# Guidance — DEL-083-01 Scope of Work (PKG-083 Inlet Separators 3-25)

## Purpose

This Scope of Work defines the EPC Integrator's contractual scope for the inlet separation package at the 03-25 West Doe Compressor Station. It exists to bind:

- the tagged equipment that constitutes the package (the two horizontal three-phase inlet separator trains V-1600-2 and V-1700-2 and their package-internal valves, internals, instrumentation, and enclosure);
- the package function — three-phase separation of sour gas, raw condensate, and produced water at 2 x 50% facility capacity;
- the package's role inside the 03-25 / 04-25 facility split (raw condensate forwarded to 04-25 MPFS/stabilization; drive-gas recycle returned from downstream of inlet compressor aftercoolers);
- the responsibility assignment between EPC Integrator, owner, vendors, and third parties (notably NRM LACT scope is excluded except for facility-side tie-in).

The Scope of Work is the Gate-5 EPC anchor deliverable for the package; downstream package deliverables (P&IDs, datasheets, MTOs, procurement packages) inherit boundaries and responsibilities from it.

## Principles

1. **Source-anchored, not narrative-anchored.** Equipment identities, design conditions, and boundary definitions are drawn from the governed 3-25 DBM (SEC-01, SEC-03, SEC-04) and the trace appendix (KTY-04-02 Inlet-Separator KAs). Decomposition summaries route the work; they do not substitute for source values.
2. **Boundary clarity beats interior detail.** A Scope of Work succeeds when the package boundary is unambiguous at every flange and signal interface. Interior detail (vendor sizing, exact internals geometry) belongs in downstream package deliverables.
3. **2 x 50%, not 2 x 100%.** Older facility text used a "2 x 100%" formulation for the separator trains. The current governed basis is "2 x 50%, no spare." Carry the current basis and reconcile the older text explicitly.
4. **Sour-service throughout.** H2S design 0.3 mol% with license value 2.0 mol% governs materials selection and inspection regime even when peak operating values are lower. Carry sour-service as a package-wide assumption rather than a section-by-section qualifier.
5. **TBC / TBD discipline.** The current basis intentionally leaves several values open (normal high operating pressure, delivery-point ESDV shutdown, exact building extent, downstream methanol disposition, CO2 design, normal high H2S operating value). Carry these explicitly in the Scope of Work rather than silently filling them.
6. **Interfaces with 04-25 are first-class.** Drive-gas recycle pressure must remain above the 04-25 stabilizer flash feed separator pressure; raw condensate routing to 04-25 MPFS/stabilization is a facility-defining interface; instrument air is sourced from 04-25 per SCA-006. These are not "utility hookups," they are package-defining interfaces.

## Considerations

- **Pig receiver and inlet ESDV ownership.** The DBM places the pig receiver and inlet ESDV upstream of the separator package boundary. PACKAGE_REGISTER.csv assignment for the pig receiver/ESDV is **TBD**; until confirmed, treat them as out-of-package while preserving the interface (sweet-gas purge, HP flare vent, 635 psig ESDV shutdown pressure) on the Scope of Work as a documented incoming boundary.
- **Methanol drain.** Methanol may appear infrequently and drains at the separator boot. Downstream methanol disposition is open; do not specify a disposition path in this Scope of Work beyond noting the requirement to accommodate methanol at the boot.
- **Building extent.** "Instrumentation and one end of each package" is to be enclosed in a heated self-framing building. Exact extent of enclosure is TBD; treat building extent as an open item for module general-arrangement resolution before procurement.
- **Inlet temperature reconciliation.** Inlet design temperature is 8.3 deg C in SEC-04 inlet conditions, but downstream excerpts have variant values requiring reconciliation. Do not select a value in this Scope of Work; require detailed design to reconcile before equipment datasheets issue.
- **Slug handling vs frac flowback.** Per-separator slug handling is ~38 m3. Frac flowback (not pigging slug) is the governing transient liquid case, with operator-managed gas rate reduction as required. The Scope of Work should articulate this as an operating-constraint inheritance to facility operations, not as additional separator sizing duty.

## Trade-offs

- **Carry sour-service materials as a package-wide standard vs section-by-section.** Package-wide is operationally simpler and reduces specification drift; section-by-section is more cost-efficient where service conditions allow non-sour materials. The DBM supports a package-wide sour-service basis; recommend package-wide.
- **Specify Devchem 253 internal coating in Scope of Work vs defer to vessel datasheet.** Scope of Work fixes the coating product, which constrains vendor selection but matches the governed DBM. Defer geometry/thickness to the vessel datasheet.
- **Building extent decision early vs late.** Resolving building extent before SoW issue increases certainty but may delay issue; deferring to detailed design preserves SoW schedule but transfers risk. Recommend explicit deferral with named decision point.
- **Inlet pressure-control valves: balanced globe hardened trim (current basis) vs alternative trims.** Current basis fixes balanced globe hardened trim with 5 psid limit; alternatives could reduce cost but would require deviation acceptance. Recommend holding current basis.

## Examples

- **Example boundary callout for raw condensate:** "Package outlet flange downstream of separator condensate level-control valve is the package boundary for raw condensate; downstream piping to the 04-25 raw-condensate forwarding system is out-of-package and is covered by the inter-facility piping package (TBD-DEL)."
- **Example responsibility assignment row:** "Inlet pressure-control valves (per R6): vendor-furnished as part of the inlet separator package; EPC Integrator responsible for procurement and installation; owner responsible for setpoint approval at C&E review."

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-01 | Sweet-gas purge and HP flare vent provisions: DBM places them on the pig receiver paragraph (§SEC-04 "Pig Receiver"), but the inlet separator package routinely owns purge/vent at the vessel skid in conventional practice. | DBM §SEC-04 "Pig Receiver" paragraph (purge/vent tied to pig receiver) | KTY-04-02 KA-08 "Inlet-Separator-Sweet-Gas-Purge" (Trace_Appendix.md row 197) | Datasheet Tagged Equipment; Specification R10; package boundary narrative | Adopt KA-08 placement (purge/vent on separator package) and document pig-receiver-side interface as continuing the system | TBD |
| CT-02 | Separator-train capacity language: SEC-04 inlet separation table specifies "two identical packages, each 50% of facility capacity" but also notes "older 2 x 100 percent table language requires reconciliation." | DBM §SEC-04 "Inlet Separation" current text (2 x 50%) | DBM §SEC-04 reference to older 2 x 100% table | Datasheet Attributes; Specification R2, R14; integration narrative | Adopt 2 x 50% (current governed); explicitly supersede older language in SoW reconciliation note | TBD |
| CT-03 | Inlet design temperature: SEC-04 inlet conditions paragraph states 8.3 deg C and notes downstream excerpts require confirmation; detailed design shall reconcile before equipment datasheets issue. | DBM §SEC-04 inlet conditions paragraph (8.3 deg C) | DBM §SEC-04 reference to variant downstream excerpts (values not extracted in this pass — location TBD) | Datasheet Conditions; Specification R15 | Carry 8.3 deg C with explicit reconciliation requirement before datasheet issue | TBD |
| CT-04 | Pig receiver and inlet ESDV package assignment: DBM places them upstream of separator, but PACKAGE_REGISTER.csv assignment was not extracted in this pass. | DBM §SEC-04 "Pig Receiver" paragraph | PACKAGE_REGISTER.csv (not read in this pass — location TBD) | Specification Scope (Out of Scope); Datasheet Tagged Equipment | Treat as out-of-package pending PACKAGE_REGISTER.csv confirmation; surface interface | TBD |
