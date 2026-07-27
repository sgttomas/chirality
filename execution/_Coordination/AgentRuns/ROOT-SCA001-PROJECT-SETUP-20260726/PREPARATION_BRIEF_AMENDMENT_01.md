# PREPARATION Brief Amendment 01 — Variant-Aware ID Validation

Date: 2026-07-26
Parent: `PROJECT_SETUP`
Child: `PREPARATION`
Amends: `PREPARATION_BRIEF.md`
State: `EFFECTIVE`

## Trigger

Before writing any target file, PREPARATION ran:

```text
tools/validation/validate_id_format.sh DEL DEL-02-06
```

The helper returned:

```text
INVALID: DEL-02-06 does not match DEL format (^DEL-[0-9]{3}-[0-9]{2}$)
```

That helper implements the PROJECT three-digit package pattern. The accepted
Root decomposition is SOFTWARE and uses the two-digit stable form
`DEL-02-06`, with the exact full register/folder identifier:

`DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance`

The same accepted Root structure already contains DEL-02-01 through
DEL-02-05 under PKG-02.

## Amended validation instruction

Replace required action 2 in `PREPARATION_BRIEF.md` with:

1. Validate the numeric stable ID against the accepted SOFTWARE pattern
   `^DEL-[0-9]{2}-[0-9]{2}$`.
2. Validate the complete identifier and target folder name by exact equality
   with the revision 1.1 deliverable-register row.
3. Record `tools/validation/validate_id_format.sh` as not applicable to this
   Root SOFTWARE ID because its current DEL rule is PROJECT-only.
4. Do not edit the helper in this tranche. Route its missing variant support
   as a separate tooling observation.

## Unchanged authority and scope

This amendment changes no ID, name, parent package, write target, acceptance
criterion, lifecycle rule, dependency posture, or authorization. All original
brief prohibitions and output requirements remain in force.
