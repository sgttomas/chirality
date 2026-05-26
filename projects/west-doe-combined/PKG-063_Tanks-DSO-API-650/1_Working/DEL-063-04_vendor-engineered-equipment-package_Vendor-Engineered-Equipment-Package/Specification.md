# Specification — DEL-063-04 Vendor Engineered Equipment Package (Tanks, DSO API 650)

## Scope

This specification defines the vendor engineering, design, fabrication/supply, and physical equipment package for the DSO (Disulphide Oil) storage tank (TK-6770-1, 1 x 400 bbl) within PKG-063 (Tanks, DSO API 650), serving the 4-25 Deepcut NGL Mercaptan Treating Unit.

Inclusions:
- Tank shell, roof, bottom, nozzles, internals, and integral attachments to API 650.
- Heating system, insulation, and weather/freeze protection for stored DSO.
- Fuel-gas blanket connection and flame-arrestor-protected incinerator-header tie-in.
- Truck-out connection and associated isolation.
- Vendor-supplied instrumentation that is integral to the package (per vendor scope split — to be confirmed in Package Datasheet, DEL-063-02).
- Vendor design basis, datasheet set, and supporting calculations.

Exclusions:
- EPC Construction Work Package execution (covered by DEL-063-03).
- Vendor document turnover (covered by DEL-063-05).
- EPC review/acceptance activities (covered by DEL-063-06).
- Foundation and tie-in piping unless explicitly included in the Package Datasheet — TBD.

Sources covering scope items SOW-0209–SOW-0212: `_CONTEXT.md`; further SOW slice content — location TBD (text in 26020-Package_Requirements.docx not locally extracted).

## Requirements

### R-1 — Governing Code
The tank shall be designed and fabricated to API 650. Edition/addenda — TBD (`location TBD`).

### R-2 — Capacity
Nominal storage capacity shall be 400 bbl (source: DBM-Deepcut L1530). Working/overflow margins per API 650 — TBD.

### R-3 — Service Fluid
The tank shall store DSO produced by the non-regenerative caustic treating process (DBM-Deepcut L528). Materials of construction shall be compatible with DSO; specific alloy selection — TBD.

### R-4 — Design Specific Gravity
Design specific gravity shall be 1.75, to be confirmed by vendor (DBM-Deepcut L1564). ASSUMPTION: applied to shell/foundation hydrostatic design loadings.

### R-5 — Heating
The tank shall be heated and insulated to maintain DSO above its freezing/handling threshold (DBM-Deepcut L1564). Heating medium, heater type, and set-point — TBD.

### R-6 — Atmospheric Operation with Fuel-Gas Blanket
The tank shall operate atmospheric with a low-pressure fuel-gas blanket (DBM-Deepcut L1564). Blanket pressure-control set point and relief sizing — TBD.

### R-7 — Vapour Route to Incinerator
The tank vapour space shall connect to the incinerator header (DBM-Deepcut L1564, L1570). The vapour connection shall include a flame arrestor for backflash protection (DBM-Deepcut L1564).

### R-8 — Truck-Out Capability
The tank shall be truck-out capable (DBM-Deepcut L1564). Loading-arm/hose interface and spill-containment requirements — TBD.

### R-9 — Alternate Disposal Path (Optional)
Provision for pumping recovered DSO into the C5+ product stream may be provided; this alternate disposal path is subject to detailed-engineering review (DBM-Deepcut L528, L1564). PROPOSAL: include nozzle and isolation provision in vendor scope pending EPC ruling.

### R-10 — Hazardous Gas Detection
LEL, H2S, methyl mercaptan, and fire detection devices shall be placed per facility hazards study; quantity, set points, voting logic, and placement are TBD pending detailed design and safety studies (DBM-Comp_and_Liquids L838).

### R-11 — Materials Constraints
No specific material constraint for the DSO tank itself was located in available sources. The caustic-building aluminum prohibition (DBM-Deepcut L1566) is scoped to the caustic building and is not extended to the DSO tank without source support — TBD whether DSO tank shares this constraint.

### R-12 — Vendor Deliverables
The vendor shall produce: (a) the physical equipment package, and (b) the vendor package design basis and datasheet set (`_CONTEXT.md` Anticipated Artifacts).

## Standards

| Standard | Use | Location Reference |
|---|---|---|
| API 650 | Welded tanks for oil storage — governing fabrication code | Package title (PROJECT_DECOMP PKG-063) |
| API 2000 (venting atmospheric/low-pressure tanks) | ASSUMPTION: applicable for blanket/vacuum sizing — `location TBD` |
| API 651 / 652 (cathodic protection, lining) | ASSUMPTION: candidate references — `location TBD` |
| Project HSE / area classification standard | Hazardous-area classification for incinerator/blanket tie-ins — `location TBD` |
| 26020-Package_Requirements.docx, heading 18 | Package-level requirements set — content `location TBD` (binary not extracted) |

## Verification

| Requirement | Verification Approach |
|---|---|
| R-1 (API 650) | Vendor design report, weld procedure qualification records, NDE records, hydrostatic test report. |
| R-2 (capacity) | Vendor general arrangement and volumetric calculation. |
| R-3 (service compatibility) | Vendor materials selection report; EPC review. |
| R-4 (SG 1.75) | Vendor shell/foundation calculations; EPC ruling required to close TBC. |
| R-5 (heating/insulation) | Heat-loss calculation; insulation specification; heater data sheet. |
| R-6 (blanket) | Blanket regulator data sheet; relief sizing per API 2000 (TBD). |
| R-7 (incinerator route + flame arrestor) | P&ID review; flame arrestor data sheet and certification. |
| R-8 (truck-out) | GA showing truck-out connection; loading procedure (Procedure.md). |
| R-9 (alternate C5+ disposal) | Detailed-engineering review record; PROPOSAL acceptance/rejection by EPC. |
| R-10 (gas detection) | Detector schedule and HAC drawing — owned at facility level. |
| R-11 (materials constraints) | EPC ruling required (TBD). |
| R-12 (vendor deliverables) | Receipt and acceptance under DEL-063-05 / DEL-063-06. |

## Documentation

Vendor shall provide (anticipated artifacts; final list per Package Datasheet DEL-063-02):
- Vendor design basis
- Tank datasheet
- General arrangement and nozzle orientation drawings
- Shell, roof, bottom design calculations
- Materials selection report
- Heat-loss / heating system calculations and data sheets
- Blanket/relief sizing calculations
- Flame arrestor data sheet
- Weld procedure specifications and qualification records
- NDE plan and records
- Hydrostatic test report
- Coatings/insulation specifications
- ITP (Inspection and Test Plan)
- Operating and maintenance manuals
- Spare parts list
- As-built drawings
