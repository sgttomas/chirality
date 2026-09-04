# APP RULING RECORD A13 — DEL-05-01 legacy session record retention — owner ruling of 2026-09-03

> **Plans-folder status:** ACTIVE owner-ruling record — non-governing transcription source. Owner: Ryan Tufts. Scope: the duplicate-shape disposition of legacy flat project-local session records after canonical materialization under the seated item `DEL-05-01-V3-01` (development node D of the v3.0.0-rc.1 pathway). Target workspace: App-dev loop. Supersedes nothing; amends DEL-05-01 `ScopeOfWork.md` rows R010 and CLM-012 through the tranche it authorizes and renders D-APP-41 historical on the single point of flat-record removal. Companion instruments: A12 (`chirality_app_v3_app_ruling_record_a12_2026-09-03.md`, SHA-256 `21b77b378a6511b48ea2e60e676ea1c9b7ee013d8c042769392decf57ceb29ec`); D-APP-41 (`projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-41_RULING_2026-06-21.md`, historical on this point, not edited); `docs/SPEC.md` Section 25.4; applied decomposition row L322. Run evidence: `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_D_2026-09-03/`.

Ruled by Ryan Tufts (K-AUTH-1) in the HELP_HUMAN session chat on
2026-09-03 by selecting one option. "[click]" marks the option the owner
selected. HELP_HUMAN relayed the ruling to the sealed ephemeral Agent 2
implementer of node D (Claude Fable 5.1), which applied it as a second
local commit on branch `codex/app-v3-nodeD-v2-session-access-2026-09-03`
from basis `0c683fb1657706316272951e4c3a0f7781b46009` (PR #681 merge; the
first frozen commit was `3b6b4758bca7cd0e4ac84f9685052a0548c4ca2e`).

## Context

A12 seated `DEL-05-01-V3-01` (`SELECTABLE`): representative v2 (release
2.0.0) project-local session records must open lazily and non-destructively
with typed failure states while list, resume, and delete behavior is
preserved (applied decomposition row L322; AT-035 "opens without
destructive rewrite"). The node D implementer retained the legacy flat file
after canonical materialization (canonical wins; corrupt canonical fails
closed; legacy bytes never rewritten), satisfying the seated row and
`docs/SPEC.md` Section 25.4 ("No bulk rewrite or destructive source move is
permitted"), but reversing DEL-05-01's accepted MUST R010 ("write the merged
canonical `session.json`, and remove the flat record"), its CLM-012
verification row ("flat-file removal"), and D-APP-41's remove-or-archive
practice, and changing shipped 2.0.0 behavior.

The independent reviewer (fresh read-only `software-code-review` instance)
returned 0 blocking / 1 major / 2 minor findings: F1 classified the conflict
as an owner decision between accepted instruments rather than a stale-map
delta or agent latitude; F2 observed that a retained flat file remained a
standing read input on every access (latent field resurrection); F3
observed that `listWithDiagnostics` aborted the whole listing on a single
candidate's non-record I/O failure. HELP_HUMAN presented F1 as the fork
below.

## Owner ruling — verbatim

```text
Question "Node D ruling. The implementer retained the legacy flat session file after canonical materialization (canonical wins; corrupt canonical fails closed; legacy bytes never rewritten). This satisfies the seated row L322 and SPEC's 'no destructive source move', but reverses DEL-05-01's accepted MUST R010 ('write the merged canonical session.json and remove the flat record'), its CLM-012 verification, and D-APP-41's remove-or-archive practice, and it changes shipped 2.0.0 behavior. Which instrument governs?"
  [click] "Ratify retention (Recommended)" — Record as A13: retention is the v3 posture (AT-035 'opens without destructive rewrite'). Node D amends R010 and CLM-012 text in DEL-05-01's SOW in the same tranche under this ruling, adds a legacySource marker so the flat file is not a standing read input (reviewer F2), fixes the list-abort regression (F3), and re-freezes for re-review. D-APP-41 stays historical.
  "Reinstate removal" — not selected.
  "Archive instead" — not selected.
```

## Applied meaning

- Retention is the v3 posture for DEL-05-01: on duplicate shape the merged
  canonical `session.json` is written; the flat record is retained
  byte-identical and is not removed; canonical wins on later reads; a
  corrupt canonical record fails closed and is never overwritten from the
  flat record.
- The canonical record carries a `legacySource: { sha256, materializedAt }`
  consumption marker written at materialization. Once present, the flat file
  is not a standing read input: legacy-only fields are merged exactly once
  (marker absent); an unchanged flat file is ignored; a flat file changed
  after consumption is reported as a `legacySourceChanged` diagnostic and
  ignored, so a field removed from the canonical record is not resurrected.
- `listWithDiagnostics` never aborts on one candidate's non-record I/O
  failure: a readable record whose materialization fails is listed
  unmaterialized with a `materializationFailed` diagnostic.
- DEL-05-01 `ScopeOfWork.md` rows R010 and CLM-012 are amended in the same
  tranche (dated amendment note CLM-032 citing this record); D-APP-41 is
  historical on the single point of flat-record removal and is not edited.
- The tranche re-freezes for a fresh independent review over the full
  basis→HEAD diff before push.

## Not ruled here

- Acceptance of the node D candidate bytes (owner byte review and merge).
- Cleanup, archival, or backup of retained flat records (the unseated
  `SCOPE_AMENDMENT_REQUIRED` S-4 in the A12 seating packet MAPPING).
- A dedicated `HarnessErrorType` for unreadable session records (Root-owned
  closed union; proposal routed with the Root schema work consumed by
  `DEL-05-01-V3-02`).
- `DEL-05-01-V3-02` (parked: `NOT_SELECTABLE_UNTIL` the accepted Root daemon
  session/storage schema is routed to App).
- Any lifecycle transition, release act, host mutation, or Root write.
