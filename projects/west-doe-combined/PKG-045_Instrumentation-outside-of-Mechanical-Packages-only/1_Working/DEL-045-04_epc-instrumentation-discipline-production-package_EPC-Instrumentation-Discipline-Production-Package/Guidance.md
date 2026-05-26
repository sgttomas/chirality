# Guidance: DEL-045-04 — EPC / Instrumentation Discipline Production Package

## Purpose

DEL-045-04 exists to define and carry the EPC/Discipline production unit that will execute the Instrumentation scope falling **outside** any vendor Mechanical Package. The decomposition recorded this package conservatively from the workbook plus DBM support; the production unit is the home for assembling the discipline-level production basis when source slices become available. (Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` DEL-045-04.)

## Principles

- **Source fidelity over convention.** Where source material is not locally accessible (as is presently the case for the bulk of detailed instrumentation requirements), prefer `TBD` over invented content. (Source: `_REFERENCES.md` Missing/Deferred References.)
- **Boundary clarity.** This package is explicitly "outside of Mechanical Packages only". Any instrumentation scope embedded inside a vendor Mechanical Package is **out of scope**. (Source: Workbook row 47; package name.)
- **No invented ownership model.** PKG-045 notes state that EPC vs subcontractor responsibility is source-dependent and no separate vendor-package ownership model is inferred. Reflect this in any assignment language. (Source: `PACKAGE_REGISTER.csv` PKG-045.)
- **Gate 5 deferral is legitimate.** The decomposition explicitly leaves detailed non-vendor package deliverable requirements open for Gate 5 disposition. Closure record should make those items visible, not paper over them. (Source: `_CONTEXT.md` Notes.)

## Considerations

- **Interface footprint is broad.** Recorded interface types include Process Piping, Utility Piping, Electrical Power, I&C / Control Cabling, and Communications / Network (`PACKAGE_REGISTER.csv` PKG-045). The production unit should plan coordination touchpoints to each.
- **Companion deliverables in PKG-045.** Coordinate the production package basis with DEL-045-01 (Scope of Work), DEL-045-02 (Package Datasheet), and DEL-045-03 (Construction Work Package). All four roll up under `SOW-0046`. (Source: `SCOPE_LEDGER.csv` SOW-0046.)
- **Exclusions caution.** Field supports, power, and comms scope are **not** carried unless package scope confirms them. Do not pull these in by default. (Source: `PACKAGE_REGISTER.csv` PKG-045 Notes.)
- **Objective mapping is heuristic.** OBJECTIVE_DELIVERABLE_MAP groups objectives by package; the deliverable-level mapping to `OBJ-002`, `OBJ-003`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-010` is recorded but should be treated as **ASSUMPTION** until confirmed.

## Trade-offs

- **Carry forward vs decompose now.** Decomposing instrumentation requirements without source slices would manufacture content; carrying forward as a placeholder preserves auditability but defers value. The decomposition chose to carry forward; this guidance endorses that until source materials are localized.
- **Single discipline unit vs subdivision.** The decomposition treats Instrumentation as a single production unit. If source review reveals materially different sub-scopes (e.g., field instruments vs control system), subdivision can be proposed at Gate 5; until then the single-unit form is retained.
- **EPC integrator vs subcontractor.** Responsible Party is `TBD`. Until source materials clarify, neither model should be hard-wired into downstream artifacts.

## Examples

- TBD — no source-grounded worked examples are available in the locally accessible reference set. Examples should be added once instrument-list or loop-count source slices are localized.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| (none recorded) | — | — | — | — | — | — |

No conflicts surfaced during the present pass; the dominant condition is source absence rather than source disagreement.
