# Specification: DEL-060-02 — Package Datasheet (Tank Farm Pump Building 4-25)

## Scope

This specification defines the normative requirements that the EPC Integrator's `Package Datasheet` deliverable must satisfy so that a third-party package vendor can execute package engineering, design, fabrication, and documentation for the **Tank Farm Pump Building 4-25** (`PKG-060`, RFQ `26020-01-PT-18-002`).

In scope:
- The package datasheet's information content and structure;
- The technical attributes, design conditions, and interface conditions the datasheet must communicate to the package vendor;
- Cross-references to project authoritative source materials.

Out of scope:
- Vendor's internal package engineering deliverables (covered by `DEL-060-04`).
- EPC review/acceptance of vendor deliverables (covered by `DEL-060-06`).
- Construction Work Package (`DEL-060-03`) and vendor turnover (`DEL-060-05`).
- Package-specific exclusions: none stated in source materials (`TBD` per PACKAGE_REGISTER row 85).

Source: `_CONTEXT.md` (Scope); PACKAGE_REGISTER row 85 (Exclusions field = "TBD; no package-specific exclusions stated").

## Requirements

### R1 — Identification fields (MUST)

The datasheet MUST identify, at minimum: DeliverableID, ParentPackageID (`PKG-060`), package name (`Tank Farm Pump Building 4-25`), RFQ tag (`26020-01-PT-18-002`), workbook row (85), discipline (Mechanical), and facility (`04-25 Deepcut`).
Source: PACKAGE_REGISTER row 85; `_CONTEXT.md`.

### R2 — Scope of supply (MUST)

The datasheet MUST enumerate the package vendor scope of supply, including quantity, configuration, and tag designators:
- 2 x condensate transfer pumps and motors (`P-9210-1`, `P-9220-1`); 2 x 150% of facility design flow of combined condensate product; both pumps capable of simultaneous operation;
- 2 x water transfer pumps and motors (`P-9290-1`, `P-9293-1`);
- 2 x sour-water treatment pumps (`P-9231-1`, `P-9232-1`);
- 2 x process water transfer pumps (`P-5317-1`, `P-5318-1`);
- 2 x fresh caustic transfer pumps (`P-6760-1`, `P-6765-1`);
- 1 x condensate recycle pump and motor with strainer (tag `TBD`).

Source: PACKAGE_REGISTER row 85; DBM-Deepcut lines 1671-1679, 2555, 2618-2622.

### R3 — Design conditions (MUST)

For each pump service, the datasheet MUST communicate the locally-supported design conditions:
- Condensate transfer pumps: 350 kPad (50 psid) differential to liquids hub; design NPSHR ≤ 0.75 m; motor sizing on inlet-stabilizer composition density at -40 °C startup (including potential JT-mode startup); minimum-flow control valve required for continuous pumping (DBM lines 1673-1679).
- Recycle / skim duties: 20 m3/h at 80 m TDH (TBC) (DBM lines 1671-1672).
- Operating conditions for water, sour-water, process-water, and fresh-caustic pumps: `location TBD` — not stated explicitly in locally accessible DBM slices; package vendor inputs and vendor data sheets to be developed.

### R4 — Interface conditions (MUST)

The datasheet MUST communicate the interface conditions for each interface type listed in PACKAGE_REGISTER row 85: Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; Area/Exterior Lighting; Cathodic Protection; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports.

### R5 — Source-of-truth references (MUST)

The datasheet MUST cite the authoritative source documents from which design conditions are derived:
- DBM-Deepcut `4-25_Deepcut_DBM.md` (specific section/line references);
- PACKAGE_REGISTER (Gate 7 snapshot) row 85;
- Workbook Packages row 85;
- 26020-Package_Requirements.docx, package heading 15;
- 26020-01-PT-RFQ-18-002-Tank_Farm_Pump.docx (Bid Docs / Budgetary).

### R6 — Vendor/EPC responsibility boundary (MUST)

The datasheet MUST state the responsibility boundary: package vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration).
Source: PACKAGE_REGISTER row 85.

### R7 — Module / construction basis (SHOULD)

The datasheet SHOULD reference the tank-farm pump module construction basis: shop-fabricated module designator `920-1` (DBM line 2817); electrical service from the 4.16 kV / 600 V General Area / Tank Farm / Process Electrical Building (DBM line 2925).

### R8 — TBD discipline (MUST)

Where source values are missing, the datasheet MUST mark the field `TBD` and identify the open item. Inferred values MUST be labelled `ASSUMPTION`.

## Standards

| Standard / Reference | Applicability | Local Access |
|---|---|---|
| API 2000 | Tank blanket-gas / vent sizing — cited in DBM tank-farm context (DBM line 1663) | Cited only; clauses not locally accessible — location TBD |
| API 610 / API 682 | Centrifugal pumps and shaft sealing | ASSUMPTION: customary basis for hydrocarbon and produced-water transfer pumps; not explicitly cited in DBM slice — location TBD |
| API 650 | Storage tanks (referenced for tank packages PKG-* (Tanks)) | Cited in DBM Package Roster (lines 2623, 2625, 2627, 2628); peripheral to pump package |
| Tourmaline West Doe Deepcut DBM (`4-25_Deepcut_DBM.md`) | Governing facility design basis | Locally accessible |
| PROJECT_DECOMP Gate 7 snapshot | Decomposition truth | Locally accessible |

## Verification

| Requirement | Verification |
|---|---|
| R1 | Inspection of datasheet identification block against PACKAGE_REGISTER row 85 and `_CONTEXT.md`. |
| R2 | Inspection — every pump service in source materials is listed with quantity and tag designators. |
| R3 | Inspection — design conditions traceable to specific DBM line numbers; `TBD` permitted where source is silent. |
| R4 | Inspection — every interface type in PACKAGE_REGISTER row 85 is addressed by the datasheet. |
| R5 | Inspection — references cited explicitly with `SourcePath` and `SectionRef` (or `location TBD`). |
| R6 | Inspection — responsibility boundary clause present and matches PACKAGE_REGISTER row 85 narrative. |
| R7 | Inspection — module and electrical-area references match DBM lines 2817 and 2925. |
| R8 | Inspection — open items use `TBD` or `ASSUMPTION` labels with provenance. |

## Documentation

Anticipated artifacts (`_CONTEXT.md`):
- Package technical datasheet;
- Vendor engineering handoff basis;
- Package interface requirements matrix;
- Source-supported equipment and design criteria.
