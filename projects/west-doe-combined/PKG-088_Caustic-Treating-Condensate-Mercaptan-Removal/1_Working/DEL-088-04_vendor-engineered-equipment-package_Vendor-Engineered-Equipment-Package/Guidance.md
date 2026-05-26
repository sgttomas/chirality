# Guidance — DEL-088-04 Vendor Engineered Equipment Package

## Purpose

This Guidance provides directional context for the Package Vendor and EPC Integrator integrating the Caustic Treating (Condensate Mercaptan Removal) equipment package. The Vendor production unit is the engineered/fabricated package developed from the EPC Scope of Work (DEL-088-01) and Package Datasheet (DEL-088-02); EPC Integrator retains facility integration responsibility (SOW-0055). (Source: DELIVERABLE_REGISTER row 267; SCOPE_LEDGER SOW-0055.)

## Principles

1. **Non-regenerative basis is settled.** The current 03-25 basis explicitly excludes caustic regeneration; the package operates on continuous fresh caustic and make-up water consumption with spent caustic and DSO outflows. Do not propose a regenerative alternative without a sanctioned change request. (Source: DBM-Comp_and_Liquids §Condensate Mercaptan Treating.)
2. **Indoor caustic handling.** All caustic treating equipment is indoor in the caustic building. Aluminum is prohibited in the caustic building. Layout, ventilation, and material selection must respect these constraints from concept onward. (Source: SOW-0058; DBM-Comp_and_Liquids §Condensate Mercaptan Treating.)
3. **Product specification drives package design.** Treated product targets — C1-C3 RSH below 175 ppmw S and total sulphur below 0.5 wt% — are the package's primary functional requirement. Sizing of contactor, water wash, caustic strength, and circulation rates must demonstrate compliance with these targets. (Source: SOW-0058.)
4. **Vendor TBC closure is required.** Several values in the design basis carry TBC qualifiers (caustic SG 1.75; DSO entrainment design 50 ppmw S; caustic tank material/coating). Vendor responses must close each TBC explicitly rather than carry them silently. (Source: DBM-Comp_and_Liquids §Condensate Mercaptan Treating.)
5. **Anchor to upstream EPC deliverables.** This vendor deliverable develops from DEL-088-01 (Scope of Work) and DEL-088-02 (Package Datasheet). Do not source-substitute the decomposition narrative for the EPC anchoring deliverables once those are issued. (Source: `_CONTEXT.md` Notes; DELIVERABLE_REGISTER row 267.)

## Considerations

- **Interface envelope.** The package has defined external interfaces with the incinerator overhead, dilution gas, and enrichment gas systems, plus condensate inlet/outlet and consumable/waste connections. Vendor layout must respect EPC-defined tie-in locations and the no-VRU constraint on fresh caustic. (Source: DBM-Comp_and_Liquids §Condensate Mercaptan Treating.)
- **Extractable slate.** Design must accommodate H2S, CO2, and methyl/ethyl/propyl/butyl mercaptans, recognizing that volatile mercaptan handling and a possible waiver are open items. (Source: DBM-Comp_and_Liquids; SOW-0058.)
- **Spent caustic management.** Atmospheric 32 oz tanks with LP fuel-gas blanket, heating, and insulation are specified; spent caustic vents to incinerator header through a flame arrestor and supports truck-out. The vendor must coordinate venting, blanketing, and trucking interfaces with EPC integration scope. (Source: DBM-Comp_and_Liquids §Condensate Mercaptan Treating.)
- **Material/coating selection.** The DBM flags aluminum prohibition and "caustic tank material/coating details remain TBC." Treat these as binding constraints for the engineered package and resolve TBCs early to avoid late re-fabrication. (Source: DBM-Comp_and_Liquids §Condensate Mercaptan Treating.)
- **Equivalence claims.** "Merichem or equivalent" appears in the DBM. Equivalent-package proposals must demonstrate equal or better compliance with the specification's product targets and the indoor/no-aluminum constraints. (Source: DBM-Comp_and_Liquids §Condensate Mercaptan Treating.)

## Trade-offs

- **Caustic concentration vs. handling hazard.** 50 wt% NaOH gives mass-efficient mercaptan extraction but raises freezing and handling concerns — hence the heated, insulated, blanketed tank requirement. Lower concentrations would relax handling but increase footprint and consumption rate. (Source: DBM-Comp_and_Liquids §Condensate Mercaptan Treating; trade-off framing is ASSUMPTION based on standard caustic treating practice.)
- **Product target margin vs. caustic consumption.** Tighter contact stages and higher circulation rates improve product sulphur margin but increase spent caustic generation and trucking frequency. Vendor sizing should disclose the margin at design conditions. (ASSUMPTION: standard caustic treating trade-off, not explicit in source.)
- **DSO entrainment design point.** Expected entrainment is 30 ppmw S, design 50 ppmw S TBC. Designing to a tighter value reduces downstream DSO handling but increases water-wash and filtration complexity. (Source: DBM-Comp_and_Liquids §Condensate Mercaptan Treating.)

## Examples

- **Stream slate example.** The DBM identifies methyl mercaptan, ethyl mercaptan, dimethyl sulphide, 2-propanethiol, n-propyl mercaptan, and methyl ethyl sulphide as volatile mercaptans in the design condensate basis (lines 210, source DBM). The vendor package design must address the C1-C4 RSH portion of this slate in the contactor; volatile sulphide species disposition depends on the SOW-0058 waiver resolution. (Source: DBM-Comp_and_Liquids §Condensate and Produced-Water Receipts; SOW-0058.)
- **Total facility capacity context.** The 03-25 Liquids Hub treats 20,000 bbl/d of C5+ condensate aggregated from 04-25, 06-29 Canlin, and future third-party stabilized condensate sources; the package is sized to the hub total. (Source: DBM-Comp_and_Liquids lines 376–383.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-088-04-01 | Authoritative source text in `26020-Package_Requirements.docx` package heading 41 is not text-accessible; PKG-088 scope items (SOW-0056..0058) are extracted into SCOPE_LEDGER but the verbatim source slice cannot be cross-checked. | `_Sources/26020-Package_Requirements.docx` (binary; inaccessible) | SCOPE_LEDGER.csv rows 57–59 | Specification REQ-088-04-04..-08; Datasheet Attributes | SCOPE_LEDGER as working authority pending docx extraction. | TBD |
| CT-088-04-02 | "Merichem or equivalent" — equivalence criteria not defined in accessible source. | DBM-Comp_and_Liquids §Condensate Mercaptan Treating | (none) | Guidance Considerations; Procurement basis | Treat as competitive with vendor demonstration of equivalent compliance to product targets and indoor/no-aluminum constraints. | TBD |
| CT-088-04-03 | Volatile mercaptan waiver applicability (SOW-0058) is "possible" and unresolved. | SCOPE_LEDGER SOW-0058 | DBM-Comp_and_Liquids §Condensate and Produced-Water Receipts (lists volatile species without waiver) | Specification REQ-088-04-06, -18; Guidance Examples | Vendor designs to extract C1-C4 RSH per product targets; volatile mercaptan and sulphide handling decision deferred to ruling. | TBD |
| CT-088-04-04 | DSO entrainment design (50 ppmw S) carries "TBC vendor"; caustic SG 1.75 carries "TBC"; caustic tank material/coating "TBC". | DBM-Comp_and_Liquids §Condensate Mercaptan Treating | (none) | Datasheet Attributes/Conditions; Specification REQ-088-04-14, -15, -19 | Vendor closes TBCs in package design basis prior to acceptance. | TBD |
