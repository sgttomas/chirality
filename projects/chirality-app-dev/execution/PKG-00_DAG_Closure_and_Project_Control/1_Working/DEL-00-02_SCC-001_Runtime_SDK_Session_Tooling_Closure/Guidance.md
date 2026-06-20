# Guidance: DEL-00-02 SCC-001 Runtime SDK Session Tooling Closure

## Purpose

DEL-00-02 exists to keep SCC-001 closure work visible as a governed PKG-00 control deliverable while preserving the boundary between control-plane reconciliation and product dependency data. The current accepted DepClosure evidence says the strict graph is acyclic for dependency-closure discovery: `CLOSURE_SCC_SAFE_MOVES_001_2026-06-16_0325Z` reports strict `scc_count = 0`, bidirectional pair count `0`, and schema-invalid register count `0`.

Sources: `_CONTEXT.md` (Deliverable Scope), `README.md` (Purpose, Boundary), `DAG_CLOSURE_CONTROL.md` (Control Status, Current Queue), `Dependency_Closure_Report.md` (Verdict, Ruling).

## Principles

- Treat the DepClosure snapshot as evidence of current graph state, not as authority to mutate rows by itself.
- Keep DEL-00-02 outside product dependency graph discovery.
- Preserve source-grounding: any row decision must cite the owning product dependency row and the evidence that justifies the ruling.
- Use existing dependency schema semantics only.
- Treat earlier unresolved edge decisions as historical unless a future dependency change introduces a new SCC or reopens a specific row under a governed workflow.

Sources: `DAG_CLOSURE_CONTROL.md` (Workflow), `SCC_Triage_Workbook.csv` (RecommendedAction, DoNotDo), `_DEPENDENCIES.md` (Boundary).

## Considerations

- The current accepted snapshot contains no non-trivial SCC membership; `Evidence/scc_summary.csv` has only the header row.
- `Dependency_Closure_Report.md` records active strict deliverable execution edges `97`, strict SCC count `0`, and bidirectional pair count `0`.
- `Closure_Acceptance_Audit.md` accepts the safe-moves snapshot for dependency-closure discovery and independently reran the analyzer with matching `scc_count = 0` evidence.
- Earlier triage files remain useful as evidence history, but they are not the current graph-state authority.

Sources: `Evidence/scc_summary.csv`, `Evidence/bidirectional_pairs.csv`, `Dependency_Closure_Report.md` (Evidence Summary, Ruling), `SCC_Triage_Workbook.csv`.

## Trade-offs

| Topic | Preferred Direction | Reason |
|---|---|---|
| Fast graph closure vs. evidence fidelity | Prefer evidence fidelity. | PKG-00 non-goals forbid inventing or deleting dependency edges merely to force DAG closure. |
| Control deliverable dependencies vs. product dependencies | Keep control dependencies unregistered in DEL-00-02. | Adding `Dependencies.csv` would promote the control deliverable into analyzer discovery. |
| Immediate mutation vs. ruling workbook | Produce the ruling workbook first. | The accepted workflow requires inspecting source-grounded rows before mutation. |
| Reporting dependency-closure status | Use the accepted safe-moves snapshot and state its boundary. | Current DepClosure evidence is acyclic for discovery, but does not create lifecycle issuance or release/professional approval. |

## Examples

- If a bidirectional pair represents duplicate reciprocal interface evidence, the ruling workbook may propose retiring or satisfying one side only after the owning row and source evidence support that decision.
- If a pair represents true hard sequencing in both directions, the ruling should remain `CONFLICT` or `TBD` until a human or RECONCILIATION resolves the model.
- If evidence shows a dependency is co-development-only and not a strict execution blocker, the ruling must still use existing schema fields and cite the source for that interpretation.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONFLICT-DEL-00-02-001 | `DAG_CLOSURE_CONTROL.md` current queue labels DEL-00-02 as `SEMANTIC_READY`, but `_STATUS.md` was reset to `OPEN` before TASK regeneration because the prior semantic-ready state was provisional. | `DAG_CLOSURE_CONTROL.md` (Current Queue) | `_STATUS.md` (History) | Datasheet Identification; status handoff | Treat `_STATUS.md` as current lifecycle authority: P1/P2 evidence restored `INITIALIZED`, and successful Pass 3 may advance document-kit state to `SEMANTIC_READY`. | TBD |
| CONFLICT-DEL-00-02-002 | After Pass 3, `_STATUS.md` may be advanced to `SEMANTIC_READY`, but the owner for accepting SCC-001 rulings and the source location for existing dependency schema actions remain unresolved. | `_STATUS.md` (Current State after Pass 3) | `Datasheet.md` (ResponsibleParty); `Specification.md` (Standards) | Handoff state; future SCC-001 ruling workflow | Treat `SEMANTIC_READY` as document-kit readiness only; row rulings remain TBD until the owner and schema-action authority are resolved. | TBD |

## Pass 3 Disposition

| ItemID | Disposition | Evidence |
|---|---|---|
| C-001 | Surfaced as conflict. | Conflict table now distinguishes document-kit lifecycle readiness from unresolved ruling authority, using `_STATUS.md`, `DAG_CLOSURE_CONTROL.md`, Datasheet Identification, and Specification Standards. |
| E-002 | Incorporated. | Considerations now state that triage categories must be normalized into existing dependency-schema actions or left `TBD` / `NEEDS_HUMAN_RULING`; supported by `SCC_Triage_Workbook.csv`, `SCC_Triage_Notes.md`, and Specification requirements. |

## References

- `_CONTEXT.md`
- `_DEPENDENCIES.md`
- `README.md`
- `DAG_CLOSURE_CONTROL.md`
- `Dependency_Closure_Report.md`
- `SCC_Triage_Notes.md`
- `SCC_Triage_Workbook.csv`
- `Evidence/scc_summary.csv`
- `Evidence/bidirectional_pairs.csv`
