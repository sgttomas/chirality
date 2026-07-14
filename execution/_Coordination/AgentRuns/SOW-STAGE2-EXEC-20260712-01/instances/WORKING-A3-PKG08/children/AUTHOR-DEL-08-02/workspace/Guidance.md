# Guidance: DEL-08-02 Persona Alias and Agent Matrix Routing Contract

## Purpose

This deliverable exists to keep Chirality's visible agent matrix, UI aliases, canonical agent instruction names, and persona routing behavior aligned. It is a small UX/UI routing slice, but it protects a larger governance boundary: users select familiar UI labels and matrix cells, while the runtime must resolve those selections into canonical instruction-root agents and governed execution surfaces.

## Principles

1. Treat `docs/TYPES.md` as the vocabulary source for aliases, matrix rows, matrix columns, and cell labels.
2. Treat `docs/PRD.md` as the product acceptance source for matrix routing, loop context, and persona resolution under the D-APP-38 authority corpus.
3. Keep alias resolution deterministic and complete for the active sourced alias set.
4. Do not create friendly aliases, hidden aliases, or fallback canonical names without a governed source update.
5. Preserve the difference between loop-persona routing and PIPELINE operative category routing.
6. Keep disabled or unsupported options visible when the product requirement says they should be visible as coming soon.
7. Keep runtime behavior warning-based for unknown option keys rather than letting unknown keys silently change behavior.

## Considerations

The active alias contract covers UI labels that resolve to Type 0/1 personas:

| UI Alias | Canonical Agent |
|---|---|
| `HELP` | `HELP_HUMAN` |
| `ORCHESTRATE` | `ORCHESTRATOR` |
| `AGENTS` | `HELPS_HUMANS` |
| `DEPENDENCIES` | `EVALUATION` |

Removed labels are deliberately not compatibility aliases:

| UI Label | Former target | Current treatment |
|---|---|---|
| `AGGREGATE` | `AGGREGATION` | Not aliased; `AGGREGATION` is a Type 2 task agent. The NORMATIVE/REVIEWING cell uses `REVIEW`. |
| `RECONCILING` | `RECONCILIATION` | Not aliased; the EVALUATIVE/REVIEWING cell uses `RESEARCH`. |

The matrix contract currently covers these row destinations:

| Row | Destination |
|---|---|
| `NORMATIVE` | Loop-persona intent |
| `OPERATIVE` | PIPELINE |
| `EVALUATIVE` | Loop-persona intent |

The matrix cells from `docs/TYPES.md` use UI-facing labels and wildcard category labels. Loop-persona routing resolves persona-style cells only to Type 0/1 personas. PIPELINE routing preserves operative categories such as `DECOMP*`, `PREP*`, `TASK*`, and `AUDIT*` as pipeline category intent rather than forcing them through persona resolution.

## Trade-offs

| Topic | Preferred Direction | Rationale | Open Detail |
|---|---|---|---|
| Alias strictness | Use only active Type 0/1 alias mappings. | Prevents hidden routing behavior and supports stable tests. | Unknown non-empty labels pass through normalized and then rely on instruction-file lookup. |
| Matrix fixtures | Snapshot the canonical 3x4 vocabulary. | Protects UI navigation from drift across docs, fixtures, and implementation. | Exact fixture filenames are TBD. |
| Loop context | Preserve agent, row, and column route context. | PRD requires active agent context and route state continuity. | Current route-state tests cover the mounted shell launch contract. |
| Pipeline distinction | Keep operative cells as pipeline categories. | TYPES and PRD route OPERATIVE to PIPELINE rather than loop-persona routing. | Category enum spelling is covered by Pipeline tests. |
| PRD source state | Use PRD content under D-APP-38. | `_REFERENCES.md` REF-006 now records MATCH under authority corpus v2. | Future authority-doc edits require corpus bump/apply. |
| Dependency picture | Treat current extracted dependency rows as available context, while preserving declared human upstream/downstream edges as TBD. | `_DEPENDENCIES.md` records the dependency-extract run and 13 ACTIVE rows. | X-001 remains open only for later accepted human edge rulings, not because `Dependencies.csv` is absent. |

## Examples

Sourced examples:

- Selecting the `HELP` alias should resolve to canonical `HELP_HUMAN`.
- Selecting a NORMATIVE matrix cell should focus the mounted loop with Type 0/1 agent context.
- Selecting an OPERATIVE matrix cell should route to PIPELINE with category context.
- A missing persona should surface `PERSONA_NOT_FOUND`.

Unsupported examples remain TBD:

- Whether future aliases should be added by a governed source update.

## Pass 3 Disposition Guidance

| ItemID | Guidance disposition |
|---|---|
| B-001 | Resolved by implementation: unknown non-empty labels pass through normalized, then `PERSONA_NOT_FOUND` is produced if no matching instruction file exists. |
| C-001 | Resolved by D-APP-38 authority corpus v2; REF-006 is MATCH in `_REFERENCES.md`. |
| E-001 | Resolved for source-state by D-APP-38; implementation proof remains separate from source proof. |

## Conflict Table

The former PRD hash mismatch is resolved for this tranche by D-APP-38 and the current `_REFERENCES.md` REF-006 MATCH state.

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-001 | Former PRD source-state conflict resolved. | `_REFERENCES.md` REF-006 | D-APP-38 authority corpus v2 | Specification requirements and standards; Guidance principles and trade-offs | Use PRD content under the current authority corpus; keep implementation proof separate. | D-APP-38 accepted current authority corpus |
