# Procedure — DEL-050-04 Vendor Engineered Equipment Package (Stabilizer Overheads Compressors)

This procedure describes the operational steps the Package Vendor follows to **produce and deliver** the Vendor Engineered Equipment Package for PKG-050. It does not describe field operation of the SOC; that is covered in operating documentation produced under DEL-050-05 (Vendor Document Turnover Package) and operated under the EPC / Operator's site procedures.

## Prerequisites

| # | Prerequisite | Source |
|---|---|---|
| 1 | Accepted EPC Scope of Work (DEL-050-01) covering SOW-0173, SOW-0174, SOW-0175, SOW-0176. | `_CONTEXT.md`; `SCOPE_LEDGER.csv` |
| 2 | Accepted EPC Package Datasheet (DEL-050-02) carrying owner / EPC values for capacity, pressures, temperatures, and interface envelope. | `PACKAGE_REGISTER.csv` row PKG-050 |
| 3 | Vendor RFQ documentation set (`26020-01-PT-RFQ-12-005_Stabilizer_OH_Comp.docx`, package tag `26020-01-PT-12-005`). | `PACKAGE_REGISTER.csv` row PKG-050 (Word Source Basis) |
| 4 | Owner / EPC project specifications and applicable codes (NEMA MG 1; CSA / provincial pressure registration; project mechanical, electrical area classification, fire & gas, HVAC, EHT specs). | SOW-0176; **location TBD** for specific spec documents |
| 5 | No declared upstream deliverable-local dependencies in `_DEPENDENCIES.md`; declared-edge constraints absent. | `_DEPENDENCIES.md` |
| 6 | SOC design basis confirmed against DBM §SEC-04 L712–L828 (process duty, stage table, MAWP, composition, controls). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |

## Steps

### Step 1 — Receive and confirm package scope
1.1 Receive and log the EPC Scope of Work, Package Datasheet, and RFQ documents.
1.2 Confirm SOW-0173 through SOW-0176 scope items are fully reflected in the issued RFQ and that no scope is silently transferred to "by others" beyond SOW-0176.
1.3 Issue a scope-confirmation memo to the EPC Integrator. **Records:** signed scope-confirmation memo.

### Step 2 — Establish package design basis
2.1 Lock the process design basis: stage capacities, suction / discharge pressures, design temperatures, cooler discharge temperatures, gas composition. Source: DBM L734–L805.
2.2 Issue Vendor package design basis document; flag every TBC / TBD item back to the EPC Integrator with a proposed disposition (see Guidance Conflict Table).
2.3 Confirm sparing philosophy (2 × 100 %) and confirm both packages must be capable of parallel operation during line-pack / upset. Source: DBM L718, L728.
**Records:** Vendor design basis document; TBC / TBD log.

### Step 3 — Compressor frame and cylinder selection
3.1 Configure Ariel KBC/6 four-stage reciprocating package to match the design stage table.
3.2 Confirm cylinder sizing covers the recycle case (100 % recycle at 40 % speed with low discharge pressure).
3.3 Confirm intermediate-stage MAWPs are bounded by 1,723 kPag (Stage 1 suction) and 9,101 kPag (Stage 4 discharge), and document the chosen values. Source: DBM L766–L773, L826.
**Records:** compressor selection sheet; MAWP cascade table.

### Step 4 — Driver / VFD design
4.1 Specify and procure 4,000 V, 3-phase, 60 Hz, 8-pole, ~891 rpm induction motor rated 2,700 hp / 2,013 kW with ~10 % excess power.
4.2 Confirm VFD compatibility delivering 3 : 1 turndown.
4.3 Confirm enclosure (TBD; TEFC quote requested), Class F / Class B insulation, non-sparking bidirectional cooling fans, NEMA MG 1 labelling, and exclusion of Toshiba motors.
4.4 Confirm electric circulating lube-oil heater and supplemental lube-oil pump provisions per OEM.
**Records:** motor and VFD datasheets; motor + drive harmonics study; lube-oil-system schematic.

### Step 5 — Aerial cooler design
5.1 Configure four common-frame AP-661 (modified) aerial intercoolers.
5.2 Include warm-air recirculation, plenum heater, automated louver control with electro-pneumatic transducers and TE feedback to the SOC control system.
5.3 Run dewpoint check at each stage; the Stage 2 margin (87.78 °C vs. 85.31 °C dewpoint) must be re-checked and corrected if narrow under off-design composition.
**Records:** cooler thermal performance datasheet; dewpoint margin report.

### Step 6 — Suction scrubbers and separation pot
6.1 Configure 1st-stage scrubber as two-phase with cyclonic element; Stages 2–4 as two-phase with demister; all using mist pads (not mesh/vane).
6.2 Size each scrubber with imperial K factor ≤ 0.25 plus pressure deration; confirm capacity over off-design range; document 0.61 SG inlet liquid density assumption explicitly.
6.3 Configure packing vent / drain separation pot (two-phase, DP 101 kPag) and vacuum pump.
**Records:** scrubber and separation-pot datasheets; capacity-range tables.

