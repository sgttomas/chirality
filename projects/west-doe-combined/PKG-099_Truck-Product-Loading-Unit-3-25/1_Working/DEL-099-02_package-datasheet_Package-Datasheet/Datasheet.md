# Datasheet — DEL-099-02 Package Datasheet (Truck Product Loading Unit 3-25)

Pass set: P1_P2 (drafted 2026-05-25 by TASK+four-documents)

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-099-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable Name | Package Datasheet | `_CONTEXT.md` |
| Parent Package | `PKG-099 — Truck Product Loading Unit 3-25` | `_CONTEXT.md` |
| Vendor Package Tag (source) | `26020-03-PT-23-001` | `26020-Package_Requirements.docx` Heading1 (3-25 Liquids Hub series) |
| Subject Equipment Title (source) | Condensate Truck Loading Stations | `26020-Package_Requirements.docx` Heading1 `26020-03-PT-23-001` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Package Datasheet | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Managed In (project) | 26020-03 3-25 Liquids Hub | `26020-Package_Requirements.docx` §Location/Status |
| Source Basis (RFQ) | `RFQ/Bid Docs/26020-03-PT-RFQ-23-001_Truck_Load_stn_R0.docx` | `26020-Package_Requirements.docx` §Source Basis |
| Decomposition snapshot | `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` | `_CONTEXT.md` |

ASSUMPTION (package mapping): The package title in `_CONTEXT.md` ("Truck Product Loading Unit 3-25") is mapped to source heading `26020-03-PT-23-001 — Condensate Truck Loading Stations` because (a) it is the only Truck Loading Stations heading in the 26020-03 (3-25 Liquids Hub) series and (b) the package name, scope items, and `Workbook Packages row 98` pointer all align. Human confirmation TBD.

## Attributes (Package-Level)

| Attribute | Value | Source |
|---|---|---|
| Function | Sweet Dehydrated Condensate is pumped from the Condensate Storage Tanks by the Truck Loading pumps to the Truck Loading stations, metered, and fills the atmospheric condensate trucks. | `26020-Package_Requirements.docx` §Basic Scope (heading 18198) |
| Stations supplied | 2 truck loading/unloading stations | §Basic Scope; §Major Included Equipment |
| Simultaneous truck capacity per station | 2 trucks (2x2 configuration) | §Basic Scope; §Major Included Equipment |
| Service fluid | Sweet, dehydrated condensate (atmospheric) | §Basic Scope |
| Upstream source | Condensate Storage Tanks via Truck Loading pumps | §Basic Scope |

## Major Included Equipment

| Item | Description / Spec | Source |
|---|---|---|
| Truck Loading/Unloading Stations | 2 stations, each 2x2 simultaneous loading | §Major Included Equipment |
| Basket strainer | Sureflow `0300BF300SS`, 316SS, c/w mesh screen — filters solids contaminants | §Major Included Equipment |
| Emergency Shut Down Valve (ESDV) | One per station (count TBD per source) | §Major Included Equipment |
| Flow transmitters | For metering at each loading point | §Major Included Equipment |

## Design Conditions

| Parameter | Value | Source |
|---|---|---|
| Design rate per station (loading or unloading) | 103 m³/h | §Scope Notes (heading 18202) |
| Total Condensate Truck Loading Header flow (4 lines) | 415 m³/h | §Scope Notes (heading 18202) |
| Capacity / design throughput (general) | TBD (source: "-") | §Scope Notes |
| Operating conditions | "See design conditions" (no separate listing in source) | §Scope Notes |

## Construction / Scope Boundaries

| Item | Status | Source |
|---|---|---|
| Shipping packages to site | By Others | §Scope Notes |
| Installation on piles | By Others | §Scope Notes |
| Tie-in piping | By Others | §Scope Notes |
| Electrical connections | By Others | §Scope Notes |
| Mounting platform, stairs, etc. | By Others | §Scope Notes |

## Physical Interface Summary

Interface source: `26020-Packages_Interfaces.3.xlsx` (cited in §Physical Interface Summary, row 98).

| Interface Type | Applicability | Source |
|---|---|---|
| Process Piping | Yes | §Physical Interface Summary |
| Utility Piping | No | §Physical Interface Summary |
| Relief / Flare / Vent | No | §Physical Interface Summary |
| Drain / Containment | Yes | §Physical Interface Summary |
| Electrical Power | Yes | §Physical Interface Summary |
| Area / Exterior Lighting | Yes (per `26020-Packages_Interfaces.3.xlsx` col M, row 98) | §Physical Interface Summary |
| EHT (electric heat trace) | No | §Physical Interface Summary |
| Grounding / Bonding | Yes | §Physical Interface Summary |
| Cathodic Protection | No | §Physical Interface Summary |
| I&C / Control Cabling | Yes | §Physical Interface Summary |
| Communications / Network | No | §Physical Interface Summary |
| Building HVAC / Services | No | §Physical Interface Summary |
| Fire & Gas / Safety Systems | Yes | §Physical Interface Summary |
| Maintenance Access | No | §Physical Interface Summary |
| Grading / Site Drainage / Spill Containment | Yes | §Physical Interface Summary |
| Structural / Foundations / Supports | Yes | §Physical Interface Summary |
| Product Loading | Yes | §Physical Interface Summary |
| Pipeline / Pigging | No | §Physical Interface Summary |

## References

- `_Sources/26020-Package_Requirements.docx` — Heading1 `26020-03-PT-23-001 — Condensate Truck Loading Stations` and its child subsections (Basic Scope, Major Included Equipment, Physical Interface Summary, Vendor Engineering Deliverables, Interface Coordination Notes).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — referenced from §Physical Interface Summary (row 98, column M for lighting applicability). **location TBD** (not parsed in this run).
- `RFQ/Bid Docs/26020-03-PT-RFQ-23-001_Truck_Load_stn_R0.docx` — source basis RFQ. **location TBD** (path not locally resolved; assumed to live in vendor RFQ bundle).
- `_CONTEXT.md`, `_REFERENCES.md` (deliverable-local).
- Decomposition snapshot Gate 7 (2026-05-24) — `PROJECT_DECOMP`.

## Open Items / TBDs

- TBD — ESDV quantity per station and per header (source lists "Emergency Shut Down Valve (ESDV)" without count).
- TBD — Capacity / design throughput rolled-up value (source line is "-").
- TBD — Operating conditions detail beyond "See design conditions".
- TBD — Truck loading metering accuracy class and custody-transfer status (not stated in §Basic Scope or §Major Included Equipment).
- TBD — Truck Loading Pump tag references and discharge conditions (cross-package; not in this heading).
- TBD — Interface Coordination Notes (source states only "TBD").
