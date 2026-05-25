# Guidance: DEL-024-06_epc-vendor-package-review-and-acceptance

## Purpose

This deliverable exists to convert the accepted Gate 7 basis for `PKG-024` plus the EPC anchor deliverables (`DEL-024-01` SOW, `DEL-024-02` Package Datasheet, `DEL-024-03` CWP) into source-supported EPC review, integration-acceptance, and handoff-readiness evidence for the Package Vendor's MV VFD package. It is not a vendor engineering deliverable and is not a substitute for the EPC Package Datasheet or CWP; it consumes them as acceptance basis.

## Principles

- Preserve source spelling and identity. The package name is carried as "MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD" because that is the workbook and Gate 7 register spelling.
- Treat workbook interface facts for `PKG-024` as acceptance items in the checklist, not as separate deliverables.
- Keep vendor-owned engineering/design/documentation/equipment with the Package Vendor; keep facility-level integration acceptance with the EPC Integrator.
- Cite the EPC SOW, EPC Package Datasheet, EPC CWP, accepted Gate 7 register row, or accessible source slice for every acceptance entry. Where no source is available, record `TBD` rather than assert acceptance.
- Use the DBM electrical basis only at the level it supports: MV VFD context within the 4.16 kV system, electrical-building housing possibility, VFD-fed motor area marking, and VFD-fed low-voltage cable type.

## Considerations

The DBM electrical design basis identifies a 4.16 kV motor control center and explicitly marks "VFD and soft-starter requirements for 4.16 kV motors" as `TBD` in the electrical TBD list. EPC review must therefore not invent VFD performance requirements from generic convention; it must require the issued EPC Package Datasheet (`DEL-024-02`) to resolve them before acceptance is closed.

The DBM allows electrical buildings to house medium-voltage VFDs, MV switchgear, MV MCCs, MV reduced-voltage soft starters, 600 V MCCs, AC/DC UPS systems, distribution transformers, panelboards, contactor panels, PLC panels, and network racks, "as required by detailed design." It does not assign the PKG-024 MV VFD to a specific building, room, or outdoor location. Housing/location acceptance is therefore an EPC Package Datasheet and CWP question.

The DBM also constrains VFD-fed motors in Zone 2 areas (marking and temperature code) and VFD-fed low-voltage cable type (copper TECK). Whether the EPC integration scope for `PKG-024` contains a Zone 2 driven motor and/or VFD-fed low-voltage cable is determined by the EPC Package Datasheet and CWP; the EPC review must verify the resulting evidence rather than asserting applicability from the package title alone.

The vendor scope under review (`DEL-024-04` Vendor Engineered Equipment Package and `DEL-024-05` Vendor Document Turnover Package) defines the actual submittals that the review log and acceptance checklist must cover. This deliverable does not list those submittals here; it instead requires the review log to enumerate them by row and disposition.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Detailed VFD acceptance criteria (efficiency, harmonics, cooling, protection coordination, output filter, control interface) | Mark `TBD` and require resolution by the issued EPC Package Datasheet (`DEL-024-02`) before acceptance closure. | DBM marks 4.16 kV VFD/soft-starter requirements as `TBD`; `_Sources/26020-Package_Requirements.docx` PKG-024 slice was not consumed in this run. |
| Housing / installation location | Identify electrical-building housing as a possibility, not a confirmed location. | DBM allows MV VFD housing in electrical buildings but does not assign PKG-024 to a specific location. |
| Zone 2 motor marking | Apply only if the EPC Package Datasheet/CWP confirms the driven motor is in a Zone 2 area. | DBM clause is conditional on area classification, not on VFD presence alone. |
| Low-voltage VFD-fed cable | Apply only to cable scope that the EPC Package Datasheet/CWP confirms is fed from this VFD package. | DBM cable type table is about cable fed from VFDs, not about MV cable to the VFD primary. |
| Test/inspection acceptance thresholds | Use vendor-stated acceptance criteria reviewed against the EPC Package Datasheet; record any threshold gaps as `TBD`. | No accessible PKG-024-specific test acceptance threshold was extracted in this run. |
| Responsibility model | Keep EPC-owned acceptance language separate from vendor-owned design language. | `PACKAGE_REGISTER.csv` row `PKG-024` distinguishes vendor scope from EPC integration scope. |

## Examples

- Acceptable checklist entry: "Interface `Electrical Power` (`IFC-68C5E24846`): accepted against EPC Package Datasheet (`DEL-024-02`) interface matrix and EPC CWP (`DEL-024-03`) tie-in plan." (where those documents are issued and consumed; otherwise `TBD`).
- Acceptable review log entry: "Vendor submittal X: accept-with-comments; basis: EPC Package Datasheet section Y; comments resolved before turnover."
- Acceptable source-gap entry: "Detailed VFD harmonic acceptance: TBD; awaiting issued EPC Package Datasheet (`DEL-024-02`) and PKG-024-specific package requirements (`26020-Package_Requirements.docx`)."
- Not acceptable without new source: "Accepted: VFD efficiency at 97% across all load points." No accessible source establishes this value for `PKG-024` in this run.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-024-06-001 | DBM electrical TBD list states "VFD and soft-starter requirements for 4.16 kV motors are TBD," yet `PKG-024` is a defined 4,160 V VFD package whose acceptance requires confirmed VFD requirements. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical TBD list (4.16 kV motor starting) and 4.16 kV MCC paragraph | Workbook Packages row 26 / `PACKAGE_REGISTER.csv` row `PKG-024` package title and function | Specification REQ-024-06-006; Datasheet Conditions; Procedure Steps | Require the issued EPC Package Datasheet (`DEL-024-02`) to resolve 4.16 kV VFD requirements before EPC review can close acceptance; do not invent requirements from DBM-level prose. | TBD |
| HRR-024-06-002 | Anchor acceptance bases (EPC SOW `DEL-024-01`, EPC Package Datasheet `DEL-024-02`, EPC CWP `DEL-024-03`) are required for EPC review but their content was not consumed in this run, so the acceptance checklist cannot yet be source-grounded against them. | `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` rows `DEL-024-01`/`DEL-024-02`/`DEL-024-03` | This deliverable folder: no copies or extracts of those anchors present | Specification REQ-024-06-003/-004/-006/-009; Datasheet Construction; Procedure Steps | Defer detailed acceptance entries to a later pass once `DEL-024-01`/`DEL-024-02`/`DEL-024-03` are issued and locally accessible; carry `TBD` until then. | TBD |
| HRR-024-06-003 | `_Sources/26020-Package_Requirements.docx` may contain PKG-024-specific MV VFD acceptance requirements but was not parsed in this run, so no package-specific acceptance thresholds are populated. | `_REFERENCES.md` Missing/Deferred References; `_Sources/26020-Package_Requirements.docx` | This deliverable's drafted content | Datasheet Construction; Specification REQ-024-06-005/-010; Guidance Trade-offs | Parse PKG-024 slice in a Pass 3 / `lens-register` enrichment run once a deterministic extractor or a vetted text excerpt is available; preserve `TBD` until then. | TBD |