### Step 7 — Valves and recycle
7.1 Specify one SOC suction PCV per side-stream service plus 1st-stage inlet PCV; ET-type preferred; <2 psid at 100 % open; fail closed.
7.2 Specify single recycle control valve sized for 100 % recycle at 40 % speed and low discharge pressure; full-port manual isolation on outlet; fail position TBC (raise to EPC Integrator for ruling).
7.3 Specify automated quarter-turn full-port ball valve for start-up bypass.
**Records:** valve datasheets; recycle sizing calculation.

### Step 8 — Packing vents, drains, and purge
8.1 Header cylinder packing vents and drains to a seal pot.
8.2 Route packing vent vapour to the VRU suction header; route collected liquids for local truck-out.
8.3 Route suction-scrubber liquids to the H2O/HCL drain header.
8.4 Provide manual sweet-gas purge connection at 1st-stage suction immediately downstream of inlet PCV.
**Records:** P&ID extract showing drain/vent routing.

### Step 9 — Controls and BoP interface
9.1 Configure unit control panel to manage package-internal control and package blowdown.
9.2 Specify BoP-controlled suction-header blowdowns upstream of side-stream PCVs and document the I/O interface to the facility DCS.
9.3 Issue control narrative and cause-and-effect.
**Records:** control narrative; C&E matrix; I/O list with BoP interface section.

### Step 10 — Building and modularisation
10.1 Configure self-framing building enclosing instrumentation.
10.2 Design for modular shop assembly and disassembly into three pieces for shipping.
10.3 Assess single-piece shipment option (TBC) and document outcome.
**Records:** GA drawing; ship-loose list; transportation study.

### Step 11 — Fabrication, FAT, and pre-shipment
11.1 Fabricate / assemble per approved design.
11.2 Conduct FAT covering compressor mechanical run, motor + VFD functional test, scrubber pressure tests, cooler functional test, control panel I/O test, and recycle valve stroke.
11.3 Address punch-list to closure.
**Records:** FAT report; pressure-test records; punch list closure record; quality dossier.

### Step 12 — Documentation turnover and shipment
12.1 Assemble vendor documentation package (datasheets, GAs, P&IDs, electrical one-line, motor / VFD datasheets, control narrative, C&E, MOC list, weld map, hydrotest, FAT / SAT procedures, O&M manuals, spare-parts list). This feeds DEL-050-05.
12.2 Issue documentation to the EPC Integrator for review (DEL-050-06).
12.3 Disassemble into three shipping pieces (or single piece if approved per Step 10.3) and ship.
**Records:** turnover index; shipment release notice; signed bill of lading.

## Verification

| Step | Verification check |
|---|---|
| 1 | Scope-confirmation memo countersigned by EPC Integrator. |
| 2 | TBC / TBD log reviewed and accepted by EPC Integrator with disposition for each open item. |
| 3 | MAWP cascade consistent with relief sizing; reciprocating frame load checks satisfied. |
| 4 | Motor and VFD certificates show NEMA MG 1 compliance; harmonics study within site limits. |
| 5 | Dewpoint margins ≥ project criterion at each stage; Stage 2 re-rate documented. |
| 6 | Scrubber sizing demonstrates capacity across stated turndown range. |
| 7 | Valve datasheets show ΔP ≤ 2 psid at 100 % open and correct fail action; recycle valve sizing supports 100 % recycle at 40 % speed. |
| 8 | P&ID confirms drain / vent / purge routing matches DBM L828. |
| 9 | C&E matrix and I/O list reviewed by EPC controls lead. |
| 10 | Shipping configuration matches site logistics study. |
| 11 | FAT report and pressure-test records signed; punch list closed. |
| 12 | Turnover index complete against agreed VDR (Vendor Document Requirements) list (**ASSUMPTION** — VDR clause-level list in `26020-Package_Requirements.docx` not directly accessible; **location TBD**). |

## Records

- Scope-confirmation memo (Step 1).
- Vendor package design basis document (Step 2).
- TBC / TBD log (Step 2 + ongoing).
- Compressor selection sheet and MAWP cascade table (Step 3).
- Motor / VFD datasheets, harmonics study, lube-oil schematic (Step 4).
- Cooler thermal datasheet and dewpoint margin report (Step 5).
- Scrubber and separation-pot datasheets (Step 6).
- Valve datasheets and recycle-sizing calculation (Step 7).
- P&ID extracts showing drain / vent / purge routing (Step 8).
- Control narrative, C&E matrix, I/O list (Step 9).
- GA drawing, ship-loose list, transportation study (Step 10).
- FAT report, pressure-test records, punch-list closure, quality dossier (Step 11).
- Turnover index, shipment release notice, bill of lading (Step 12).

Records produced under this procedure are the substantive inputs to DEL-050-05 (Vendor Document Turnover Package) and DEL-050-06 (EPC Vendor Package Review and Acceptance). Source: `SCOPE_LEDGER.csv` SOW-0173 deliverable list.
