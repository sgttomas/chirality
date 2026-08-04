# ORCHESTRATION PLAN — ROOT_TM112_STOP_CONTRACT_2026-08-03

Manager: `HELPS_HUMANS` (Agent 1), managed by `HELP_HUMAN` (Agent 0)
Run posture: decision preparation only; no implementation
Authority: signed `ROOT-TM112-STOP-CONTRACT-01 OPTION 1` and Owner Addition 4 in
`../ROOT_TM112_DECISION_PREP_2026-08-03/OWNER_RULING_TRANSCRIPT_2026-08-03.md`,
SHA-256 `66b967008f67934b08383291e68ef0af9923463d749cac9dbe7a74090e9cbb06`.

## Objective

Return exact, bounded, decision-ready shutdown semantics for human selection
before any implementation: finite grace duration; interruption obligations and
ordering for runtime routes/SSE; and residual-connection force behavior after
grace, including cleanup, errors, idempotence, and restart.

## Scope and holds

- Exclusive write root:
  `execution/_Coordination/AgentRuns/ROOT_TM112_STOP_CONTRACT_2026-08-03/**`.
- Read basis: N1 executed evidence; current runtime source/tests; accepted Root
  contract surfaces; local installed Node v24.18.0 behavior and public API
  declarations.
- Held: all runtime implementation, tests, canonical docs, registers, App
  content, lifecycle changes, Git operations, and downstream App notice.
- The App notice remains conditional on both human acceptance of semantics and
  an accepted repair landing.

## Classification and work graph

This is bounded novel contract reasoning, so the manager uses ephemeral
generalist Agent 2 instances with sealed briefs. No new skill, tool, or
dedicated specialist is proposed. Agent 2 instances do not delegate.

1. `E1-NODE-BEHAVIOR` — independently establish installed Node API behavior
   and version caveats; write only its instance directory.
2. `E2-CONTRACT-MAP` — map reproduced evidence, source flow, accepted
   contracts, and approved test cases; write only its instance directory.
3. Manager fan-in — prepare options, recommendation, candidate clauses,
   machine-checkable selection form, scope map, risks, and owner templates.
4. `E3-INDEPENDENT-REFUTER` — receive the completed draft by explicit
   follow-up; test option completeness/exclusivity, semantic coherence,
   implementation feasibility, evidence calibration, and held boundaries.
5. Manager repair, deterministic validation, manager return, and terminal
   handoff to `HELP_HUMAN`.

## Acceptance checks

- Three human-selected dimensions have named, bounded, non-overlapping options.
- One evidence-based recommendation is coherent and implementable within the
  approved minimum candidate scope.
- Recommended candidate wording is exact and explicitly non-authoritative.
- Completed keep-alive, incomplete request, live SSE, socket disappearance,
  owner-record completion, App-specific causality, and process/SIGTERM are not
  conflated.
- Node/platform caveats and source/evidence hashes are current.
- No implementation or out-of-scope write occurs.
- Independent refutation is durable and dispositioned.
- App notice stays conditional on semantic acceptance plus accepted repair.
