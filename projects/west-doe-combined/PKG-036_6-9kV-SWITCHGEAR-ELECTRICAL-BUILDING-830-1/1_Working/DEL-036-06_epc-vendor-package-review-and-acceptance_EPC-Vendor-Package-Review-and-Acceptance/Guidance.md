# Guidance — DEL-036-06 EPC Vendor Package Review and Acceptance

## Purpose

This deliverable exists so that the EPC Integrator can demonstrably accept the PKG-036 vendor package (a 6.9 kV switchgear electrical building, 830-1) for integration into the West Doe Deepcut facility. It is the EPC-side counterpart to the vendor production deliverables (DEL-036-04, DEL-036-05). Acceptance evidence supports project objectives OBJ-001 and OBJ-004 through OBJ-010 as mapped in the Gate 7 OBJECTIVE_DELIVERABLE_MAP.

## Principles

- **EPC Integrator owns facility integration.** Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator accepts vendor work against EPC documents and integrates into the facility (PACKAGE_REGISTER.csv row PKG-036 Responsibility text; DBM source slice for Electrical Buildings).
- **Acceptance is evidence-based, not narrative.** Every acceptance decision should reference a vendor document ID/revision and the corresponding clause in DEL-036-01 SOW, DEL-036-02 Datasheet, or DEL-036-03 CWP.
- **Code and project-standard compliance is non-negotiable.** Acceptance requires evidence of CSA C22.1-21 compliance and conformance to the project ELC-QAS-* electrical specifications referenced in the DBM (Table 12-1).
- **Interface acceptance is itemized.** The package has at least 12 declared interface types (PACKAGE_REGISTER.csv row PKG-036); each should be discharged with vendor evidence and EPC acceptance signoff rather than rolled into a single global acceptance.

## Considerations

- The package title carries an apparent classification mismatch (see Conflict Table CFL-036-06-001 below). Until the conflict is ruled, acceptance work should record both the workbook identity (6.9 kV at 830-1) and any vendor-documented voltage class on the actual equipment supplied, and flag any discrepancy on the review log.
- The DBM uses 6.9 kV at the motor control center level (DBM lines 2935, 2955), not the switchgear level, for medium-voltage service to AC inverter-drive motors rated 5,500 hp and above. Acceptance reviewers should not assume "6.9 kV switchgear" without confirming the vendor SLD; this affects which ELC-QAS specification (Medium Voltage Switchgear vs. Medium Voltage Motor Control Centers) is primary for clause-level compliance review.
- Detailed acceptance criteria depend on ELC-QAS-000003-001 and ELC-QAS-000007-001 clause text, which is not in the locally accessible source set. Acceptance work should not proceed to final signoff until those source slices are available.
- The deliverable has no declared upstream/downstream dependencies in `_DEPENDENCIES.md`, but the peer deliverables DEL-036-01, -02, -03 are de facto upstream inputs to this review and DEL-036-04, -05 are the vendor outputs being reviewed. Treat these as ASSUMPTION-level edges and surface them when `TASK + dependency-extract` is run.

## Trade-offs

- **Witness vs. document-only acceptance of FAT.** Witnessing factory tests provides stronger evidence but costs schedule and travel; document-only acceptance relies on vendor test record quality. The choice is project-policy driven and is `TBD` for this package.
- **Single combined acceptance checklist vs. interface-by-interface checklists.** A combined checklist is simpler; interface-by-interface checklists better support the 12 declared interface types and downstream integration tracking. Interface-by-interface is recommended (see Principle 4) but adds review overhead.
- **Acceptance gate placement.** Acceptance can gate at vendor document submittal, at FAT, at delivery, or at turnover. Aligning gates with DEL-036-03 CWP construction sequencing is preferred but introduces coordination dependency.

## Examples

- ELC-QAS-000003-001 "Electrical Requirements for Packaged Equipment" Rev 2 is named in the DBM Table 12-1 as the project standard for packaged equipment; acceptance checklist items for vendor-supplied electrical equipment should trace to this specification (clause-level text TBD).
- ART-2E1BDD099B "Factory/shop test and inspection evidence" is named in the ARTIFACT_REGISTER as an expected artifact; a representative example for medium-voltage switchgear would include dielectric test reports, mechanical operation tests, primary/secondary injection relay test records, and HV insulation resistance records (illustrative basis: standard medium-voltage switchgear factory tests; specific scope is TBD pending ELC-QAS-000007-001 clause text).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CFL-036-06-001 | Package title says "6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1)" but DBM building-tag table identifies 830-1 as "4.16kV Acid Gas/Overheads Compressor Electrical Building"; DBM identifies 820-1 as the "6.9kV Inlet/Sales Compressor Electrical Building". | PACKAGE_REGISTER.csv row PKG-036 (Workbook Packages row 38) | _Sources/DBM-Deepcut/4-25_Deepcut_DBM.md line 2813 (building-tag table) and line 2812 (820-1 row) | Datasheet Identification & Conditions; Specification REQ-036-06-004 (which ELC-QAS standard is primary); Guidance considerations | PROPOSAL: treat the workbook identity (PKG-036 = 830-1, 6.9 kV switchgear) as authoritative for deliverable identity and surface the DBM building-tag mismatch for resolution at detailed engineering; either (a) reconcile DBM building-tag table to workbook, or (b) re-assign PKG-036 to building tag 820-1. | TBD |
| CFL-036-06-002 | "Switchgear" vs. "Motor Control Center" for 6.9 kV. DBM applies 6.9 kV at the MCC level for AC inverter-drive motors rated 5,500 hp and above (DBM line 2935, 2955); package title applies 6.9 kV at the switchgear level. | _Sources/DBM-Deepcut/4-25_Deepcut_DBM.md lines 2935, 2955 | PACKAGE_REGISTER.csv row PKG-036; DELIVERABLE_REGISTER.csv row DEL-036-06 (inherits) | Specification REQ-036-06-004 (governing ELC-QAS spec selection); Datasheet Construction (quality standards referenced) | PROPOSAL: until ruled, require acceptance review to confirm which 6.9 kV equipment classes the vendor actually supplies (switchgear, MCC, both) and apply ELC-QAS-000007-001 and ELC-QAS-000008-001 accordingly. | TBD |
| CFL-036-06-003 | No declared upstream/downstream dependencies in `_DEPENDENCIES.md`, but DEL-036-01/-02/-03 are clearly logical upstream inputs and DEL-036-04/-05 are the vendor outputs reviewed. | `_DEPENDENCIES.md` (no declared edges) | DELIVERABLE_REGISTER.csv peer rows in PKG-036; deliverable Description text for DEL-036-06 | Procedure prerequisites; Specification scope | PROPOSAL: declare upstream {DEL-036-01, DEL-036-02, DEL-036-03, DEL-036-04, DEL-036-05} as part of `TASK + dependency-extract` for this deliverable. | TBD |
