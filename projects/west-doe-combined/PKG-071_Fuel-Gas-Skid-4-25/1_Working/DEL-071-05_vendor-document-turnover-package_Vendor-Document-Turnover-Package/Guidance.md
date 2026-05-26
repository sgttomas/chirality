# Guidance — DEL-071-05 Vendor Document Turnover Package (PKG-071 Fuel Gas Skid 4-25)

## Purpose

This guidance explains why the vendor document turnover package exists for PKG-071, how to interpret the four-document set for this deliverable in the absence of a locally readable project-level package-requirements source, and which areas of judgment are sensitive enough that they should be deferred to human ruling or to vendor confirmation rather than asserted from convention.

The deliverable exists because PKG-071 Fuel Gas Skid 4-25 is a vendor-furnished equipment package. The Owner / EPC requires the vendor to deliver a controlled, auditable documentation set so that the skid can be installed, commissioned, operated, maintained, and re-certified across its life cycle, and so that the Owner can demonstrate code compliance and trace each delivered document to a project-controlled register. (Source: `_CONTEXT.md` Scope and Anticipated Artifacts; Notes.)

## Principles

1. **Single vendor owner, EPC review.** The Package Vendor authors the documentation; the EPC Integrator reviews for interface/integration consistency. The vendor is accountable for content correctness; the EPC is accountable for ensuring the content integrates with the rest of the plant (Source: `_CONTEXT.md` ResponsibleParty).
2. **Register-first.** The Vendor Document Register is the navigational and contractual spine of the turnover package. All other artifacts hang off it (ASSUMPTION — standard practice; specific register schema TBD).
3. **Artifact rows are evidence, not deliverables.** Individual source vendor documents listed in the decomposition are evidence rows of this deliverable, not separate deliverables (Source: `_CONTEXT.md` Notes).
4. **Source fidelity for technical content.** Vendor data must match the LP fuel gas system design basis (DBM-Deepcut L1839-L1903). Where the vendor proposes deviation, deviation must be raised through the project change-control process before fabrication.
5. **Revision discipline equals turnover quality.** Hand-Over readiness is a property of the register: every entry must be at its terminal revision class before Hand-Over is asserted (ASSUMPTION — class names TBD).

## Considerations

- **Binary source inaccessibility.** The canonical project source (`26020-Package_Requirements.docx` heading 25, and `26020-Packages_Interfaces_4_export.xlsx` row 61) is in binary formats that are not locally readable in plain-text form. Significant portions of this deliverable's normative content (vendor document classes, register columns, revision-class naming, format requirements) are therefore marked TBD or ASSUMPTION. Drafters at the next pass should obtain plain-text extracts or a vendor master document register before lifting TBDs to FACT.
- **Shared-utility implications.** The fuel gas skid is a shared utility (04-25/03-25 coordination). Vendor documentation that references "plant fuel gas demand" or "buyback sizing" should be reviewed against the still-open demand-split TBDs in DBM-Deepcut L1830, L1841.
- **Sour-service exposure.** Sweet gas purge for sour service is a sensitive area; vendor materials documentation should explicitly address sour-service compatibility, mercaptan exposure, and purge media. Do not assume fuel gas purge alone is sufficient (Source: DBM-Deepcut L1899).
- **Emergency generator interface.** Vendor documentation must reflect the < 66 psig pressure ceiling for generator fuel and the 0.468 MMSCFD / 3.6 MMSCFD-for-30-s start-gas duty (Source: DBM-Deepcut L1870).
- **Objective association is best-effort.** OBJ-001/004/005/006/007/008/009/010 are recorded as supporting objectives by package-grouping heuristic (`OBJECTIVE_ASSOCIATION_MODE = PACKAGE_HEURISTIC`); they are not contractual until the human-confirmed objective map is published.

## Trade-offs

- **Strict register schema vs vendor latitude.** A rigid EPC-imposed register schema simplifies integration but constrains vendors with established document-control systems. The project-level numbering and column standard is TBD; choose deliberately.
- **Native + PDF vs PDF-only.** Native files enable downstream re-use (BIM, GIS, asset management) but increase IP and version-control burden. The project requirement is TBD.
- **Early partial turnover vs single final turnover.** Staged turnover (per milestone) reduces commissioning risk but raises register reconciliation cost. The milestone schedule for this deliverable is TBD.

## Examples

Examples and worked patterns are deferred pending access to either (a) the project document-control plan or (b) a vendor master register. Until then, drafted register schemas and revision-class names would be authored from convention rather than source and are therefore omitted (Source-grounding rule).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-1 | OBJ list in `_CONTEXT.md` for DEL-071-05 (OBJ-001/004/005/006/007/008/009/010) is asserted by package heuristic, not by an explicit objective-to-deliverable map row | `_CONTEXT.md` Supports Objectives | `OBJECTIVE_DELIVERABLE_MAP.csv` (snapshot) at deliverable-ID granularity | Datasheet Identification; Guidance Considerations | Treat as ASSUMPTION pending confirmation from objective map at deliverable-ID resolution | TBD |
| C-2 | Vendor document class list and register schema asserted as ASSUMPTION because `26020-Package_Requirements.docx` heading 25 is not locally readable | Datasheet Construction; Specification R-2 | `26020-Package_Requirements.docx` heading 25 (binary; not readable) | Specification R-1, R-2, R-5, R-6, R-7 | Extract the binary source to markdown and re-anchor the requirements before lifting TBDs | TBD |
