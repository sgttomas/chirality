# Work graph amendment 02

- Selection authority and product objective remain the owner
  `PREPARE-THEN-OWNER` ruling recorded in `ACTIVATION.md`.
- Manager ownership transfers to
  `WI-PKG09-LOGIN-PROOF-PREP-02`, still exactly one package (`PKG-09`) and one
  selected deliverable (`DEL-09-04`).
- N1 attempt 1 remains interrupted with no product/test bytes. N1-R1 attempt 2
  is interrupted without an acceptable return after Agent 0 stopped the stale
  child to eliminate overlapping writes.
- Replacement implementation node:
  `N1-R2 / A2-PKG09-LOGIN-PROOF-PREP-IMPLEMENT-03` is the sole writer for the
  candidate product script, focused test, TASK run record, and its own return.
- Review node:
  `N2 / A2-PKG09-LOGIN-PROOF-PREP-REVIEW-01` remains a fresh, read-only
  `software-code-review` child over 100% of the frozen final product diff.
- Fan-in node: N3 remains manager-owned and writes the minimal owner procedure,
  DEL-09-04 state/evidence, manager return, and handoff after N1-R2 and N2 pass.
- Revised edge: `N1-R2 -> N2 -> N3`; no concurrent writes.
- Checks: N1-R2 runs focused tests and scope containment. After a zero-finding
  fresh review, N3 runs registered typecheck, full Vitest, build, App hold,
  root harness checks, plus applicable syntax/static boundary checks.
- Escalation points and exclusions are unchanged: no logout/login, no proof
  claim, no default/operator LaunchAgent action, no bootstrap/kickstart in the
  proof path, no launcher mutation, and no scope expansion.
