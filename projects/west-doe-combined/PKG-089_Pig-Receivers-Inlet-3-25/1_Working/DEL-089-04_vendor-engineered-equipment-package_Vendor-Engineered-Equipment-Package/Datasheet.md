# Datasheet — Vendor Engineered Equipment Package (DEL-089-04)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-089-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Name | Vendor Engineered Equipment Package | `_CONTEXT.md` |
| ParentPackageID | `PKG-089` | `_CONTEXT.md` |
| PackageName | Pig Receivers (Inlet) 3-25 | `_CONTEXT.md` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | Vendor Package Production Unit | `_CONTEXT.md` |
| ResponsibleParty | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md` |
| Tagged Equipment | PR-1010-2; PR-1020-2 (two 24" / 610 mm OD pig receivers) | SCOPE_LEDGER.csv SOW-0159 |
| Service | Sour gas pipeline pig receiving (plant inlet) | SCOPE_LEDGER.csv SOW-0158 |
| Workbook Row | Packages row 77 | `_CONTEXT.md` |
| Source Heading | 26020-Package_Requirements.docx package heading 42 | `_CONTEXT.md` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Quantity | 2 identical pig receiver assemblies | SOW-0158; SOW-0159 |
| Receiver OD | 610 mm (24 in) | SOW-0158; SOW-0159 |
| Mounting | Dedicated structural steel non-enclosed skid (one skid per receiver) | SOW-0158; SOW-0159 |
| Skid-mounted Isolation | All skid-mounted isolation or ESDV | SOW-0159 |
| ESDV Position | Installed upstream of the receiver | SOW-0159 |
| Sour Service | Design 0.1 mol% H2S (per source statement) | SOW-0159 |
| Purge | Sweet gas purge downstream of manual isolation valve for sour gas purge of receiver barrel prior to opening for pig retrieval | SOW-0159 |
| Vent | Vent line to HP flare system | SOW-0159 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Design Throughput (package) | 80 MMSCFD | SOW-0160 |
| Normal Operating Pressure | 125 psig to 200 psig | SOW-0160 |
| Maximum Allowable Operating Pressure (MAOP) | 572 psig | SOW-0160 |
| Design Pressure (low) | 125 psig | SOW-0160 |
| Design Pressure (normal high) | 200 psig | SOW-0160 |
| Maximum Allowable Working Pressure (MAWP) | 635 psig | SOW-0160 |
| Historical Ambient Temperature | -19 °C min., +22.2 °C max. | SOW-0160 |
| Ambient Design Temperature | -40 °C min., +35 °C max. | SOW-0160 |
| Normal Flowrate per Receiver | TBC (TBD) | SOW-0160 |

## Construction

| Item | Value | Source |
|---|---|---|
| Receiver Barrel | 24 in (610 mm) OD pig receiver — barrel materials, wall thickness, end-closure type | TBD (not stated in accessible sources) |
| Skid | Structural steel non-enclosed skid | SOW-0158; SOW-0159 |
| Isolation Valves | Skid-mounted isolation valves; ESDV upstream of receiver | SOW-0159 |
| Purge System | Sweet gas purge tie-in downstream of manual isolation | SOW-0159 |
| Vent Routing | Routed to HP flare header | SOW-0159 |
| Materials of Construction (sour service compatible per NACE MR0175 / ISO 15156) | ASSUMPTION: sour-service-rated materials per project sour-service philosophy (OBJ-009); specific MoC TBD by vendor design | SOW-0159; OBJ-009 |
| By Others (not vendor scope) | Interconnecting piping; DCS integration; foundations; electrical supply to MCC | SOW-0160 |

## References

- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/SCOPE_LEDGER.csv` (rows SOW-0157, SOW-0158, SOW-0159, SOW-0160)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (row DEL-089-04)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/ARTIFACT_REGISTER.csv` (artifacts ART-AFDDE0BE60, ART-6017932F95, ART-8976B99094)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/OBJECTIVE_REGISTER.csv` (OBJ-002..OBJ-010)
- Upstream EPC deliverables: DEL-089-01 (Scope of Work), DEL-089-02 (Package Datasheet) — location TBD (sibling deliverables not yet drafted)
- 26020-Package_Requirements.docx package heading 42 — location TBD (source not locally accessible as text extract)
