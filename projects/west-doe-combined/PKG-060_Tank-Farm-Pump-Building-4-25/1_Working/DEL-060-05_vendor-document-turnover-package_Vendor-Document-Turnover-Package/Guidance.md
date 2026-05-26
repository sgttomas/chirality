# Guidance: DEL-060-05_vendor-document-turnover-package

## Purpose

This guidance explains why the Vendor Document Turnover Package for `PKG-060` (Tank Farm Pump Building 4-25) exists, the principles that govern how it is assembled and reviewed, the considerations its authors and reviewers should weigh, the trade-offs that recur in pump-building vendor turnover, and example patterns drawn from the accepted decomposition.

The Vendor Document Turnover Package is the single Package-Vendor deliverable that conveys all source-required vendor documentation, the vendor document register, vendor document submittals, and turnover records to the EPC Integrator. It is the input to `DEL-060-06_epc-vendor-package-review-and-acceptance`. Without it, EPC Integrator interface/integration review cannot demonstrate that the Package Vendor has discharged its scope.

## Principles

- **Source authority before convention.** Vendor document categories and items are governed by `26020-Package_Requirements.docx` package heading 15 (Vendor Engineering Deliverables table) and the resulting Gate 7 `ARTIFACT_REGISTER.csv` rows. Generic vendor-document convention does not override the source. (`_REFERENCES.md`; `ARTIFACT_REGISTER.csv`.)
- **Decomposition routes; sources determine content.** The Gate 7 decomposition routes which vendor document categories and interfaces apply to `PKG-060`. The detailed wording, numbering, and acceptance criteria are governed by the source package requirements text and the project vendor document control specification.
- **Register-first.** The vendor document register is the spine of the turnover package; all submittals and turnover records must be traceable to a register row.
- **Interface-complete.** The fourteen PKG-060 interface facts in `INTERFACE_REGISTER.csv` must each be addressed by at least one vendor document; uncovered interfaces are gaps to be recorded, not omitted.
- **Artifact, not deliverable.** Individual rows of the source Vendor Engineering Deliverables table are evidence under this one production unit and are not promoted to separate `DEL-*` records.
- **TBD over invention.** Numbering schemes, submittal acceptance criteria, and turnover record templates that are not present in accessible source slices remain `TBD` until vendor data or extracted source resolves them.

## Considerations

- **Pump-building scope drives rotating-equipment depth.** The 4-25 Tank Farm Pump Building houses condensate transfer, water transfer, condensate recycle, and process water transfer pumps (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2555, 2618-2622). The vendor document set must include pump data sheets, NPSH calculations, mechanical seal/lube oil specifications, motor starting study, and FAT procedures and reports proportionate to this scope.
- **EHT and freeze protection.** EHT is a PKG-060 interface (`IFC-10732C110E`). Sour produced water service in cold-climate sites typically depends on dual heat-tracing circuits; vendor documents shall include the EHT design package and piping insulation/heat tracing schedule (`ARTIFACT_REGISTER.csv` rows `ART-9BBED06174`, `ART-F48D2609DA`, `ART-609CA4DDC5`).
- **Cathodic protection scope.** The CP interface fact (`IFC-E715EB5D71`) applies, but no dedicated CP artifact is enumerated in `ARTIFACT_REGISTER.csv` for `DEL-060-05`. Reviewers should confirm whether CP is delivered under the structural/foundations artifact set or whether a separate CP design package is required (`TBD`).
- **Fire and gas / SIL.** PKG-060 carries a Fire & Gas / Safety Systems interface (`IFC-0A19AB343B`) and the artifact register lists SIL determination, SRS, and supplier SIL documentation. The Package Vendor must coordinate supplier SIL documentation with project-level SIL determination so the EPC review can close on SIL/SRS consistency.
- **Building / HVAC and occupied-building risk.** The Building HVAC / Services interface (`IFC-AE5871A3F7`) and the building/HVAC/code artifact category include occupied-building risk assessment and ventilation inputs; the building-type and human-occupancy assumptions should be confirmed with the EPC Integrator before submittal.
- **Maintenance access for pump removal.** Lifting/handling study (`ART-88C54F4EBB`) and platform/access drawings (`ART-57485C85B5`) must demonstrate that the largest pump and motor can be removed without disturbing other equipment.

