# D-PEC-04 - RULING: PEC profile Gate 2 remains open until pilot evidence

**Status:** RULED / O-B affirmed by owner.
**Date prepared:** 2026-07-05
**Decision ID:** D-PEC-04
**Prepared by:** PEC work loop agent under the standing PEC loop. The ruling act is the owner's (K-AUTH-1; D-GOV-04).
**Ruling SHA:** TBD - backfill to the commit publishing this ruling record.

## Decision ruled

Decide whether `_DomainEngines/profiles/pec.yaml` should be adopted at Gate 2
now, or remain DRAFT until the D-PEC-01 pilot evidence validates the operation
surface against real usage.

## Context

- D-T0-12 already affirmed the validator evidence path while keeping ADOPTED
  owner-only and Gate 2 open.
- `_DomainEngines/profiles/pec.yaml` currently declares `profile_status:
  "DRAFT"` and records that location under `_DomainEngines/profiles/` is not
  adoption.
- D-PEC-01 now authorizes a narrow pilot-only real-data rehearsal, but the
  exact owner-supplied basis is still pending.

## Human ruling

**Ruling:** O-B affirmed by owner (Ryan Tufts), 2026-07-05, in-session.

Owner ruling of record:

> Gate 2: O-B. Keep `_DomainEngines/profiles/pec.yaml` DRAFT with Gate 2 open. The pilot rehearsal is the event that validates the profile's operation surface against real usage; adoption comes after that evidence, not before.

This ruling keeps the PEC profile DRAFT. It does not alter D-T0-12's lifecycle
rule; it records the current Gate 2 timing decision for PEC.
