# Amendment 02 — KeepAlive cleanup-race remediation

- Parent disposition: `AMEND` the same implementation node in place.
- Trigger: fresh review v2 closed all six v1 findings but found one bounded
  cleanup-recovery defect.
- Required change: make cleanup reclaim the unique proof service/process even
  across a transient first `bootout` failure and KeepAlive PID replacement.
  Use a bounded loop that re-inspects the service, captures any replacement PID,
  retries `bootout` until exact not-found, identity-gates any necessary signal,
  waits after SIGTERM/SIGKILL, and only then verifies service/process/plist
  absence. Never target the default service or an unverified process.
- Focused regressions: transient bootout then success; KeepAlive replacement PID;
  bounded terminal failure when cleanup cannot reclaim; post-SIGKILL wait.
- Preserve all Amendment 01 behavior, PR #590 byte intent, workflow gates,
  artifact retention, write scope, and exclusions.
- Rerun: focused tests and registered frontend test/typecheck/build plus always
  checks, syntax, diff, origin/main-intent, and containment.
- Return: exact remediation/evidence/new hashes and residual PR-CI proof only.
