# Amendment 02 — manager pre-freeze security repair

- Disposition: `REPAIR` before fresh review.
- Detection layer: WORKING_ITEMS manager fan-in.
- Failure class: security-preservation and production-bypass defects.
- Product scope: existing authorized cleanup state validation and runtime-host
  socket guard only.

## F1 — preserve state strictness

The candidate parser retained a single state field but stopped enforcing the
prior PID-present `state === running` rule. Repair must require every
PID-present job to be exactly running before strict lsof identity inspection.
An exact-owned pid-less job may skip lsof only in a non-running
crash-loop/scheduled state; a pid-less job claiming running must fail closed.
Focused tests must cover both negative cases while preserving exact pid-less
`spawn scheduled` cleanup.

## F2 — remove production platform bypass

The candidate changed `startRuntimeHost` to accept a caller-controlled
platform override. Remove that public bypass and restore its no-argument
production signature using actual `process.platform`. The test may safely
mock and restore `process.platform` or use an equivalent non-bypass design to
prove rejection occurs before daemon construction/listen.

After repair, rerun syntax, focused tests, typecheck, full frontend tests,
candidate whitespace, diff/cached checks, App containment, and empty-index
checks. Refresh source/test/R17/evidence/return hashes. Preserve Amendment 01's
short future root. Do not broaden authority or perform any prohibited action.
