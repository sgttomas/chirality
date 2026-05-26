# Guidance — DEL-066-04 Vendor Engineered Equipment Package

> Directional rationale for the Package Vendor and EPC Integrator working on the PKG-066 condensate storage tank package, framed around the Modified API 650 basis at the 04-25 Deepcut facility.

## Purpose

This deliverable exists because PKG-066 ("Tanks, Condendate (API 650) 4-25") is delivered by a Package Vendor under contract to the EPC Integrator. The vendor must engineer, design, and supply the physical condensate tank package using the EPC Scope of Work (DEL-066-01) and the EPC Package Datasheet (DEL-066-02) as inputs, and align with the Construction Work Package (DEL-066-03) for installation, then submit documents through DEL-066-05 for EPC acceptance under DEL-066-06.

The package's purpose in the facility is to provide approximately 4.5 days of stabilized C5+ condensate buffer storage at the 04-25 Deepcut plant against liquids-hub upsets, with the downstream disposition being transfer to the 03-25 Liquids Hub via the condensate transfer pumps. [Source: `4-25_Deepcut_DBM.md` § Condensate Product Storage]

## Principles

- **API 650, modified, atmospheric basis.** The DBM is explicit: condensate tanks are Modified API 650, atmospheric, 16 oz test pressure, 90% max fill. Vendor design must not silently upgrade to a code basis the project did not require, nor downgrade. [Source: same]
- **Cascade-by-elevation tank farm topology.** The DBM specifies two inlet tanks receiving stabilizer bottoms, with internal pipe stand cascading product to downstream tanks. This is a design intent, not a vendor option. [Source: same]
- **Tank vapours go to VRU; blanket gas prevents winter vacuum.** Storage tanks are connected to the VRU suction header (Module 930), and API 2000-based blanket gas is provided to prevent vacuum during winter when condensate vapour pressure can fall below atmospheric. [Source: `4-25_Deepcut_DBM.md` § Condensate Product Storage; § VRU Configuration and Design Parameters]
- **Pump suction-limited tank geometry.** Tank nozzle elevations interact directly with the condensate transfer pump NPSH; design NPSHR ≤ 0.75 m at design flow because tanks are not elevated. Vendor cannot independently choose nozzle locations without coordinating with pump scope. [Source: `4-25_Deepcut_DBM.md` § Product Pumps]
- **Vendor responsibility, EPC review.** Per `_CONTEXT.md`, the Package Vendor owns engineering/design/equipment; the EPC Integrator reviews for integration. The vendor should not defer integration calls to the EPC; the vendor proposes, the EPC accepts. [Source: `_CONTEXT.md` ResponsibleParty]

## Considerations

- **Sour vapour potential.** The DBM flags "tank isolation philosophy must be reviewed in the context of potential sour vapours" for produced-water tanks. By analogy, condensate stabilizer-bottoms streams at 04-25 are part of a sour service plant; vendor should not assume sweet-only nozzle and vent design without confirming H2S basis with the EPC Integrator. (Direct claim for condensate tanks is `location TBD`; the DBM only explicitly states it for produced water tanks. ASSUMPTION: same consideration applies to condensate tanks.)
- **Winter operability.** Tanks are non-insulated; recycle from a product recycle pump may be required for winter temperature maintenance. Vendor must provide a recycle return nozzle and confirm thermal/dimensional behavior of the tank shell at -40 deg C. [Source: `4-25_Deepcut_DBM.md` § Condensate Product Storage; § Product Pumps]
- **Vapour-space pressure dynamics.** The VRU suction header pressure must hold tank vapour space within EPRV/PVRV bounds; piping fitting count and length are explicitly called out as critical by the DBM. Vendor nozzle sizing and orientation should support a low-fitting tie-in to the Module 930 suction header. [Source: `4-25_Deepcut_DBM.md` § VRU Configuration / discussion]
- **Plot plan as an open project gap.** The governing plot plan drawing (CIV-235633-5002) is not in the accessible source set per the DBM. Vendor should treat plot coordinates as TBD inputs to be received from the EPC Integrator, not as self-asserted values. [Source: `4-25_Deepcut_DBM.md` § Plot plan / § Existing-Facility Interfaces and Metering]
- **Spacing constraints.** NFPA 30, OGAOM § 9.6.15, and DPR 48 spacings govern tank-to-tank and tank-to-public-road; flare-to-tank and fired-heater-to-tank distances are also fixed. Vendor general arrangement must be checked against those rules even before the plot plan is finalized. [Source: `4-25_Deepcut_DBM.md` § Atmospheric Tank and General Plant Spacing]

