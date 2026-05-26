# Package Datasheet — PKG-076 Lube Oil Supply

DeliverableID: `DEL-076-02_package-datasheet`
ParentPackageID: `PKG-076`
PackageName: Lube Oil Supply
Discipline: Mechanical
Type: EPC Package Datasheet
ResponsibleParty: EPC Integrator

## Identification

| Field | Value | Source |
|---|---|---|
| Package ID | PKG-076 | `_CONTEXT.md`; PROJECT_DECOMP DELIVERABLE_REGISTER row DEL-076-02 |
| Package Name | Lube Oil Supply | DBM-Deepcut SEC-08, Package Line-Item Requirements row 51 (`4-25_Deepcut_DBM.md` §"Package Line-Item Requirements") |
| Plant / Area | 4-25 Deepcut (LSD) | `4-25_Deepcut_DBM.md` §"Package Line-Item Requirements" row 51 |
| Function | Heated compressor cylinder and crank-case lube oil storage with transfer pumps to compressor frame day tanks | `4-25_Deepcut_DBM.md` §"Lube Oil Storage and Pump Basis"; §"Utility System Summary" lube oil row |
| Service | Compressor frame (crank-case) and reciprocating compressor cylinder lubrication | `4-25_Deepcut_DBM.md` §"Lube Oil Storage and Pump Basis" |
| Package equipment count (source basis) | 2 (Lube Oil Supply Pumps) | `4-25_Deepcut_DBM.md` §"Package Line-Item Requirements" row 51 |
| Equipment tags | P-9240-1, P-9250-1 | `4-25_Deepcut_DBM.md` §"Package Line-Item Requirements" row 51 |

## Attributes — Storage and Transfer Equipment

| Item | Tag | Quantity | Service | Source |
|---|---|---:|---|---|
| Compressor cylinder lube oil storage tank | TBD | 1 | 400 bbl heated storage tank in storage tank area | `4-25_Deepcut_DBM.md` §"Lube Oil Storage and Pump Basis" |
| Compressor crank-case lube oil storage tank | TBD | 1 | 200 bbl heated storage tank in storage tank area | `4-25_Deepcut_DBM.md` §"Lube Oil Storage and Pump Basis" |
| Compressor cylinder lube oil pump | P-9240-1 | 1 | Fills compressor frame day tanks as needed | `4-25_Deepcut_DBM.md` §"Lube Oil Storage and Pump Basis"; §"Package Line-Item Requirements" row 51 |
| Compressor crank-case lube oil pump | P-9250-1 | 1 | Fills compressor frame day tanks as needed | `4-25_Deepcut_DBM.md` §"Lube Oil Storage and Pump Basis"; §"Package Line-Item Requirements" row 51 |
| Lube Oil Transfer Pump (sparing entry) | TBD | 1 | 100% capacity, 100% installed (sparing register entry) | `4-25_Deepcut_DBM.md` SEC-09 sparing table (Lube Oil Transfer Pump) |

CONFLICT-001: The DBM SEC-08 Lube Oil Storage and Pump Basis names two pumps (P-9240-1 cylinder, P-9250-1 crank-case) with no installed spare implied, while the SEC-09 sparing register lists a single "Lube Oil Transfer Pump" at 1×100%. Whether P-9240-1 and P-9250-1 are each unspared, or whether a third transfer-service pump is intended, is not resolvable from accessible sources. Surfaced in `Guidance.md` Conflict Table.

## Conditions — Design Basis

| Parameter | Value | Source |
|---|---|---|
| Compressor cylinder lube oil tank design specific gravity | 1.00 (TBC) | `4-25_Deepcut_DBM.md` §"Lube Oil Storage and Pump Basis" |
| Compressor crank-case lube oil tank design specific gravity | 1.00 (TBC) | `4-25_Deepcut_DBM.md` §"Lube Oil Storage and Pump Basis" |
| Cylinder oil grade(s) | TBC during FEED; multiple cylinder oils may be required by service (inlet, sales, stabilizer overheads, acid gas, sales booster) due to sulphur content, rich gas and H2S | `4-25_Deepcut_DBM.md` §"Lube Oil Storage and Pump Basis" |
| Crank-case (frame) oil grade | TBD | not stated in accessible source |
| Storage temperature / tank heating | Heated tanks; specific design temperature TBD | `4-25_Deepcut_DBM.md` §"Utility System Summary" lube oil row, §"Lube Oil Storage and Pump Basis" |
| Tank type / code (e.g. API 650, atmospheric) | TBD | not stated in accessible source |
| Containment / secondary containment basis | TBD; lube-oil storage referenced to project hazardous-material list which was not available in the workspace | `3-25_Comp_and_Liquids_DBM.md` §"Emergency Power, Lube Oil, and Analyzers" |
| Additional storage requirements | TBD | `4-25_Deepcut_DBM.md` §"Lube Oil Storage and Pump Basis"; §"Open Design Development Requirements" Lube oil row |
| Truck offload / fill connection | TBD | not stated in accessible source |
| Day-tank quantity, sizing, location at compressor frames | TBD (associated with served compressor packages, not this package) | ASSUMPTION based on §"Lube Oil Storage and Pump Basis" wording "fill frame day tanks as needed" |

