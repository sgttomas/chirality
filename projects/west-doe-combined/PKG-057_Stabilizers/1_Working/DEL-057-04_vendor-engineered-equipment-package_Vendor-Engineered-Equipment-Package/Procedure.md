# Procedure — DEL-057-04 Vendor Engineered Equipment Package (Stabilizers)

## Purpose

Operational procedure to **produce** the Vendor Engineered Equipment Package for PKG-057 Stabilizers: from receipt of the EPC handoff through engineering/design, fabrication/supply, FAT, and delivery of the physical equipment package to the EPC Integrator for site integration. Source: `_CONTEXT.md`; SOW-0177; `DELIVERABLE_REGISTER.csv` row DEL-057-04.

## Prerequisites

### Inputs from EPC Integrator (Upstream)
- **DEL-057-01 Scope of Work** issued and accepted (anchors tagged equipment, package function, source basis, boundaries, integration narrative). Source: `DELIVERABLE_REGISTER.csv` row DEL-057-01.
- **DEL-057-02 Package Datasheet** issued and accepted (technical handoff: package datasheet, vendor engineering handoff basis, interface requirements matrix). Source: `DELIVERABLE_REGISTER.csv` row DEL-057-02.
- RFQ `26020-01-PT-RFQ-17-005_Inlet Stabilizers_R0.docx`. Source: `PACKAGE_REGISTER.csv` row PKG-057.
- `26020-Package_Requirements.docx` package heading 12 (binary; clause text **location TBD**).

