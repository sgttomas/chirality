# Guidance — DEL-052-05 Vendor Document Turnover Package (PKG-052)

> Directional. Provides rationale, principles, considerations, and trade-offs supporting the Specification. Items not supported by accessible source slices are marked `TBD` or `ASSUMPTION`.

## Purpose

This deliverable exists to consolidate, control, and turn over the vendor documentation set for PKG-052 (Inlet / TEG Dehy Cross Exchanger, E-5718-1) so that the EPC Integrator, the host facility, and downstream operations can:

- accept the vendor package against a single, source-anchored register;
- evidence quality, fabrication, inspection, and FAT outcomes;
- preserve as-built drawings, IOM material, and registration records as durable turnover evidence.

The deliverable scope is intentionally narrowed to **documentation** — physical equipment engineering belongs to DEL-052-04, EPC review/acceptance belongs to DEL-052-06, and construction execution belongs to DEL-052-03.

Source: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv rows 336-341.

## Principles

1. **Source-anchored register.** Each row in the register cites its decomposition source (Workbook Packages row 62; `26020-Package_Requirements.docx` heading 7 Vendor Engineering Deliverables table; or sibling deliverable). No invented document classes.
   - Source: ARTIFACT_REGISTER.csv (Source column convention).
2. **Carry rows as artifacts, not deliverables.** Individual source vendor-document rows remain artifact evidence under DEL-052-05; they are not promoted to standalone deliverables.
   - Source: DELIVERABLE_REGISTER.csv row 340 (Notes).
3. **Single vendor production unit.** PKG-052 has one vendor document production unit (this deliverable); EPC review is a separate review/acceptance deliverable (DEL-052-06).
   - Source: DELIVERABLE_REGISTER.csv rows 340, 341.
4. **Interface awareness.** The register's interface-discipline categories mirror the applicable interface types listed for PKG-052 (Process Piping; Utility Piping; Drain / Containment; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports).
   - Source: PACKAGE_REGISTER.csv row 62 (ApplicableInterfaceTypes).
5. **Turnover-readiness over completeness-for-its-own-sake.** Submittals are valuable to the extent they enable acceptance and durable operations evidence.

## Considerations

- **Document Control Procedure governs everything else.** Without an active vendor document control procedure, revision tracking, distribution, and acceptance handling are not enforceable. Plan to receive and approve this document first.
  - Source: ARTIFACT_REGISTER.csv DEL-052-05 (Vendor Document Control Procedure row); sequencing is `ASSUMPTION`.
- **Pressure equipment registration is a regulator-facing obligation.** E-5718-1 at 9,756 kPag is pressure equipment by any plausible jurisdictional threshold; the Pressure Equipment Registration Package must be planned early enough to support jurisdictional acceptance.
  - Source: SCOPE_LEDGER.csv SOW-0106; ARTIFACT_REGISTER.csv DEL-052-05.
- **FAT outcomes feed shipment release.** FAT procedure and FAT report belong to the heat exchanger's release-to-ship gating.
  - Source: ARTIFACT_REGISTER.csv DEL-052-05; sequencing `ASSUMPTION`.
- **Interface documents serve EPC integration.** Piping, drainage, electrical, I&C, and structural interface documents are the basis on which the EPC Integrator (under DEL-052-06) accepts integration readiness.
  - Source: PACKAGE_REGISTER.csv row 62; DELIVERABLE_REGISTER.csv row 341.

## Trade-offs

- **Granularity vs. usability of the register.** Carrying every source vendor-document row as a discrete artifact row gives strong traceability but produces a large register. The decomposition has accepted the trade-off in favor of granular traceability.
  - Source: DELIVERABLE_REGISTER.csv row 340 (Notes).
- **Early review effort vs. late rework.** Front-loading review on the Document Control Procedure, Supplier Quality Plan, and ITP increases early effort but reduces late rework on FAT, inspection releases, and final Vendor Data Book.
- **Standards specificity vs. local source absence.** Some standards (e.g., ASME BPVC Section VIII, jurisdictional pressure equipment regulator) are not explicitly cited in the accessible source slice. Treating them as `ASSUMPTION` preserves epistemic honesty; treating them as `FACT` would overclaim.

## Examples

Example register rows (drawn from ARTIFACT_REGISTER.csv DEL-052-05):

- `Vendor Document Index` (ART-FF916F10D3, Core vendor documents) — index for the rest of the submittals.
- `Inspection and Test Plan (ITP)` (ART-23F5BF5334, Core vendor documents) — fabrication-and-inspection plan tied to QLT-003.
- `Pressure Equipment Registration Package` (Heat transfer equipment) — jurisdictional registration evidence for E-5718-1.
- `Piping and Instrumentation Diagrams (P&IDs)` (Process package design) — vendor scope P&IDs forming the integration baseline.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-001 | Submittal lifecycle states (planned/submitted/under review/accepted/incorporated) are not explicitly listed in any accessible source slice; the Specification asserts them as ASSUMPTION. | Specification REQ-DEL-052-05-004 | `26020-Package_Requirements.docx` heading 7 — slice not directly accessible | Specification §Requirements; Procedure §Steps | PROPOSAL: confirm or revise lifecycle states when the source slice is extracted; default lifecycle as drafted | TBD |
| CONF-002 | Sequencing rules ("FAT before shipment"; "Document Control Procedure first") are inferred from document-name semantics, not stated in the accessible source slice. | Specification REQ-DEL-052-05-006, REQ-DEL-052-05-010 | `26020-Package_Requirements.docx` heading 7 — slice not directly accessible | Specification §Requirements; Procedure §Steps | PROPOSAL: confirm during EPC review or extract the source slice | TBD |
| CONF-003 | Governing pressure-equipment jurisdictional authority and code (e.g., ABSA, ASME BPVC Section VIII) is not explicitly cited in the accessible source slice. | Specification §Standards | Accessible source slices | Specification §Standards; Datasheet §Conditions | PROPOSAL: confirm jurisdiction and applicable code during EPC review | TBD |
