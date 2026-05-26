# Specification — DEL-066-03 Construction Work Package (PKG-066 Tanks, Condensate (API 650) 4-25)

> Normative document. States what the Construction Work Package (CWP) deliverable must contain and which requirements govern installation, inspection, turnover, and tie-in of the 04-25 condensate tank package.

## Scope

This Specification governs the **EPC Integrator Construction Work Package** for PKG-066 (Tanks, Condensate (API 650), 4-25 facility). It addresses how the package equipment listed in the Package Datasheet (DEL-066-02) and Scope of Work (DEL-066-01) is to be physically installed, built, inspected, turned over, and tied into the larger 04-25 facility systems.

**Included:**
- Construction work package content for the 5 condensate storage tanks at 04-25 (TK-9110-1, TK-9120-1, TK-9130-1, TK-9140-1, TK-9150-1) and their immediate tank-farm interfaces.
- Installation and tie-in workface plan content covering site grading, foundations, tank erection, mechanical hookup, shipped-loose instrument/valve installation, ISBL/OSBL tie-in piping, electrical/instrumentation hookup, blanket-gas and VRU vapour return connection, and condensate transfer to the 03-25 Liquids Hub.
- Construction interface and turnover checklist content addressing mechanical completion, hydrostatic/leak verification, coating/insulation/heat-trace verification (where applicable), instrumentation loop checks, and operational handover.

**Excluded:**
- Vendor-fabrication engineering, tank design calculations, or vendor document content — those belong to DEL-066-04 (Vendor Engineered Equipment Package) and DEL-066-05 (Vendor Document Turnover Package).
- 03-25 Liquids Hub tank construction (separate facility, separate package), except as required to describe the cross-facility condensate transfer tie-in.
- LACT, sales-condensate metering, and third-party NRM scope.

## Requirements

### REQ-CWP-01 — Mandatory EPC anchor content
The CWP shall include, at minimum: (a) a construction work package document, (b) an installation and tie-in workface plan, and (c) a construction interface and turnover checklist.
Source: `_CONTEXT.md` ("Anticipated Artifacts"); decomposition GATE-07 deliverable row.

### REQ-CWP-02 — Tank specification compliance
Installed tanks shall conform to Modified API 650 atmospheric design with 16 oz test pressure and a 90% maximum-fill shutdown limit.
Source: DBM-Deepcut lines 1646-1648.

### REQ-CWP-03 — Tank quantity and tag assignment
Five (5) condensate tanks shall be installed at 04-25 with tag set TK-9110-1, TK-9120-1, TK-9130-1, TK-9140-1, TK-9150-1.
Source: DBM-Deepcut line 2625.
**CONFLICT note:** DBM-Deepcut line 1639/1640 states "4 x 3,800 bbl tanks" for local 04-25 condensate storage; the equipment register at line 2625 lists 5 tanks. Quantity is carried as 5 here pending human ruling; see Guidance Conflict Table.

### REQ-CWP-04 — Inlet/outlet cascade configuration
Two tanks shall be designated inlet tanks receiving stabilizer bottoms; an internal pipe stand shall enable cascade by elevation into downstream product tanks; one tank shall be configured as slop with a dedicated truck-in/out envirobox connection; remaining tanks shall be product service. Common truck-out connection shall be provided for inlet and outlet condensate tanks.
Source: DBM-Deepcut lines 1661, 1665. **ASSUMPTION:** allocation of the 5 tags (2 inlet / 1 slop / 2 product) follows the DBM allocation pattern; final tag-to-service mapping `location TBD` pending the package datasheet (DEL-066-02).

### REQ-CWP-05 — Blanket gas and vapour recovery hookup
Each tank shall be connected to the blanket-gas supply for winter vacuum prevention (API 2000 rate basis) and to the VRU suction header for vapour collection. Off-spec overhead vent sizing, EPRV sizing, tank isolation philosophy for sour vapours, vacuum-truck rates, and thermal expansion review remain detailed-engineering items.
Source: DBM-Deepcut line 1663.

### REQ-CWP-06 — Insulation and winterization
Slop tank shall be fully insulated. Product condensate tanks shall be installed non-insulated; winter temperature maintenance shall be by product recycle through the product recycle pump (per DEL-066-02).
Source: DBM-Deepcut lines 1644-1645, 1671.

### REQ-CWP-07 — Foundation basis
Tank foundations shall be designed and installed against the final geotechnical report. Until the geotechnical report is accepted, foundation parameters are placeholders only and construction-release is prohibited.
Source: DBM-Comp_and_Liquids lines 141, 688, 700.

