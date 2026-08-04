# Existing daemon-suite baseline

Command (outside sandbox because Unix sockets were denied inside it):

```sh
cd /tmp/chirality-tm112-runtime.iID3BU
npm test -- --run tests/daemon.test.ts
```

Exact terminal summary:

```text
> @chirality/runtime-workspace@0.1.0 test
> vitest run --run tests/daemon.test.ts

 RUN  v3.2.7 /private/tmp/chirality-tm112-runtime.iID3BU

 ✓ tests/daemon.test.ts (5 tests) 182ms

 Test Files  1 passed (1)
      Tests  5 passed (5)
   Start at  20:26:04
   Duration  405ms (transform 73ms, setup 0ms, collect 99ms, tests 182ms, environment 0ms, prepare 27ms)
```

Coverage inspection: the five tests cover credential replacement, private
socket/auth/SSE wire format, pre-stream failure, client-disconnect
interruption, and stale-socket/owner rejection. Teardown calls `daemon.stop()`
after each test, but no existing test invokes stop while an ordinary request
or SSE response remains live.
