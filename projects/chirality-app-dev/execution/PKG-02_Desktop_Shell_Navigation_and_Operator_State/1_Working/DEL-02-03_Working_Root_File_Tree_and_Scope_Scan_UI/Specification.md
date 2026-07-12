# Specification: DEL-02-03 Working Root File Tree and Scope Scan UI

## Scope

DEL-02-03 covers the UI slice that connects the desktop shell to working-root selection, validation feedback, bounded file-tree browsing, deliverable summaries, and scan-state feedback.

Included:

- Working-root selector integration in the desktop shell.
- Presentation of bounded file tree data for the selected working root.
- Presentation of scope scan results for deliverables and knowledge-type directories.
- Deliverable summary widgets sufficient for operator routing and read-only inspection.
- UI handling for root changes, stale scan selections, invalid roots, and scan truncation.

Excluded:

- Runtime engine internals.
- Filesystem policy enforcement internals owned by PKG-07.
- Dependency extraction; `Dependencies.csv` creation is deferred.
- Domain-engine future-scope behavior.

Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §PKG-02 and DEL-02-03; `docs/PRD.md` §§7.1, 8.1, 13.

## Requirements

| ReqID | Requirement | Source |
|---|---|---|
| DEL-02-03-REQ-001 | The UI shall expose working-root selection globally through path entry, Electron folder selection, apply, and clear controls. | `docs/PRD.md` FR-002 |
| DEL-02-03-REQ-002 | The UI shall present validation failures for non-absolute, missing, inaccessible, non-directory, or instruction-root-contained paths. | `docs/PRD.md` FR-003; `docs/SPEC.md` §1.2 |
| DEL-02-03-REQ-003 | Clearing the working root shall disable runtime actions that require `projectRoot`. | `docs/PRD.md` §7.1 |
| DEL-02-03-REQ-004 | The UI shall render a bounded file tree for the selected working root using the workspace tree API. | `docs/PRD.md` FR-004; `docs/SPEC.md` §17.2 |
| DEL-02-03-REQ-005 | File tree presentation shall account for skipped directories `.git`, `.next`, `node_modules`, `dist`, `dist-electron`, and `out`. | `docs/PRD.md` FR-004 |
| DEL-02-03-REQ-006 | File tree presentation shall indicate inaccessible directories or truncation when reported by the API. | `docs/PRD.md` FR-004 |
| DEL-02-03-REQ-007 | Scope scan UI shall present deliverables and knowledge-type directories without treating UI-local state as project truth. | `docs/SPEC.md` §17.2; `docs/CONTRACT.md` K-FS-1; `docs/TYPES.md` §8.2 |
| DEL-02-03-REQ-008 | Dynamic scope scan state shall clear invalid selections when the root changes, deliverables are removed, knowledge markers are disabled, or knowledge targets become stale. | `docs/PRD.md` FR-013 |
| DEL-02-03-REQ-009 | Deliverable summary widgets shall support routing to PIPELINE `TASK*` with a deliverable preselected when deliverables are present. | `docs/PRD.md` §7.2 |
| DEL-02-03-REQ-010 | The UI shall consume status and dependency contract snapshots read-only where applicable; transition controls belong only where supported by the active workflow. | `docs/PRD.md` FR-010 |
| DEL-02-03-REQ-011 | Scan and workspace errors surfaced by the UI shall preserve typed-error information where available. | `docs/PRD.md` NFR-009 |
| DEL-02-03-REQ-012 | File and scope scans shall avoid runaway traversal by respecting bounded depth/count behavior exposed by the runtime. | `docs/PRD.md` NFR-012 |
| DEL-02-03-REQ-013 | Stable deliverable IDs, not folder labels alone, shall drive deliverable identity in summary widgets and route targets. | `docs/CONTRACT.md` K-ID-1, K-PATH-1; `docs/TYPES.md` §1.2 |
| DEL-02-03-REQ-014 | ASSUMPTION: The UI should not expose dependency extraction as part of this deliverable; dependency extraction remains a later `TASK + dependency-extract` step. | `_DEPENDENCIES.md`; dispatch instruction |

