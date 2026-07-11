# Deliverable Concordance Method

Chirality AI Ltd. Date: 2026-07-11. Revision 0.

**Status: DRAFT pending human ratification (K-AUTH-1).** This document is not
accepted governance and is **non-binding**: while it is DRAFT, each project's
own concordance plan remains the self-contained operative method, and no agent
may cite this document as authority for any act (GEN-6 discipline — draft
basis is never binding). Ratification is gated on completion of both adopting
projects' R0 method calibrations. Owner direction of record (2026-07-11,
in-session, Ryan Tufts): the method is intended as part of Chirality itself,
authored at root as a DRAFT canon-pattern document.

**Provenance.** Distilled from the two project method plans —
`projects/chirality-app-dev/plans/PLAN_2026-07-10_deliverable_implementation_reconciliation.md`
and
`projects/chirality-piping/plans/PLAN_2026-07-10_deliverable_implementation_reconciliation.md`
— and the 2026-07-10/11 owner design session recorded in those plans and in
`projects/chirality-app-dev/loop/LOOP_RECEIPTS.md`. This document is
derivative of those sources; on any disagreement while DRAFT, the project
plans govern.

## 1. Purpose

Restore and keep a deliverable corpus as a reliable statement of accepted
scope, implemented behavior, verification evidence, unresolved work, and
lifecycle state — without requiring anyone to reconstruct project truth from
plans, chat history, or memory.

## 2. The problem this method exists for

Project truth decays when it is distributed across too many representations —
plans, assessments, specifications, status files, coordination records,
implementation, tests, decisions, run records — each maintained independently.
Together they behave like an unsynchronized database: every copy made sense
when written, and their disagreements compound silently. Drift is therefore a
**normalization problem**: each kind of truth must have exactly one designated
home, and everything else must be derivative and dated.

The normalized homes:

| Kind of truth | Sole home |
|---|---|
| Normative scope | Current authority documents and decomposition |
| Accepted decisions | The project decision register and its ruling records |
| Executable open work | Deliverable-local `_STATUS.md` `## Remaining` |
| Lifecycle state | Deliverable-local `_STATUS.md`, human-gated |
| Implementation truth | Source, tests, and build/validation artifacts |
| Evidence | Immutable, dated, source-state-bound run artifacts |
| Method and provenance | Plans — historical, never work-selection surfaces |

## 3. Reconciliation is an epistemic operation

Concordance is not "update documents from code" — implementation is evidence,
not scope authority. Every claim is audited by distinguishing kinds of
knowledge: normative scope, accepted decisions, declared current state,
observed implementation, verification evidence, validation evidence (where the
claim class demands it), lifecycle state, and recorded remaining work. The
audit unit is the **claim** (a requirement or stable scope statement), never
the whole deliverable: one deliverable can simultaneously contain aligned
requirements, stale wording, unvalidated mechanics, and legitimate deferrals,
and a single verdict would destroy that information. Deliverable summaries are
derived from claim rows, never substituted for them.

Core controlled dispositions (projects extend, never weaken): `ALIGNED`,
`IMPLEMENTED_UNDOCUMENTED`, `DOCUMENTED_UNIMPLEMENTED`, `PARTIALLY_IMPLEMENTED`,
`IMPLEMENTED_DIFFERENTLY`, `ACCEPTED_DIVERGENCE`,
`LIFECYCLE_REASSESSMENT_REQUIRED`, `DEFERRED_AGENT_WORKFLOW`,
`AUTHORITY_CONFLICT`, `UNKNOWN`, `STALE_INPUT`.

Fixed epistemic guardrails: discovery is read-only and separated from repair
(never edit the audit target while determining what it means); every evidence
citation binds to the source state it actually evaluated; conflicts between
live normative sources are recorded (`AUTHORITY_CONFLICT`), never resolved by
agent precedence-invention; no agent disposition is ever represented as a
human ruling; completion is an evidence-coherence state, never issuance,
release readiness, or professional approval.

