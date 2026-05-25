# Guidance: DEL-020-04_vendor-engineered-equipment-package

## Purpose

This guidance supports the Package Vendor production unit (engineering, design, fabrication/supply, and physical equipment) for the 13.8kV SWITCHGEAR EQUIPMENT package, `PKG-020`. The deliverable converts the accepted EPC Scope of Work and EPC Package Datasheet into a vendor-engineered package with a defendable design basis and supplied equipment. EPC integration review is performed downstream (`DEL-020-06`).

## Principles

- **Vendor inputs are EPC outputs.** The vendor design starts from `DEL-020-01` (Scope of Work) and `DEL-020-02` (Package Datasheet). The vendor shall not invent package scope outside those inputs.
- **Responsibility split is preserved.** Package engineering, design, vendor documentation, and physical equipment belong to the Package Vendor. Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration belong to the EPC Integrator.
- **Source-anchored values only.** Where accessible source slices (DBM electrical sections, Gate 7 registers, workbook row 22) define a value or constraint, the vendor design shall reflect it. Where source is silent, values remain `TBD` for vendor data to close — not for invention by drafting.
- **Interfaces drive design, not the reverse.** The six package interfaces (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) are inputs to vendor engineering, not items the vendor may redefine.
- **Standby power and integration items remain with the EPC.** The vendor designs for compatibility; no 13.8 kV-level emergency generator interface is to be engineered into this package because the standby-power basis has moved to low-voltage MCC generators with transfer switches.

## Considerations

- **Plant main distribution role.** The 13.8 kV switchgear is the plant main power distribution center. Bus sizing, breaker schedule, and protective-relay coordination must support the full facility scope, not just one downstream feeder. Specific values are `TBD` pending electrical studies and vendor data.
- **Upstream and downstream boundaries.** Upstream: utility-supplied 25 kV/13.8 kV transformer (outside this package). Downstream: step-down transformers (13.8 kV/4.16 kV, 13.8 kV/600 V) feeding electrical buildings, plus the 04-25 → 03-25 cross-facility sub-feed. The vendor package terminates at its incoming and outgoing 13.8 kV terminations; cables, transformers, and remote equipment are outside the package.
- **Indoor electrical building.** DBM identifies a "13.8 kV Switchgear Electrical Building" as a prefabricated, modular shop-built building. Vendor design should anticipate indoor electrical-building installation while leaving final building assignment to EPC integration.
- **Grounding application.** Low-resistance grounded 13.8 kV system; major-equipment two-point ground grid connection and CEC-sized grounding conductors apply per DBM. Vendor switchgear grounding bus and bonding provisions shall accommodate this.
- **Cable separation and access.** 13.8 kV, 4,160 V, and 600 V power circuits must be separated from control/instrument circuits; vendor-supplied internal cable management, terminations, and access provisions must preserve maintenance access and arc-flash safety boundaries.
- **MV cable basis.** Three-conductor copper TECK 15 kV, 133% insulation, shielded — the vendor package shall terminate or supply MV cable consistent with this basis where applicable.
- **Co-located equipment.** The switchgear electrical building may also house MV MCCs, MV soft-starters, MV VFDs, 600 V MCCs, UPS systems, distribution transformers, contactor panels, PLC panels, and network racks. The vendor package boundary must remain distinct from these adjacent vendor packages.

## Trade-offs

- **Single bus vs. main-tie-main or double-ended.** Bus configuration affects redundancy, breaker count, and arc-flash zones. Source does not prescribe a configuration; the EPC Package Datasheet and electrical studies drive this trade-off.
- **Air-insulated vs. gas-insulated switchgear (AIS vs. GIS).** AIS is conventional and typical for indoor electrical buildings; GIS reduces footprint but adds gas-handling and serviceability considerations. Source is silent; vendor recommendation point.
- **Arc-resistant vs. standard metal-clad switchgear.** Arc-resistant designs reduce arc-flash hazard at the cost of capital and maintenance access patterns; trade-off depends on EPC arc-flash policy.
- **Protective-relay platform.** Vendor protective-relay selection (IED platform, communications protocol) affects the Communications / Network interface and integration with facility-wide protection coordination.
- **Spare cubicles / capacity margin.** Headroom for future feeders vs. footprint/cost; vendor proposal to be confirmed against the EPC Package Datasheet.

## Examples

- A vendor 13.8 kV metal-clad indoor switchgear lineup with one incoming utility feeder breaker, multiple outgoing feeder breakers to step-down transformers and the 03-25 sub-feed, microprocessor protective relays, control wiring to the electrical-building network/PLC, and a prefabricated electrical building enclosure interface. (ASSUMPTION: representative configuration; actual configuration set by vendor data and the EPC Package Datasheet.)
- A vendor design basis documenting the six interface positions (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) and the vendor's response to each at the package boundary.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFL-020-04-001 | Package title states "13.8kV SWITCHGEAR EQUIPMENT" but accessible sources do not define bus continuous current, short-circuit duty, breaker schedule, or protective-relay scheme for PKG-020. | Workbook Packages row 22 (package name and discipline) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (general 13.8 kV switchgear basis only) | Datasheet attributes; Specification REQ-020-04-005, REQ-020-04-012; Guidance Considerations | Treat the package identity as 13.8 kV main switchgear and leave detailed ratings, breaker counts, and protection scheme `TBD` until vendor data and EPC Package Datasheet resolve them. | TBD |
| CFL-020-04-002 | Installation location: DBM names a "13.8 kV Switchgear Electrical Building" (`810-1`) as a shop-built modular electrical building, but no Gate 7 register row confirms PKG-020's assignment to that specific building. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph and equipment-building table | Gate 7 registers (silent on PKG-020 location) | Datasheet construction; Specification standards (area classification); Guidance Considerations | Defer building assignment to EPC integration; vendor design accommodates indoor electrical-building installation as the working basis. | TBD |
| CFL-020-04-003 | Standby power: DBM eliminates the prior 13.8 kV emergency generator concept and uses LV standby generators on 600 V MCCs; the vendor package should therefore not engineer a 13.8 kV emergency interface, but the EPC Package Datasheet may still call for one. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, standby power paragraph; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, emergency power paragraph | EPC Package Datasheet (`DEL-020-02`) — not extracted into deliverable-local truth set | Datasheet attributes (standby/emergency tie-in); Specification REQ-020-04-007; Guidance Principles | Adopt the DBM "no 13.8 kV emergency-generator interface" basis unless `DEL-020-02` explicitly overrides; flag any override as an integration issue at `DEL-020-06`. | TBD |
| CFL-020-04-004 | Industry standards (e.g., IEEE/CSA metal-clad switchgear, arc-resistant testing) are likely applicable but not extracted from accessible source materials. | Industry convention for MV metal-clad switchgear (ASSUMPTION) | `_REFERENCES.md` (no clause-level standard text accessible) | Specification Standards | Carry standard family as ASSUMPTION until the EPC Package Datasheet or `26020-Package_Requirements.docx` slice is extracted and confirms specific editions/clauses. | TBD |
