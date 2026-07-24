# Context: DEL-05-04 Runtime Replay, Dialogue, and Agent Transcript Projection

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-05 |
| PackageName | Session Audit, Replay, and Tool Result Records |
| DeliverableID | DEL-05-04 |
| DeliverableName | Runtime Replay, Dialogue, and Agent Transcript Projection |
| ResponsibleParty | TBD |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** Canonical session layout, `HarnessEvent`, JSONL append/replay, redaction, tool result artifacts.

**InclusionCriteria:** Runtime audit records and replay surfaces.

**Exclusions:** Tool permission semantics.

## Deliverable Scope

Reconstruct accepted turns, recorded-session transcript/replay, tool summaries,
terminal states, attribution, and evidence-conditioned Agent projections from
canonical Chirality records. A selected recorded session is a clearly labelled,
read-only replay lens: it never resumes, switches, merges with, or mutates the
mounted primary live dialogue, and it never transfers the primary dialogue's
draft, attachments, next-turn context, permissions, interruption state, or
session identity.

## Anticipated Artifacts

Replay parser; transcript reconstruction tests; selected-session read-only
replay lens; bounded/stale/malformed projection tests; exact-parentage and
primary-dialogue isolation tests

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-006, SOW-042, SOW-046 |
| SupportsObjectives | OBJ-001, OBJ-003 |
| ContextEnvelopeNotes | Replay/reporting slice over canonical records; projection is rebuildable and presentation-only. |

## SCA-APP-004 Ownership Boundary

- DEL-05-04 owns transcript/replay reconstruction and semantic runtime
  projection.
- DEL-08-05 remains the unchanged owner of canonical child-run records and
  exact parentage/return references.
- DEL-02-01 and DEL-02-02 own shell and Coordination Panel presentation.
- DEL-08-02 owns persona/agent/session routing and guarded selection.
- DEL-08-03 owns Pipeline dispatch semantics.
- DEL-05-04 does not own project plans, approvals, assignments, aliases,
  dispatch, child-record persistence, direct child messaging, or editable
  hierarchy.
- Missing, stale, bounded, malformed, conflicting, or unrecorded evidence is
  shown explicitly rather than inferred.

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
