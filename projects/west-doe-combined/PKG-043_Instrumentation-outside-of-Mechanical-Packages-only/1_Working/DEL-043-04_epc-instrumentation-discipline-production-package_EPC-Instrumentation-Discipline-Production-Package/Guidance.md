# Guidance — DEL-043-04 EPC / Instrumentation Discipline Production Package

## Purpose

This deliverable is the EPC Integrator or discipline-subcontractor production unit for the non-vendor portion of `PKG-043` (Instrumentation outside of Mechanical Packages only). It exists because the workbook records an Instrumentation package whose detailed discipline-production requirements are not fully covered by vendor-package deliverables, and a discipline production track is needed to close out the package scope (source: `DELIVERABLE_REGISTER.csv` row DEL-043-04 Description and Notes; `PACKAGE_REGISTER.csv` row PKG-043).

## Principles

- **Source-grounded over speculative.** The decomposition explicitly carries this deliverable "conservatively" because non-vendor package detail is source-limited (source: `DELIVERABLE_REGISTER.csv` row DEL-043-04 Description). Drafted content should follow the same discipline: cite sources, mark gaps TBD, refer disputes to Gate 5.
- **Plug-n-play interface inclusion.** Per Gate 6 disposition recorded against the interface rows, instrumentation field supports, power, and communications are included in each package scope as appropriate under the plug-n-play package philosophy (source: `INTERFACE_REGISTER.csv` notes).
- **Responsibility deferred, not assumed.** The responsible party is recorded as TBD pending assignment between EPC Integrator and discipline subcontractor (source: `DELIVERABLE_REGISTER.csv` row DEL-043-04 ResponsibleParty). Production work should not pre-allocate responsibility.

## Considerations

- The five recorded package-level interfaces (Process Piping, Utility Piping, Electrical Power, I&C / Control Cabling, Communications / Network) all apply to PKG-043 (source: `INTERFACE_REGISTER.csv` rows IFC-AE83B2D0FC, IFC-F41620D435, IFC-E5A8000199, IFC-4929B68CCD, IFC-35EBF9CD91). Discipline production work touches all five and should coordinate accordingly.
- The deliverable's objectives (`OBJ-001`, `OBJ-003`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-010`) are inherited at the package grouping level (ASSUMPTION: PACKAGE_HEURISTIC mapping — source: `OBJECTIVE_DELIVERABLE_MAP.csv` rows for DEL-043-04).
- DBM-Deepcut (4-25_Deepcut_DBM.md) is referenced by `PACKAGE_REGISTER.csv` SourceRef as supporting material; the relevant slice was not locally extracted during PREPARATION (source: `_REFERENCES.md`; `PACKAGE_REGISTER.csv` SourceRef). TBD: extract DBM slice before Gate 5.

## Trade-offs

- **Conservative carry vs. premature specification.** The decomposition author chose to carry this production unit conservatively rather than fabricate detailed requirements. Pulling forward speculative requirement detail would conflict with that choice and with K-PROV-1.
- **Single discipline production unit vs. multiple sub-deliverables.** The current decomposition records a single discipline production unit at this level. Sub-decomposition into multiple discipline deliverables is a Gate 5 disposition option but is not pre-judged here.

## Examples

- Interface coverage cross-walk: each of the five `INTERFACE_REGISTER.csv` rows for PKG-043 should have at least one production-package element that references it; gaps become TBD entries in the closure record.
- Source-limited requirements closure record: a tabular record listing each anticipated requirement, the source slice that supports it (or "location TBD"), and disposition (closed / Gate 5 referral / TBD).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| (none) | No source conflicts detected in accessible registers for DEL-043-04 at Pass 2. | — | — | — | — | TBD |
