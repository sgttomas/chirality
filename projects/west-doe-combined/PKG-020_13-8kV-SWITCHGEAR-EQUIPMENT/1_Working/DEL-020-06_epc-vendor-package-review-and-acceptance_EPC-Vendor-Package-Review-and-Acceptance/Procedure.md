# Procedure: DEL-020-06_epc-vendor-package-review-and-acceptance

## Purpose

Produce the EPC Vendor Package Review and Acceptance evidence for `PKG-020` (13.8kV SWITCHGEAR EQUIPMENT): vendor document review log, package acceptance checklist, test/inspection evidence, and turnover evidence.

## Prerequisites

- Declared upstream dependencies: none declared in `_DEPENDENCIES.md`. The functional prerequisites below are the project-substance prerequisites, not declared dependency edges.
- Functional prerequisites:
  - DEL-020-01 (EPC Scope of Work) available and accepted.
  - DEL-020-02 (EPC Package Datasheet) available and accepted.
  - DEL-020-03 (Construction Work Package) available and accepted.
  - DEL-020-04 (Vendor Engineered Equipment Package) and DEL-020-05 (Vendor Document Turnover Package) issued by the Package Vendor.
  - Required electrical studies (hazardous-area-classification, load, short-circuit, relay-coordination/arc-flash, load-flow) completed. (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12.)
- Reference materials:
  - `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`.
  - `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `INTERFACE_REGISTER.csv` rows for `PKG-020`.
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12.
  - ELC-QAS-000007-001 (Medium Voltage Switchgear) and ELC-QAS-000003-001 (Electrical Requirements for Packaged Equipment) (`location TBD`).

## Steps

1. **Confirm preconditions.** Verify the prerequisites above are in place. Where any item is missing, record it and either pause acceptance or grant conditional acceptance with explicit gating. (Recommendation: hard-gate on electrical studies per REQ-020-06-04.)
2. **Enumerate vendor submittals.** Build the vendor document review log from the DEL-020-05 vendor document register. Record reviewer, submission date, and project document-control identifier (numbering scheme TBD).
3. **Review vendor submittals.** For each submittal, perform the review against:
   - the EPC Scope of Work (DEL-020-01),
   - the EPC Package Datasheet (DEL-020-02),
   - the Construction Work Package (DEL-020-03),
   - governing electrical standards (CSA C22.1-21; Tourmaline electrical specifications, particularly ELC-QAS-000007-001 and ELC-QAS-000003-001).
   Capture comments and assign review status per project document-control procedure.
4. **Build the package acceptance checklist.** Populate line items for:
   - scope conformance (against DEL-020-01),
   - datasheet conformance (against DEL-020-02),
   - constructability/tie-in conformance (against DEL-020-03),
   - interface conformance (one line item per PKG-020 interface row in `INTERFACE_REGISTER.csv`: Electrical Power, Grounding/Bonding, I&C/Control Cabling, Communications/Network, Maintenance Access, Structural/Foundations/Supports),
   - code/standard conformance (CSA C22.1-21; Tourmaline electrical specifications),
   - electrical-study-outcome incorporation (ratings, protection settings, arc-flash labels).
5. **Verify certification.** Confirm that the supplied equipment is new, of current design, and third-party certified by CSA, ULc, FM, ETL, or another acceptable NRTL. Record certificate identifiers in the acceptance checklist. (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 codes/standards paragraph.)
6. **Collect FAT/SAT and inspection evidence.** Attach FAT records, SAT records, and inspection reports to the acceptance package. Default witness scope to high-impact tests (bus-bar dielectric, breaker functional, relay logic, primary injection per cubicle) until ELC-QAS-000007-001 clause text is accessible.
7. **Reconcile turnover evidence.** Cross-reference DEL-020-05 turnover index entries to vendor manuals, mechanical-completion records, and EPC acceptance sign-offs. Reference the facility turnover procedure (`location TBD`).
8. **Process deviations.** Where the vendor package or its review surfaces a deviation or exception from applicable codes/standards, record it in a deviation register and confirm formal approval by Tourmaline Oil Corp before acceptance. (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12.)
9. **Final acceptance decision.** When all checklist items are satisfied (or carry approved deviations), record the EPC-Integrator acceptance decision (accept / accept-with-conditions / reject). Capture conditions, owners, and due dates.
10. **Archive the evidence set.** Store the four artifacts (review log, acceptance checklist, test/inspection evidence, turnover evidence) in the deliverable folder under stable filenames and document-control identifiers.

## Verification

| Verification check | How performed |
|---|---|
| All required artifacts exist | File-system audit of deliverable folder. |
| Every PKG-020 interface row has a matching checklist line item | Cross-tab of `INTERFACE_REGISTER.csv` rows for `PKG-020` against acceptance checklist. |
| Every DEL-020-05 vendor submittal has a review-log entry with disposition | Reconciliation between vendor document register and review log. |
| No open code/standard deviation lacks approval | Inspection of deviation register against Tourmaline approval records. |
| All electrical studies complete and incorporated | Inspection of study outputs against vendor ratings, protection settings, and arc-flash labels. |
| Equipment certification verified | Inspection of NRTL certificate records vs. nameplate data. |

## Records

The following records shall result from this procedure and shall be retained within `{DELIVERABLE_PATH}`:

- Vendor document review log (with reviewer, date, status, comments, disposition).
- Package acceptance checklist (with line-item evidence references).
- Test and inspection evidence set (FAT records, SAT records, inspection reports).
- Turnover evidence set (reconciliation index, mechanical-completion sign-offs, EPC acceptance sign-off).
- Deviation register (if any), with Tourmaline approval evidence.
- Final acceptance decision record (accept / accept-with-conditions / reject), with conditions, owners, and due dates.
