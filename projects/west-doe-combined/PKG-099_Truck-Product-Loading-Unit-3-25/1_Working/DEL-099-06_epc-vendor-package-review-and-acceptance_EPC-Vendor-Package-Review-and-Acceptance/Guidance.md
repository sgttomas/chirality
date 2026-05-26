# Guidance — EPC Vendor Package Review and Acceptance (DEL-099-06)

> Directional document. Why this review/acceptance deliverable exists, principles to apply, considerations, trade-offs, and the Conflict Table for human ruling.

## Purpose

This deliverable produces the evidence that the EPC Integrator has reviewed the Truck Product Loading vendor package (DEL-099-04), reviewed the vendor's documentation turnover (DEL-099-05), and concluded that the package is acceptable for integration into the Unit 3-25 liquids hub against the EPC Scope of Work (DEL-099-01), Package Datasheet (DEL-099-02), and Construction Work Package (DEL-099-03). It is the closing acceptance artifact for PKG-099 from the EPC Integrator's perspective.

## Principles

1. **Acceptance is human authority.** The EPC Integrator (and Owner where required) signs acceptance; this deliverable supplies evidence to support that decision but does not itself certify (K-AUTH-1).
2. **Source-grounded acceptance.** Acceptance statements must trace to the EPC SOW, Package Datasheet, CWP, vendor submittals, and to the DBM where the design basis is in question.
3. **Boundary clarity.** Custody, scope, and interface boundaries (especially the LACT/NRM third-party boundary at the tie-in flange) are explicit acceptance topics, not assumptions.
4. **Explicit deferrals.** Items not resolvable at acceptance are recorded as punchlist items with owner and date — they are not silently closed.
5. **Integration over isolation.** The package is accepted as a part of the wider Unit 3-25 facility (fire/gas, ESD, BPCS, civil, electrical), not only as a stand-alone skid.

## Considerations

- **Quantity verification.** DBM SEC-06 fixes three loading stations and three loading pumps; vendor count deviations require explicit dispositioning.
- **Hydraulic verification.** DBM SEC-06 fixes 103 m3/h at 345 kPad per station; vendor curves and FAT data should bracket this duty point.
- **Cold-climate verification.** -40 deg C ambient design (DBM SEC-04) drives heat tracing, building heating, instrument winterization, and material selection; acceptance must not silently accept a milder vendor basis.
- **Fire/gas and shutdown.** LEL, H2S, methyl mercaptan, and fire detection (DBM SEC-16) and shutdown coordination with BPCS/RIO/ESD (DBM SEC-17) are integration-side requirements that frequently lag vendor-only design and must be explicitly checked.
- **Civil/spill control.** Truck-loading slab geometry, traffic flow, and spill containment (DBM SEC-13) sit at the EPC/Civil/Vendor boundary and are common sources of late punchlist items.
- **Permitting.** DBM SEC-18 notes that a truck rack permit amendment is required against BCER 100120203; this is an external dependency to surface in the acceptance package.

## Trade-offs

- **Conditional vs full acceptance.** Conditional acceptance lets schedule proceed but transfers risk to punchlist closure; full acceptance withholds closure until everything clears but may block downstream turnover.
- **Document-only vs witnessed verification.** Document review is cheaper and faster; witnessed FAT/SAT/loop checks are more expensive but reduce field surprises during commissioning.
- **EPC-led vs Vendor-led closeout.** EPC-led closeout improves integration assurance; Vendor-led closeout can be faster where vendor familiarity dominates. The decomposition assigns lead to the EPC Integrator with Package Vendor input.
- **Scope of test/inspection evidence.** Broader evidence sets (NDE, hydrotest, electrical loop, fire/gas, ESD) reduce residual risk but increase coordination cost; the acceptance checklist should make the chosen scope explicit.

## Examples

- *Quantity check:* Vendor P&ID shows three loading stations with one P-XXXX condensate loading pump per station → REQ-1 satisfied; recorded in review log row for the relevant vendor drawing.
- *Hydraulic check:* Vendor pump curve at duty point 103 m3/h / 345 kPad with FAT performance test report → REQ-2 satisfied; recorded under V-1/V-2.
- *Boundary check:* Tie-in list and interface drawing show LACT skid as third-party NRM, with facility scope ending at the tie-in flange → REQ-3 satisfied; recorded under V-3.

(Additional source-specific examples beyond DBM coverage: TBD pending access to the package-requirements document and workbook row.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFT-1 | Objective association (OBJ-002 ... OBJ-010) is asserted by `_CONTEXT.md` but PACKAGE_HEURISTIC was used (no deliverable-level mapping was directly verified during this run). | `_CONTEXT.md` Supports Objectives | `OBJECTIVE_DELIVERABLE_MAP.csv` (not directly parsed in this run) | Datasheet §Identification, Specification §Scope | Keep associations as ASSUMPTION until deliverable-level mapping is confirmed. | TBD |
| CFT-2 | Package-level EPC requirements text exists in `26020-Package_Requirements.docx` heading 51 and `Workbook Packages row 98`, but neither was readable as text during this run; package-specific requirements may exist that this draft does not capture. | `_REFERENCES.md` (cited) | Source files (`.docx`/`.xlsx`, not text-accessible) | Specification §Requirements, §Standards | Treat referenced package-requirements text as ASSUMPTION present; convert specific requirements to TBD until human extracts text. | TBD |
| CFT-3 | Permit status for the truck rack (BCER 100120203 amendment) per DBM SEC-18 may evolve and affect acceptance preconditions. | DBM SEC-18 (line 872) | Project permitting status (live; not in folder) | Specification REQ-14, Procedure §Prerequisites | Carry permit status as a live precondition in the acceptance checklist; do not accept the package without confirmed permit status disposition. | TBD |
| CFT-4 | Final test/inspection scope (NDE, hydrotest, fire/gas, ESD coverage) is not enumerated in available sources at the package-acceptance level. | (no direct source) | DBM SEC-09, SEC-16, SEC-17 (general only) | Specification REQ-10, Procedure §Steps | Adopt EPC standard inspection set; require human ruling on inclusion/exclusion of each test family. | TBD |
