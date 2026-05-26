# Guidance — DEL-066-02 Package Datasheet (PKG-066 Tanks, Condensate (API 650) 4-25)

## Purpose

The Package Datasheet exists to give the third-party vendor or discipline package engineer a single, source-supported technical handoff: it answers "what equipment, in what service, under what conditions, with which code basis and which interfaces" for PKG-066 (`_CONTEXT.md`). It is a Gate 5 mandatory EPC anchor deliverable; interface facts are carried here as evidence rather than separated into standalone deliverables (`_CONTEXT.md` Notes).

## Principles

- Source authority over convention. Where a project DBM source explicitly states an attribute (tank quantity, size, coating, spacing), that value is used. Where the source is silent or inaccessible, `TBD` is used rather than a default.
- One package, one datasheet. All package equipment, interfaces, and design criteria are consolidated here so the downstream vendor has a single technical handoff.
- Code-driven design. API 650 governs the tank fabrication. NFPA 30, API 2510, and BC OGAOM/DPR 48 govern atmospheric tank spacing and locator constraints (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-03).
- Conservative carry-over. Where the produced-water-tank "API-650 Modified + external insulation/heating + Devchem 253" design from the 03-25 Liquids Hub (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`) is plausibly applicable to sour condensate service, it is recorded as an ASSUMPTION until the vendor datasheet confirms.

## Considerations

- Cold-climate service. Stabilizer-bottoms condensate at expected < 650 kg/m3 at 15 deg C, with winter density references near 641-670 kg/m3 (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` C5+ Condensate). External insulation and heating likely required to avoid wax/precipitation issues; basis carries from produced-water analog.
- Sour service. The package is in sour-condensate service; materials and coating must accommodate H2S and mercaptans. Devchem 253 internal coating is the produced-water analog basis; condensate-service coating may differ — vendor confirmation required.
- Spacing constraints are governing. The 50 m flare distance, 80 m public-road distance, and 30.5 m unstable-liquid property-line distance can dominate plot plan layout. These are not negotiable without code/regulator concession.
- Vapour recovery interlocked. All tank vents tie to VRU, post-SCA-002 routed to the 04-25 SOC suction (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Vapour Recovery). Tank breathing/relief design must align.
- Package locator vs. equipment locator. The PKG-066 package name reads "Tanks, Condensate (API 650) 4-25" implying 04-25 location. However, the 04-25 DBM SEC-04 storage summary lists only produced-water and slop tanks at 04-25; stabilized C5+ condensate is stored at 03-25. This is a CONFLICT — see Conflict Table below.

## Trade-offs

- Single shared sour C5+ tank group at 03-25 vs. dedicated 04-25 condensate tanks: the current DBM uses a shared 6 x 3,800 bbl sour C5+ tank group at 03-25 (1.0-day storage at 7,900 bbl/d). A dedicated 04-25 inventory would shorten the export interface but duplicate equipment and reopen the 03-25 supersession basis (cf. SCA-001 / SCA-002, `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Current Supersession Controls). Current basis favors the shared 03-25 group.
- API 650 baseline vs. API 650 Modified (external insulation/heating + internal coating): the modified spec adds cost but is required for cold-climate sour service. The produced-water tanks use the modified basis; carry-over to condensate is ASSUMPTION pending vendor confirmation.

## Examples

- Atmospheric tank spacing example (per 04-25 DBM SEC-03): for two atmospheric condensate tanks adjacent to a flare and a public road, layout must satisfy 50 m to flare, 80 m to road, and 2.35 m tank-to-tank simultaneously.
- Material analog example: produced-water tanks use Devchem 253 internal coating (3-25 DBM Produced-Water section). A condensate vendor may propose an alternate coating system suited to hydrocarbon service; this is acceptable provided the vendor demonstrates compatibility with sour C5+ service.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted Sections | Proposed Authority (PROPOSAL) | Human Ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-066-02-01 | Package name "Tanks, Condensate (API 650) 4-25" implies condensate tanks at 04-25, but the 04-25 DBM SEC-04 Product Storage Summary lists only produced-water and slop tanks at 04-25; stabilized C5+ condensate is stored at the 03-25 Liquids Hub. | `_CONTEXT.md` (package name `Tanks, Condendate (API 650) 4-25`) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-04 Product Storage and Distribution Summary (lines 488-498) | Datasheet Attributes; Specification REQ scope; Guidance Considerations; Procedure Prerequisites | PROPOSAL: PKG-066 covers the project condensate-tank scope physically located at 03-25 Liquids Hub but commercially packaged under the 04-25 EPC scope; alternatively PKG-066 covers the 04-25 produced-water + slop atmospheric tanks and the package name "Condensate" is mistaken. Human ruling needed to fix scope. | TBD |
| CONF-066-02-02 | Coating/MOC basis for sour C5+ condensate tanks is not stated in accessible DBM sources; produced-water analog uses Devchem 253. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Produced-Water section | (no positive condensate-tank coating statement in accessible sources) | Datasheet Construction; Specification REQ-066-02-02 | PROPOSAL: carry produced-water analog as ASSUMPTION; require vendor to confirm or propose alternative. | TBD |
| CONF-066-02-03 | Package-heading-21 detail in `26020-Package_Requirements.docx` is the named authoritative source per `_REFERENCES.md` and the decomposition row, but is not locally accessible in readable form. | `_REFERENCES.md`; decomposition row (`Source Reference` for DEL-066-02) | (file not locally readable in markdown form) | All four documents | PROPOSAL: convert package-heading-21-only content to TBD with explicit "source not accessible" marker; resolve before vendor handoff. | TBD |
| CONF-066-02-04 | Source folder name uses "Condendate" (typo) while the standard term is "Condensate". | `_CONTEXT.md` PackageName field | Standard project terminology | All four documents | PROPOSAL: documents use "Condensate"; preserve "Condendate" only where quoting the registered folder/package name. | TBD |
