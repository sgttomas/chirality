# Superseded generated candidate — never accepted

These raw bytes were generated from clean runner commit
`b1f0d71f128e31fb2f0d10b579abf6523bae7d3c` and formed part of reviewed
candidate `2c42f919aa38546c5a4ad9eb692b450aa5c13d06`.

Round-3 review rejected that candidate on J3-F1: a TERM-resistant descendant
could call `setsid()`, leave the controller-anchored process group, and survive
cleanup. The candidate therefore never became accepted revision-2 evidence.
Its raw run bytes and verifying per-run manifest are retained as dated
history, but the folder is excluded from `COMPARE_RESULT_revision2.txt` and
from the current preservation claim.

The accepted replacement run is
`../run-app-ede175910-runner-9dfbb7962-revision2/`. It uses the host-pinned
LaunchAgent resource/jetsam coalition and audit-token cleanup method reviewed
after J3-F1.
