# Guidance: DEL-038-04_vendor-engineered-equipment-package

## Purpose

This guidance supports the Package Vendor production unit (engineering, design, fabrication/supply, and physical equipment) for the 600V ELECTRICAL BUILDING (820-1) package, `PKG-038`. The deliverable converts the accepted EPC Scope of Work and EPC Package Datasheet into a vendor-engineered prefabricated modular electrical building (tag 820-1) and its housed equipment set, with a defendable design basis. EPC integration review is performed downstream (`DEL-038-06`).

## Principles

- **Vendor inputs are EPC outputs.** Vendor design starts from `DEL-038-01` (Scope of Work) and `DEL-038-02` (Package Datasheet). The vendor shall not invent package scope outside those inputs.
- **Responsibility split is preserved.** Package engineering, design, vendor documentation, and physical equipment belong to the Package Vendor. Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration belong to the EPC Integrator.
- **Source-anchored values only.** Where DBM electrical-building source slices and Gate 7 registers define a value or constraint, the vendor design shall reflect it. Where source is silent, values remain `TBD` for vendor data to close, not for invention by drafting.
- **Interfaces drive design, not the reverse.** The twelve applicable package interfaces (per `INTERFACE_REGISTER.csv` for `PKG-038`) are inputs to vendor engineering, not items the vendor may redefine.
- **Voltage-class identity is not assumed.** The building tag `820-1` carries a documented conflict between the workbook package name ("600V") and the DBM electrical-buildings table ("6.9 kV Inlet / Sales Compressor"). The vendor design shall not commit voltage class until EPC integration resolves CFL-038-04-001.

## Considerations

- **Building basis.** Per DBM, electrical buildings are prefabricated and modular, located in general purpose areas, climate controlled with n + 1 HVAC, elevated on piles, with bottom-entry cable provisions, wired with TECK/ACIC cables, with EMT conduit between adjacent equipment, and equipped with an outdoor GFI receptacle and equipment-removal door provisions.
- **Equipment set.** DBM allows electrical buildings to house 13.8 kV main switchgear, MV motor control centers, MV reduced-voltage soft starters, MV VFDs, 600 V MCCs, 120 V AC and 125 V DC UPS systems with battery banks and distribution panels, 600 V to 208/120 V distribution transformers and panelboards, 208/120 V contactor panels, PLC control panels, and network racks "as required by detailed design." Final equipment list is set by EPC inputs and vendor data, not by this guidance.
- **Power feed.** The 13.8 kV main switchgear distributes power radially through step-down transformers to facility electrical buildings; the specific feed to building 820-1 depends on the resolved voltage class and EPC integration topology.
- **Hazardous-area classification.** Electrical buildings shall be located in general purpose areas. If the EPC site decision places this building near a classified area, enclosure ratings, conduit seals, and equipment selection must be coordinated. Final classification is `TBD` pending EPC site decisions.
- **Foundation and grading.** DBM specifies elevated, pile-supported foundations to provide cable space beneath the building. Vendor design shall coordinate with EPC Grading / Site Drainage / Spill Containment and Structural / Foundations / Supports interfaces.
- **Door sizing.** Equipment doors (or removable transoms) shall accommodate removal of the largest housed equipment, which depends on the equipment list resolved through vendor data.
- **Drain / containment.** DBM does not state package-specific drain/containment detail for electrical buildings; the vendor shall coordinate floor drain and containment provisions with the EPC Drain / Containment interface.

## Trade-offs

- **Voltage-class assumption vs. defer.** Designing to a single assumed voltage class (e.g., 600 V or 6.9 kV) before CFL-038-04-001 is ruled risks rework. Deferring detailed equipment selection until the ruling slows vendor schedule but preserves correctness. Recommended: develop a building shell and HVAC basis that supports either voltage class, and hold detailed MCC/switchgear configuration until the ruling.
- **Shop-only vs. partial field finish.** DBM marks 820-1 as Shop fabricated. Maximizing shop assembly reduces field risk but constrains shipping dimensions; partial field finish increases construction scope (`DEL-038-03`).
- **HVAC sizing.** n + 1 redundancy is mandatory per DBM; oversizing increases cost but eases future capacity additions, while sizing to the n + 1 minimum lowers cost but tightens future flexibility.
- **UPS inclusion.** Including 120 V AC and 125 V DC UPS systems inside the 820-1 building (DBM-permitted) increases building footprint but reduces inter-building cabling. Decision depends on EPC site topology.

## Examples

- A prefabricated, modular Shop-fabricated electrical building tagged 820-1, located in a general purpose area, pile-supported, with n + 1 HVAC, bottom-entry power cabling, TECK/ACIC wiring, EMT inter-cabinet conduits, an outdoor GFI receptacle, and equipment-removal doors — housing 600 V MCCs, distribution transformers and panelboards, contactor panels, PLC and network racks, and (per EPC decision) 120 V AC / 125 V DC UPS systems. (ASSUMPTION: representative configuration; actual equipment set set by vendor data once CFL-038-04-001 is ruled.)
- A vendor design basis documenting the twelve interface positions for `PKG-038` and the vendor's response to each at the building boundary.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFL-038-04-001 | Building tag `820-1` voltage class differs between sources: workbook package name "600V ELECTRICAL BUILDING (820-1)" vs. DBM electrical-buildings table entry "820-1 6.9kV Inlet / Sales Compressor Electrical Building". | Workbook Packages row 40 (`PACKAGE_REGISTER.csv` row `PKG-038`) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings table | Datasheet identification and attributes; Specification REQ-038-04-004, REQ-038-04-006, REQ-038-04-010; Guidance Principles, Considerations, Trade-offs; Procedure Step 2 | Treat the building identity as tag `820-1` and defer voltage-class commitment until EPC integration rules; vendor design shall accommodate either class until ruling. | TBD |
| CFL-038-04-002 | Equipment list for the 820-1 building is open. DBM lists permitted equipment ("as required by detailed design") but does not assign a PKG-038-specific equipment schedule. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section | Workbook Packages row 40; Gate 7 registers (silent on package-specific equipment counts) | Datasheet attributes; Specification REQ-038-04-006, REQ-038-04-011; Guidance Considerations | Record equipment list as `TBD` to be resolved by vendor data after voltage-class ruling. | TBD |
| CFL-038-04-003 | Installation location for the 820-1 building is unassigned; DBM places electrical buildings in general purpose areas but does not assign a site coordinate. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph | Gate 7 registers (silent on PKG-038 site location) | Datasheet construction; Specification standards (area classification); Guidance Considerations | Defer installation location to EPC integration; vendor design accommodates pile-supported, general-purpose-area placement until resolved. | TBD |
