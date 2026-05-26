# Guidance: DEL-040-01 Scope of Work

## Purpose

This Scope of Work exists to give the EPC Integrator a bounded, source-traceable package integration basis for PKG-040, the 600V ELECTRICAL BUILDING (860-1), before downstream package datasheet, construction work package, vendor package production, vendor document turnover, and EPC acceptance work proceeds.

The source basis is intentionally narrow. Workbook row 42 establishes the package identity and the twelve interface flags. Gate 7 establishes the mandatory EPC anchor deliverable role and the Package Vendor / EPC Integrator responsibility split. The DBM Deepcut electrical design basis (Section 12) provides facility-level basis for the 600 V system, prefabricated electrical buildings, grounding, standby power, and building heaters. Package-specific interior equipment, ratings, quantities, dimensions, and loads remain `TBD` unless later source material provides them.

## Principles

- Preserve the source spelling `600V ELECTRICAL BUILDING (860-1)` in identity fields because it is the accepted workbook/Gate 7 package name.
- Treat the Scope of Work as an EPC integration document, not a vendor design document for the prefabricated electrical building.
- Keep Package Vendor responsibilities (engineering, design, vendor documentation, equipment supply) separate from EPC Integrator responsibilities (integration, interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration).
- Include all twelve source-supported package interfaces; do not silently drop or add interface categories.
- Use the DBM electrical-building basis as facility context only; do not infer package-specific equipment lineup, ratings, quantities, or vendor configurations.
- Prefer `TBD` over inferred technical values where accessible sources do not provide package-specific detail.
- Surface the DBM building-name variant in the Conflict Table rather than silently normalizing names.
- Carry the general-area / tank-farm service-area characterization as descriptive context; do not pre-allocate specific tank-farm loads to 860-1.

## Considerations

The package title `600V ELECTRICAL BUILDING (860-1)` together with the DBM facility electrical-building list (line 2816) supports describing the building as a prefabricated modular 600 V electrical building tagged 860-1 serving the general area / tank farm, located in a general purpose area, with bottom-entry cabling, n+1 HVAC, building heaters at 600 V, and 5 A continuous high-resistance grounding on the 600 V system. The DBM identifies what may be housed in such a building (600 V MCCs; 120 VAC and 125 VDC UPS systems with battery banks and distribution panels; 600 V to 208/120 V distribution transformers and panelboards; 208/120 V contactor panels; plant PLC control panels; network racks). It does not assign any specific lineup to 860-1.

The twelve interface flags on workbook row 42 — Utility Piping, Drain / Containment, Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Building HVAC / Services, Fire & Gas / Safety Systems, Maintenance Access, Grading / Site Drainage / Spill Containment, and Structural / Foundations / Supports — should drive the SOW boundary narrative and later construction coordination. They should not be expanded to additional interface categories unless later accepted sources add them.

The 860-1 building's service-area characterization as "General Area / Tank Farm" (DBM line 2816) is relevant to drain/containment, area classification, and grounding/bonding coordination but does not by itself authorize allocation of specific tank-farm electrical loads to this package; those allocations are TBD pending detailed engineering.

DBM-identified TBDs that directly affect this building include standby generator integration (sizing, count, connection, transfer switch, paralleling, load-shedding), RDC quantity and locations, and field-routed secondary cable tray. The SOW should carry these as visible TBDs rather than resolving them locally.

## Trade-offs

