# Guidance: DEL-00-01 SCC-002 PKG-10 Policy Proposal Closure

## Purpose

Use this deliverable as a bounded control record for SCC-002, not as a place to mutate dependency edges. The purpose is to preserve the current DepClosure evidence, focus review on the two SCC-002 rows, and hand a source-grounded ruling path to RECONCILIATION.

Sources: `_CONTEXT.md` section `Deliverable Scope`; `README.md` sections `Purpose` and `Boundary`; `DAG_CLOSURE_CONTROL.md` section `Workflow`.

## Principles

- Prefer evidence-preserving closure over edge deletion. The triage workbook explicitly says not to waive or retire either SCC-002 row without source citation (`SCC_Triage_Workbook.csv` row `SCC-002`).
- Treat `DEP-10-03-006` as the likely true sequencing edge unless source evidence proves it is satisfied or not applicable (`SCC_Triage_Notes.md` section `SCC-002 Initial Reading`).
- Treat `DEP-10-02-004` as opposite-direction interface evidence that may need conversion, satisfaction, or retirement only if source evidence supports that action (`SCC_Triage_Workbook.csv` row `SCC-002`).
- Keep PKG-00 outside the strict product graph. Its control deliverables intentionally have no local dependency registers (`README.md` section `Boundary`; `_DEPENDENCIES.md` section `Boundary`).
- Use a new immutable DepClosure snapshot to prove closure after any accepted product-register updates (`DAG_CLOSURE_CONTROL.md` section `Acceptance Condition`).

## Considerations

The current DepClosure snapshot reports strict FULL_GRAPH as `CYCLIC`, with two remaining SCCs and SCC-002 as the smaller two-node cycle (`Dependency_Closure_Report.md` sections `Verdict` and `Remaining SCCs`; `Evidence/scc_summary.csv`). The blocker subset is already acyclic, so the remaining issue is strict graph closure rather than blocker-subset closure (`Dependency_Closure_Report.md` section `Evidence Summary`).

The two source rows differ in reading:

- `DEP-10-02-004` is an `INTERFACE` row from `DEL-10-02` to `DEL-10-03`, with `SatisfactionStatus` `TBD`, `Confidence` `MEDIUM`, and notes that it is future-boundary only.
- `DEP-10-03-006` is a `PREREQUISITE` row from `DEL-10-03` to `DEL-10-02`, with `SatisfactionStatus` `PENDING`, `Confidence` `HIGH`, and notes that it is an explicit sibling-deliverable prerequisite.

Sources: PKG-10 `Dependencies.csv` rows `DEP-10-02-004` and `DEP-10-03-006`.

## Trade-offs

| Option | Benefit | Risk | Current disposition |
|---|---|---|---|
| Preserve both rows unchanged | No unsupported mutation; preserves evidence. | SCC-002 remains cyclic. | Acceptable as an interim handoff, not closure. |
| Preserve `DEP-10-03-006` and reclassify or satisfy `DEP-10-02-004` | Matches the current triage reading if source evidence supports it. | Requires source citation and owning-register update outside this task. | Candidate for RECONCILIATION ruling. |
| Retire or waive either row without citation | Produces apparent graph relief. | Violates triage instruction and source-grounding rules. | Not allowed. |
| Add a PKG-00 dependency register | Could make the control deliverable visible to graph tooling. | Violates PKG-00 boundary and may pollute product graph discovery. | Not allowed without later human ruling. |

## Examples

- Valid ruling shape: "Preserve `DEP-10-03-006`; propose action for `DEP-10-02-004` only after citing its source row and supporting artifact evidence."
- Invalid ruling shape: "Delete the weaker row because a cycle exists." The current triage evidence forbids waiver or retirement without source citation.
- Valid closure evidence: a later DepClosure snapshot whose report shows strict FULL_GRAPH acyclic and `scc_count = 0`.

## Ruling Rationale Notes

`E-003` disposition: the current rationale is provisional and evidence-preserving. `DEP-10-03-006` is the likely true sequencing edge because the source row is a `PREREQUISITE`, `PENDING`, `HIGH` confidence row whose evidence quote names the protected path and proposal path policy as a sibling prerequisite. `DEP-10-02-004` is an `INTERFACE`, `TBD`, `MEDIUM` confidence row whose notes describe a future-boundary-only interface. This supports a RECONCILIATION review path, not a row mutation during this task.

The decision authority for product-register edits remains unresolved. `E-001` is carried as a HumanRuling item: approval may belong to the human operator, RECONCILIATION, or both, and no PKG-10 row edit should proceed until that authority is explicit.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONFLICT-DEL-00-01-001 | `DAG_CLOSURE_CONTROL.md` still labels `DEL-00-01` as `SEMANTIC_READY`, while `_STATUS.md` was reset to `OPEN` for TASK regeneration. | `DAG_CLOSURE_CONTROL.md` section `Current Queue` | `_STATUS.md` section `History` | Datasheet Identification; Procedure Records | Treat `_STATUS.md` as lifecycle authority for this run and update to `INITIALIZED` after successful P1/P2. | TBD |

`E-002` disposition: the lifecycle-state conflict remains a HumanRuling item for downstream reporting. This Pass 3 run may advance `_STATUS.md` to `SEMANTIC_READY` after successful enrichment, but it does not retroactively validate the earlier provisional `DAG_CLOSURE_CONTROL.md` queue label.
