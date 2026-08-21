# Real daemon replay — partial result

Verdict: `DAEMON FIXTURE PASS / PACKAGED UI REPLAY NOT OBSERVED`

The frozen package started one isolated daemon on
`/private/tmp/chirality-d86pkg02.VWKLGL/userdata/runtime/control.sock` as PID
`67623`. Only the current worktree manifest was registered. The deterministic
stub adapter was used; no provider credential or provider call was used.

Recorded fixture:

- project: `chirality-app-dev`
- session: `2900d411-0e02-4054-9dd4-5fe8c04716ac`
- persona / role: `WORKING_ITEMS` / `agent1`
- adapter / provider / model: `stub` / `stub` / `stub-parity`
- final status: `completed`
- accepted event: `fd591faf-752f-4c63-975e-ffee28d634c3`
- terminal event: `471df70c-adb5-41b8-b70e-d6e543b6da54`
- canonical events: 2
- derived transcript items: 1
- malformed events: 0

The durable sanitized fixture is
`instances/A2-PKG02-PARITY-EXECUTOR-01/evidence/runtime/fixture.json`
(SHA-256 `39dcee74ea8ddfc1aa110addc3ff8e280d4aea0b8f595b4d73b7efa3ffba7cd8`).

No packaged UI replay binding is claimed. The required GUI observation was
not lawfully reached after the owner-state stop condition fired.
