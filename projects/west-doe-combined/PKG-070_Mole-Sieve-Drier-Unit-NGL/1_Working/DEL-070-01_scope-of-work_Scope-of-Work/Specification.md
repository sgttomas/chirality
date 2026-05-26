# Specification — DEL-070-01 Scope of Work (PKG-070 Mole Sieve Drier Unit (NGL))

> Normative requirements for the EPC Integrator Scope of Work deliverable for
> the NGL Mole Sieve Drier Unit package (PKG-070). Requirements are derived
> from the GATE-07 PROJECT_DECOMP snapshot rows for `PKG-070`,
> `SOW-0145..SOW-0148`, and the 12 PKG-070 interface rows. Where a requirement
> would depend on the NGL-specific RFQ
> (`26020-01-PT-RFQ-22-003_NGL-Mole-Sieve-Dehy.docx`) or
> `26020-Package_Requirements.docx` heading 24 and those sources are not
> locally accessible as text slices, the requirement is marked **location
> TBD** or **TBD**.

## Scope

### In scope (this deliverable)
- The EPC Integrator's Scope of Work document for `PKG-070` Mole Sieve Drier
  Unit (NGL), covering: package identity, tagged-equipment/identity reference,
  package function and integration narrative, source-grounded boundaries,
  whole-facility integration narrative, and responsibility assignment record.
- The four anticipated artifacts listed in `_CONTEXT.md`:
  - Package scope of work
  - Tagged equipment and package identity list
  - Package function and integration narrative
  - Responsibility assignment record

### In scope (described package, summarized for SoW purposes)
- One NGL molecular sieve dehydration package, three-tower configuration
  (1 adsorbing / 1 regenerating / 1 standby), rated 2,385 m³/d (15,000 bbl/d),
  processing water-saturated C3+ NGL to <7 ppmw outlet water content.
- Major included equipment per SCOPE_LEDGER SOW-0147 (inlet pretreatment and
  free-water removal; three sieve vessels with 3A sieve and silica gel layer;
  regeneration-gas heating, cooling, three-phase scrubber, relief provisions;
  outlet particulate filtration; local instrumentation and moisture analyzer;
  heated enclosure where required).
- Package utility, electrical, flare, drain, and control-system tie-in
  provisions to package battery limits (SCOPE_LEDGER SOW-0147).

### Out of scope (excluded — by others)
- NGL mercaptan treating process package and caustic process-provider design
  (upstream).
- NGL storage bullets, NGL loading, LACT, and product export systems
  (downstream).
- Sales gas compressors and stabilizer overheads compressor package.
- Produced-water tank, produced-water drain header, and facility drain
  infrastructure beyond package nozzles/tie-ins.
- Flare header.

(Source: SCOPE_LEDGER SOW-0148.)

### Out of scope (deliverable boundary)
- Vendor engineering, design, fabrication, and physical supply of the
  equipment package — carried by DEL-070-04 Vendor Engineered Equipment
  Package (ASSUMPTION; mapping per DELIVERABLE_REGISTER PKG-070 rows).
- Detailed technical datasheet content for vendor handoff — carried by
  DEL-070-02 Package Datasheet.
- Construction work package — carried by DEL-070-03.
- Vendor document turnover — carried by DEL-070-05.
- EPC vendor package review and acceptance — carried by DEL-070-06.

## Requirements

### R-1 — Identity and traceability
- R-1.1 The Scope of Work SHALL identify the package by `PackageID = PKG-070`,
  Name "Mole Sieve Drier Unit (NGL)", Workbook row 74, WBS 01, and tracking
  number `26020-01-PT-22-003`. (Source: `PACKAGE_REGISTER.csv`.)
- R-1.2 The Scope of Work SHALL state the responsibility model: Package
  Vendor owns package engineering, package design, vendor documentation, and
  physical equipment; EPC Integrator owns facility integration, interfaces,
  tie-ins, constructability, procurement/construction coordination, and
  facility-level integration. (Source: `PACKAGE_REGISTER.csv` ResponsibilityModel;
  OBJ-004.)
- R-1.3 The Scope of Work SHALL cite the GATE-07 Final Published
  PROJECT_DECOMP snapshot as the authoritative decomposition basis.
  (Source: `_REFERENCES.md`.)

### R-2 — Package function and capacity
- R-2.1 The Scope of Work SHALL specify one (1) NGL molecular sieve
  dehydration package in three-tower configuration (1 adsorbing /
  1 regenerating / 1 standby). (Source: SCOPE_LEDGER SOW-0146.)
- R-2.2 The Scope of Work SHALL specify a package capacity of 2,385 m³/d
  (15,000 bbl/d) of water-saturated C3+ NGL. (Source: SCOPE_LEDGER SOW-0146.)
