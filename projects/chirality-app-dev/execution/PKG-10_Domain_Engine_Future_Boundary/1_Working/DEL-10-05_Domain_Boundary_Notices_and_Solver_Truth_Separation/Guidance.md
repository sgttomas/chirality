# Guidance: DEL-10-05 Domain Boundary Notices and Solver Truth Separation

## Purpose

Use this deliverable to keep future domain-engine language clear, conservative, and reviewable. Chirality may govern interaction, proposal records, audit records, adapter policy, protected/proposal path boundaries, and human gates. It must not present itself as the domain solver, the professional approver, the code-compliance authority, or the owner of solver truth.

## Principles

1. Keep ownership explicit: the domain engine or deterministic adapter owns its domain output; Chirality owns the governed interaction record; humans own acceptance and professional reliance decisions.
2. Use boundary notices wherever domain outputs, proposed domain operations, protected artifacts, or fixture profiles are shown to users.
3. Treat future domain-engine work as gated amendment scope until the accepted project state says otherwise.
4. Separate proposal language from acceptance language. "Proposed", "review aid", "summary", and "candidate operation" are non-binding; "accepted" requires explicit human evidence.
5. Prefer concrete prohibitions over vague disclaimers. State what Chirality does not do: approve, validate, certify, issue, sign, seal, prove compliance, or own solver truth.

## Considerations

- Domain-engine boundary language overlaps with general professional-boundary language in `docs/DIRECTIVE.md` and `docs/CONTRACT.md`; keep the wording mutually consistent.
- PRD Section 8.17 defines future compatibility requirements, but the PRD hash mismatch in `_REFERENCES.md` remains a source warning until reconciled.
- DomainEngineProfile details remain future work. Do not invent profile fields beyond the source-backed set: engine identity, optional version, protected paths, proposal paths, artifact types, operations, manifest rules, and boundary notices.
- OpenPipeStress may be useful as a first fixture profile, but examples must not hardcode OpenPipeStress assumptions into Chirality core behavior.
- Runtime events, adapter results, and deterministic checks can support review; they do not make a deliverable professionally reliable by themselves.
- The notice wording below is proposal-quality copy until an accountable human accepts it for a specific future UI, documentation, event-record, profile, or operation-proposal surface.

## Trade-offs

| Trade-off | Guidance |
|---|---|
| Strong notice vs. concise UI | Keep UI notice short but unambiguous; put longer rationale in documentation and review checklists. |
| Future compatibility vs. premature implementation | Preserve terms, examples, and requirements that keep a future path open; do not describe endpoints/tools as active current-release capabilities. |
| Adapter validation vs. professional validation | Deterministic adapters can validate format, manifest, operation preconditions, or profile rules; they do not replace professional review or acceptance. |
| Fixture examples vs. product identity | Fixture examples can make boundaries concrete, but must remain marked as profiles/adapters outside Chirality core. |

## Boundary Notice Copy

### Standard Notice

Chirality records and governs domain-engine interactions, proposals, and review evidence. It does not approve, certify, issue, sign, seal, prove code compliance, externally validate, or own solver truth. Domain results require review and explicit acceptance by an accountable human before reliance.

### Compact UI Notice

Domain output is a review aid. Chirality does not approve, validate, or own solver truth. Human acceptance is required before reliance.

### Operation Proposal Notice

This operation is a proposal. It identifies candidate inputs, checks, intended changes, risks, and outputs for human review. It does not apply accepted domain state until the required human gate is completed.

### Protected Artifact Notice

Protected domain artifacts are not agent-writable Chirality files. Agents may write proposals, summaries, and review aids only; accepted domain-state changes require an approved adapter or operation workflow and explicit human acceptance.

### Fixture Notice

OpenPipeStress, if used, is a fixture profile or adapter example. Its assumptions belong in the profile/adapter layer and must not be treated as Chirality core runtime behavior.

## Domain Review Checklist

| Check | Question | Expected Answer |
|---|---|---|
| Professional authority | Does the copy avoid claims that Chirality approves, signs, seals, certifies, issues, transmits, or releases work for reliance? | Yes |
| Code compliance | Does the copy avoid claims that Chirality proves code compliance or professional adequacy? | Yes |
| Solver truth | Does the copy avoid claims that Chirality owns solver truth? | Yes |
| Domain truth | Does the copy state or imply that authoritative domain truth belongs to the domain engine/domain workflow, not Chirality? | Yes |
| Human gate | Does accepted domain state require explicit human acceptance? | Yes |
| Protected paths | Are protected domain artifacts separated from proposal/review-aid paths? | Yes |
| Current scope | Is domain operation execution marked future-boundary/gated where relevant? | Yes |
| Fixture posture | Is OpenPipeStress treated as a fixture profile if mentioned? | Yes |
| Unsupported facts | Are missing details marked TBD, ASSUMPTION, PROPOSAL, or human-ruling items? | Yes |

## Completed Checklist Capture

Completed checklist evidence should be captured as part of the review output record described in `Procedure.md#Review Output Record`. Until a future amendment defines a product-native storage location, the capture location is `TBD` and the completed checklist is closure support only, not a human approval record.

## Examples

| Context | Acceptable Wording | Avoid |
|---|---|---|
| Domain result panel | "Result imported from the domain engine for review. Chirality records the interaction and does not own solver truth." | Any claim that Chirality has validated the domain result. |
| Operation proposal | "Proposed operation pending human acceptance." | Any claim that Chirality has approved the operation. |
| Compliance note | "Reviewer must determine whether the result supports project requirements and applicable standards." | Any claim that the output establishes code compliance. |
| Protected artifact | "Write a proposal or summary; do not directly modify protected model truth." | Any claim that an agent may update protected solver model files directly. |
| Fixture mention | "OpenPipeStress fixture profile, if adopted by amendment." | Any claim that OpenPipeStress is Chirality core behavior. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CT-001 | PRD source hash mismatch recorded in `_REFERENCES.md`; dispatch instructs treating mismatch as source warning only. | `_REFERENCES.md` REF-006 expected/actual SHA values | User dispatch instruction | Datasheet Conditions; Specification Documentation; this Guidance section | Use current accessible `docs/PRD.md` for P1/P2 drafting while preserving the warning until reconciled. | TBD |

## Human Rulings Needed

- Confirm whether the standard and compact boundary notices are accepted wording or remain proposal copy.
- Confirm who may accept proposed boundary notice copy as sufficient for specific future surfaces.
- Confirm future `DomainEngineProfile` copy locations once DEL-10-01 is accepted.
- Confirm engine-specific wording if OpenPipeStress or another domain engine is adopted by amendment.
