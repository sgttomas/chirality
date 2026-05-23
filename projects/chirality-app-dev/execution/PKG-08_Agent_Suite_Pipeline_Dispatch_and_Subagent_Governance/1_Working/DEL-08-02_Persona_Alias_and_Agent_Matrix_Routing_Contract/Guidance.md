# Guidance: DEL-08-02 Persona Alias and Agent Matrix Routing Contract

## Purpose

This deliverable exists to keep Chirality's visible agent matrix, UI aliases, canonical agent instruction names, and persona routing behavior aligned. It is a small UX/UI routing slice, but it protects a larger governance boundary: users select familiar UI labels and matrix cells, while the runtime must resolve those selections into canonical instruction-root agents and governed execution surfaces.

## Principles

1. Treat `docs/TYPES.md` as the vocabulary source for aliases, matrix rows, matrix columns, and cell labels.
2. Treat `docs/PRD.md` as the product acceptance source for matrix routing, workbench context, and persona resolution, with the recorded hash mismatch warning preserved.
3. Keep alias resolution deterministic and complete for the sourced alias set.
4. Do not create friendly aliases, hidden aliases, or fallback canonical names without a governed source update.
5. Preserve the difference between WORKBENCH persona routing and PIPELINE operative category routing.
6. Keep disabled or unsupported options visible when the product requirement says they should be visible as coming soon.
7. Keep runtime behavior warning-based for unknown option keys rather than letting unknown keys silently change behavior.

## Considerations

The alias contract currently covers five explicit UI aliases:

| UI Alias | Canonical Agent |
|---|---|
| `HELP` | `HELP_HUMAN` |
| `ORCHESTRATE` | `ORCHESTRATOR` |
| `AGGREGATE` | `AGGREGATION` |
| `RECONCILING` | `RECONCILIATION` |
| `AGENTS` | `HELPS_HUMANS` |

The matrix contract currently covers these row destinations:

| Row | Destination |
|---|---|
| `NORMATIVE` | WORKBENCH |
| `OPERATIVE` | PIPELINE |
| `EVALUATIVE` | WORKBENCH |

The matrix cells from `docs/TYPES.md` use UI-facing labels and wildcard category labels. WORKBENCH routing should resolve persona-style cells to canonical agents where applicable. PIPELINE routing should preserve operative categories such as `DECOMP*`, `PREP*`, `TASK*`, and `AUDIT*` as pipeline category intent rather than forcing them through persona resolution.

## Trade-offs

| Topic | Preferred Direction | Rationale | Open Detail |
|---|---|---|---|
| Alias strictness | Use only sourced alias mappings. | Prevents hidden routing behavior and supports stable tests. | Unknown alias behavior is TBD unless code already defines it. |
| Matrix fixtures | Snapshot the canonical 3x4 vocabulary. | Protects UI navigation from drift across docs, fixtures, and implementation. | Exact fixture filenames are TBD. |
| Workbench context | Preserve agent, row, and column route context. | PRD requires active agent context and route state continuity. | Exact query-param names are TBD. |
| Pipeline distinction | Keep operative cells as pipeline categories. | TYPES and PRD route OPERATIVE to PIPELINE rather than WORKBENCH. | Exact category enum spelling in code is TBD. |
| PRD hash mismatch | Use PRD content with warning. | Dispatch explicitly says the mismatch is not a blocker. | E-001: acceptance-ready PRD-backed evidence requires either a refreshed matching REF-006 hash or explicit human acceptance of the current PRD hash. |
| Dependency picture | Treat current extracted dependency rows as available context, while preserving declared human upstream/downstream edges as TBD. | `_DEPENDENCIES.md` records the dependency-extract run and 13 ACTIVE rows. | X-001 remains open only for later accepted human edge rulings, not because `Dependencies.csv` is absent. |

## Examples

Sourced examples:

- Selecting the `HELP` alias should resolve to canonical `HELP_HUMAN`.
- Selecting a NORMATIVE matrix cell should route to WORKBENCH with agent context.
- Selecting an OPERATIVE matrix cell should route to PIPELINE with category context.
- A missing persona should surface `PERSONA_NOT_FOUND`.

Unsupported examples remain TBD:

- Whether alias matching is case-sensitive.
- B-001: whether unknown aliases are rejected, passed through as canonical names, or normalized through another governed path.
- Exact route-state/query parameter names.
- D-001: the exact selected-agent, row, and column context key names used by route state or query parameters.

## Pass 3 Disposition Guidance

| ItemID | Guidance disposition |
|---|---|
| B-001 | Do not infer unknown alias behavior from runtime unknown-option behavior; keep resolver behavior TBD until source or code selects it. |
| C-001 | Preserve the PRD hash mismatch as a source-state conflict for acceptance, even though it is non-blocking for drafting. |
| E-001 | Move PRD-backed requirements from warning-labeled draft evidence to acceptance-ready evidence only after REF-006 is refreshed to MATCH or a human records hash acceptance. |

## Conflict Table (for human ruling)

The PRD hash mismatch is a source-state conflict for acceptance readiness, even though the dispatch explicitly ruled it non-blocking for document drafting.

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-001 | REF-006 `docs/PRD.md` content is used for FR-backed requirements while `_REFERENCES.md` records a hash mismatch. | `docs/PRD.md` Sections 7.2, 7.4, 8.2, and 8.4 | `_REFERENCES.md` REF-006 expected and actual SHA values | Specification requirements and standards; Guidance principles and trade-offs | Continue warning-labeled drafting; require refreshed hash or human hash acceptance for acceptance-ready evidence. | TBD |
