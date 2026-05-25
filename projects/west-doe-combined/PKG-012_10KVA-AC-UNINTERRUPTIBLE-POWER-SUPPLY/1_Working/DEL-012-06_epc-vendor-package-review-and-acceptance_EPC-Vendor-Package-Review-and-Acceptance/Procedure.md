# Procedure: EPC Vendor Package Review and Acceptance

## Purpose

Define the working procedure to produce and use the EPC Vendor Package Review and Acceptance deliverable for PKG-012, the 10KVA AC UNINTERRUPTIBLE POWER SUPPLY package.

## Prerequisites

- Accepted Gate 7 decomposition snapshot is available.
- Package identity, responsibility split, anticipated artifacts, and interface categories are taken from the accepted Gate 7 registers.
- EPC Scope of Work, Package Datasheet, and Construction Work Package are available or their absence is recorded as TBD/open.
- Vendor documentation, test/inspection evidence, and turnover evidence are available or their absence is recorded as TBD/open.
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm package identity.
   - Verify deliverable ID DEL-012-06_epc-vendor-package-review-and-acceptance.
   - Verify parent package PKG-012, 10KVA AC UNINTERRUPTIBLE POWER SUPPLY.
   - Verify discipline Electrical, WBS 02, and scope item SOW-0013.

2. Confirm responsibility boundaries.
   - Record that Package Vendor owns package engineering, package design, vendor documentation, and physical equipment.
   - Record that EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

3. Assemble evidence records.
   - Create or attach the vendor document review and comment log.
   - Create or attach the vendor package acceptance and turnover checklist.
   - Attach factory/shop test and inspection evidence where available.
   - Mark unavailable evidence as TBD/open.

4. Review declared interface categories.
   - Electrical Power.
   - Grounding / Bonding.
   - Maintenance Access.
   - Structural / Foundations / Supports.
   - For each interface, record accepted, accepted with comments, rejected, open, not applicable, or TBD.

5. Check acceptance basis.
   - Compare vendor package evidence against the EPC Scope of Work, Package Datasheet, and Construction Work Package where available.
   - If those source slices are unavailable, record the detailed acceptance criteria as TBD rather than closing the item.

6. Record open items and exceptions.
   - Identify missing documents, unresolved review comments, unavailable test evidence, incomplete interface checks, and turnover gaps.
   - Assign owner and closure basis where the project source provides them; otherwise mark owner or closure basis TBD.

7. Prepare handoff readiness summary.
   - State whether the package is accepted, accepted with open items, rejected, or not ready for acceptance.
   - Identify evidence included in the turnover set.
   - Identify remaining blockers or advisory open items. Under the current coordination mode, blockers are limited to declared dependency edges; none are declared in this deliverable folder.

## Verification

Verify that:

- Datasheet identity matches _CONTEXT.md and Gate 7 DELIVERABLE_REGISTER.csv.
- Specification requirements have corresponding procedure checks.
- Guidance assumptions and human-ruling items are reflected as TBD/open items, not hidden acceptance.
- All four accepted interface categories have a review disposition.
- Artifact register expectations are represented in the evidence list.
- No vendor-owned design work has been reassigned to the EPC Integrator.

## Records

Maintain the following records in or by reference from the acceptance package:

- Vendor document review and comment log.
- Vendor package acceptance and turnover checklist.
- Factory/shop test and inspection evidence.
- Interface acceptance notes.
- Open-item and exception list.
- Handoff readiness summary.
- Human rulings resolving TBD acceptance criteria or source-basis gaps.
