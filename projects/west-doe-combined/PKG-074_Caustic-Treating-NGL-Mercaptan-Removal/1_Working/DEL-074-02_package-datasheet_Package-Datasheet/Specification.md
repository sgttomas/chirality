# Specification — Package Datasheet (PKG-074 Caustic Treating, NGL Mercaptan Removal)

## Scope

Defines the normative content required of the EPC Integrator Package Datasheet for PKG-074 Caustic Treating (NGL Mercaptan Removal). The Package Datasheet conveys process, performance, equipment, materials, interface, and documentation requirements sufficient for a third-party proprietary process provider to engineer and supply the package, and for the EPC Integrator to integrate the package into the 04-25 Deep Cut Gas Plant. The package scope is supply of a non-regenerative caustic treating system for C3+ NGL mercaptan removal immediately downstream of the de-ethanizer (PACKAGE_REGISTER.csv row 51; DBM-Deepcut lines 1509-1513).

**Excluded:** On-site caustic regeneration column (not part of the current non-regenerative basis; DBM-Deepcut line 1513). Incinerator hardware (located at and operated from 3-25; DBM-Deepcut line 1570). NGL filtration, water wash internals, molecular-sieve dehydration, and NGL storage hardware downstream of the package boundary (separate packages; DBM-Deepcut line 1513). Package-specific exclusions from PACKAGE_REGISTER.csv row 51 are marked TBD: no package-specific exclusions stated in source materials.

## Requirements

### R-001 Process function (FACT)
The package shall remove mercaptans (RSH) from cooled C3+ NGL using a non-regenerative caustic process, with extraction performance consistent with the basis cases in `Datasheet.md` Conditions section. Source: DBM-Deepcut lines 1511, 1519, 1534-1537, 1541, 1544.

### R-002 Governing capacity (FACT)
Governing design rate: 2,385 m3/d (15,000 bbl/d). Source: DBM-Deepcut line 1520.

### R-003 Design pressures (FACT)
Inlet design 2,213 kPag; outlet design 1,978 kPag. Low/high pressure cases shall be confirmed in detailed engineering (TBC). Source: DBM-Deepcut lines 1522-1524.

### R-004 Inlet temperature envelope (FACT)
Inlet temperature shall accommodate low 26.7 deg C, design 43.3 deg C, and high 48.8 deg C. Downstream caustic solution shall not fall below 26.7 deg C (80 deg F). Source: DBM-Deepcut lines 1338, 1525.

### R-005 Caustic strength (FACT / ASSUMPTION)
Fresh caustic concentration shall be 50 wt% NaOH (FACT). Circulating process caustic concentration is 14.7 wt% NaOH, to be confirmed in detailed engineering (ASSUMPTION pending confirmation). Source: DBM-Deepcut lines 1526-1527.

### R-006 Treated NGL sulphur targets (FACT, case-based)
At 1 mol% H2S inlet gas, with caustic treating, the package shall achieve:
- Total C1-C3 RSH as S in treated C3+: 203.7 ppmw S (25.71 lb/h S)
- Total sulphur in treated C3+: 970 ppmw S (122.5 lb/h S)
Source: DBM-Deepcut lines 1541, 1544.

### R-007 Equipment configuration (FACT)
- Caustic NGL contactor with circulating caustic loop (DBM-Deepcut line 1554)
- NGL contactor caustic outlet filters: 2 x 100% sparing, independent vessels (DBM-Deepcut line 1554)
- Water wash recycle pumps: vertical inline single-stage centrifugal, single mechanical seal, 2 x 100% (DBM-Deepcut line 1558)
- Pressurized caustic drain drum: heated, insulated, demister, K factor < 0.2 (DBM-Deepcut line 1560)
- Fresh caustic tank: 1 x 400 bbl, atmospheric, heated, insulated, truck-in capable, fuel-gas blanket, NOT connected to VRU header (DBM-Deepcut lines 1528, 1562)
- Spent caustic tank: 1 x 400 bbl, atmospheric, heated, insulated, truck-out capable, connected to incinerator header with flame arrestor, LP fuel-gas blanket (DBM-Deepcut lines 1529, 1562)
- DSO tank: 1 x 400 bbl, atmospheric, heated, insulated, truck-out capable, connected to incinerator header with flame arrestor, LP fuel-gas blanket (DBM-Deepcut lines 1530, 1564)

