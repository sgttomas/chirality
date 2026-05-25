# Guidance: DEL-022-04_vendor-engineered-equipment-package

## Purpose

`DEL-022-04` is the Package Vendor's production-unit deliverable for the medium-voltage switchgear package (`PKG-022`, "5kV SWITCHGEAR EQUIPMENT"). It carries the vendor's engineering, design, fabrication/supply, and the physical equipment, framed by the EPC Scope of Work (`DEL-022-01`) and Package Datasheet (`DEL-022-02`), and concluded by EPC Vendor Package Review and Acceptance (`DEL-022-06`). This Guidance interprets the deliverable conservatively from the available source materials and surfaces the open items that need a human ruling before downstream work over-commits.

## Principles

- **EPC anchors the package; Vendor engineers the package.** The EPC Scope of Work and Package Datasheet are the upstream package contract. This deliverable is the vendor's response, not a re-derivation of facility scope.
- **Source over convention.** Where the DBM and project Electrical specifications state a requirement (e.g., MV MCC Ethernet communication ports, grounding-resistor sizes, cable insulation classes), use the source basis. Do not invent vendor design parameters from convention.
- **Title carries identity, not engineering numbers.** "5kV SWITCHGEAR EQUIPMENT" identifies the package but does not, by itself, define nominal bus voltage, equipment count, or physical scope. Treat the title as identity until the Package Datasheet confirms numbers.
- **Conservative when source is silent.** When the source is silent on a package-specific parameter, prefer `TBD` over a derived value.

## Considerations

- **Voltage class.** The facility electrical basis uses 13.8 kV (backbone), 6.9 kV, and 4.16 kV as medium-voltage services, and 5 kV is the insulation class used for 4.16 kV cabling. A nominal "5 kV" switchgear bus is not separately called out in the DBM. The vendor's bus voltage and equipment scope should be confirmed against the Package Datasheet (`DEL-022-02`) before fabrication release. See Conflict Table HRR-022-04-001.
- **MCC versus switchgear scope.** The electrical specifications table separates Medium Voltage Switchgear (`ELC-QAS-000007-001`) from Medium Voltage Motor Control Centers (`ELC-QAS-000008-001`). The vendor scope should not silently fold MCC content into switchgear scope or vice versa.
- **Control power.** Protection and breaker control rely on 120 VAC / 125 VDC UPS services. The vendor's interface with the UPS package (`PKG-013` 100A DC UPS or related) should be coordinated through the package interface requirements matrix.
- **Studies before final ratings.** Short-circuit, relay coordination/arc-flash, load-flow, and load analysis study outputs are inputs to equipment ratings. Releasing for fabrication before these studies are accepted risks rating mismatches.
- **Building integration.** Electrical buildings are prefabricated, modular, climate-controlled (HVAC n+1), bottom-entry. Specifying equipment that requires top-entry or out-of-envelope environmental conditions creates an integration conflict.
- **Hazardous area marking.** Electrical buildings are generally general-purpose; however, VFD-fed motors in Zone 2 areas have specific marking requirements per the DBM. Vendor-supplied auxiliaries crossing into Zone 2 areas need to be specified with appropriate area classification.

## Trade-offs

- **Vendor standardization versus project specificity.** Vendors often prefer their standard designs; the project specification stack (`ELC-QAS-000003-001`, `ELC-QAS-000007-001`) sets specific requirements. Conformance matrices should make deviations explicit.
- **Single MV bus voltage versus multiple.** Combining 6.9 kV and 4.16 kV sections in one vendor package may simplify procurement but increase coordination complexity. Source does not require either approach.
- **Fabrication release timing.** Releasing for fabrication early reduces schedule risk but increases re-work risk if upstream studies or interface confirmations shift.

## Examples

- Specification conformance: a vendor specification conformance matrix that references `ELC-QAS-000007-001` Rev 1 clauses and explicitly marks deviations is the expected pattern (source: DBM electrical specifications table).
- Interface coverage: the vendor datasheet set should map directly onto the six `PKG-022` interfaces in `INTERFACE_REGISTER.csv` (Electrical Power, Grounding/Bonding, I&C/Control Cabling, Communications/Network, Maintenance Access, Structural/Foundations/Supports).

Further worked examples are TBD until vendor data or the EPC Package Datasheet (`DEL-022-02`) is available.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HRR-022-04-001 | Package title says "5kV SWITCHGEAR EQUIPMENT", but the facility electrical basis defines 13.8 kV main switchgear and 6.9/4.16 kV MV MCCs and uses 5 kV only as an insulation class for 4.16 kV cabling. Nominal bus voltage and equipment count for PKG-022 are not confirmed. | `PACKAGE_REGISTER.csv` row `PKG-022` (package title); `Workbook Packages` row 24 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Power System, System Voltages, and cabling rows | Datasheet Attributes (package function, equipment list anchor, system voltage basis); Specification R-03, R-07, R-08; Guidance Considerations; Procedure prerequisites | Treat "5kV" as title/identity only; carry nominal bus voltage and equipment count as `TBD` until the Package Datasheet (`DEL-022-02`) confirms. | TBD |
| HRR-022-04-002 | The DBM equipment list identifies Medium Voltage Switchgear (qty 1) and Medium Voltage Motor Control Centers (qty 1) but does not explicitly allocate either count to PKG-022. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical specifications equipment list | `DELIVERABLE_REGISTER.csv` / `PACKAGE_REGISTER.csv` row `PKG-022` (no equipment allocation field) | Datasheet Attributes (equipment list anchor); Specification R-07, R-08, R-14; Procedure Steps | Do not assume the qty-1 MV Switchgear belongs to PKG-022 alone; carry allocation as `TBD` until Package Datasheet confirms. | TBD |
| HRR-022-04-003 | DBM specifies that 4.16 kV MCC VFD and soft-starter requirements are TBD; if PKG-022 includes any 4.16 kV scope, vendor design must wait for this resolution. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, motor control paragraphs | None | Specification R-08; Procedure Verification | Hold any 4.16 kV vendor design for VFD/soft-starter content until the project rules. | TBD |
