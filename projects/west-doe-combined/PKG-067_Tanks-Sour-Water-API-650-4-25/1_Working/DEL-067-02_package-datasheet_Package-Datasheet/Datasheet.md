# Datasheet — DEL-067-02 Package Datasheet (PKG-067 Tanks, Sour Water (API 650) 4-25)

**Discipline:** Mechanical
**Type:** EPC Package Datasheet
**Responsible Party:** EPC Integrator
**Decomposition basis:** GATE-07 Final Published (2026-05-24)

## Identification

| Field | Value | Source |
|---|---|---|
| Package ID | PKG-067 | PACKAGE_REGISTER row 94 |
| Workbook Row | 94 | PACKAGE_REGISTER row 94 |
| Package Name (decomposition) | Tanks, Sour Water (API 650) 4-25 | PACKAGE_REGISTER row 94 |
| Package Tag (workbook) | 26020-01-PT-19-005 | PACKAGE_REGISTER row 94 (Tag field) |
| Plant / Facility | West Doe Deepcut Expansion, facility 04-25 (LSD 04-25-80-15W6) | 4-25_Deepcut_DBM.md §1, §2 (lines 5-22) |
| Service | Storage of sour/produced water received from the 04-25 facility prior to pipeline transfer to the 03-25 Liquids Hub | 4-25_Deepcut_DBM.md §Storage and §Produced Water (lines 493, 504-524) |
| Discipline | Mechanical | DELIVERABLE_REGISTER row 529 |
| Tank tags (member equipment) | TK-9010-1, TK-9020-1 | PACKAGE_REGISTER companion equipment row (line 2627) |
| Quantity | 2 tanks (1 train pair) | 4-25_Deepcut_DBM.md line 493; PACKAGE_REGISTER line 2627 |

NOTE on naming: The package is titled "Tanks, Sour Water (API 650)" while the underlying tank tags and DBM Process Storage Areas table label these as "Produced Water Storage Tank." Both names refer to the same TK-9010-1 / TK-9020-1 pair per PACKAGE_REGISTER row 94. ASSUMPTION: "sour water" and "produced water" are used interchangeably for this service; downstream documents use "produced/sour water" until human confirmation.

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Tank standard | Modified API-650 atmospheric, 16 oz (water column) test pressure | 4-25_Deepcut_DBM.md line 518 |
| Nominal capacity per tank | 2,000 bbl | 4-25_Deepcut_DBM.md line 493 |
| Number of tanks | 2 | 4-25_Deepcut_DBM.md line 493 |
| Maximum fill | 90% of tank volume; thermal expansion review required | 4-25_Deepcut_DBM.md line 519 |
| External insulation | Yes | 4-25_Deepcut_DBM.md line 524 |
| Heat tracing / heating | Yes (tanks heated) | 4-25_Deepcut_DBM.md line 524 |
| Internal coating | Devchem 253 on floor, walls, and roof | 4-25_Deepcut_DBM.md line 524 |
| Hydrocarbon skim | Kennilworth-type hydrocarbon skim float system | 4-25_Deepcut_DBM.md line 524 |
| Pressure/vacuum relief | At least one PVRV per tank; EPRV sizing to be reviewed in detailed engineering | 4-25_Deepcut_DBM.md line 524 |
| Blanket gas | Provided for winter vacuum prevention; API-2000 basis for rates | 4-25_Deepcut_DBM.md line 523 |
| Tank isolation philosophy | To be reviewed in context of potential sour vapours | 4-25_Deepcut_DBM.md line 524 |
| Design specific gravity (tank design) | 1.25 (TBC) | 4-25_Deepcut_DBM.md line 508 |
| Fluid specific gravity (operating) | Produced water density 1008 kg/m³ at 26.7 °C; conservative pump SG 1.18 | 4-25_Deepcut_DBM.md line 508 |
| Storage days (sizing basis) | 8.9 days at 380 bbl/d | 4-25_Deepcut_DBM.md line 493 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service category | Atmospheric storage; sour potential (vapours may contain H2S); contents include trace lube oils, hydrocarbons, TEG, amine, H2S, caustic, mercaptans (list not comprehensive, TBC) | 4-25_Deepcut_DBM.md line 508 |
| Average accumulation rate | 60 m³/d continuous at 04-25 | 4-25_Deepcut_DBM.md line 506 |
| Batch pump-in rate (to 03-25 pipeline) | ~240 m³/d | 4-25_Deepcut_DBM.md line 506 |
| Flow to storage, summer | 1,684 kg/h / 39.9 Am³/d | 4-25_Deepcut_DBM.md line 511 |
| Flow to storage, normal | TBC | 4-25_Deepcut_DBM.md line 512 |
| Flow to storage, design | TBC | 4-25_Deepcut_DBM.md line 513 |
| Production rate basis (sizing) | 380 bbl/d | 4-25_Deepcut_DBM.md line 493 |
| Site (climatic) | West Doe Deepcut Expansion, BC; ~22.2 km north of Dawson Creek; cold-climate design (winterization required) | 4-25_Deepcut_DBM.md §1 (lines 7, 524) |
| Sour-service potential | Yes (sour vapours possible; tank isolation philosophy under review) | 4-25_Deepcut_DBM.md line 524 |
| Truck-out provision | Common envirobox connection; vacuum truck assumption 2.75 m³/min TBC; typical B-train 55 m³ in 20 min | 4-25_Deepcut_DBM.md lines 514-516 |
| Secondary containment | TBD — not stated for produced water tanks in source slice (TBD; analog to amine surge tank which is explicitly stated as containment-equipped per DBM line 1173 but this is different service) | TBD |