## Trade-offs

- **Insulation vs recycle.** The DBM chose non-insulated tanks with optional recycle, accepting recycle operation rather than insulation cost. Vendor should not silently propose insulation; if a thermal review shows insulation is necessary, surface it as a CONFLICT for EPC ruling.
- **Tank count.** DBM narrative says four tanks; package roster row 90 lists five tanks. Either total live capacity or the storage-day count changes depending on which is correct. Surfaced as CONFLICT C-01 below.
- **Common truck-out vs per-tank truck-out.** DBM specifies a common truck-out connection; this trades simpler piping for the operational constraint that truck-out cannot run simultaneously from inlet and outlet tanks without isolation valving. Vendor should confirm valving philosophy with EPC.

## Examples

The most directly analogous tank scope in the same DBM is the produced water tank package: two API-650-modified atmospheric tanks with 16 oz test pressure, 90% fill, blanket gas (API-2000 rate basis), each tank with at least one PVRV, externally insulated and heated, internally coated with Devchem 253, Kennilworth-type hydrocarbon skim float. [Source: `4-25_Deepcut_DBM.md` § Produced water tanks]

The condensate tank scope differs from the produced-water analog principally in: service fluid (stabilized C5+ condensate vs produced water), insulation (non-insulated vs externally insulated/heated), internal coating (TBD vs Devchem 253), interior fittings (internal pipe stand cascade vs hydrocarbon skim float), and operational arrangement (inlet/outlet tank cascade vs uniform tank duty). Vendor should not transplant produced-water-tank design choices into the condensate package without explicit basis.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-01 | Condensate tank count: four vs five | `4-25_Deepcut_DBM.md` § Condensate Product Storage ("four 3,800 bbl condensate product storage tanks") | `4-25_Deepcut_DBM.md` package roster row 90 (5 tanks: TK-9110-1, TK-9120-1, TK-9130-1, TK-9140-1, TK-9150-1) | Datasheet Identification / Attributes; Specification R-04; Guidance Trade-offs | PROPOSAL: Package roster (5 tanks) governs equipment count; DBM narrative paragraph may be stale relative to the equipment-tag basis. | TBD — EPC Integrator to rule and update EPC Scope of Work / Package Datasheet. |
| C-02 | H2S/sour vapour design basis for condensate tank vents and isolation | DBM § Produced water tanks explicitly calls for sour-vapour isolation review | DBM § Condensate Product Storage does not state H2S design vapour concentration for condensate tanks | Specification R-08 to R-11; Guidance Considerations | PROPOSAL: Treat condensate tank vent and isolation philosophy as sour-service until EPC Package Datasheet (DEL-066-02) confirms a numeric H2S basis. | TBD — EPC Integrator to confirm sour vapour basis. |
| C-03 | Package-heading-21 clause-level requirements not accessible in this run | `_REFERENCES.md` points to 26020-Package_Requirements.docx package heading 21 | .docx not text-readable from agent context | Specification R-08, R-17, R-23; Documentation list | PROPOSAL: Vendor and EPC Integrator confirm package-heading-21 requirements during DEL-066-02 (Package Datasheet) handoff; this Specification will be reconciled in a later pass. | TBD — EPC Integrator to publish heading-21 contents into the EPC Package Datasheet. |
