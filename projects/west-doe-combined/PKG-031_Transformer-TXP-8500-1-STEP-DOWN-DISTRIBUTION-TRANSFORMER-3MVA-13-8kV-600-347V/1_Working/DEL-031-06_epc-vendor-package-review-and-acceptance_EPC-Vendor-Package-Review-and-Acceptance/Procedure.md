# Procedure: DEL-031-06_epc-vendor-package-review-and-acceptance

## Purpose

Describe the operational steps the EPC Integrator follows to review the Package Vendor's engineered equipment package for `PKG-031` (Transformer TXP-8500-1, 3 MVA, 13.8 kV / 600 V / 347 V), capture review evidence, complete the acceptance checklist, and document turnover readiness.

## Prerequisites

- Accepted EPC Scope of Work for the package (`DEL-031-01`).
- Accepted Package Datasheet (`DEL-031-02`) defining the technical handoff basis.
- Accepted Construction Work Package (`DEL-031-03`) defining installation, tie-in, and turnover plan.
- Vendor Engineered Equipment Package available for review (`DEL-031-04`).
- Vendor Document Turnover Package available for review (`DEL-031-05`), including vendor document register, submittals, and turnover records.
- Access to the Gate 7 PROJECT_DECOMP snapshot for identity and interface verification.
- Access to the facility electrical design basis source slices (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`).
- Declared upstream dependencies: none recorded during PREPARATION; sibling deliverables `DEL-031-01` through `DEL-031-05` are de facto inputs.

## Steps

1. **Initialize review record.**
   - Open the vendor document review log (`ART-8D69884269`) and import the vendor document register entries from `DEL-031-05`.
   - Confirm identity fields against `_CONTEXT.md`, workbook row 33, and `PACKAGE_REGISTER.csv`.

2. **Review identity and responsibility.**
   - Confirm the vendor package matches `PKG-031` identity: TXP-8500-1, 3 MVA, 13.8 kV / 600 V / 347 V, WBS 01, CoA 26020-01-30-022.
   - Confirm the responsibility split (Vendor authoring; EPC integration) is reflected in vendor documents.

3. **Review interface compliance for each of the seven `PKG-031` interface facts.**
   - Electrical Power: verify primary 13.8 kV connection arrangement and secondary 600 V distribution; check ratings, terminal arrangements, and protection coordination boundary against the Package Datasheet.
   - Grounding / Bonding: verify ground grid connection (two points), 600 V secondary 5 A continuous high-resistance grounding architecture, and primary-side grounding connection to the medium-voltage system.
   - Area / Exterior Lighting: verify general arrangement does not conflict with site lighting layout.
   - I&C / Control Cabling: verify temperature, tap-changer (if applicable), alarm, and status terminations. Specific I&C scope `TBD` pending Package Datasheet finalization.
   - Communications / Network: verify any network interface or confirm absence. ASSUMPTION: distribution transformers typically lack native network interfaces.
   - Maintenance Access: verify operator clearances, oil sampling/handling access (if oil-filled), bushing replacement clearance, and de-energization isolation.
   - Structural / Foundations / Supports: verify foundation type (precast concrete bearing pad / structural steel base), anchor pattern, load data, and seismic/wind basis against the EPC civil/structural package.
   - Record each interface disposition (Pass / Conditional / Fail) with comment basis and source citation.

4. **Review vendor document set.**
   - Walk the vendor document register entries; for each entry, record review status (Reviewed Without Comment / Reviewed With Comment / Rejected) and reviewer name/date.
   - Where comments are issued, ensure the vendor's response and resolution are recorded; closure must occur before acceptance.

5. **Review test and inspection evidence.**
   - Verify factory acceptance test reports, routine test records, and shop inspection evidence (`ART-0D8191743E`) are present.
   - Compare against the test scope required by the Package Datasheet and vendor ITP. Detailed list of required tests is `TBD` pending Package Datasheet; record missing items as comments.

6. **Verify turnover readiness.**
   - Confirm turnover records from `DEL-031-05` are present and complete (e.g., nameplate data, calibration records, as-shipped condition records).
   - Confirm tie-in readiness against the Construction Work Package (`DEL-031-03`).

7. **Complete acceptance checklist (`ART-E97EECD60B`).**
   - Mark each interface and document-register section Pass / Conditional / Fail.
   - For conditional acceptance, list specific remediation actions, owners, and due dates.
   - For fail dispositions, suspend acceptance and route back to the vendor.

8. **Issue acceptance disposition.**
   - Human authorized EPC Integrator reviewer signs the acceptance checklist. Per `K-AUTH-1`, this signature is human-authored and not agent-generated.
   - Update `_STATUS.md` and notify downstream consumers per the Construction Work Package handoff plan.

9. **Track conditions to closure.**
   - Maintain an open-item / conditional-acceptance tracker until all conditions are closed.
   - Conditions outstanding at facility turnover trigger escalation rather than silent carry-forward.

## Verification

| Verification item | Method | Acceptance criterion |
|---|---|---|
| Identity completeness | Comparison against workbook row 33 and Gate 7 registers. | All identity fields match. |
| Interface coverage | Checklist coverage of all seven `PKG-031` interfaces. | No interface omitted; each has a disposition. |
| Vendor document coverage | Review log includes every vendor-register entry. | No document omitted. |
| Test evidence coverage | Test records present per Package Datasheet / ITP. | Missing items recorded as comments or accepted with waiver. |
| Source citation | Each acceptance criterion cites the source slice. | No uncited or invented criteria. |
| Disposition completeness | All checklist sections marked. | No section left blank at acceptance time. |
| Human acceptance signature | Authorized human reviewer signed acceptance checklist. | `K-AUTH-1` satisfied. |
| Open-item tracker | All conditional items have owners and due dates. | No open-ended conditions. |

## Records

- Vendor document review log (`ART-8D69884269`).
- Package acceptance and turnover checklist with disposition (`ART-E97EECD60B`).
- Factory/shop test and inspection evidence (`ART-0D8191743E`).
- Conditional-acceptance / open-item tracker (where conditional acceptance is granted).
- Acceptance signature record (human-authored).
- Provenance pointers to the Gate 7 snapshot, workbook row 33, and Gate 7 registers used.
