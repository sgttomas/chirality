# UI Validation v7

Subject: `UI_SOURCE_FREEZE_v7.md`

- subject SHA-256: `240a974e9e6a0c9317ea77b9588997adf2d03b613bfd78595ee1a8c3c5405a80`
- subject members: 48/48 hashes verified
- focused App v3 suite: 9 files, 70 tests passed
- full frontend suite: 188 files and 1,993 tests passed; one file and four registered tests skipped
- frontend and Electron TypeScript typecheck: passed
- diff check: passed
- App authority corpus: v21, all 12 applicable members match; status and audit passed

Independent Astra review passed with zero remaining actionable App UI findings:

- reviewer return SHA-256: `0bbe887d2d6a9fe4c3324a1083a99f206daebf544b80ab367e71519dd8250c94`
- reviewer manifest SHA-256: `483f6abaaa0cf5151e4e4e185ffe7b87d4538c6ac8ee36bc0d5a47b9baa38997`
- reviewer checks: 48/48 postimages, 10/10 preserved counterexamples, and 9 files / 55 independent focused tests passed

The controlled browser journey used a hand-seeded mock protocol daemon through
the real Unix-socket RuntimeClient and Next proxy. It proved same-session replay
and continuation, unavailable native Plan Mode handling, method selection and
inspection, and a real Refresh refetch. It does not prove production Runtime
catalog discovery, provider behavior, supplier completion, native Plan Mode
qualification, packaging, or release readiness. The final continuation capture
was stacked and clipped by IAB, so visual layout evidence remains the earlier
settled v4 desktop capture; v7 did not change styling or layout.

Runtime's independent review reported a separate historical native-plan export
qualification coupling issue. The App renders returned historical revisions
without conditioning them on current capability, but Runtime must close and
re-review its response semantics before the integrated tranche is accepted.
