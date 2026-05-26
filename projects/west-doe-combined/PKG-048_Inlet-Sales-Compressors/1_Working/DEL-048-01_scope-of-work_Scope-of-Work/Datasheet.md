# Datasheet: DEL-048-01 — Scope of Work, PKG-048 Inlet / Sales Compressors

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-048-01_scope-of-work | _CONTEXT.md |
| Deliverable Name | Scope of Work | _CONTEXT.md |
| Parent Package ID | PKG-048 | _CONTEXT.md; PACKAGE_REGISTER.csv |
| Parent Workbook ID | 48 (Workbook Packages row 65) | PACKAGE_REGISTER.csv |
| Package Name | Inlet / Sales Compressors | PACKAGE_REGISTER.csv |
| Equipment Tag / RFQ | 26020-01-PT-12-003 — Inlet / Sales Compressors | PACKAGE_REGISTER.csv |
| Discipline | Mechanical | PACKAGE_REGISTER.csv; _CONTEXT.md |
| Deliverable Type | EPC Scope of Work | _CONTEXT.md |
| Responsible Party (this deliverable) | EPC Integrator | _CONTEXT.md |
| Package Vendor Responsibility | Package engineering, package design, vendor documentation, physical equipment package | PACKAGE_REGISTER.csv (Responsibility) |
| EPC Integrator Responsibility | Integration into the functional process facility: interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration | PACKAGE_REGISTER.csv (Responsibility) |
| Host Facility | 04-25 West Doe Deep Cut Gas Plant expansion | DBM-Deepcut/4-25_Deepcut_DBM.md SEC-01, SEC-05 |
| Covers Scope Items | SOW-0115, SOW-0116, SOW-0117, SOW-0118 | _CONTEXT.md; DELIVERABLE_REGISTER.csv |
| Supports Objectives | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (ASSUMPTION: PACKAGE_HEURISTIC association) | _CONTEXT.md; DELIVERABLE_REGISTER.csv |

## Attributes

### Tagged Equipment / Package Identity

| Attribute | Value | Source |
|---|---|---|
| Equipment description | Five (5) inlet / sales gas multi-service reciprocating compressor packages | PACKAGE_REGISTER.csv (Scope); DBM-Deepcut SEC-05 |
| Configuration | Five identical parallel multi-service packages; no installed spare package | DBM-Deepcut SEC-05 "Compression Configuration" |
| Per-package services | One sour inlet gas compression stage; two sweet sales gas compression stages on a common frame | DBM-Deepcut SEC-05 "Compression Configuration" |
| Sparing basis | 5 x 20% (each sized for ~120% per-unit per workbook scope; no installed spare) | PACKAGE_REGISTER.csv (Scope: "Each compressor shall be sized for 120%"); DBM-Deepcut SEC-05 |
| Compressor frame (preliminary) | Ariel KBC/6, to be confirmed (legacy conflicting frame reference unresolved — TBD pending human ruling) | DBM-Deepcut SEC-05 "Inlet / Sales Compressor Basis" |
| Driver | 6,700 hp, 3-phase electric induction motor (conflict against 7,000 hp legacy value — TBD) | DBM-Deepcut SEC-05 |
| Motor start method | Starting VFD with synchronous transfer to normal-service bus after full speed (workbook scope row 65 states DOL with soft-start — CONFLICT, see Guidance) | DBM-Deepcut SEC-05; PACKAGE_REGISTER.csv (Scope) |

### Inlet Service Conditions (per package)

| Parameter | Value | Source |
|---|---|---|
| Compression stages | One | DBM-Deepcut SEC-05 design table |
| Per-package capacity | 62.4 MMSCFD supported basis (60 MMSCFD appears in some detailed tables — TBC) | DBM-Deepcut SEC-05 design table |
| Total inlet capacity | ~312 MMSCFD (300 MMSCFD TBC) | DBM-Deepcut SEC-05 design table |
| Suction pressure | 4,309 kPag (625 psig) service basis; 385 psig at compressor cylinder inlet | DBM-Deepcut SEC-05 design table |
| Discharge pressure | 7,791 kPag (1,130 psig) service basis | DBM-Deepcut SEC-05 design table |
| Operating inlet temperature | 27.3 deg C winter / 35.7 deg C summer; J-T mode TBD | DBM-Deepcut SEC-05 design table |
| Minimum MAWP | 9,032 kPag initial estimate (suction and discharge) | DBM-Deepcut SEC-05 design table |
| H2S content (cylinder) | ~0.296 mol% (sour) per DBM Comp&Liquids inlet compressor composition; Deep Cut inlet feed includes combined 03-25 sour gas | DBM-Comp_and_Liquids SEC-05; DBM-Deepcut SEC-05 |

