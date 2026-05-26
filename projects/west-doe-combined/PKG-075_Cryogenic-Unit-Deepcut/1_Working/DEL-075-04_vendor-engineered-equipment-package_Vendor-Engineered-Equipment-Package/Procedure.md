# Procedure — DEL-075-04 Vendor Engineered Equipment Package (Cryogenic Unit "Deepcut")

This procedure describes how to **produce** the Vendor Engineered Equipment Package deliverable (design, fabrication/supply, and physical equipment package). Operational procedures for the cryogenic unit are governed by the EPC Construction Work Package (DEL-075-03), operator-facing procedures, and vendor operating manuals; references appear in the Records section.

## Prerequisites

1. Accepted upstream EPC anchors:
   - DEL-075-01 Scope of Work — defines vendor scope boundary.
   - DEL-075-02 Package Datasheet — defines technical handoff to the vendor.
   - DEL-075-03 Construction Work Package — defines installation/hookup expectations the vendor's package must accommodate.
   - Current status: not yet drafted in `1_Working/`; vendor engineering must not begin without these (TBD).
2. Accessible design basis: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (SEC-01, SEC-02, SEC-06, SEC-10).
3. Vendor selection complete (TBD — no vendor selection evidence in scope).
4. Site climate and spacing basis acknowledged (DBM-Deepcut SEC-02).
5. Plot plan CIV-235633-5002 (currently unavailable — proceed with TBD layout compliance per DBM-Deepcut SEC-02 Plot Plan Status).
6. Required references per `_REFERENCES.md` available to the vendor team (including `26020-Package_Requirements.docx` heading 29 — location TBD as binary).

## Steps

### 1. Receive and interpret EPC anchors
1.1 Receive DEL-075-01 SoW and DEL-075-02 Datasheet from EPC Integrator.
1.2 Reconcile EPC datasheet values against DBM-Deepcut SEC-06 UltraTEF Design Values; flag any discrepancy back to EPC Integrator before proceeding.
1.3 Confirm the 15 equipment tags from DBM-Deepcut SEC-10 row 9 (Cryogenic Unit "Deepcut") match the EPC Datasheet boundary.

### 2. Produce vendor package design basis
2.1 Publish vendor design basis covering process operating envelope (Expander and J-T modes), design conditions, control philosophy, and material/standards adoption.
2.2 Resolve open items called out in DBM-Deepcut SEC-06 to the extent the vendor's design responsibility allows; surface those that require Tourmaline / EPC decisions.
2.3 Cite source values explicitly (DBM-Deepcut SEC-06 + EPC Datasheet); label vendor inferences as ASSUMPTION.

### 3. Detailed engineering
3.1 BAHX design: ALPEMA 3rd Edition + vendor practice with explicit exceptions; >=10% excess area; 0 mm corrosion allowance; max 150 degF; mercury-tolerant practice; ASME U Stamp + BC CRN registration.
3.2 Turbo-expander/compressor: common-shaft design, ER ~0.3961, IGV sized to 125% normal design flow, anti-surge recycle, lube-oil/seal-gas system per R-3.7.
3.3 Cold separator, J-T valve, propane absorber, deethanizer, reflux/reboiler, expander aftercooler, methanol storage and triplex pump per Specification R-3.4-R-3.14.
3.4 Controls and protective functions per Specification R-4 (J-T stroke limit, anti-surge recycle, seal-gas/lube-oil permissives, A-pass bypass, E-pass MDMT bypass, methanol injection logic, cryo dry-out at low pressure).
3.5 Produce datasheets, GA, P&ID, isometrics, cause-and-effect, ITP.

### 4. Procurement and fabrication
4.1 Issue purchase specifications for long-lead items (BAHX, turbo-expander, columns, exchangers, pumps).
4.2 Execute vendor sub-supplier inspection per ITP.
4.3 Fabricate skids, columns, and modules; perform code testing (hydrotest, NDE per material class, U Stamp validation, CRN registration).

### 5. Factory acceptance testing
5.1 Conduct mechanical run test on turbo-expander package; verify bearing vibration, lube-oil rundown duration after simulated ESD (>=1 minute), and seal-gas heater function.
5.2 Hydrostatic test BAHX, columns, exchangers per ASME.
5.3 Cause-and-effect / interlock FAT for control functions per Specification R-4.
5.4 Methanol pump performance test; tank construction inspection.

### 6. Delivery / handoff
6.1 Prepare package for transport: module breakdown compatible with Tourmaline field-construction handling (off-loading, setting, mechanical hookup are Tourmaline field scope per DBM-Deepcut SEC-01).
6.2 Issue vendor documentation submittals into the Vendor Document Turnover process (DEL-075-05).
6.3 Support EPC Vendor Package Review and Acceptance (DEL-075-06).

## Verification

| Check | Method |
|---|---|
| Vendor design basis reconciled to DBM-Deepcut SEC-06 | Document review by EPC Integrator |
| Equipment roster matches DBM-Deepcut SEC-10 row 9 | Bill-of-materials cross-check |
| ALPEMA / ASME / API / TEMA / CRN compliance | Certification packages |
| Performance criteria (R-1) achievable | Process simulation + FAT + commissioning PTC (PTC during operation) |
| Control and protective functions (R-4) | Cause-and-effect FAT + commissioning hot-loop checks |
| ESD rundown duration | Mechanical run test record |
| Layout compatible with DBM-Deepcut SEC-02 spacing | GA review (provisional, pending CIV-235633-5002) |

## Records

- Vendor design basis document (output of Step 2).
- Equipment datasheets and GA / P&ID set (Step 3.5).
- Procurement records and sub-supplier ITP results (Step 4).
- FAT reports including mechanical run test, hydrotests, cause-and-effect (Step 5).
- Code certifications: ASME U Stamp, BC CRN registration, ALPEMA compliance statement (Step 5).
- Shipping documentation and module handling instructions (Step 6).
- Vendor document submittals forwarded to DEL-075-05 register.
- Run record: `_run_records/TASK_RUN_2026-05-24_2335.md` (this drafting run).
