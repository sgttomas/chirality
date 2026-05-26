# Guidance — DEL-057-04 Vendor Engineered Equipment Package (Stabilizers)

## Purpose

This deliverable is the **Package Vendor production unit** for the three (3) Inlet Stabilizer Packages comprising PKG-057. The vendor engineers, designs, fabricates/supplies, and delivers the physical equipment package on the basis of the EPC Integrator's Scope of Work (DEL-057-01) and Package Datasheet (DEL-057-02). Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-057-04; SOW-0177.

The vendor scope is a contained mechanical package that converts MPFF bottoms into stabilized C5+/NGL product meeting the project's vapour-pressure, density, and CAPP butane-equivalent specifications, while routing overhead vapours to the SOC at defined interface pressures. Source: DBM §SEC-04 L676–L710; product specifications DBM L685–L687, L484.

## Principles

- **Source authority over decomposition.** The DBM (`DBM-Deepcut/4-25_Deepcut_DBM.md` §SEC-04) is the live design basis. Where the decomposition narrative and DBM disagree, DBM governs. The package's binary RFQ (`26020-01-PT-RFQ-17-005_Inlet Stabilizers_R0.docx`) and `26020-Package_Requirements.docx` package heading 12 are authoritative but are not directly readable in this run; clause-level claims must be traced back to those documents in detailed engineering. Source: `_REFERENCES.md`; `PACKAGE_REGISTER.csv` row PKG-057.
- **EPC handoff, not parallel design.** The vendor consumes the EPC Scope of Work (DEL-057-01) and Package Datasheet (DEL-057-02); the vendor does not redefine package boundaries. Integration reviews are EPC-Integrator-led. Source: SOW-0177; `PACKAGE_REGISTER.csv` row PKG-057.
- **Conservative sparing on 3 × 40 % basis.** Three installed units at 40 % each give 120 % installed capacity; loss of one unit leaves 80 % capacity. This is acceptable for normal operation but constrains line-pack/off-design transients. Source: DBM L612, L682–L684.
- **Skid-edge discipline.** Vendor responsibility ends at skid edge: interconnecting piping, foundations, MCC supply, and DCS integration are owner/EPC scope. Source: SOW-0180.

## Considerations

- **Reboiler heat-medium temperature** is to be reviewed in detailed engineering. The vendor's reboiler thermal design depends on the heat-medium supply/return temperatures locked in the heat-medium utility deliverable. Source: DBM L706.
- **Product cooler elevation.** Whether the product cooler bundle should be elevated 25 ft above grade to reduce flare-header loading in the fire case has not been ruled. Stabilizer low design pressure and flare backpressure limitations drive this decision. Source: DBM L708.
- **Flash/feed retention time** is carried at 15 minutes in SOW-0180 but tagged "TBC" in DBM L704. Vendor sizing should hold ≥10 minutes between LLL and HLL as the hard floor and reconcile the 15-minute target with the EPC before issuing vessel datasheets. Source: SOW-0180; DBM L704.
- **Strainer mesh and pump seal type** are TBD pending pump selection. The vendor should converge these with the feed-pump OEM at the package design freeze, not push them to construction. Source: DBM L706.
- **Stabilizer overhead disposition** is tied to the SOC (PKG-050). Loss of SOC capacity directly constrains stabilizer throughput because the overhead vapour route is pressure-controlled to SOC second-stage suction. Source: DBM L678.

## Trade-offs

- **3 × 40 % vs. 2 × 100 % / 2 × 50 %.** The 3 × 40 % choice is set by the DBM (L682–L684). It trades capital cost (three smaller packages) for operational flexibility and turndown coverage; it accepts 80 % capacity on a single failure.
- **NEN thermosiphon reboiler vs. kettle.** The DBM specifies a vertical NEN single-pass thermosiphon shell-and-tube exchanger with process on the tube side, sited outside the building wall for cleaning access (DBM L706). The trade-off is: higher cleaning accessibility and lower fouling risk on the tube side, against the higher headroom and structural-support cost of an external vertical exchanger. Vendor should not substitute a kettle reboiler without explicit EPC ruling.
- **Aerial product cooler with 130 % excess area.** The 130 % excess area trades capital and footprint against the combined design duty (cooler alone vs. cooler + feed/bottoms exchanger duty whichever is higher) and ambient-temperature variability. Source: SOW-0180; DBM L708.
- **Devchem 253 internal coating on flash/feed separator** (DBM L704) trades coating QA and inspection burden against corrosion margin given residual produced water and sour service. Coating substitution requires EPC ruling.

## Examples

The DBM stabilizer tables (DBM L680–L688, L692–L700) provide the per-package basis the vendor must meet. Example reading:
- A single stabilizer must handle up to 2.821 MMSCFD total two-phase inlet (winter design) at the 1,272 m³/d (8,000 bbl/d) per-package liquid design rate. DBM L683, L697.
- The product must hit < 85 kPaa vapour pressure (ASTM D6377), 650–775 kg/m³ density, and CAPP butane equivalent < 5 vol %. DBM L484, L685–L687.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-01 | Flash feed separator retention time stated as ~15 minutes in scope ledger but tagged "TBC" in DBM | SOW-0180 (Operating conditions) | `DBM-Deepcut/4-25_Deepcut_DBM.md` L704 | Datasheet "Conditions"; Specification R3; Procedure prerequisites | PROPOSAL: Treat 15 min as a target subject to TBC; hard floor is ≥10 min between LLL and HLL per DBM L704. | TBD |
| CONF-02 | Direct clause references to `26020-Package_Requirements.docx` package heading 12 not accessible (binary) | `_REFERENCES.md` Missing/Deferred | SOW-0177..0180 extracts | All four documents (Standards, References) | PROPOSAL: All clause-level claims carried as SOW extracts; mark `location TBD` for the docx. Re-resolve when a text/markdown copy of package heading 12 is staged in `_Sources`. | TBD |
| CONF-03 | Stabilizer overhead gas disposition under revised downstream configuration tagged "to be confirmed" | DBM L690 | (no other source) | Datasheet "Boundary and Routing Notes"; Specification R11 | PROPOSAL: Retain current basis (overhead to SOC 2nd-stage suction) until SOC interface deliverable rules otherwise. | TBD |
| CONF-04 | Objective-to-deliverable association carried as PACKAGE_HEURISTIC ASSUMPTION (OBJ-001, OBJ-003..OBJ-010) | `_CONTEXT.md`; `OBJECTIVE_DELIVERABLE_MAP.csv` | (mapping operates at package grouping) | All four documents (Identification / Objectives) | PROPOSAL: Carry as ASSUMPTION until human confirms the deliverable-ID-level mapping. | TBD |