### Sales Service Conditions (per package)

| Parameter | Value | Source |
|---|---|---|
| Compression stages | Two | DBM-Deepcut SEC-05 design table |
| Per-package capacity | 57.6 MMSCFD | DBM-Deepcut SEC-05 design table |
| Total sales capacity | 288 MMSCFD TBC | DBM-Deepcut SEC-05 design table |
| Suction pressure | 440 psig service basis (430 psig normal in detailed pressure table) | DBM-Deepcut SEC-05 design table |
| Discharge pressure | 10,343 kPag (1,500 psig) current supported basis; 1,700 psig second-stage detailed estimate TBC | DBM-Deepcut SEC-05 design table |
| Suction temperature | 43.3 deg C (first stage); 71.1 deg C (second stage); J-T mode TBD | DBM-Deepcut SEC-05 design table |
| Minimum MAWP | 9,032 kPag lower stages; 13,100 kPag third-stage discharge | DBM-Deepcut SEC-05 design table |

## Conditions

### Process Boundaries

| Boundary | Description | Source |
|---|---|---|
| Inlet service suction | Sour gas from inlet/TEG heat exchanger combined with West Doe sour gas from 03-25 Compressor Station | DBM-Deepcut SEC-05 |
| Inlet service discharge | To downstream amine sweetening | DBM-Deepcut SEC-05 |
| Sales service suction | Sweet sales gas from turbo expander compressor aftercooler (440 psig, 110 deg F) | DBM-Deepcut SEC-05 |
| Sales service discharge | To sales gas booster compressor suction (PKG-049) | DBM-Deepcut SEC-05; PACKAGE_REGISTER.csv (PKG-049) |

### Interface Types (EPC Integrator scope)

Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports.

Source: PACKAGE_REGISTER.csv (Applicable interface types).

## Construction

| Attribute | Value | Source |
|---|---|---|
| Package count | Five (5) parallel identical packages | PACKAGE_REGISTER.csv; DBM-Deepcut SEC-05 |
| Modularization | Modularized; transportation/installation provisions location TBD | ASSUMPTION based on DBM-Comp_and_Liquids SEC-05 inlet compression convention (location TBD for 04-25 packages) |
| Installed spare | None | DBM-Deepcut SEC-05 |
| Common air-cooler frame per package | Yes, common cooler frame serving both inlet and sales services | DBM-Deepcut SEC-05 |
| Air cooler control | Automated louver control by pneumatic temperature control | DBM-Deepcut SEC-05 |
| Suction scrubbers | Two-phase suction scrubbers upstream of each stage (sales-service necessity to be evaluated in detailed engineering) | DBM-Deepcut SEC-05 |
| Blowdown valves | One per service: inlet fails open; sales fails closed | DBM-Deepcut SEC-05 |
| Recycle valves | 100% capacity each; inlet fail position stated fail open (TBD); sales stated fail closed (TBD) | DBM-Deepcut SEC-05 |
| Start basis | Starts from equalization pressure both services; alternate depressure to inlet headers if MAWP exceeded | DBM-Deepcut SEC-05 |
| Lube oil | Each frame includes electric circulating lube oil heater for quick start | DBM-Deepcut SEC-05 |
| Sweet gas purge | Manual sweet gas purge from fuel gas for maintenance sweeping (sour inlet system) | DBM-Deepcut SEC-05 |
| Seal-pot routing | Packing drains/vents to common seal pot; vapour to VRU suction header; liquids by local truck-out | DBM-Deepcut SEC-05 |
| Clearance pockets | Automated continuously variable or fixed-volume pockets vs. standard manual variable volume pockets — selection TBD | DBM-Deepcut SEC-05 |

## References

- _CONTEXT.md (this deliverable)
- _REFERENCES.md (this deliverable)
- _DEPENDENCIES.md (this deliverable)
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv (row DEL-048-01_scope-of-work)
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv (row PKG-048)
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md (SEC-01 Scope Boundary; SEC-05 Compression and Acid Gas Handling Basis — Inlet/Sales Compressor Basis)
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (cross-reference for 03-25 sour gas feed)
- Workbook Packages row 65 (location TBD — not locally accessed as text in this run)
- 26020-Package_Requirements.docx package heading 3 (.docx not converted; location TBD)
- 26020-01-PT-RFQ-12-003-Inlet Sales Comp.docx (RFQ; location TBD — not locally accessed in this run)
