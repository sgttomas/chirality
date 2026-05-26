# Datasheet — DEL-079-04 Vendor Engineered Equipment Package

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-079-04_vendor-engineered-equipment-package` |
| Name | Vendor Engineered Equipment Package |
| ParentPackageID | `PKG-079` |
| PackageName | Instrument Air Building |
| Discipline | Mechanical |
| Type | Vendor Package Production Unit |
| ResponsibleParty | Package Vendor (engineering/design/equipment) with EPC Integrator integration review |
| Facility location | 04-25 (Deepcut); serves 04-25 gas plant, 03-25 liquids hub, and 03-25 compressor station (SourcePath: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; SectionRef: "Instrument Air Basis", L1908) |

## Attributes

Equipment scope per Equipment-by-Building listing for Instrument Air Building (SourcePath: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; SectionRef: building row L2601):

| Tag | Description (per source row) |
|---|---|
| K-4210-1 | Instrument air compressor (lead) — ASSUMPTION based on K- tag convention |
| K-4220-1 | Instrument air compressor (lag) — ASSUMPTION based on K- tag convention |
| F-4215-1 | Filter (F-class) — service TBD |
| F-4220-1 | Filter (F-class) — service TBD |
| F-4225-1 | Filter (F-class) — service TBD |
| F-4230-1 | Filter (F-class) — service TBD |
| V-4210-1 | Vessel (receiver) — service TBD |
| V-4240-1 | Vessel (receiver/dryer) — service TBD |

Counts confirmed: 2 x 100 percent capacity air compressors in lead-lag operation with skid spacing and piping provision for a future third 100 percent compressor (SourcePath: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; SectionRef: "Instrument Air Design Values", L1939-L1940; cross-ref Sparing Philosophy table row "Instrument Air Compressors", L2354).

## Conditions

Design and operating conditions (SourcePath: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; SectionRef: "Instrument Air Design Values", L1929-L1943):

| Parameter | Value |
|---|---|
| Water dewpoint | Maximum -73.3 deg C at 1000 kPag |
| PSV setting | 1034 kPag (150 psig) or less |
| Compressor capacity rating condition | SCM/H at 930 kPag (135 psig) |
| Minimum actuator supply pressure | 551 kPag (80 psig) upstream of valve instrument air supply regulators |
| Facility shutdown pressure | 482 kPag (70 psig) |
| Normal header supply pressure | 827 kPag (120 psig) |
| Compressor max discharge / shutdown pressure | 1000 kPag (145 psig) |
| Reserve volume | 15 minutes usable reserve after instrument air shutdown |
| Reserve-volume calculation range | Header, dry receiver, and wet receiver volume from 120 psig down to 80 psig |
| Building area classification | Assumed General Purpose / Non-Classified; validation required |

## Capacity / Demand

(SourcePath: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; SectionRef: "Instrument Air Demand", L1910-L1925.)

| Demand Component | Flow, SCFM | Status |
|---|---:|---|
| 04-25 gas plant calculated total | 600 | TBC |
| 04-25 contingency, 20 percent | 120 | TBC |
| 04-25 total demand | 720 | TBC |
| 03-25 caustic unit oxidation air | 214 | TBC |
| 03-25 calculated total, remaining instruments | 100 | TBC |
| 03-25 contingency, 20 percent | 79 | TBC |
| 03-25 total demand | 393 | TBC |
| Consolidated 04-25 instrument-air package demand | 1,113 | TBC |

Sizing basis per instrument type: 0.5 SCFM per control valve / air-operated pump / air-cooler louver; 1.0 SCFM per shutdown valve / switching valve / blowdown valve; 20 percent contingency.

## Construction

- Piping classification: ASME Category D (SourcePath: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; SectionRef: "Instrument Air Design Values", L1933).
- Skid-edge isolation: skid-edge block valve required for all services; skid-edge spectacle blind required for all services **except instrument air** (SourcePath: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; SectionRef: "Skid-Edge and Processing-Unit Isolation", L2451-L2452).
- Skid-edge isolation located outside buildings in interconnect piping (same SectionRef).
- Module location: shop-built vendor package (SourcePath: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; SectionRef: Modular Equipment List row "420-1 Instrument Air Package", L2785).
- Materials of construction: TBD (location TBD in source).
- Coatings, insulation, noise specs: TBD (location TBD in source).

## References

- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — Instrument Air Basis (L1906-L1943); Sparing Philosophy table (L2354); Building/Equipment table (L2601); Modular Equipment List (L2785); Skid-Edge Isolation (L2447-L2458).
- `_Sources/26020-Package_Requirements.docx` — package heading 32 (binary; location TBD; not directly readable in this run).
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row 381 (DEL-079-04).
- `_CONTEXT.md` (deliverable identity).
