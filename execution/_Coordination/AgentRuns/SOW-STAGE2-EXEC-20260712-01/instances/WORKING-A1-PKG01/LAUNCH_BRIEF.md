# WORKING-A1-PKG01 Sealed Launch Brief — v1

Role: `WORKING_ITEMS` Agent 1. Package: `APP-PKG-01`. Members: `DEL-01-01`,
`DEL-01-02`, `DEL-01-03`, `DEL-01-04`. Execute exactly the accepted PKG-01
row of `snapshots/W_A1/preflight/PACKAGE_PLAN.tsv`, its four rows in
`A1_MANIFEST.tsv`, and `amendments/A1-PACKAGE-ACTIVATION-001.md`.

Write only `candidates/W_A1/APP-PKG01/**` and
`instances/WORKING-A1-PKG01/**`. Live project paths are read-only. Dispatch
one sealed author and one later fresh verifier per member under the shared
activation contract. Require 4/4 complete pairs, exact 20-row replacement and
inverse rollback, package checks, portable evidence, and terminal package
fan-in. Return PASS/BLOCKED/DECISION_REQUIRED to HELP_HUMAN; do not integrate.
