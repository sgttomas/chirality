# Root v3 Phase 5 orchestration plan

- **Run ID:** `ROOT_V3_PHASE5_2026-08-23`
- **Plan version:** 1 (frozen before dispatch)
- **Selection authority:** HUMAN — Ryan Tufts Phase 5 owner-carried steer and R8-B
- **Basis:** `origin/main@f7264975f63799912addbfe0442144ab5de26ca7`
- **Posture:** ordered terminal fan-out/fan-in with an independent N2 review
- **Objective:** transcribe R8-A beside the immutable estimate package, draft and independently seal an effort-hours-and-ordering-only schedule basis, then regenerate the dependency graph and closure audit at current identities.

## Ordered nodes

1. `N1_ACCEPTANCE_TRANSCRIPTION` — write the additive R8 acceptance record beside the immutable estimate snapshot.
2. `N2_SCHEDULE_BASIS` — derive the schedule-basis package from accepted estimates and Phase-3 dependency truth.
3. `N2_SCHEDULE_REVIEW` — independently review, repair if required, and seal N2 with hash manifests and `AWAITING_OWNER_ACCEPTANCE`.
4. `N3_EVIDENCE_RERUNS` — regenerate the graph and dependency-closure snapshots using current identities; depends on the accepted-basis transcription and sealed schedule package for contextual pins, but dependency truth remains unchanged.

Writes are serialized. Each child owns only its sealed brief's new targets and its own return/status. HELP_HUMAN owns the run-level control records, Receipt 125, Root handoff append, validation, Git commits, push, and PR creation.

## Fan-in gates

- N1: one additive acceptance artifact; all pre-existing estimate-snapshot bytes remain immutable.
- N2: exact aggregate 1,012 / 560–1,464 effort-hours; accepted gating edges only; no dates, staffing, velocity, commitments, or implied resolution of blockers/holds.
- N2 review: every input pin and arithmetic result reproduces; terminal fresh review has zero actionable findings; artifact manifest is generated last; package return is `AWAITING_OWNER_ACCEPTANCE`.
- N3: current inputs are pinned, including repaired Phase-3 N1 return bytes; graph node/edge/SCC and closure results agree with Phase 3 exactly or the node stops and reports deviation.

## Human gates and stops

Schedule acceptance remains an owner act. Stop for drift, an out-of-scope write, an ungrounded edge or hour, any graph deviation, a human-gated SCC move, a calendar/staffing/velocity assumption, acceptance, implementation, activation, pin change, hold lift, App authority, or foreign write.
