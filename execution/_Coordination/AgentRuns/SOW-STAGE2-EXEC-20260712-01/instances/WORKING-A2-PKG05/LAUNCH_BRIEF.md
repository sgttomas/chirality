# WORKING-A2-PKG05 Sealed Launch Brief — v1

Role: `WORKING_ITEMS` Agent 1. Package: `APP-PKG-05`. Members: `DEL-05-01`,
`DEL-05-02`, `DEL-05-03`, `DEL-05-04`, `DEL-05-05`. Execute exactly the
accepted PKG-05 row of `snapshots/W_A2/preflight/PACKAGE_PLAN.tsv`, its five
rows in `A2_MANIFEST.tsv`, and `amendments/A2-PACKAGE-ACTIVATION-001.md`.

Write only `candidates/W_A2/APP-PKG05/**` and
`instances/WORKING-A2-PKG05/**`. Live project paths are read-only. Dispatch one
sealed author and one later fresh verifier per member under the shared
activation contract. Require 5/5 complete pairs, exact 25-row replacement and
inverse rollback, package checks, portable evidence, and terminal package
fan-in. Return PASS/BLOCKED/DECISION_REQUIRED to HELP_HUMAN; do not integrate.
