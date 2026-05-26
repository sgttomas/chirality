# Guidance — DEL-063-02 Package Datasheet (PKG-063 Tanks, DSO (API 650))

## Purpose

The Package Datasheet is the mandatory Gate-5 EPC anchor deliverable that consolidates the technical handoff from the EPC Integrator to the third-party package vendor responsible for engineering, design, fabrication, and supply of the PKG-063 DSO storage tank. It binds the package's tagged identity, design basis, mechanical attributes, and interface requirements into a single source-anchored document set so that the vendor can produce a stamped design and so that subsequent vendor-package review, construction work package, and acceptance deliverables consume a consistent technical truth (PACKAGE_REGISTER.csv PKG-063; DELIVERABLE_REGISTER.csv DEL-063-02 — `Notes`).

## Principles

- **Source primacy.** Every datasheet value should trace to a workbook row, Word source-basis heading, or DBM section. Values not so traceable are explicit `TBD` or `ASSUMPTION`, never silently asserted (K-PROV-1).
- **Single tank, single package.** PKG-063 is a single-equipment package (one 400 bbl DSO storage tank). The datasheet describes that one tank in full rather than family-level options. Source: DBM-Deepcut/4-25_Deepcut_DBM.md ("Disulphide oil storage — 1 x 400 bbl tank").
- **Modified API 650.** "Modified" is honored because the source explicitly says so (ARTIFACT_REGISTER.csv ART-966875EFC3). The specific modifications are not enumerated in accessible sources and are carried as `TBD` rather than guessed.
- **Interface facts as evidence, not deliverables.** The nine declared interfaces are recorded as datasheet evidence (per `_CONTEXT.md` Notes) rather than spun out as separate deliverables. The datasheet is the single place where interface scope is presented to the vendor.
- **Vendor/EPC boundary is non-negotiable.** The vendor owns package engineering, design, vendor documentation, and the physical package; the EPC Integrator owns facility-level integration. Datasheet language should not assign vendor responsibility for items inside the EPC scope (foundations, cathodic protection installation, grounding pads, area lighting, grading/drainage) and vice versa (PACKAGE_REGISTER.csv PKG-063).

## Considerations

- **Pour point unknowns drive insulation and heater sizing.** REQ-063-02-15 is `TBD`. Until the minimum design temperature is fixed, vendor heater calculations and insulation thickness cannot be verified. Resolve this before issuing the datasheet for fabrication-grade vendor design (DBM-Deepcut/4-25_Deepcut_DBM.md).
- **Off-gas routing crosses package boundaries.** The DSO off-gas leaves PKG-063 and feeds the incinerator at the 3-25 facility through a shared header (DBM-Deepcut/4-25_Deepcut_DBM.md). The flame-arrestor location, header line size, and pressure profile must be coordinated with the incinerator package; this is an EPC integration item, not a vendor-only datasheet item.
- **Specific gravity 1.75 is TBC.** The 1.75 design SG drives both tank-shell and foundation loading. Confirming this value early reduces rework risk across REQ-063-02-08 and the Structural / Foundations interface (IFC-DFD52CFB01).
- **Alternate DSO disposal (mixing into C5+ product) is out of base scope.** It is explicitly a detailed-engineering review item (DBM-Deepcut/4-25_Deepcut_DBM.md). Do not embed C5+ pumping into the vendor's base mechanical scope; flag it as a future-revision placeholder if at all.
- **Standards listed without locally accessible text are not authority.** API 650 modifications and the RFQ R0 document are referenced but not extracted; do not derive specific clause-level requirements from titles alone.

## Trade-offs

- **Heater sizing vs. operating cost:** Maintaining ≥ 32.2 °C (90 °F) is the explicit source basis (ARTIFACT_REGISTER.csv ART-966875EFC3). A higher maintained temperature would reduce viscosity for truck-out but raise duty; a lower setpoint risks pour-point excursions. The 32.2 °C basis should not be reduced without source change.
- **Internal coating system selection:** A coating selected for compatibility with disulphide-oil chemistry trades initial cost for long-term integrity; without an accessible coating spec, the trade-off cannot be resolved here (REQ-063-02-12).
- **Cathodic protection scope split:** Buried steel and tank bottom CP coupons are EPC integration items; package vendor's responsibility is limited to providing bonding lugs and corrosion-allowance basis. Pulling CP into vendor scope would shift integration risk inappropriately (PACKAGE_REGISTER.csv PKG-063 responsibility line).

## Examples

- Major-equipment line item for the Datasheet "Identification / Attributes" block — verbatim source slice:

  > "Item No. DSO Storage Tank: Design & fabrication to modified API 650, 400 bbl, nominal capacity. Atmospheric pressure tank. Design pressure: 32 Oz, 1.0 Oz Vacuum. c/w heater at 32.2 °C (90 °F) minimum. Vendor to design heater. Internally coated (floor, walls, roof). Insulated to maintain DSO above pour point for truck-out and handling. Minimum temperature TBD."
  > — ARTIFACT_REGISTER.csv ART-966875EFC3 / 26020-Package_Requirements.docx heading 18, Major Included Equipment.

- Off-gas / blanket gas / flame arrestor statement for the Datasheet "Construction / Safety" block — verbatim source slice:

  > "The DSO storage tank is atmospheric, heated, insulated, truck-out capable, connected to the incinerator header, protected against backflash with a flame arrestor, and blanketed with low-pressure fuel gas. DSO tank design specific gravity is 1.75 TBC."
  > — DBM-Deepcut/4-25_Deepcut_DBM.md §"Disulphide Oil, Spent Caustic, and Waste Amine".

## Conflict Table (for human ruling)

No source-level conflicts were detected during Pass 2 between accessible sources (PACKAGE_REGISTER.csv, ARTIFACT_REGISTER.csv, INTERFACE_REGISTER.csv, DBM-Deepcut). The workbook row, artifact-register rows, and DBM passage are mutually consistent on the major equipment basis.

| Conflict ID | Conflict | Source A | Source B | Impacted Sections | Proposed Authority | Human Ruling |
|---|---|---|---|---|---|---|
| (none) | — | — | — | — | — | TBD |
