# Package Datasheet Guidance — PKG-076 Lube Oil Supply

## Purpose

The Package Datasheet for PKG-076 Lube Oil Supply exists so the EPC Integrator can hand a third-party Package Vendor or discipline package engineer (DEL-076-04) the package data needed to engineer, design, and supply the lube oil storage and transfer system without re-reading the full plant DBM. It is one of the four mandatory Gate 5 EPC anchor deliverables for PKG-076 (Scope of Work, Package Datasheet, Construction Work Package, plus the three Gate 5 vendor/acceptance deliverables) per `_CONTEXT.md` and the GATE-07 DELIVERABLE_REGISTER.

## Principles

- **Source-anchored.** Every non-trivial value in the Datasheet should trace to `4-25_Deepcut_DBM.md` SEC-08 §"Lube Oil Storage and Pump Basis", §"Utility System Summary", §"Package Line-Item Requirements" row 51, or to the cross-referenced `3-25_Comp_and_Liquids_DBM.md` lube-oil note. Where the source itself says TBC/TBD, the Datasheet preserves that label.
- **Bounded scope.** The Datasheet describes storage tanks, transfer pumps, and the interface to served compressor packages. Day tanks at each compressor frame and the compressors' own integral electric circulating lube oil heaters belong to the served compressor packages (`4-25_Deepcut_DBM.md` SEC-05 §828, §928, §967).
- **Carry the interface evidence.** `_CONTEXT.md` notes that interface facts for PKG-076 are intentionally carried in the Package Datasheet rather than as standalone deliverables. The interface summary section is therefore the primary handoff surface for vendor scoping.
- **Don't invent design values.** Specific gravity 1.00 (TBC), 400 bbl cylinder tank, and 200 bbl crank-case tank are the only quantitative basis values stated. Cylinder oil grades, frame oil grade, tank materials, area classification, tank heating utility, secondary containment, and additional storage requirements are all stated as TBC/TBD or are absent from the accessible source and remain TBD.

## Considerations

- **Multiple cylinder oils may be required.** Different compressor services (inlet/sales, sales booster, stabilizer overheads, acid gas) handle different gas compositions including H2S, sulphur, and rich gas, and the source explicitly warns that manufacturer-recommended cylinder oils may differ across services. The Package Vendor must therefore size storage for the possibility of more than one cylinder oil SKU. (Source: `4-25_Deepcut_DBM.md` §"Lube Oil Storage and Pump Basis".)
- **Heated storage is required.** Both tanks are described as heated. The source does not specify the heating medium (heat medium loop, electric trace, or jacket steam). Selection should be cross-checked against the heat medium loop open item in §"Open Design Development Requirements".
- **Hazardous-material list controls.** `3-25_Comp_and_Liquids_DBM.md` notes that lube-oil storage is referenced to the project hazardous-material list but the list was not available in the workspace. Final containment, area classification, and spill response basis depend on that list.
- **Reciprocating compressor packages include their own electric circulating lube oil heater for quick start** (e.g. SOC inlet/sales compressors §828; sales gas booster §967; acid gas compressors §1027). The PKG-076 transfer pumps replenish frame day tanks; they do not provide compressor-frame oil temperature control.
- **The Expander has its own dedicated Expander Lube Oil Pumps and Filters (2 × 50%)** listed under the cryogenic package sparing register; that lube oil system is internal to the Expander/Compressor and is not part of PKG-076. (Source: `4-25_Deepcut_DBM.md` SEC-09 sparing register, Expander Lube Oil Pumps / Filters.)

## Trade-offs

- **Single bulk storage vs. service-segregated storage.** A single 400 bbl cylinder tank assumes one cylinder oil SKU; multiple SKUs may force segregated storage and additional pumps. The source flags additional storage requirements as TBD; vendor should propose segregation strategy based on final cylinder oil selections.
- **Transfer pump sparing.** SEC-08 implies two service-dedicated pumps (one cylinder, one crank-case), neither with an installed spare. SEC-09's sparing register entry for a single "Lube Oil Transfer Pump" at 1 × 100% does not match the two-pump SEC-08 basis. Operability and maintainability trade-offs depend on resolving this conflict (see Conflict Table).
- **Tank heating medium.** Heat-medium tracing reuses an existing utility but adds heat-medium load; electric trace is independent of the heat-medium loop but adds electrical load and complicates classification. The source does not select.

## Examples

The Datasheet content for analogous heated atmospheric tank packages on the 4-25 facility (e.g. Caustic tanks, Condensate tanks listed as API 650 in `4-25_Deepcut_DBM.md` §"Package Line-Item Requirements") can be used as a structural template for tank-design fields, but **values must not be carried across** — only the field-set pattern (capacity, design SG, materials, heating, containment, area classification, tag, location).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-076-02-01 | Pump count and sparing: SEC-08 lists two service-dedicated pumps (P-9240-1 cylinder, P-9250-1 crank-case) with no implied spare; SEC-09 sparing register lists "Lube Oil Transfer Pump" 1 × 100% (single pump, no spare). | `4-25_Deepcut_DBM.md` §"Lube Oil Storage and Pump Basis" (lines 2068-2070) and §"Package Line-Item Requirements" row 51 | `4-25_Deepcut_DBM.md` SEC-09 sparing register row "Lube Oil Transfer Pump" (line 2363) | Datasheet Attributes table; Spec REQ-076-02-02, REQ-076-02-09 | PROPOSAL: SEC-08 line-item basis (two service-dedicated pumps P-9240-1 and P-9250-1) governs; SEC-09 sparing entry is a partial/legacy summary. | TBD |
| CONF-076-02-02 | Hazardous-material classification basis: `3-25_Comp_and_Liquids_DBM.md` references the project hazardous-material list as the controlling document, but the list is not in the accessible workspace. | `3-25_Comp_and_Liquids_DBM.md` §"Emergency Power, Lube Oil, and Analyzers" | (absent locally) | Datasheet Construction row (Hazardous-materials inventory); Spec REQ-076-02-08 | PROPOSAL: leave classification as TBD; require retrieval of hazardous-material list before Datasheet Gate 5 issue. | TBD |
| CONF-076-02-03 | Tank construction standard: Other 4-25 atmospheric tanks are explicitly tagged "API 650" in the package basis; lube oil tanks are not. | `4-25_Deepcut_DBM.md` §"Package Line-Item Requirements" rows for "Tanks, Caustic/Condensate/DSO/Sour Water/Water (API 650)" | `4-25_Deepcut_DBM.md` §"Lube Oil Storage and Pump Basis" (no construction standard cited) | Datasheet Construction row (Tank materials/code); Spec Standards row | PROPOSAL: ASSUMPTION API 650 applies for heated atmospheric oil storage; confirm in detailed engineering. | TBD |