## Standards

| Standard / Authority | Applicability | Source |
|---|---|---|
| Working-root contract | Governs selected root validity, containment, and project-truth placement | `docs/SPEC.md` §1.2; `docs/CONTRACT.md` K-ROOT/K-FS surfaces |
| Workspace API contract | Defines the read endpoints this UI consumes | `docs/SPEC.md` §17.2 |
| PRD current product scope | Establishes working-root selection, file-tree browsing, deliverable scanning, and lifecycle/dependency contract API support as current scope | `docs/PRD.md` §6.2 |
| Unknown-value discipline | Unsupported facts remain `TBD` rather than guesses | `docs/CONTRACT.md` K-INVENT-1 |

## Verification

| ReqID | Verification Approach |
|---|---|
| DEL-02-03-REQ-001 | UI test or manual acceptance showing type path, choose folder, apply, and clear states. |
| DEL-02-03-REQ-002 | API/UI integration tests with invalid root cases and typed error display checks. |
| DEL-02-03-REQ-003 | State test confirming root-dependent actions become disabled after clear. |
| DEL-02-03-REQ-004 | API/UI integration test with representative tree data from `/api/working-root/tree`. |
| DEL-02-03-REQ-005 | Fixture tree test proving skipped directories are absent or marked according to API shape. |
| DEL-02-03-REQ-006 | Fixture or mocked response test for inaccessible/truncated directory indicators. |
| DEL-02-03-REQ-007 | Scope scan fixture test using deliverables and knowledge-type directories. |
| DEL-02-03-REQ-008 | State reset tests for root change, removed deliverable, disabled knowledge marker, and stale target cases. |
| DEL-02-03-REQ-009 | Routing test from deliverable row to PIPELINE `TASK*` preselection. |
| DEL-02-03-REQ-010 | Read-only contract snapshot rendering test; transition-control behavior TBD by owning workflow. |
| DEL-02-03-REQ-011 | Error rendering test preserving type/status/message/details where available. |
| DEL-02-03-REQ-012 | Runtime/API tests own depth/count enforcement; UI test verifies bounded-result feedback. |
| DEL-02-03-REQ-013 | Rename/path-label fixture test confirming route identity uses stable deliverable ID. |
| DEL-02-03-REQ-014 | Review check confirming no `Dependencies.csv` is created by this deliverable. |

## Documentation

Required deliverable artifacts:

- File tree panel.
- Deliverable summary widgets.
- Scope scan integration.
- UI tests or acceptance notes for selector, scan, truncation, stale-selection reset, and deliverable routing.

TBD:

- Exact component/module paths.
- Exact API response shape details for skipped-directory, truncation, and inaccessible-directory markers.
- Exact status/dependency summary widget fields; unsupported fields remain deferred rather than inferred.

## Pass 3 Disposition Notes

| ItemID | Disposition | Evidence |
|---|---|---|
| B-001 | Converted to `TBD` / already covered: implementation-level component paths, API field names, and UI copy remain unresolved. | `Specification.md` Documentation; `Guidance.md` Human-Ruling Needed; `Procedure.md` Steps. |
| X-001 | Incorporated as `TBD`: skipped-directory response-shape details were added to the API response shape unknowns. | `docs/PRD.md` FR-004; `docs/SPEC.md` §17.2. |
| X-002 | Already covered: verification binds error rendering to preserving type/status/message/details where available. | `docs/PRD.md` NFR-009; `Specification.md` Verification for DEL-02-03-REQ-011. |
| E-001 | Converted to `TBD` / deferred: exact status/dependency summary fields remain unresolved and unsupported fields must not be inferred. | `docs/PRD.md` FR-010; `docs/SPEC.md` §17.2. |

## D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-108 supersedes run-scoped extraction deferral wording: the nine-row derivative register exists; the file-tree UI still does not own dependency extraction.

## D-APP-56 launcher confirmation (2026-07-12)

R4-P29 confirms that the portal deliverable-rows launcher is within the existing DEL-02-03 REQ-009 claim. This is an ownership confirmation, not a new lifecycle or implementation claim.
