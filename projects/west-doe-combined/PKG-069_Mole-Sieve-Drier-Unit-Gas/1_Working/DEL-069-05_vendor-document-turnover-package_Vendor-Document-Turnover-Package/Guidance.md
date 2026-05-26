# Guidance — DEL-069-05 Vendor Document Turnover Package

## Purpose

The Vendor Document Turnover Package exists to deliver, to the EPC Integrator and ultimately to the Owner/Operator, a complete, controlled, and verifiable set of vendor documents covering the PKG-069 Mole Sieve Drier Unit (Gas) — sufficient to support engineering integration, construction, mechanical completion, commissioning, and long-term operations and maintenance. It is one of the standard Gate 5 deliverables for each package and is the documentary half of the package vendor's scope, complementary to the physical Vendor-Engineered Equipment Package (DEL-069-04).

## Principles

1. **Vendor authorship, EPC integration review.** The Package Vendor is responsible for producing and maintaining the documents. The EPC Integrator reviews for interface/integration consistency, not for vendor-internal design decisions.
2. **Register-first.** The Vendor Document Register is the single source of truth for what documents exist, what state they are in, and where they have been issued. Submittals that do not appear on the register do not exist for project purposes.
3. **Source fidelity.** Every requirement carried in the register or in submittals must be traceable to the purchase contract, the package datasheet (DEL-069-02), the vendor scope-of-work (DEL-069-01), or a recorded change.
4. **Artifact retention, not duplication.** Source vendor document table rows are retained as evidence within this deliverable, not promoted to separate deliverables — they support traceability without inflating the deliverable hierarchy. (Per `_CONTEXT.md` Notes.)
5. **Turnover for operations.** The turnover record set must be usable by operations and maintenance, not merely by document control. Manuals, spare parts lists, as-builts, and certifications take precedence over preliminary or interim documents in the turnover index.

## Considerations

- **Mole sieve regeneration temperature CONFLICT.** The DBM states regeneration temperature basis is unresolved between 450 degF (system overview) and 460 degF (heater detail) (DBM line 1280). Vendor documents must adopt a single value; the EPC Integrator should drive closure of this CONFLICT before vendor heater datasheet approval — see Conflict Table below.
- **Adsorbent life.** The DBM cites typical 3-year life with possible 5-year extension to align with turnaround (line 1271). Vendor guarantees and spare-adsorbent provisioning in the turnover record should reflect whichever life is contractually committed.
- **Flange rating context.** Vendor pressure-vessel and piping submittals must be consistent with the 900# flange rating required by the molecular sieve system (DBM line 628). Mixed-rating submittals are a red flag.
- **Adsorbent grade is mandatory.** 3A adsorbent with silica gel protective layer is mandatory; 4A and 5A are explicitly prohibited due to H2S adsorption risk and resulting sulphur spikes in the regeneration return loop (DBM lines 1269, 1270). Any vendor proposal substituting these grades must be rejected.
- **Controls philosophy is operator-initiated.** Molecular-sieve blowdown is HMI-initiated only, not automatic with facility ESD (DBM line 1361). Vendor cause-and-effect and SAFE chart submittals must reflect this rather than copying a generic auto-blowdown template.
- **Open items propagate.** Several DBM-level items remain TBC (final regen compressor capacity and design differential, scrubber drain sizing, dry-out header MAWP — DBM line 1291). Vendor documents that close any of these must be flagged in the register as design-basis-closing changes, not routine submittals.

## Trade-offs

- **Submission detail vs. cycle time.** Requiring extensive early submittal detail improves integration risk management but lengthens the vendor's engineering cycle. The register should distinguish documents required for fabrication release versus documents required only for turnover.
- **Source row preservation vs. register clarity.** Keeping source vendor document table rows in the artifact set aids traceability but can clutter the register if those rows are not visually distinguished from formal submittals.
- **Vendor manuals vs. operator handbooks.** Vendor manuals are usually optimized for the vendor's product line, not for this specific facility's operating context. Operations may need a thin facility-specific overlay; this is normally an EPC scope item rather than a vendor turnover obligation.
- **TBD vs. ASSUMPTION.** Where the project document control matrix (numbering, transmittal format, turnover-index template) is not yet locally available, prefer TBD with a placeholder over importing a generic template that may have to be reworked.

## Examples

Examples are limited because the project document control matrix and Workbook Packages row 73 source list are not locally accessible. Indicative items only:

- **Indicative VDR row:** `MS-VDR-001 | Adsorber Vessel V-6130-1 General Arrangement | Rev B | Approved | Trans #069-014 | Required for IFC` — column set ASSUMPTION; project-specific format TBD.
- **Indicative turnover index entry:** `Operating Manual — Mole Sieve Drier Unit (Gas) — Vendor: TBD — Doc: TBD — Status: Final As-Built — Location: Turnover Vol. 3, Tab 5` — ASSUMPTION.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-VDT-01 | Mole sieve regeneration temperature basis differs between system overview (450 degF) and heater detail (460 degF). | DBM-Deepcut/4-25_Deepcut_DBM.md sec. "Molecular-Sieve Equipment, Controls, and Protection" — Regeneration gas heater row (line 1280) | DBM-Deepcut/4-25_Deepcut_DBM.md same row (cites both 450 degF and 460 degF) | Specification REQ-VDT-06; Procedure step on heater datasheet review | PROPOSAL: adopt the heater-detail value (460 degF) for vendor heater datasheet review until EPC Integrator confirms; document the chosen value in the register before vendor heater datasheet approval. | TBD |
| CONF-VDT-02 | Workbook Packages row 73 vendor document list is not locally extracted, so the authoritative required-document set for this deliverable cannot be reconciled with the deliverable's anticipated artifacts. | `_REFERENCES.md` lists `26020-Packages_Interfaces_4_export.xlsx` as the source workbook (binary) | `_CONTEXT.md` Anticipated Artifacts lists four artifact classes (register, submittals, source rows, turnover records) | All specification requirements; all procedure steps; turnover index composition | PROPOSAL: extract Workbook Packages row 73 to a text-readable artifact under `_References/` (or equivalent) and reissue this deliverable's documents with the extracted list as the authoritative basis. | TBD |
| CONF-VDT-03 | `_DEPENDENCIES.md` declares no upstream dependencies during PREPARATION, but DEL-069-05 inherently depends on DEL-069-01 (vendor scope) and DEL-069-02 (package datasheet) for source content, and DEL-069-06 (EPC review/acceptance) inherently consumes this deliverable downstream. | `_DEPENDENCIES.md` Declared Upstream/Downstream: None | Sibling deliverables in `/PKG-069_Mole-Sieve-Drier-Unit-Gas/1_Working/` (DEL-069-01, DEL-069-02, DEL-069-06) | Procedure prerequisites; dependency view | PROPOSAL: declare DEL-069-01 and DEL-069-02 as upstream and DEL-069-06 as downstream via a follow-on `TASK + dependency-extract` run; do not silently edit `_DEPENDENCIES.md` here. | TBD |
