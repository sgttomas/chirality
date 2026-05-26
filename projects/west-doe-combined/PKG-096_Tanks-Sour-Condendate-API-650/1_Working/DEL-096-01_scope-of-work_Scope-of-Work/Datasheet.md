# Datasheet — DEL-096-01 Scope of Work (PKG-096 Tanks, Sour Condendate (API 650))

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-096-01_scope-of-work |
| Deliverable Name | Scope of Work |
| Parent Package ID | PKG-096 |
| Parent Workbook ID | 96 |
| Package Name | Tanks, Sour Condendate (API 650) |
| Source Package Tag | 26020-03-PT-19-005 (Tanks, Sour Condensate) |
| Discipline | Mechanical |
| Type | EPC Scope of Work |
| Responsible Party | EPC Integrator |
| Facility / Location | 3-25 West Doe Liquids Hub tank farm |
| Decomposition Reference | GATE-07_Final_Published_2026-05-24 |
| Covers Scope Items | SOW-0217; SOW-0218; SOW-0219; SOW-0220 |
| Supports Objectives | OBJ-002; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 |

## Attributes

### Tagged Equipment (Major)

| Tag | Description | Quantity | Capacity |
|---|---|---|---|
| TK-9110-2 | Sour Inlet Condensate Storage Tank | 1 | 3800 bbl |
| TK-9120-2 | Sour Inlet Condensate Storage Tank | 1 | 3800 bbl |

Source: `26020-Package_Requirements.docx` package heading "26020-03-PT-19-005 - Tanks, Sour Condensate", Basic Scope / Major Included Equipment.

### Package Function

Sour C5+ Condensate Storage Tanks supporting the 03-25 West Doe Liquids Hub tank farm. Source: same as above, Basic Scope line.

## Conditions

| Parameter | Value | Notes / Source |
|---|---|---|
| Service | Sour service (H2S present); NACE compliant | Major Included Equipment |
| Operating Pressure | Atmospheric | Scope Notes / Open Items |
| Operating Temperature | TBD (not stated for Item No. 1 — "Ambient") | Scope Notes / Open Items — ASSUMPTION: ambient site conditions |
| Design Pressure | 32 oz test pressure | Scope Notes / Open Items |
| Design Temperature | -40 °C (min) / 60 °C (max) | Scope Notes / Open Items |
| Design Flow (Item No. 1) | 27,606 kg/h / 919 Am3/d | Scope Notes / Open Items |
| Fill Limit | Maximum fill 90% shutdown | Major Included Equipment |
| Fill Rate | Tank nozzles sized so plant design capacity can fill a single tank | Major Included Equipment |

Note: The source row "Design Flow: 94,940 kg/h / 3187 Am3/d for Item No. 2" and "Temperature: 5 °C (min) & 40 °C (max) for Item No. 2" appears in SOW-0220 but the Sour Condensate package basic scope only enumerates Item No. 1. CONFLICT recorded in `Guidance.md` Conflict Table.

## Construction

| Element | Requirement | Source |
|---|---|---|
| Design & Fabrication Code | Modified API 650 | Major Included Equipment |
| Blanket Gas / Pressure Protection | Blanket gas system per API 2000 | Major Included Equipment |
| Insulation | Non-insulated | Major Included Equipment |
| Sour Service | NACE compliant | Major Included Equipment |
| Internal Coating | Devchem 253 on floors, walls, roofs | Major Included Equipment |
| Pressure / Vacuum Relief | PVRV (vacuum or modulating pressure relief) per tank | Major Included Equipment |
| Emergency Relief | EPRV (emergency relief) per tank | Major Included Equipment |
| Vapour Recovery | VRU header connection per tank | Major Included Equipment |

## Interface Applicability (from Physical Interface Summary)

| Interface | Applicability |
|---|---|
| Process Piping | Yes |
| Utility Piping | No |
| Relief / Flare / Vent | Yes |
| Drain / Containment | Yes |
| Electrical Power | No |
| Area / Exterior Lighting | Yes |
| EHT | No |
| Grounding / Bonding | Yes |
| Cathodic Protection | Yes |
| I&C / Control Cabling | Yes |
| Communications / Network | No |
| Building HVAC / Services | No |
| Fire & Gas / Safety Systems | No |
| Maintenance Access | No |
| Grading / Site Drainage / Spill Containment | Yes |
| Structural / Foundations / Supports | Yes |
| Product Loading | No |
| Pipeline / Pigging | No |

Source: `26020-Package_Requirements.docx` package heading "26020-03-PT-19-005 - Tanks, Sour Condensate", Physical Interface Summary. Interface source row: `26020-Packages_Interfaces.3.xlsx` (per package text).

## Responsibility Assignment (Summary)

| Role | Scope |
|---|---|
| EPC Integrator | Authoring this Scope of Work; package boundary definition; whole-facility integration; foundations, mounting, electrical/instrumentation, platforms, staircases (declared "By others" relative to vendor package — SOW-0220) |
| Package Vendor | Engineering, design, fabrication/supply of tanks per Modified API 650 (per OBJ-004) |

## References

- `_Sources/26020-Package_Requirements.docx` — package heading 48 ("26020-03-PT-19-005 - Tanks, Sour Condensate")
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — workbook Packages row 92; Interfaces row 92
- Bid Docs/Budgetary/26020-03-PT-RFQ-19-005 - Sour Conde Tanks.docx (Source Basis cited by package text; not locally accessible — location TBD)
- Decomposition: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
