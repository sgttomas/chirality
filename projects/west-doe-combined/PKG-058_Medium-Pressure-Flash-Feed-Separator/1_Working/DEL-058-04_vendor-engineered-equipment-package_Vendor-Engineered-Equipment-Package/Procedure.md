# Procedure — DEL-058-04 Vendor Engineered Equipment Package (Medium Pressure Flash Feed Separator)

## Purpose

Operational procedure to **produce** the Vendor Engineered Equipment Package: vendor engineering, design, fabrication/supply, and physical delivery of the MPFF separator package, anchored to EPC inputs and subject to EPC integration review.

## Prerequisites

- EPC Scope of Work (`DEL-058-01`) issued by EPC Integrator. [Source: `_CONTEXT.md`; decomposition row 71]
- EPC Package Datasheet (`DEL-058-02`) issued by EPC Integrator. [Source: `_CONTEXT.md`]
- Accessible source-of-record materials:
  - DBM-Deepcut `4-25_Deepcut_DBM.md`
  - DBM-Comp_and_Liquids `3-25_Comp_and_Liquids_DBM.md`
  - `_REFERENCES.md`, `_CONTEXT.md` (deliverable-local)
- ASSUMPTION: Upstream declared dependencies are not yet enumerated in `_DEPENDENCIES.md` ("None declared during PREPARATION"). Vendor design must not begin under a final-issue assumption until EPC inputs are confirmed issued. [Source: `_DEPENDENCIES.md`]

## Steps

1. **Receive and confirm EPC inputs.**
   - Confirm receipt of `DEL-058-01` (Scope of Work) and `DEL-058-02` (Package Datasheet) at issued state.
   - Log any TBDs flagged in those documents (especially MPFF inlet temperature, low/high pressures, and per-separator flow values). [Source: DBM-Deepcut MPFF Operating and Capacity Basis]

2. **Develop vendor design basis.**
   - Restate the source-anchored attributes (design pressure 1724 kPag; minimum 10 minutes liquid residence; Mistex internals; no internal coating; -40 deg C ambient). [Source: DBM-Deepcut; DBM-Comp_and_Liquids]
   - Document open-item register for all TBDs from the EPC Package Datasheet and DBM (heater bundle disposition; MPFF inlet temperature; low/high pressure; per-MPFF flows; relief routing). [Source: DBM-Deepcut MPFF feed conditions; Conflict C-058-04-001 in `Guidance.md`]
   - Capture sparing basis (2 x 100% normal; no spare for line-pack) and isolation philosophy. [Source: DBM-Deepcut Sparing table; MPFF and Stabilizer Train Relationship]

3. **Engineer the vessels and heater bundle (conditional).**
   - Vessels V-7110-1 and V-7310-1: design to 1724 kPag, 10 minutes residence between weir and NLL-interface, Mistex internals, no internal coating, with the assumed 40 deg C design operating temperature carried as ASSUMPTION pending confirmation. [Source: DBM-Deepcut MPFF Operating and Capacity Basis; MPFF feed conditions]
   - Heater bundle E-7120-1 (and parallel): if retained, U-bundle/BKU-type with heat medium on tube side, sized to original basis (140 deg F in MPFF, 87 deg F at 50 psig downstream LP flash feed, 10% excess surface area for line-pack). Preserve vessel nozzle provisions even if bundle disposition is pending. [Source: DBM-Deepcut MPFF feed conditions]

4. **Engineer pressure-control, purge, methanol-injection, and blowdown interfaces.**
   - Overhead vapour routing to SOC third-stage suction; pressure regulation to keep MPFF above downstream stabilizer flash/feed separator.
   - LP fuel-gas purge regulated for both normal pressure floor and sour-gas sweep service.
   - Methanol injection nozzle and piping upstream of MPFF inlet LCV (safeguard retained). [Source: DBM-Deepcut MPFF feed conditions]
   - Automated blowdown valve specified. Relief routing to be confirmed against `DEL-058-02` (Conflict C-058-04-001).

5. **Design the package building and modular layout.**
   - Self-framing building enclosing instrumentation and one end of the vessel (mirrors inlet-separator pattern). [Source: DBM-Deepcut MPFF feed conditions]
   - Assign equipment to MPFF modules 710-1 and 730-1 (shop-shipped). [Source: DBM-Deepcut Module/Shop table]
   - Apply -40 deg C ambient discipline across buildings, panels, instrumentation, field devices, and materials. [Source: DBM-Comp_and_Liquids site basis]

6. **Produce vendor documentation set.**
   - Datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, vendor document register. [Source: DBM-Comp_and_Liquids mechanical packaging discipline paragraph]

7. **Fabricate, factory-accept, and ship.**
   - Apply vendor jurisdictional pressure-vessel code certification (edition TBD pending `DEL-058-02`; see Conflict C-058-04-002).
   - Conduct FAT including automated blowdown valve and trip-logic exercising; capture FAT records.
   - Ship complete package and shipped-loose items to site for installation under `DEL-058-03`.

8. **Submit to EPC for integration review and acceptance.**
   - Submit vendor documentation set to `DEL-058-05` (Vendor Document Turnover) and support `DEL-058-06` (EPC Vendor Package Review and Acceptance) review activity.

## Verification

| Step | Check | Evidence |
|---|---|---|
| 1 | EPC inputs received at issued state; TBDs logged | EPC handoff transmittal; vendor open-item register |
| 2 | Vendor design basis covers all source-anchored attributes and explicitly lists TBDs | Vendor design basis document |
| 3 | Vessel design pressure, residence time, internals match source | Vessel datasheet; sizing calculation; internals drawing |
| 3 | Heater bundle disposition documented; nozzle provisions preserved if removed | Heater bundle decision record; vessel nozzle schedule |
| 4 | Overhead, purge, methanol, blowdown interfaces present on P&ID | P&ID review record |
| 5 | -40 deg C suitability demonstrated for buildings, panels, instruments, materials | Materials certs; low-temperature impact tests; building structural review |
| 6 | Required vendor documentation set produced | Vendor document register vs. checklist |
| 7 | Pressure-vessel code certification; FAT complete | Vessel code stamp / certificate; FAT report |
| 8 | Submission to EPC review accepted | EPC review log entry (handled in `DEL-058-06`) |

## Records

- Vendor design basis document
- Vessel datasheet and sizing calculations
- Heater bundle disposition record (retain/remove/de-rate)
- P&ID set and nozzle schedule
- Materials and coating basis (recording absence of internal coating with source citation)
- Cause-and-effect / blowdown trip logic record
- FAT report and pressure-vessel certification
- Vendor document register (also referenced by `DEL-058-05`)
- Open-item / TBD register transmitted to EPC for resolution

## Notes

- Final acceptance and integration sign-off is not in scope of this deliverable; it is `DEL-058-06`.
- Construction/installation/tie-in is not in scope; it is `DEL-058-03`.
- Turnover documentation aggregation is `DEL-058-05`.
