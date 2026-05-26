# Procedure — DEL-055-06 EPC Vendor Package Review and Acceptance

> Operational procedure for producing the EPC Integrator's vendor package
> review and acceptance evidence set for PKG-055 (LP Flare KO Drum).

## Purpose

Define the repeatable steps the EPC Integrator follows to review the Package
Vendor's engineered equipment package (DEL-055-04) and vendor document turnover
(DEL-055-05) against the EPC Scope of Work (DEL-055-01), Package Datasheet
(DEL-055-02), and Construction Work Package (DEL-055-03), and to record the
review, acceptance, and turnover-readiness evidence required by PKG-055.

## Prerequisites

- DEL-055-01 (Scope of Work) issued at INITIALIZED or better.
- DEL-055-02 (Package Datasheet) issued at INITIALIZED or better.
- DEL-055-03 (Construction Work Package) drafted with turnover checklist.
- DEL-055-04 (Vendor Engineered Equipment Package) — vendor submittals available
  for review.
- DEL-055-05 (Vendor Document Turnover Package) — vendor document register
  available.
- Access to authoritative sources: `26020-Package_Requirements.docx` heading 10
  (location TBD — currently binary), and `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- Reviewer authorization to issue acceptance dispositions on behalf of the EPC
  Integrator.

## Steps

1. **Initialize the review register.** Create the vendor document review log
   keyed by vendor document number; populate from DEL-055-05's vendor document
   register.
2. **Build the acceptance checklist.** Generate the line-item checklist by
   extracting acceptance criteria from:
   - DEL-055-01 (Scope of Work) — what the vendor is contracted to deliver;
   - DEL-055-02 (Package Datasheet) — the technical handoff basis;
   - DEL-055-03 (Construction Work Package) — installation and turnover
     interface requirements.
   Each checklist row SHALL cite its source (DEL ID + section).
3. **Review vendor engineered package (DEL-055-04).** For each vendor submittal:
   a. Record receipt in the review log.
   b. Compare against the acceptance checklist row(s) it satisfies.
   c. Assign a disposition: Approved / Approved-as-Noted / Rejected /
      Information.
   d. Record reviewer, date, and comments.
4. **Review vendor turnover documents (DEL-055-05).** Verify the following are
   present and acceptable (specific record types may be refined when source
   heading 10 is extracted; TBD):
   - Vessel manufacturer data report and ASME Code stamp record (ASSUMPTION).
   - Pressure-test records (hydrotest / pneumatic), including duration and
     joint inspection results.
   - NDE records as required by the vessel and piping codes.
   - FAT and SAT certificates for instrumentation and skid-level functional
     tests.
   - Vendor data book transmittal.
5. **Verify layout / siting.** Reconcile the as-built skid placement against
   flare/KO drum spacing rules:
   - Distance between flare tanks (including KO drums) and vegetation or fire
     hazards >= 10 m (OGAOM Sec. 9.6.15 via DBM-Deepcut). Reject if violated.
   - Thermal radiation flux <= 9 kW/m^2 inside boundary, <= 5 kW/m^2 outside
     boundary (OGPFR Appx 1). Coordinate-level reconciliation against plot plan
     CIV-235633-5002 is TBD until that drawing is issued.
6. **Reconcile open items.** Build the consolidated punchlist from rejected and
   approved-as-noted dispositions. Close items by re-submission cycles with the
   vendor.
7. **Issue acceptance.** When all checklist rows are dispositioned Approved or
   Approved-as-Noted (with no open safety- or code-affecting items), the EPC
   Integrator's authorized reviewer signs the package acceptance record.
   Acceptance with outstanding items requires explicit conditional-acceptance
   text and identified closure dates.
8. **Compile turnover evidence.** Assemble the final turnover evidence record:
   acceptance signature, vendor data book reference, mechanical completion
   certificate reference, punchlist closure log, and pointer to DEL-055-05
   final transmittal.
9. **Update deliverable status.** When the acceptance record is signed and
   turnover evidence is compiled, request a `_STATUS.md` advance through the
   normal status workflow.

## Verification

| Check | Evidence |
|---|---|
| Every SoW item (SOW-0083..0086) has at least one acceptance checklist row | Cross-reference report (checklist vs. DEL-055-01). |
| Every checklist row has a disposition and reviewer signature | Inspect review log and checklist. |
| No outstanding rejected items remain at acceptance | Punchlist closure record. |
| Layout complies with KO-drum / flare spacing rules | Layout reconciliation note vs. OGAOM Sec. 9.6.15 and (when issued) CIV-235633-5002. |
| Vessel test and NDE records are present and within acceptance limits | Test/inspection evidence index entries. |
| Turnover artifacts (MCC, data book, punchlist closure) are present | Turnover evidence record. |

## Records

The following records are the deliverable's artifact set (per `_CONTEXT.md`):

- Vendor Document Review Log
- Package Acceptance Checklist (with dispositions)
- Test & Inspection Evidence Index
- Punchlist (open) and Punchlist Closure Log
- Layout Reconciliation Note (against OGAOM Sec. 9.6.15 and CIV-235633-5002 when issued)
- Turnover Evidence Record (acceptance signature + supporting record pointers)

All records SHALL be retained under this deliverable folder or referenced by
durable identifier from this folder.
