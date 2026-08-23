# TM candidate — local-socket fixture sandbox determinism

Status: `HARVESTED ONLY — NOT PROMOTED OR DISPOSITIONED`

Owner attribution: the 2026-08-22 Tranche A full-suite disposition directed:
mark local-socket fixture tests with an explicit sandbox-detect
skip-with-reason, or place them in a separate Vitest project, so sandboxed
suite behavior is deterministic and the socket-denial classification stops
recurring.

## Candidate

Consider one bounded future Task Management candidate for tests that require
local TCP or Unix-socket listening:

1. Detect the execution sandbox deterministically and skip affected fixtures
   with an explicit reason; or
2. Isolate those fixtures in a separate Vitest project whose required local
   socket permission is explicit.

Source evidence is the retained R18 diagnostic
`review-1/full-vitest.log`, SHA-256
`8e10b2cab4a156f7254c5555ccf1eb823af24e57f8b6e6f86ed1cd677496ca19`,
classified `ENVIRONMENT_SANDBOX_SOCKET_DENIAL` with 21 failed / 1,246 passed /
4 skipped. The owner-authorized exact cure passed with 1,267 passed / 4
skipped and no source/test/package-script change.

This file is harvest evidence only. No implementation, Action Item register
row, promotion, ruling, priority, authority, disposition, or lifecycle effect
occurred. Task Management remains optional and no workflow act depends on this
candidate.
