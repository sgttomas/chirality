# Procedure — DEL-072-06 EPC Vendor Package Review and Acceptance

## Purpose

Procedure for the EPC Integrator to execute review and acceptance of the PKG-072 vendor package, producing the evidence set described in the Datasheet and Specification.

## Prerequisites

- **Acceptance-basis documents available at INITIALIZED or later:**
  - DEL-072-01 EPC Scope of Work
  - DEL-072-02 Package Datasheet
  - DEL-072-03 Construction Work Package
- **Vendor production unit deliverables submitted:**
  - DEL-072-04 Vendor Engineered Equipment Package
  - DEL-072-05 Vendor Document Turnover Package
- **Source references accessible:**
  - 4-25_Deepcut_DBM.md
  - 26020-Package_Requirements.docx package heading 26 (location TBD — binary source not parsed)
  - 26020-Packages_Interfaces_4_export.xlsx Packages row 99 (location TBD — binary source not parsed)
- **Authority:** EPC Integrator review/acceptance authority designated; human ruling channel available for CONFLICT items.
- **Open items from Guidance Conflict Table reviewed**, including the package-label-vs-equipment reconciliation (CONFLICT-0).

## Steps

1. **Confirm acceptance basis and package identity.** Obtain the latest issued revisions of DEL-072-01, DEL-072-02, DEL-072-03 and record revision identifiers. Reconcile the workbook package label with the tagged-equipment list per CONFLICT-0; record the agreed acceptance object.
2. **Receive vendor submittal package** (DEL-072-04 outputs and DEL-072-05 register). Confirm transmittal completeness against the DEL-072-05 register.
3. **Document review.** For each item in the DEL-072-05 register, evaluate the vendor document against the corresponding SOW/Datasheet/CWP requirement. Log conformance, deviation, or missing entries in the vendor document review log (per REQ-1, REQ-2, REQ-3, REQ-4).
4. **Package boundary envelope check.** Confirm the vendor design envelopes the SOW-0248 boundary values per Specification REQ-5 (Design Flow > 8.4 MMSCFD; Operating Pressure 150 psig; Design Pressure 150 psig; Design Temperature -40 C to 35 C). Carry Final Flow and MAWP as TBD.
5. **Service-envelope check.** Confirm the vendor design covers the LP fuel-gas service envelope per Specification REQ-6 (normal source upstream of expander-compressor; H2O < 0.1 ppmv normal, <= 4 lb/MMSCF upset; H2S < 6 mg/m3; J-T-mode supply pressure up to 2895 kPag high). Record discrepancies as deviations. Cross-facility demand split (CONFLICT-1) recorded as TBD; do not close.
6. **Site-basis check.** Confirm winterization, heat tracing, panel ratings, structural loads, and material selection against the -40 deg C / +35 deg C envelope, 673 m AMSL elevation, snow loads Ss 2.5 kPa / Sr 0.2 kPa, and wind pressure q(1/50) 0.40 kPa per Specification REQ-7.
7. **Regulator and start-gas review.** Verify 2 x 100% regulator sparing, individual isolation, outlet test connections, pilot isolation on pilot-type regulators, and quick-acting internally-sensing start-gas regulators per Specification REQ-8. Inspect P&ID and instrument index entries.
8. **Emergency-generator supply review.** Verify < 66 psig supply pressure for classification compliance, design flow 0.468 MMSCFD, start-gas 3.6 MMSCFD for 30 s, and combined-case piping/vessel sizing per Specification REQ-9.
9. **Scrubber and heater review.** Verify scrubber sizing at K = 0.35 Imperial (operating-pressure derated), liquids routing (DBM basis to TK-9130-1), and the electric resistance heater control narrative (SCR; skin-temperature thermocouple override; gas outlet control) per Specification REQ-10. Carry heater duty as TBD pending DE.
10. **Test/inspection review.** Review or witness FAT, SAT, pressure tests, NDE, and functional tests per the vendor ITP. Collect certificates, reports, and traceability records (REQ-11). Specific test plan content TBD pending vendor ITP.
11. **Construction interface and turnover review.** Walk the package against DEL-072-03 tie-in/turnover checklist. Resolve or punchlist tie-in non-conformities. Confirm mechanical-completion conditions (REQ-3, REQ-12).
12. **Hazard review confirmation.** Confirm the sweet-gas purge / methyl-mercaptan hazard review (DBM sec. Emergency Buyback and Purge) has been executed or recorded as an open item per REQ-13.
13. **Compile acceptance checklist** covering REQ-1 through REQ-14 with status (ACCEPTED / DEVIATION / TBD / NEEDS_HUMAN_RULING) and source citations (REQ-15).
14. **Open-items register.** Itemize all TBD and NEEDS_HUMAN_RULING entries, including CONFLICT-0, CONFLICT-1, CONFLICT-2, CONFLICT-3, and any newly surfaced conflicts.
15. **EPC Integrator sign-off proposal.** Propose acceptance status (ACCEPT / ACCEPT WITH PUNCHLIST / REJECT) for human authority decision. The Integrator records the evidence; the human authority makes the binding decision (per K-AUTH-1 — ASSUMPTION).
16. **Turnover transmittal.** On human-authority acceptance, package the acceptance dossier and transmit to commissioning with mechanical-completion certificate and signed turnover.

## Verification

- All Specification requirements (REQ-1 through REQ-15) have a corresponding checklist entry with status and source citation.
- Vendor document review log entries reconcile against the DEL-072-05 register (no orphan or missing items unaccounted for).
- Open-items register contains every TBD/NEEDS_HUMAN_RULING entry from the checklist.
- Test/inspection evidence dossier is complete per the vendor ITP, or non-completeness is recorded as a punchlist item.
- Turnover evidence dossier carries mechanical-completion certificate and signed transmittal (or recorded as outstanding).
- Hazard-review confirmation record (REQ-13) is present or explicitly open.
- Acceptance decision (ACCEPT / ACCEPT WITH PUNCHLIST / REJECT) is recorded against a human authority.

## Records

- Vendor document review log
- Package acceptance checklist (REQ-1 through REQ-15)
- Test/inspection evidence dossier (FAT, SAT, NDE, pressure-test, functional-test reports)
- Turnover evidence dossier (mechanical-completion certificate, punchlist, signed transmittal)
- Hazard-review confirmation record
- Open-items register
- Acceptance decision record (human-authored)