### Reference Basis
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §SEC-04 "Stabilizer Design and Operating Basis" (L676–L710).
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` for this deliverable.

### Declared Dependencies
- Upstream / Downstream: none declared in `_DEPENDENCIES.md` (PREPARATION state). Vendor should not treat absence of declared dependencies as absence of integration interfaces; SOC (PKG-050) is an integration counterpart. Source: `_DEPENDENCIES.md`.

## Steps

### Step 1 — Receive and reconcile EPC handoff
1. Confirm DEL-057-01 (SOW) and DEL-057-02 (Package Datasheet) are both at an accepted state.
2. Cross-check the EPC Package Datasheet values against DBM §SEC-04 L676–L710. Log any discrepancies in the package Conflict Table (see Guidance.md) before continuing.
3. Confirm RFQ scope (`26020-01-PT-RFQ-17-005_Inlet Stabilizers_R0.docx`) is aligned with the EPC handoff. Resolve disagreements with the EPC Integrator before issuing the package design basis. Source: `PACKAGE_REGISTER.csv` row PKG-057.

### Step 2 — Issue vendor package design basis and datasheet set
1. Produce vendor package design basis covering:
   - Three (3) Inlet Stabilizer Packages on a 3 × 40 % basis at 1,272 m³/d (8,000 bbl/d) per unit. Source: SOW-0179; DBM L682–L684.
   - Stabilizer column: trayed reboiled distillation column, 20 floating-valve trays, 3:1 turndown. Source: SOW-0179; DBM L678.
   - Operating conditions (flash feed separator 345 kPag / 30.6 °C; column inlet 71 °C; min column pressure 793 kPag). Source: SOW-0180.
   - Design conditions (flash feed separator 1,724 kPag / 60 °C; feed/bottoms exchanger 16.7 °C minimum approach). Source: SOW-0180; DBM L706.
   - Product specifications: vapour pressure < 85 kPaa (ASTM D6377); density 650–775 kg/m³; CAPP butane equivalent < 5 vol %. Source: DBM L484, L685–L687.
2. Produce vendor datasheets for: stabilizer column, flash feed separator, feed pumps (2 × 100 %), feed/bottoms exchanger, reboiler, product cooler, basket strainers, instrumentation (minimum 1 LIT + 1 TIT per SOW-0179).
3. Submit design basis and datasheet set to EPC Integrator for integration review (per `_CONTEXT.md` ResponsibleParty). Source: `_CONTEXT.md`.

### Step 3 — Detailed engineering and design
1. Confirm reboiler heat-medium temperature with the heat-medium utility owner (open item per DBM L706). If TBD, hold reboiler thermal design until resolved.
2. Confirm flash-feed retention time target — 15 min (SOW-0180) vs. "TBC" (DBM L704) — with the EPC Integrator. Hold ≥10 min between LLL and HLL as a non-negotiable floor.
3. Rule on product cooler elevation (grade vs. 25 ft) based on flare-header loading analysis. Source: DBM L708.
4. Finalize pump selection, strainer mesh, and seal type. Source: DBM L706.
5. Issue P&IDs, GAs, mechanical/electrical/instrumentation datasheets, control narrative, and HAZOP-ready documentation for the package.
6. Confirm interface routing:
   - Stabilizer overhead vapour → SOC second-stage suction (pressure-controlled). Source: DBM L678.
   - Flash/feed overhead vapour → SOC first-stage suction (pressure-controlled). Source: DBM L704.
   - Flash/feed relief and blowdown → HP flare. Source: DBM L704.
   - Stabilized product → NGL mercaptan treating unit (with manual diversion to condensate slop tank). Source: DBM L710.

### Step 4 — Fabrication / supply
1. Procure long-lead items (stabilizer column shells, feed pumps, reboiler, product cooler) against issued datasheets.
2. Fabricate skid(s) and modular package(s), with internal coatings applied (Devchem 253 on flash/feed separator per DBM L704).
3. Seal-weld reboiler tubes to the tubesheet (DBM L706).
4. Apply quality controls per vendor QMS and project ITP.

### Step 5 — Factory acceptance test (FAT)
1. Hydrotest pressure vessels and exchangers.
2. Mechanical run test the stabilizer feed pumps; confirm VFD compatibility (SOW-0180).
3. Loop-check instrumentation (minimum 1 LIT + 1 TIT per SOW-0179; full instrument index TBD).
4. Demonstrate control logic for the flash/feed inlet LCV low-select controller (closes on high level, high pressure, or high overhead flow). Source: DBM L704.
5. Functional-test the stabilizer product cooler fan VFD turndown.
6. Issue FAT report to EPC Integrator.

### Step 6 — Delivery and turnover preparation
1. Prepare the package for shipping per the EPC scope-by-others provisions: shipping packages, installation on foundations, tie-in piping, electrical connection, mounting, and DCS integration are out of vendor scope. Source: SOW-0180.
2. Coordinate with the EPC Integrator for site receipt, lifting, and pre-installation inspection.
3. Hand off the vendor documentation register, submittals, and turnover records to the sibling deliverable `DEL-057-05_vendor-document-turnover-package`. Source: `DELIVERABLE_REGISTER.csv` row DEL-057-05.
4. Support EPC Integrator review and acceptance under sibling deliverable `DEL-057-06_epc-vendor-package-review-and-acceptance`. Source: `DELIVERABLE_REGISTER.csv` row DEL-057-06.

## Verification

| Check | Method | Source |
|---|---|---|
| Three (3) stabilizer packages supplied at 1,272 m³/d each | Equipment list audit; FAT count | SOW-0179; DBM L683 |
| Column has 20 floating-valve trays, 3:1 turndown | Vendor mechanical datasheet review; internals inspection at FAT | SOW-0179; DBM L678 |
| Vessel design pressures meet 1,724 kPag (flash feed) and 793 kPag (column min) | Vessel datasheet and PSV calc review | SOW-0180 |
| Feed/bottoms exchanger meets 16.7 °C minimum approach | Heat-exchanger thermal datasheet review | SOW-0180; DBM L706 |
| Product cooler 130 % excess area and 110 °F (43.3 °C) outlet | Cooler thermal datasheet review; performance test | SOW-0180; DBM L708 |
| Product meets vapour pressure (< 85 kPaa, D6377), density 650–775 kg/m³, C4- < 5 vol % | Performance test with lab sampling at startup | DBM L685–L687 |
| Flash/feed inlet LCV uses low-select on level/pressure/overhead flow | Control narrative review; FAT logic test | DBM L704 |
| Devchem 253 internal coating on flash/feed separator | Coating ITP and QA record | DBM L704 |
| Vendor scope excludes interconnecting piping, DCS, foundations, MCC supply, installation | Scope split review with EPC Integrator | SOW-0180 |

## Records

- Vendor package design basis and datasheet set (issued in Step 2).
- Detailed engineering deliverables (P&IDs, GAs, mechanical/electrical/instrument datasheets, control narrative, HAZOP record).
- Fabrication / inspection records (material test certs, weld records, NDE, coating ITP).
- FAT report (hydrotest, run test, loop check, control logic demo, product performance demo).
- Shipping and delivery records.
- Open items / TBD log (reboiler heat-medium temperature; flash/feed retention time TBC; product cooler elevation ruling; full instrument index; sparing/operating split; stabilizer overhead disposition under revised downstream configuration).
- Handoffs to DEL-057-05 (vendor document turnover) and DEL-057-06 (EPC vendor package review and acceptance).
