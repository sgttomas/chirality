# Guidance: DEL-032-04_vendor-engineered-equipment-package

## Purpose

Provide directional guidance for engineering and reviewing the Package Vendor production unit for `PKG-032` (Cathodic Protection Design and Installation). This deliverable produces the vendor-engineered physical equipment package and its design basis/datasheet set, anchored by the accepted EPC Scope of Work (`DEL-032-01`) and Package Datasheet (`DEL-032-02`), and integrated by the EPC Integrator into the broader facility design.

## Principles

- Preserve the accepted responsibility split: Package Vendor owns package engineering, design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration and interfaces (`PACKAGE_REGISTER.csv` row `PKG-032`).
- Stay anchored to accepted EPC inputs (`DEL-032-01`, `DEL-032-02`). Do not expand the vendor package by inferring scope absent from those inputs.
- Treat cathodic protection design and supply as an owner-coordinated scope at the facility boundary (`4-25_Deepcut_DBM.md`, Cathodic Protection). The vendor package fulfills the cathodic-protection scope itself; the facility coordinates interfaces to it rather than absorbing it into facility design.
- Engineer all four declared interfaces (Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network) explicitly; do not silently drop or overload interface scope.
- Mark unsupported values `TBD` and label inferences `ASSUMPTION`. Do not invent quantities, ratings, or method choices ahead of vendor data.

## Considerations

- Grounding interaction: cathodic protection inevitably interacts with facility grounding and bonding. The vendor must coordinate with the EPC grounding scheme (`IFC-F1FE9DF9DD`) such that cathodic protection does not compromise grounding integrity or vice versa. Detailed coordination steps are TBD pending vendor design.
- Method selection (impressed-current vs. sacrificial anode) is not specified in accessible source slices. The vendor shall select the method based on protected-asset characteristics, soil conditions, and owner preference.
- The 3-25 DBM lists cathodic protection within electrical design scope, while the 4-25 DBM excludes it from facility design scope. See the Conflict Table below.
- Remote monitoring of cathodic protection (rectifier output, anode current, reference cell readings) may use the declared Communications / Network interface (`IFC-8594557BD3`). Vendor shall confirm whether monitoring is in scope for this package.

## Trade-offs

- Impressed-current vs. sacrificial anode is a primary trade-off (initial cost, operating cost, monitoring complexity, protected-asset suitability). The accessible source set does not constrain this choice for PKG-032; the vendor shall justify the selected method in the vendor design basis.
- Tight coupling to facility grounding can simplify integration but increases the risk of stray-current effects; loose decoupling improves cathodic performance but increases integration complexity at the Grounding / Bonding interface.

## Examples

No package-specific examples are present in accessible source slices for PKG-032. Vendor experience and conventional NACE/AMPP practice (`ASSUMPTION`) should inform examples in the vendor design basis, with sources cited there rather than asserted here.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-032-04-001 | Cathodic protection is included in the electrical design scope per the 3-25 DBM, but excluded from facility design scope per the 4-25 DBM. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical design scope paragraph | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cathodic Protection section | Datasheet `Attributes`; Specification `Scope`, `Requirements` REQ-032-04-004; Guidance `Principles` | Treat 4-25 DBM as authoritative for facility-design boundary (cathodic protection is owner/vendor scope; facility supports owner interfaces). PKG-032 itself is the production unit that performs the cathodic protection scope. | TBD |
| CONF-032-04-002 | Source set does not specify cathodic protection method, anode type, rectifier ratings, protected-asset coverage, quantities, or location for PKG-032. | `_REFERENCES.md` (no package-specific source slices) | `26020-Package_Requirements.docx` (not retrieved for PKG-032 in this run) | Datasheet `Attributes`, `Construction`; Specification `Requirements` REQ-032-04-008 | Hold all such values as `TBD` until vendor data is produced. Vendor to populate during package engineering. | TBD |