## 4. Lifecycle model

Lifecycle states are **change regimes, not maturity grades**:

- `IN_PROGRESS` — ordinary edits permitted. The honest holding state whenever
  warranted open scope exists, however advanced the implementation.
- `CHECKING` — a frozen candidate under review against a declared basis.
  Reversal to `IN_PROGRESS` is the only edit path; review evidence appends to
  run/review records, never to the frozen claim surfaces. The review is
  internal to the claims the deliverable makes about itself.
- `ISSUED` — accepted baseline; changes only through the governed
  scope-change process.

**Entry trigger:** a deliverable becomes a CHECKING candidate when its
`## Remaining` is **warranted-empty** — empty, and a current evidence basis
(a concordance pass or equivalent review bound to the candidate source state)
certifies that the emptiness is warranted. The entry act is the owner
declaring the checking basis and freezing the candidate. There are no
disclosed-deferral carve-outs: any warranted Remaining item — owner-gated
included — keeps the deliverable `IN_PROGRESS`; boundary adjustments happen
through the decision register while `IN_PROGRESS` (rescope before freeze,
never carve out during review). A failed check exits by reversal, its
findings becoming Remaining items. Concordance is thus the process that makes
`## Remaining` sections warranted — the path back to `CHECKING`.

**Rebaseline asymmetry:** demotion to `IN_PROGRESS` requires no criteria —
only the absence of a current, accepted basis for the asserted state.
Promotion requires a contemporary declared basis. Lifecycle corrections are
human-authorized administrative acts recorded through the register; they do
not invalidate prior work or evidence, which is preserved as history.

Checking-basis criteria are **layered and emergent**: a small universal entry
condition set, a per-candidate declared basis assembled from the deliverable's
nature and risk, and maturity feedback from real checks hardening into
reusable profiles — profiles are ruled documentation surfaces, not
predetermined checklists.

## 5. Program state model

A concordance program creates no standing surface. Its state divides three
ways, each with an existing home:

1. **One run's phase state** — the immutable, append-only run folder
   (`execution/_Reconciliation/DeliverableConcordance/<RunID>/`), bound to its
   source state and expected to age out.
2. **Cross-session visibility** (program open/closed) — the activation
   decision's register row, whose ruling-record cell points at the run folder
   and receives a closure note; registers are re-read every loop iteration.
3. **The recurring process asset** (checking-entry profiles, maturity
   feedback) — a ruled docs profile surface, amended only by ruling.

## 6. Activation pattern

- Activation is a **register decision**: a PROPOSAL packet, an owner ruling
  naming the activated scope, and a ruling record. The ruling record and
  register flip **land on the shared mainline before any dispatch** —
  concurrent sessions are mutually blind, and an owner act that exists only
  in one session's context is a governance fork waiting to happen.
- Executable per-deliverable work is seeded as gated `## Remaining` items in
  the owning deliverables and unlocked by the ruling's suffix flips; run-level
  phases execute directly under the ruling as ruled-program work.
- Single-surface compliance: the plan, the run artifacts, and this document
  never select work. Owner decisions live in the register; executable
  residuals live only in the owning deliverable's `## Remaining`.

## 7. Adoption

Each adopting project keeps a self-contained project plan as its operative
method and adoption record. Project-local layers are expected to diverge —
e.g. engineering validation/provenance disciplines in one project,
inspection-assessment recency disciplines in another — and are never
flattened into this kernel. Sibling plans are not resynchronized without
owner direction. This kernel is amended only by owner act; at ratification,
the project plans may thin to project-specific parameters citing this
document as the shared method.

## Document History

| Revision | Date | Change |
|---|---|---|
| 0 (DRAFT) | 2026-07-11 | Initial distillation from the two project concordance plans and the 2026-07-10/11 owner design session. Non-binding pending ratification after both R0 calibrations. |
