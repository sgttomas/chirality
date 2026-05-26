# Guidance: DEL-106-05 — Vendor Document Turnover Package

Pass: P1/P2 (initial draft and cross-reference sweep) — Source-grounded against GATE-07 Final Published PROJECT_DECOMP snapshot.

## Purpose

PKG-106 (Yard Lighting) is a workbook-defined vendor-owned Electrical package. The Package Vendor owns package engineering, design, vendor documentation, and the physical equipment, while the EPC Integrator owns facility-level integration (Source: PACKAGE_REGISTER.csv). DEL-106-05 exists to consolidate, register, and turn over the full vendor document set that supports the engineered equipment package (DEL-106-04) and enables the EPC Integrator's review and acceptance (DEL-106-06). It is the documentation backbone for the package's lifecycle handoff.

## Principles

- **Single vendor document deliverable.** Per `_CONTEXT.md`, individual source vendor-document rows are artifacts/evidence, not separate deliverables. This keeps the vendor's documentation surface coherent under one turnover unit. (Source: `_CONTEXT.md` Notes; DELIVERABLE_REGISTER.csv.)
- **Register before submittal.** A documented Vendor Document Register precedes and indexes the submittals so that completeness can be evaluated against a known target (ASSUMPTION based on standard turnover practice; not stated in source).
- **Vendor produces, Integrator reviews.** The producing/reviewing split is asymmetric and explicit. The vendor authors and submits; the EPC Integrator reviews and accepts under DEL-106-06. (Source: DELIVERABLE_REGISTER.csv; PACKAGE_REGISTER.csv.)
- **Source-grounded contents.** Where the source workbook enumerates required vendor documents for the package, those entries determine the register's required minimum. Where the source is silent (as it currently is for PKG-106 — ART-182773E33C), required content is TBD and must be resolved with the responsible party.
- **Interface-aware documentation.** Vendor documentation must reflect the package's three declared interfaces — Electrical Power, Grounding / Bonding, and Area / Exterior Lighting — so the EPC Integrator can verify tie-ins against DEL-106-02 evidence. (Source: INTERFACE_REGISTER.csv; PACKAGE_REGISTER.csv.)

## Considerations

- **Vendor-document source gap.** ART-182773E33C explicitly flags the vendor document register as "TBD" with "Vendor Documentation Gap Evidence" because detailed requirements are not present in current source material for PKG-106. Any concrete vendor-document list assembled now is provisional. (Source: ARTIFACT_REGISTER.csv.)
- **Workbook xlsx not opened.** `_Sources/26020-Packages_Interfaces_4_export.xlsx` and `_Sources/26020-Package_Requirements.docx` exist in the shared source root but were not opened during this drafting pass — the GATE-07 snapshot's register CSVs are the locally-accessible authoritative extracts. Clause-level vendor-doc requirements may exist there: location TBD.
- **WBS unknown.** PKG-106 WBS is TBD in the source (PACKAGE_REGISTER.csv). Vendor document numbering schemes that depend on WBS cannot be fixed until that is resolved.
- **Objective mapping is heuristic.** OBJ-001/004/005/009/010 are associated via the package-grouping heuristic and `_CONTEXT.md`. Treat as directionally relevant, not as hard requirements, until human-confirmed against OBJECTIVE_DELIVERABLE_MAP.csv at deliverable granularity.

## Trade-offs

- **Comprehensive register vs. just-in-time submittal.** A larger up-front register improves auditability of the turnover but increases vendor effort before source-driven scope is firm. Given the current PKG-106 source gap, a minimal seed register that is iterated as source clarifies is the conservative path (ASSUMPTION).
- **Carrying source rows as artifacts vs. promoting them to deliverables.** The decomposition explicitly chose the artifact treatment (Source: `_CONTEXT.md` Notes; DELIVERABLE_REGISTER.csv). This keeps the deliverable count stable and the vendor's documentation surface unified, at the cost of needing care so that no individually-required source document is overlooked when the register is built.
- **EPC review depth.** Light EPC review accelerates handoff but risks integration defects surfacing late; deep review is safer but consumes integrator effort. Depth is governed by DEL-106-06, not this deliverable.

## Examples

- TBD — no source-supported examples are available. Examples from sibling DEL-xxx-05 deliverables in PROJECT_DECOMP (e.g., DEL-011-05, DEL-014-05, DEL-020-05) share identical decomposition narrative wording and likewise carry no enumerated vendor-document rows in the GATE-07 snapshot. (Source: DELIVERABLE_REGISTER.csv.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-01 | Decomposition anticipates a "Vendor document register" as a required artifact, but ARTIFACT_REGISTER.csv records the register for PKG-106 as `ART-182773E33C "TBD vendor document register"` with explicit "Vendor Documentation Gap Evidence", i.e., the required content is not actually defined in source. | DELIVERABLE_REGISTER.csv (DEL-106-05 Anticipated Artifacts); `_CONTEXT.md` Anticipated Artifacts | ARTIFACT_REGISTER.csv (ART-182773E33C) | Datasheet (Construction); Specification (REQ-106-05-01, REQ-106-05-08); Procedure (Steps 1-2) | Treat the register as required-in-form but TBD-in-content; resolve content by opening the workbook source (xlsx/docx) or by EPC + Vendor agreement on a project-standard vendor-document list. | TBD |
| CONF-02 | Objective mapping in `_CONTEXT.md` (OBJ-001/004/005/009/010) is reproduced from the DELIVERABLE_REGISTER row but is also derived via the package-grouping heuristic; deliverable-level OBJECTIVE_DELIVERABLE_MAP.csv was not opened to confirm exact deliverable-row associations. | `_CONTEXT.md` Supports Objectives | OBJECTIVE_DELIVERABLE_MAP.csv (not opened in this pass) | Datasheet (Identification); Specification (REQ-106-05-07) | Keep the listed objectives as ASSUMPTION (package-heuristic) until confirmed. | TBD |
| CONF-03 | PACKAGE_REGISTER.csv lists Package WBS as TBD. Any vendor document numbering or coding scheme that assumes a WBS will need that resolved. | PACKAGE_REGISTER.csv (PKG-106 WBS) | None | Datasheet (Attributes); Procedure (Step 1) | Defer numbering scheme decisions until WBS is set; record as TBD in register skeleton. | TBD |
