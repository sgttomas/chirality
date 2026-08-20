# Amendment 03 — Reverify identity before SIGKILL

- Parent disposition: `AMEND` same implementation node.
- Required change: in `terminateVerifiedProcess`, after the SIGTERM wait and
  immediately before SIGKILL, reinspect the numeric PID's text executable and
  require the same single exact packaged executable identity. Refuse SIGKILL
  and fail closed when identity is absent, changed, or ambiguous.
- Tests: identity changes after TERM => no SIGKILL and terminal failure;
  successful SIGKILL path => second identity inspection occurred.
- Preserve all prior behavior, tests, PR #590 intent, scope, and exclusions.
- Rerun focused and full registered checks, freeze hashes, and return for fresh
  review v4. No local launchd or Git/dependency action.
