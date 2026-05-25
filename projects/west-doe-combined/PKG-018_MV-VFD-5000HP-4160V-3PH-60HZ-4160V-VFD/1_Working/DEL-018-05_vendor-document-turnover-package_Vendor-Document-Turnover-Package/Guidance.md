# Guidance — DEL-018-05 Vendor Document Turnover Package

## Purpose

`DEL-018-05` exists so that the Package Vendor's design, supply, and acceptance evidence for the `PKG-018` MV VFD package becomes a single auditable documentation handoff to the EPC Integrator. It is the documentation counterpart to the physical equipment package (`DEL-018-04`) and the input to EPC review/acceptance (`DEL-018-06`). Source: `DELIVERABLE_REGISTER.csv` rows `DEL-018-04`/`DEL-018-05`/`DEL-018-06`; `_CONTEXT.md` Scope.

## Principles

- **Single-deliverable bundling.** The decomposition explicitly carries this as one deliverable rather than splitting by document type; individual source vendor document rows are artifacts, not separate deliverables. Source: `DELIVERABLE_REGISTER.csv` Notes column.
- **Vendor authorship, EPC review.** The Package Vendor authors and submits; the EPC Integrator reviews for interface/integration fit. Source: `_CONTEXT.md`; `PACKAGE_REGISTER.csv` (ownership boundary).
- **Source-aligned content.** Vendor documentation must reflect the DBM-stated electrical, mechanical, and environmental basis for the driven equipment and the MV system it ties into. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- **Project-required document classes are the floor.** The mechanical-packages organization paragraph in the DBM enumerates required content classes (datasheets, cause-and-effect inputs, utility load summaries, relief/load data, tie-in lists, operating/design envelopes, sparing philosophy, materials/coating, maintenance access, shipped-loose lists, vendor document register). The vendor register may add to but not subtract from this floor. Source: same.

## Considerations

- **Identity ambiguity.** The package title says "5000HP, 4160V" while the DBM body describes inlet compressor motors at 5,200 hp / 4,000 V. The MV system basis says 4,160 V. The VFD vendor documentation set should either reconcile or escalate this before turnover. See Conflict Table CT-1.
- **Starting VFD vs continuous-duty VFD.** The DBM states "starting VFD" under SCA-001 VE #34 for KM-2150/KM-2250; the package title implies a 4160 V VFD without qualifying "starting." Vendor documentation should declare the operating mode explicitly. See Conflict Table CT-2.
- **Capacitor-bank coordination.** SCA-001 VE #37 removes capacitor banks where VFDs are present; vendor documentation should make harmonic and reactive-power assumptions explicit and traceable to detailed electrical studies. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- **Environmental.** -40 °C minimum ambient must be reflected on enclosures, control panels, and shipped-loose materials. Source: same.
- **Package-requirements file present but not extracted.** `PKG-018/26020-Package_Requirements.docx` exists; clause-level submittal/revision conventions remain TBD until that slice is read. Source: `_REFERENCES.md`.

## Trade-offs

- **Register completeness vs schedule.** A broader, fully cross-referenced register costs vendor time but reduces EPC review iterations in `DEL-018-06`. The decomposition treats turnover as a single deliverable, implying a complete-at-handoff bias.
- **Pass-through vs interpretation.** Some vendor documents are pass-throughs of source rows; others require interpretation of project basis (e.g., MV harmonic mitigation). Treat interpretation items as draft until EPC review confirms.

## Examples

None taken from sources. The DBM does not provide an example document register layout for an MV VFD package; do not invent one. Mark `TBD` and resolve from `26020-Package_Requirements.docx` when accessible.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-1 | Package title says "5000HP, 4160V"; DBM body says inlet compressor motors are 5,200 hp / 4,000 V (with MV system at 4,160 V). | `PACKAGE_REGISTER.csv` row `PKG-018` (description "MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD"); `_CONTEXT.md` Identity | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Electric Driver and Starting Basis; Medium-voltage service row) | Datasheet (Identification, Conditions), Specification (R-3, R-4, R-5), Guidance | PROPOSAL: treat package title as a catalog-level descriptor; treat the DBM Electric Driver and Starting Basis text (5,200 hp / 4,000 V motor) and the MV service row (4,160 V system) as authoritative for vendor documentation parameters. | TBD |
| CT-2 | Package title implies a 4160V VFD; DBM states a "starting VFD" under SCA-001 VE #34 — operating mode (start-only vs continuous inverter duty) is not unambiguous. | `PACKAGE_REGISTER.csv` row `PKG-018` (description) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` ("supplied with starting VFD under SCA-001 VE #34"; motor "continuous inverter duty") | Specification (R-5), Procedure (Steps) | PROPOSAL: vendor documentation must declare operating mode explicitly; default to "starting VFD" per SCA-001 VE #34 unless an SCA update supersedes. | TBD |
| CT-3 | Per-package vendor document class list is not in accessible source slices. | `_REFERENCES.md` Missing/Deferred | `PKG-018/26020-Package_Requirements.docx` (present but not extracted) | Datasheet (Construction), Specification (R-2, R-11), Procedure (Steps) | PROPOSAL: extract `26020-Package_Requirements.docx` and confirm/extend the register floor. | TBD |
