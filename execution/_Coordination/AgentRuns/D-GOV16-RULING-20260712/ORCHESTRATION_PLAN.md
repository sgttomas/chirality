# D-GOV-16 Ruling Publication Plan

Status: `ACTIVE — PUBLICATION ONLY`
Date: 2026-07-12
Parent: `HELP_HUMAN`

## Objective

Publish and SHA-bind the owner's exact approval of D-GOV-16 items 1–10. This
run is a governance-publication boundary only. It must not apply the approved
TYPES/SPEC patches, move or convert deliverables, merge pilot branches, change
lifecycle state, refresh the Stage-2 census, or dispatch Stage-2 work.

## Accepted basis

- synchronized integration basis at run start:
  `main@2770fda4c63c98ee9f18cffbafd14c9aa59f497f` and
  `origin/main@2770fda4c63c98ee9f18cffbafd14c9aa59f497f`;
- closed Stage-1 branch state:
  `codex/sow-stage1-execution@6fcd1a6d06031b43a33d793064c8fb1f43457e63`;
- approved D-GOV-16 proposal snapshot:
  `31e5efd985db4cc7b25543e11a65933979e07e4f`; and
- owner direction, verbatim:
  "I rule APPROVED for D-GOV-16 items 1–10 exactly as proposed. Publish the
  ruling, then stop before Stage-2 implementation until a fresh governed
  orchestration plan is presented from synchronized main."

## Work graph

1. HELPS_HUMANS transcribes the ruling without changing any approved item.
2. Root validates authority, references, hashes, and prohibited-path
   containment.
3. CHANGE creates a scoped publication commit, then a binding commit that
   records the publication SHA in the decision and handoff.
4. Root verifies clean Git state and stops.

## Terminal gate

The terminal handoff must state `D-GOV-16_RULED_STAGE2_PLAN_REQUIRED` and name
the following release condition: a new governed orchestration plan derived
from a synchronized `main` that contains the published ruling. Approval of
D-GOV-16 is authority for the exact ten items; it is not this run's authority
to execute them.
