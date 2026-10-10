# DEL-02-06 — current contract revision

Preserved from `24e9117b9c:projects/chirality-runtime/execution/_Coordination/AgentRuns/RUNTIME_DGOV43_HOLD_CLOSURE_20260912/Impact_Assessment.md`.

## DEL-02-06 carrier revision notes (recorded here; `ScopeOfWork.md` unchanged)

Fan-in paragraph: DEL-02-07 through DEL-02-12 are retired under D-GOV-43
items 7 and 11 (A2 supplement); their six fan-in inputs no longer gate this
carrier. The nine held bindings are closed by this packet, not released by
evidence. The carrier's remaining stewardship is the application-owned
Runtime service and the lockfile-pinned stock Codex dependency; release
readiness is established by ordinary checks and the three retained human
decisions.

REQ-010: the `HOST-P1` lease, the atomic supplier snapshot with opaque
account and workspace identifiers, and the capability or version-mismatch
refusal are superseded. The stock Codex version is pinned by the package
manifest and lockfile and updated as an ordinary dependency update with
re-validation; upstream drift is not a stop condition. Account identity
comes from Codex's own account methods within the App's effective home. The
fail-closed precondition posture otherwise stands, read against the
application-owned service.

REQ-041: the daemon-owned trusted supplier authentication process, exact
supplier qualification and the D-GOV-36 custody exception are superseded on
the App path. Sign-in and sign-out use Codex's own account methods inside
the Chirality effective home; credentials are custodied by Codex and never
read, copied or relayed by the Runtime. DEL-02-09 is retired; the separation
purpose is verified by the S-8 check.
