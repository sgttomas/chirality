# Specification: DEL-07-06 Reference Hash and Snapshot Conventions

## Scope

This deliverable specifies documentation conventions for reference hash handling, snapshot immutability, deterministic script/tool continuity, and CHANGE/SHA approval evidence in PKG-07.

In scope:

- Preserve reference hash behavior and approved bypass conventions for deliverable-local references.
- Preserve snapshot conventions for timestamped immutable folders and optional `_LATEST.md` pointers.
- Preserve CHANGE/publication SHA checks and human-only approval boundaries.
- Preserve notes that deterministic project tools/scripts remain indexed and locally executable when present.

Out of scope:

- Reintroducing retired execution-root validator, dependency graph generator, deliverable lock, unified pipeline run record persistence, or automated staleness propagation.
- Implementing the status transition API, dependency linter, or tool registry itself except as referenced conventions.
- Claiming automated professional approval, external validation, or human-gate authority.

Sources: `_CONTEXT.md`; `docs/PLAN.md` Section 9; `docs/PRD.md` Sections 6.4 and 8.10 with REF-006 hash warning; decomposition DEL-07-06 row.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| DEL-07-06-REQ-001 | Documentation for this deliverable MUST identify SOW-032, SOW-033, and SOW-034 as its covered scope items. | `_CONTEXT.md` Traceability; decomposition DEL-07-06 row |
| DEL-07-06-REQ-002 | Reference-hash convention notes MUST keep `_REFERENCES.md` as the deliverable-local source reference and hash-note surface. | `docs/SPEC.md` Sections 3.1 and 5.3 |
| DEL-07-06-REQ-003 | Out-of-folder references SHOULD include content hashes when tooling is available. | `docs/SPEC.md` Section 5.3 |
| DEL-07-06-REQ-004 | Hash bypasses MUST require human approval and durable bypass records. | `docs/SPEC.md` Section 5.3 |
| DEL-07-06-REQ-005 | `HASH_VERIFICATION_BYPASS.jsonl` MAY be used as the deliverable-local durable bypass record. | `docs/SPEC.md` Section 3.1 |
| DEL-07-06-REQ-006 | Snapshot-producing workflows SHOULD write timestamped immutable folders. | `docs/SPEC.md` Section 2; `docs/CONTRACT.md` K-SNAP-1 |
| DEL-07-06-REQ-007 | Snapshot-producing workflows MAY update mutable `_LATEST.md` pointers, but prior accepted snapshots MUST NOT be overwritten. | `docs/SPEC.md` Section 2; `docs/CONTRACT.md` K-SNAP-1; `docs/PRD.md` FR-062 with REF-006 hash warning |
| DEL-07-06-REQ-008 | CHANGE/publication conventions MUST require explicit approval tokens and SHA checks. | `docs/PRD.md` FR-063 with REF-006 hash warning; decomposition SOW-034 |
| DEL-07-06-REQ-009 | Human approvals MUST bind to specific content evidence, normally a git SHA or equivalent immutable evidence. | `docs/DIRECTIVE.md` Section 2.4; `docs/CONTRACT.md` K-AUTH-2 |
| DEL-07-06-REQ-010 | Content changed after approval MUST be treated as no longer approved until reviewed again. | `docs/DIRECTIVE.md` Section 2.4; `docs/CONTRACT.md` K-AUTH-2 |
| DEL-07-06-REQ-011 | Human-gate lifecycle transitions to `CHECKING` or `ISSUED` MUST require approval SHA evidence. | `docs/SPEC.md` Section 4.3; `docs/CONTRACT.md` K-STATUS-2 |
| DEL-07-06-REQ-012 | Accepted reference hash tooling and dependency-linter tooling MUST remain available without reintroducing retired hardening scope. | `docs/CONTRACT.md` K-REF-1; `docs/PLAN.md` Section 9 |
| DEL-07-06-REQ-013 | Deterministic project tools and scripts SHOULD remain indexed and locally executable when present. | `docs/PRD.md` FR-061 with REF-006 hash warning; decomposition SOW-032 |
| DEL-07-06-REQ-014 | PRD-derived requirements MUST carry the REF-006 source-state warning until `docs/PRD.md` hash state is reconciled or accepted. | `_REFERENCES.md` REF-006; task brief |
| DEL-07-06-REQ-015 | The deliverable MUST NOT state or imply that runtime events, tools, validators, SDKs, or agents approve, sign, seal, issue, certify, or externally validate work. | `docs/DIRECTIVE.md` Sections 2.3-2.4; `docs/CONTRACT.md` K-AUTH-1 and K-BIND-1 |
| DEL-07-06-REQ-016 | Exact deterministic tool/script registry membership MUST remain `TBD` unless verified by the owning implementation slice or an accepted registry source. | `docs/PRD.md` FR-061 with REF-006 hash warning; `docs/PRD.md` KG-013 with REF-006 hash warning; `docs/CONTRACT.md` K-INVENT-1 |

