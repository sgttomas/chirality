# Guidance — DEL-102-02 Package Datasheet (PKG-102 Monolithic concrete foundations)

## Purpose

The Package Datasheet is the mandatory Gate-5 EPC anchor deliverable that gives a third-party vendor or discipline-package engineering team the technical handoff data needed to produce detailed engineering and design for PKG-102 "Monolithic concrete foundations." Per `_CONTEXT.md` Notes, interface facts are intentionally carried here as evidence rather than as standalone deliverables.
Source: `_CONTEXT.md` §Scope, §Notes; `DELIVERABLE_REGISTER.csv` row `DEL-102-02_package-datasheet`.

## Principles

- **Source-grounded handoff.** Every datasheet entry should trace to a workbook row, a DBM source slice, an interface register row, or be explicitly marked TBD. Decomposition prose alone is not sufficient grounding for technical values.
  Source: skill `four-documents` Authority hierarchy.
- **Carry workbook interface evidence inline.** Per `_CONTEXT.md` Notes, the active interface X-marks from Workbook Packages row 103 are recorded here as `ART-05281DC8CE` and `ART-F35AC96771` rather than as separate deliverables.
  Source: `_CONTEXT.md` §Notes; `ARTIFACT_REGISTER.csv`.
- **Defer to the geotechnical report for soil-derived values.** Bearing capacity, lateral pile design (LPILE), dynamic criteria, and related parameters are TBD pending report completion. Do not propose values from convention.
  Source: DBM-Deepcut §"Geotechnical and Topographical Assumptions"; §"External Dependencies".
- **Reconcile the package label with the source-stated foundation basis.** The workbook labels PKG-102 as "Monolithic concrete foundations," whereas the DBM specifies driven steel piles as the project default support method and identifies precast concrete forms only for transformers (precast bearing foundations) and compressors (precast concrete block on driven steel piles). The scope of "monolithic concrete foundations" within this project must be confirmed by a human ruling (see Conflict C-01).
  Source: `PACKAGE_REGISTER.csv` row PKG-102; DBM-Deepcut §"Piles and Foundations".
- **Latest-edition discipline.** The DBM directs use of the latest edition of governing codes; the datasheet should record the edition in effect at the time of vendor handoff.
  Source: DBM-Deepcut §"Governing Civil and Structural Basis".

## Considerations

- **Spill containment is a design constraint, not just an interface.** The DBM requires compressor foundation/skid design to consider containment and management of on-skid equipment oil leaks. Where PKG-102 supports such equipment, the datasheet should carry that requirement forward.
  Source: DBM-Deepcut §"Piles and Foundations".
- **Top-of-cap coordination with pad grading.** The civil basis allows pad slope reduction from 1.5% to 1.0% to maintain reasonable top-of-pile-cap elevations. Foundation elevations are an interface to civil pad grading and should be tracked on the interface matrix.
  Source: DBM-Deepcut §"Site Grading and Surface Water Management".
- **Concrete mix, reinforcement, and anchorage are TBD.** The DBM does not state `f'c`, exposure class, rebar grade, or anchor schedules for PKG-102. Treat these as TBD; do not invent values from convention.
  Source: DBM-Deepcut §"Civil Scope" through §"Piles and Foundations" (no clause states these values).
- **Workbook binaries are referenced but not text-accessible in this run.** `26020-Package_Requirements.docx` and `26020-Packages_Interfaces_4_export.xlsx` row 103 are cited as canonical sources but were not opened during drafting; relevant content has been carried instead from the DBM markdown and the Gate-7 register CSVs.
  Source: `_REFERENCES.md`; `_Sources/` listing.

## Trade-offs

