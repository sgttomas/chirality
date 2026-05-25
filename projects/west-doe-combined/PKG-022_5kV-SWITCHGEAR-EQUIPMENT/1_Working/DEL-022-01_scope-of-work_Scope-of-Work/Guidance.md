# Guidance: DEL-022-01 Scope of Work

## Purpose

This Scope of Work exists to give the EPC Integrator a bounded, source-traceable package integration basis for PKG-022 (`5kV SWITCHGEAR EQUIPMENT`) before downstream package datasheet, construction work package, vendor package production, vendor document turnover, and EPC acceptance work proceeds.

The source basis is intentionally narrow. Workbook row 24 establishes the package identity and interface flags; Gate 7 establishes the mandatory EPC anchor deliverable role and the Package Vendor / EPC Integrator responsibility split; the DBM Deepcut electrical sections describe the facility MV system at 13.8 kV (main distribution), 6.9 kV (large motor service, 5,500 hp and above), and 4.160 kV (motor service 250 hp up to 5,500 hp) with 5 kV-class insulation on the 4.16 kV cable system. The accessible Deepcut DBM does not describe a discrete 5 kV facility bus. Package-specific switchgear design details remain `TBD` unless later source material provides them.

## Principles

- Preserve the source package name `5kV SWITCHGEAR EQUIPMENT` in identity fields because it is the accepted workbook/Gate 7 spelling.
- Treat the Scope of Work as an EPC integration document, not a vendor design document.
- Keep Package Vendor responsibilities (package engineering, design, vendor documentation, equipment supply) separate from EPC Integrator responsibilities (integration, interfaces, tie-ins, constructability, procurement/construction coordination, acceptance).
- Include only source-supported package interfaces (the six listed for PKG-022).
- Use the DBM Deepcut MV electrical basis as facility context only; do not infer switchgear topology, breaker type, short-circuit rating, lineup configuration, BIL, enclosure, or footprint from it.
- Prefer `TBD` over inferred technical values where accessible sources do not provide package-specific detail.
- Do not silently reconcile the package-name "5kV" designation against the facility MV bus voltages defined in the DBM; carry it as a human ruling item.
- Do not silently link PKG-022 to PKG-037 (5kV Switchgear Electrical Building 880-1) without source confirmation; carry the relationship as a dependency context.

## Considerations

The package name reads "5kV SWITCHGEAR EQUIPMENT." The Deepcut DBM defines facility MV services at 13.8 kV, 6.9 kV, and 4.16 kV, and specifies 4.160 kV medium-voltage cables as three-conductor copper TECK cable rated 5 kV with 100 percent insulation. Industry practice commonly designates switchgear by insulation class (e.g., "5 kV class" switchgear used on a 4.16 kV system) rather than by nominal bus voltage; treat the link between the package name and the 4.16 kV facility bus as ASSUMPTION pending human ruling, and do not pre-allocate the switchgear to a specific facility bus without source confirmation.

The Gate 7 register also lists PKG-037 "5kV SWITCHGEAR ELECTRICAL BUILDING (880-1)." The PKG-022 equipment package and the PKG-037 building package may be a paired equipment/building set within the 880-1 area, but the accessible source slices for PKG-022 do not state this association. The SOW should record the contextual existence of PKG-037 and surface the relationship as a TBD rather than assert a binding allocation.

The workbook and Gate 7 interface basis flags Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. These should drive the SOW boundary narrative and later construction coordination. They should not be expanded to additional interface categories (e.g., HVAC, Fire & Gas) unless later accepted sources add them; PKG-037 (the companion building package) carries a broader interface set per Gate 7.

The DBM also defines the facility MV system as low-resistance grounded with EtherNet-to-plant-PLC communications on the MCC equipment. The Scope of Work should reference this as a facility-level integration consideration without prescribing protection settings, relay models, or network protocol details for the PKG-022 switchgear.

## Trade-offs