- R-2.3 The Scope of Work SHALL specify an outlet water content target of
  <7 ppmw in the dry NGL. (Source: SCOPE_LEDGER SOW-0146.)

### R-3 — Included equipment and functions
- R-3.1 The Scope of Work SHALL list, as included equipment, the items in
  SCOPE_LEDGER SOW-0147: inlet pretreatment and free-water removal (liquid/
  liquid coalescer(s) with coalesced water level control to produced water);
  three (3) sieve vessels with 3A molecular sieve and silica gel protective
  layer, complete with internals, valves, and drains; regeneration-gas
  heating, aerial cooler with automated warm-air recirculation louvers,
  automated intake louvers, and plenum heating bundle for winterization
  (split-header design); three-phase scrubber with mist pad; pressure relief
  provisions; outlet particulate filtration on dry NGL; local instrumentation
  and analyzer interface for one (1) moisture analyzer with vaporizing
  regulator for C3+ sampling; heated building/enclosure housing inlet gas
  coalescer, inline mixers, settling vessel, and regeneration gas scrubber
  as required by final heater/scrubber location and area classification.
- R-3.2 The Scope of Work SHALL state that 3A molecular sieve is required and
  identify the silica gel layer as protective against upstream liquid
  carryover. (Source: SCOPE_LEDGER SOW-0147; consistent with DBM SEC-06
  Molecular-Sieve Bed and Regeneration Basis adsorbent rule, ASSUMPTION for
  NGL service.)

### R-4 — Process design conditions
- R-4.1 The Scope of Work SHALL carry the adsorption-side design conditions
  from SCOPE_LEDGER SOW-0148 (per latest DBM SEC-07):
  - Inlet pressure: 1,978 kPag design (low/high TBC).
  - Outlet pressure: 1,943 kPag design (low/high TBC).
  - Inlet temperature: 29.7 °C (low) / 46.3 °C (design) / 51.8 °C (high).
  - Inlet water content: saturated at design inlet conditions and flow.
- R-4.2 The Scope of Work SHALL state the bed pressure-drop limits:
  start-of-life < 4 psid (27.6 kPad); end-of-life including vessel nozzles
  < 10 psid. (Source: SCOPE_LEDGER SOW-0148.)
- R-4.3 The Scope of Work SHALL state the preliminary adsorption cycle of
  24 hours and mark the draining/heating ramp/regeneration pre-heat-hold/
  heating/cooling/filling/standby/total regeneration cycle as **TBC by
  vendor**. (Source: SCOPE_LEDGER SOW-0148.)
