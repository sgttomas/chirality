# Guidance: DEL-032-05_vendor-document-turnover-package

## Purpose

The Vendor Document Turnover Package consolidates the Package Vendor's documentation set for `PKG-032` Cathodic Protection Design and Installation so the EPC Integrator can accept the package into facility records. It is the closing documentary deliverable for the vendor production unit (`DEL-032-04`), distinct from the EPC anchor deliverables (`DEL-032-01`/`-02`/`-03`). Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`.

## Principles

- **Vendor produces; EPC accepts.** Documentation is authored by the Package Vendor and reviewed/integrated by the EPC Integrator. Acceptance is recorded; it is not implied by transmittal.
- **Single closure artifact.** The Final Vendor Data Book (PRQ-016) is the consolidated closure artifact; all other documents are inputs into that compilation. Source: `_Sources/26020-Package_Requirements.docx`, Vendor Engineering Deliverables.
- **Artifacts, not deliverables.** Source vendor document table rows referenced upstream are carried as artifacts/evidence inside this deliverable, not promoted to standalone deliverables. Source: `_CONTEXT.md`, Notes.
- **Interface fidelity.** Vendor documentation must reflect the declared package interfaces (electrical power, grounding/bonding, I&C/control cabling, communications/network) so EPC integration is verifiable. Source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, row 34.

## Considerations

- **Generic vs. CP-specific document set.** The Vendor Engineering Deliverables list in `26020-Package_Requirements.docx` is generic. Cathodic protection introduces additional submittals — anode design records, soil resistivity surveys, rectifier data sheets, reference electrode installation records, current-density calculations, commissioning potential surveys — that are not enumerated in the accessible source. Tailoring of the vendor document list to CP is TBD pending EPC discipline ruling.
- **Standards basis is not source-anchored here.** Cathodic protection industry standards (e.g., NACE/AMPP SP0169 for external corrosion control of buried/submerged metallic piping; SP0285 for tank exteriors; ISO 15589 for pipelines) are conventionally applicable but no source slice in `_REFERENCES.md` cites them for PKG-032. Avoid asserting clause-level requirements from these standards in vendor data without source confirmation.
- **Lifecycle states.** Document submittal lifecycle (IFR/IFA/IFC/AFC, code 1/2/3/4, transmittal cadence) is not defined in accessible sources. The EPC document control procedure must be supplied before the vendor's DOC-008 procedure can be measured against it.
- **Turnover record set.** Installation, pre-commissioning, commissioning, mechanical completion, and final acceptance certificate templates are not defined in the accessible source set. Turnover record content remains TBD.

## Trade-offs

- **Breadth vs. tailoring.** Applying the full generic vendor document list maximizes documentation coverage but may overstate vendor effort for a comparatively self-contained CP package. The trade-off (drop, combine, or tailor entries) requires an EPC discipline ruling.
- **Interleaved vs. final-only review.** Interleaved EPC review during submittal extends EPC effort but reduces late re-work risk at turnover; final-only review compresses the EPC effort window but increases risk of late nonconformities in PRQ-016 compilation.

## Examples

No source-grounded examples of accepted vendor turnover packages for cathodic protection are available in the accessible source set. **TBD** pending EPC reference material.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-032-05-001 | The generic Vendor Engineering Deliverables list in `26020-Package_Requirements.docx` does not enumerate cathodic-protection-specific submittals (anode design records, soil resistivity surveys, rectifier datasheets, reference-cell installation, commissioning potential surveys). | `_Sources/26020-Package_Requirements.docx`, Vendor Engineering Deliverables table | Industry CP practice (no accessible source slice) | Datasheet "Cathodic protection-specific submittals"; Specification R-4, R-5, R-11; Procedure Steps 4-5 | PROPOSAL: Treat the generic list as the floor; add CP-specific submittals as a tailoring addendum to be confirmed by the EPC discipline lead. | TBD |
| CONF-032-05-002 | Submittal lifecycle (IFR/IFA/IFC/AFC, code 1/2/3/4) and transmittal cadence are not defined in accessible sources. | `_Sources/26020-Package_Requirements.docx` (silent) | EPC document control procedure (not accessible) | Specification R-2, R-12; Procedure Steps 2-3, 6 | PROPOSAL: Carry as TBD until EPC document control procedure is provided. | TBD |
| CONF-032-05-003 | Cathodic protection standards (NACE/AMPP SP0169, SP0285; ISO 15589) are conventionally applicable but no source slice in `_REFERENCES.md` cites them for PKG-032. | `_REFERENCES.md` (silent on CP standards) | Industry convention | Specification Standards row; Guidance Considerations | PROPOSAL: Mark as ASSUMPTION/location TBD; do not derive clause-level requirements until confirmed. | TBD |
