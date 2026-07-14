# PKG-04 Reconciliation Checks

Terminal technical verdict: `PASS`.

- HEAD, local `main`, `origin/main`, and remote `main` equal
  `2a5e3825d8d2fc4943742a53ccad3b89c4c81902`.
- Five upstream manifests rehashed 3,117/3,117 bindings. The package manifest
  has 1,606 rows; child manifests have 776, 400, 167, and 168 rows. Every row
  passed portability, containment, existence, uniqueness, self-exclusion,
  byte-count, and SHA-256 checks.
- The 1,607 unique upstream manifest surfaces, including the five manifests,
  have zero trailing-whitespace and terminal-blank-line findings.
- Four child returns and their manifest identities reproduce exactly from
  `CHILD_INDEX.tsv`: two `PASS` authors and two fresh `PASS_UNCHANGED`
  evidence-only verifiers.
- Live source/status/context/reference/dependency bindings passed 54/54;
  candidate evidence/production/finalization bindings passed 18/18.
- Fresh full-package reproduction passed all six members, 178 mappings,
  1,368/1,368 physical source lines, exact 30-row replacement and inverse
  rollback manifests, 6/6 simulations, and 12/12 fail-closed negative probes.
- Every member freshly passed validation, production-bound mapping, parity,
  twice-repeated checklist derivation, twice-repeated offline rendering, and
  deterministic finalization binding. Repeated artifacts were byte-identical;
  rendered HTML contains no script or external URL.
- Fresh `tools/practitioner_harness/harness.py self-check` exited 0. Fresh
  `pytest -q -p no:cacheprovider tools/practitioner_harness` passed 264/264;
  JUnit records zero failures and errors.
- The Piping project tree remained exactly 191,216 files at SHA-256
  `0bdb64423d995287242654be8449b9c6c2ac955e8dd2c1a88b1d30a13c4b9b01`
  before and after reconciliation. Project-scoped Git status is clean.

Separate verdicts: schema `PASS`; content/authority `PASS`;
preservation/containment `PASS`; clean finalization `PASS`; execution
substrate `PASS`.
