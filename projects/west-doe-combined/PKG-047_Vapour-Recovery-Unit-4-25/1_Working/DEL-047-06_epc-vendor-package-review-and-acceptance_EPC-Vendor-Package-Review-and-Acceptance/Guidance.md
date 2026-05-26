# Guidance — DEL-047-06 EPC Vendor Package Review and Acceptance

## Purpose

This deliverable provides the EPC Integrator's evidentiary record that the Package Vendor's VRU package (PKG-047) is reviewed against the EPC-authored inputs (Scope of Work DEL-047-01, Package Datasheet DEL-047-02, Construction Work Package DEL-047-03) and is acceptable for integration into the wider facility. It is the bridge between vendor-owned engineering/documentation and EPC-owned facility integration and turnover.

Source: DELIVERABLE_REGISTER.csv row DEL-047-06; PACKAGE_REGISTER.csv row PKG-047 (Package Vendor vs. EPC Integrator responsibility split).

## Principles

1. **Responsibility split is the spine of the review.** The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration). Every review entry should be locatable on one side of that line. (Source: PACKAGE_REGISTER.csv row PKG-047.)
2. **Two 100% trains, lead-lag, one building.** Acceptance must treat both trains as independently complete and the shared building/ancillaries as a common scope, not as a single composite. (Source: PACKAGE_REGISTER.csv row PKG-047.)
3. **Sour service governs metallurgy and pressure boundaries.** Reviewers should treat any silence on sour-service qualification as a gap, not as compliance. (Source: PACKAGE_REGISTER.csv row PKG-047 "sour service"; specific standard list `TBD`.)
4. **Acceptance is human.** Agents may compile the review log, but the acceptance decision is authored by a human (ASSUMPTION: project governance default K-AUTH-1; not from package source).

## Considerations

- The decomposition lists thirteen interface types for PKG-047. The acceptance checklist should make each interface type explicit; "no comment" entries are still acceptance evidence and should be recorded as such.
- Vendor document availability (DEL-047-05) is a precondition for completing the review. If submittals are missing at the time of acceptance, the gaps must be enumerated rather than assumed away.
- The Construction Work Package (DEL-047-03) defines the installation, tie-in, and turnover workflow this deliverable's evidence ultimately feeds; alignment with that workflow should be checked rather than re-invented.
- Test/inspection scope (FAT, SAT, NDE, hydrotest, performance) is not enumerated in accessible decomposition sources at the deliverable level. The specific required set should be confirmed against `26020-Package_Requirements.docx` package heading 2 once that slice is local; until then, treat test scope items as `TBD`.

## Trade-offs

- **Breadth vs. evidentiary depth.** Reviewing every vendor document in detail is impractical; a risk-weighted depth (full review for safety-critical and sour-service items; spot review for non-critical) is preferable. ASSUMPTION — not specified by accessible sources.
- **Integration acceptance vs. mechanical completion.** Integration acceptance can proceed on interface readiness even when minor punch-list items remain on the physical package; the turnover evidence index should make this distinction explicit.
- **Vendor variance vs. EPC scope changes.** Where vendor deviations from the Package Datasheet are unavoidable, the EPC Integrator must decide whether to accept, require redesign, or absorb the change into a downstream EPC document. Recording the decision and its basis preserves auditability.

## Examples

Examples specific to the PKG-047 vendor submittals are TBD until the vendor submittal list materializes through DEL-047-04 and DEL-047-05. Once available, exemplars belong in this section by reference, not by duplication.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-01 | Specific test/inspection set required for PKG-047 (FAT/SAT/NDE/hydro/performance) is not enumerated in accessible deliverable-local sources. | DELIVERABLE_REGISTER.csv row DEL-047-06 ("test/inspection evidence" listed generically) | `26020-Package_Requirements.docx` package heading 2 (location TBD; not local) | Specification R-04; Procedure step 4 | Resolve by slicing 26020 heading 2 into `_REFERENCES.md`-linked local material, then update Specification R-04 and Procedure step 4. | TBD |
| C-02 | Applicable sour-service standards not enumerated in accessible deliverable-local sources. | PACKAGE_REGISTER.csv row PKG-047 ("sour service") | NACE MR0175 / ISO 15156 (ASSUMPTION) | Specification R-05; Datasheet Attributes (service) | Confirm against vendor RFQ (`26020-01-PT-RFQ-12-002_VRU_2_R0.docx`) and DBM-Deepcut `4-25_Deepcut_DBM.md`. | TBD |
