# WORKING-A1-PKG00 Sealed Launch Brief — v1

Role: `WORKING_ITEMS` Agent 1. Package: `APP-PKG-00`. Members: `DEL-00-01`,
`DEL-00-02`. Execute exactly the accepted PKG-00 row of
`snapshots/W_A1/preflight/PACKAGE_PLAN.tsv`, its two rows in
`A1_MANIFEST.tsv`, and `amendments/A1-PACKAGE-ACTIVATION-001.md`.

Write only `candidates/W_A1/APP-PKG00/**` and
`instances/WORKING-A1-PKG00/**`. Live project paths are read-only. Dispatch
one sealed author and one later fresh verifier per member under the shared
activation contract. Require 2/2 complete pairs, exact ten-row replacement and
inverse rollback, package checks, portable evidence, and terminal package
fan-in. Return PASS/BLOCKED/DECISION_REQUIRED to HELP_HUMAN; do not integrate.
