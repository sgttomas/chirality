# Procedure: DEL-095-04 Vendor Engineered Equipment Package (PKG-095 Tanks, Slop API 650)

Procedure to PRODUCE the vendor engineered slop tank package. (Use/operate aspects are deferred to operations procedures outside this deliverable.)

## Prerequisites

- DEL-095-01 Scope of Work issued by EPC Integrator (input). [Source: `DELIVERABLE_REGISTER.csv` row DEL-095-01]
- DEL-095-02 Package Datasheet issued by EPC Integrator (input). [Source: `DELIVERABLE_REGISTER.csv` row DEL-095-02]
- Vendor access to `26020-Package_Requirements.docx` heading 47 for the vendor engineering deliverables list. [Source: `_REFERENCES.md`]
- Final tank register status (or interim register) communicated by EPC Integrator. [Source: `3-25_Comp_and_Liquids_DBM.md` line 406]
- Facility design basis context relevant to slop tankage (DBM sections cited in Datasheet/Specification). [Source: `_REFERENCES.md`]
- Conflict Table HRR items in `Guidance.md` reviewed; rulings recorded where available, otherwise carried as TBD. [Source: `Guidance.md` Conflict Table]
- Declared upstream dependencies (none at PREPARATION) re-checked before kickoff. [Source: `_DEPENDENCIES.md`]

## Steps

1. **Kickoff and basis confirmation.**
   - Vendor reviews DEL-095-01 and DEL-095-02 with EPC Integrator.
   - Vendor confirms Modified API 650 + 16 oz test pressure equivalent class. [Source: `4-25_Deepcut_DBM.md` line 518]
   - Vendor confirms tank count, capacity, and per-facility allocation (03-25: 1 x 3,800 bbl; 04-25: 2 x 2,000 bbl) against the final tank register. [Source: `4-25_Deepcut_DBM.md` lines 494, 498; `3-25_Comp_and_Liquids_DBM.md` line 406]
   - Resolve HRR-095-04-01 through HRR-095-04-06 to the extent possible at this stage; record remaining items as open. [Source: `Guidance.md` Conflict Table]

2. **Engineering design phase.**
   - Develop tank mechanical design per API 650 (Modified): shell, roof, bottom, anchorage, nozzle schedule.
   - Produce nozzle schedule covering: inlet from hydrocarbon drain header; inlet from LP condensate pump header; inlet from stabilizer outlet header (03-25); inlet from flare KO drum pump discharges; amine/TEG/caustic skim inlets (per DEL-095-02 routing); truck-in/out envirobox connection; PVRV; instrumentation. [Source: `3-25_Comp_and_Liquids_DBM.md` lines 1661, 1665, 463, 497-499]
   - Specify internal coating (Devchem 253 - ASSUMPTION; or per DEL-095-02 ruling). [Source: `3-25_Comp_and_Liquids_DBM.md` line 421]
   - Specify external insulation and tank heating envelope sized for -40 deg C ambient. [Source: `3-25_Comp_and_Liquids_DBM.md` site basis]
   - Specify PVRV; size EPRV per simultaneous-input scenario. [Source: `4-25_Deepcut_DBM.md` line 522; `Guidance.md` HRR-095-04-06]
   - Develop foundation interface design (anchor pattern, sole plate, sliding base if applicable) to receive final geotechnical inputs from EPC. [Source: foundations section of DBM]
   - Run design review with EPC Integrator at IFA/IFR milestones.

3. **Procurement / fabrication.**
   - Place orders for plate material per confirmed MOC (TBD - see HRR-095-04-03).
   - Fabricate tank shell/roof/bottom; control welding per qualified WPS; perform NDE per ITP.
   - Apply internal coating per coating QA plan; verify DFT and holiday testing.
   - Install insulation and heat-trace; verify circuit integrity.
   - Mount instrumentation and PVRV; perform mechanical completion check.

4. **Pressure / leak test.**
   - Conduct hydrostatic and pneumatic (16 oz) tests per API 650 Modified; record results in MTR/test record dossier. [Source: `4-25_Deepcut_DBM.md` line 518]

5. **Vendor document package preparation.**
   - Assemble vendor design basis, datasheets, GA drawings, P&ID extensions, instrumentation list, weld map, NDE records, MTRs, coating QA, insulation/heat-trace QA, pressure test records.
   - Conform document register to DEL-095-05 turnover format. [Source: `DELIVERABLE_REGISTER.csv` row DEL-095-05]

6. **Shipment and turnover handoff.**
   - Coordinate logistics with EPC Integrator (DEL-095-03 Construction Work Package consumer).
   - Submit Vendor Data Book / Final Supplier Documentation per DEL-095-05.
   - Support EPC Vendor Package Review and Acceptance (DEL-095-06). [Source: `DELIVERABLE_REGISTER.csv` row DEL-095-06]

## Verification

| Step | Verification | Source |
|---|---|---|
| 1 | DEL-095-01 and DEL-095-02 receipt; HRR ruling log present | `Guidance.md` Conflict Table |
| 2 | EPC design-review sign-off at IFA/IFR; nozzle schedule reconciled with facility P&IDs | `3-25_Comp_and_Liquids_DBM.md` lines 1661, 1665 |
| 3 | MTRs, NDE records, coating QA (DFT/holiday), insulation/heat-trace continuity certificates | `3-25_Comp_and_Liquids_DBM.md` line 421 (coating basis) |
| 4 | Pressure/leak test records signed by vendor QC and EPC inspector | `4-25_Deepcut_DBM.md` line 518 |
| 5 | Document register conformance check vs DEL-095-05 format | `DELIVERABLE_REGISTER.csv` row DEL-095-05 |
| 6 | EPC acceptance ruling per DEL-095-06; remaining open HRR items dispositioned | `DELIVERABLE_REGISTER.csv` row DEL-095-06 |

## Records

- Vendor package design basis document
- Tank datasheets (per tag, e.g., TK-9130-2)
- GA drawings; nozzle schedules; foundation interface drawings
- P&ID extensions covering tank tie-ins
- Instrumentation list and control narrative
- Weld map; NDE report; MTRs
- Coating QA records (DFT, holiday test)
- Insulation and heat-trace QA records
- Hydrostatic / pneumatic test record per API 650 Modified
- HRR ruling log captured from `Guidance.md` Conflict Table dispositions
- Vendor Data Book / Final Supplier Documentation (turnover artifact handed to DEL-095-05)
