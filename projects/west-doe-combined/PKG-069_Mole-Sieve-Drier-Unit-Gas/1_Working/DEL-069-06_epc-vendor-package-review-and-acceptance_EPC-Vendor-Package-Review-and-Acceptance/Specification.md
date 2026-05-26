# Specification — DEL-069-06 EPC Vendor Package Review and Acceptance

## Scope

This specification defines the requirements for the EPC Integrator's review and acceptance of the PKG-069 Mole Sieve Drier Unit (Gas) vendor package, covering vendor document review, integration acceptance against the EPC basis (Scope of Work, Package Datasheet, Construction Work Package), and handoff readiness to construction/commissioning. (Source: `_CONTEXT.md` Scope; DEL-069-06 decomposition row, `DELIVERABLE_REGISTER.csv`.)

In scope:
- Review of vendor design deliverables (DEL-069-04) and vendor document turnover (DEL-069-05).
- Conformance verification against the EPC SOW (DEL-069-01), EPC Package Datasheet (DEL-069-02), and Construction Work Package (DEL-069-03).
- Integration interface acceptance (process, mechanical, controls, utilities) with the 04-25 Deepcut facility.
- Issue, hold-point, and exception management to closure.

Out of scope:
- Vendor-internal engineering execution (DEL-069-04 vendor responsibility).
- Turnover document authoring (DEL-069-05 vendor responsibility, EPC review only).
- Other PKG-069 deliverables' production content (this is acceptance evidence).

## Requirements

### R-1 — Vendor Document Review Log
The EPC Integrator SHALL maintain a vendor document review log covering every vendor submittal in the Vendor Document Turnover Package (DEL-069-05), recording: document ID, revision, date received, reviewer, review status (Approved / Approved-with-Comments / Returned-for-Revision / Rejected), comments, and closeout reference. (Source: `_CONTEXT.md` Anticipated Artifacts; decomposition narrative for DEL-069-06.)

### R-2 — Conformance to EPC Scope of Work
Each vendor deliverable SHALL be checked against the EPC SOW (DEL-069-01). Nonconformities SHALL be recorded as exceptions with disposition. (Source: DEL-069-06 decomposition narrative.)

### R-3 — Conformance to EPC Package Datasheet
Vendor design SHALL conform to the EPC Package Datasheet (DEL-069-02), including the following source-anchored configuration baseline:
- R-3.1 Three-bed configuration (two adsorbing, one in standby/regeneration/cooling); downflow adsorption. (DBM-Deepcut SEC-06.)
- R-3.2 3A molecular sieve adsorbent only; 4A and 5A SHALL NOT be used. (DBM-Deepcut SEC-06.)
- R-3.3 Bed flow basis 166.3 MMSCFD per adsorbing bed; 25.45 MMSCFD regeneration/cooling. (DBM-Deepcut SEC-06.)
- R-3.4 Bed sizing 9.5 ft ID; regeneration tower 8 ft x 20 ft vertical (vendor MAY propose changes with engineering justification; deviations require EPC acceptance). (DBM-Deepcut SEC-06.)
- R-3.5 Two 100% inlet filter/coalescers on independent module with building. (DBM-Deepcut SEC-06.)
- R-3.6 Regeneration gas compressor 2 x 100% with installed standby; 25 MMSCFD basis; final differential and capacity to be confirmed by vendor (open item: assumed 100 psid vs detailed 79.5 psid). (DBM-Deepcut SEC-06.)
- R-3.7 Mol-sieve dust filter and MRU dust filter each 1 x 100%; 2 psid clean dP; manual online-bypass change-out. (DBM-Deepcut SEC-06.)
- R-3.8 900# flange class for the molecular-sieve system. (DBM-Deepcut SEC-04 §Inlet Pipeline Pressure and Flow.)
- R-3.9 Regeneration gas heater BEU heat-medium/process-gas S&T exchanger; regeneration temperature basis SHALL be resolved by vendor between 450 degF and 460 degF prior to acceptance. (DBM-Deepcut SEC-06.)
- R-3.10 Regeneration thermal efficiency target less than 40% SHALL be addressed in vendor heat-balance submittal. (DBM-Deepcut SEC-06.)
- R-3.11 Blowdown design SHALL provide operator-initiated HMI-only blowdown with two valves (regeneration and adsorption loops), 50 psi/min rate limit at maximum inlet pressure, and regen-compressor bypass to prevent reverse rotation. (DBM-Deepcut SEC-06.)
- R-3.12 Recycle return path SHALL provide normal return upstream of TEG inlet coalescer and an alternate normally-closed path upstream of mole-sieve coalescers. (DBM-Deepcut SEC-06.)
- R-3.13 Dehydrated outlet shall meet downstream cryogenic-service quality, supporting the < 0.1 ppmv sales-gas water spec attributable to mol-sieve dehydration. (DBM-Deepcut SEC-05 Sales Gas Booster Design Conditions.)

