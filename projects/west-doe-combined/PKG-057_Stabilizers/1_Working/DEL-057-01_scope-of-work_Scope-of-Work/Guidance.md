# Guidance — DEL-057-01_scope-of-work — Scope of Work (PKG-057 Stabilizers)

## Purpose

The Scope of Work for PKG-057 is the EPC Integrator's anchor document for the three (3) Inlet Stabilizer Packages at 04-25 Deepcut. It exists so the Package Vendor and downstream EPC deliverables (Datasheet, Construction Work Package, Vendor Document Turnover, Vendor Package Review and Acceptance) share a single, source-grounded statement of what is being supplied, what is "by others", and how the package integrates with the rest of the facility. (Source: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv; OBJ-001; OBJ-004.)

## Principles

1. **Source-anchored, not narrative-anchored.** Statements of design rate, sparing, operating/design conditions, and equipment configuration are taken from the 26020-Package_Requirements.docx package heading 12 extracts (SOW-0178 through SOW-0180) and from DBM-Deepcut SEC-04. Decomposition prose is route/scope context, not a substitute for source text. (Source: skill Authority hierarchy; SCOPE_LEDGER.csv.)
2. **Vendor / EPC split is structural.** Package Vendor owns engineering, design, vendor documentation, and physical equipment package. EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. (Source: PACKAGE_REGISTER.csv `_responsibility`; OBJ-004.)
3. **Train integrity matters.** One MPFF is paired with one stabilizer; loss of a stabilizer takes its paired MPFF out of service. Sparing claims must respect the 3 x 40% installed basis and the 80% capacity result of single-unit outage. (Source: DBM-Deepcut SEC-04 lines 608–612.)
4. **Skid-edge is the contract surface.** Interconnecting piping at skid edge, DCS integration, foundations, electrical supply from plant MCC, and installation are "by others." Anything that crosses skid edge becomes an EPC integration item, not a vendor scope item. (Source: SOW-0180.)
5. **Routing claims must match facility basis.** Stabilized C5+ goes to NGL mercaptan treating as primary feed (with single-package divert to condensate slop). Overhead vapours go to SOC stages (flash feed → 1st stage; tower overhead → 2nd stage). Relief and blowdown from flash feed and tower route to HP flare. (Source: DBM-Deepcut SEC-04 lines 678, 704, 710, 712, 813.)

## Considerations

- **C5+ blending downstream.** Stabilizer bottoms condensate alone is not expected to meet density specification (~641 kg/m3 winter, ~648 kg/m3 summer at 15 °C); blending with field-stabilizer condensate at the 03-25 Liquids Hub may be required. This is a downstream-product implication, not a PKG-057 scope item, but it should be acknowledged in the integration narrative. (Source: DBM-Deepcut SEC-04 lines 469–484.)
- **Open detailed-engineering items.** Strainer mesh, pump seal type, reboiler heat-medium temperature, product-cooler elevation (25 ft above grade trade-off for fire-case flare loading), and exact stabilizer feed-source mix beyond MPFF bottoms (recycle from C5+ storage and HC skim) remain TBD. The Scope of Work should not pre-empt these. (Source: DBM-Deepcut SEC-04 lines 702, 706, 708.)
- **Operating temperature reconciliation.** Source documents express the flash feed temperature both as 30.6 °C (SOW-0180) and as ~87 °F / ~30.6 °C (DBM-Deepcut SEC-04 line 704). Values are consistent within rounding; the Scope of Work should cite both source locations rather than choose silently.
- **Interface breadth.** Thirteen interface types apply at the package level. The integration narrative should walk them in PACKAGE_REGISTER order so INTERFACE_REGISTER traceability is preserved. (Source: PACKAGE_REGISTER.csv `_interface_types`.)
- **Objective coverage.** This deliverable supports nine objectives (OBJ-001, 003, 004, 005, 006, 007, 008, 009, 010) under the PACKAGE_HEURISTIC association mode. Treat that association as **ASSUMPTION (best-effort mapping)** at the package level; objective-deliverable traceability for this specific deliverable beyond package mapping is to be confirmed during EPC review.

## Trade-offs

- **Vendor latitude vs. EPC prescription.** Over-specifying internals (trays, reboiler bundle, exchanger seal-weld detail) tightens integration but narrows vendor optimization. The Scope of Work should preserve the source-stated constraints (20 floating-valve trays; BEU feed/bottoms; NEN reboiler with seal-welded tubes) without dictating sub-component design.
- **Skid-edge boundary vs. integration risk.** Pushing more piping/cabling into "by others" reduces vendor scope but increases EPC integration burden. SOW-0180 fixes the current boundary; deviations need to be ruled rather than negotiated silently.
- **Product cooler elevation.** Source flags a possible trade-off between elevating the cooler bundle 25 ft to reduce fire-case flare backpressure vs. structural/cost impact. The Scope of Work should surface the choice rather than presuppose it. (Source: DBM-Deepcut SEC-04 line 708.)

## Examples

- Section ordering hint (illustrative): Identity → Process Function → Package Boundary → Equipment Set → Operating and Design Conditions → Drivers → Vendor / EPC Responsibility Split → Interface Narrative → Open Items / TBDs. This mirrors the order in which source text supports each section.
- For interface narrative, cite INTERFACE_REGISTER rows by ID when available; otherwise cite PACKAGE_REGISTER `_interface_types` and mark **location TBD** for any interface fact not yet recorded in INTERFACE_REGISTER for PKG-057.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-057-01-01 | Flash feed separator operating temperature stated as "30.6 °C" in SOW-0180 vs. "~87 °F" (~30.6 °C) in DBM-Deepcut. | SOW-0180 (`SCOPE_LEDGER.csv`) | DBM-Deepcut/4-25_Deepcut_DBM.md line 704 | Datasheet Operating Conditions; Specification R4 | Cite both; treat values as consistent within rounding. | TBD |
| CONF-057-01-02 | Inlet stabilizer C5+ blending need stated in DBM SEC-04 (lines 469–484) implies stabilizer-bottoms-only product may not meet density spec; not stated in SOW-0178/0179/0180. | DBM-Deepcut SEC-04 lines 469–484 | SOW-0178/0179/0180 | Guidance Considerations; integration narrative | Disclose as downstream-product implication; do not impose stabilizer-side requirement. | TBD |
| CONF-057-01-03 | Source basis cites vendor RFQ "26020-01-PT-RFQ-17-005_Inlet Stabilizers_R0.docx" not opened as raw source in this pass. | PACKAGE_REGISTER.csv `_source_basis` | (no opened slice) | Specification Standards; Datasheet References | Mark **location TBD** for RFQ-derived clauses until source is opened. | TBD |
