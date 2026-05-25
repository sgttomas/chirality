# Guidance: DEL-021-05_vendor-document-turnover-package

## Purpose

The Vendor Document Turnover Package exists to consolidate the Package Vendor's documentation set for `PKG-021` (6.9kV SWITCHGEAR EQUIPMENT) into a single, traceable evidence package that the EPC Integrator can use for review, facility integration, and acceptance. It is the documentation counterpart to the physical vendor-engineered equipment package (`DEL-021-04`) and the precursor evidence consumed by the EPC review and acceptance deliverable (`DEL-021-06`).

## Principles

- Preserve source spelling and identity. The package name is carried as "6.9kV SWITCHGEAR EQUIPMENT" because that is the workbook and Gate 7 register spelling.
- Keep vendor documentation authorship with the Package Vendor; keep review and facility-level integration with the EPC Integrator.
- Treat all six workbook interface facts (Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports) as documentation coverage targets, not as separate deliverables.
- Use `TBD` for items where the accessible source set does not yet define vendor-document requirements (register format, document list, transmittal/gating protocol, detailed test/inspection requirements) rather than inventing project conventions.
- Do not duplicate `DEL-021-06` review/acceptance/turnover-checklist content; reference it instead.

## Considerations

The Gate 7 artifact register explicitly records this deliverable's vendor document register row as gap evidence ("TBD vendor document register — detailed vendor-document requirements are not present in current source material for this package"). The conservative interpretation is that the Package Vendor must propose the register content and submittal cadence, and the EPC Integrator must confirm completeness against facility integration needs. The cross-cutting analogous expectation in the project — that package deliverables include a vendor document register — comes from the mechanical-packages paragraph of the Comp and Liquids DBM, and is therefore directionally applicable but not a clause-level requirement for an electrical switchgear package.

The DBM Deepcut source defines the 6.9 kV medium-voltage service basis (6.9 kV, 3-phase, 3-wire, 60 Hz, low-resistance grounded; serves inverter-drive motors rated 5,500 hp and above) and the facility electrical building context (including the 6.9 kV Inlet/Sales Compressor Electrical Building). Vendor documentation should be consistent with this electrical basis at the package battery limit; however, the source does not specify a vendor document register or detailed submittal protocol for `PKG-021`, so those items remain `TBD`.

Grounding/bonding documentation should reflect the project basis that each 6.9 kV transformer is grounded using a 100 A, 10 s neutral grounding resistor operating as a tripping system. The vendor documentation should record the resulting protection/coordination interfaces at the switchgear, but specific relay settings and coordination studies are package-engineering items owned by the Package Vendor.

Maintenance access is both a workbook interface fact and a routing/clearance constraint in the DBM. Vendor documentation should preserve maintenance access through drawings, clearance requirements, and racking/withdrawal data.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Detailed vendor document list | Treat as Package Vendor proposal + EPC confirmation, with items not yet confirmed marked `TBD`. | Gate 7 artifact register names this as a gap; no project-wide document list is available in the accessible source set. |
| Register format and numbering | Mark `TBD`; defer to project-wide vendor documentation standard when issued. | The accessible source set does not define a project-wide register format or numbering convention. |
| Submittal staging (for review / for approval / certified / as-built) | Carry as ASSUMPTION until source confirms. | A staged submittal convention is industry-typical but not source-confirmed for this package. |
| Test/inspection record set | Reference `ART-E523401B0C` and mark detailed requirements `TBD` until vendor proposal is accepted. | Detailed test/inspection requirements are source-specific where available and otherwise `TBD`. |
| Overlap with `DEL-021-06` | Reference, do not duplicate. | `DEL-021-06` owns the review log, acceptance checklist, and turnover checklist; `DEL-021-05` owns the documentation set being reviewed. |

## Examples

- Acceptable register entry: "Document `PKG-021-DR-001` — Front-view general arrangement drawing, revision A, submittal stage: For Review, intended use: facility-integration check by EPC."
- Acceptable source-gap entry: "Vendor document register format and numbering convention: TBD. No project-wide standard identified in the accessible source set."
- Not acceptable without new source: "Vendor shall submit documents per project document control procedure DCP-001, rev. 3, sections 4.2 and 4.3." (No such procedure has been resolved in the accessible source set.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-021-05-001 | Gate 7 artifact register tags this deliverable's vendor document register as gap evidence (`ART-FA39AD509D`), while the Comp and Liquids DBM mechanical-packages paragraph implies that package deliverables routinely include a vendor document register. | `ARTIFACT_REGISTER.csv` row `ART-FA39AD509D` (gap evidence) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, mechanical packages paragraph | Datasheet Attributes/Construction; Specification REQ-021-05-003, REQ-021-05-010; Procedure Steps | Carry the register as a Package Vendor proposal that the EPC Integrator confirms; keep detailed content `TBD` until vendor proposal is accepted. | TBD |
| HRR-021-05-002 | No project-wide vendor document register format, numbering convention, or transmittal/gating protocol has been resolved for this package in the accessible source set. | `_REFERENCES.md` (no project-wide register/transmittal standard resolved) | Industry convention (not source) | Datasheet Construction (register format, gating); Specification Standards (project-wide register standard); Procedure Steps | Defer format and gating to a forthcoming project-wide standard; record gating as ASSUMPTION until confirmed. | TBD |
| HRR-021-05-003 | Boundary between `DEL-021-05` (vendor documentation set) and `DEL-021-06` (EPC vendor package review and acceptance, including review/comment log, acceptance checklist, turnover checklist, factory/shop test evidence) is at risk of being conflated. | `DELIVERABLE_REGISTER.csv` row `DEL-021-05_vendor-document-turnover-package` | `ARTIFACT_REGISTER.csv` rows `ART-5D5CAC1D6D`, `ART-4B01C09131`, `ART-E523401B0C` under `DEL-021-06` | Datasheet Attributes/Construction; Specification Documentation; Procedure Steps | `DEL-021-05` owns the vendor documentation set; `DEL-021-06` owns review/acceptance/turnover-checklist artifacts. Maintain reference, not duplication. | TBD |
