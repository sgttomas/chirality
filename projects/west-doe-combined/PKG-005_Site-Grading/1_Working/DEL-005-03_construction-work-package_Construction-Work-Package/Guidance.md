# Guidance: DEL-005-03 Construction Work Package

## Purpose

The Construction Work Package translates the accepted `PKG-005` Site Grading scope into an EPC Integrator construction-control package. Its role is to make physical installation, drainage/containment interfaces, inspection, turnover, and tie-in readiness explicit without inventing discipline detail that is not present in the accepted source set.

## Principles

- Use the Gate 7 snapshot for package identity, deliverable identity, objective mapping, and artifact expectations.
- Use the 3-25 DBM as the governing source for site conditions, civil design basis, drainage, roads/access, foundations, buildings, and standards-register caveats.
- Keep package-specific exclusions, drawing lists, geotechnical final values, hydrology updates, and detailed construction sequences as `TBD` until accepted source material is available.
- Treat objective associations as contextual support, not new requirements, except where the Gate 7 deliverable and package rows explicitly assign them.
- Do not promote interface facts into separate deliverables; keep them as construction interface and turnover checklist content.

## Considerations

The key drafting risk is overclaiming readiness. The DBM identifies several civil foundations for construction planning, but also makes final geotechnical closure and hydrology updates unresolved. For this reason, the CWP should include hold points rather than assert final foundation, pile, settlement, frost-protection, or retention pond sizing criteria.

The package is source-limited. The Gate 7 registers identify workbook row 6 and the 3-25 DBM, but PREPARATION did not copy a deliverable-specific source slice or IFC drawing package. A usable CWP can be initialized from the accepted basis, but construction release requires human or project-team confirmation of the missing drawing, geotechnical, hydrology, and permit inputs.

## Trade-offs

| Topic | Direction |
|---|---|
| Specificity vs. fidelity | Prefer `TBD` and hold points over invented construction methods or dimensions. |
| Interface completeness | Include known interface types now; require construction review to complete detailed interface parties and signoffs. |
| Civil readiness | Capture DBM civil requirements now; do not close final foundation or drainage design until final geotechnical and hydrology inputs are accepted. |
| Regulatory readiness | Record permit-related gaps without assigning detailed agency workflow not present in the source set. |

## Examples

- Acceptable: "Drainage and containment interface checklist shall address Drain / Containment and Grading / Site Drainage / Spill Containment interfaces."
- Not acceptable without more source: "Retention pond volume shall be X m3."
- Acceptable: "Foundation design closure requires final geotechnical report acceptance."
- Not acceptable without more source: "Use pile type X at spacing Y."

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HRR-001 | Package-specific civil IFC drawing list is not available in the deliverable-local source set. | `_REFERENCES.md` Missing / Deferred References | DBM-Comp_and_Liquids SEC-11 requires plot plan and civil drawing verification before final issue. | Datasheet Construction; Specification Documentation; Procedure Prerequisites | Treat current documents as initialized only; require human/project input before construction release. | TBD |
| HRR-002 | Final geotechnical report is required for foundation design closure but is not available locally. | DBM-Comp_and_Liquids SEC-02 and SEC-11 | Current deliverable folder has no geotechnical report reference. | Specification Requirements; Procedure Verification | Retain geotechnical acceptance as a hold point. | TBD |
| HRR-003 | Hydrology and retention pond sizing basis remains provisional. | DBM-Comp_and_Liquids SEC-02 and SEC-11 | No site-specific hydrology update is referenced in deliverable context. | Datasheet Conditions; Specification Standards; Procedure Steps | Use current DBM basis for initialization and require hydrology update before final drainage design closure. | TBD |
| HRR-004 | Waste management permit details are required but regulation, format, agency workflow, and attachments are TBD in the source set. | DBM-Comp_and_Liquids SEC-15 Specifications, Codes, and Standards | Current deliverable folder has no permit register. | Specification Standards; Procedure Prerequisites | Keep permit details as a construction-readiness hold point. | TBD |
