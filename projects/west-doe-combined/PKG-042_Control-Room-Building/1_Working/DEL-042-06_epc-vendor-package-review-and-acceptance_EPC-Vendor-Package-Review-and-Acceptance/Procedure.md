# Procedure — DEL-042-06 EPC Vendor Package Review and Acceptance

**Interpretation:** This procedure describes how the EPC Integrator produces the acceptance evidence set for the PKG-042 Control Room Building vendor package. It is a review-and-acceptance procedure, not a vendor engineering procedure.

## Prerequisites

- EPC anchor deliverables are issued and current:
  - `DEL-042-01_scope-of-work`
  - `DEL-042-02_package-datasheet`
  - `DEL-042-03_construction-work-package`
- Package Vendor production deliverables are available for review:
  - `DEL-042-04_vendor-engineered-equipment-package`
  - `DEL-042-05_vendor-document-turnover-package`
- Access to the GATE-07 decomposition snapshot (`PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_REGISTER.csv`).
- Declared upstream dependencies: none recorded in `_DEPENDENCIES.md` as of initialization (TBD — review against actual schedule when vendor deliverables are issued).
- Reviewer assignments covering Electrical, I&C/Controls, Civil/Structural, Safety, and Utility/HVAC scopes.

Sources: `_CONTEXT.md`, `_DEPENDENCIES.md`, `DELIVERABLE_REGISTER.csv` rows DEL-042-01..05.

## Steps

1. **Establish the review baseline.**
   1.1 Capture the issued revisions of `DEL-042-01`, `DEL-042-02`, `DEL-042-03` as the anchor baseline.
   1.2 Capture the vendor submittal index from `DEL-042-05` as the input to the review log.
   1.3 Record baseline revisions in the package acceptance checklist header.

2. **Build the vendor document review log.**
   2.1 For each vendor document in the submittal index, record document ID, revision, reviewer, review date, disposition (Accept / Accept-with-Comment / Reject / Hold), and disposition rationale.
   2.2 Cross-reference each document to the SoW / Datasheet / CWP item(s) it satisfies.
   2.3 Flag any expected vendor document that is missing relative to the 26020-Package_Requirements.docx vendor-document tables. `location TBD` — when that source slice becomes accessible, reconcile and update.

3. **Conduct interface compliance review.**
   For each interface type tagged to PKG-042 (see Datasheet), perform a discipline walkdown of the vendor package against:
   3.1 The interface fact recorded in `INTERFACE_REGISTER.csv` (PKG-042 rows).
   3.2 The relevant facility-basis objective (OBJ-005 electrical, OBJ-006 controls/I&C, OBJ-007 utilities/HVAC, OBJ-008 civil/structural, OBJ-009 safety).
   3.3 Record findings per interface in the acceptance checklist with status (Compliant / Compliant-with-Comment / Non-Compliant / Hold).

4. **Conduct integration acceptance review.**
   4.1 Verify the vendor package preserves the responsibility split (vendor: engineering/design/equipment/documentation; EPC: integration). (Source: PACKAGE_REGISTER row PKG-042; OBJ-004.)
   4.2 Verify the vendor package can be installed per `DEL-042-03_construction-work-package` (constructability and tie-in coordination).
   4.3 Record findings in the acceptance checklist.

5. **Gather and index test/inspection evidence.**
   5.1 Collect vendor FAT/test/inspection records from `DEL-042-05`.
   5.2 Index each record to the corresponding requirement or interface.
   5.3 Flag records that are absent or do not satisfy the corresponding requirement; route to open-item log.

6. **Gather turnover evidence against OBJ-010 closure conditions.**
   6.1 For each OBJ-010 closure condition (operability, maintainability, sparing, isolation, winterization, vendor-documentation, commissioning, turnover, controlled open-item closure), record the evidence pointer and status.
   6.2 Note `TBD` where evidence is not yet available.

7. **Manage open items to closure.**
   7.1 Open an open-item register entry for each Reject / Hold / Non-Compliant finding from Steps 2-6.
   7.2 Track each item to documented closure (vendor action, EPC verification, closure date, evidence pointer).
   7.3 Acceptance is not granted while open items remain in Hold or Non-Compliant state for in-scope requirements.

8. **Produce the package acceptance checklist (signed).**
   8.1 Assemble the checklist with sections for: baseline, vendor document review summary, interface compliance summary, integration acceptance, test/inspection evidence summary, turnover evidence summary, open-item summary, and final disposition.
   8.2 Submit the checklist for human EPC Integrator signature. (Agents do not sign acceptance; see Guidance Principle 5.)

9. **Issue the acceptance evidence package.**
   9.1 Deliver the signed acceptance checklist, vendor document review log, indexed test/inspection evidence, turnover evidence, and open-item closure log as the deliverable output.

## Verification

| Step | Verification Check |
|---|---|
| 1 | Baseline revisions are recorded and match issued anchor deliverables. |
| 2 | Every vendor document in the submittal index has a disposition row. |
| 3 | Every PKG-042 interface type has an associated finding. |
| 4 | Integration findings cite the responsibility split and CWP. |
| 5 | Every requirement linked to a test/inspection has an evidence pointer or a flagged gap. |
| 6 | Each OBJ-010 closure condition is addressed with evidence or marked `TBD`. |
| 7 | No open Reject/Hold/Non-Compliant items remain unresolved at acceptance. |
| 8 | Acceptance checklist carries human signature; no agent signature is present. |
| 9 | All anticipated artifacts from `_CONTEXT.md` are present in the issued package. |

## Records

The following records SHALL exist on completion:

- Vendor document review log (Step 2).
- Interface compliance findings (Step 3) — embedded in or attached to the acceptance checklist.
- Integration acceptance findings (Step 4) — embedded in or attached to the acceptance checklist.
- Indexed test/inspection evidence (Step 5).
- Turnover evidence against OBJ-010 (Step 6).
- Open-item closure log (Step 7).
- Signed package acceptance checklist (Step 8).
- Acceptance evidence package transmittal record (Step 9).
