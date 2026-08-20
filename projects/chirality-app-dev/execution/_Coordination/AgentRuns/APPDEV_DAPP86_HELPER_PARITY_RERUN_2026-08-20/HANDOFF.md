# D-APP-86 helper-rerun handoff

Closure verdict: `OPEN — BLOCKED / PARTIAL`

Accepted upstream basis: D-APP-86 Option A, accepted D-APP-88/D-APP-93 closure,
and commit `89758a32634ee6cedbd1dbadf35e3728fb48d2eb`.

Current derivative-package status:

- source/package identity: captured;
- focused tests, typecheck, and build: pass;
- frozen package existence/hash: pass; successful package-command and
  network-authorization provenance: `UNKNOWN`;
- isolated real-daemon fixture: pass;
- four packaged UI observations: not executed;
- full validation, secret scan, and final manifest backcheck: not executed;
- parity closure: not established.

Blocker: packaged GUI startup wrote the owner-scoped launcher
`/Users/ryan/.local/bin/chirality`, contrary to the run's isolation boundary.
Only post-write facts are available: the app logged `status=written`; after the
stop the path had mode `-rwx------`, size `1114`, inode `45468523`, mtime
`2026-08-20T15:26:36-0600`, and SHA-256
`f16bc2ba9228b5321deb9c66ba9526aa60fbe3bb02179d32fd66ce1de208384a`.
No trustworthy before-state was captured. The executor did not repair,
restore, overwrite, or remove the launcher.

Live source exposes `CHIRALITY_SKIP_CLI_LAUNCHER=1` for verification, and the
instrument invocation omitted it. Agent 0 accepted this as an invocation
defect, held N2, and determined that the live package does not establish the
statuses' explicitly distinct-helper trigger. No rerun is authorized on this
basis. No deliverable surface closes on this result; the launcher remains
untouched after the recorded write.
