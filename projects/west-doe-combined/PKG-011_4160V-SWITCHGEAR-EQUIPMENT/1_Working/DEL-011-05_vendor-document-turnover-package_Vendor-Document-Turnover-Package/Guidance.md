# Guidance: Vendor Document Turnover Package

## Purpose

The Vendor Document Turnover Package exists to collect the Package Vendor's documentation for the 4160V switchgear equipment package and provide a controlled handoff for EPC Integrator interface/integration review. Source: DELIVERABLE_REGISTER.csv row 52; PACKAGE_REGISTER.csv row 13.

## Principles

- Keep DEL-011-05 as a single package-level vendor-document turnover deliverable. The accepted Gate 5 basis says vendor-document rows are artifacts under the turnover package, not separate deliverables.
- Preserve the Package Vendor/EPC Integrator split: the Package Vendor owns vendor documentation; the EPC Integrator reviews for facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.
- Use the accepted interface facts as review prompts, not as invented document titles. For PKG-011 these are Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports.
- Treat missing package-specific vendor-document detail as a controlled gap. ARTIFACT_REGISTER.csv row 200 states the detailed vendor-document requirements are not present in current source material for this package.

## Considerations

- The turnover package should be reviewable even before the detailed document list is resolved by carrying a clear register placeholder and explicit TBDs.
- EPC review should focus on whether vendor documents are sufficient to support accepted package interfaces and downstream facility integration.
- The package is Electrical and vendor-owned; however, the current source set does not provide detailed PKG-011 vendor document rows such as specific switchgear drawings, test reports, or manuals. Those titles require source support or human ruling.
- Because no declared upstream or downstream dependencies exist in _DEPENDENCIES.md, dependency blockers are advisory only and none are currently declared.

## Trade-offs

| Topic | Conservative handling |
|---|---|
| Detailed vendor-document list | Keep TBD rather than borrowing lists from other packages or generic switchgear practice. |
| Interface review coverage | Include accepted interface categories as review context without converting them into unsupported deliverable rows. |
| Register schema | Define only minimal control intent; leave project-specific fields TBD unless a document control source is provided. |
| Acceptance criteria | Tie acceptance to presence, status, responsibility, and interface-review traceability; keep technical criteria TBD where source detail is absent. |

## Examples

TBD. No source-supported PKG-011 vendor-document table rows were accessible for examples in this run.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-001 | The deliverable requires vendor document register/submittals/turnover records, but detailed package-specific vendor-document requirements are absent. | DELIVERABLE_REGISTER.csv row 52; _CONTEXT.md Anticipated Artifacts | ARTIFACT_REGISTER.csv row 200 states detailed vendor-document requirements are not present in current source material for this package. | Datasheet Attributes; Specification Requirements/Documentation; Procedure Steps/Records | Use Gate 7 deliverable scope as the required package container and keep detailed document line items TBD until source material or human ruling supplies them. | TBD |
