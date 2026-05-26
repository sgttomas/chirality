# Datasheet: Vendor Engineered Equipment Package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-074-04_vendor-engineered-equipment-package |
| Deliverable name | Vendor Engineered Equipment Package |
| Parent package | PKG-074 - Caustic Treating (NGL Mercaptan Removal) |
| Workbook ID / row | 74 / row 51 |
| WBS | 01 |
| CoA tracking number | 26020-01-27-002 |
| Discipline | Mechanical |
| Type | Vendor Package Production Unit |
| Responsible party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review |
| Covers scope items | SOW-0059; SOW-0060; SOW-0061; SOW-0062 |
| Supports objectives | OBJ-001; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 (ASSUMPTION: package-grouping heuristic) |

## Attributes

| Attribute | Current basis | Source |
|---|---|---|
| Package description | Workbook-defined Mechanical package supplying a complete caustic treating system for NGL/C3+ mercaptan removal immediately downstream of the deethanizer. | PACKAGE_REGISTER.csv, PKG-074 |
| Vendor responsibility scope | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. | PACKAGE_REGISTER.csv, PKG-074 (Responsibility column) |
| EPC Integrator responsibility scope | EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | PACKAGE_REGISTER.csv, PKG-074 (Responsibility column) |
| Process basis identity | Non-regenerative caustic treating unit on cooled C3+ NGL downstream of the de-ethanizer; third-party proprietary process provider supplies the detailed engineering package. | 4-25_Deepcut_DBM.md, Current-Scope NGL Mercaptan Treating |
| Vendor design basis evidence | Expected vendor package design basis and datasheet evidence; detailed rows are source-specific where available. | ARTIFACT_REGISTER.csv, ART-04D78DC493 |
| Vendor physical package evidence | Vendor-owned engineering, design, fabrication/supply, and physical package evidence. | ARTIFACT_REGISTER.csv, ART-7D22DB55EB |
| Major included equipment scope | Caustic contactor/mixer equipment, caustic outlet filtration, water wash and coalescing equipment, caustic regeneration equipment, heaters/exchangers, circulation and transfer pumps, pressurized caustic drain drum, DSO handling, caustic storage interfaces, incinerator interface, instrumentation, controls, and building-contained caustic equipment. | ARTIFACT_REGISTER.csv, ART-EDAC8A3AB7; 26020-Package_Requirements.docx package heading 28 (location TBD; binary source not locally readable) |
| Tagged equipment list (workbook) | E-6720-1, H-6710-1, MX-6727-1, MX-6728-1, P-6720-1, P-6725-1, P-6730-1, P-6735-1, P-6726-1, P-6710-1, P-6711-1, V-6720-1 | 4-25_Deepcut_DBM.md, Common Equipment / package equipment row |

## Conditions

| Condition | Current basis | Source |
|---|---|---|
| Design rate | 2,385 m3/d / 15,000 bbl/d. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Design Parameters |
| Inlet service | Cooled C3+ NGL from the de-ethanizer outlet path. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Design Parameters |
| Inlet design pressure | 2,213 kPag. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Design Parameters |
| Outlet design pressure | 1,978 kPag. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Design Parameters |
| Pressure low/high cases | TBC at source. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Design Parameters |
| Inlet temperature range | Low 26.7 deg C; design 43.3 deg C; high 48.8 deg C. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Design Parameters |
| Fresh caustic concentration | 50 wt% NaOH. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Design Parameters |
| Circulating caustic concentration | 14.7 wt% NaOH, to be confirmed. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Design Parameters |
| Fresh caustic storage | 1 x 400 bbl atmospheric tank, heated, insulated, truck-in capable, fuel-gas blanketed, not connected to VRU header; design SG 1.75 TBC. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Equipment and Utilities |
| Spent caustic storage | 1 x 400 bbl atmospheric tank, heated, insulated, truck-out capable, incinerator-header connected, backflash-protected with flame arrestor, low-pressure fuel gas blanketed. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Equipment and Utilities; Disulphide Oil, Spent Caustic, and Waste Amine |
| Disulphide oil (DSO) storage | 1 x 400 bbl atmospheric tank, heated, insulated, truck-out capable, incinerator-header connected, backflash-protected, fuel-gas blanketed; design SG 1.75 TBC; DSO-to-C5+ blending is a detailed-engineering review item. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Equipment and Utilities; Disulphide Oil, Spent Caustic, and Waste Amine |
| Treated NGL sulphur performance | At 1 mol% H2S inlet, total C1-C3 RSH as S 3,240 ppmw inlet to 203.7 ppmw treated; total sulphur 4,166 ppmw inlet to 970 ppmw treated. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Design Parameters (NGL sulphur case table) |
| Indoor installation | All caustic treating equipment installed indoors due to caustic freezing/crystallization risk; segregated into the Mercaptan Treating Unit building or immediately adjacent area. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Equipment and Utilities |
| Safety showers | Building includes water safety showers; quantity and location TBD; activation must trigger discrete control-room alert. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Equipment and Utilities |
| Materials restrictions | No aluminum in the caustic building; insulation cladding/straps in caustic exposure areas are stainless steel; caustic storage tanks must use polymer or other caustic-compatible materials; building floor material and caustic tank material remain detailed-engineering TBDs. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Equipment and Utilities |
| Common-equipment classification | NGL caustic treating equipment is "common equipment" — single train serves the facility and must be taken out of service for maintenance. | 4-25_Deepcut_DBM.md, Common Equipment discussion |

## Construction

| Item | Current basis | Source |
|---|---|---|
| Contactor function | Caustic NGL contactor mixes NGL and circulating caustic solution to extract mercaptans; sweetened NGL flows downstream to filtration and water wash. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Equipment and Utilities |
| Contactor outlet filters | NGL contactor caustic outlet filters are independent vessels from the contactor, provided as 2 x 100%. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Equipment and Utilities |
| Water wash and coalescing | Downstream water wash and coalescing filtration dilute and remove entrained caustic from treated NGL to protect the molecular sieve. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Equipment and Utilities |
| Water wash recycle pumps | Single-stage vertical inline centrifugal pumps with single mechanical seals; 2 x 100% sparing. Water wash recycled internally and drained on flow control to produced water tanks. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Equipment and Utilities |
| Pressurized caustic drain drum (V-6940-1) | Receives high-pressure caustic drains; vapours flow to stabilizer overheads compressor first-stage suction; caustic level-controlled to spent caustic storage; heated, insulated, demister, sized with K factor less than 0.2. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Equipment and Utilities; SOC inlet source table |
| Make-up water | Supplied from process water storage tank if required during upset operation; final routing TBC. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Equipment and Utilities |
| Incinerator interface | Spent caustic tank vapours and DSO off-gas route to incinerator located at 3-25 facility near the flare stacks; knock-out drum upstream of incinerator separates free liquids; supplemental fuel gas rate, incinerator flow basis, and shared-facility operational responsibility remain TBD. | 4-25_Deepcut_DBM.md, Incinerator Interface |
| Applicable interface types | Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports. | INTERFACE_REGISTER.csv, IFC rows for PKG-074 |
| Detailed-engineering open items | Process provider selection, contactor stages quantity, caustic concentration confirmation, winter vapour pressure values, high-ethane case review, low/high pressure cases, shower quantity/location, building floor material, caustic tank material selections. | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Design Parameters; NGL Mercaptan Treating Equipment and Utilities |

## References

- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/ARTIFACT_REGISTER.csv
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/OBJECTIVE_DELIVERABLE_MAP.csv
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx (binary; not locally readable; location TBD)
