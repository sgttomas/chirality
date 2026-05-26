# Guidance: DEL-046-05 — Vendor Document Turnover Package (PKG-046 Acid Gas Compressors)

## Purpose

The Vendor Document Turnover Package is the contractual handover artifact set that converts the Package Vendor's design, fabrication, and commissioning evidence into a controlled record that the EPC Integrator and Owner/Operator can rely on for facility integration, regulatory submission, operations, and long-term asset management. For PKG-046 Acid Gas Compressors, the package documents two operating reciprocating compressor packages (Unit 1 K-5450-1 and Unit 2 V-5530-1) plus one spare compressor that together compress H2S/CO2 acid gas for injection disposal (PACKAGE_REGISTER PKG-046; DBM-Deepcut lines 878, 885, 2529, 2572-2573).

## Principles

- **VDR is the index, not the content.** The Vendor Document Register defines what is required; the submitted documents are the substance. Both must be consistent throughout the project life cycle.
- **Source authority preserved.** Where the Package Requirements document defines a required vendor document table, those rows are kept as artifacts/evidence and are not promoted to standalone deliverables (`_CONTEXT.md` Notes).
- **Revision discipline.** Documents progress through controlled revision states; the exact revision lexicon is governed by `26020-Package_Requirements.docx` (location TBD).
- **Interface visibility.** Because the acid gas compressor package interfaces with many disciplines (Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas; Maintenance Access; Structural — per PACKAGE_REGISTER PKG-046), the VDR must surface the documents that each EPC discipline needs for integration review.
- **Traceability of unresolved items.** Where design basis remains TBD (e.g., compressor model Ariel KBT/6 vs KBK/6; discharge pressure 1,200 psig vs 1,500 psig; configuration 2x100% vs 3x50% — DBM-Deepcut lines 1090-1092), the VDR shall surface the resolving documents so reviewers can see where the convergence occurs.

## Considerations

- **Sour service rigor.** Acid gas service (H2S) triggers NACE MR0175 / ISO 15156 material conformance evidence. Material certs and weld-procedure qualifications should be planned for early submission so they do not gate mechanical completion (ASSUMPTION; precise governance TBD per source).
- **Reciprocating compressor analysis artifacts.** Pulsation/vibration studies (API 618 framework, ASSUMPTION) are typically high-value submittals that affect skid layout, piping support, and field installation; their early issue benefits the EPC Integrator's piping design (DEL-046-04 interface).
- **Lube oil, valve, distance-piece purge documentation.** Long two-compartment distance pieces with inboard/outboard purge are part of the design basis (DBM-Deepcut line 2218); the turnover should include purge philosophy, leak-management, and check-valve arrangement documentation (DBM-Deepcut line 2218 reference to check valves preventing backflow of sour gas).
- **Lube oil injection into disposal well.** Because lubrication oil injected into compressor valves/cylinders ultimately enters the disposal well (DBM-Deepcut line 1061), lube selection documentation has regulatory and reservoir-compatibility implications that the turnover should cover.
- **Two-times-100% plus spare logistics.** The spare compressor introduces additional turnover artifacts (parallel material certs, parallel ITPs); the VDR should treat the spare as a peer unit unless source materials direct otherwise (ASSUMPTION).

## Trade-offs

- **Early issue vs. final revision.** Issuing engineering documents IFR / IFA early supports EPC integration and constructability but increases re-issue churn. The Package Requirements document should govern minimum submittal milestones; the package planner should resist using "AB only" as the sole submission point.
- **VDR granularity.** A finely line-itemed VDR improves reviewer visibility but increases tracking overhead. The Package Requirements document is the authoritative granularity; do not consolidate rows that the source treats discretely.
- **Acceptance authority.** EPC Integrator review (DEL-046-06) is the acceptance pathway; this deliverable shall not embed acceptance disposition. Keep the VDR neutral on disposition until the reviewer signs.

## Examples

- **Two operating units plus spare.** VDR shall reflect documents that are unit-specific (e.g., GA per K-5450-1 and per V-5530-1) and documents that are common (e.g., shared cause-and-effect, shared lube specification). The list is **TBD** pending source access.
- **Discipline-tagged submittals.** Process datasheets and P&IDs are reviewed by Process; one-lines and motor data are reviewed by Electrical; cause-and-effect is reviewed by I&C and Process jointly. The VDR should label discipline ownership where the source format allows.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-046-05-01 | `_REFERENCES.md` lists `26020-Package_Requirements.docx` and `26020-Packages_Interfaces_4_export.xlsx` as source materials, but neither is locally text-accessible. Most VDR composition, revision lexicon, milestone schedule, and standards clause references therefore remain TBD. | `_REFERENCES.md` Source Materials Referenced By Decomposition Row | `_Sources/` directory listing (only .docx and .xlsx present for these references) | Datasheet Construction table; Specification REQ-R-02, R-03, R-04, R-07, R-08; Specification Standards section | Convert .docx/.xlsx to markdown via `tools/pdf2md/` family or equivalent and re-run with `RUN_PASSES=P3_ONLY` after lensing | TBD |
| C-046-05-02 | Acid gas compressor model: DBM-Deepcut detailed basis is Ariel **KBT/6** but a KBK/6 reference appears as TBC. | DBM-Deepcut line 1090 ("Ariel KBT/6 detailed basis conflicts with KBK/6 TBC reference") | DBM-Deepcut line 2198 (Acid Gas Compressor model column "KBT/6") | Datasheet Attributes ("Compressor model"); Specification REQ-R-03 | KBT/6 (detailed-basis value); flag for vendor confirmation in submitted GA | TBD |
| C-046-05-03 | Acid gas compressor discharge pressure: 1,200 psig normal operating basis vs 1,500 psig design-discharge reference. | DBM-Deepcut line 1091 | (same) | Datasheet Conditions ("Discharge pressure"); Specification verification of MAWP basis | Carry both values explicitly until vendor datasheet resolves; do not pick a single value | TBD |
| C-046-05-04 | Compressor configuration: two x 100% plus one spare detailed basis vs possible three x 50% alternative. | DBM-Deepcut lines 878, 994, 1092 | (same source, marked TBD) | Datasheet Attributes ("Number of compressor packages in scope"); VDR scope (per-unit vs three-unit documents) | Two x 100% plus one spare (detailed basis) | TBD |