## Standards

| Standard / Contract | Applicability | Source |
|---|---|---|
| Lifecycle file contract | Approval SHA handling and forward-only status conventions referenced by CHANGE/SHA checklist. | `docs/SPEC.md` Section 4 |
| Deliverable folder layout | `_REFERENCES.md`, document kit, optional `HASH_VERIFICATION_BYPASS.jsonl`, and disabled `_MEMORY.md` expectations. | `docs/SPEC.md` Section 3.1; `docs/PRD.md` Section 10.8 with REF-006 hash warning |
| Filesystem project truth | Project state and approvals must land in versioned project files and accepted git history, not hidden memory or runtime logs alone. | `docs/DIRECTIVE.md` Sections 2.1-2.3; `docs/TYPES.md` Section 1 |
| Snapshot invariant | Immutable timestamped folders and mutable pointer convention. | `docs/CONTRACT.md` K-SNAP-1 |
| Reference-tool invariant | Reference hash tooling continuity without retired scope reactivation. | `docs/CONTRACT.md` K-REF-1 |

## Verification

| Requirement(s) | Verification Approach |
|---|---|
| REQ-001 | Traceability review confirms SOW/objective rows match `_CONTEXT.md` and decomposition DEL-07-06. |
| REQ-002 through REQ-005 | Documentation review confirms `_REFERENCES.md`, content hash, human approval, and `HASH_VERIFICATION_BYPASS.jsonl` conventions are present without inventing unaccepted bypass fields. |
| REQ-006 through REQ-007 | Snapshot/runbook review confirms timestamped immutable snapshot folders, optional `_LATEST.md`, and non-overwrite wording. |
| REQ-008 through REQ-011 | CHANGE/SHA checklist review confirms approval token/SHA evidence, HEAD/content evidence recheck, and human-gate SHA requirements. |
| REQ-012 through REQ-013 | Scope review confirms tool/script continuity is documented while exact registry membership remains `TBD` unless separately verified. |
| REQ-014 | Review confirms PRD-derived statements visibly carry the REF-006 hash warning. |
| REQ-015 | Professional-boundary review confirms no automated approval, issue, certification, external validation, or reliance claim is introduced. |
| REQ-016 | Registry review confirms exact tool/script membership is not asserted without accepted registry evidence. |

## Pass 3 Disposition Notes

| Item ID | Disposition | Evidence |
|---|---|---|
| B-002 | Converted to explicit `TBD` control by REQ-016; exact registry membership awaits owning implementation evidence. | Requirements and Verification tables |
| C-001 | Already covered and retained; REQ-014 and its verification row require visible REF-006 warning language for PRD-derived statements. | Requirements and Verification tables |

## Documentation

Required outputs or records for this deliverable:

- Snapshot/runbook notes covering immutable timestamped folders and `_LATEST.md` pointer behavior.
- Hash bypass convention covering human approval, durable bypass records, and `HASH_VERIFICATION_BYPASS.jsonl`.
- CHANGE/SHA checklist covering candidate SHA/action list, approval evidence, and HEAD/content recheck before approved actions.
- Source-state note carrying the `docs/PRD.md` `HASH_MISMATCH` warning.
- Open-item note for exact deterministic tool/script registry membership if not verified by the owning implementation slice.
