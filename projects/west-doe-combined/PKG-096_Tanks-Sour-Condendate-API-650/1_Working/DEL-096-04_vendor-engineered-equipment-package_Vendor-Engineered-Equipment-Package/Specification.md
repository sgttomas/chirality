# Specification — DEL-096-04 Vendor Engineered Equipment Package (Tanks, Sour Condensate, API 650)

> Normative deliverable. Requirements bind the Package Vendor's engineered/designed/fabricated equipment package and its associated vendor design basis and datasheet set. Requirements are grounded in accessible source slices; inferred or downstream-design-dependent items are explicitly labeled `ASSUMPTION` or `TBD`.

## Scope

### In Scope
- Vendor engineering, design, fabrication/supply, and physical delivery of the sour condensate atmospheric storage tank package within the 03-25 Liquids Hub: 2 × 3,800 bbl sour inlet condensate tanks and 4 × 3,800 bbl sour condensate tanks (subject to final tank register). SourcePath: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, lines 406, 410, 411.
- Vendor-issued design basis and datasheet set for the tanks (process datasheet, mechanical datasheet, materials selection, GA, P&IDs (vendor portion), foundation loads, weld map, NDE/ITP plan).
- Tank shells, bottoms, roofs, internal coating, external insulation/heat tracing, nozzles, manways, tank-mounted instrumentation/relief devices, stairs/platforms/handrails, grounding/bonding lugs.
- Vapour interface preparation to the EPC-defined VRU header tie-in (vendor terminal point at the tank nozzle). Source line 434.
- Compliance with API 650 (per package title). ASSUMPTION pending source confirmation — see Guidance CT-01.
- Anchoring to the EPC Scope of Work (DEL-096-01) and EPC Package Datasheet (DEL-096-02). `_CONTEXT.md` Scope.

### Out of Scope
- Construction work package, installation/tie-in, and turnover (DEL-096-03 EPC scope).
- Vendor document register, vendor document submittals, source vendor document tabling, and turnover records (DEL-096-05 scope).
- EPC vendor package review and acceptance (DEL-096-06 scope).
- Product (sweet) condensate tanks, slop tank, produced-water tanks, caustic tanks, and H₂O₂ tank — separate packages.
- Booster, loading, recycle, and skim pumps — separate scope.
- LACT and custody-transfer equipment (NRM third-party scope; same source, line 417).
- 03-25 stabilization, 03-25 SOC, 03-25 condensate dehydration (withdrawn / removed per SCA basis; same source lines 64–65, 366, 442).
- Offsite pipeline scope (by others) downstream of the facility tie-in. Same source, line 432.

## Requirements

### R-1 — EPC Anchor (FACT)
The vendor package shall be developed from, and shall remain traceable to, the EPC Scope of Work (DEL-096-01) and the EPC Package Datasheet (DEL-096-02). Where vendor scope departs from those documents, the vendor shall raise a documented deviation. SourcePath: `_CONTEXT.md` Scope; decomposition narrative.

### R-2 — Quantity and Capacity (FACT)
The package shall comprise **2 × 3,800 bbl sour inlet condensate tanks** and **4 × 3,800 bbl sour condensate tanks** unless superseded by the final tank register. SourcePath: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, lines 406, 410, 411. See CT-03.

### R-3 — Sour Inlet Storage Retention (FACT)
Sour inlet condensate storage shall provide approximately **0.6 day upset storage**. SourcePath: same, line 411.

### R-4 — Design Code (ASSUMPTION)
Tanks shall be designed and fabricated to **API 650** (per package title). ASSUMPTION — DBM SEC-06 explicitly cites "API-650 Modified" only for produced-water tanks (line 421); the literal code basis for sour condensate tanks is not stated in the accessible DBM slice. See Guidance CT-01. API 650 clause-level location: **TBD** (standard not locally accessible).

### R-5 — Minimum Design Ambient and Winterization (FACT)
The package shall be suitable for a minimum ambient of **−40 °C** and shall include **external insulation, heat tracing, and tank heating** consistent with the site winterization basis. SourcePath: same, lines 145, 421.