- R-4.4 Regeneration-side process design conditions are **TBD** (the source
  slice in SCOPE_LEDGER SOW-0148 terminates at "Regeneration side. Design
  conditions:" without enumerated values). Resolution requires
  `26020-Package_Requirements.docx` heading 24 or
  `26020-01-PT-RFQ-22-003_NGL-Mole-Sieve-Dehy.docx` (location TBD — not
  locally accessible).

### R-5 — Battery limits and tie-ins
- R-5.1 The Scope of Work SHALL define package battery limits and require
  package utility, electrical, flare, drain, and control-system tie-in
  provisions at the package battery limits. (Source: SCOPE_LEDGER SOW-0147.)
- R-5.2 The Scope of Work SHALL list the twelve (12) applicable facility
  interface types for PKG-070: Process Piping; Relief / Flare / Vent;
  Drain / Containment; Electrical Power; EHT; Grounding / Bonding;
  Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services;
  Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations /
  Supports. (Source: `INTERFACE_REGISTER.csv` rows for PKG-070;
  `PACKAGE_REGISTER.csv` InterfaceTypes.)

### R-6 — Exclusions ("by others")
- R-6.1 The Scope of Work SHALL state the "by others" exclusions verbatim or
  in faithful paraphrase from SCOPE_LEDGER SOW-0148 (upstream mercaptan
  treating; downstream NGL storage/loading/LACT/export; sales gas and
  stabilizer overheads compressors; produced-water tank/drain header and
  facility drain infrastructure beyond nozzles/tie-ins; flare header).

### R-7 — Whole-facility integration narrative
- R-7.1 The Scope of Work SHALL include a whole-facility integration
  narrative addressing how the NGL Mole Sieve Drier Unit integrates with
  upstream NGL mercaptan treating, downstream NGL storage/loading/LACT,
  facility utilities, flare, drain, electrical power, controls, and fire &
  gas systems. (Source: `_CONTEXT.md` Scope; OBJ-003, OBJ-007, OBJ-009.)
- R-7.2 The narrative SHALL identify facility-level interfaces and call out
  the responsibility split at each. (ASSUMPTION: consistent with OBJ-004 and
  the responsibility model.)

### R-8 — Responsibility assignment record
- R-8.1 The Scope of Work SHALL include a responsibility assignment record
  identifying, for each package function and interface, the responsible
  party (Package Vendor or EPC Integrator) consistent with R-1.2.
  (Source: `_CONTEXT.md` Anticipated Artifacts; OBJ-004.)

### R-9 — Tagged equipment and package identity list
- R-9.1 The Scope of Work SHALL include a tagged equipment and package
  identity list at the level available in the source basis. Per-vessel tag
  numbers are **TBD** in accessible sources and will be issued/refined in
  DEL-070-02 Package Datasheet. (Source: `_CONTEXT.md` Anticipated Artifacts;
  ASSUMPTION on hand-off split.)

### R-10 — Source citation
- R-10.1 Every substantive design value, capacity, condition, or exclusion in
  the Scope of Work SHALL cite either the GATE-07 PROJECT_DECOMP row
  (`PACKAGE_REGISTER.csv`, `SCOPE_LEDGER.csv`, `INTERFACE_REGISTER.csv`) or
  the underlying source document with "location TBD" when the source is not
  locally accessible. (Governance: K-PROV-1.)

## Standards

| Standard / Code basis | Statement | Source |
|---|---|---|
| 3A molecular sieve mandatory; 4A/5A not permitted (process-gas service) | The DBM rule prohibits 4A/5A sieves because larger pore sizes adsorb H2S and cause sulphur spikes in regeneration. Treated as ASSUMPTION for the NGL package (analogous service); confirm in NGL RFQ when accessible. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-06 Molecular-Sieve Bed and Regeneration Basis (location TBD for direct NGL citation) |
| Sour-service materials (NACE) | Carried at the project level via OBJ-009 sour-service safety/relief/flare/drain/containment/fire&gas requirements; NGL-package material-class specification is **TBD** in accessible sources. | OBJ-009; location TBD |
| Area classification | Heated enclosure required "as required by final heater/scrubber location and area classification" — specific classification document **location TBD**. | SCOPE_LEDGER SOW-0147 |
| Codes/standards applicable to vessels, piping, electrical, I&C, fire & gas | **TBD** — not enumerated in accessible source slices for this package. | TBD; see DEL-070-02 |

## Verification

| Requirement | Verification approach |
|---|---|
| R-1.x Identity and traceability | Cross-check with `PACKAGE_REGISTER.csv` row `PKG-070` and DELIVERABLE_REGISTER row `DEL-070-01_scope-of-work` (GATE-07 snapshot). |
| R-2.x Function and capacity | Cross-check against SCOPE_LEDGER SOW-0146 verbatim. |
| R-3.x Included equipment | Cross-check against SCOPE_LEDGER SOW-0147 itemized list. |
| R-4.1–R-4.3 Process design conditions | Cross-check against SCOPE_LEDGER SOW-0148. |
| R-4.4 Regeneration conditions | Pending vendor RFQ source slice; verification deferred to DEL-070-02 / DEL-070-04. |
| R-5.x Battery limits and interfaces | Cross-check against `INTERFACE_REGISTER.csv` rows for PKG-070 (12 rows) and SCOPE_LEDGER SOW-0147. |
| R-6.x Exclusions | Cross-check against SCOPE_LEDGER SOW-0148 verbatim. |
| R-7.x Integration narrative | EPC Integrator review against OBJ-001, OBJ-003, OBJ-007, OBJ-009 mapping. |
| R-8.x Responsibility assignment | EPC Integrator review against PACKAGE_REGISTER ResponsibilityModel and OBJ-004. |
| R-9.x Tagged equipment list | Reviewed at SoW level; finalized in DEL-070-02 Package Datasheet. |
| R-10.x Source citation | Documentation review — every substantive claim has a source pointer or TBD marker. |

## Documentation

Required artifacts of this deliverable (from `_CONTEXT.md` Anticipated Artifacts):
- Package scope of work document (this deliverable's primary artifact).
- Tagged equipment and package identity list.
- Package function and integration narrative.
- Responsibility assignment record.

Downstream deliverables that consume this Scope of Work (from
`SCOPE_LEDGER.csv` SOW-0145..SOW-0148):
- DEL-070-02 Package Datasheet (vendor handoff technical basis).
- DEL-070-03 Construction Work Package.
- DEL-070-04 Vendor Engineered Equipment Package.
- DEL-070-05 Vendor Document Turnover Package.
- DEL-070-06 EPC Vendor Package Review and Acceptance.
