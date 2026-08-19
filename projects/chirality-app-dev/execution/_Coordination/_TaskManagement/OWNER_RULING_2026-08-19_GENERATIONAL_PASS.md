# Owner ruling — App Task Management generational pass

Date: `2026-08-19`

This record transcribes the owner's rulings from the active Task Management
session. It authorizes only the stated App-register maintenance and any later
ruled draft routes. It creates no work, priority, acceptance, lifecycle,
foreign-register, or source-surface effect.

## Candidate harvest ruling — verbatim

```text
HARVEST — PROMOTE NONE
```

Effect: no candidate is promoted and no new register row is minted.

## Deferral-review ruling — verbatim

```text
STEP 4 RULINGS — deferral review, under K-AUTH-1:

TM-APP-027 — ACTIVATABLE accepted: RETAIN DEFERRED; route the existing draft
notice to Root coordination in the closeout tranche with reciprocal citations.
Trigger text unchanged.

TM-APP-028 — ACTIVATABLE accepted: RETAIN DEFERRED; route via the same
existing draft (one routed notice may serve both rows where the draft covers
the shared completion gate — state which rows it carries). Trigger text
unchanged.

TM-APP-032 — STILL_BLOCKED accepted: RETAIN DEFERRED. No routing; TM-ROOT-117
is already the live Root carrier. Trigger text unchanged.

TM-APP-043 — TRIGGER_FIRED accepted: CLOSE RESOLVED_WITH_CHANGE. Evidence:
PR #568 (merge b67197f5b647fbf0b972eee158e94c7215db9e6c) and PR #573 (merge
1a995d571a6509d82321e4c982c7b788f16aff36) AgentRuns packages carry run-level
registered-check artifacts with no check artifacts under child instances/;
cite the packages' check-artifact paths as EvidenceRef with their blob SHAs
and note the verifying observation in the row. No follow-on row is warranted.
```

Effects:

- `TM-APP-027` and `TM-APP-028` remain `DEFERRED`; their Trigger fields are
  byte-identical, and one combined Root notice carrying both rows is reserved
  for the closeout route.
- `TM-APP-032` remains `DEFERRED`; its Trigger is byte-identical and no route
  is prepared because `TM-ROOT-117` remains the live Root carrier.
- `TM-APP-043` is `CLOSED / RESOLVED_WITH_CHANGE` with the four package-level
  check-artifact paths and their Git blob identities bound in its evidence
  fields. No follow-on row is minted.
