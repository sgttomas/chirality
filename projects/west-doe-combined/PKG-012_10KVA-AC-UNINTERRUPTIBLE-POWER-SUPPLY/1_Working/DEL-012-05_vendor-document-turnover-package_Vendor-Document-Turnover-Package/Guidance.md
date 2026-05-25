# Guidance: Vendor Document Turnover Package

## Purpose

This deliverable exists to preserve the vendor documentation and turnover evidence for the `PKG-012` 10KVA AC uninterruptible power supply package while maintaining the Gate 7 responsibility split: the Package Vendor owns vendor documentation and the EPC Integrator performs interface/integration review.

## Principles

- Treat Gate 7 as the accepted upstream truth for Phase 2.2.
- Keep vendor-owned content and EPC integration review evidence distinct.
- Use the vendor document register as the control point for submittals, turnover records, review status, and unresolved gaps.
- Preserve interface visibility for Electrical Power, Grounding / Bonding, Maintenance Access, and Structural / Foundations / Supports.
- Mark missing source requirements as `TBD`; do not infer a complete vendor document list from the package name alone.

## Considerations

- Gate 7 records only one artifact for this deliverable: `TBD vendor document register`, with the note that detailed vendor-document requirements are not present in current source material for this package.
- Objective `OBJ-010` is especially relevant because it names vendor-documentation, commissioning, turnover, and controlled open-item closure evidence as package procurement and downstream handoff needs.
- Objectives `OBJ-004` and `OBJ-005` frame the vendor/EPC split and the electrical power/interface basis; they should guide review coverage without becoming unverified clause-level requirements.
- Objectives `OBJ-008` and `OBJ-009` may be directionally relevant where structural/support/access or safety/compliance information appears in vendor submittals, but no package-specific detailed criteria are available in Gate 7.

## Trade-offs

| Topic | Trade-off | Recommended handling |
|---|---|---|
| Completeness vs. source fidelity | A complete vendor document list would be useful, but Gate 7 does not provide one for this package. | Keep the list `TBD` until a vendor document register or governing document-control source is accepted. |
| Vendor ownership vs. EPC review | Vendor documentation should not be rewritten as EPC design work. | Keep EPC content limited to review, interface, integration, and acceptance evidence. |
| Interface breadth vs. review burden | Gate 7 lists four interface types, but detailed acceptance criteria are unavailable. | Require explicit review disposition for each listed interface type or a justified not-applicable statement. |

## Examples

TBD. No package-specific example turnover forms, register templates, or vendor document tables are present in the accepted Gate 7 source set for this deliverable.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HR-012-05-001 | Required detailed vendor document list is unavailable; only a `TBD vendor document register` artifact is present. | Gate 7 `DELIVERABLE_REGISTER.csv`, `DEL-012-05_vendor-document-turnover-package` anticipated artifacts | Gate 7 `ARTIFACT_REGISTER.csv`, `ART-68AD3064DD` note: detailed vendor-document requirements are not present | Datasheet Attributes; Specification Requirements; Procedure Steps | Treat Gate 7 as authoritative for the gap; require human/vendor register before closure. | TBD |
| HR-012-05-002 | Project document-control procedure, review status codes, turnover acceptance form, and final record-document rules are not available in the accepted source set. | `_REFERENCES.md` lists Gate 7 and shared source root but no copied deliverable-specific source slices | Specification Standards and Verification require document-control rules for closure | Specification Standards; Procedure Verification; Records | Keep these requirements as `TBD` until a governing document-control source is accepted. | TBD |
