# Source Pack: SRC-DEL-DEL-07-06-REFERENCE-HASH-AND-SNAPSHOT-CONVENTIONS

Grouping: `GROUPED_DELIVERABLE`  RepoGlob: `execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-06_Reference_Hash_and_Snapshot_Conventions/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-06_Reference_Hash_and_Snapshot_Conventions/Datasheet.md

### Datasheet: DEL-07-06 Reference Hash and Snapshot Conventions

#### Identification

| Field | Value |
|---|---|
| Package ID | PKG-07 |
| Package Name | Filesystem Execution, Lifecycle, and Dependencies |
| Deliverable ID | DEL-07-06 |
| Deliverable Name | Reference Hash and Snapshot Conventions |
| Responsible Party | TBD |
| Type | DOC_UPDATE |
| Context Envelope | S |
| Decomposition Variant | SOFTWARE_DECOMP v3.2 |

#### Attributes

| Attribute | Value | Source |
|---|---|---|
| Deliverable purpose | Preserve deterministic tools/scripts, reference hash behavior, immutable snapshots, and SHA approval conventions without reactivating retired scope. | `_CONTEXT.md` Deliverable Scope; decomposition DEL-07-06 row |
| Covered scope items | SOW-032 deterministic tools/scripts, SOW-033 immutable snapshots, SOW-034 CHANGE/publication SHA checks. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SSOW and SOW-to-deliverable rows |
| Supported objectives | OBJ-006 filesystem project truth; OBJ-009 professional boundary and reliance-boundary ownership. | `_CONTEXT.md` Traceability; decomposition Objectives |
| Anticipated artifacts | Snapshot/runbook notes; hash bypass convention; CHANGE/SHA checklist. | `_CONTEXT.md` Anticipated Artifacts; decomposition DEL-07-06 row |
| Reference hash bypass record | Deliverable folders may include `HASH_VERIFICATION_BYPASS.jsonl`; hash bypasses require human approval and durable bypass records. | `docs/SPEC.md` Sections 3.1 and 5.3 |
| Snapshot convention | Snapshot-producing workflows should write timestamped immutable folders and may update `_LATEST.md` pointers. | `docs/SPEC.md` Section 2; `docs/CONTRACT.md` K-SNAP-1; `docs/PRD.md` FR-062 with REF-006 hash warning |
| Approval evidence convention | Human approvals bind to specific content evidence, normally a git SHA; human-gate lifecycle transitions require approval SHA evidence. | `docs/DIRECTIVE.md` Section 2.4; `docs/CONTRACT.md` K-AUTH-2 and K-STATUS-2; `docs/SPEC.md` Section 4.3 |
| Reference tool continuity | Accepted reference hash tooling and dependency-linter behavior remain in scope; retired hardening scope must not be reintroduced by runtime event logging. | `docs/CONTRACT.md` K-REF-1; `docs/PLAN.md` Section 9 |

#### Conditions

| Condition | Handling | Source |
|---|---|---|
| `docs/PRD.md` source state | REF-006 is locally accessible but `_REFERENCES.md` reports `HASH_MISMATCH`; this run treats it as a source-state warning per brief. PRD-only statements remain review-aware until hash reconciliation or acceptance. | `_REFERENCES.md` REF-006; task brief |
| Unknown owner | `ResponsibleParty` remains `TBD` until assigned by a human. | `_CONTEXT.md` Source Authority |
| Retired scope boundary | Do not reactivate execution-root validator, dependency graph generator, deliverable lock, unified pipeline run records, or staleness propagation as current commitments. | `docs/PLAN.md` Section 9; `docs/PRD.md` Section 6.4 and KG-012 with REF-006 hash warning |
| Human authority | No agent, SDK, tool, runtime event, validator, or adapter can author binding approval records. | `docs/CONTRACT.md` K-AUTH-1; `docs/DIRECTIVE.md` Section 2.4 |

#### Pass 3 Disposition Notes

| Item ID | Disposition | Evidence |
|---|---|---|
| A-002 | Already covered; ownership remains `TBD` and is not assigned by this pass. | Identification table; `_CONTEXT.md` Source Authority |

#### Construction

| Component | Expected Content | Source |
|---|---|---|
| Snapshot/runbook notes | Rules for timestamped immutable snapshot folders, optional `_LATEST.md` pointer updates, non-overwrite of accepted snapshots, and source-state warnings. | `docs/SPEC.md` Section 2; `docs/CONTRACT.md` K-SNAP-1 |
| Hash bypass convention | When reference hash verification is bypassed, record human approval and durable evidence in deliverable-local `HASH_VERIFICATION_BYPASS.jsonl` where applicable. | `docs/SPEC.md` Sections 3.1 and 5.3 |
| CHANGE/SHA checklist | Checklist confirming candidate content evidence, approval token/SHA, HEAD recheck before approved actions, and continued human-only authority. | `docs/DIRECTIVE.md` Sections 2.2 and 2.4; `docs/PRD.md` FR-063 with REF-006 hash warning |
| Tool continuity notes | Notes confirming deterministic project tools/scripts remain indexed and locally executable when present. Exact registry membership is `TBD` unless verified by the owning implementation slice. | `docs/PRD.md` FR-061 with REF-006 hash warning; decomposition SOW-032 |

#### References

| RefID | Source | Sections Used | Source State |
|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Sections 2.1, 2.2, 2.4, 2.5 | MATCH |
| REF-002 | `docs/CONTRACT.md` | K-AUTH-1, K-AUTH-2, K-BIND-1, K-STATUS-1, K-STATUS-2, K-SNAP-1, K-REF-1 | MATCH |
| REF-003 | `docs/SPEC.md` | Sections 2, 3.1, 4.3, 5.3 | MATCH |
| REF-004 | `docs/TYPES.md` | Sections 1-2, 3.3 | MATCH |
| REF-005 | `docs/PLAN.md` | Section 9 | MATCH |
| REF-006 | `docs/PRD.md` | Sections 6.4, 8.10, 10.8, 15 | HASH_MISMATCH source-state warning |
| REF-007 | `AGENT_SOFTWARE_DECOMP.md` | Decomposition method context | MATCH |

## Component: execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-06_Reference_Hash_and_Snapshot_Conventions/Guidance.md

### Guidance: DEL-07-06 Reference Hash and Snapshot Conventions

#### Purpose

This deliverable preserves the conventions that let filesystem project truth stay reviewable: reference hashes make source state explicit, snapshots preserve accepted point-in-time outputs, and approval SHA checks bind human decisions to concrete content evidence. The work is intentionally documentary and continuity-focused, not an implementation expansion.

Sources: `_CONTEXT.md`; decomposition DEL-07-06; `docs/DIRECTIVE.md` Sections 2.1-2.4; `docs/CONTRACT.md` K-SNAP-1 and K-REF-1.

#### Principles

1. Evidence is stronger than plausible continuity.
   Reference hashes, durable bypass records, snapshot names, `_LATEST.md` pointers, and git SHA evidence are all project-truth aids. If an input is unknown, mark it `TBD` rather than inferring a value. Sources: `docs/DIRECTIVE.md` Section 2.5; `docs/CONTRACT.md` K-INVENT-1.

2. Snapshot means preserved state, not a mutable workspace.
   A snapshot-producing workflow should create a new timestamped folder and may move a pointer. It should not overwrite a previously accepted snapshot. Sources: `docs/SPEC.md` Section 2; `docs/CONTRACT.md` K-SNAP-1.

3. Hash bypass is exceptional and human-approved.
   A bypass should not silently downgrade source fidelity. When used, it needs human approval and a durable record, with `HASH_VERIFICATION_BYPASS.jsonl` available as the deliverable-local record surface. Source: `docs/SPEC.md` Sections 3.1 and 5.3.

4. CHANGE/SHA checks are reliance controls, not ceremonial metadata.
   Approval evidence must bind to specific content, normally a git SHA or equivalent immutable evidence. Changed content needs renewed review. Sources: `docs/DIRECTIVE.md` Section 2.4; `docs/CONTRACT.md` K-AUTH-2.

5. Runtime audit records do not approve project work.
   Runtime logs may explain what happened, but they do not substitute for accepted project-state files or human approval records. Sources: `docs/DIRECTIVE.md` Section 2.3; `docs/CONTRACT.md` K-BIND-1.

#### Considerations

| Topic | Guidance | Source |
|---|---|---|
| PRD source warning | Treat `docs/PRD.md` as accessible but warning-qualified because REF-006 is `HASH_MISMATCH`. Prefer matching CONTRACT/SPEC/DIRECTIVE/TYPES sources where available. | `_REFERENCES.md` REF-006; task brief |
| Tool/script registry | State that deterministic tools/scripts remain indexed and locally executable when present, but keep exact registry membership `TBD` unless verified by the owning implementation slice. | `docs/PRD.md` FR-061 with REF-006 hash warning; decomposition SOW-032 |
| Retired scope | Do not turn reference hashes or snapshot notes into commitments for retired execution-root validator, graph generator, deliverable lock, unified pipeline run records, or staleness propagation. | `docs/PLAN.md` Section 9; `docs/PRD.md` KG-012 with REF-006 hash warning |
| Human gate language | Use approval, issue, sign, seal, certify, and validate only for human-controlled processes; do not attribute those actions to agents or tools. | `docs/DIRECTIVE.md` Section 2.4; `docs/CONTRACT.md` K-AUTH-1 |
| Pointers | `_LATEST.md` is mutable convenience metadata; the timestamped snapshot folder is the durable point-in-time artifact. | `docs/SPEC.md` Section 2; `docs/CONTRACT.md` K-SNAP-1 |

#### Trade-offs

| Choice | Benefit | Cost / Risk |
|---|---|---|
| Use warning-qualified PRD text where corroborated | Keeps the draft aligned with active vNext direction. | Requires later source-hash reconciliation before final acceptance. |
| Keep tool registry membership `TBD` | Avoids inventing exact current script inventory from narrative sources. | Leaves implementation owner to confirm registry paths and tests. |
| Allow mutable `_LATEST.md` pointers | Gives operators a convenient current pointer. | Review must distinguish the pointer from immutable snapshot evidence. |
| Require durable bypass records | Makes source exceptions auditable. | Adds review overhead when a hash mismatch is intentionally accepted. |

#### Examples

| Situation | Recommended Handling |
|---|---|
| A source file hash differs from `_REFERENCES.md`. | Record the mismatch as a source-state warning, use the source only as instructed or corroborated, and require human/source-hash reconciliation before final acceptance. |
| A workflow reruns snapshot generation. | Create a new timestamped snapshot folder and update `_LATEST.md` if the workflow owns that pointer; do not overwrite an accepted prior snapshot. |
| CHANGE is asked to publish after edits. | Confirm approval token/SHA evidence, compare the current candidate content to the approved evidence, and recheck HEAD before approved actions. |
| A tool needs to ignore a hash mismatch. | Require explicit human approval and append a durable bypass record, using deliverable-local `HASH_VERIFICATION_BYPASS.jsonl` when applicable. |

#### Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| SOURCE-WARN-001 | `docs/PRD.md` is accessible and needed for active vNext direction, but `_REFERENCES.md` reports a hash mismatch. | `_REFERENCES.md` REF-006 | `docs/PRD.md` current accessible text | All PRD-cited requirements and examples | Continue using PRD as warning-qualified source per task brief; require hash reconciliation or explicit acceptance before closure. | TBD |

#### Pass 3 Disposition Notes

| Item ID | Disposition | Evidence |
|---|---|---|
| A-001 | Surfaced as conflict; SOURCE-WARN-001 remains open until hash reconciliation or explicit acceptance. | Conflict Table |
| B-001 | Surfaced as conflict; PRD-derived closure-ready statements remain warning-qualified. | Conflict Table; Considerations |
| E-001 | Surfaced as conflict; SOURCE-WARN-001 remains the active human-ruling item. | Conflict Table |

## Component: execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-06_Reference_Hash_and_Snapshot_Conventions/Procedure.md

### Procedure: DEL-07-06 Reference Hash and Snapshot Conventions

#### Purpose

Use this procedure to produce or review the DEL-07-06 convention notes: snapshot/runbook notes, hash bypass convention, and CHANGE/SHA checklist.

#### Prerequisites

| Prerequisite | Status / Source |
|---|---|
| Deliverable-local context, references, dependencies, and status files are present. | `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md` |
| Current lifecycle state permits drafting. | `_STATUS.md` was `OPEN` at P1/P2 start |
| Authoritative sources are locally accessible. | `_REFERENCES.md` REF-001 through REF-007; REF-006 has HASH_MISMATCH warning |
| Accepted dependency edges are available. | TBD: `_DEPENDENCIES.md` declares no accepted upstream/downstream edges yet |
| Human owner is assigned. | TBD: `_CONTEXT.md` preserves `ResponsibleParty: TBD` |

#### Steps

1. Confirm source state.
   - Read `_REFERENCES.md`.
   - Record the status of each authoritative reference.
   - Preserve the `docs/PRD.md` `HASH_MISMATCH` as a source-state warning unless a human/source-owner reconciles the hash.

2. Confirm scope boundary.
   - Use `_CONTEXT.md` and the decomposition row for DEL-07-06.
   - Confirm the deliverable covers SOW-032, SOW-033, and SOW-034.
   - Confirm the work remains a `DOC_UPDATE`, not an implementation task.

3. Draft snapshot/runbook notes.
   - State that snapshot-producing workflows should create timestamped immutable folders.
   - State that `_LATEST.md` pointers may move when the owning workflow permits.
   - State that accepted snapshots must not be overwritten.
   - Cite `docs/SPEC.md` Section 2 and `docs/CONTRACT.md` K-SNAP-1.

4. Draft the hash bypass convention.
   - State that `_REFERENCES.md` carries source references and hash notes.
   - State that out-of-folder references should include content hashes when tooling is available.
   - State that hash bypasses require human approval and durable bypass records.
   - When a concrete bypass is used, confirm the review package includes both human approval evidence and the durable bypass record before treating the bypass as accepted.
   - Identify `HASH_VERIFICATION_BYPASS.jsonl` as the deliverable-local bypass record surface where applicable.
   - Cite `docs/SPEC.md` Sections 3.1 and 5.3.

5. Draft the CHANGE/SHA checklist.
   - Confirm candidate content evidence and action list are recorded before approval.
   - Confirm human approval evidence is present and SHA-like where required.
   - Before any `CHECKING` or `ISSUED` transition, confirm approval SHA evidence exists for the exact candidate content under review.
   - Recheck HEAD/current candidate content before executing approved CHANGE/publication actions.
   - State that content changed after approval requires renewed review.
   - Cite `docs/DIRECTIVE.md` Section 2.4, `docs/CONTRACT.md` K-AUTH-2, and `docs/PRD.md` FR-063 with REF-006 hash warning.

6. Guard retired scope.
   - Confirm the convention notes do not reactivate execution-root validator, dependency graph generator, deliverable lock, unified pipeline run record persistence, or automated staleness propagation.
   - Cite `docs/PLAN.md` Section 9 and `docs/PRD.md` KG-012 with REF-006 hash warning.

7. Confirm human-authority language.
   - Remove any wording implying that an agent, SDK, tool, runtime event, validator, or adapter approves, issues, certifies, signs, seals, or externally validates work.
   - Cite `docs/DIRECTIVE.md` Sections 2.3-2.4 and `docs/CONTRACT.md` K-AUTH-1/K-BIND-1.

8. Run cross-document consistency check.
   - Confirm Datasheet attributes map to Specification requirements.
   - Confirm Specification verification rows have corresponding procedure steps.
   - Confirm Guidance source warnings match Datasheet and Specification warning language.
   - Leave unresolved values as `TBD` and list human rulings in Guidance.

#### Verification

| Check | Acceptance |
|---|---|
| Source-state warning | REF-006 `docs/PRD.md` hash mismatch is visible anywhere PRD-derived requirements or examples are used. |
| Snapshot convention | Notes include timestamped immutable folders, optional `_LATEST.md`, and non-overwrite of accepted snapshots. |
| Hash bypass convention | Notes include human approval, durable bypass record, and `HASH_VERIFICATION_BYPASS.jsonl` where applicable. |
| Hash bypass evidence | If a bypass is used, review confirms explicit human approval evidence and a durable bypass record exist before accepting the bypass. |
| CHANGE/SHA checklist | Notes include candidate evidence, approval token/SHA, approval SHA evidence before `CHECKING` or `ISSUED`, HEAD/current-content recheck, and renewed review after content changes. |
| Retired scope | No current commitment is made for retired execution-root validator, dependency graph generator, deliverable lock, unified pipeline run record persistence, or automated staleness propagation. |
| Human authority | No automated approval, signing, sealing, issue, certification, external validation, or professional reliance claim is introduced. |

#### Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` for DEL-07-06.
- `_run_records/TASK_RUN_*.md` capturing the TASK run and source-state warnings.
- Future human/source-owner record resolving or accepting the `docs/PRD.md` hash mismatch: TBD.
- Future exact deterministic tool/script registry evidence: TBD unless produced by the owning implementation slice.
- Future accepted dependency edge record source: TBD until `_DEPENDENCIES.md` or `Dependencies.csv` records accepted upstream/downstream edge availability.

