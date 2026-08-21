# Work graph amendment 04

- N2 review verdict: `FAIL`, two blocking P1 findings after verified hashes,
  scope, and 100% review of both frozen files.
- Finding F1: source revision is optional/falls back to `unavailable`, so an
  incomplete source identity can reach `PASS`.
- Finding F2: cleanup may `bootout` any loaded same-label service after capture
  identity mismatch, without first proving that the live job is the prepared
  proof-owned program/argv/executable.
- Disposition: reject frozen product diff 01. Dispatch fresh bounded remediation
  node `N1-R3 / A2-PKG09-LOGIN-PROOF-PREP-REMEDIATE-01`, sole writer to the
  exact two product/test files.
- Revised serial graph: `N1-R3 -> N2-R1 fresh full-diff review -> N3 manager
  gates/fan-in`. No concurrent writes.
- Remediation acceptance requires focused regression tests for both findings,
  all focused tests passing, syntax passing, and exact two-path containment.
- Authority, owner-act boundary, exclusions, and absence of host proof remain
  unchanged.
