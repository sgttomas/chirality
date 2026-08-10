# Sealed brief — fresh D-APP-92 ruling-adoption verifier

- Instance: fresh bounded ephemeral-generalist Agent 2
- Parent: `HELPS_HUMANS`
- Delegation: prohibited
- Tools: read-only repository inspection and hash/count commands
- Writes: none
- Accepted input: the owner's exact D-APP-92 Option A token

## Objective

Independently determine whether the current D-APP-92 ruling record, register
row, and execution-routing requirements adopt the owner's token exactly and
only, reproduce their content identities, preserve every operational fence,
and avoid execution or unrelated state effect.

## Required reads

- `AGENTS.md`
- D-APP-92 packet, ruling, and decision-register row
- Receipt 119
- DEL-09-04 `_STATUS.md`
- TM-APP-036 current register row
- this run's `ACTIVATION.md` and `EXECUTION_BRIEF_REQUIREMENTS.md`

## Assertions

1. The exact owner token is transcribed without amendment.
2. The packet and ruling hashes cited by the unique register row reproduce.
3. Exactly one D-APP-92 register row and exactly one ruling record exist.
4. The ruling and register preserve all required operational boundaries:
   diagnostic-only; exact source-aligned uninstrumented replay; individually
   enumerated command/tool list in a sealed brief; separate pre-invocation
   command-level approval for elevation/privilege/entitlement; no persistent
   entitlement/SIP/security/signing/admin grant; no credential access;
   unchanged mandatory first-signal gate; and no automatic product remedy,
   acceptance, closure, release, or reliance effect.
5. D-APP-88 and DEL-09-04 remain open and TM-APP-036 remains unfired.
6. The routing requirements are sufficient for a later WORKING_ITEMS sealed
   brief but do not execute or widen the ruling.
7. The adoption write set contains no product/frontend, Task Management,
   foreign-loop, release, reliance, or Git effect.

## Return contract

Return `ACCEPT` or `REJECT`, every finding with severity, independently
reproduced hashes and uniqueness counts, and any required correction. Do not
rely on parent claims; inspect actual bytes.
