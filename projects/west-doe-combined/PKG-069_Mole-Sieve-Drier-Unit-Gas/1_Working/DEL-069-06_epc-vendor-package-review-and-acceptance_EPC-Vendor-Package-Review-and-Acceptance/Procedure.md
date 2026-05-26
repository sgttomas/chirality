# Procedure — DEL-069-06 EPC Vendor Package Review and Acceptance

## Purpose

Operational procedure for the EPC Integrator team to execute review and acceptance of the PKG-069 Mole Sieve Drier Unit (Gas) vendor package. The procedure produces the four artifacts named in `_CONTEXT.md`: vendor document review log, package acceptance checklist, test/inspection evidence, and turnover evidence.

## Prerequisites

- EPC Scope of Work (DEL-069-01) issued.
- EPC Package Datasheet (DEL-069-02) issued and baseline-controlled.
- Construction Work Package (DEL-069-03) issued.
- Vendor Engineered Equipment Package (DEL-069-04) submittals received from Package Vendor.
- Vendor Document Turnover Package (DEL-069-05) register established and being populated.
- Accessible references: `_REFERENCES.md`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-04, SEC-05, SEC-06.
- Declared upstream dependencies: none recorded in `_DEPENDENCIES.md` (PREPARATION). ASSUMPTION: practical upstream dependencies are sibling PKG-069 deliverables enumerated above.

## Steps

### S-1 — Establish acceptance workspace
1. Open the vendor document review log (R-1 artifact) and the package acceptance checklist (R-5 artifact).
2. Seed both with the baseline configuration values from the Specification (R-3 items) and the Datasheet Attributes table.
3. Seed the open-items register with the SEC-06 open items (R-8).

### S-2 — Receive and triage vendor submittals
1. For each vendor submittal entered in DEL-069-05, create a row in the review log (R-1) with document ID, revision, date received, and assigned reviewer.
2. Classify submittal by review type: process, mechanical, instrumentation/controls, electrical, materials, NDE, hydrotest, FAT/SAT, documentation.

### S-3 — Conformance review against EPC basis
1. For each submittal, check conformance against EPC SOW (R-2), EPC Package Datasheet (R-3), and Construction Work Package (R-4) as applicable.
2. Apply baseline checks from Spec R-3.1 through R-3.13. Verify, in particular:
   - 3-bed configuration and downflow adsorption (R-3.1).
   - 3A adsorbent only (R-3.2). Reject any other adsorbent type immediately.
   - Bed flow basis 166.3 / 166.3 / 25.45 MMSCFD (R-3.3).
   - Bed sizing 9.5 ft ID; regen tower 8 ft x 20 ft (R-3.4) — verify or accept documented deviation.
   - Two 100% inlet filter/coalescers on independent module (R-3.5).
   - Regen compressor 2 x 100%, 25 MMSCFD (R-3.6) — reconcile differential (CFT-02).
   - Dust filter sizing and bypass design (R-3.7).
   - 900# flange class (R-3.8) — reject any lower-class proposal for the mol-sieve system.
   - Regen heater temperature (R-3.9) — reconcile 450 vs 460 degF (CFT-01).
   - Blowdown philosophy (R-3.11) — verify HMI-only, dual valves, 50 psi/min, compressor bypass.
   - Recycle return paths (R-3.12) — verify both normal and alternate-closed installed.
3. Record review status (Approved / Approved-with-Comments / Returned-for-Revision / Rejected), comments, and closeout reference in the review log.

### S-4 — Witness and collect test/inspection evidence
1. Per vendor ITP (TBD — to be issued by vendor and accepted by EPC), schedule and witness FAT activities for high-criticality scope (regeneration compressor, control-system integration, hydrotest, NDE).
2. Collect ITP evidence records: FAT reports, NDE reports, hydrotest certificates, instrument calibration certificates, performance test data.
3. Index each evidence file in the acceptance checklist (R-5) by checklist item.

### S-5 — Open-item closure
1. For each SEC-06 open item in the open-items register (R-8), record: status (OPEN / RESOLVED / DEFERRED-WITH-DISPOSITION), responsible party, evidence reference, decision date.
2. Items affecting safety or rated capacity SHALL be RESOLVED before acceptance. Other items MAY be DEFERRED-WITH-DISPOSITION provided the disposition is documented and accepted by EPC process engineering.

### S-6 — Conflict Table adjudication
1. For each conflict in `Guidance.md` Conflict Table (CFT-01, CFT-02, CFT-03), record human ruling.
2. Update the affected source documents (Datasheet, Specification) only after ruling is recorded. (NOTE: Datasheet and Specification updates are out of scope for this deliverable's run unless authorized; conflicts may be carried to the next iteration.)

### S-7 — Turnover packaging
1. Confirm DEL-069-05 vendor document turnover register is closed (all expected documents received, reviewed, and dispositioned).
2. Confirm punchlist closure (no open punch items affecting acceptance).
3. Confirm mechanical-completion certification has been issued.
4. Compile the turnover evidence package referencing the closed review log (R-1), closed acceptance checklist (R-5), and closed open-items register (R-8).

### S-8 — Issue package acceptance certificate
1. Verify all R-1 through R-8 acceptance criteria pass with evidence on file.
2. Issue the package acceptance certificate referencing all closed registers. (Per K-AUTH-1, the acceptance certificate is authored and signed by the human EPC authority, not by any agent.)

## Verification

| Step | Verification |
|---|---|
| S-1 | Review log, acceptance checklist, and open-items register exist with baseline values seeded. |
| S-2 | Every DEL-069-05 submittal has a review-log row. |
| S-3 | Every submittal has a final review status and disposition; deviations have engineering justification. |
| S-4 | Every checklist item has an evidence reference (file path or document ID). |
| S-5 | Open-items register shows RESOLVED or DEFERRED-WITH-DISPOSITION for every entry; no OPEN items at acceptance. |
| S-6 | Every Conflict Table row has a human ruling recorded. |
| S-7 | Turnover package complete; mechanical-completion certificate present. |
| S-8 | Package acceptance certificate issued and human-signed. |

## Records

The following records SHALL be produced and retained in the deliverable folder (or referenced from it):

- Vendor document review log (R-1) — populated and closed at acceptance.
- Package acceptance checklist (R-5) — populated and closed at acceptance.
- Test and inspection evidence index (R-6) — file index with links/IDs to evidence artifacts.
- Open-items disposition register (R-8) — closed at acceptance.
- Conflict Table rulings (from `Guidance.md`) — recorded with date and signing authority.
- Turnover evidence package (R-7) — compiled summary referencing all of the above.
- Package acceptance certificate — human-signed; final record of acceptance.