### R-4 — Conformance to Construction Work Package
Vendor installation, tie-in, inspection, and turnover provisions SHALL conform to the Construction Work Package (DEL-069-03). Construction interface and turnover checklist items SHALL be tracked to closure in R-1 / R-5. (Source: DEL-069-03 decomposition row.)

### R-5 — Package Acceptance Checklist
A package acceptance checklist SHALL be maintained, listing every acceptance criterion (process, mechanical, instrumentation/controls, electrical, materials, painting/coatings, NDE, hydrotest, FAT/SAT, documentation) with pass/fail status, evidence reference, and reviewer signature. (Source: `_CONTEXT.md` Anticipated Artifacts.)

### R-6 — Test and Inspection Evidence
Test and inspection evidence SHALL include vendor FAT records, NDE reports, hydrotest records, pressure-test certificates, instrument calibration records, performance test data where applicable, and any SAT evidence completed prior to acceptance. Each record SHALL be traceable from the acceptance checklist (R-5). (Source: `_CONTEXT.md` Anticipated Artifacts. ASSUMPTION: typical EPC vendor-package acceptance content; specific test list TBD pending vendor ITP.)

### R-7 — Turnover Evidence
Turnover evidence SHALL include the closed vendor document turnover register (DEL-069-05), punchlist closure, mechanical-completion certification, and EPC-issued package acceptance certificate referencing the closed checklist (R-5) and closed review log (R-1). (Source: `_CONTEXT.md` Anticipated Artifacts.)

### R-8 — Open-Item Resolution
The EPC Integrator SHALL not accept the package until the SEC-06 open items affecting vendor scope are resolved or formally deferred with documented disposition: mol-sieve inlet pressure, mol-sieve inlet-temperature final estimates, cycle times, adsorbent life, final regen-compressor capacity/differential, regeneration heater temperature basis, scrubber drain sizing, dry-out header operating pressure, and dry-out header MAWP. (DBM-Deepcut SEC-06 "Molecular-Sieve Open Items and Assumptions".)

## Standards

- Project DBM (governing): `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (SEC-06 and applicable SEC-04/SEC-05 clauses cited above).
- Project standards and codes cited within the package datasheet and vendor specifications — location TBD (not text-accessible during this run; `26020-Package_Requirements.docx` is the named binary source reference per the deliverable register).
- ASSUMPTION: industry standards typical for mole-sieve dehydration packages (e.g., ASME Section VIII Div 1, applicable piping/flange standards, GPSA Engineering Data Book guidance) apply; exact list to be confirmed against the EPC Package Datasheet (DEL-069-02).

## Verification

| Requirement | Verification Approach |
|---|---|
| R-1 | Review log artifact exists; sample audit; every DEL-069-05 entry mapped. |
| R-2 | Cross-check matrix vs DEL-069-01; nonconformities logged and dispositioned. |
| R-3.1–R-3.13 | Document review against vendor datasheets, P&IDs, and equipment lists; values compared to baseline in this specification; deviations recorded with engineering justification. |
| R-4 | Cross-check matrix vs DEL-069-03; construction interface checklist completed. |
| R-5 | Checklist exists, fully populated, signed; every item has evidence link. |
| R-6 | Evidence files indexed; FAT/NDE/hydrotest/calibration completeness audit. |
| R-7 | Turnover register closed; punchlist status report; acceptance certificate issued. |
| R-8 | Open-items register shows each SEC-06 item RESOLVED or DEFERRED-WITH-DISPOSITION before acceptance. |

## Documentation

Required artifacts (from `_CONTEXT.md`):
- Vendor document review log (R-1)
- Package acceptance checklist (R-5)
- Test and inspection evidence (R-6)
- Turnover evidence (R-7)

Supporting artifacts:
- Open-items disposition register (R-8)
- Nonconformity / deviation register (R-2, R-3)
- Final package acceptance certificate (R-7)
