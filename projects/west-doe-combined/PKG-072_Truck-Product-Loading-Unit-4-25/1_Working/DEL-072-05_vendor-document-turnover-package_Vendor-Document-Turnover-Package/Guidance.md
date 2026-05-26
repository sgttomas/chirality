# Guidance — Vendor Document Turnover Package (DEL-072-05)

## Purpose

The Vendor Document Turnover Package exists so the Owner / EPC Integrator can take custody of the PKG-072 Truck Product Loading Unit 4-25 with a complete, traceable, vendor-authored documentation set. It is the documentary counterpart of the physical package handover: without it, the package cannot be operated, maintained, audited, or modified safely.

Decomposition framing: this is an "Additional Gate 5 deliverable" — individual source document rows remain artifacts/evidence and are not promoted to separate deliverables (`_CONTEXT.md` Notes).

## Principles

- **Vendor authority, integrator review.** The Package Vendor authors and submits; the EPC Integrator reviews from an interface/integration standpoint. Neither party unilaterally approves a document for binding reliance (consistent with project governance).
- **Register-first.** The vendor document register is the single index of truth for what exists, at what revision, and in what disposition. Submittals without a register row are not part of turnover.
- **Source-grounded.** Where a vendor document row in the upstream workbook source identifies a required document, that row IS the evidence; the turnover package preserves it.
- **Stage discipline.** Documents flow through declared stages (e.g., preliminary, for-approval, final, as-built). The stage matters: as-built records, not preliminary ones, are what get archived at turnover.
- **Interface alignment.** Vendor documentation must cover every interface type the package presents to the facility (Process Piping; Drain/Containment; Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports; Product Loading) — gaps here are integration risks.

## Considerations

- **Binary source files.** The two primary basis documents (`26020-Package_Requirements.docx` heading 26 and `26020-Packages_Interfaces_4_export.xlsx` row 99) are not directly machine-readable in this environment. Clause-level requirements for which documents are required, in what stage, and to what acceptance criteria are TBD until an extraction is performed.
- **PKG-072 identity ambiguity.** See Conflict Table below — the package name in different registers and field positions is not identical.
- **Equipment tag ambiguity.** Per `4-25_Deepcut_DBM.md` (around line 2630, 2645) the "Truck Loading Ticket Shack 2" package equipment tag is TBD; this propagates to the vendor document register's tag column.
- **Heuristic objective association.** The objectives OBJ-001, OBJ-003 through OBJ-010 are mapped to this deliverable via package-grouping heuristic (PACKAGE_HEURISTIC mode) — recorded as ASSUMPTION pending human confirmation.

## Trade-offs

- **Granularity of register vs. effort.** A richer register (e.g., per-document linkages to SOW rows and interfaces) increases authoring effort but materially improves auditability and downstream operability. Recommendation: include the linkages.
- **Early vs. late EPC Integrator review.** Reviewing only at final stage minimizes vendor rework cycles but maximizes integration risk if an interface mismatch is discovered late. Recommendation: stage-gated review at "for-approval" minimum.
- **Treating source-row artifacts as evidence vs. promoting them to deliverables.** The decomposition explicitly chose evidence-only treatment (`_CONTEXT.md` Notes); this trade-off is settled, not re-litigated here.

## Examples

- TBD — no worked example of a comparable closed vendor document turnover package is locally accessible.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CONF-01 | PKG-072 package identity. `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv` row 562 call the parent package "Truck Product Loading Unit 4-25". `PACKAGE_REGISTER.csv` row 99 ScopeNotes describes "1 skid mounted Low Pressure Fuel Gas Package …" while its WorkbookReferenceTag is "26020-01-PT-23-001 - Condensate Truck Loading Stations". | `DELIVERABLE_REGISTER.csv` row 562; `_CONTEXT.md` Identity | `PACKAGE_REGISTER.csv` row 99 (ScopeNotes vs. PackageName vs. WorkbookReferenceTag) | Datasheet Identification, Specification Scope, Guidance Purpose | PROPOSAL: PackageName + WorkbookReferenceTag ("Truck Product Loading … / Condensate Truck Loading Stations") are authoritative; ScopeNotes prose mentioning "Low Pressure Fuel Gas Package" appears to be a register-cell content mismatch carried over from another package row. | TBD |
| CONF-02 | Package equipment tag for the Truck Loading Ticket Shack 2 referenced in DBM is TBD. | `4-25_Deepcut_DBM.md` line ~2630 (TBD in table) | `4-25_Deepcut_DBM.md` line ~2645 (explicit TBD note) | Datasheet Attributes (Package equipment tag), Specification Documentation | PROPOSAL: leave tag as TBD in register until vendor confirms tagging. | TBD |
| CONF-03 | Clause-level vendor-document requirements live in `26020-Package_Requirements.docx` heading 26 which is a binary `.docx` not locally parsed. | `_REFERENCES.md` Source Materials | (no second source) | Specification Requirements, Verification, Documentation | PROPOSAL: run a docx extraction task (or human review) and re-issue Pass 1/Pass 2 with clause-level requirements before INITIALIZED -> SEMANTIC_READY transition. | TBD |
