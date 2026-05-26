# Specification — DEL-057-04 Vendor Engineered Equipment Package (Stabilizers)

## Scope

### In Scope (Package Vendor)
- Engineering, design, fabrication/supply, and physical equipment package for three (3) Inlet Stabilizer Packages per SOW-0178/0179. Source: `_CONTEXT.md`; SOW-0178; SOW-0179.
- Vendor package design basis and datasheet set covering the trayed reboiled distillation column, stabilizer flash feed separator, feed pumps, feed/bottoms exchanger, reboiler, and product cooler. Source: SOW-0179; DBM §SEC-04 L676–L710.
- Vendor responsibility for package engineering, package design, vendor documentation contributing to integration, and physical equipment package. Source: `PACKAGE_REGISTER.csv` row PKG-057; SOW-0177.

### Out of Scope (By Others — EPC Integrator and Owner)
- Interconnecting piping at skid edge; DCS integration; foundations; electrical power supply from plant MCC; installation/erection. Source: SOW-0180.
- Facility-level integration, tie-ins, constructability, procurement/construction coordination, and interface management. Source: SOW-0177; `PACKAGE_REGISTER.csv` row PKG-057.
- Stabilizer overheads compression (handled by PKG-050 SOC); routing of stabilizer overhead to SOC second-stage suction defined as an interface, not vendor scope. Source: DBM L678.

## Requirements

### R1 — Equipment count and design split
The vendor shall supply three (3) Inlet Stabilizer Packages on a 3 × 40 % design basis, each rated at 1,272 m³/d (8,000 bbl/d). Source: SOW-0179; DBM L682–L684.

### R2 — Stabilizer column configuration
Each stabilizer column shall be a trayed, reboiled distillation column with 20 conventional floating-valve trays and 3:1 turndown. Source: SOW-0179; DBM L678.

### R3 — Operating conditions (flash feed separator)
The stabilizer flash feed separator shall operate at 345 kPag and 30.6 °C, with approximately 15 minutes retention time and ≥10 minutes of liquid retention between LLL and HLL. ASSUMPTION: 15-minute retention figure carried per SOW-0180; DBM L704 notes 15 min "TBC." Source: SOW-0180; DBM L704.

### R4 — Design conditions (flash feed separator)
The flash feed separator shall have a design inlet pressure of 1,724 kPag and design inlet temperature of 60 °C. Source: SOW-0180.

### R5 — Feed/bottoms exchanger
The feed/bottoms exchanger shall be designed for a 16.7 °C (30 °F) minimum approach, with inlet liquids on the shell side for cleanability. Source: SOW-0180; DBM L706.

### R6 — Stabilizer column inlet conditions
Liquid hydrocarbons shall be pre-heated to 71 °C upstream of the stabilizer column top tray. Source: SOW-0180; DBM L678.

### R7 — Stabilizer column minimum pressure
The stabilizer column shall have a minimum operating pressure of 793 kPag. Source: SOW-0180.

### R8 — Stabilizer product cooler
The product cooler shall have 130 % excess area at the design point, with a single fan and VFD-compatible electric motor; final product temperature shall be 43.3 °C (110 °F). Source: SOW-0180; DBM L708.

### R9 — Feed pumps
Two (2) × 100 % multistage horizontal centrifugal stabilizer feed pumps, electric-motor driven and VFD-compatible, shall be supplied with upstream basket strainers. Strainer mesh and pump seal type are TBD pending pump selection. Source: SOW-0180; DBM L706.

### R10 — Stabilizer reboiler
The stabilizer reboiler shall be a vertical NEN single-pass thermosiphon shell-and-tube exchanger with process fluid on the tube side and tubes seal-welded to the tubesheet; service is hot heat medium with required temperature to be reviewed during detailed engineering. Source: DBM L706.

### R11 — Vapour disposition interfaces
Stabilizer overhead vapour shall be pressure-controlled to SOC second-stage suction; stabilizer flash/feed overhead vapour shall be pressure-controlled to SOC first-stage suction. Source: DBM L678, L704.

### R12 — Product quality specifications
The stabilized product shall meet:
- Vapour pressure < 85 kPaa by ASTM D6377;
- Density 650 to 775 kg/m³;
- C4- basis (C3- × 3 + C4) < 5 liquid vol %.
Source: DBM L685–L687.