#### Pass 3 Disposition Notes

| Item ID | Disposition | Evidence |
|---|---|---|
| F-001 | Converted to explicit `TBD`; dependency edge availability remains unresolved until an accepted dependency record source is present. | Prerequisites; Records |
| D-001 | Incorporated; the CHANGE/SHA checklist now requires approval SHA evidence before any `CHECKING` or `ISSUED` transition. | Steps; Verification |
| X-001 | Incorporated; bypass review now requires human approval evidence and a durable bypass record when a bypass is used. | Steps; Verification |

## Component: execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-06_Reference_Hash_and_Snapshot_Conventions/Specification.md

### Specification: DEL-07-06 Reference Hash and Snapshot Conventions

#### Scope

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

#### Requirements

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

#### Standards

| Standard / Contract | Applicability | Source |
|---|---|---|
| Lifecycle file contract | Approval SHA handling and forward-only status conventions referenced by CHANGE/SHA checklist. | `docs/SPEC.md` Section 4 |
| Deliverable folder layout | `_REFERENCES.md`, document kit, optional `HASH_VERIFICATION_BYPASS.jsonl`, and disabled `_MEMORY.md` expectations. | `docs/SPEC.md` Section 3.1; `docs/PRD.md` Section 10.8 with REF-006 hash warning |
| Filesystem project truth | Project state and approvals must land in versioned project files and accepted git history, not hidden memory or runtime logs alone. | `docs/DIRECTIVE.md` Sections 2.1-2.3; `docs/TYPES.md` Section 1 |
| Snapshot invariant | Immutable timestamped folders and mutable pointer convention. | `docs/CONTRACT.md` K-SNAP-1 |
| Reference-tool invariant | Reference hash tooling continuity without retired scope reactivation. | `docs/CONTRACT.md` K-REF-1 |

#### Verification

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

#### Pass 3 Disposition Notes

| Item ID | Disposition | Evidence |
|---|---|---|
| B-002 | Converted to explicit `TBD` control by REQ-016; exact registry membership awaits owning implementation evidence. | Requirements and Verification tables |
| C-001 | Already covered and retained; REQ-014 and its verification row require visible REF-006 warning language for PRD-derived statements. | Requirements and Verification tables |

#### Documentation

Required outputs or records for this deliverable:

- Snapshot/runbook notes covering immutable timestamped folders and `_LATEST.md` pointer behavior.
- Hash bypass convention covering human approval, durable bypass records, and `HASH_VERIFICATION_BYPASS.jsonl`.
- CHANGE/SHA checklist covering candidate SHA/action list, approval evidence, and HEAD/content recheck before approved actions.
- Source-state note carrying the `docs/PRD.md` `HASH_MISMATCH` warning.
- Open-item note for exact deterministic tool/script registry membership if not verified by the owning implementation slice.
