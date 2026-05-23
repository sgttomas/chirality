# Guidance: DEL-02-03 Working Root File Tree and Scope Scan UI

## Purpose

This deliverable gives the operator a trustworthy, bounded view of the selected working root and the scanned deliverable scope. It supports the desktop shell by making filesystem project truth visible enough for routing and inspection while leaving enforcement and data mutation to the runtime and workflow-specific APIs.

Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §DEL-02-03; `docs/PRD.md` §§7.1-7.2 and FR-002 through FR-004.

## Principles

- Treat the filesystem as project truth: render what the workspace APIs report; do not create hidden UI-only project truth. Source: `docs/CONTRACT.md` K-FS-1; `docs/PRD.md` §5.
- Preserve stable identity: deliverable summaries and routing should key on deliverable IDs, not mutable labels or paths alone. Source: `docs/CONTRACT.md` K-ID-1, K-PATH-1.
- Keep enforcement in the runtime: the UI should surface validation, containment, and scan-limit outcomes, while PKG-07/runtime slices own the underlying filesystem policy. Source: `_CONTEXT.md`; `docs/SPEC.md` §1.2; decomposition SOW-002 note.
- Prefer visible boundedness over silent omission: skipped directories, inaccessible nodes, and truncated scans should be visible enough for operator judgment when the API reports them. Source: `docs/PRD.md` FR-004, NFR-012.
- Reset stale operator choices: root and scan changes must clear invalid selections rather than carrying stale scope into TASK dispatch. Source: `docs/PRD.md` FR-013.
- Keep unsupported facts as `TBD`: exact component paths, response field names, and UI copy require source or implementation confirmation. Source: `docs/CONTRACT.md` K-INVENT-1.

## Considerations

- Working-root validation is a shared boundary. DEL-02-03 should integrate with validation feedback, but the security-control implementation is attributed to DEL-07-01 by the decomposition SOW ledger.
- Scope scan results bridge PKG-02 and PKG-07. The UI is responsible for presentation and selection behavior; deterministic filesystem scanning and contract data belong to runtime/filesystem deliverables.
- Deliverable summaries may need to show `_STATUS.md` and dependency snapshot information, but dependency extraction is explicitly deferred for this run.
- The PRD source has a recorded hash mismatch. Use PRD requirements as warned local source material for this run; do not treat the mismatch as resolved.
- The dispatch path named `PKG-02_Desktop_UI_and_Local_Experience`, but the accessible scaffolded folder is `PKG-02_Desktop_Shell_Navigation_and_Operator_State`. Stable IDs match; package folder-name mismatch needs human confirmation.

## Trade-offs

| Trade-off | Guidance | Source |
|---|---|---|
| Dense scan UI vs. operator clarity | Favor a dense but readable operational panel; avoid hiding truncation or invalid-selection states behind decorative UI. | `docs/PRD.md` FR-006, FR-013 |
| UI convenience state vs. project truth | Local UI state can remember view preferences, but project truth remains in working-root files and accepted git history. | `docs/DIRECTIVE.md` §2; `docs/CONTRACT.md` K-FS-1 |
| Presentation ownership vs. runtime ownership | DEL-02-03 should not duplicate root validation, scan traversal, dependency parsing, or lifecycle transition logic; it should consume and represent API results. | `_CONTEXT.md`; `docs/SPEC.md` §17.2 |
| Deliverable display by path vs. ID | Use paths for navigation context, but use stable IDs for identity and dispatch preselection. | `docs/CONTRACT.md` K-ID-1, K-PATH-1 |

## Examples

| Scenario | Expected UI behavior | Source |
|---|---|---|
| User clears the working root | Root-dependent runtime actions become disabled and stale scope selections clear. | `docs/PRD.md` §7.1, FR-013 |
| Tree API reports skipped folders | The file tree omits or marks skipped folders according to API output; skipped set includes `.git`, `.next`, `node_modules`, `dist`, `dist-electron`, and `out`. | `docs/PRD.md` FR-004 |
| Scope scan no longer contains selected deliverable | The prior selection is cleared rather than dispatched. | `docs/PRD.md` FR-013 |
| Deliverables are present | A deliverable row can route to PIPELINE `TASK*` with that deliverable preselected. | `docs/PRD.md` §7.2 |

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| DEL-02-03-CONFLICT-001 | Dispatch path uses stale package folder label `PKG-02_Desktop_UI_and_Local_Experience`; scaffolded folder uses `PKG-02_Desktop_Shell_Navigation_and_Operator_State`. | Dispatch brief `DeliverablePath / ScopePath` | `_CONTEXT.md`; `docs/CONTRACT.md` K-ID-1/K-PATH-1; decomposition PKG-02 | Datasheet Identification; run record; final report | Treat stable IDs `PKG-02` and `DEL-02-03` plus accessible scaffold as controlling for this run. | TBD |
| DEL-02-03-CONFLICT-002 | PRD hash mismatch exists for REF-006. | `_REFERENCES.md` expected/actual hash row for REF-006 | Dispatch instruction says treat mismatch as source warning, not blocker | All PRD-derived requirements | Proceed with warned PRD source for P1/P2 drafting; leave hash acceptance unresolved. | TBD |

## Human-Ruling Needed

- Confirm whether the package-folder label mismatch should be normalized, renamed, or left as a path-history artifact.
- Resolve or explicitly accept the PRD hash mismatch for future closure.
- Confirm exact UI component/module paths and API response field names before implementation-level acceptance.
