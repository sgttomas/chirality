# Deferral Classification Report — App generational pass

Date: `2026-08-19`

Mode: `deferral review / full live DEFERRED population`

Repository basis: `origin/main` at
`26e32f0f6813335ec06816a32826a2667d88ef6a` (PR #577 merge)

This report records the classification evidence and the owner's exact applied
rulings. It creates no foreign-register, work, priority, acceptance, or
lifecycle effect.

## Population and classification totals

All four live App `DEFERRED` rows were reviewed. Step 3 minted no row.

| Class | Rows |
|---|---:|
| `TRIGGER_FIRED` | 1 |
| `ACTIVATABLE` | 2 |
| `STILL_BLOCKED` | 1 |

| Row | Classification | Owner ruling | Register effect |
|---|---|---|---|
| `TM-APP-027` | `ACTIVATABLE` | `RETAIN DEFERRED; ROUTE EXISTING DRAFT` | remains `DEFERRED`; Trigger unchanged; review evidence appended |
| `TM-APP-028` | `ACTIVATABLE` | `RETAIN DEFERRED; SAME ROUTE` | remains `DEFERRED`; Trigger unchanged; review evidence appended |
| `TM-APP-032` | `STILL_BLOCKED` | `RETAIN DEFERRED; NO ROUTING` | remains `DEFERRED`; Trigger unchanged; review evidence appended |
| `TM-APP-043` | `TRIGGER_FIRED` | `CLOSE RESOLVED_WITH_CHANGE` | closed with four check-artifact paths and blob SHAs |

## ACTIVATABLE

### TM-APP-027 — version negotiation and incompatibility policy

The recorded condition has not fired. Root DEL-02-06 remains `INITIALIZED`;
its current status leaves first production activation unauthorized and all
outputs/acceptance criteria unproduced or unevaluated. The semantic-acceptance
handoff still names the exact compatibility epoch unresolved and the complete
six-member binding manifest unproduced/unaccepted. No reciprocal Root notice
carrying accepted completion bytes has landed in App.

The row remains `ACTIVATABLE` because bounded Root DEL-02-06 production and
accountable-human acceptance can satisfy the recorded condition. The existing
undispatched App-owned draft requests that exact Root action and can be shipped
through closeout if the owner rules it.

Evidence:

- Root DEL-02-06 `_STATUS.md` SHA-256
  `3fedf815696ffd753a1dd83f2fbe23dcc57101acc34c0a700f32e074cc5d9b67`;
- accepted semantic handoff SHA-256
  `acf64d0518e4a589650bea6885bd5b3c2ada7dfd0f01880f05150e9017ffe2d6`;
- existing combined draft notice SHA-256
  `333bcc84e295cb7bf482d6fd905ff74fcb4f1a87b073d1222039200cadd0d73a`.

Applied effect: remains `DEFERRED`; the exact Trigger and `NoticeRef` are
retained; `LastReviewed=2026-08-19`; review evidence appended. The existing
combined draft is reserved for one closeout route carrying `TM-APP-027` and
`TM-APP-028`. No foreign register write.

### TM-APP-028 — complete degraded-mode contract

The same strict compatibility-completion condition remains unfired. The
accepted semantic snapshot alone does not satisfy the row because the Root
epoch and binding manifest remain absent, and no reciprocal Root notice states
whether the accepted ten-condition degraded-mode member remains current or is
superseded. Root `TM-ROOT-108` remains `OPEN` and is narrower than this row.

The row remains `ACTIVATABLE` through the same bounded Root DEL-02-06
instrument and combined draft route.

Evidence: the same DEL-02-06 status, semantic handoff, and draft-notice hashes
listed for `TM-APP-027`.

Applied effect: remains `DEFERRED`; the exact Trigger and `NoticeRef` are
retained; `LastReviewed=2026-08-19`; review evidence appended. It shares the
single combined closeout route with `TM-APP-027`. No foreign register write.

## STILL_BLOCKED

### TM-APP-032 — accepted current Root successor identity for D-APP-48

Root `TM-ROOT-117` remains `OPEN` in the current Root register. Its reciprocal
carrier notice explicitly says no successor identity is named, implied, or
scheduled. No later routed notice names an accepted D-APP-48 successor or
directs App to rescope the trigger.

Evidence:

- Root register SHA-256
  `6955ae0b1a606e7053e78ccf33258f3247eee6d4ef8133720a0dbeb939dc9978`;
- Root carrier notice SHA-256
  `3cae92c7ee53c86db2c20798b4fbfb1202031f7dff7d072aa9d5bbd7f7382edd`.

Applied effect: remains `DEFERRED`; the exact Trigger is retained;
`LastReviewed=2026-08-19`; review evidence appended. No notice is routed and no
duplicate Root carrier is created.

## TRIGGER_FIRED

### TM-APP-043 — per-run AgentRuns check artifacts

The trigger fired in full:

1. PR #563 merged at
   `65735390590e500dbbea6b63a4a79ba42944bf6d`, establishing the App
   work-type-conditioned delegation posture and the per-run check-artifact
   rule.
2. The first later App tranche that dispatched children, packaged adapter
   loading (PR #568, merge
   `b67197f5b647fbf0b972eee158e94c7215db9e6c`), records
   `REGISTERED_CHECKS.json`, `RUNTIME_EVENTS.jsonl`, and
   `RUNTIME_SUMMARY.json` once at its run root. Child instance folders contain
   launch brief, return, and status only; no child check or runtime-summary
   artifact exists.
3. The second later App tranche that dispatched children, the parallel
   canonical-replay/Agent-0-delegation tranche (PR #573, merge
   `1a995d571a6509d82321e4c982c7b788f16aff36`), records checks once per
   manager run and once at integration fan-in. Its child instance folders
   likewise contain no check or runtime-summary artifact.

All three merge commits are ancestors of the current `origin/main` basis.

Evidence SHA-256s:

- current App `AGENTS.md`:
  `e6bf5ce4e3b8596d85df8f8d19cb2e3d963022447811239217b8e9e233ecd7aa`;
- packaged-adapter `REGISTERED_CHECKS.json`:
  `60ae60f31401890ff581d152fa6a2bc685c76eb8016d98e05630a8c8bfb17aab`;
- Agent-0-delegation `REGISTERED_CHECKS.json`:
  `d9b07378a89ff57528b734eeeba1523b0ead7f6561ebd1cfdeb0f215c0d2ba9f`;
- canonical-replay `REGISTERED_NARROW_CHECKS.json`:
  `a7a356e1bf0e292298be990529b307993de5bda7d918266333c5fa7f26443c40`;
- parallel integration `CHECK_RESULTS.json`:
  `34196e18ebe184bab7530b2813172a0ff25e320d3b3381a897e5eaf742ec5d7e`.

Applied disposition: `RESOLVED_WITH_CHANGE`. The four package-level
check-artifact paths and their Git blob SHAs are recorded in `EvidenceRef` and
`EvidenceSha`; the verifying observation is recorded in `EvidenceQuote` and
Notes. `LastReviewed=2026-08-19`, `Closed=2026-08-19`. No follow-on row.

## Owner ruling — applied

```text
TM-APP-027 — ACTIVATABLE accepted: RETAIN DEFERRED; route existing draft.
TM-APP-028 — ACTIVATABLE accepted: RETAIN DEFERRED; same combined route.
TM-APP-032 — STILL_BLOCKED accepted: RETAIN DEFERRED; no routing.
TM-APP-043 — TRIGGER_FIRED accepted: CLOSE RESOLVED_WITH_CHANGE.
```

Deferral delta before archive: three reviewed rows remain `DEFERRED`; one row
is newly `CLOSED`; zero rows were added or elevated. The combined notice route
occurs only in closeout.
