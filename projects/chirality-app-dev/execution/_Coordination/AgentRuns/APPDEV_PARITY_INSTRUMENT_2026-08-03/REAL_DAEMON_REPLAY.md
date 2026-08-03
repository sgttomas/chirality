# Real Daemon Replay Binding

Verdict: `PASS`

## Isolated runtime posture

Retry 02 ran the frozen packaged daemon as PID `54016` with a fresh absolute
`CHIRALITY_USER_DATA` under the exact temporary root
`/private/tmp/chirality-dapp86-parity-r2.wfbKam`, the stub adapter, no provider
credential, no provider network path, and no real launcher/LaunchAgent write.
Only the App worktree manifest was registered.

Registered project:

- Project ID: `chirality-app-dev`
- Client ID: `project-72eb360c-c21e-4326-b612-33004b11bee7`
- Manifest hash:
  `5a79777038acd2b5fda3b0416c0092e2c980ff0eff7e84a019fdac3bac8fdc04`
- Durable sanitized register response SHA-256:
  `39616b65e2fbb05d5020bdbf4f042f16af8c79d53f269e8f88d36175373aad57`

## Recorded session and events

- Session ID: `e2c32024-fa62-48d5-b27a-d8637080d2c3`
- Persona: `WORKING_ITEMS`
- Role: `agent1`
- Parent: none recorded
- Adapter/provider/model: `stub` / `stub` / `stub-parity`
- Final runtime status: `completed`
- Turn ID: `069051b9-d567-45f7-ad03-1ec37aa99844`
- Accepted event ID: `18da5693-3791-4e2e-a96c-363785f4d647`
- Terminal event ID: `a26a661d-721e-491d-ab9f-66b2aa3b2dd0`
- Canonical events: 2 (`turn.accepted`, `turn.completed`)
- Derived transcript items: 1
- Malformed events: 0

Durable runtime evidence:

- `retry02-session-create.json` SHA-256
  `4f4d4748949bf8a0f7635f382ea36b5ff03b4a0d686214d3139110fbcd161fe7`
- `retry02-turn.jsonl` SHA-256
  `dd00964018e1000bbb514eec3ba06754118bc0e1ae763bcef34e0aeabc2bdb1f`
- `retry02-replay.json` SHA-256
  `82c96ff95cc34a31877e2ee8ee25e4bac6fe73abf73c8c6b162bad0eb01e948a`

The packaged UI replay cites the same exact session ID and terminal event ID.
This binds the UI observation to the isolated daemon store rather than to a
mocked renderer-only record.

## Cleanup binding

The Retry-02 daemon log's final SHA-256 before removal was
`5176bfd82e6b464c731abca27f42c570dab41793f8f36c67eeaef82b0b3cc15b`.
Its final lines recorded `desktop.shutdown.started` and
`desktop.shutdown.completed` at `2026-08-03T08:55:04.967Z` for PID `54016`.
The GUI log's final SHA-256 was
`2ec098f05b428709669b22eef8dc3e7d0cfc788205d576ef74e6d0adad2eb921`
and likewise recorded completed shutdown for PID `54094`. These final raw
logs lived only in the isolated root; the hashes and exact terminal facts are
retained here, and the root was then removed as required.