### R-008 Material restrictions (FACT)
No aluminum materials shall be installed in the caustic building. Insulation cladding and straps in caustic-exposure areas shall be stainless steel. Caustic storage tanks shall use polymer or other caustic-compatible materials; specific selection TBD. Building floor material TBD. Source: DBM-Deepcut line 1566.

### R-009 Installation location (FACT)
All caustic-containing equipment shall be installed indoors in the Mercaptan Treating Unit building or immediately adjacent area, due to caustic freezing and crystallization risks. Source: DBM-Deepcut line 1552.

### R-010 Safety showers (FACT)
The building shall be equipped with water safety showers. Shower activation shall provide a discrete control-room alert. Shower quantity and location TBD. Source: DBM-Deepcut line 1552.

### R-011 Tank venting (FACT)
Spent caustic tank and DSO tank vapours shall route to the incinerator header (incinerator physically at 3-25). Flame arrestors required on incinerator-header connections. Fresh caustic tank shall NOT connect to the VRU header. Source: DBM-Deepcut lines 1562, 1570.

### R-012 Drain handling (FACT)
The pressurized caustic drain drum shall route NGL vapours to the stabilizer overheads compressor first-stage suction header and shall level-control caustic to the spent caustic storage tank. Source: DBM-Deepcut line 1560.

### R-013 Make-up water (ASSUMPTION pending DE)
Make-up water during upset operation shall be supplied from the process water storage tank. Final routing to be confirmed in detailed engineering. Source: DBM-Deepcut line 1556.

### R-014 Package interface scope (FACT)
The package vendor is responsible for package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator is responsible for integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Source: PACKAGE_REGISTER.csv row 51 (`PackageVendorScope`, `IntegratorScope` columns).

### R-015 Applicable interface types (FACT)
The package shall provide interface points compatible with the interface set declared for PKG-074: Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports. Source: PACKAGE_REGISTER.csv row 51.

### R-016 Process provider selection (PROPOSAL / TBD)
A third-party proprietary process provider will supply the detailed engineering package; selection is TBD. Contactor stage count, caustic concentration confirmation, winter vapour pressures, high-ethane case, and pressure low/high cases are detailed-engineering TBDs. Source: DBM-Deepcut lines 1511, 1548.

## Standards

| Standard / Code | Applicability | Location | Source |
|---|---|---|---|
| Mechanical pressure-vessel code (ASME BPVC or equivalent jurisdictional code) | Pressure vessels (contactor, drain drum) | location TBD | ASSUMPTION (common industry practice; not explicitly cited in DBM-Deepcut NGL caustic section) |
| API atmospheric storage tank standard | Fresh caustic, spent caustic, and DSO tanks (atmospheric 400 bbl) | location TBD | ASSUMPTION (atmospheric tanks per DBM-Deepcut lines 1562, 1564; specific API standard not stated in source) |
| 26020-Package_Requirements.docx | Package documentation and engineering requirements | package heading 28 | PACKAGE_REGISTER.csv row 51 (source not parsed locally; location TBD within document) |
| 26020-Packages_Interfaces_4_export.xlsx | Package and interface declared content | Packages row 51 | PACKAGE_REGISTER.csv row 51 (binary spreadsheet; location TBD within file) |

## Verification

| Requirement | Verification method |
|---|---|
| R-001, R-002, R-006 | Process guarantee from package vendor; performance test on commissioning at design flow and inlet sulphur basis |
| R-003, R-004 | Vendor mechanical design submittal review; pressure-test and operating-temperature checks at commissioning |
| R-005 | Caustic concentration sampling and lab confirmation during commissioning and routine operation |
| R-007 | Equipment list, P&ID, and isometric review against this Specification |
| R-008 | Materials of construction review against vendor MTRs and inspection reports |
| R-009, R-010, R-011 | Building/plot-plan review; F&G and alarm test on commissioning |
| R-012 | P&ID review; functional test of drain drum level control and routing |
| R-013 | Process water tie-in review; commissioning walkdown |
| R-014, R-015 | EPC interface matrix sign-off against package vendor scope and the PKG-074 interface-type set |
| R-016 | Vendor selection and detailed-engineering closeout register |

## Documentation

The package datasheet shall be supported by (anticipated artifacts from `_CONTEXT.md`):
- Package technical datasheet (this deliverable)
- Vendor engineering handoff basis
- Package interface requirements matrix
- Source-supported equipment and design criteria

Additional package vendor documentation requirements (per PACKAGE_REGISTER.csv row 51 narrative) are sourced from `26020-Package_Requirements.docx` package heading 28; specific document list within that section is TBD (not parsed locally).
