# C2F-R2 Consumer Fan-In

Overall verdict: `PASS — NO RECONCILIATION BLOCKER TO C2G FAN-IN`

## Reconciled populations

| Population | Expected | Reproduced | Result |
|---|---:|---:|---|
| P0 exact caller rows | 64 | 64 | PASS |
| C2R rows | 52 | 52 | PASS |
| C2A App rows | 9 | 9 | PASS |
| C1G canon rows | 3 | 3 | PASS |
| C2R changed source paths | 48 | 48 | PASS |
| C2A changed source paths | 4 | 4 | PASS |
| Unclassified callers | 0 | 0 | PASS |

All non-App root manifest post-hashes match live files. All nine App identities
match the initial C2A manifest overlaid by the exact two-path C2A-R1 repair.
The root and App source sets are disjoint. Terminal root C2R-R3 and App C2A-R1
returns/statuses are present; the root C2A-R1 pointer binds the terminal
project-local package.

## Criterion closure

- Exact unpadded ruled authority succeeds only for an isolated, exact-path,
  valid, exactly bound dual candidate at the root resolver, converter, App
  scanner, and checklist CLI seams.
- Synthetic `D-GOV-16@0123456`, alternate valid-looking, padded, malformed,
  missing, marker-mismatched, non-isolated, wrong-path, invalid, partial,
  ambiguous, and requested-format-mismatched states fail closed.
- `derive_review_checklist.py` passes the raw CLI authority to the resolver.
  Its end-to-end regression proves padded authority exits nonzero and writes no
  requested checklist artifact.
- ISSUED preparation requires accepted basis, source commit, all four source
  hashes, and status hash; embeds the bindings; preserves `_STATUS.md`; remains
  lifecycle-neutral; and does not satisfy H1.
- SOW-only and retained legacy-only compatibility remain green. DOMAIN/KTY and
  independent schemas remain outside this resolver.

## Outcome separation

- Schema/mechanical: `PASS` — caller identity/counts, state behavior,
  deterministic checklist contract, hashes, and terminal evidence reconcile.
- Content/authority: `PASS` — all prior exact-authority and accepted-basis
  blockers are closed on the live source state.
- Preservation/containment: `PASS` — exact 48+4 disjoint source writes and no
  governed project-state write.
- Execution substrate: `PASS` — current direct remediation returns record root
  focused `19 passed`, full tools `792 passed`; App focused `76 passed`, full
  frontend `713 passed, 4 skipped`, plus typecheck, build, self-check,
  practitioner `264 passed`, and owned-server premerge PASS. No waiver is used.

No expensive suite was duplicated by this final fan-in; current evidence was
consumed and live identities, source semantics, manifests, and changed sets
were independently reproduced.
