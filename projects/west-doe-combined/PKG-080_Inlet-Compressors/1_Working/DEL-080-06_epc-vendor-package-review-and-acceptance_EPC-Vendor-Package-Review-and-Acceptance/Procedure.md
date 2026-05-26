# Procedure — DEL-080-06 EPC Vendor Package Review and Acceptance

**Interpretation:** This procedure describes the steps the EPC Integrator follows to **produce** the acceptance evidence artifacts for the vendor-engineered Inlet Compressors package (PKG-080).

## Prerequisites

- DEL-080-01 Scope of Work (PKG-080) issued/available (peer deliverable).
- DEL-080-02 Package Datasheet (PKG-080) issued/available (peer deliverable).
- DEL-080-03 Construction Work Package (PKG-080) issued/available (peer deliverable).
- DEL-080-04 Vendor Engineered Equipment Package (PKG-080) submitted by Package Vendor.
- DEL-080-05 Vendor Document Turnover Package (PKG-080) submitted by Package Vendor.
- `_REFERENCES.md` — Gate 7 PROJECT_DECOMP snapshot reachable; PKG-080 register row and SOW-0119..SOW-0122 entries accessible.
- ASSUMPTION: declared upstream dependencies are `None declared during PREPARATION` (`_DEPENDENCIES.md`); peer DEL-080-01..-05 are treated as effective upstream by package logic but are not formally declared as edges. TBD: confirm whether dependency-extract should be run.
- Access (locally or via vendor data room) to: `26020-Package_Requirements.docx` package heading 33; relevant DBM slice (`DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`); applicable NACE clauses. TBD where not locally accessible.

## Steps

1. **Establish acceptance basis.** Confirm the issued versions of DEL-080-01, DEL-080-02, and DEL-080-03 to be used as the acceptance basis. Record version IDs in the acceptance checklist header.
2. **Build the vendor document review log.** Enumerate every vendor document in DEL-080-05. For each, record: document ID, title, revision, EPC reviewer, review date, comment status (Code 1/2/3 or equivalent — exact coding TBD per project document control standard), and disposition (Accepted / Accepted with comments / Rejected).
3. **Engineering and design conformance review.** For each requirement in the EPC Scope of Work (DEL-080-01) and each datasheet line in the Package Datasheet (DEL-080-02), record conformance disposition against the vendor's package engineering (DEL-080-04). Flag non-conformances as NCRs.
4. **Scope-item verification.** Verify against SOW-0120, SOW-0121, SOW-0122:
   - Two identical parallel sour inlet gas reciprocating compressor packages supplied.
   - Two (2) Ariel KBZ/6 separable reciprocating compressors with two-stage compression, intercooling and aftercooling.
   - Modular self-framing buildings, piping, instrumentation, electrical, HVAC, package auxiliaries supplied.
   - 2 x 50% configuration with no dedicated spare.
   - Sour-service NACE-compliant materials and seals.
   - Operating envelope: per-unit ~40 MMSCFD, combined ~80 MMSCFD; suction ~1275 kPag; discharge ~6550 kPag (confirm vendor as-engineered values; record any deviation).
5. **Interface verification matrix.** For each interface type declared for PKG-080 (Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports), record interface owner, tie-in points, design conditions, and conformance disposition.
6. **Safety/regulatory review (OBJ-009).** Confirm sour-service, fire and gas, relief/flare/vent, drain/containment, emissions, and code/standard expectations are addressed in vendor documents. Cite source clauses where locally available; mark `TBD` where unavailable.
7. **Commercial/stream-boundary review (OBJ-003).** Confirm stream disposition, metering, and tie-in limits for sour/sales gas are reflected in vendor documents and interface verifications. ASSUMPTION via OBJ-003 package-heuristic association.
8. **Test and inspection evidence collation.** Collect ITR/ITP completion records, witness/hold-point sign-offs, NCR register and closeouts, FAT records, and SAT records (as applicable) for each package unit.
9. **Open-item register and closure plan (OBJ-010).** Maintain an open-item register for every conditional-acceptance item or outstanding NCR. Assign owner, target closure date, and closure evidence requirement.
10. **Turnover evidence assembly.** Assemble mechanical completion records, system turnover packages, and the open-item closure status as the handoff evidence record.
11. **EPC acceptance disposition.** Record overall EPC acceptance disposition per package unit: Accepted / Conditionally Accepted (with open-item list) / Rejected (with NCRs and remediation requirements).
12. **Issue acceptance evidence set.** Issue the four artifacts (review log, acceptance checklist, test/inspection evidence, turnover evidence) and update `_STATUS.md` consistent with the package lifecycle.

## Verification

- Every reviewed vendor document has a disposition recorded in the review log (no blanks).
- Every requirement in DEL-080-01 and every datasheet line in DEL-080-02 is reflected on the acceptance checklist with a disposition.
- Every declared interface type for PKG-080 appears in the interface verification matrix with a disposition.
- Sour-service / NACE compliance is explicitly confirmed (not silently assumed).
- All NCRs have a closure path; the open-item register reconciles to the acceptance checklist.
- Per-unit traceability is preserved for the two package units (no aggregated-only evidence for safety-critical scope).

## Records

- Vendor document review log (per package unit and consolidated).
- Package acceptance checklist (per package unit and consolidated).
- Test/inspection evidence package: ITR/ITP completion records, witness sheets, NCR register and closeout records, FAT and SAT records.
- Open-item register and closure evidence (OBJ-010).
- Turnover evidence package: mechanical-completion records, system turnover records, controlled open-item closure record.
- Signed EPC acceptance disposition per package unit.