## Trade-offs

- **Submit-as-package vs. submit-by-discipline.** Bundling all categories into a single submittal simplifies turnover indexing but slows iterative EPC review. Discipline-by-discipline submittals enable parallel review but increase register and revision-control overhead. The chosen approach should be agreed early and recorded.
- **Vendor numbering vs. project numbering.** Pure vendor numbering preserves vendor traceability; project-numbered documents simplify EPC document control. The project vendor document control specification is the governing reference (location TBD); until accessible, the register should carry both identifiers.
- **FAT scope depth.** Deeper FAT scope catches more issues pre-shipment but compresses the schedule and increases vendor cost. Pump-building FAT typically covers pump performance and mechanical run; extension to packaged-instrument loop verification is a project choice.
- **Final documentation media.** Vendor data books delivered as bound paper preserve historical practice; electronic-only delivery reduces handling but requires verified site search capability. Project document control should specify.

## Examples

- **Vendor document register as the spine.** `ART-0D208A7734` (Vendor document register) anchors all other rows in `ARTIFACT_REGISTER.csv` for `DEL-060-05`; every submittal cites a register row.
- **Core vendor documents.** `ART-592E147111` (Vendor Document Index), `ART-1C06C559C8` (Vendor Document Control Procedure), `ART-B3643E864D` (Supplier Quality Plan), `ART-75C9A5E28A` (ITP), `ART-D923215BF0` (MTRs), `ART-946006CE7C` (Inspection Release Certificate), `ART-326C9FD2D6` (MRB / Vendor Data Book), `ART-C3FA5659EF` (Final Supplier Documentation).
- **Rotating-equipment depth.** `ART-9ACA1B82C8` (Pump Data Sheets), `ART-BC76FBFF8B` (Pump Hydraulic / NPSH Calculations), `ART-B7CC124120` (Mechanical Seal / Lube Oil Specification), `ART-E7FADAEFB7` (Motor Starting Study).
- **Process piping depth.** `ART-60DD9FC11C` (P&IDs), `ART-BF1997D4DC` (Tie-In List), `ART-B02B6C22C5` (Piping Isometric Drawings), `ART-E9627A4EE5` (Hydrotest/Pressure Test Packages).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-060-05-001 | The vendor document numbering convention is not present in accessible markdown sources; `26020-Package_Requirements.docx package heading 15` is cited but not extracted. | `_REFERENCES.md` (Missing/Deferred References) | `ARTIFACT_REGISTER.csv` rows (register/index entries imply a convention exists) | Datasheet "Detailed numbering scheme"; Specification REQ-060-05-010 | PROPOSAL: defer to project vendor document control specification when extracted; until then mark `TBD`. | TBD |
| CONF-060-05-002 | Cathodic Protection interface applies (`IFC-E715EB5D71`) but no CP-specific artifact is enumerated in `ARTIFACT_REGISTER.csv` for `DEL-060-05`. | `INTERFACE_REGISTER.csv` `IFC-E715EB5D71` | `ARTIFACT_REGISTER.csv` rows for `DEL-060-05` (no CP row) | Datasheet Conditions row "Cathodic Protection"; Specification REQ-060-05-009 | PROPOSAL: include CP design basis under Structural / access artifact set, or add a CP-specific artifact during register issue. | TBD |
| CONF-060-05-003 | Objective-to-deliverable mapping is package-grouped, not deliverable-grouped; the supported-objectives list (`OBJ-001`, `OBJ-003`-`OBJ-010`) is heuristic. | `_CONTEXT.md` (Supports Objectives list) | `OBJECTIVE_DELIVERABLE_MAP.csv` (package-grouped rows) | Datasheet Attributes row "Supported objectives" | PROPOSAL: retain as ASSUMPTION (PACKAGE_HEURISTIC) pending human confirmation of objective scope. | TBD |
