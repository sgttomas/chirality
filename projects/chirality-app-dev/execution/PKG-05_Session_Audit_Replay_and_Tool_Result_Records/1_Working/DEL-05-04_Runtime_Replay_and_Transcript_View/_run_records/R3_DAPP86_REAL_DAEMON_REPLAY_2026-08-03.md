# R3 D-APP-86 Real-Daemon Transcript-Item Evidence — DEL-05-04

- Date: 2026-08-03
- Run: `APPDEV_PARITY_INSTRUMENT_2026-08-03`
- Authority: D-APP-86 Option A, packet SHA-256
  `80c5bd5d752715eb69f10aa510ded3d6856bc5f036a48018d352401b3e8921d6`
  and ruling SHA-256
  `b6d927259dc7ee706d019b395aeedb9d38e409c2b132797c515fa168169241e8`.
- Accepted fan-in: manager return SHA-256
  `921655319bfbe91150f8d9191dccbb8237f4ecaac50c2f37898d96803e398810`,
  handoff SHA-256
  `66869ff9be91748b2557ac7d9961c627db3d46ae94bf6649bf7d1f117c5aad5c`,
  App HELP_HUMAN notice SHA-256
  `bd3bd64f6498053f20545e8656d9a6388da7a6c0e46f025318bf6b7d4544ea1f`,
  and fresh verifier-02 return SHA-256
  `2d44a51e7083ea6c1269ee8ff9eb5b2368828cba36553f7a66ca1e56f61ea3b9`.
- Lifecycle effect: none. State remains `IN_PROGRESS`; `Authorization Basis`,
  `Directive`, and `Checking Approval SHA` are unchanged.

## Exact evidence admitted for this deliverable

The accepted derivative evidence proves only the previously recorded
real-daemon transcript-item-rendering residual. The packaged read-only replay
lens rendered exact daemon-owned session
`e2c32024-fa62-48d5-b27a-d8637080d2c3` with:

- admitted persona `WORKING_ITEMS` and role `agent1`;
- two canonical events (`turn.accepted` and `turn.completed`);
- one derived transcript item;
- terminal event `a26a661d-721e-491d-ab9f-66b2aa3b2dd0`; and
- zero malformed events.

No parent or child attribution was recorded in the session/runtime evidence.
None is inferred by this reconciliation.

## Evidence pointers

All paths below are relative to
`execution/_Coordination/AgentRuns/APPDEV_PARITY_INSTRUMENT_2026-08-03/`:

- `REAL_DAEMON_REPLAY.md` — SHA-256
  `4420a1c306687ecac55f0ee19ff7fa38058475daa04aa1d32b3673ace1127817`;
- `instances/A2-PARITY-EXECUTOR-01/evidence/runtime/retry02-session-create.json`
  — SHA-256
  `4f4d4748949bf8a0f7635f382ea36b5ff03b4a0d686214d3139110fbcd161fe7`;
- `instances/A2-PARITY-EXECUTOR-01/evidence/runtime/retry02-replay.json` —
  SHA-256
  `82c96ff95cc34a31877e2ee8ee25e4bac6fe73abf73c8c6b162bad0eb01e948a`;
- `instances/A2-PARITY-EXECUTOR-01/evidence/ui/retry02-recorded-session-replay.dom.json`
  — SHA-256
  `f3fa7e1ed48bc440ac8d0a261b61c3335ba63ae0486c25533e41845dbe095d1e`;
- `EVIDENCE_INDEX.csv` — SHA-256
  `f6fb49d322ce4c6d94b0b68de20efc5dcfb8efe69d7a1df02352e77ebbca2c73`.

This reconciliation independently recomputed the evidence index: all 39 data
rows exist and all 39 recorded SHA-256 values match.

## Status reconciliation and preserved residual

The `## Remaining` entry for transcript-item rendering against a real daemon
session is removed because the exact observation now exists. The separate
pre-existing residual remains unchanged and gated: prove Desktop and CLI
replay the same daemon-owned canonical session and preserve manager/child
attribution across restart and lazy migration.

This record does not prove broad replay coverage, Desktop/CLI equivalence,
restart or lazy-migration behavior, manager/child attribution, deliverable
closure, lifecycle advancement, release, or domain-target behavior. The
evidence package remains derivative and does not replace decomposition truth.

The accepted D-APP-88 distinct-helper implementation remains absent/blocked
on this evidence basis. Any later accepted implementation of that helper is a
mandatory non-blocking parity rerun trigger.
