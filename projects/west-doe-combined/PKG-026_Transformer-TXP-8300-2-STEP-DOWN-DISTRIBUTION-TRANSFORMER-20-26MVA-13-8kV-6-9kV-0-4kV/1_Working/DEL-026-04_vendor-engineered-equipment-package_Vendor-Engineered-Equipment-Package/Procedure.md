# Procedure: DEL-026-04 — Vendor Engineered Equipment Package (PKG-026 TXP-8300-2)

## Purpose

Operational procedure to produce, accept, and turn over the Vendor Engineered Equipment Package production unit for PKG-026 (step-down distribution transformer TXP-8300-2). Steps cover both producing the vendor work product and supporting EPC integration review.

## Prerequisites

- **Declared upstream dependencies:** None declared during PREPARATION (`_DEPENDENCIES.md`). The EPC anchors (DEL-026-01 Scope of Work and DEL-026-02 Package Datasheet) are functional prerequisites per DELIVERABLE_REGISTER.csv even though not in the declared upstream list.
- **Declared downstream dependencies:** None declared (`_DEPENDENCIES.md`). Functional downstreams include DEL-026-03 (Construction Work Package), DEL-026-05 (Vendor Document Turnover Package), and DEL-026-06 (EPC Vendor Package Review and Acceptance).
- **References available:** Gate 7 snapshot (`_REFERENCES.md`); DBM electrical slices (`3-25_Comp_and_Liquids_DBM.md`, `4-25_Deepcut_DBM.md`); PACKAGE_REGISTER.csv; DELIVERABLE_REGISTER.csv.
- **Open items resolved (or carried as TBD):** see `Guidance.md` Conflict Table and HRR list.

## Steps

### Production steps (vendor side)

1. **Receive EPC anchors.** Confirm DEL-026-01 Scope of Work and DEL-026-02 Package Datasheet are issued and accepted. (If not, surface as blocking input; do not proceed to engineering.)
2. **Resolve identity envelope.** Reconcile winding topology, voltage class allocation, and cooling class (CONF-026-04-001, -002) against DEL-026-02. Record reconciliation in vendor design basis.
3. **Prepare vendor design basis.** Document ratings (20/26 MVA), voltage classes (13.8/6.9/0.4 kV), cooling class, BIL, impedance, vector group, tap range, ambient/altitude, sound, enclosure rating, NGR rating per site grounding conventions, accessory list, and control interface scheme. Cite sources or mark TBD.
4. **Prepare vendor datasheet set.** Issue transformer nameplate datasheet, NGR datasheet, accessory datasheets, and sensor/control datasheets.
5. **Prepare general arrangement and outline drawings.** Cover footprint, lifting points, oil containment (if applicable), maintenance clearances, and the seven PKG-026 interface types (PACKAGE_REGISTER.csv PKG-026).
6. **Prepare electrical schemes.** Single-line, protection, control, alarm, and metering schemes consistent with site grounding (100 A / 10 s NGR on 6.9 kV; 5 A HRG on 600 V where applicable).
7. **Prepare interface drawings.** Document each applicable interface type so that EPC tie-in design can proceed (Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Communications/Network; Maintenance Access; Structural/Foundations/Supports).
8. **Submit for EPC integration review.** Issue the design basis, datasheet set, and drawings for EPC review (handled within DEL-026-06).
9. **Fabricate / supply the equipment.** After accepted design, fabricate the transformer and assemble the package.
10. **Run FAT.** Execute factory acceptance tests per the governing standards (TBD — see CONF-026-04-004) and the vendor datasheet set. Issue FAT report.
11. **Prepare shipping, handling, storage, installation instructions.** Issue to EPC for use in DEL-026-03 Construction Work Package.
12. **Transfer vendor documentation.** Route all vendor documents through DEL-026-05 Vendor Document Turnover Package; do not retain originals in this production unit.

### Integration review steps (EPC side, summarized)

13. **EPC reviews vendor design basis and datasheet set** against DEL-026-01 SOW and DEL-026-02 Package Datasheet; records review log under DEL-026-06.
14. **EPC reviews vendor interface drawings** against facility integration design; flags interface gaps.
15. **EPC participates in / witnesses FAT** as required.
16. **EPC issues acceptance evidence** under DEL-026-06 once the package satisfies the EPC anchors and integration requirements.

## Verification

| Verification check | Method | Pass criterion |
|---|---|---|
| Package envelope matches EPC anchors | Document review (vendor design basis vs DEL-026-01/02) | No unsurfaced deviations |
| Equipment identity is correct | Nameplate inspection at FAT and on site | TXP-8300-2, 20/26 MVA, 13.8/6.9/0.4 kV per DEL-026-02 |
| Grounding scheme correct | Vendor scheme review; site IR/continuity test | 100 A / 10 s NGR on 6.9 kV winding(s); 5 A HRG on 600 V where applicable |
| Interface drawings cover all applicable types | Checklist against PACKAGE_REGISTER.csv PKG-026 interface types | All 7 interface types addressed |
| FAT passed | FAT report review | All test cases pass per governing standards |
| Vendor documentation transferred | DEL-026-05 register entry | Documents listed in turnover register |
| Integration acceptance issued | DEL-026-06 acceptance record | Acceptance record cites this deliverable's contents |

## Records

- Vendor package design basis (vendor-controlled document).
- Vendor datasheet set (transformer, NGR, accessories, sensors, controls).
- General arrangement, outline, single-line, protection, control, and interface drawings.
- FAT procedures and FAT report.
- Shipping/handling/storage/installation instructions (issued to DEL-026-03).
- Vendor document register entries (under DEL-026-05).
- EPC review log and acceptance evidence (under DEL-026-06).
- This deliverable's `_STATUS.md` History entries and `_run_records/` task runs.
