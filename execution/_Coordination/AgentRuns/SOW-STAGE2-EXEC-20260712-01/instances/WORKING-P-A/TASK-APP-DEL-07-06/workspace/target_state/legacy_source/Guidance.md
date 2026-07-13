# Guidance: DEL-07-06 Reference Hash and Snapshot Conventions

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Purpose

This deliverable preserves the conventions that let filesystem project truth stay reviewable: reference hashes make source state explicit, snapshots preserve accepted point-in-time outputs, and approval SHA checks bind human decisions to concrete content evidence. The work is intentionally documentary and continuity-focused, not an implementation expansion.

Sources: `_CONTEXT.md`; decomposition DEL-07-06; `docs/DIRECTIVE.md` Sections 2.1-2.4; `docs/CONTRACT.md` K-SNAP-1 and K-REF-1.

## Principles

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

## Considerations

| Topic | Guidance | Source |
|---|---|---|
| PRD source warning | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` REF-006; task brief — reconciled under D-APP-38 |
| Tool/script registry | State that deterministic tools/scripts remain indexed and locally executable when present, but keep exact registry membership `TBD` unless verified by the owning implementation slice. | `docs/PRD.md` FR-061 with REF-006 hash warning; decomposition SOW-032 |
| Retired scope | Do not turn reference hashes or snapshot notes into commitments for retired execution-root validator, graph generator, deliverable lock, unified pipeline run records, or staleness propagation. | `docs/PLAN.md` Section 9; `docs/PRD.md` KG-012 with REF-006 hash warning |
| Human gate language | Use approval, issue, sign, seal, certify, and validate only for human-controlled processes; do not attribute those actions to agents or tools. | `docs/DIRECTIVE.md` Section 2.4; `docs/CONTRACT.md` K-AUTH-1 |
| Pointers | `_LATEST.md` is mutable convenience metadata; the timestamped snapshot folder is the durable point-in-time artifact. | `docs/SPEC.md` Section 2; `docs/CONTRACT.md` K-SNAP-1 |

## Trade-offs

| Choice | Benefit | Cost / Risk |
|---|---|---|
| Use warning-qualified PRD text where corroborated | Keeps the draft aligned with active vNext direction. | Requires later source-hash reconciliation before final acceptance. |
| Keep tool registry membership `TBD` | Avoids inventing exact current script inventory from narrative sources. | Leaves implementation owner to confirm registry paths and tests. |
| Allow mutable `_LATEST.md` pointers | Gives operators a convenient current pointer. | Review must distinguish the pointer from immutable snapshot evidence. |
| Require durable bypass records | Makes source exceptions auditable. | Adds review overhead when a hash status: MATCH is intentionally accepted. — reconciled under D-APP-38 |

## Examples

| Situation | Recommended Handling |
|---|---|
| REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |
| A workflow reruns snapshot generation. | Create a new timestamped snapshot folder and update `_LATEST.md` if the workflow owns that pointer; do not overwrite an accepted prior snapshot. |
| CHANGE is asked to publish after edits. | Confirm approval token/SHA evidence, compare the current candidate content to the approved evidence, and recheck HEAD before approved actions. |
| A tool needs to ignore a hash status: MATCH. | Require explicit human approval and append a durable bypass record, using deliverable-local `HASH_VERIFICATION_BYPASS.jsonl` when applicable. — reconciled under D-APP-38 |

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| SOURCE-WARN-001 | `docs/PRD.md` is accessible and needed for active vNext direction, but `_REFERENCES.md` reports a hash status: MATCH. | `_REFERENCES.md` REF-006 | `docs/PRD.md` current accessible text | All PRD-cited requirements and examples | Continue using PRD as warning-qualified source per task brief; require hash reconciliation or explicit acceptance before closure. | TBD — reconciled under D-APP-38 |

## Pass 3 Disposition Notes

| Item ID | Disposition | Evidence |
|---|---|---|
| A-001 | Surfaced as conflict; SOURCE-WARN-001 remains open until hash reconciliation or explicit acceptance. | Conflict Table |
| B-001 | Surfaced as conflict; PRD-derived closure-ready statements remain warning-qualified. | Conflict Table; Considerations |
| E-001 | Surfaced as conflict; SOURCE-WARN-001 remains the active human-ruling item. | Conflict Table |
