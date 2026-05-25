# Guidance: DEL-038-01 Scope of Work

## Purpose

This Scope of Work exists to give the EPC Integrator a bounded, source-traceable package integration basis for PKG-038, the workbook-defined Electrical package `600V ELECTRICAL BUILDING (820-1)`, before downstream package datasheet, construction work package, vendor package production, vendor document turnover, and EPC acceptance work proceeds.

The source basis is intentionally narrow. Workbook row 40 establishes the package identity and twelve interface flags. Gate 7 establishes the mandatory EPC anchor deliverable role and the Package Vendor / EPC Integrator responsibility split. The DBM Deepcut electrical design basis provides facility-level basis for low-voltage services, prefabricated electrical buildings, grounding, standby power, cable entry, and electrical-building services. Package-specific interior equipment, ratings, quantities, dimensions, loads, and the apparent building-number mismatch remain `TBD` unless later accepted source material resolves them.

## Principles

- Preserve the source spelling `600V ELECTRICAL BUILDING (820-1)` in identity fields because it is the accepted workbook and Gate 7 package name.
- Treat the Scope of Work as an EPC integration document, not a vendor design document for the prefabricated electrical building.
- Keep Package Vendor responsibilities (package engineering, design, vendor documentation, and physical equipment supply) separate from EPC Integrator responsibilities (facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration).
- Include all twelve source-supported package interfaces; do not silently drop or add interface categories.
- Use the DBM electrical-building basis as facility context only; do not infer package-specific equipment lineup, ratings, quantities, or vendor configurations.
- Prefer `TBD` over inferred technical values where accessible sources do not provide package-specific detail.
- Surface the workbook/Gate 7 name versus DBM building-list discrepancy in the Conflict Table rather than choosing one variant silently.

## Considerations

The accepted package title is `600V ELECTRICAL BUILDING (820-1)`, but the DBM Deepcut electrical-building list identifies `820-1` as the 6.9 kV Inlet / Sales Compressor Electrical Building and lists the 600 V electrical buildings as 840-1, 850-1, and 860-1. The SOW should therefore preserve the accepted upstream package name for traceability while flagging the building-number allocation as a human ruling item.

The DBM supports describing the facility electrical-building basis as prefabricated modular buildings in general purpose areas, with potential contents such as 600 V MCCs, UPS systems, distribution transformers, panelboards, contactor panels, PLC panels, and network racks. It also supports n+1 HVAC, bottom-entry incoming and outgoing power cables, pile-supported elevation, TECK and ACIC wiring, EMT for adjacent equipment, outdoor GFI receptacles, removable transoms or doors sized for equipment removal, 600 V high-resistance grounding, and 600 V MCC ground/resistor fault detection. These are facility-level conditions for SOW integration context, not package-specific equipment assignments.

The twelve interface flags on workbook row 40 - Utility Piping, Drain / Containment, Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Building HVAC / Services, Fire & Gas / Safety Systems, Maintenance Access, Grading / Site Drainage / Spill Containment, and Structural / Foundations / Supports - should drive the SOW boundary narrative and later construction coordination. They should not be expanded to additional interface categories unless later accepted sources add them.

## Trade-offs

| Topic | Conservative treatment | Risk if overstated |
|---|---|---|
| Package identity | Preserve `600V ELECTRICAL BUILDING (820-1)` as the workbook/Gate 7 identity and carry DBM building-list mismatch as a human ruling item. | Silent renaming could break accepted register traceability or hide an upstream source conflict. |
| Package function | Describe as a vendor-owned electrical-building package requiring EPC facility integration; mark site-number allocation and interior lineup `TBD`. | The SOW could pre-allocate equipment, ratings, or vendor scope before vendor and detailed-engineering data are available. |
| EPC responsibility | State facility integration, twelve interface categories, tie-ins, constructability, procurement/construction coordination, and acceptance support. | EPC scope could absorb vendor package engineering and design obligations. |
| Technical values | Use only source-supported values and `TBD` elsewhere. | Unsupported values could propagate into datasheets, procurement, construction packages, or acceptance criteria. |
| Standby power scope split | Mention TOU low-voltage standby generator basis as facility context; mark package-specific allocation `TBD`. | Premature allocation of standby generator scope to PKG-038 could conflict with future DBM or vendor resolution. |

## Examples

- Acceptable SOW language: "PKG-038 is the workbook-defined Electrical package `600V ELECTRICAL BUILDING (820-1)`, WBS 01, tracking number `26020-01-30-029`; the Package Vendor owns package engineering/design/equipment and the EPC Integrator owns facility integration and interface coordination across the twelve flagged interface categories."
- Acceptable SOW language: "The DBM electrical-building basis applies as facility context; interior equipment lineup, ratings, foundation loads, HVAC unit count, standby-generator allocation, and final building-number reconciliation are TBD pending accepted source resolution."
- Avoid: "The EPC Integrator shall design the 600 V MCC lineup." Gate 7 assigns package engineering and design to the Package Vendor.
- Avoid: "Building 820-1 is definitively the 600 V Inlet / Sales Compressor Electrical Building." The accessible DBM list identifies 820-1 as a 6.9 kV building and lists 600 V buildings separately.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HR-038-01-01 | The workbook/Gate 7 package name is `600V ELECTRICAL BUILDING (820-1)`, while the DBM building list names 820-1 as `6.9kV Inlet / Sales Compressor Electrical Building` and lists 600 V electrical buildings as 840-1, 850-1, and 860-1. | Workbook Packages row 40 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-038. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2812, 2814-2816, and 2921-2925. | Identity fields across all four documents; package function narrative; downstream package datasheet and construction work package. | Preserve accepted workbook/Gate 7 package name for traceability; treat DBM building list as a source conflict; defer authoritative reconciliation to a human ruling. | TBD |
| HR-038-01-02 | Package-specific interior equipment, ratings, quantities, dimensions, foundation loads, and HVAC unit details are not exposed in accessible sources. | Workbook row 40 gives identity and twelve interface flags only. | DBM electrical-building basis describes facility-level possible contents and basis, not a PKG-038-specific lineup. | Datasheet Conditions, Specification Requirements, Procedure Steps. | Treat DBM as facility context and keep package-specific technical values as `TBD` pending vendor and detailed-engineering data. | TBD |
| HR-038-01-03 | Standby generator integration for this electrical building is dependent on facility-wide standby power coordination and does not assign package-specific generator/transfer-switch scope to PKG-038. | DBM line 2943 establishes TOU low-voltage standby generators at 600 V MCCs with transfer switches. | Accessible PKG-038 package sources do not assign generator count, LV switchgear assignment, transfer-switch configuration, fuel selection, or battery/charger sizing. | Datasheet Conditions; Specification Requirements SOW-038-08; Procedure Steps. | State the facility standby-power basis and mark PKG-038-specific allocation `TBD` until detailed design or vendor data resolves it. | TBD |