### R13 — Instrumentation (called out in SOW)
The package shall include at minimum one (1) LIT and one (1) TIT. ASSUMPTION: additional instrumentation per vendor standard and detailed engineering; full instrument index is TBD. Source: SOW-0179.

### R14 — Flash/feed inlet level control
The stabilizer flash/feed inlet LCV shall use a low-select controller that closes on high flash-feed level, high flash-feed pressure, or high flash-feed overhead flow. Source: DBM L704.

### R15 — Relief and blowdown routing
Stabilizer flash/feed separator relief and blowdown shall route to HP flare; the vessel shall be internally coated with Devchem 253. Source: DBM L704.

### R16 — Capacity envelope (per package, winter)
Each package shall accommodate up to a winter two-phase inlet of 2.821 MMSCFD, liquid inlet of 11.97 m³/h, and vapour inlet of 0.6412 MMSCFD at the design point. Source: DBM L697, L699, L700.

### R17 — Product routing
Stabilized C5+/NGL product shall be level-controlled from tower bottoms through the feed/bottoms exchanger and product cooler, with normal routing to the NGL mercaptan treating unit and manual diversion outside the package to the condensate slop tank. Source: DBM L710.

## Standards

| Standard / Spec | Application | Source |
|---|---|---|
| ASTM D6377 | Product vapour pressure measurement basis (< 85 kPaa) | DBM L685; **location TBD** for clause |
| CAPP butane equivalent | Product C4- and RVP constraints (3·(C1+C2+C3) + iC4 + nC4 < 5.0 vol %; 12 psia RVP) | DBM L484; **location TBD** for clause |
| `26020-Package_Requirements.docx` package heading 12 | Authoritative package requirements (binary; not directly read) | SOW-0177/0178/0179/0180; **location TBD** for clause |
| RFQ `26020-01-PT-RFQ-17-005_Inlet Stabilizers_R0.docx` | Word source basis for package RFQ scope | `PACKAGE_REGISTER.csv` row PKG-057; **location TBD** for clause |

## Verification

| Requirement | Verification Approach |
|---|---|
| R1 | Equipment list / general arrangement review against SOW; FAT count check |
| R2 | Vendor mechanical datasheet review; column internals inspection (tray count, type) at FAT |
| R3, R4 | Vessel datasheet review against process datasheet; PSV sizing review |
| R5 | Heat-exchanger thermal/mechanical datasheet review against approach criterion |
| R6 | Process datasheet review and performance test at startup |
| R7 | Vessel design pressure stamping; relief device sizing |
| R8 | Cooler thermal datasheet review; performance test at design ambient |
| R9 | Pump datasheet review; mechanical run test; VFD compatibility check |
| R10 | Exchanger datasheet review; weld procedure qualification; hydrotest |
| R11 | P&ID interface check vs. PKG-050 SOC; pressure-control loop FAT |
| R12 | Performance test with product sampling and laboratory analysis (ASTM D6377; chromatograph for C4-) |
| R13 | Instrument index review; loop check at FAT |
| R14 | Control narrative review; logic test at FAT |
| R15 | Flare-header tie-in design review; coating QA record |
| R16 | Capacity calc/heat-mass-balance review against per-package basis |
| R17 | P&ID review; tie-in field walk during construction |

## Documentation (Vendor Deliverables Anticipated)

- Vendor engineered physical equipment package (the supplied equipment). Source: `_CONTEXT.md` Anticipated Artifacts.
- Vendor package design basis and datasheet set. Source: `_CONTEXT.md` Anticipated Artifacts.
- The full vendor document register, submittals, and turnover records are tracked under sibling deliverable `DEL-057-05_vendor-document-turnover-package` (separate scope). Source: `DELIVERABLE_REGISTER.csv` row DEL-057-05.

## Exclusions and Assumptions

- Objective associations (OBJ-001, OBJ-003..OBJ-010) carried as **ASSUMPTION** under `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC` pending explicit objective-to-deliverable confirmation. Source: `_CONTEXT.md`.
- Detailed sparing philosophy and operating split across the three units is TBD. Source: DBM L612.
- Stabilizer overhead gas disposition under revised downstream configuration is TBC. Source: DBM L690.
- Direct extraction from binary `26020-Package_Requirements.docx` is **location TBD**; all clause-level claims tagged to SOW extracts.
