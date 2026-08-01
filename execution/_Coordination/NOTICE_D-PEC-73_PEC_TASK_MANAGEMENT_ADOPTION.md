# Notice — PEC Task Management adoption under D-PEC-73

**From:** PEC loop

**To:** Root loop / TASK_MANAGEMENT

**Date:** 2026-08-01

**Notice status:** ordinary coordination notice; never authority

## Decision and applied effect

The PEC owner ruled `D-PEC-73: O-A.` on 2026-08-01. The owning decision
record is
`projects/pec/execution/_Coordination/_DECISIONS/D-PEC-73_task_management_adoption.md`.

PEC has therefore minted its loop-owned Task Management register at
`_DomainEngines/pec/_TaskManagement/REGISTER.csv` with schema 1.0, the exact
25-column closure-capable header, and ID family `TM-PEC-<seq>`. It is
header-only at adoption. Option A leaves `_DomainEngines/pec/LOOP_INIT.md`
unchanged; TASK_MANAGEMENT is invoked on demand or on an owner-scheduled
routine.

No root row migrates. Live review found no root row deferred against this
adoption. Candidate harvest remains proposal-only until the PEC owner promotes
specific rows, and no PEC action writes the root register.

## Requested root-side disposition

The root loop may close `TM-ROOT-100` as `RESOLVED_BY_DECISION`, citing
`D-PEC-73` and this notice as evidence. That root-register disposition remains
the root owner's act under the root loop's instruments.

## Non-effects

This adoption opens no PEC P1 source work, WORKING_ITEMS activation,
implementation, lifecycle, release, cross-loop duty, or authority effect.
`D-PEC-72` was separately selected for packet drafting only and remains an
unruled source-work gate.
