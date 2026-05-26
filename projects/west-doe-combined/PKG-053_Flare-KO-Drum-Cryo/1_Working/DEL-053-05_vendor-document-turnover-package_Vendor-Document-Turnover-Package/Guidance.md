# Guidance — DEL-053-05 Vendor Document Turnover Package (Flare KO Drum, Cryo)

> Directional guidance for assembling and executing the vendor document turnover package for PKG-053. Captures intent behind the granularity rule, EPC/Vendor split, and key risks for cryogenic-service documentation.

## Purpose

Provide a single consolidated vendor-document production unit so that:
- All vendor-required documents from the source Vendor Engineering Deliverables table are held under one deliverable and one register, rather than as dozens of separate deliverables.
- EPC Integrator review of vendor documents has one consistent interface (this deliverable -> DEL-053-06 acceptance).
- The Package Vendor has a clear bound for its documentation responsibility and turnover obligation.
- Source-required document categories are preserved as artifacts/evidence, not lost in deliverable noise.

Source: DELIVERABLE_REGISTER.csv DEL-053-05; PROJECT_DECOMP DEC-004; PROJECT_DECOMP Gate 5 narrative ("vendor-document turnover is a single deliverable where needed").

## Principles

1. **Single-deliverable consolidation.** Vendor documentation for one package is one production unit. The register, not the deliverable graph, enumerates documents. Source: PROJECT_DECOMP DEC-004.
2. **Source-row fidelity as artifacts.** Each source-required vendor document row from `26020-Package_Requirements.docx` heading 8 is preserved as an artifact in the Gate 7 ARTIFACT_REGISTER; the vendor register MUST cover every such row. Source: ARTIFACT_REGISTER.csv DEL-053-05 (97 rows).
3. **EPC/Vendor split is permanent.** Package Vendor produces and owns the documents; EPC Integrator reviews and integrates. Acceptance is not granted in this deliverable; it lives in DEL-053-06. Source: PROJECT_DECOMP DEC-006; DELIVERABLE_REGISTER.csv DEL-053-05 ResponsibleParty.
4. **Cryogenic-service rigor.** Documents must reflect sub -45.5 degC service basis (impact testing, MDMT, PSV sizing, blowdown studies). Source: DEL-053-04 Datasheet (sibling); DBM-Deepcut cryogenic flare row.
5. **Turnover bundle finality.** The final Vendor Data Book (PRQ-016) is the binding turnover artifact; the register and individual submittals are working state on the way to it.
6. **Conservative inference.** Vendor document numbers, revisions, and submittal schedules are vendor-scope. Until vendor award and document control plan are received, those fields remain TBD; do not invent them.

## Considerations

- **Document count is large.** ARTIFACT_REGISTER.csv contains ~97 rows for DEL-053-05 across nine-plus categories. Register tooling and EPC review capacity must be sized for this volume. ASSUMPTION: a spreadsheet or document management system will be used; format TBD.
- **Category boundaries overlap.** Some artifacts straddle categories (e.g., heat tracing appears under Electrical and under piping). The register SHOULD use a single canonical category per row plus cross-references where needed.
- **Cryogenic items are a small but high-consequence subset.** PRO-015 PSV sizing, PRO-018 blowdown, MEC-009 vessel data sheet, QLT-013 MTRs with impact data, REG-022 registration package — these require focused EPC review.
- **Interface specs feed two deliverables.** CTL-026 Package Vendor Interface Specification and CTL-006 DCS I/O List feed both vendor turnover (here) and EPC integration (DEL-053-02 interface facts; DEL-053-06 acceptance). Alignment is essential; misalignment is a top integration risk.
- **Some categories are aspirational pending vendor scope.** Electrical, structural, civil, and HVAC categories may be partially in vendor scope and partially EPC scope depending on the package boundary. The Scope of Work (DEL-053-01) defines the cut. The register MUST reflect only what the vendor produces.
- **Hold-points need EPC bandwidth.** The ITP (QLT-003) defines witness/hold points. EPC review capacity must be planned around the fabrication schedule (location TBD).
- **Pressure registration timing.** REG-022 typically requires pre-fabrication submittal for design review by the jurisdictional authority; delays here can stop fabrication. Surface this risk early.

