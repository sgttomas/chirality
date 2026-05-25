# Guidance: DEL-013-05_vendor-document-turnover-package

## Purpose

The Vendor Document Turnover Package exists so that one Package Vendor deliverable consolidates the vendor document register, vendor document submittals, any source-required vendor documentation, and turnover records for PKG-013 (100A DC UNINTERUPTIBLE POWER SUPPLY), with EPC Integrator interface/integration review. It is the documentation channel that lets the EPC Integrator perform the separate package review and acceptance work (`DEL-013-06`) and ultimately integrate the vendor-engineered package (`DEL-013-04`) into the facility. (Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` rows `DEL-013-04`, `DEL-013-05`, `DEL-013-06`.)

## Principles

- **Vendor authors; EPC reviews.** Vendor documentation is owned by the Package Vendor; integration review belongs to the EPC Integrator. Do not blur authorship by re-creating vendor documents inside the EPC scope. (Source: `PACKAGE_REGISTER.csv` row `PKG-013`; `DELIVERABLE_REGISTER.csv` row `DEL-013-05`.)
- **Register before submittals.** A vendor document register defines the document set the vendor will submit before submittals begin to land; the register is the control surface against which submittals are tracked. (Source: `_CONTEXT.md` anticipated artifacts; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` package deliverables paragraph.)
- **Source rows are evidence, not new deliverables.** Where source material exposes specific vendor document table rows for this package, they are carried as artifacts/evidence inside this deliverable rather than minted as separate deliverables. (Source: `_CONTEXT.md` notes; `DELIVERABLE_REGISTER.csv` row `DEL-013-05` notes.)
- **Interface coverage matters.** The register and submittals should provide the package-side data needed for the four declared PKG-013 interfaces (Electrical Power, Grounding / Bonding, Maintenance Access, Structural / Foundations / Supports). Missing interface data is a turnover gap, not a vendor preference. (Source: `PACKAGE_REGISTER.csv` row `PKG-013`; `INTERFACE_REGISTER.csv` rows for PKG-013.)
- **Turnover is the closeout, not a backlog.** Turnover records consolidate certified data, tests, and handoff documentation; missing items at turnover become punch items against EPC acceptance (`DEL-013-06`). (Source: `_CONTEXT.md`; `ARTIFACT_REGISTER.csv` `ART-E565B29B24`.)

## Considerations

- **Source gap for package-specific requirements.** The Gate 7 artifact register explicitly flags this deliverable as a "Vendor Documentation Gap Evidence" item: detailed vendor-document requirements are not present in current source material for PKG-013. The register and submittal scope therefore start from the general package-deliverables expectation and require source closure before they can be finalized. (Source: `ARTIFACT_REGISTER.csv` `ART-23F404EC4B`.)
- **Cross-discipline application of the package-deliverables paragraph.** The locally accessible package-deliverables paragraph addresses mechanical packages. Using it to scope an electrical UPS vendor document set is directional rather than literal; UPS-specific items (battery sizing/test reports, charger commissioning records, IEEE/CSA/UL certifications, autonomy verification) are not enumerated by the accessible source. (Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.)
- **No declared dependencies.** `_DEPENDENCIES.md` carries no declared upstream or downstream edges. The substantive coupling to `DEL-013-04` (vendor-engineered equipment package) and `DEL-013-06` (EPC review and acceptance) is real and should be declared if/when `TASK + dependency-extract` is run. (Source: `_DEPENDENCIES.md`; `DELIVERABLE_REGISTER.csv`.)
- **No package-specific RFQ row found.** Unlike some other packages (e.g., PKG-083), PACKAGE_REGISTER.csv for PKG-013 does not point at a discoverable `26020-..._RFQ_...docx` row. Vendor documentation requirements that would normally appear in an RFQ/Bid Doc are therefore not available for grounding. (Source: `PACKAGE_REGISTER.csv` row `PKG-013`; comparison with row PKG-083.)
- **Objective association is PACKAGE_HEURISTIC.** Objectives `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-008`, `OBJ-009`, `OBJ-010` are carried from the package row and should be treated as directional context, not as binding requirements at the deliverable level, until human-confirmed. (Source: `_CONTEXT.md`; `OBJECTIVE_DELIVERABLE_MAP.csv`.)

## Trade-offs

- **Drafting now vs. waiting for source closure.** Drafting the register and submittal list before vendor scope is firm risks rework; waiting risks holding up EPC review readiness. Bias is to draft the structure now (register fields, interface coverage map, turnover checklist skeleton) and mark content TBD where source-grounded detail is unavailable.
- **Generic vs. UPS-specific document list.** A generic list satisfies the structural requirement but misses UPS-specific evidence (battery capacity verification, charger settings, autonomy, transfer behaviour). Accept generic coverage with explicit UPS-specific TBDs rather than inventing a UPS-specific list without source.
- **Carrying source rows as artifacts vs. promoting them.** Promoting source rows to deliverables would inflate the WBS and break the convention captured in the deliverable register; keep them as artifacts within this deliverable.

## Examples

- Example register column set (illustrative, structure only, content TBD): document number, document title, document type, revision, status (planned/in review/accepted), submittal date, related interface(s), turnover-required flag, EPC reviewer disposition reference.
- Example turnover-record categories (illustrative, structure only, content TBD): certified vendor datasheet set, factory acceptance test records, battery capacity verification, charger commissioning record, as-shipped equipment list and shipped-loose items, operating and maintenance manuals, certifications and conformity declarations, spares/recommended-spares list, drawing index (general arrangement, single-line, schematic, interconnect, foundation/anchor).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-013-05-001 | Whether the general "package deliverables" paragraph from `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (mechanical packages) applies to the PKG-013 electrical UPS vendor document set. | DBM-Comp_and_Liquids package-deliverables paragraph | Artifact register `ART-23F404EC4B` flags absence of package-specific requirements | Datasheet (general source basis), Specification R-013-05-07, Guidance Principles/Considerations | PROPOSAL: treat as directional; require source closure before binding the list. | TBD |
| HRR-013-05-002 | Whether the absence of declared upstream/downstream edges in `_DEPENDENCIES.md` correctly reflects the real coupling to `DEL-013-04` (vendor-engineered equipment package) and `DEL-013-06` (EPC review and acceptance). | `_DEPENDENCIES.md` (none declared) | `DELIVERABLE_REGISTER.csv` and `ARTIFACT_REGISTER.csv` linkage to `DEL-013-04` and `DEL-013-06` | Specification scope; Guidance Considerations | PROPOSAL: declare `DEL-013-04` as upstream (vendor package being documented) and `DEL-013-06` as downstream (EPC review consumer) via `TASK + dependency-extract`. | TBD |
| HRR-013-05-003 | What document control numbering, revision, and transmittal convention governs PKG-013 vendor documentation. | None locally accessible | None locally accessible | Specification R-013-05-09; Procedure Steps; Datasheet Construction | PROPOSAL: keep TBD until project-wide vendor document control source is identified. | TBD |
