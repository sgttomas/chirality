# Procedure — DEL-036-06 EPC Vendor Package Review and Acceptance

**Interpretation:** This Procedure describes the steps the EPC Integrator follows to produce the review-and-acceptance evidence set for the PKG-036 vendor package (6.9 kV Switchgear Electrical Building, 830-1).

## Prerequisites

- DEL-036-01 (EPC Scope of Work) available and at a maturity sufficient to anchor acceptance criteria.
- DEL-036-02 (EPC Package Datasheet) available and at a maturity sufficient to anchor technical acceptance criteria.
- DEL-036-03 (EPC Construction Work Package) available for turnover/handoff alignment.
- DEL-036-04 vendor engineered equipment package and DEL-036-05 vendor document turnover package submittals available for review.
- Access to project standards: CSA C22.1-21; ELC-QAS-000003-001 (Rev 2); ELC-QAS-000007-001 (Rev 1); ELC-QAS-000015-001 (Rev 1). Local clause-level text is `TBD` (location TBD).
- Acceptance threshold and witness/no-witness FAT policy: `TBD` (project policy not in accessible sources).

## Steps

1. **Establish acceptance scope.** From DEL-036-01 SOW and DEL-036-02 Datasheet, extract the equipment list, voltage classes, ratings, and declared interface types for PKG-036 (use PACKAGE_REGISTER.csv row PKG-036 interface list as the baseline). Record in the acceptance checklist scaffold (ART-8F50EF826E).
2. **Set up the vendor document review log.** Create the review log (ART-FB61C5F7B1) keyed by vendor document ID and revision. Populate review log fields: vendor doc ID, revision, type, SOW/Datasheet/CWP clause reference, review status, comment ID, reviewer, date.
3. **Review vendor documents (DEL-036-05 submittals).** For each submittal: (a) confirm certification and code basis evidence (REQ-036-06-003, REQ-036-06-004); (b) verify compliance with the relevant ELC-QAS specification class; (c) record comments and disposition (Accepted / Accepted-with-Comments / Rejected). Resolve `TBD` items where the underlying project standard is required by issuing an EPC clarification request.
4. **Review vendor engineered equipment package (DEL-036-04).** Verify equipment specifications, single-line diagrams, grounding scheme (REQ-036-06-006), and building/services design (REQ-036-06-007) against DBM Electrical Buildings clauses. Apply Conflict Table CFL-036-06-001 and CFL-036-06-002 to confirm which equipment classes are actually supplied.
5. **Discharge interface acceptance.** For each declared interface type (12 types per PACKAGE_REGISTER.csv row PKG-036), record vendor evidence and EPC integrator acceptance on the interface-by-interface checklist (REQ-036-06-005).
6. **Capture test/inspection evidence (ART-2E1BDD099B).** Collect or witness factory/shop test reports per the vendor ITP. Confirm closure of any non-conformances. Detailed FAT acceptance criteria are `TBD` pending ELC-QAS-000007-001 clause access.
7. **Assemble turnover evidence.** Compile certification records, as-built vendor documentation, spare parts list, test records, and operating manuals into the turnover evidence package. Confirm alignment with DEL-036-03 Construction Work Package handoff requirements (REQ-036-06-009).
8. **Acceptance decision and signoff.** EPC Integrator (lead) records final acceptance decision on the package acceptance checklist with evidence references. Open items above an agreed threshold block acceptance; threshold value is `TBD`.
9. **Issue turnover.** Deliver the complete review-and-acceptance evidence set (review log, checklist, test/inspection evidence, turnover evidence) into the project document control system and to the parties consuming DEL-036-03 Construction Work Package.

## Verification

- Review log contains an entry for every vendor document submitted under DEL-036-05.
- Interface checklist has a dispositioned line per declared interface type from PACKAGE_REGISTER.csv row PKG-036.
- Certification (CSA/ULc/FM/ETL/other NRTL) is evidenced for each piece of supplied electrical equipment (REQ-036-06-003).
- FAT/shop test evidence is present for each equipment item with a required factory test per the vendor ITP.
- Acceptance checklist is signed by the EPC Integrator with explicit references to the vendor evidence files.
- Open conflict items CFL-036-06-001/-002/-003 are tracked to a human ruling before final acceptance.

## Records

- Vendor document review log (ART-FB61C5F7B1) — final revision in document control.
- Package acceptance and turnover checklist (ART-8F50EF826E) — signed final revision.
- Factory/shop test and inspection evidence (ART-2E1BDD099B) — bundle indexed in the turnover package.
- Turnover evidence package (composition `TBD`) — indexed in document control and handed to DEL-036-03 consumers.
- Human rulings for CFL-036-06-001, -002, -003 — recorded in deliverable `MEMORY.md` when created.
