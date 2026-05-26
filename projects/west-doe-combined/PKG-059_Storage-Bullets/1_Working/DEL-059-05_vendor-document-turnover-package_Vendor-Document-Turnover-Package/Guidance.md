# Guidance — DEL-059-05 Vendor Document Turnover Package (PKG-059)

> Directional. Provides rationale, principles, considerations, and trade-offs supporting the Specification. Items not supported by accessible source slices are marked `TBD` or `ASSUMPTION`.

## Purpose

This deliverable exists to consolidate, control, and turn over the vendor documentation set for PKG-059 (Storage Bullets — two unstable condensate bullets and sixteen LPG product bullets) so that the EPC Integrator, the host facility, and downstream operations can:

- accept the vendor package against a single, source-anchored register;
- evidence quality, fabrication, inspection, pressure-equipment registration, and FAT outcomes per bullet;
- preserve as-built drawings, IOM material, relief/flare/vent design records, and civil containment evidence as durable turnover evidence.

The deliverable scope is intentionally narrowed to **documentation** — physical equipment engineering belongs to DEL-059-04, EPC review/acceptance belongs to DEL-059-06, and construction execution belongs to DEL-059-03. Foundations, DCS integration, and MCC-side electrical supply are out of vendor scope entirely.

Source: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv rows 462-467; SCOPE_LEDGER.csv SOW-0184.

## Principles

1. **Source-anchored register.** Each row in the register cites its decomposition source (Workbook Packages row 83; `26020-Package_Requirements.docx` heading 14 Vendor Engineering Deliverables table; or sibling deliverable). No invented document classes.
   - Source: ARTIFACT_REGISTER.csv (Source column convention).
2. **Carry rows as artifacts, not deliverables.** Individual source vendor-document rows remain artifact evidence under DEL-059-05; they are not promoted to standalone deliverables.
   - Source: DELIVERABLE_REGISTER.csv row 466 (Notes).
3. **Single vendor production unit.** PKG-059 has one vendor document production unit (this deliverable); EPC review is a separate review/acceptance deliverable (DEL-059-06).
   - Source: DELIVERABLE_REGISTER.csv rows 466, 467.
4. **Interface awareness.** The register's interface-discipline categories mirror the applicable interface types listed for PKG-059 (Process Piping; Relief / Flare / Vent; Drain / Containment; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports).
   - Source: PACKAGE_REGISTER.csv row 83 (ApplicableInterfaceTypes).
5. **Turnover-readiness over completeness-for-its-own-sake.** Submittals are valuable to the extent they enable acceptance and durable operations evidence.
6. **Bullet-fleet bookkeeping.** Per-unit evidence (pressure equipment registration, FAT records, material test reports) must be traceable per bullet across the fleet of eighteen units (two unstable condensate + sixteen LPG product).
   - Source: SCOPE_LEDGER.csv SOW-0183.

## Considerations

- **Document Control Procedure governs everything else.** Without an active vendor document control procedure, revision tracking, distribution, and acceptance handling are not enforceable. Plan to receive and approve this document first.
  - Source: ARTIFACT_REGISTER.csv ART-D4D95E703A; sequencing is `ASSUMPTION`.
- **Pressure equipment registration is a regulator-facing obligation per bullet.** Each bullet at 1724 kPag and full-vacuum design is pressure equipment by any plausible jurisdictional threshold; the Pressure Equipment Registration Package must be planned early enough to support jurisdictional acceptance for all eighteen units.
  - Source: SCOPE_LEDGER.csv SOW-0183; ARTIFACT_REGISTER.csv ART-01EEC704CB.
- **Relief / flare / vent design is non-negotiable for LPG storage.** LPG product storage with full-vacuum design pressure raises both overpressure protection (PSV sizing, flare loads) and vacuum protection considerations; the relief/flare/vent category documents are the basis for safety acceptance.
  - Source: ARTIFACT_REGISTER.csv (Relief / flare / vent category rows); SCOPE_LEDGER.csv SOW-0183.
- **LPG vapour equalization and blanket gas are scope-defining features.** SOW-0184 explicitly calls out that LPG vapour equalization must avoid pockets and butane storage requires blanket gas; the P&IDs, line list, tie-in list, and Control Narrative must show these features.
  - Source: SCOPE_LEDGER.csv SOW-0184.
- **Civil grading and spill containment carry LPG inventory risk.** With sixteen LPG bullets, retention pond / containment basin sizing and grading become safety-relevant turnover documents, not merely civil convenience.
  - Source: PACKAGE_REGISTER.csv row 83 (Applicable interface types); ARTIFACT_REGISTER.csv (Civil category rows).
- **FAT outcomes feed shipment release per bullet.** FAT procedure and FAT report belong to each bullet's release-to-ship gating.
  - Source: ARTIFACT_REGISTER.csv ART-0D1E51ADA7, ART-5098C5E6CC; sequencing `ASSUMPTION`.
- **Interface documents serve EPC integration.** Piping, drainage, electrical (lighting/EHT/grounding), I&C, structural (foundations/anchors/access), and civil interface documents are the basis on which the EPC Integrator (under DEL-059-06) accepts integration readiness.
  - Source: PACKAGE_REGISTER.csv row 83; DELIVERABLE_REGISTER.csv row 467.