## Trade-offs

| Decision | Option A | Option B | Note |
|---|---|---|---|
| Register tooling | Spreadsheet (simple, vendor-friendly) | Document management system (better access control, audit trail) | TBD (project policy not in accessible sources). |
| Vendor-document numbering | Vendor's native scheme | Project-mapped scheme | ASSUMPTION: vendor's native scheme with project cross-reference column; final policy TBD. |
| Comment incorporation | Iterative revisions | Batched at hold points | Iterative recommended for cryogenic safety-critical documents; batched acceptable for non-safety documents. |
| Vendor Data Book medium | Bound paper + digital | Digital-only | TBD (project archival policy). |
| Coverage of "may-not-apply" categories (e.g., HVAC) | Register row marked N/A with rationale | Omit category entirely | Prefer N/A row with rationale for audit traceability. |

## Examples

(Example workflow narratives are not directly extracted from accessible source text; the examples below are ASSUMPTIONS aligned with industry convention. Treat as directional only.)

- **Example A — Cryogenic vessel registration:** Vendor issues MEC-009 (Pressure Vessel Data Sheet) and MEC-014 (Mechanical Calculation Package) at IFR; EPC reviews; vendor incorporates comments; REG-022 package compiled and submitted to jurisdictional authority; certificate returned; final revisions bound into PRQ-016 prior to shipment. ASSUMPTION.
- **Example B — PSV cryogenic relief:** PRO-014 (Relief and Flare Design Basis) and PRO-015 (PSV Sizing) iterate against the DBM-Deepcut cryogenic flare row; PRO-016 (Valve Data Sheets) finalized only after sizing accepted; PSV procurement evidence (MTR, FAT) flows into the MRB. ASSUMPTION.
- **Example C — I&C interface alignment:** CTL-026 Package Vendor Interface Specification and CTL-006 DCS I/O List are reviewed against the DEL-053-02 interface facts (carried as artifacts in the EPC Package Datasheet); discrepancies are surfaced as Conflict Table items, not silently reconciled. ASSUMPTION.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CT-053-05-001 | Source-text level requirements for the Vendor Engineering Deliverables table are not directly parsed; ARTIFACT_REGISTER rows are used as the source-derived enumeration. | `_Sources/26020-Package_Requirements.docx` package heading 8 | `ARTIFACT_REGISTER.csv` DEL-053-05 rows (Gate 7 accepted snapshot) | Specification R-1, R-3; Datasheet Construction tables | PROPOSAL: Treat the Gate 7 ARTIFACT_REGISTER row set as the binding source-derived enumeration until the source-text slice is parsed/copied locally. | TBD |
| CT-053-05-002 | Objective associations (OBJ-001..010) for DEL-053-05 are derived via package-grouping heuristic from PROJECT_DECOMP rather than a confirmed objective-to-deliverable map. | `_CONTEXT.md` "Supports Objectives" | `OBJECTIVE_DELIVERABLE_MAP.csv` (mapping at package granularity) | Datasheet Identification; Specification Scope | PROPOSAL: Keep listing as ASSUMPTION per skill default until objective-to-deliverable mapping is confirmed at deliverable ID granularity. | TBD |
| CT-053-05-003 | Some categories in ARTIFACT_REGISTER (e.g., Electrical, Structural, Civil) may exceed actual vendor scope for a cryogenic flare KO drum skid; the register may need to mark some rows N/A. | `ARTIFACT_REGISTER.csv` DEL-053-05 categories | DEL-053-01 Scope of Work (defines the EPC/Vendor cut) | Specification R-3; Datasheet Construction categories 7, 9 | PROPOSAL: Resolve by reading DEL-053-01 once finalized and marking inapplicable rows N/A with rationale. | TBD |
