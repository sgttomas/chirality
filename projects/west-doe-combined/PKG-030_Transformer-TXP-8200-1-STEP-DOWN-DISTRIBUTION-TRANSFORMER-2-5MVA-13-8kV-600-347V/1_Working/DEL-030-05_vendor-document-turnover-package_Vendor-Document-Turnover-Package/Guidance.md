# Guidance: DEL-030-05_vendor-document-turnover-package

## Purpose

The Vendor Document Turnover Package exists to consolidate, transmit, and evidence acceptance of the vendor-supplied documentation for `PKG-030`, the Transformer TXP-8200-1 (2.5 MVA, 13.8 kV / 600/347 V step-down distribution transformer). It is the audit-grade record that the Package Vendor supplied a complete, reviewed, and integrated document set against the package scope of supply, and that the EPC Integrator accepted it for facility integration.

## Principles

- Preserve source spelling and identity. The package name is carried as "Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V" because that is the workbook and Gate 7 register spelling.
- Treat workbook interface `X` facts as evidence within the vendor turnover documentation, not as separate deliverables.
- Keep vendor-owned documentation authoring with the Package Vendor and facility-level integration review with the EPC Integrator.
- Individual source-vendor document rows remain artifacts/evidence (per `_CONTEXT.md` Notes); they are not separately decomposed deliverables.
- Use `TBD` where the accessible source set does not establish package-specific vendor-documentation requirements; do not synthesize requirements from generic convention.
- Use the DBM mechanical-package deliverable basis only at the level it supports: a conservative menu of expected document types (datasheets, load summaries, tie-in lists, operating envelopes, sparing philosophy, materials/coating, maintenance access, shipped-loose lists, vendor document register).

## Considerations

The accessible source set is thin for package-specific vendor-documentation requirements for `PKG-030`. The DBM mechanical-package paragraph (line 617 of `3-25_Comp_and_Liquids_DBM.md`) provides the strongest available basis for the general content menu of a vendor turnover, but it is written for mechanical packages generally and not for this specific transformer. The DBM also confirms the electrical context (13.8 kV to 600 V step-down feeding a 600 V MCC, line 745) so the deliverable can confidently locate the package in the overall distribution architecture without inventing detail.

The `ARTIFACT_REGISTER.csv` row `ART-8B1CB2D887` explicitly records the vendor-documentation gap for this deliverable ("TBD vendor document register; Detailed vendor-document requirements are not present in current source material for this package"). The Vendor Document Turnover Package must therefore be structured so the register and submittal log can absorb vendor-supplied content as it arrives, rather than being pre-populated with unsupported document names and counts.

The EPC Integrator integration review consumes this deliverable into `DEL-030-06_epc-vendor-package-review-and-acceptance`. The turnover documentation must therefore expose interface-relevant evidence cleanly (Electrical Power, Grounding/Bonding, Area/Exterior Lighting, I&C/Control Cabling, Communications/Network, Maintenance Access, Structural/Foundations/Supports) so EPC review can verify integration impact without re-reading the entire vendor package.

Maintenance access is both an explicit workbook interface fact and a DBM routing constraint (cable tray and conduit routing shall not interfere with maintenance access). The turnover documentation should preserve clearances and identify access-sensitive components.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Vendor document register content | Define the register schema and leave entries `TBD` until vendor scope of supply is confirmed. | DBM and Gate 7 registers do not enumerate `PKG-030`-specific vendor documents; over-prescription risks misalignment with vendor scope. |
| Specific transformer standards | List likely-applicable transformer standards (CSA/IEEE/IEC) as `ASSUMPTION`. | No accessible source slice cites a specific transformer standard for `PKG-030`. |
| Turnover record schema | Use a conservative acceptance-evidence menu (factory test, field test, name-plate, as-built) with content `TBD`. | No accessible source defines the package-specific turnover-record set. |
| Source-vendor document table | Treat each source-table row as artifact/evidence; do not promote to deliverable. | `_CONTEXT.md` Notes and decomposition policy explicitly state this. |
| Submittal sequence | Inherit project submittal/document-control standard; do not invent package-specific sequencing. | No source slice establishes a `PKG-030` submittal sequence. |

## Examples

- Acceptable register entry: "Document number: TBD (vendor-assigned). Title: Transformer general arrangement drawing. Type: Drawing. Revision: TBD. Submittal status: TBD. EPC review status: TBD. Source: vendor scope of supply (to be issued)."
- Acceptable interface-evidence entry: "Grounding/Bonding evidence: vendor-supplied transformer grounding diagram (TBD), cross-referenced to facility ground grid drawing under EPC integration review."
- Acceptable source-gap entry: "Factory acceptance test report list: TBD pending vendor scope confirmation. No package-specific source slice available."
- Not acceptable without new source: "Vendor shall provide 22 documents listed below." The accessible source set does not establish a fixed count or list for `PKG-030`.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-030-05-001 | The accessible source set does not enumerate package-specific vendor documents for `PKG-030`; only a generic mechanical-package deliverable menu is available. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617 (mechanical package deliverable menu) | `ARTIFACT_REGISTER.csv` row `ART-8B1CB2D887` (documented vendor-documentation gap) | Datasheet Attributes/Construction; Specification REQ-030-05-003/006/007; Guidance Considerations | Define register schema now; leave content rows `TBD` until vendor scope of supply is confirmed and the project document-control standard is provided. | TBD |
| HRR-030-05-002 | Applicable transformer standards (CSA/IEEE/IEC) are likely governing but no accessible source slice cites a specific transformer standard for `PKG-030`. | Decomposition narrative implies industry standards apply | No source slice cites a specific clause | Specification Standards | Carry transformer-standard references as `ASSUMPTION: likely applicable; location TBD` until project specification index or vendor data is accepted. | TBD |
| HRR-030-05-003 | Boundary between `DEL-030-05` (turnover documentation) and `DEL-030-04` (vendor engineered equipment package) requires explicit allocation of who originates each document vs. who packages it for turnover. | `DELIVERABLE_REGISTER.csv` row `DEL-030-04` (vendor engineering/design/equipment) | `DELIVERABLE_REGISTER.csv` row `DEL-030-05` (vendor documentation/turnover) | Specification Scope; Procedure Steps | Treat `DEL-030-04` as the origin of authored vendor engineering documents and `DEL-030-05` as the register/submittal/turnover wrapper that consumes them. | TBD |