### R-6 — Vapour Routing Interface (FACT)
Tank vapours shall be designed to be collected and routed to the **VRU suction header**. The vendor scope terminates at the tank nozzle; downstream piping to the VRU header is EPC scope. The VRU discharge ultimately routes to the 04-25 SOC suction per SCA-002. SourcePath: same, lines 434, 436.

### R-7 — Stored Fluid Compatibility (FACT)
The tanks and all wetted components shall be compatible with **stabilized sour C5+ condensate** received from 04-25 (stabilized) and future third-party stabilized sources, including the mercaptan family: methyl mercaptan, ethyl mercaptan, dimethyl sulphide, 2-propanethiol, n-propyl mercaptan, methyl ethyl sulphide. SourcePath: same, lines 20, 210, 376, 380, 382.

### R-8 — Sour Service Metallurgy (ASSUMPTION)
Materials shall be selected for sour-service compatibility consistent with applicable NACE/CSA requirements. ASSUMPTION — specific NACE standard (e.g., MR0175 / ISO 15156) is not named in the accessible DBM slice; location TBD. See CT-04.

### R-9 — Internal Coating (TBD)
Internal coating selection is **TBD**. Devchem 253 is the accepted basis for produced-water tanks (DBM line 421) and is a candidate for sour condensate service pending vendor confirmation of mercaptan compatibility. See CT-02.

### R-10 — Aluminum Use (ASSUMPTION)
Aluminum shall not be used in any wetted or vapour-contact component of the package. ASSUMPTION — the accessible DBM prohibits aluminum **in the caustic building** (line 402); no equivalent prohibition is stated for the condensate tank package. Conservative metallurgy applies.

### R-11 — Site Civil/Structural Loads (FACT)
The vendor design shall accommodate site loads as published in the DBM: snow Ss = 2.5 kPa, wind pressure 0.30 kPa (1-in-10) / 0.40 kPa (1-in-50), site elevation 673 m AMSL, barometric pressure 93.3 kPa(a), Site Class D seismic with Sa(0.2)=0.253 g, Sa(0.5)=0.223 g, Sa(1.0)=0.128 g, Sa(2.0)=0.0717 g, PGA=0.142 g. Maximum wind speed 138 km/h is TBC. SourcePath: same, SEC-02.

### R-12 — Foundation Loads Deliverable (FACT)
The vendor shall provide foundation loads (dead, live, wind, snow, seismic, hydrotest, settlement criteria) to the EPC Integrator for civil/structural foundation design. ASSUMPTION on output form (load table + plan). Final foundation design is EPC scope.

### R-13 — Final Tank Register Supersession (FACT)
Tank quantity and functional allocation shall be reconfirmed against the final tank register; the vendor shall accommodate changes via documented engineering change before fabrication release. SourcePath: same, line 406. See CT-03.

### R-14 — Vendor Design Basis and Datasheet Set (FACT)
The vendor shall produce and issue, as part of this deliverable, a **vendor design basis and datasheet set** covering at minimum: process datasheet, mechanical/strength datasheet, materials selection diagram, nozzle schedule, GA drawings, foundation load drawings, weld map, NDE/ITP plan, MTR list, coating system specification. `_CONTEXT.md` Anticipated Artifacts. ASSUMPTION on enumeration; the binary `26020-Package_Requirements.docx` (heading 48) may further specify — location TBD. See CT-05.

### R-15 — Inspection and Testing (ASSUMPTION)
The vendor shall execute API 650 hydrostatic test, bottom weld vacuum-box test, RT/UT/MT/PT per code, and coating holiday inspection, and shall furnish records to the EPC Integrator. ASSUMPTION — clause-level API 650 text not locally accessible.

### R-16 — Vapour Space Pressure Coordination (FACT)
Tank vapour-space design pressure and PVRV setpoints shall be coordinated with the VRU suction header design pressure to avoid both overpressure and excessive flare/breather discharge. SourcePath: same, line 434; principle stated in Guidance.

