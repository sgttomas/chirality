# Datasheet: DEL-01-01 Governance Alignment, Human Authority, and Project Truth

## Identification

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-01 |
| PackageName | Product Governance and Reliance Boundaries |
| DeliverableID | DEL-01-01 |
| DeliverableName | Governance Alignment, Human Authority, and Project Truth |
| ResponsibleParty | TBD |
| Type | DOC_UPDATE |
| ContextEnvelope | M |
| CurrentLifecycleStateAtDraft | INITIALIZED |

## Attributes

| Attribute | Source-grounded value |
|---|---|
| Deliverable purpose | Keep `docs/PRD.md`, `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/PLAN.md`, and the active decomposition mutually consistent while preserving human authority, filesystem project truth, accepted git history, and runtime-audit boundaries. |
| Package scope | Product intent, invariants, professional boundary, reliance-boundary ownership, and out-of-scope discipline. |
| Inclusion criteria | Governance docs, acceptance checks, product identity, and scope boundaries. |
| Exclusions | Runtime implementation details except as required for boundary enforcement. |
| Covered scope items | SOW-074; SOW-075. |
| Supported objective | OBJ-009. |
| Anticipated artifacts | Governance consistency notes; human-authority checklist; project-truth checklist; doc diff checklist; acceptance checklist. |
| Source warning | PRD reference hash is a known mismatch and is treated as a warning, not a blocker, per dispatch instruction. |

## Conditions

| Condition | Value |
|---|---|
| Human authority condition | Only humans may author binding approval records, approve issue/release actions, select governing standards, accept residual risk, adjudicate judgment conflicts, and decide whether work may be relied upon. |
| Project truth condition | Gate-relevant project state must be represented in versioned project files under the working root and accepted git history. Hidden app state, chats, SDK transcripts, runtime logs, model context, caches, API keys, and provider transcripts are not project truth unless imported through a governed process. |
| Runtime audit condition | Runtime events explain work and support replay, but they do not approve deliverables, issue work, prove code compliance, or substitute for accepted project files and human approval records. |
| Reliance-boundary condition | Product-critical boundaries must be documented, implemented, and tested in Chirality terms; prompt text or opaque SDK defaults alone are insufficient for P0 boundaries. |
| Lifecycle condition | `_STATUS.md` is the canonical lifecycle file. Current deliverable state is `INITIALIZED`; later lifecycle transitions remain governed by SPEC and human-gate rules where applicable. |
| Dependency extraction condition | Dependency extraction is out of scope for this P3 enrichment run; do not create or update dependency records in this pass. |

## Construction

| Component | Required treatment |
|---|---|
| Governance consistency notes | Compare the governing document set using the authority order in `docs/DIRECTIVE.md` and the invariant catalog in `docs/CONTRACT.md`; record conflicts rather than silently resolving them. |
| Human-authority checklist | Verify no document, UI copy, runtime event, validator, SDK behavior, agent, tool, or domain adapter claims to approve, certify, sign, seal, issue, transmit, externally validate, or make professional work reliable by itself. |
| Project-truth checklist | Verify reliance-relevant facts land in proper project files and accepted git history, not only in runtime state, chat, SDK transcripts, UI state, caches, or hidden memory. |
| Runtime-audit checklist | Verify Chirality-owned `.chirality/sessions/<sessionId>/events.jsonl` remains the canonical runtime audit mirror and that SDK transcripts remain secondary unless imported into `HarnessEvent` form. |
| Diff/acceptance checklist | Verify PRD, DIRECTIVE, CONTRACT, SPEC, TYPES, PLAN, and decomposition changes remain mutually consistent with SOW-074, SOW-075, OBJ-009, and CONTRACT invariant families owned by PKG-01. |

## References

| RefID | Source | Use in this datasheet |
|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Authority order, filesystem truth, human authority, evidence posture, reliance boundaries, professional responsibility. |
| REF-002 | `docs/CONTRACT.md` | Binding invariants for project truth, human authority, lifecycle, invention/conflict discipline, runtime boundaries, and professional boundaries. |
| REF-003 | `docs/SPEC.md` | Execution-root layout, deliverable file contract, lifecycle states, runtime audit and engine contracts. |
| REF-004 | `docs/TYPES.md` | Canonical vocabulary for project truth, runtime audit mirror, deliverables, stable IDs, and agent authority. |
| REF-005 | `docs/PLAN.md` | Roadmap acceptance principles, current R0/R1 focus, SDK-governance boundaries, out-of-scope items. |
| REF-006 | `docs/PRD.md` | Current product requirements and acceptance criteria; used with source-warning due to observed hash mismatch. |
| REF-007 | `/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md` | SOFTWARE_DECOMP no-invention, human gate, stable-ID, bounded-deliverable method context. |
| DEC-001 | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | DEL-01-01 scope, SOW-074, SOW-075, OBJ-009, package scope, and anticipated artifacts. |