| Topic | Conservative treatment | Risk if overstated |
|---|---|---|
| Package function | Describe as a prefabricated 600 V electrical building (tag 860-1) supporting facility low-voltage distribution and control infrastructure in the general area / tank farm; mark interior lineup `TBD`. | The SOW could pre-allocate equipment, ratings, or vendor scope before vendor and detailed-engineering data are available. |
| EPC responsibility | State facility integration, twelve interface categories, tie-ins, constructability, procurement/construction coordination, and acceptance review. | EPC scope could absorb vendor package engineering and design obligations. |
| Building-name reconciliation | Carry the workbook/Gate 7 name `600V ELECTRICAL BUILDING (860-1)` as identity and surface the DBM variant as a human-ruling item. | Silently normalizing either name could break register traceability or appear to alter accepted upstream truth. |
| Service-area characterization | Note the DBM-identified general-area / tank-farm role descriptively; mark specific tank-farm load allocation `TBD`. | Pre-allocating tank-farm loads to PKG-040 could conflict with future detailed engineering. |
| Technical values | Use only source-supported values and `TBD` elsewhere. | Unsupported values could propagate into datasheets, procurement, or construction packages. |
| Standby power scope split | Mention TOU low-voltage standby generator basis as facility context; mark the package-specific connection scope `TBD`. | Premature allocation of standby generator scope to PKG-040 could conflict with future DBM resolution. |
| Area classification | Treat area classification at the 860-1 location as TBD until detailed engineering establishes hazardous-area zoning around the tank farm. | Implicit area-classification assumptions could under- or over-specify F&G and electrical-equipment ratings. |

## Examples

- Acceptable SOW language: "PKG-040 is the workbook-defined Electrical package `600V ELECTRICAL BUILDING (860-1)`, WBS 01, tracking number `26020-01-30-031`, identified in the DBM electrical-building list as the 860-1 General Area / Tank Farm electrical building; the Package Vendor owns package engineering/design/equipment and the EPC Integrator owns facility integration and interface coordination across the twelve flagged interface categories."
- Acceptable SOW language: "Interior equipment lineup, ratings, foundation loads, HVAC unit count, area classification at the 860-1 location, and standby generator integration details are TBD pending vendor data and detailed engineering."
- Avoid: "The EPC Integrator shall design the 600 V MCC lineup." Gate 7 assigns package engineering and design to the Package Vendor.
- Avoid: "Building 860-1 shall serve loads X, Y, Z in the tank farm." No accessible source slice supports those package-specific load allocations.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HR-040-01 | The package name in the workbook/Gate 7 is `600V ELECTRICAL BUILDING (860-1)`, while the DBM facility electrical-building list (line 2816) names building 860-1 as `860-1 600V General Area / Tank Farm Electrical Building`. | Workbook Packages row 42 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-040. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2816. | Identity fields across all four documents; package function narrative. | Preserve accepted workbook/Gate 7 package name for traceability; treat the DBM name as descriptive context; defer authoritative reconciliation to a human ruling. | TBD |
| HR-040-02 | Package-specific interior equipment, ratings, quantities, dimensions, foundation loads, and HVAC unit details are not exposed in accessible sources. | Workbook row 42 gives identity and twelve interface flags only. | DBM Electrical Buildings (lines 2971-2981) describes facility-level possible contents and basis, not 860-1 specific lineup. | Datasheet Conditions, Specification Requirements, Procedure Steps. | Treat DBM as facility context and keep package-specific technical values as `TBD` pending vendor and detailed-engineering data. | TBD |
| HR-040-03 | Standby generator integration for this 600 V building is dependent on facility-wide standby power coordination still listed as TBD by the DBM. | DBM line 2943 establishes TOU low-voltage standby generators at 600 V MCCs with transfer switches. | DBM line 3086 lists standby generator integration (sizing, count, connection, transfer switch, paralleling, load-shedding) as TBD. | Datasheet Conditions; Specification Requirements SOW-040-05/06; Procedure Steps. | State the facility basis and mark package-specific allocation `TBD` until DBM Assumptions/TBDs are resolved. | TBD |
| HR-040-04 | Specific tank-farm loads served by 860-1 and the area classification at the 860-1 building location are not exposed in accessible sources. | DBM line 2816 names 860-1 as the General Area / Tank Farm electrical building. | Workbook row 42 and Gate 7 PKG-040 row do not enumerate served loads or area classification. | Datasheet Conditions; Specification Requirements SOW-040-06/11; Procedure Steps. | Carry the general-area / tank-farm characterization descriptively; mark served loads and area classification `TBD` until detailed engineering resolves them. | TBD |
