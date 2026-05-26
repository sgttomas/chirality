# Specification — DEL-059-04 Vendor Engineered Equipment Package

> Normative requirements for the Package Vendor's engineered NGL storage-bullet equipment package for PKG-059 Storage Bullets. Requirements are derived only from accessible source material; inferences are labeled `ASSUMPTION` and missing items are `TBD`.

## Scope

**In scope.** Vendor engineering, design, fabrication/supply, and delivery of the physical equipment package comprising the PKG-059 NGL storage-bullet system, developed from the upstream EPC Scope of Work (`DEL-059-01`) and Package Datasheet (`DEL-059-02`).

Source-grounded scope basis:
- Storage configuration basis is 16 x 120,000 USG NGL storage bullets at 04-25 for processed C3+ NGL product (production-rate basis 15,400 bbl/d, 2.5 days of storage). [`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 448, line 492, lines 1627-1629]
- Product disposition is to the NRM NEBC Connector via LACT. [`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 446]
- The source basis explicitly states that "Detailed NGL bullet design parameters are not fully developed in the available product-storage basis and remain a required design-development item." [`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 1629]
- "Develop the detailed design basis for 16 x 120,000 USG NGL storage bullets" is identified as required design-development work. [`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 1814]

**Out of scope.** Civil/foundation work outside the package skid limits; site grading/spill containment (interface only — site civil owns it); facility-wide electrical area classification and detection (interface only); cross-facility utility supply to package battery limits (interface only); EPC integration acceptance review (covered by `DEL-059-06`).

## Requirements

### R-1 Package configuration

**R-1.1** The package shall comprise sixteen (16) NGL storage bullets, each of 120,000 USG nominal storage capacity, for C3+ NGL product service. [Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 448 and line 492.]

**R-1.2** The package shall provide aggregate storage duration consistent with the 2.5-day duration basis at the 15,400 bbl/d production-rate basis. [Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 448.]

**R-1.3** The package shall accommodate routing of stored C3+ NGL to the NRM NEBC Connector via LACT (suction-pump interface to facility). [Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 446; spacing interface line 252.]

### R-2 Layout and spacing (API 2510)

The vendor's package layout proposal shall be consistent with the following minimum-spacing requirements that drive cluster-internal geometry and inform package battery-limit definitions. Final plot-plan verification is owned by EPC layout (see Interfaces).

**R-2.1** Maximum pressurized bullets per cluster: **<=6**. [Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 249, API 2510.]

**R-2.2** Minimum distance between pressurized bullet clusters: **15.24 m (50 ft)**. [Source: line 250, API 2510.]

**R-2.3** Minimum distance between butane bullet and propane bullet (where applicable): **2.804 m (9.2 ft)**. [Source: line 251, API 2510.]

**R-2.4** Minimum distance between pressurized bullets and the pump skid taking suction from bullets: **3.05 m (10 ft)**. [Source: line 252, API 2510.]

**R-2.5** Minimum distance between pressurized bullets and rotating equipment unrelated to bullets: **15.24 m (50 ft)**. [Source: line 253, API 2510.]

**R-2.6** Minimum distance between pressurized bullets and property line: **38.1 m (125 ft)**. [Source: line 259, API 2510 Table 1.]

**R-2.7** Minimum distance between pressurized bullets and nearest atmospheric tank: **30.48 m (100 ft)**. [Source: line 265, API 2510.]

**R-2.8** Minimum distance between pressurized bullets and nearest spill-containment area: **3.05 m (10 ft)**. [Source: line 266, API 2510.]

**R-2.9** Minimum distance between flare and pressurized bullets: **30.48 m (100 ft)**. [Source: line 284, API 2510.]

**R-2.10** Minimum distance between fired heater and pressurized bullets: **15.24 m (50 ft)**. [Source: line 299, API 2510.]

### R-3 Spill containment interface

**R-3.1** The package design shall be compatible with sloped grading beneath the NGL bullets that redirects NGL away from the pipe rack and process areas to reduce pool-fire exposure (site civil scope; package provides drainage/containment interface points). [Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2722.]

### R-4 Pressure vessel design and fabrication (ASSUMPTION-flagged where not sourced)

**R-4.1** Detailed mechanical design parameters (design pressure, design temperature, allowable corrosion, materials of construction, internals, nozzle schedule, external loads, insulation) shall be developed by the vendor as part of the package scope. The current upstream basis explicitly defers these to design-development work. [Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 1629, 1814.] Numerical values: **TBD**.

