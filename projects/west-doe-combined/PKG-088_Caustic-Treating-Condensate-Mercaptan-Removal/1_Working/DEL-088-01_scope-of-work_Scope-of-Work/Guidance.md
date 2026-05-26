# Guidance — DEL-088-01 Scope of Work (PKG-088 Caustic Treating, Condensate Mercaptan Removal)

## Purpose

The Scope of Work exists as the mandatory Gate-5 EPC Integrator anchor deliverable for PKG-088. It bounds what the package is, what it does, where it interfaces with the rest of the 03-25 facility, and who is responsible for which slice of work. Downstream deliverables — Package Datasheet (DEL-088-02), Construction Work Package (DEL-088-03), Vendor Engineered Equipment Package (DEL-088-04), Vendor Document Turnover (DEL-088-05), and EPC Vendor Package Review and Acceptance (DEL-088-06) — depend on this Scope of Work as their integration baseline. [Source: DELIVERABLE_REGISTER.csv; `_CONTEXT.md` Notes]

## Principles

1. **Authority hierarchy.** Where the DBM (DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md) and `26020-Package_Requirements.docx` heading 41 disagree, treat `26020-Package_Requirements.docx` heading 41 as authoritative for package-level requirements; treat the DBM as authoritative for whole-facility integration basis. [ASSUMPTION: both are project authoritative; resolution rule per Authority hierarchy convention; human ruling TBD]
2. **Package vs. integration split.** Package engineering, package design, vendor documentation, and the physical equipment package are Package Vendor scope. Tie-ins, facility-level interfaces, constructability, procurement coordination, and integration are EPC Integrator scope. [Source: PACKAGE_REGISTER.csv IntegrationModel]
3. **Source-grounded narrative.** Every substantive Scope of Work statement should trace to either the DBM, the Word package requirements, or the workbook register. Statements without a source citation are TBD or ASSUMPTION.
4. **Whole-facility integration is real, not nominal.** PKG-088 interacts with the incinerator system (overhead, dilution and enrichment gas), LP fuel-gas system (blanket gas), spent-caustic and DSO logistics (truck-out), drains (300# ANSI minimum, caustic-grade materials), and area electrical/F&G systems. Treat these as scope, not as "vendor problems." [Source: DBM-Comp_and_Liquids §Condensate Mercaptan Treating; §Drains; §LP Fuel Gas; §LEL/H2S/Methyl Mercaptan; PACKAGE_REGISTER.csv]
5. **Material restrictions are binding.** Aluminum shall not be used in the caustic building (DBM). Caustic tank coatings/materials are TBC and must not be silently chosen. [Source: DBM-Comp_and_Liquids §Condensate Mercaptan Treating]

## Considerations

- **Mercaptan toxicity.** Methyl mercaptan is a recognized toxic/odor hazard with IDLH and LC50 context referenced in the source KTY data; this drives F&G detector placement, purge design, and operator access provisions for PKG-088. The Scope of Work should reference, not duplicate, the facility F&G design. [Source: DBM-Comp_and_Liquids §LEL, H2S, Methyl Mercaptan, and Fire Detection]
- **Spent caustic truck-out vs. VRU exclusion.** The spent caustic tank vents through a flame arrestor to the incinerator header and supports truck-out; fresh caustic is NOT connected to the VRU. The Scope of Work should make these route choices explicit so they are not overridden during detailed design. [Source: DBM-Comp_and_Liquids §Condensate Mercaptan Treating]
- **Caustic drain segregation.** The caustic drain has its own design pressure regime (300# ANSI minimum, up to spent-caustic tank), temperature considerations (max 121 deg C / 250 deg F TBC), and material concerns (caustic embrittlement). The Scope of Work should call out the caustic drain as a dedicated facility interface. [Source: DBM-Comp_and_Liquids §Drains]
- **No regeneration.** The Scope of Work should explicitly state that caustic regeneration is excluded; superseded equipment rows for caustic regeneration pumps and related items are not active 03-25 design basis. Do not allow vendors to assume a regenerable system. [Source: DBM-Comp_and_Liquids §Condensate Mercaptan Treating; §Current Supersession Controls]
- **Objective association is heuristic.** Objectives OBJ-002 through OBJ-010 are mapped to PKG-088 via the package-grouping heuristic from the decomposition; they should be carried as informational context, not as binding requirements, until a per-deliverable objective ruling is recorded. [Source: OBJECTIVE_DELIVERABLE_MAP.csv; OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC]

## Trade-offs

- **Specification depth in this deliverable vs. in DEL-088-02 (Datasheet).** The Scope of Work should remain at the function/boundary/responsibility level. Detailed process/datasheet entries (sizes, MOC, design pressures/temperatures per item) belong in DEL-088-02 Package Datasheet. Avoid pulling vendor-engineering detail forward. [Source: DELIVERABLE_REGISTER.csv]
- **Stating "Merichem or equivalent" vs. open-vendor.** The DBM names Merichem as the basis. The Scope of Work should preserve "Merichem or equivalent" to maintain a defensible technical basis without prematurely sole-sourcing. [Source: DBM-Comp_and_Liquids §Condensate Mercaptan Treating]
- **TBC values vs. firm values.** Several DBM values are TBC (caustic SG 1.75, DSO design entrainment 50 ppmw, caustic drain max temp 121 deg C). The Scope of Work should reference these as DBM basis carried subject to vendor confirmation rather than declaring them firm specifications. [Source: DBM-Comp_and_Liquids §Condensate Mercaptan Treating; §Drains]

## Examples

- A correctly framed Scope of Work statement: "PKG-088 is a non-regenerative caustic treating package, Merichem or equivalent, treating 20,000 bbl/d C5+ condensate; caustic regeneration is excluded from the 03-25 basis. [Source: DBM-Comp_and_Liquids §Condensate Mercaptan Treating]"
- An incorrectly framed statement (do not produce this): "PKG-088 will use Merichem THIOLEX technology with specific clause-level performance guarantees" — clause-level vendor performance is not in any accessible source slice and would be invention.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFL-088-01-001 | Authority precedence between `26020-Package_Requirements.docx` heading 41 (package-level requirements) and DBM-Comp_and_Liquids §Condensate Mercaptan Treating (facility design basis) when both could speak to the same attribute. | `26020-Package_Requirements.docx` heading 41 (binary; not yet sliced) | DBM-Comp_and_Liquids §Condensate Mercaptan Treating | Specification §Standards; Datasheet §Attributes | PROPOSAL: Word package requirements authoritative for package-level requirements; DBM authoritative for facility integration. | TBD |
| CFL-088-01-002 | SOW-0055..SOW-0058 item text and mapping is not directly readable from any locally accessible source slice; mapping in Specification SOW-R-09 is currently TBD. | `_CONTEXT.md` Covers Scope Items | (no accessible Scope-Item register source slice) | Specification SOW-R-09 | PROPOSAL: produce Scope-Item register slice or rely on Workbook row 50 expansion. | TBD |
| CFL-088-01-003 | Objective-to-deliverable mapping for PKG-088 deliverables is package-grouped (heuristic), not deliverable-specific. | OBJECTIVE_DELIVERABLE_MAP.csv (package-grouped rows) | None | Specification SOW-R-10; Datasheet Identification | PROPOSAL: keep ASSUMPTION label until OBJECTIVE_ASSOCIATION_MODE changes or a per-deliverable objective ruling is recorded. | TBD |