### REQ-CWP-08 — Field-construction responsibility split
Construction management, grading, piling, foundations, plant roads, module/equipment off-loading and setting, mechanical hookup, shipped-loose instrument and valve installation, miscellaneous structural supports, home-run cabling, electrical terminations, area lighting, fence/security, and demolition where required shall be Tourmaline field-construction scope. ISBL/OSBL tie-in piping responsibility is an external interface marker; per-tie-in responsibility shall be confirmed.
Source: DBM-Deepcut §"Construction Responsibility" lines 101-127.

### REQ-CWP-09 — Tie-in joint planning
Joint planning shall be required for all tie-ins to existing or related facilities (notably the condensate transfer tie-in to the 03-25 Liquids Hub via P-9210-1 / P-9220-1). Tie-in timing shall be established as the project progresses.
Source: DBM-Deepcut lines 127, 1673.

### REQ-CWP-10 — CWP register alignment before IFC
The CWP register shall be aligned to the plot plan, equipment list, and overall construction work package register before issue for construction.
Source: DBM-Comp_and_Liquids line 661.

### REQ-CWP-11 — Plot plan dependency
Final coordinate-level tank placement and access/spacing verification shall be against plot plan drawing CIV-235633-5002. Until that drawing is supplied, compliance-by-inspection is `TBD` and CWP coordinate content shall be marked accordingly.
Source: DBM-Deepcut line 323.

### REQ-CWP-12 — Spacing / siting compliance
Tank siting shall satisfy applicable spacing rules including: 50 m flare-to-atmospheric-condensate-tank distance (OGAOM Sec. 9.6.15); 25 m fired-heater-to-atmospheric-tank distance (OGAOM Sec. 9.6.15); 2.35 m tank-to-tank spacing (NFPA 30 Table 22.4.2.1); 80 m tank-to-public-road (OGAOM Sec. 9.6.15, DPR 48).
Source: DBM-Deepcut lines 268-270, 282, 297.

### REQ-CWP-13 — Coordination with adjacent tank-farm pump module
Tank installation shall be sequenced with the tank-farm pump module installation (product recycle pump, condensate skim pump, and condensate transfer pumps P-9210-1 / P-9220-1) to permit functional commissioning of recycle, skim, and transfer services.
Source: DBM-Deepcut lines 1669-1674.

## Standards

| Standard | Use | Locally accessible? |
|---|---|---|
| API 650 (Modified) | Tank design / fabrication / erection basis | Referenced; standard text `location TBD` |
| API 2000 | Blanket-gas and venting rate basis | Referenced; standard text `location TBD` |
| API 2510 (storage spacing) | Cited in DBM spacing table | DBM-Deepcut line 258 (cited); standard text `location TBD` |
| NFPA 30 (flammable/combustible liquids spacing) | Tank-to-tank and tank-to-property-line spacing | Cited; standard text `location TBD` |
| OGAOM Sec. 9.6.15 (BC OGC; provincial spacing) | Tank-to-flare, tank-to-road, tank-to-heater spacing | Cited; standard text `location TBD` |

## Verification

| Requirement | Verification Approach |
|---|---|
| REQ-CWP-02 | Witness hydrostatic test and inspection records per API 650; verify 16 oz test pressure record. |
| REQ-CWP-03 | Equipment tag walkdown against package equipment list and Datasheet. |
| REQ-CWP-04 | Walkdown of inlet/outlet piping cascade, slop envirobox connection, and common truck-out manifold against P&ID. |
| REQ-CWP-05 | Blanket-gas pressure/leak check; VRU header isolation valve walkdown; loop-check PVRVs. |
| REQ-CWP-06 | Insulation inspection (slop); recycle-loop functional test (product). |
| REQ-CWP-07 | Foundation QC records traceable to accepted geotechnical report. |
| REQ-CWP-08 | Construction responsibility matrix sign-off per work-front. |
| REQ-CWP-09 | Joint tie-in schedule and tie-in permit records. |
| REQ-CWP-10 | Pre-IFC CWP-register reconciliation record. |
| REQ-CWP-11 | Coordinate walkdown against released plot plan (when available). |
| REQ-CWP-12 | Surveyed spacing measurements vs. governing standards. |
| REQ-CWP-13 | Sequenced commissioning checklist for tanks + pump module. |

## Documentation (CWP deliverable artifact set)

Per `_CONTEXT.md` anticipated artifacts and the decomposition register entry:

- **Construction Work Package** (master document; integrates plot reference, equipment list reference, package datasheet reference, tie-in schedule, inspection plan, turnover plan).
- **Installation and tie-in workface plan** (work-front by work-front sequencing; tie-in tickets; lockout/permit references).
- **Construction interface and turnover checklist** (mechanical completion items; loop-check items; ITP signoffs; punch list; care-and-custody handover).
- Supporting evidence: foundation QC records, hydrotest records, coating/insulation inspection records, instrument loop check records, blanket-gas leak-check records, tank-farm pump module commissioning checklists.