- **Scope-by-others must be visible in interface documents.** Foundations, DCS integration, and MCC electrical supply are by others (per SOW-0184); the vendor must still supply Foundation Drawings, Anchor Bolt / Embedment Drawings, DCS I/O List, Cause and Effect Matrix, and Package Vendor Interface Specification so EPC can execute these.
  - Source: SCOPE_LEDGER.csv SOW-0184; ARTIFACT_REGISTER.csv DEL-059-05 (interface rows).

## Trade-offs

- **Granularity vs. usability of the register.** Carrying every source vendor-document row as a discrete artifact row (93 rows for DEL-059-05) gives strong traceability but produces a large register. The decomposition has accepted the trade-off in favor of granular traceability.
  - Source: DELIVERABLE_REGISTER.csv row 466 (Notes); ARTIFACT_REGISTER.csv DEL-059-05 row count.
- **Per-bullet vs. fleet-level evidence aggregation.** Pressure-equipment registration and FAT records logically apply per-bullet (eighteen unit-level records). Some other records (Mechanical Design Basis, Supplier Quality Plan, Relief and Flare Design Basis) make sense once at fleet level. The register should track which records are per-bullet and which are fleet-level — explicit per-bullet vs. fleet-level convention is `location TBD` in the accessible source slice.
- **Early review effort vs. late rework.** Front-loading review on the Document Control Procedure, Supplier Quality Plan, ITP, and Relief / Flare design basis increases early effort but reduces late rework on FAT, inspection releases, registration packages, and final Vendor Data Book.
- **Standards specificity vs. local source absence.** Several standards (ASME BPVC Section VIII, API 2510/510, jurisdictional pressure equipment regulator) are not explicitly cited in the accessible source slice. Treating them as `ASSUMPTION` preserves epistemic honesty; treating them as `FACT` would overclaim.

## Examples

Example register rows (drawn from ARTIFACT_REGISTER.csv DEL-059-05):

- `Vendor Document Index` (ART-3E0A93243E, Core vendor documents) — index for the rest of the submittals.
- `Inspection and Test Plan (ITP)` (ART-80332A9924, Core vendor documents) — fabrication-and-inspection plan covering all eighteen bullets.
- `Pressure Equipment Registration Package` (ART-01EEC704CB, Static pressure equipment) — jurisdictional registration evidence per bullet.
- `PSV / Pressure Relief Sizing Calculations` (ART-FEBD5A09B8, Relief / flare / vent design) — overpressure protection basis.
- `Retention Pond / Containment Basin Design` (Civil grading / spill containment interfaces) — secondary-containment evidence for LPG inventory.
- `Piping and Instrumentation Diagrams (P&IDs)` (ART-19D47BD356, Process piping interfaces) — vendor scope P&IDs showing vapour equalization and blanket-gas arrangements.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-001 | Submittal lifecycle states (planned/submitted/under review/accepted/incorporated) are not explicitly listed in any accessible source slice; the Specification asserts them as ASSUMPTION. | Specification REQ-DEL-059-05-004 | `26020-Package_Requirements.docx` heading 14 — slice not directly accessible | Specification §Requirements; Procedure §Steps | PROPOSAL: confirm or revise lifecycle states when the source slice is extracted; default lifecycle as drafted | TBD |
| CONF-002 | Sequencing rules ("FAT before shipment"; "Document Control Procedure first") are inferred from document-name semantics, not stated in the accessible source slice. | Specification REQ-DEL-059-05-006, REQ-DEL-059-05-010 | `26020-Package_Requirements.docx` heading 14 — slice not directly accessible | Specification §Requirements; Procedure §Steps | PROPOSAL: confirm during EPC review or extract the source slice | TBD |
| CONF-003 | Governing pressure-equipment jurisdictional authority and code (e.g., ABSA, ASME BPVC Section VIII, API 2510) are not explicitly cited in the accessible source slice. | Specification §Standards | Accessible source slices | Specification §Standards; Datasheet §Conditions | PROPOSAL: confirm jurisdiction and applicable code during EPC review | TBD |
| CONF-004 | Per-bullet vs. fleet-level convention for pressure equipment registration, FAT records, and material test reports is not explicit in the accessible source slice. | Specification REQ-DEL-059-05-005, REQ-DEL-059-05-006 | `26020-Package_Requirements.docx` heading 14 — slice not directly accessible | Specification §Requirements; Procedure §Steps; Datasheet §Conditions | PROPOSAL: default to per-bullet for registration, FAT, and material certs; fleet-level for design basis documents; confirm with EPC | TBD |
| CONF-005 | Explicit document-to-feature mapping for LPG vapour equalization and butane blanket gas (which documents must show them) is not stated in the accessible source slice; assumed to be P&IDs, line list, tie-in list, and Control Narrative. | Specification REQ-DEL-059-05-012 | SCOPE_LEDGER.csv SOW-0184 (states the features, not the documenting documents) | Specification §Requirements; Procedure §Steps | PROPOSAL: confirm document mapping during EPC review | TBD |
