# Datasheet: DEL-02-03 Working Root File Tree and Scope Scan UI

## Identification

| Field | Value | Source |
|---|---|---|
| DecompositionVariant | SOFTWARE_DECOMP | `_CONTEXT.md` |
| DecompositionRevision | v3.2 | `_CONTEXT.md` |
| PackageID | PKG-02 | `_CONTEXT.md` |
| PackageName | Desktop Shell, Navigation, and Operator State | `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §PKG-02 |
| DeliverableID | DEL-02-03 | `_CONTEXT.md` |
| DeliverableName | Working Root File Tree and Scope Scan UI | `_CONTEXT.md` |
| ResponsibleParty | TBD | `_CONTEXT.md` |
| Type | UX_UI_SLICE | `_CONTEXT.md` |
| ContextEnvelope | M | `_CONTEXT.md` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary UI responsibility | Working-root selector integration, bounded file tree display, deliverable summaries, and scan-state feedback | `_CONTEXT.md`; decomposition row for DEL-02-03 |
| Covered scope items | SOW-002, SOW-003 | `_CONTEXT.md`; decomposition SOW ledger |
| Supported objectives | OBJ-001, OBJ-006 | `_CONTEXT.md`; decomposition row for DEL-02-03 |
| Anticipated artifacts | File tree panel; deliverable summary widgets; scope scan integration | `_CONTEXT.md`; decomposition row for DEL-02-03 |
| Workspace APIs surfaced by this UI | `/api/working-root/validate`, `/api/working-root/tree`, `/api/working-root/scope`, `/api/project/deliverables` | `docs/SPEC.md` §17.2; `docs/PRD.md` §13 |
| Scope mode vocabulary consumed by scan UI | `DELIVERABLES`, `KNOWLEDGE_TYPES` | `docs/TYPES.md` §8.2 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Working root validity | Must be an absolute existing directory, readable and writable by the app, and not inside the instruction root | `docs/SPEC.md` §1.2; `docs/PRD.md` FR-003 |
| File tree traversal | Must be bounded; tree API skips `.git`, `.next`, `node_modules`, `dist`, `dist-electron`, and `out`; inaccessible directories mark truncation | `docs/PRD.md` FR-004 |
| Dynamic selection behavior | Root changes, removed deliverables, disabled knowledge markers, and stale knowledge targets clear invalid selection state | `docs/PRD.md` FR-013 |
| Scan runaway protection | File scans enforce depth/count limits | `docs/PRD.md` NFR-012 |
| Authority boundary | UI consumes workspace APIs but remains presentation-focused | `_CONTEXT.md`; decomposition row for DEL-02-03 |
| Source warning | PRD expected hash differs from observed hash; content using PRD is accepted for this run only as a warned source | `_REFERENCES.md`; dispatch instruction |

## Construction

| Component | Expected construction detail | Source |
|---|---|---|
| Working-root selector integration | Allow path entry, Electron folder selection, apply, and clear actions; clearing the root disables runtime actions that require `projectRoot` | `docs/PRD.md` §7.1 and FR-002 |
| File tree panel | Render selected working root through bounded tree API results, including skipped and inaccessible/truncated directory feedback | `docs/PRD.md` FR-004; `docs/SPEC.md` §17.2 |
| Scope scan integration | Consume scope scan results for deliverables and knowledge-type directories without inventing missing project truth | `docs/SPEC.md` §17.2; `docs/TYPES.md` §8.2 |
| Deliverable summary widgets | Present deliverable identity, status/dependency snapshots where available, and routeable deliverable rows for TASK workflows | `docs/PRD.md` §7.2; `docs/PRD.md` FR-010, FR-012 |
| Error feedback | Surface typed validation and scan errors in the UI; exact error copy is TBD | `docs/PRD.md` FR-003, NFR-009 |

## References

| RefID | Source | SectionRef | Use |
|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | §§2, 5, 6 | Working-root truth and instruction-root separation context |
| REF-002 | `docs/CONTRACT.md` | K-HIER-1, K-ID-1, K-PATH-1, K-FS-1, K-INVENT-1 | Governance invariants for identity, path, and unknowns |
| REF-003 | `docs/SPEC.md` | §§1.2, 3.1, 17.2 | Working-root rules, deliverable files, workspace APIs |
| REF-004 | `docs/TYPES.md` | §§1.1-1.2, 8.2 | Package/deliverable and task-scope vocabulary |
| REF-006 | `docs/PRD.md` | §§7.1-7.2, 8.1, 13, 11.2 | User journeys, functional requirements, endpoint targets, scan limits |
| DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | PKG-02 row; DEL-02-03 row; SOW ledger | Deliverable identity and decomposition scope |
