# WORKING-A1-PKG02 Sealed Launch Brief — v1

Role: `WORKING_ITEMS` Agent 1. Package: `APP-PKG-02`. Members: `DEL-02-01`,
`DEL-02-02`, `DEL-02-03`, `DEL-02-04`, `DEL-02-05`. Execute exactly the
accepted PKG-02 row of `snapshots/W_A1/preflight/PACKAGE_PLAN.tsv`, its five
rows in `A1_MANIFEST.tsv`, and `amendments/A1-PACKAGE-ACTIVATION-001.md`.

Write only `candidates/W_A1/APP-PKG02/**` and
`instances/WORKING-A1-PKG02/**`. Live project paths are read-only. Dispatch
one sealed author and one later fresh verifier per member under the shared
activation contract. Require 5/5 complete pairs, exact 25-row replacement and
inverse rollback, package checks, portable evidence, and terminal package
fan-in. Return PASS/BLOCKED/DECISION_REQUIRED to HELP_HUMAN; do not integrate.
