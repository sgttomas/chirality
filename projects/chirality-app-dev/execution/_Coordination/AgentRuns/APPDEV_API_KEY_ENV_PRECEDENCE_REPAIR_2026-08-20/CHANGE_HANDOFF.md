# CHANGE handoff — API-key environment-precedence repair

- Branch: `codex/app-api-key-precedence-20260820`.
- Stacked base: PR #586 head `6710ee6354debc201f6a454e2802897026cd4b38`.
- Dependency: publish as the next stacked iteration after PR #586; do not
  fold this work into that prior iteration.
- Graph: serialized N1 PKG-04 -> N2 PKG-02 -> N3 PKG-09 -> integrated review.
- Product identities: storage `d810b1ef…1444db`, storage test
  `c9cadac3…17dac4`, IPC `3293cbf1…ed3cb`, IPC test `818b7424…4b1a6`.
- Packaged proof: PASS, subject `1623b297…b4ce2`; secret scan 5,868/0.
- Frozen reviewed subject: 98 paths, aggregate
  `7ea308cf90bac02a7c439c71d0f01d2024ecee2a90c1fc16cfd1f4fd95bc1959`.
- Fresh integrated Review 03: PASS, zero actionable findings.
- Final APP-HOLD reliance: ALLOW for DEL-09-06 and DEL-09-04.
- Manager fan-in: PASS; no blocker or human ruling.

CHANGE owns exact candidate staging, candidate-wide staged whitespace and
containment validation, commits in graph dependency order, push, and one
stacked PR against the live PR #586 branch unless the predecessor has merged.
No receipt or shared completion-log write occurred in this manager run.
