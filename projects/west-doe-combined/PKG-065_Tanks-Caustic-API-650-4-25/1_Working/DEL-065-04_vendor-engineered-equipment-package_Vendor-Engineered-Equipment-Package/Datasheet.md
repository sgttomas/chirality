# Datasheet — DEL-065-04 Vendor Engineered Equipment Package

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-065-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Deliverable Name | Vendor Engineered Equipment Package | `_CONTEXT.md` |
| Parent Package | `PKG-065` — Tanks, Caustic (API 650) 4-25 | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 87 |
| Workbook Row / Workbook ID | Workbook Packages row 87; Workbook ID 65 | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` row 87 |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable Type | Vendor Package Production Unit | `_CONTEXT.md` |
| Responsible Party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| CoA / Tracking Number | `26020-01-19-003` | `PACKAGE_REGISTER.csv` row 87 |
| Package Vendor Reference | `26020-01-PT-19-003 - Tanks, Caustic` | `PACKAGE_REGISTER.csv` row 87 |

## Attributes (Equipment Identity)

Item-level identity is taken from `26020-Package_Requirements.docx package heading 20 — Major included equipment`, as carried in `SCOPE_LEDGER.csv` (SOW-0199) and `ARTIFACT_REGISTER.csv` (ART-C0D02DC228, ART-ADA4B7EA85), corroborated by `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Disulphide Oil, Spent Caustic, and Waste Amine; and Mercaptan Treating Unit tables).

| Tag / Item | Service | Quantity | Source |
|---|---|---|---|
| TK-6780-1 | Spent Caustic Storage Tank — receives spent caustic from the pressurized caustic drain drum via level control | 1 | `26020-Package_Requirements.docx` pkg heading 20 — Major included equipment; SOW-0199 |
| Item No. 2 — Fresh Caustic Tank | Stores and supplies fresh caustic solution to the caustic treatment unit | 1 | `26020-Package_Requirements.docx` pkg heading 20 — Basic scope; SOW-0198. Tag number TBD (not in source slice) |
| Heater (on TK-6780-1) | Maintain ≥ 32.2 °C (90 °F); Vendor to design the heater | 1 (per tank, item 1) | `26020-Package_Requirements.docx` pkg heading 20 — Major included equipment; SOW-0199 |

## Conditions (Design and Operating)

Values are quoted from the package-requirements source slice (`SOW-0199`, `SOW-0200`). Items not present in the source are marked `TBD` (do not invent).

| Parameter | Item 1 — Spent Caustic Tank (TK-6780-1) | Item 2 — Fresh Caustic Tank | Source |
|---|---|---|---|
| Service classification | Atmospheric pressure tank | Atmospheric pressure tank | SOW-0199; SOW-0200 |
| Nominal capacity | 400 bbl | 400 bbl | SOW-0199; SOW-0200 |
| Design pressure | 32 oz (gauge); 1.0 oz vacuum | TBD — not in source slice (ASSUMPTION: likely identical, not confirmed) | SOW-0199 |
| Design temperature — minimum | Minimum ambient temperature (site-specific value TBD) | Minimum ambient temperature (site-specific value TBD) | SOW-0200 |
| Minimum process temperature (heater setpoint) | ≥ 32.2 °C (90 °F) — vendor to design heater | TBD | SOW-0199 |
| Flow rate (in/out) | TBD | TBD | SOW-0200 |
| Capacity/design throughput | TBC (to be confirmed) | TBC | SOW-0200 |
| Fluid — spent caustic composition | Sourced from pressurized caustic drain drum V-6940-1; circulating caustic basis ~14.7 wt% NaOH (to be confirmed) | Fresh caustic 50 wt% NaOH | DBM-Deepcut §Mercaptan Treating Unit; DBM table "Circulating process caustic concentration / Fresh caustic concentration" |
| Operating conditions narrative | Not stated in source slice | Not stated in source slice | SOW-0200 ("Operating conditions: -") |

## Construction

| Attribute | Value | Source |
|---|---|---|
| Code of construction | "Design & fabrication to modified API 650" (modifications not enumerated in source slice) | SOW-0199; `26020-Package_Requirements.docx` pkg heading 20 |
| Tank orientation / geometry | TBD (not stated in source slice) | — |
| Material of construction | TBD (not stated in source slice; ASSUMPTION: caustic-compatible carbon steel per typical industry practice — vendor to confirm and propose) | — |
| Internal lining / coating | TBD | — |
| External coating | TBD | — |
| Insulation / heat tracing | Heater required on TK-6780-1 to maintain ≥ 32.2 °C (90 °F); insulation/heat-tracing details TBD | SOW-0199 |
| Nozzles / vent / overflow | TBD (vendor to specify per modified API 650) | — |
| Foundations / mounting | By Others (EPC Integrator) — explicitly out of vendor scope | SOW-0200 ("By others: Foundations, mounting tanks at site, electrical/instrumentation, platforms, staircase etc.") |
| Platforms, staircase | By Others | SOW-0200 |
| Electrical / instrumentation | By Others (interface only) | SOW-0200; PACKAGE_REGISTER.csv applicable interface types |

## Interfaces (Battery Limits)

The following interface types apply to PKG-065 per `PACKAGE_REGISTER.csv` row 87 and `INTERFACE_REGISTER.csv` rows 754-… (carried as Interface Fact Evidence on DEL-065-02). Vendor-engineered equipment must be designed compatible with each interface; integration is owned by EPC Integrator.

- Process Piping — `IFC-746AF098A2`
- Relief / Flare / Vent — `IFC-68999FB972`
- Drain / Containment — `IFC-C6DBF5EC2F`
- Grounding / Bonding — `IFC-46B5B20CA6`
- Area / Exterior Lighting — `IFC-CB4A32B74F`
- Cathodic Protection — `IFC-3611C9BD9E`
- I&C / Control Cabling — `IFC-1A43B79AA8`
- Grading / Site Drainage / Spill Containment — `IFC-D33D2B89D5`
- Structural / Foundations / Supports — `IFC-C60E3E079C`

## References

- `_CONTEXT.md` (deliverable identity, scope, anticipated artifacts)
- `_REFERENCES.md` (authoritative decomposition basis)
- `SCOPE_LEDGER.csv` SOW-0197 / 0198 / 0199 / 0200 (Gate 7 snapshot)
- `PACKAGE_REGISTER.csv` row 87 (PKG-065)
- `ARTIFACT_REGISTER.csv` rows 6086-6088 (DEL-065-04 artifacts)
- `INTERFACE_REGISTER.csv` PKG-065 interface rows
- Workbook Packages row 87
- `26020-Package_Requirements.docx` package heading 20 (consumed via SCOPE_LEDGER/ARTIFACT_REGISTER extraction; binary source not directly opened in this run — `location TBD` for line/clause)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Disulphide Oil/Spent Caustic; Mercaptan Treating Unit tables)
