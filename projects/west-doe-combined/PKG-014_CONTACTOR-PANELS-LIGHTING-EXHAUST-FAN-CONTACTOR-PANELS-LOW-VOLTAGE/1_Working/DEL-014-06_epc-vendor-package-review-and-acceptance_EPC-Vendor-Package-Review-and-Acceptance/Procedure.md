# Procedure — DEL-014-06 EPC Vendor Package Review and Acceptance

## Purpose

Operational steps for the EPC Integrator to execute the vendor package review and produce the acceptance evidence set (vendor document review log, package acceptance checklist, test/inspection evidence, turnover evidence) for PKG-014.

## Prerequisites

- Upstream EPC basis deliverables for PKG-014 are available and at a maturity state permitting reliance (see HRR-014-06-001):
  - DEL-014-01 Scope of Work
  - DEL-014-02 Package Datasheet
  - DEL-014-03 Construction Work Package
- Vendor-side deliverables are available for review:
  - DEL-014-04 Vendor Engineered Equipment Package
  - DEL-014-05 Vendor Document Turnover Package
- Access to accepted Gate 7 PROJECT_DECOMP snapshot for register-level identity confirmation.
- Access to DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md for electrical/integration basis.
- Declared upstream/downstream dependencies are recorded in `_DEPENDENCIES.md` (currently none declared).

## Steps

1. **Initialize acceptance dossier.** Create the acceptance evidence container with placeholder entries for the four required artifacts: vendor document review log, package acceptance checklist, test/inspection evidence, turnover evidence.
2. **Index vendor submissions.** From the DEL-014-05 vendor document register, populate the vendor document review log with one row per submitted vendor document/revision.
3. **Construct the acceptance checklist.** Build the package acceptance checklist by extracting acceptance lines from:
   - DEL-014-01 SOW deliverable items;
   - DEL-014-02 Package Datasheet attributes, requirements, and interface matrix;
   - DEL-014-03 Construction Work Package installation/turnover items;
   - PKG-014 interface set (Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports).
4. **Verify electrical compatibility.** Confirm vendor LV equipment characteristics match the project LV basis (600 V, 3 phase, 3 wire, 60 Hz HRG; lighting/utility 120/208 V) and grounding scheme. Record findings against the checklist.
5. **Verify controls integration.** Confirm exhaust-fan/heater control wiring tie-in to nearest Flex5000 RIO node where practical; review vendor I&C drawings. Record findings.
6. **Verify standby power continuity.** Confirm accepted loads' power continuity through the LV MCC + LV standby generator + transfer switch arrangement. Record findings; flag any open items (generator rating remains TBD at project basis).
7. **Verify environmental fitness.** Confirm vendor enclosure/equipment ratings against -40 deg C minimum ambient for exposed locations. Record findings.
8. **Verify mechanical/structural/maintenance interfaces.** Confirm foundations, supports, and maintenance-access provisions against the PKG-014 interface set and DEL-014-03 construction package.
9. **Collect test/inspection evidence.** File factory acceptance test, site acceptance test, and inspection records against the relevant checklist lines; cross-reference each evidence document.
10. **Disposition vendor documents.** For each vendor document review log entry, record disposition (accepted / accepted with comments / rejected) and resolution status.
11. **Assemble turnover evidence.** Verify DEL-014-05 turnover register completeness; file the turnover evidence dossier.
12. **Resolve or escalate open items.** Items not closeable by evidence become open items requiring human ruling; escalate per project change-control conventions.
13. **Issue acceptance.** When all checklist lines are dispositioned and open items are below the project acceptance threshold (threshold TBD per HRR-014-06-001), issue the signed acceptance record.
14. **Archive.** File the complete acceptance dossier in the deliverable folder per project records-management conventions.

## Verification

| Check | How verified |
|---|---|
| Vendor document review log is complete vs. DEL-014-05 register | Row-count and identity reconciliation |
| Acceptance checklist traces to DEL-014-01/02/03 | Traceability matrix review |
| Each PKG-014 interface has an acceptance disposition | Interface-by-interface walk |
| Test/inspection evidence is filed and referenced | Spot-check of references |
| Open items have an explicit disposition path | Open-item log review |
| Acceptance signature present from EPC Integrator owner | Signature verification |

## Records

- Vendor document review log (final, signed).
- Package acceptance checklist (final, signed).
- Test/inspection evidence file (compiled).
- Turnover evidence file (compiled).
- Open-item log with dispositions (working record).
- Acceptance issuance record (final).

All records are filed inside this deliverable folder or referenced from it; no records are written outside the deliverable scope by this procedure.