## Construction

| Item | Value | Source |
|---|---|---|
| Tank type | Atmospheric, modified API-650 | 4-25_Deepcut_DBM.md line 518 |
| Foundation | TBD (not specified in DBM produced-water section) | TBD |
| Materials of construction (shell, floor, roof) | Carbon steel base assumed (ASSUMPTION, API-650 default); internally coated Devchem 253 | 4-25_Deepcut_DBM.md line 524; ASSUMPTION on base material |
| Insulation system | External insulation; type and thickness TBD | 4-25_Deepcut_DBM.md line 524; thickness TBD |
| Heating | Tank heaters provided; medium TBD | 4-25_Deepcut_DBM.md line 524; medium TBD |
| Nozzles and connections | Inlet from upstream collection (including stage-1 compressor scrubber liquids via Hydra-Cell pump); outlet to produced water transfer pumps (2 x 100%); blanket gas connection; PVRV; truck-out (envirobox); skim float fittings; level/temperature instrumentation TBD | 4-25_Deepcut_DBM.md lines 521, 1025, 524 |
| Spacing (between atmospheric tanks) | 2.35 m (7.72 ft) | 4-25_Deepcut_DBM.md line 268 (NFPA 30 Table 22.4.2.1) |
| Spacing from public road | 80 m (262.5 ft) | 4-25_Deepcut_DBM.md line 270 (OGAOM Sec. 9.6.15, DPR 48) |
| Spacing from flare | 25 m (82 ft) from separators/atmospheric produced-water tanks | 4-25_Deepcut_DBM.md line 283 |
| Spacing from fired heater | 25 m (82 ft) | 4-25_Deepcut_DBM.md line 297 |
| Cathodic protection | Required as an applicable interface (per package interface list) | PACKAGE_REGISTER row 94 (Applicable Interfaces) |
| Grounding/bonding | Required as an applicable interface | PACKAGE_REGISTER row 94 |
| Structural / foundations / supports | Required as an applicable interface | PACKAGE_REGISTER row 94 |

## Interface Requirements Matrix (Package-Level)

Per PACKAGE_REGISTER row 94, the following interface types apply to this package and form the EPC Integrator interface-handoff envelope for the vendor:

| Interface Type | Applicability | EPC vs. Vendor Boundary (TBD pending interface register row resolution) |
|---|---|---|
| Process Piping | Yes | Inlet to tank, transfer outlet to pumps, blanket gas piping, drain piping — boundaries at tank flange (ASSUMPTION) |
| Relief / Flare / Vent | Yes | PVRV vent routing TBD (atmospheric vs. flare header) |
| Drain / Containment | Yes | Tank drains, hydrocarbon skim drain, containment system — boundaries TBD |
| Grounding / Bonding | Yes | Tank shell bonding to facility grid |
| Area / Exterior Lighting | Yes | Tank area lighting outside vendor scope (EPC) |
| Cathodic Protection | Yes | CP system tie-ins (EPC scope) |
| I&C / Control Cabling | Yes | Level, temperature, PVRV monitoring; cabling to BPCS (EPC scope) |
| Grading / Site Drainage / Spill Containment | Yes | EPC scope |
| Structural / Foundations / Supports | Yes | Tank foundation EPC scope; tank shell vendor scope (ASSUMPTION) |

Detailed per-interface tag-and-spec resolution is downstream and tracked under INTERFACE_REGISTER for PKG-067 (TBD: confirm interface row coverage during vendor RFQ readiness).

## Equipment List (member tags)

| Tag | Description | Source |
|---|---|---|
| TK-9010-1 | Produced Water Storage Tank #1 (within PKG-067 "Tanks, Sour Water (API 650)" package) | 4-25_Deepcut_DBM.md line 2627 |
| TK-9020-1 | Produced Water Storage Tank #2 (within PKG-067) | 4-25_Deepcut_DBM.md line 2627 |

Adjacent / related (NOT in this package, but supplying inlet flow): Stage-1 compressor scrubber liquid Hydra-Cell pump (DBM line 1025); produced water transfer pumps WATER TRANSFER PUMP (x4) and SOUR WATER TREATMENT PUMPS (x2) housed in Tank Farm Pump Building 2 (DBM line 2555).

## References

- `_REFERENCES.md` (deliverable-local)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (locally accessible authoritative source)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` row 94
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row 529
- `_Sources/26020-Package_Requirements.docx` package heading 22 (binary; package-specific paragraph text not locally extracted — content depending on this source is marked TBD)
