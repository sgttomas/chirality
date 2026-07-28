# OD6 V → D → R ordering and effect boundary

**Status:** `APPLICATION_CANDIDATE_ONLY`
**Order:** `OD6-V-A → OD6-D-A → OD6-R-A`

## Ordering rule

1. V-A is the first design basis.
2. D-A may be consumed only with the exact accepted V-A basis.
3. R-A may be consumed only with the exact accepted V-A and D-A bases.
4. Each consumer records every exact source and integral-artifact SHA.
5. Source drift, missing bytes, or a changed predecessor returns the later
   consumption gate rather than being silently reconciled.

## Effect boundary

These records preserve accepted design bases. They do not:

- make a compatibility identity effective;
- create a live contract or implementation requirement;
- initialize or activate DEL-02-06;
- establish affected clients or client obligations;
- prove compatibility, degraded-mode conformance, release readiness, or
  rollback eligibility;
- select or publish a release;
- authorize migration, implementation, activation, publication, or reliance.

The accepted DEL-02-06 ScopeOfWork, if later applied and initialized, remains
the standing Root carrier. These coordination records do not substitute for
that contract or any activation record.
