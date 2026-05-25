# Procedure: DEL-022-04_vendor-engineered-equipment-package

This Procedure describes the steps to **produce** the Vendor Engineered Equipment Package deliverable (`DEL-022-04`) for `PKG-022`. It does not cover field operation of the installed switchgear, which is governed by separate operations and maintenance procedures.

## Prerequisites

- Accepted EPC Scope of Work (`DEL-022-01`) for `PKG-022`.
- Accepted EPC Package Datasheet (`DEL-022-02`) for `PKG-022`, including the package interface requirements matrix.
- Available facility electrical studies (short-circuit, relay coordination/arc-flash, load-flow, load analysis) at the maturity needed to confirm equipment ratings (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical studies table).
- Project Electrical specifications available to the vendor: `ELC-QAS-000003-001`, `ELC-QAS-000007-001`, `ELC-QAS-000002-001`, `ELC-QAS-000001-001`, and `ELC-QAS-000008-001` if MV MCC scope is in the package.
- Gate 7 PROJECT_DECOMP snapshot for register lookups: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`.
- Resolution of HRR-022-04-001 and HRR-022-04-002 in `Guidance.md` to fix nominal bus voltage and equipment count.
- Declared upstream dependencies: none recorded in `_DEPENDENCIES.md`. Functional upstream dependence on `DEL-022-01` and `DEL-022-02` is from the deliverable contract.

## Steps

1. **Confirm package identity and scope.** Read `_CONTEXT.md`, `_REFERENCES.md`, `DELIVERABLE_REGISTER.csv` row `DEL-022-04_vendor-engineered-equipment-package`, and `PACKAGE_REGISTER.csv` row `PKG-022`. Confirm the bus voltage, equipment count, and physical scope from the Package Datasheet (`DEL-022-02`). If unresolved, do not proceed to step 4 without a written human ruling on HRR-022-04-001/-002.
2. **Establish the interface set.** Pull the six `PKG-022` rows from `INTERFACE_REGISTER.csv` (`IFC-FAD0C5C924`, `IFC-291807A33B`, `IFC-FFD6E87354`, `IFC-652BE03197`, `IFC-53BEFBC3CA`, `IFC-ED54C3FD1A`) and confirm their handling in the Package Datasheet's package interface requirements matrix.
3. **Establish the specification stack.** Record `ELC-QAS-000003-001` (Electrical Requirements for Packaged Equipment) and `ELC-QAS-000007-001` (Medium Voltage Switchgear). Add `ELC-QAS-000008-001` if MV MCC scope is included.
4. **Develop vendor package design basis.** Capture nominal voltages, ratings basis (with reference to facility study outputs), grounding basis (e.g., 100 A 10 s NGR for 6.9 kV transformers if applicable), control power (120 VAC / 125 VDC UPS), area classification assumptions, and environmental envelope.
5. **Produce vendor datasheet set.** At minimum: single-line, bus arrangement, breaker schedule, protection and metering schedule, control and DC schematics, layout/general arrangement, and nameplate schedule. Specific document list is TBD pending `DEL-022-02` and `DEL-022-05`.
6. **Produce specification conformance matrix.** Map vendor design to clauses of `ELC-QAS-000003-001` and `ELC-QAS-000007-001` (and `-008-001` if applicable). Mark deviations explicitly. Clause-level mapping detail is `location TBD` until the specifications are accessed.
7. **Produce interface coverage matrix.** Map vendor design to each of the six `PKG-022` interface rows. Address cabling (TECK; insulation per voltage class), bottom cable entry, maintenance access, and PLC Ethernet communication where applicable.
8. **Fabrication release control.** Do not release for fabrication until: (a) equipment ratings reconciled to the facility study outputs; (b) EPC Integrator confirms the package interface requirements matrix; (c) HRR items in `Guidance.md` are resolved.
9. **Fabrication and FAT.** Fabricate the physical equipment package per the released design. Conduct Factory Acceptance Test (FAT) covering protection, control, and mechanically latched fused contactor operation where applicable.
10. **Vendor document turnover.** Deliver the vendor document register and submittals through `DEL-022-05` and support EPC review/acceptance through `DEL-022-06`.

## Verification

- Identity verified against `DELIVERABLE_REGISTER.csv` and `PACKAGE_REGISTER.csv` rows.
- Interfaces verified against `INTERFACE_REGISTER.csv` rows for `PKG-022`.
- Specification conformance verified by the specification conformance matrix.
- Equipment ratings verified against facility study outputs (short-circuit, relay coordination/arc-flash, load-flow, load analysis).
- FAT verified by FAT report acceptance.
- Acceptance verified by `DEL-022-06` EPC Vendor Package Review and Acceptance record.

## Records

- Vendor package design basis.
- Vendor datasheet set (per Step 5).
- Specification conformance matrix.
- Interface coverage matrix mapped to `INTERFACE_REGISTER.csv` rows for `PKG-022`.
- FAT report.
- Vendor document register (delivered through `DEL-022-05`).
- EPC acceptance record (delivered through `DEL-022-06`).
- This deliverable's `_run_records/` entries documenting drafting/enrichment passes.
