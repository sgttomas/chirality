# Specification: DEL-028-05_vendor-document-turnover-package

## Scope

This Specification governs the **Vendor Document Turnover Package** deliverable for PKG-028 (Transformer TXP-8801-1 — Step-Down Distribution Transformer, 7.5 MVA, 13.8 kV / 4160/2400 V).

**In scope**

- Production of a complete vendor document register for the PKG-028 transformer package.
- Submittal of vendor documents required by source materials (DBM, package requirements, applicable standards, vendor data sheets).
- Compilation of turnover records (submittals, test reports, certifications, as-built drawings, warranty documentation, and other artifacts indicated by source materials).
- EPC Integrator interface/integration review of submitted vendor documentation.

**Out of scope (within this deliverable)**

- Engineering, design, or fabrication of the transformer itself (covered by `DEL-028-04_vendor-engineered-equipment-package`).
- EPC Scope of Work and Package Datasheet authorship (`DEL-028-01`, `DEL-028-02`).
- Construction Work Package authorship (`DEL-028-03`).
- EPC vendor package review and acceptance closeout (`DEL-028-06`).
- Individual source vendor document rows as separately decomposed deliverables (they remain artifacts/evidence per `_CONTEXT.md` Notes).

Sources: `_CONTEXT.md` (Scope, Anticipated Artifacts, Notes); `DELIVERABLE_REGISTER.csv`; `PACKAGE_REGISTER.csv` row `PKG-028`.

## Requirements

| ID | Requirement | Basis | Status |
|---|---|---|---|
| R-01 | A vendor document register shall be produced for PKG-028 covering all vendor documentation associated with the TXP-8801-1 step-down distribution transformer. | `_CONTEXT.md` (Anticipated Artifacts); `DELIVERABLE_REGISTER.csv` row `DEL-028-05` | Required |
| R-02 | The register shall include all vendor document submittals required by source materials, the project package requirements ("Core vendor documents" block: PRQ-009 Vendor Document Index, DOC-008 Vendor Document Control Procedure, QLT-006 Supplier Quality), and any deliverable-specific vendor document rows. | `_Sources/26020-Package_Requirements.docx`, recurring "Core vendor documents" block (PRQ-009 / DOC-008 / QLT-006) | Required |
| R-03 | Each register entry shall identify the source vendor document row that gives rise to it, where such a row exists; otherwise the entry shall be labeled as derived from the deliverable type convention. | `_CONTEXT.md` (Anticipated Artifacts: "source vendor document table rows as artifacts where available"); `DELIVERABLE_REGISTER.csv` row `DEL-028-05` | Required |
| R-04 | Turnover records shall be compiled and provided for closeout, covering submittals, factory and field test reports, certifications, as-built drawings, warranty documentation, and other artifacts indicated by source materials and applicable standards. | `_CONTEXT.md` (Anticipated Artifacts: turnover records); deliverable type = "Vendor Document Turnover" | Required |
| R-05 | The Package Vendor shall own production and maintenance of the vendor document register and submittals; the EPC Integrator shall perform interface/integration review. | `_CONTEXT.md` (ResponsibleParty); `PACKAGE_REGISTER.csv` row `PKG-028` (responsibility model) | Required |
| R-06 | The vendor document register and turnover records shall preserve traceability to the applicable interface types declared for PKG-028: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. | `PACKAGE_REGISTER.csv` row `PKG-028` (Applicable interface types); `INTERFACE_REGISTER.csv` `PKG-028` rows | Required |
| R-07 | Vendor documents shall be controlled per DOC-008 (Vendor Document Control Procedure), and supplier quality documentation shall be aligned with QLT-006 (Supplier Quality). | `_Sources/26020-Package_Requirements.docx`, recurring "Core vendor documents" block | Required (ASSUMPTION: project-wide block applies to PKG-028 by analogy; PKG-028–specific section was not located) |
| R-08 | The vendor document register shall include the package-specific drawings, datasheets, test reports, and turnover artifacts typical for a step-down distribution transformer at 7.5 MVA, 13.8 kV / 4160/2400 V. Specific document list is TBD pending a PKG-028 package requirements section or vendor data. | Source gap; package title in `PACKAGE_REGISTER.csv` row `PKG-028` | TBD — list pending source |
| R-09 | The deliverable shall be treated as an additional Gate 5 deliverable; individual source vendor document rows remain artifacts/evidence, not separately decomposed deliverables. | `_CONTEXT.md` (Notes); `DELIVERABLE_REGISTER.csv` row `DEL-028-05` (Notes) | Required (framing constraint) |
| R-10 | Grounding-related vendor documentation shall demonstrate that the transformer grounding arrangement is suitable for the DBM grounding basis (separate copper ground conductor sized per CEC, connected directly to ground). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2991 | Required (interface-coupled) |
| R-11 | Vendor documentation of the primary medium-voltage connection arrangement shall be compatible with the DBM 13.8 kV cabling basis (three-conductor copper TECK, 15 kV rated, 133% insulation, shielded). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 3007 | Required (interface-coupled) |