- **Concrete vs. piled support.** The package label suggests cast-in-place concrete forms; the DBM defaults to driven steel piles for most structures. A wholesale "monolithic concrete foundations" interpretation would conflict with the DBM default and would carry additional geotechnical, dynamic, and cold-region design implications. The conservative position is to confine PKG-102 to the source-stated concrete-bearing cases (transformers; compressor blocks) plus any cases that detailed engineering subsequently confirms require a monolithic concrete foundation. (PROPOSAL; see C-01.)
- **Carrying interface facts in the datasheet vs. separate interface deliverables.** Carrying X-mark interface facts inline (per `_CONTEXT.md`) keeps the handoff one document but obliges the datasheet to be re-issued whenever the workbook interface row changes; a future scope-change packet may revisit this.
  Source: `_CONTEXT.md` §Notes.

## Examples

- **Transformer foundation example.** The DBM directly identifies transformers as "generally supported on precast concrete bearing foundations." Where PKG-102 supplies transformer bases, the datasheet should record: foundation form (precast concrete bearing), governing concrete code (CAN/CSA A23.3), materials/testing standard (CSA A23.1/A23.2), bearing capacity (TBD per geotech), and grounding/anchorage interface (location TBD).
  Source: DBM-Deepcut §"Piles and Foundations".
- **Compressor block example.** The DBM identifies compressor foundations as "precast concrete block supported on driven steel piles, subject to dynamic analysis." Where PKG-102 supplies compressor blocks, the datasheet should additionally record: dynamic analysis status (TBD), oil-containment constraint, and pile-cap interface to the geotechnical pile design (TBD).
  Source: DBM-Deepcut §"Piles and Foundations".

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-01 | Package label "Monolithic concrete foundations" (workbook row 103) versus DBM-stated default of driven steel piles, with concrete forms identified only for transformers (precast bearing foundations) and compressors (precast concrete block on driven steel piles). | `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 103 (not text-accessible; carried via `PACKAGE_REGISTER.csv` row PKG-102) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §"Piles and Foundations" (lines 2738–2749) | Datasheet §Attributes, §Construction; Specification R4; Guidance §Principles, §Trade-offs; Procedure §Steps | Confine PKG-102 scope to source-stated concrete-bearing cases (transformer precast bearing foundations; compressor precast concrete blocks) and label the broader "monolithic concrete" reading as awaiting detailed-engineering confirmation. | TBD |
| C-02 | Governing-code editions: DBM specifies "latest edition" of all listed codes (NBCC, CAN/CSA A23.3, CSA A23.1/A23.2, Canadian Foundation Engineering Manual, CAN/CSA S16, CSA G40.20/G40.21); the datasheet must commit to a specific edition for vendor handoff. | DBM-Deepcut §"Governing Civil and Structural Basis" | Project execution practice (not locally documented) | Datasheet §Attributes; Specification §Standards | EPC Integrator selects edition in force at handoff date and records it on the datasheet. | TBD |
| C-03 | Concrete mix design parameters (`f'c`, exposure class, durability, slump, air entrainment), reinforcement grade and detailing, and anchor/embedment schedules are not stated in the locally accessible source slices. | DBM-Deepcut §"Civil Scope" through §"Piles and Foundations" (no clause provides these values) | None | Datasheet §Attributes/Construction; Specification R4.5 | Mark TBD on the datasheet; close via detailed-engineering issue. | TBD |
| C-04 | Interface requirements matrix (R5.2) versus workbook content: the workbook carries interface X-marks only (presence/absence), without attribute details for each interface type. | `INTERFACE_REGISTER.csv` rows IFC-1EDEDC0453, IFC-8283744B5B (X = YES only) | `ARTIFACT_REGISTER.csv` row ART-BA3D34EA23 (calls for "matrix") | Datasheet §Interfaces; Specification R5.2 | Populate the matrix with interface ID, type, receiving discipline, and a TBD column for attribute detail to be supplied during handoff. | TBD |
| C-05 | Responsible party: `_CONTEXT.md` records "EPC Integrator," while `PACKAGE_REGISTER.csv` row PKG-102 carries the caveat "EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred from the current sources." | `_CONTEXT.md` Identity table | `PACKAGE_REGISTER.csv` row PKG-102 (`ResponsibleParty` field note) | Datasheet §Identification; Specification R1.2 | Carry "EPC Integrator" as the working assignment with the source-dependent caveat shown verbatim. | TBD |
