# OD7-G3 AR-C — Authentication Reuse Deferral Candidate

**Status:** EXACT CANDIDATE — NOT ACCEPTED
**Candidate gate:** `OD7-G3-AR-C`
**Provisional PEC carrier:** `D-PEC-67`

## Exact candidate disposition

Defer the choice between a separate PEC service token and reuse of the Root
runtime project principal. Keep transport and access-class authoring
auth-provider-neutral. Keep `SOW-080` / `OI-006` open; no completed-auth,
security-completeness, or production-access reliance is permitted.

This deferral expires before the earliest of:

1. activation or acceptance of `DEL-08-01` as an authenticated service;
2. any non-test harness integration needing a PEC credential; or
3. any claim that PEC access control is complete.

At expiry, an exact credential candidate must identify ownership, issuance,
storage, audience, verification, rotation, redaction, and failure behavior.
This deferral neither authorizes credential reuse nor revives frozen v0.4 RBAC
or profile authority.

## Conditional write surfaces

- PEC decision record and register
- PEC open-item/coordination status surfaces that already carry
  `SOW-080` / `OI-006`

No Root credential contract, PEC service credential, PRD, decomposition,
ScopeOfWork, profile, or implementation write is authorized.
