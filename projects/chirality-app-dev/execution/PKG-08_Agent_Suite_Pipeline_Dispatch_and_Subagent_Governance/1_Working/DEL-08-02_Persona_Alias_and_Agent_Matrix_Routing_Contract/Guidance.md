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
| PRD hash mismatch | Use PRD content with warning. | Dispatch explicitly says the mismatch is not a blocker. | Human should decide whether to refresh the expected hash. |

## Examples

Sourced examples:

- Selecting the `HELP` alias should resolve to canonical `HELP_HUMAN`.
- Selecting a NORMATIVE matrix cell should route to WORKBENCH with agent context.
- Selecting an OPERATIVE matrix cell should route to PIPELINE with category context.
- A missing persona should surface `PERSONA_NOT_FOUND`.

Unsupported examples remain TBD:

- Whether alias matching is case-sensitive.
- Whether unknown aliases are rejected, passed through as canonical names, or normalized through another path.
- Exact route-state/query parameter names.

## Conflict Table (for human ruling)

No direct source conflicts were identified during P1/P2 drafting. The PRD hash mismatch is a source warning and should be reviewed, but the dispatch explicitly ruled it non-blocking for this run.

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| TBD | No active conflict. | TBD | TBD | TBD | TBD | TBD |
