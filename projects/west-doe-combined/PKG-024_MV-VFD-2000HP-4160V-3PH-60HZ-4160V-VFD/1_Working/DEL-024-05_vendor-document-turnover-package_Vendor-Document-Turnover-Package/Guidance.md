# Guidance: DEL-024-05_vendor-document-turnover-package

## Purpose

This deliverable exists to consolidate the Package Vendor's documentation obligations for `PKG-024` (MV VFD - 2000 HP, 4160 V, 3-phase, 60 Hz, 4160 V VFD) into a single Vendor Document Turnover Package: a register of vendor documents, the submittals themselves, the source-required documents where called out, and the final turnover record set, with EPC Integrator interface/integration review. The deliverable is the controlled handoff artifact for vendor-originated documentation, kept distinct from vendor engineering/equipment delivery (`DEL-024-04`) and from EPC review and acceptance evidence (`DEL-024-06`). (Sources: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-024-05`.)

## Principles

- The Package Vendor owns vendor documentation; the EPC Integrator reviews for interface and integration consistency. Do not blur these roles. (`PACKAGE_REGISTER.csv` row `PKG-024`.)
- Individual source document rows are evidence/artifacts under this deliverable, not standalone deliverables. (`_CONTEXT.md` Notes; `DELIVERABLE_REGISTER.csv` row `DEL-024-05`.)
- The vendor document register is the single point of truth for what is submitted, what is in review, what is accepted, and what forms the turnover record. (ASSUMPTION — industry convention; aligned with `_CONTEXT.md` Anticipated Artifacts.)
- Source-required vendor documents shall not be invented. When source material does not list specific required documents for `PKG-024`, the register reflects what the Package Vendor actually produces and explicitly marks source-required content as `TBD` until a source slice is accepted. (`ARTIFACT_REGISTER.csv` row `ART-66A1FEA60C`.)

## Considerations

- Interface evidence routing. Each applicable interface row for `PKG-024` (Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports) should be traceable to at least one vendor document; the register should make that mapping legible. (`INTERFACE_REGISTER.csv` rows for `PKG-024`.)
- Hazardous-area applicability. If the VFD or a VFD-fed motor lands in Zone 2, vendor documents must carry the marking and temperature-code evidence consistent with the EPC area-classification drawing or fugitive-emissions study. (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, VFD-fed motor / hazardous-area paragraph.)
- Source-required list gap. The accepted decomposition explicitly records that detailed vendor-document requirements are not present in current source material for this package. (`ARTIFACT_REGISTER.csv` row `ART-66A1FEA60C`: "Detailed vendor-document requirements are not present in current source material for this package.") Treat the source-required list as `TBD` until a `PKG-024`-specific slice from `26020-Package_Requirements.docx` (or equivalent) is accepted.
- Interaction with `DEL-024-06`. EPC review dispositions live with `DEL-024-06`; acceptance status should be reflected back into the vendor document register as evidence, not duplicated as primary content.

## Trade-offs

- Register depth vs. agility. A heavy register schema (every metadata field) gives strong auditability but adds friction; a light register is easier to keep current but weaker at evidence gap detection. Default to the minimum field set in Specification R-02 and extend only when a gap surfaces.
- Carrying source rows as artifacts vs. as deliverables. The decomposition has decided to carry them as artifacts; do not relitigate by spinning up per-document deliverables. (`_CONTEXT.md` Notes.)
- Including external standards (e.g., NETA, IEC, NEMA) as required vendor document drivers without a source slice would overstate the decomposition. Keep such drivers `ASSUMPTION` or `TBD` until accepted.

## Examples

No accessible source slice provides a worked example of a `PKG-024`-specific vendor document set, so concrete document-list examples are intentionally omitted. The DBM general references to VFDs (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`) inform interface and hazardous-area considerations but do not enumerate vendor documents.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-024-05-001 | The deliverable explicitly anticipates a "vendor document register" and "source-required vendor documentation" (`_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-024-05`), but `ARTIFACT_REGISTER.csv` row `ART-66A1FEA60C` records that detailed vendor-document requirements are not present in current source material for `PKG-024`. | `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row `DEL-024-05` | `ARTIFACT_REGISTER.csv` row `ART-66A1FEA60C` | Datasheet Attributes; Specification R-05; this Guidance | Carry the source-required vendor documentation list as `TBD` and treat the register schema as the active commitment until a `PKG-024`-specific source slice (e.g., from `26020-Package_Requirements.docx`) is accepted. | TBD |
| HRR-024-05-002 | The deliverable supports `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010` per `_CONTEXT.md`, associated by PACKAGE_HEURISTIC; it is not confirmed that all listed objectives are individually traceable to this specific vendor-documentation deliverable. | `_CONTEXT.md` Supports Objectives; `OBJECTIVE_DELIVERABLE_MAP.csv` | This deliverable's narrow scope (vendor documentation only) | Datasheet References; Specification scope | Treat objective association as ASSUMPTION (PACKAGE_HEURISTIC) and rely on `DEL-024-06` for objective-level acceptance evidence. | TBD |
| HRR-024-05-003 | Hazardous-area marking and temperature-code requirements applied via `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` assume the VFD or VFD-fed motor may be in Zone 2. The actual area classification for the `PKG-024` install location is not stated in accessible sources. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (VFD-fed motor / hazardous-area paragraph) | No accessible area-classification drawing for `PKG-024` | Datasheet Conditions; Specification R-07 | Keep R-07 conditional ("if … Zone 2") until the EPC area-classification drawing for the install location is accepted as evidence. | TBD |