### R-17 — Methanol and Trace Methanol Handling (TBD)
Tank design shall not preclude infrequent methanol presence in the stored fluid. SourcePath: same, line 218.

### R-18 — Tank Service Flexibility (TBD)
Vendor design should not preclude future routing of third-party stabilized condensate to sour tanks with optional product-tank routing. SourcePath: same, line 382.

### R-19 — Vendor Document Boundary (FACT)
The vendor document register, submittals, and turnover records are tracked under **DEL-096-05 Vendor Document Turnover Package**, not under this deliverable. This deliverable produces the **vendor design basis and datasheet set** plus the physical equipment. `_CONTEXT.md` Anticipated Artifacts.

### R-20 — EPC Integration Review Interface (FACT)
The vendor package shall be reviewed by the EPC Integrator for integration acceptance per **DEL-096-06**. The vendor shall support review cycles, comment dispositioning, and document re-issue. `_CONTEXT.md` ResponsibleParty.

## Standards

| Standard | Applicability | Location |
|---|---|---|
| API 650, Welded Tanks for Oil Storage | Tank design, fabrication, inspection, testing | **TBD (not locally accessible)** |
| NACE MR0175 / ISO 15156 | Sour-service materials selection | **TBD (not locally accessible; not explicitly named in DBM slice)** — ASSUMPTION |
| SSPC / NACE surface preparation standards | External coating prep | **TBD (not locally accessible)** — ASSUMPTION |
| Applicable Canadian provincial codes (BC) for atmospheric storage | Site-specific compliance | **TBD** — ASSUMPTION |
| 26020-Package_Requirements.docx heading 48 | Project-specific package requirements | Referenced in `_CONTEXT.md`; **binary, not locally accessible** — see CT-05 |

## Verification

| Requirement | Verification Approach |
|---|---|
| R-1 | EPC Integrator review of vendor deviations register; traceability matrix vendor scope ↔ DEL-096-01/02 |
| R-2, R-3 | Inspection of tank quantity and capacity against final tank register; vendor datasheet review |
| R-4 | Vendor design package compliance check vs. API 650 (subject to standard access) |
| R-5 | Vendor datasheet review (insulation/heat tracing specification); cold-weather operability check |
| R-6 | Inspection of tank nozzle for VRU vapour tie-in; PVRV setpoint review |
| R-7, R-8 | Materials Selection Diagram review; MTR audit; coating compatibility test results (if any) |
| R-9 | Coating system specification review; manufacturer compatibility statement |
| R-10 | Vendor BOM review for absence of aluminum in wetted/vapour service |
| R-11, R-12 | Vendor foundation load drawing review; EPC civil acceptance |
| R-13 | Engineering change record audit against final tank register |
| R-14 | Document register check that all enumerated vendor documents have been issued |
| R-15 | ITP execution records; hydrotest report; NDE reports; coating holiday test report |
| R-16 | PVRV sizing calculation review; VRU header pressure compatibility check |
| R-17 | Materials/coating compatibility statement for methanol exposure |
| R-18 | Nozzle layout review demonstrating service flexibility |
| R-19 | DEL-096-05 turnover package completeness (separate deliverable) |
| R-20 | DEL-096-06 acceptance record (separate deliverable) |

## Documentation

The Package Vendor shall produce the following documentation set as part of this deliverable (per `_CONTEXT.md` Anticipated Artifacts and R-14):

- Vendor design basis (cover document tying tank design to EPC SOW + Package Datasheet).
- Process datasheet (per tank service).
- Mechanical/strength datasheet (per tank).
- Materials Selection Diagram and MTR list.
- Coating system specification.
- Nozzle schedule and GA drawings.
- Foundation load drawings.
- Weld map and NDE/ITP plan.
- Hydrostatic test procedure and acceptance record.
- Tank nameplate/marking detail.

Vendor document register-level governance (submittal numbering, transmittal logs, turnover index) is **DEL-096-05** scope, not this deliverable.
