# Guidance: DEL-022-05_vendor-document-turnover-package

## Purpose

This deliverable is the single Package Vendor production unit that consolidates vendor documentation for PKG-022 5kV SWITCHGEAR EQUIPMENT into a controlled, transmitted, and reviewed turnover set. Its existence ensures that the EPC Integrator can integrate the package into the facility on the basis of an explicit, reviewed body of vendor data rather than ad-hoc submittals.

## Principles

- **Single-source vendor accountability.** One Package Vendor owns the entire vendor-document body for the package, even where the underlying source documents originate from sub-suppliers.
- **Interface-traceable documentation.** Every required vendor document should resolve to one or more of the six declared interface types so that the EPC Integrator's interface review can be evidenced.
- **Source fidelity over convention.** Where the project's vendor-data requirements are not yet visible in accessible source materials, mark the line item TBD rather than asserting a generic requirement set.
- **Artifacts, not deliverables.** Individual source vendor-document table rows are evidence under this deliverable; they are not standalone production units.
- **Separation from acceptance.** Producing the turnover package is this deliverable's scope; the EPC acceptance decision belongs to `DEL-022-06`.

## Considerations

- The artifact register currently records only `ART-E34A2C824B` ("TBD vendor document register") and explicitly flags the situation as Vendor Documentation Gap Evidence. Treat this as a known starting condition, not an error.
- `_Sources/26020-Package_Requirements.docx` is package-organized but contains no PKG-022 / 5kV switchgear section. Do not borrow a template from a different package without an explicit human ruling.
- The DBM Deepcut design basis describes 13.8 kV main switchgear and 4.16 kV motor control centers, plus 5 kV-insulation medium-voltage TECK cabling. None of these are an authoritative description of the PKG-022 equipment itself. Treat them as adjacent context only.
- The package name says "5kV SWITCHGEAR EQUIPMENT" but no accessible source describes a 5 kV-rated switchgear assembly for this facility. The exact voltage class and configuration of the PKG-022 equipment is TBD and may interact with what vendor documents are required.
- No upstream or downstream dependencies were declared during PREPARATION. The deliverable is not blocked by declared edges, but coordination with `DEL-022-04` (vendor engineered equipment package) and `DEL-022-06` (EPC review and acceptance) is structurally implied.

## Trade-offs

- **Comprehensive standard vendor data set vs. source-only requirements.** A comprehensive set (quality plan, datasheets, drawings, manuals, FAT records, spares list, certificates) is conventional for MV switchgear; however, asserting it as a requirement without project source backing exceeds source authority. The trade-off is resolved here by carrying that set only as ASSUMPTION-flagged guidance and as TBD requirements pending source confirmation.
- **Capturing source-required rows as embedded artifacts vs. controlled pointers.** Embedding preserves a turnover-time snapshot but increases storage; pointers reduce duplication but depend on continued source availability. Choice depends on the project's document-control policy (TBD).

## Examples

- A vendor document register row for a switchgear FAT report would trace to the Electrical Power and I&C / Control Cabling interfaces and to the source-required FAT row (when the source row exists).
- A grounding/bonding drawing in the submittal package would trace to the Grounding / Bonding interface and to whatever source-required electrical drawing list applies.

(Concrete examples are kept abstract because no source-confirmed PKG-022 vendor-document list is locally accessible.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-022-05-001 | Package name says "5kV SWITCHGEAR EQUIPMENT" but DBM and source documentation describe MV systems at 13.8 kV and 4.16 kV; only cable insulation is rated 5 kV. The technical content of the PKG-022 equipment is not described in accessible sources. | Workbook Packages row 24 (`PACKAGE_REGISTER.csv` `PKG-022`) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, MV switchgear and cable paragraphs | Datasheet "Package equipment scope"; Specification "Standards" | Treat "5kV SWITCHGEAR EQUIPMENT" as authoritative package identity only; defer technical voltage class, configuration, and vendor-document basis to source confirmation. | TBD |
| HRR-022-05-002 | `_Sources/26020-Package_Requirements.docx` contains no PKG-022 / 5kV switchgear section, so source-required vendor document table rows for the package cannot be enumerated. | `_Sources/26020-Package_Requirements.docx` table of contents | `_CONTEXT.md`, Anticipated Artifacts (mentions source vendor-document table rows) | Datasheet "Source vendor document table rows"; Specification R-3; Procedure step "Identify source-required rows" | Carry source-required rows as TBD until a PKG-022 source vendor-document basis is provided or until the human authorizes use of a different reference (e.g., a project-wide vendor-data requirements document). | TBD |
| HRR-022-05-003 | Conventional MV switchgear vendor-data sets (quality plan, datasheets, drawings, manuals, FAT, spares, certificates) are widely used industry practice, but no project source text confirms which subset applies. | Industry convention (ASSUMPTION) | Project source materials (gap) | Specification "Standards"; Guidance "Trade-offs" | Do not encode the conventional set as a requirement; offer it only as ASSUMPTION-flagged guidance until EPC vendor-data requirements are confirmed. | TBD |
