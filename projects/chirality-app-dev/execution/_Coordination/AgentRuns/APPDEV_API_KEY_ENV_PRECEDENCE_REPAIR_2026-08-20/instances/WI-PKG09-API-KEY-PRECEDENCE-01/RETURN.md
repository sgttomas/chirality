# Return — WI-PKG09-API-KEY-PRECEDENCE-01

RUN_STATUS: SUCCESS

## Outcome

N3 consumed the accepted PKG-04 and PKG-02 precedence repair, built a fresh
unsigned arm64 desktop artifact, and passed the fail-closed packaged-security
proof. The integrated behavior is persisted UI safeStorage, then canonical
`ANTHROPIC_API_KEY`, then compatibility `CHIRALITY_ANTHROPIC_API_KEY`, with a
non-secret `ui | env | none` source fact consumed by IPC without environment
re-inference.

## Accepted identities and proof

- Storage source: `d810b1ef79d528ee86d09b879d76f2c1e46dec1517d77c4d8749c8d0741444db`.
- Storage test: `c9cadac32f892613a3a0b3e3f9afb8200b14ab375408f5ea89c23e53b817dac4`.
- IPC source: `3293cbf15164105ac61f7cc7e34da66c5c12701823a6e302f90d59c385eed3cb`.
- IPC test: `818b7424ef1de3f4418486a4a7ae839cb837d84a23af6fdd73621f847d74b1a6`.
- Packaged subject: `1623b2971bcef5fc6a2ae80ce0baa747a6746e28a2b821cd1e6bf125574b4ce2`.
- DMG: `8e22c0976ada252f467ba55ece4395c27735f4eb0461d6cf8516f804032b519b`.

The unsigned distribution, packaged dependency boundary, 43-file instruction
root, safeStorage store/status/remove, encrypted owner-only blob, provider
isolation, renderer blocking, five TCP snapshots with zero non-allowlisted
outbound, clean GUI/daemon shutdown, stream closure, cleanup, and retained
secret checks all passed. The final scan covered 5,868 files with zero blocked
findings.

## Validation and review

- Focused: 3 files / 47 tests PASS.
- Full frontend: 150 files passed / one skipped; 1,174 tests passed / four
  skipped.
- Typecheck, build, practitioner harness 350, root self-check, and APP-HOLD
  integrity: PASS.
- Final APP-HOLD reliance: ALLOW for DEL-09-06 and DEL-09-04.
- Integrated Review 03: PASS, exact 98-path aggregate
  `7ea308cf90bac02a7c439c71d0f01d2024ecee2a90c1fc16cfd1f4fd95bc1959`,
  zero findings.

## Deliverable effects and boundaries

DEL-09-06 and DEL-09-04 remain `IN_PROGRESS`. Only the two named packaged-
security residuals were removed. Their compact assessment/status/memory/run-
record evidence is current to the proved artifact and is derivative of the
accepted product and raw host proof; it does not replace ScopeOfWork or
product truth.

No lifecycle transition, dependency or Checking Approval SHA change,
RunAtLoad, owner-machine deployment, signing, notarization, distribution,
publication, release, receipt, completion log, commit, push, PR, or merge was
performed.

MISSING: none

NEEDS_HUMAN_RULING: none

DEPENDENCY_NOTES: CHANGE may publish the exact reviewed tranche as one stacked
iteration after PR #586. Any product/test/proof/evidence byte change requires
proportional checks, a new frozen identity, and fresh review.