## Standards

| Standard / Reference | Applicability | Source / status |
|---|---|---|
| PRQ-009 — Vendor Document Index | Project-standard vendor document index applied per package. | `_Sources/26020-Package_Requirements.docx`, "Core vendor documents" block; full text `location TBD` (not located in searched extract for PKG-028) |
| DOC-008 — Vendor Document Control Procedure | Procedure governing vendor document control. | `_Sources/26020-Package_Requirements.docx`, "Core vendor documents" block; full text `location TBD` |
| QLT-006 — Supplier Quality | Supplier quality controls applied to vendor documentation and turnover. | `_Sources/26020-Package_Requirements.docx`, "Core vendor documents" block; full text `location TBD` |
| Step-down distribution transformer standards (e.g., IEEE C57, CSA C88, IEC 60076 family) | ASSUMPTION: likely applicable based on equipment class (7.5 MVA, 13.8 kV / 4160/2400 V). Specific clause-level requirements not derivable without source text. | No accessible source text within `_REFERENCES.md` scope; `location TBD` |
| Project DBM (04-25 Deepcut) | Provides the incoming-power-and-transformer distribution basis, grounding requirement for distribution transformers, and the 13.8 kV medium-voltage cabling basis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, lines 2917-2937, 2991, 3007 |
| Canadian Electrical Code (CEC) | Sizing basis for separate copper grounding conductor as cited by DBM. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2991 (CEC reference) |

## Verification

| Requirement | Verification approach |
|---|---|
| R-01 | Inspection: vendor document register exists, is package-scoped to PKG-028, and is signed off by the Package Vendor. |
| R-02 | Inspection: register entries cover (a) source-material-driven documents, (b) the PRQ-009 / DOC-008 / QLT-006 core block, and (c) any deliverable-specific rows. |
| R-03 | Inspection: each register row carries a source-row pointer or a "derived from deliverable type convention" label. |
| R-04 | Audit: turnover records are present and complete prior to package acceptance under `DEL-028-06`. |
| R-05 | Audit: register and submittals are produced by the Package Vendor; EPC Integrator review records exist. |
| R-06 | Cross-check: each applicable interface type in `PACKAGE_REGISTER.csv` row `PKG-028` is represented by at least one register entry or turnover record. |
| R-07 | Document control audit against DOC-008 and QLT-006 (when source text becomes available); until then, evidence that the Package Vendor follows a vendor-document control procedure. |
| R-08 | Inspection at acceptance: register contains the package-specific transformer documents required by source materials and applicable standards. |
| R-09 | Decomposition cross-check: no separately decomposed deliverable shadows an individual vendor document row of PKG-028. |
| R-10 | Inspection of vendor grounding submittals against DBM grounding basis; cross-check against the Grounding / Bonding interface row. |
| R-11 | Inspection of vendor primary-connection drawings/datasheets against DBM 13.8 kV cabling basis; cross-check against the Electrical Power interface row. |

## Documentation

Required artifacts produced under this deliverable:

- Vendor document register (master list of all vendor documents for PKG-028).
- Vendor document submittals (per-row transmittals as identified by the register).
- Source vendor document table rows as artifacts where available (per `_CONTEXT.md` Anticipated Artifacts).
- Turnover records (submittals, test reports, certifications, as-built drawings, warranty documentation, and other artifacts indicated by source materials).

Source: `_CONTEXT.md` (Anticipated Artifacts); `DELIVERABLE_REGISTER.csv` row `DEL-028-05`.
