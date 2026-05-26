# Procedure — DEL-093-04 Vendor Engineered Equipment Package (Tanks, Water (API 650) 3-25)

## Purpose

Operational procedure for the **Package Vendor** to produce the engineered design and physical equipment for `PKG-093` (Tanks, Water (API 650) 3-25), and for the EPC Integrator to interface with the vendor through engineering, fabrication, shop test, and delivery readiness.

## Prerequisites

- `DEL-093-01_scope-of-work` (EPC Scope of Work) accepted/issued for vendor use.
- `DEL-093-02_package-datasheet` (EPC Package Datasheet) accepted/issued for vendor use.
- Source SOW rows SOW-0229, SOW-0230, SOW-0231, SOW-0232 are stable in `SCOPE_LEDGER.csv` (GATE-07 Final Published 2026-05-24 snapshot).
- Conflict Table items in `Guidance.md` (CONF-093-04-01..06) reviewed; for HRR items not yet ruled, vendor and EPC have agreed an interim posture.
- Local-access references: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (SEC-01, SEC-02, SEC-03, SEC-06).

## Steps

### Step 1 — Vendor Engineering Kick-Off

1.1 Vendor confirms receipt and currency of `DEL-093-01` and `DEL-093-02`.
1.2 Vendor establishes a design basis document for the package using SOW-0230/0231/0232 attributes and DBM §SEC-06 (line 421) as surrounding context. ASSUMPTION: Vendor flags departures from API 650 baseline as "Modified" clauses, deferring enumeration to EPC closure (CONF-093-04-06).
1.3 Vendor registers open items from the Conflict Table with the EPC Integrator and proposes interim postures.

### Step 2 — Detailed Mechanical Design

2.1 Tank shell, bottom, and roof sizing per API 650 Modified using design SG 1.25 (Guidance proposed authority for CONF-093-04-01) and design pressure of 32 oz (CONF-093-04-03 proposed authority).
2.2 Material selection qualified for -40 °C MDMT, including impact testing where required (REQ-093-04-005).
2.3 Nozzle schedule including inlet, outlet, vapour to VRU, blanket gas, vent, drain, manway, instrumentation, skim, and vacuum-truck connection (REQ-093-04-016; DBM §SEC-06 line 430).
2.4 Vent and vacuum-protection sizing per API 2000 (edition per CONF-093-04-05 proposed authority).
2.5 Insulation/heating interface design: penetrations, brackets, clearance plan for EPC-supplied insulation/heating (SOW-0231; "by others" boundary per SOW-0232).
2.6 Internal coating (Devchem 253) specification including surface preparation, application, cure, and inspection plan (SOW-0231).
2.7 Skim system design: Kennilworth-type HCL float, float SG ≤ 0.67, one per tank (SOW-0231).
2.8 Hold Item No. 2 detailed design until flow and operating temperature are closed (CONF-093-04-04).

### Step 3 — Design Review and Datasheet Issue

3.1 Vendor issues design basis, per-tank datasheets, GA drawings, and interface drawings to EPC Integrator for review.
3.2 Address EPC review comments and update vendor design.
3.3 Issue vendor datasheets and design basis "for fabrication" upon EPC concurrence.

### Step 4 — Material Procurement

4.1 Procure plate, nozzles, fittings, gaskets, and coating system materials with MTRs.
4.2 Verify materials against -40 °C MDMT qualification.
4.3 Record procurement evidence into the vendor document register (handoff to `DEL-093-05`).

### Step 5 — Fabrication

5.1 Welding per qualified WPS/PQR per API 650 Modified.
5.2 NDE per code/spec (RT/UT/MT/PT as applicable).
5.3 Bottom plate seam testing and shell weld inspection per API 650 Modified.
5.4 Surface preparation and Devchem 253 internal coating application; thickness and adhesion inspection.
5.5 Skim system installation and verification.

### Step 6 — Shop Testing

6.1 Hydrostatic / leak test per API 650 Modified provisions, interpreting "32 oz test pressure" per CONF-093-04-03 proposed authority.
6.2 Coating inspection (DFT, holiday/spark test) per Devchem 253 specification.
6.3 Nozzle dimensional checks; manway and access verification.

### Step 7 — Vendor Document Compilation

7.1 Compile final design basis, datasheets, calculations (API 650 Modified, API 2000 vent sizing, structural), GA drawings, interface drawings, weld and NDE records, coating records, MTRs, and shop test records.
7.2 Submit to `DEL-093-05_vendor-document-turnover-package` per the vendor document register.

### Step 8 — Delivery and Integration Handoff

8.1 Prepare tanks for shipment to site.
8.2 Provide handling, lifting, and on-site reassembly information.
8.3 Coordinate with EPC Integrator on site receipt and installation readiness (mounting, foundations, electrical/instrumentation, platforms, staircase — all by others per SOW-0232).
8.4 Support EPC review and acceptance activities under `DEL-093-06`.

## Verification

| Step | Verification | Source / Acceptance Reference |
|---|---|---|
| 1 | Design basis issued; Conflict Table acknowledged | Guidance Conflict Table; EPC review log |
| 2 | Calculations and drawings complete; -40 °C MDMT material qualification documented | REQ-093-04-003, 005 |
| 3 | EPC-reviewed datasheets and design basis "for fabrication" | Specification §Documentation |
| 4 | Material MTRs on file; impact testing where required | REQ-093-04-005 |
| 5 | WPS/PQR records; NDE reports; coating inspection records | REQ-093-04-003, 008 |
| 6 | Hydrotest / leak test records; coating DFT/holiday records | REQ-093-04-004, 008 |
| 7 | Complete vendor document submission accepted by `DEL-093-05` | `DEL-093-05` register |
| 8 | Delivery sign-off; EPC integration readiness | `DEL-093-06` acceptance checklist |

## Records

The following records shall be produced and retained:

- Vendor design basis (signed) and revision history.
- Final per-tank datasheets and GA/interface drawings.
- API 650 Modified design calculations.
- API 2000 vent / vacuum-protection calculations.
- WPS/PQR/welder qualifications.
- NDE reports (RT/UT/MT/PT) per applicable code clauses.
- Hydrostatic / leak test records (per CONF-093-04-03 interpretation).
- Coating qualification (PQR) and inspection records (Devchem 253).
- MTRs for plate, nozzles, fittings, and gaskets.
- Insulation/heating interface drawings (vendor side).
- Skim system fabrication and SG-verification records.
- Shipping/handling documentation.

All records flow into `DEL-093-05_vendor-document-turnover-package` and support `DEL-093-06_epc-vendor-package-review-and-acceptance`.