**R-4.2 (ASSUMPTION)** Pressure-vessel fabrication is expected to follow ASME Section VIII (Division 1 or 2) and applicable jurisdictional registrations. The available source slices do not state the governing pressure-vessel code; vendor shall confirm with the EPC Integrator at kick-off. **Authority TBD**.

### R-5 Package deliverables (vendor document scope)

**R-5.1** The package shall include, at minimum, the following vendor deliverables: datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, and vendor document registers. [Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617 — project-wide mechanical-package basis applied to PKG-059. ASSUMPTION: applicability to a storage-bullet package by analogy with the cited project-wide statement; vendor scope confirmed by `_CONTEXT.md`.]

**R-5.2** Vendor deliverables shall preserve clear scope boundaries among process vendors, electrical/controls systems, field construction, and cross-facility utility interfaces. [Source: same.]

### R-6 Scope coverage

**R-6.1** The package shall satisfy scope items `SOW-0181`, `SOW-0182`, `SOW-0183`, and `SOW-0184`. [Source: `_CONTEXT.md` "Covers Scope Items".] Detailed line-item content of each `SOW-018x` is `TBD` until the SOW deliverable (`DEL-059-01`) is consumed.

### R-7 Truck/rail distribution exclusion

**R-7.1** The package shall not be designed for truck or rail distribution of NGL product from 04-25. [Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 446 — "No truck or rail distribution is planned for NGL product from 04-25."]

## Standards

| ID | Standard | Status |
|---|---|---|
| STD-1 | API 2510 (Design and Construction of LPG Installations) | Cited in DBM spacing tables; full text `location TBD` (not locally accessible) |
| STD-2 | API 2510 Table 1 | Cited for property-line spacing; `location TBD` |
| STD-3 | ASME Section VIII Div 1/2 | ASSUMPTION (governing pressure-vessel code); authority `TBD` |
| STD-4 | NFPA 30 | Cited in DBM for atmospheric-tank spacing context; package applicability `TBD` |
| STD-5 | OGAOM Sec. 9.6.15 / DPR 48 | Cited for public-road and flare spacing; applicability to bullet package interface `TBD` |
| STD-6 | OGPFR Appendix 1 Schedule 1 | Cited for flare thermal-radiation flux (interface only); `TBD` for package scope |

## Verification

| Req. | Verification approach |
|---|---|
| R-1.1, R-1.2, R-1.3 | Design review against upstream Package Datasheet (`DEL-059-02`) and Scope of Work (`DEL-059-01`); vendor datasheet sign-off |
| R-2.1 - R-2.10 | Layout/plot-plan review against API 2510 spacing table; EPC Integrator verification (input to `DEL-059-06`) |
| R-3.1 | Interface review with site civil grading and containment design; drainage tie-in inspection |
| R-4.1 | Vendor design-development package review; mechanical datasheets signed by vendor engineer of record |
| R-4.2 | Code-compliance verification (ASME stamping/registration evidence); jurisdictional inspection records |
| R-5.1, R-5.2 | Vendor document register completeness check; turnover package gate (`DEL-059-05`) |
| R-6.1 | Traceability matrix to `SOW-018x` items |
| R-7.1 | Confirmation in vendor scope-of-supply document that no truck/rail loading is provided |

## Documentation

The vendor shall produce, at minimum:

- Equipment datasheets (per bullet, per skid)
- Mechanical drawings (GA, fabrication, nozzle orientation)
- P&ID input
- Cause-and-effect input
- Utility load summary (electrical, instrument air, drains)
- Relief and depressurization load data
- Field tie-in list
- Operating and design envelopes
- Sparing philosophy
- Materials and coating basis
- Maintenance-access plan
- Shipped-loose item list
- Vendor document register (master index)

Source for the deliverable list: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617.

## Interfaces

- Upstream: `DEL-059-01_scope-of-work` (SOW), `DEL-059-02_package-datasheet` (datasheet basis)
- Downstream: `DEL-059-05_vendor-document-turnover-package` (turnover), `DEL-059-06_epc-vendor-package-review-and-acceptance` (acceptance)
- Cross-discipline: Civil (grading/containment), Electrical/Instrumentation, Process (pump suction), Fire-and-Gas detection layout (spacing context)

`_DEPENDENCIES.md` declares no Upstream/Downstream edges at PREPARATION; the interfaces above are decomposition-derived context (ASSUMPTION until declared).
