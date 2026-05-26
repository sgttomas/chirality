# Procedure — DEL-100-06 EPC Vendor Package Review and Acceptance

## Purpose

Produce the EPC Integrator's review-and-acceptance evidence pack for `PKG-100` (Hydrogen Peroxide Sweetening Unit): a vendor document review log, a package acceptance checklist, test/inspection evidence, and turnover evidence — culminating in a human-issued acceptance disposition. (`_CONTEXT.md` Anticipated Artifacts; REQ-100-06-01; REQ-100-06-10)

## Prerequisites

**Declared upstream dependencies (from `_DEPENDENCIES.md`):** None declared at PREPARATION. See Guidance §Conflict Table CONF-002.

**Logically required inputs (per `_CONTEXT.md` Scope and REQ-100-06-02..04):**

- `DEL-100-01` (Scope of Work) — accepted or sufficiently mature for review
- `DEL-100-02` (Package Datasheet) — accepted or sufficiently mature for review
- `DEL-100-03` (Construction Work Package) — accepted or sufficiently mature for review
- `DEL-100-04` (Vendor Engineered Equipment Package) — vendor-issued for review
- `DEL-100-05` (Vendor Document Turnover Package) — vendor-issued for review

**Reference materials:**

- GATE-07 decomposition snapshot (`DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `SCOPE_LEDGER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_REGISTER.csv`) — accessible.
- `_Sources/26020-Package_Requirements.docx` package heading 52 — referenced; clause-level slices not copied (location TBD).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 63 — referenced; cell-level slices not copied (location TBD).

**Roles:**

- EPC Integrator (lead reviewer)
- Package Vendor (provides clarifications, RFIs, document re-issues)
- Human approver(s) for disposition (specific role TBD)

## Steps

1. **Assemble the reviewer working set.**
   - Pull current versions of `DEL-100-01` through `DEL-100-05` from their respective folders.
   - Pull `SCOPE_LEDGER.csv` rows `SOW-0107..SOW-0110`, `PACKAGE_REGISTER.csv` PKG-100, and the 13 PKG-100 `INTERFACE_REGISTER.csv` rows.
   - Record each input with its version/snapshot identifier in the acceptance disposition record.

2. **Build the vendor document review log.**
   - For each vendor document in `DEL-100-05` (Vendor Document Turnover Package), record: document ID, title, revision, date, reviewer, review status (accepted / commented / rejected), comment references.
   - Cross-check the log against the vendor-document tables referenced by `OBJ-010` (in `26020-Package_Requirements.docx`). Flag missing documents.

3. **Build the package acceptance checklist** with sections aligned to Specification requirements:
   - **Scope conformance** (REQ-100-06-02): line items from `DEL-100-01`, `DEL-100-02`, `DEL-100-03`.
   - **Equipment conformance** (REQ-100-06-03): items from `SOW-0109` equipment list.
   - **Capacity / operating-condition conformance** (REQ-100-06-05): values from `SOW-0110`.
   - **Electrical driver conformance** (REQ-100-06-06): values from `SOW-0110`.
   - **Environmental design conformance** (REQ-100-06-07): values from `SOW-0110`; TBCs flagged.
   - **Interface conformance** (REQ-100-06-08): one row per PKG-100 interface type from `INTERFACE_REGISTER.csv`; "By others" items from `SOW-0110` mapped to EPC-side deliverable.
   - **Operability / maintainability / handoff** (REQ-100-06-09): per `OBJ-010` closure items.
   - Each row records: requirement reference, source artifact reviewed (provenance per REQ-100-06-12), reviewer, status, comments.

4. **Compile test and inspection evidence.**
   - Collect FAT/SAT records, NDE reports, hydrotest records, electrical/instrumentation tests, and any third-party inspection certificates provided by the vendor.
   - Index each record to the relevant checklist row(s) and to the relevant interface.
   - Where evidence is unavailable, mark TBD and add to the open-items log.

5. **Compile turnover evidence.**
   - Verify the vendor turnover package per `DEL-100-05` is complete: O&M manuals, spare parts list, lubrication schedule, commissioning procedures, warranty documents (per `OBJ-010`; specific list TBD where not enumerated in accessible sources).
   - Verify handoff readiness: sparing, isolation, winterization, maintenance access (per `OBJ-010`).

6. **Manage open items.**
   - Open-items log entries SHALL include: item ID, originating source (`SOW-0110` TBCs and any reviewer-raised items), owner, target date, status.
   - The two explicit TBCs from `SOW-0110` — pump capacity and design conditions — are mandatory open-items log entries until closed by vendor.

7. **Issue acceptance disposition (human).**
   - A human approver reviews the checklist, evidence, and open-items log.
   - Disposition is one of: **accept**, **accept with conditions**, **reject**.
   - Conditions, if any, reference open-items-log rows.
   - Sign-off is recorded in the acceptance disposition record with date, approver, and rationale.
   - No agent or tool may issue or alter the disposition. (K-AUTH-1; REQ-100-06-10)

8. **Update `_STATUS.md` and notify downstream.**
   - When acceptance is issued, advance `_STATUS.md` per project lifecycle (specific target state TBD — outside this skill's safe-update rule).
   - Notify EPC integration consumers (downstream packages and the project handoff process).

## Verification

| Step | Verification Check | Pass Criterion |
|---|---|---|
| 1 | All five upstream deliverables and required register rows are listed in the disposition record with version/snapshot IDs. | Complete input inventory exists. |
| 2 | Vendor document review log covers every entry in the vendor-document tables and every document delivered. | No silently missing documents. |
| 3 | Acceptance checklist has at least one row per Specification requirement (REQ-100-06-02 through REQ-100-06-09). | Requirement coverage = 100% (or explicit TBD with rationale). |
| 4 | Each test/inspection record indexes to at least one checklist row. | No orphan or unreferenced evidence. |
| 5 | Turnover evidence list maps to the `OBJ-010` closure conditions. | All `OBJ-010` items addressed or explicitly TBD. |
| 6 | Open-items log includes the two `SOW-0110` TBCs at minimum. | Mandatory open items present. |
| 7 | Disposition record carries a human signature with date and rationale; no agent or tool entries in the signature line. | K-AUTH-1 satisfied. |
| 8 | `_STATUS.md` updated by the appropriate skill/agent; downstream consumers notified. | Status reflects post-acceptance state. |

## Records

The following records are produced and retained in this deliverable folder:

- **Vendor document review log** (REQ-100-06-01)
- **Package acceptance checklist** (REQ-100-06-01; REQ-100-06-02..09)
- **Test/inspection evidence index** (REQ-100-06-01) — evidence files may be linked to their owning deliverable folder rather than duplicated
- **Turnover evidence index** (REQ-100-06-01; REQ-100-06-09)
- **Open-items log** (REQ-100-06-11)
- **Acceptance disposition record** (REQ-100-06-10; signed by human approver)
- **Provenance metadata** embedded in each record (REQ-100-06-12)
