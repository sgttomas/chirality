# PKG02 Generated Check-Evidence Normalization Checks

Authority: `amendments/A1-PKG02-CHECK-EVIDENCE-PORT-001.md`.

Verdict: `PASS`.

- The only modified files are `PROJECT_CHECKS.json` and
  `PROJECT_CHECKS_PREMERGE.json`.
- Exact authorized substitutions: 27 checkout-root occurrences and four
  temp-root occurrences. Remaining preimage-prefix occurrences: zero.
- Both postimages parse as JSON. All six registered results remain `PASS`
  with exit code zero: self-check, harness pytest, typecheck, full test, build,
  and live-stub premerge.
- Reverse substitution reproduces both exact amendment-bound preimage hashes.
  Therefore commands, exit codes, statuses, stdout, stderr, and all other
  substantive JSON content are unchanged modulo the two authorized literals.
- Direct package-local preimage hash/summary bindings before repair: `NONE`.
  No binding refresh was required.
- Candidate, source, status, control, mapping, parity, checklist, render,
  child verdict, project, Git, lifecycle, and integration bytes were not
  changed by this repair.