| Topic | Conservative treatment | Risk if overstated |
|---|---|---|
| Bus voltage alignment | Preserve the package name; note that DBM facility MV buses are 13.8 / 6.9 / 4.16 kV and that 5 kV is the cable insulation class for the 4.16 kV system; flag for human ruling. | Picking a single bus voltage could silently overwrite accepted upstream truth or contradict vendor or facility design intent. |
| Driven / served-load allocation | Reference the DBM MV motor service ranges as facility context; keep PKG-022 fed-load list `TBD`. | The SOW could pre-allocate switchgear feeders before facility integration data confirms allocation. |
| EPC responsibility | State facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and acceptance review. | EPC scope could accidentally absorb vendor switchgear design obligations. |
| Building / location association | Reference PKG-037 (5kV Switchgear Electrical Building 880-1) as contextual; do not bind PKG-022 to PKG-037 without source confirmation. | A premature equipment-to-building binding could distort PKG-037 scope and create false dependencies. |
| Standards basis | Reference IEEE/ANSI/NEMA MV switchgear standards generically; mark specific governing project specifications as TBD. | Citing clause-level requirements without source text could overstate authority. |
| Technical values | Use only source-supported values and `TBD` elsewhere. | Unsupported values could propagate into datasheets, procurement, or construction packages. |

## Examples

- Acceptable SOW language: "PKG-022 is the workbook-defined Electrical package `5kV SWITCHGEAR EQUIPMENT`, WBS 01, tracking number `26020-01-30-013`; the Package Vendor owns package engineering/design/vendor documentation/equipment and the EPC Integrator owns facility integration and interface coordination."
- Acceptable SOW language: "The Deepcut DBM defines facility MV services at 13.8 kV, 6.9 kV, and 4.16 kV with 5 kV-class insulation on 4.16 kV cables; the specific facility bus served by PKG-022 is TBD."
- Acceptable SOW language: "Bus rating, short-circuit rating, breaker type, lineup configuration, BIL, enclosure, environmental rating, weights, and footprint are TBD pending vendor/source data."
- Avoid: "The EPC Integrator shall design the 5 kV switchgear lineup." Gate 7 assigns package engineering and design to the Package Vendor.
- Avoid: "PKG-022 supplies the 4.16 kV switchgear for the 880-1 electrical building." Bus voltage allocation and the PKG-022/PKG-037 binding are not confirmed in accessible sources.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HR-022-01-01 | Package name "5kV SWITCHGEAR EQUIPMENT" does not correspond to any discrete 5 kV facility bus in the Deepcut DBM; DBM facility MV buses are 13.8 kV / 6.9 kV / 4.16 kV, with 5 kV-class insulation specified for the 4.16 kV cable system. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-022; workbook Packages row 24. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2917-2925, 2935-2936, 3009. | Datasheet Identification/Conditions, Specification Requirements SOW-022-05/07, Procedure verification steps. | Treat "5kV" as a switchgear insulation/voltage-class designation (likely applied to the 4.16 kV system) rather than as a nominal bus voltage; preserve the accepted package name as identity; do not normalize to any specific facility bus until human/vendor ruling. | TBD |
| HR-022-01-02 | Tagged equipment, served loads, and association between PKG-022 (equipment) and PKG-037 (5kV Switchgear Electrical Building 880-1) are not stated in accessible sources. | Workbook Packages row 24; Gate 7 `PACKAGE_REGISTER.csv` row PKG-022. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-037; DBM Deepcut electrical sections (no explicit allocation). | Datasheet Attributes (tagged equipment) and Conditions (companion building package), Specification SOW-022-10, Procedure Steps. | Keep tagged equipment, fed-load list, and building/location association `TBD` until source data or human ruling confirms allocation. | TBD |
| HR-022-01-03 | Project-level governing standards and specifications for MV switchgear (IEEE/ANSI/NEMA series, project specification numbers, CSA/Provincial code basis) are not directly enumerated in the accessible source slices for PKG-022. | `_REFERENCES.md` (no slice-level standard text accessible). | Workbook Packages row 24; Gate 7 PKG-022 register rows. | Datasheet References, Specification Standards, Guidance Considerations. | Reference standards generically; mark specific governing project specifications and locations as TBD; do not derive clause-level requirements. | TBD |
