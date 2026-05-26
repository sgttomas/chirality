# Guidance — DEL-095-05 Vendor Document Turnover Package

## Purpose

The Vendor Document Turnover Package exists so that, at the point of vendor-to-EPC and EPC-to-owner handover, there is a single, well-indexed, source-traceable body of evidence demonstrating that the PKG-095 Slop Tank (API 650) vendor scope is documented, complete, and acceptable for integration into the facility. The package is the durable record that an external party can rely on to operate, inspect, maintain, and audit the slop-tank package without re-discovering vendor intent.

It is a **vendor production unit deliverable** (Package Vendor responsible) with EPC Integrator interface/integration review — not an EPC-authored document.

## Principles

1. **Register-first.** The Vendor Document Register is the spine of the package. Every other artifact is reachable from a register row.
2. **Source rows as artifacts.** Individual rows of the source vendor document table (heading 47, `26020-Package_Requirements.docx`) live here as evidence; they are not split out as separate deliverables (`_CONTEXT.md` Notes).
3. **Scope boundary preservation.** Vendor content stays vendor-owned; EPC review/acceptance lives in `DEL-095-06`. Construction and installation records live in `DEL-095-03`. Do not mix.
4. **Trace to equipment and SOW.** Every document row should be traceable to a tagged piece of equipment (anchored by the API 650 slop tank, likely TK-9130-2) and to the SOW items SOW-0213..SOW-0216.
5. **Turnover means acceptance-ready.** A turnover record is not just a transmittal — it must demonstrate that the EPC reviewer can close out interface/integration acceptance against the SOW, Package Datasheet, and Construction Work Package.

## Considerations

- The Package Vendor controls revision discipline; the EPC Integrator's review cadence and acceptance criteria are defined upstream in `DEL-095-01` (SOW) and `DEL-095-02` (Package Datasheet) and operationalized in `DEL-095-06`.
- API 650 fabrication imposes specific evidence classes (MTRs, weld/NDE, hydrotest, coating). These classes typically populate any vendor document register for an atmospheric tank package; however, the project-specific heading-47 source row list is the binding list once extracted.
- Slop service implies contamination-class considerations (off-spec condensate, contaminated hydrocarbons, treating-chemical-bearing liquids) per SOW-0216. Document evidence around materials compatibility, coating, and venting selections gains weight from this service classification, but the document **list** itself is governed by heading-47 source rows.
- The final source list, disposition path, and tank design basis for slop sources remain open (SOW-0216). This affects which equipment-tagged documents are eventually pulled into the register; expect register churn until those are confirmed.

## Trade-offs

- **Breadth vs. discipline.** Pulling every conceivable tank-vendor document into the register reduces audit risk but inflates review burden. Resolution: bind the register to the heading-47 source list once extracted, plus any documents the EPC Integrator explicitly demands during DEL-095-06.
- **Vendor format vs. project format.** Vendor-native formats (e.g., proprietary CAD, vendor templates) accelerate vendor delivery but slow EPC integration. Resolution: accept vendor-native originals as artifacts and require structured metadata (number, revision, status, date, scope tag) in the register itself.
- **Early staging vs. final turnover.** Submitting documents only at end-of-project simplifies vendor workflow but blocks DEL-095-06 review; staging documents through revisions enables review but multiplies handling. Resolution: maintain rolling register state through the project; the "turnover record" is the final acceptance-ready snapshot.

## Examples

- A "vendor document register" row for the API 650 slop tank GA drawing would include: document number, revision, issue status (e.g., IFR/IFA/IFC), equipment tag (e.g., TK-9130-2), SOW linkage (SOW-0215), and a path to the latest submittal artifact.
- A turnover record for the slop tank hydrotest would include the source vendor document table row reference, the dated test certificate, vendor sign-off, EPC integrator acknowledgment from DEL-095-06, and any deviation/disposition note.

(These are convention-based examples; the binding shape of register rows and turnover records is TBD pending project document-control basis.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-095-05-01 | Specific vendor document classes required (REQ-095-05-08) are derived by convention (API 650 tank package norms), not from extracted heading-47 source rows. | DBM §Mechanical Package Structure (line 617) — generic "vendor document registers" only | `26020-Package_Requirements.docx` heading 47 — binary, not extracted locally | Datasheet §Construction; Specification REQ-095-05-02, REQ-095-05-08; Guidance §Principles, §Considerations | PROPOSAL: Extract heading-47 source slice (markdown conversion) and replace ASSUMPTION-labeled rows with heading-47-grounded ones. Treat current list as ASSUMPTION until extraction. | TBD |
| C-095-05-02 | Equipment list anchor (TK-9130-2) is qualified by source as "likely". SOW-0216 declares the final source list, disposition path, and tank design basis require process confirmation. | SCOPE_LEDGER SOW-0215 — "likely TK-9130-2" | SCOPE_LEDGER SOW-0216 — open items including final source list and tank design basis | Datasheet §Identification/Attributes; Specification REQ-095-05-06; Guidance §Considerations | PROPOSAL: Treat TK-9130-2 as ASSUMPTION until process confirmation; do not write final equipment tag into a binding register column until confirmed. | TBD |
| C-095-05-03 | Register and turnover record format conventions (schema, file types) are not specified by accessible sources. | DBM (silent on register schema) | `26020-Package_Requirements.docx` heading 47 (binary; possibly specifies — unverified) | Specification §Documentation; Procedure §Steps, §Records | PROPOSAL: Adopt project document-control basis once published; until then, require minimum register metadata (number, revision, status, date, scope/equipment tag, submittal path) as a working baseline. | TBD |
| C-095-05-04 | The DBM source labels the trove generically as "vendor document registers" (plural) for mechanical packages; the deliverable register names a single Vendor Document Turnover Package. | DBM §Mechanical Package Structure (line 617) | DELIVERABLE_REGISTER row DEL-095-05 | Guidance §Purpose, §Principles; Specification §Scope | PROPOSAL: Treat the DBM's "vendor document registers" as a class label and this deliverable as the package-level instance for PKG-095. No conflict in intent; flag for human confirmation. | TBD |

**HRR (Hold/Review/Required) note:** All four conflict rows above are HRR items requiring human ruling before any value asserted here becomes binding.