## Construction — Materials, Layout, and Hazardous-Area

| Item | Value | Source |
|---|---|---|
| Location | Storage tank area, 4-25 Deepcut | `4-25_Deepcut_DBM.md` §"Lube Oil Storage and Pump Basis" |
| Spacing basis | Atmospheric Tank and General Plant Spacing per DBM §2.5 applies; specific lube-oil tank spacing not separately tabulated | `4-25_Deepcut_DBM.md` §2.5 "Atmospheric Tank and General Plant Spacing" |
| Tank materials of construction | TBD | not stated in accessible source |
| Pump type, driver | TBD (driver assumed electric motor by analogy to other utility transfer pumps; mark ASSUMPTION) | ASSUMPTION |
| Area classification | TBD | not stated in accessible source |
| Insulation / heat-trace basis | Heated tank implies tracing or tank heater; medium TBD | ASSUMPTION based on "heated" descriptor in §"Lube Oil Storage and Pump Basis" |
| Hazardous-materials inventory listing | Refers to project hazardous-material list; list not available in workspace | `3-25_Comp_and_Liquids_DBM.md` §"Emergency Power, Lube Oil, and Analyzers" |

## Interface Summary (for handoff)

| Interface | Counterparty | Description | Source |
|---|---|---|---|
| Compressor frame day-tank fill | Inlet/Sales Compressors (PKG mapped to K-2150-1…K-2550-1), Acid Gas Compressors, Sales Gas Booster, Stabilizer Overheads Compressors, Expander | Pumps deliver crank-case and cylinder oil to served compressor packages' frame day tanks; many compressor packages also include their own electric circulating lube oil heater for quick start | `4-25_Deepcut_DBM.md` §"Lube Oil Storage and Pump Basis"; §828, §928, §967 (SOC, booster, acid gas compressors); §"Package Line-Item Requirements" rows 33-40 |
| Tank heating utility | Heat-medium / electric (utility selection TBD) | Tanks are heated; supply utility not specified in accessible source | TBD |
| Truck-in delivery | Bulk oil supplier | Tank fill from truck delivery (typical for bulk lube oil); not explicitly stated for this package | ASSUMPTION |
| Drainage and spill containment | Project drain / hazardous-material handling system | Containment basis not stated; referenced to project hazardous-material list (not accessible) | `3-25_Comp_and_Liquids_DBM.md` §"Emergency Power, Lube Oil, and Analyzers" |

## References

- `4-25_Deepcut_DBM.md` — §"Utility System Summary" (line 1835 lube oil row); §"Lube Oil Storage and Pump Basis" (lines 2059-2072); §"Package Line-Item Requirements" row 51 (lines 2602); SEC-09 sparing register Lube Oil Transfer Pump (line 2363); §"Open Design Development Requirements" Lube oil row (line 2163). Located at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- `3-25_Comp_and_Liquids_DBM.md` — §"Emergency Power, Lube Oil, and Analyzers" (lube-oil storage and hazardous-material list note). Located at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- PROJECT_DECOMP GATE-07 snapshot: `DELIVERABLE_REGISTER.csv` row DEL-076-02; `PACKAGE_REGISTER.csv` PKG-076; `ARTIFACT_REGISTER.csv`; `INTERFACE_REGISTER.csv`; `OBJECTIVE_DELIVERABLE_MAP.csv`. Snapshot root: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Decomposition reference text identified in `_CONTEXT.md`: "Workbook Packages row 70; 26020-Package_Requirements.docx package heading 30". The `.docx` and `.xlsx` source artifacts under `_Sources/` are binary and not parsed in this pass (location TBD for clause-level citations).
