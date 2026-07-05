# D-PEC-06 - RULING: seed.demo guard repair authorized

**Status:** RULED / O-A affirmed by owner.
**Date prepared:** 2026-07-05
**Decision ID:** D-PEC-06
**Prepared by:** PEC work loop agent under the standing PEC loop. The ruling act is the owner's (K-AUTH-1; D-GOV-04).
**Ruling SHA:** `3e4ba7543` - the commit publishing this ruling record (backfilled same-branch per the D-T0-10 / D-T0-17 precedent).

## Decision ruled

Decide whether to authorize a narrow code-change packet/PR for the `seed.demo`
guard gap recorded in the PEC profile and Receipt 6 / L1-evidence-02 manifest.

## Context

- `_DomainEngines/profiles/pec.yaml` records that `seed.demo` is destructive to
  the configured `PEC_DB` and is lawful only under explicit scratch/demo
  authority until repaired.
- Receipt 6 records the concrete tool gap: `projects/pec/tools/seed.ts`
  hardcodes the DB path and ignores `PEC_DB`, while the server honors `PEC_DB`.
- The PEC loop fences normally exclude writes under `projects/pec/tools/**`,
  so an explicit owner ruling is required before this code change can proceed.

## Human ruling

**Ruling:** O-A affirmed by owner (Ryan Tufts), 2026-07-05, in-session.

Owner ruling of record:

> seed.demo guard: O-A. Authorize the narrow code-change packet/PR. Rider: scope it to also fix the recorded tool gap that `tools/seed.ts:43` hardcodes the DB path and ignores `PEC_DB` (Receipt 6 / L1-evidence-02 MANIFEST) -- refusing non-scratch/non-demo targets and honoring `PEC_DB` are two sides of the same guard. Run it as a separate narrow PR after this ruling is accounted for.

This ruling authorizes a separate narrow PR after the ruling-accounting PR. The
authorized code scope is limited to making `seed.demo` honor `PEC_DB` and refuse
non-scratch/non-demo targets.
