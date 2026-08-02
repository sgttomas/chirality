# Launch Brief — HELPS_HUMANS Ruling Recorder and Router

RunID: `APPDEV_DAPP84_REV2_RULING_ROUTE_2026-08-02`

BriefVersion: `1`

Parent: `HELP_HUMAN`

Role: `HELPS_HUMANS` (`Agent 1`)

## Objective

Act on the exact owner return
`APPROVE D-APP-84 REVISION 2: B1 + V1 + P1 + X1 + H1 + R1.` by recording
only that ruling and its required cross-loop control-plane route.

## Required reads

`AGENTS.md`; `agents/AGENT_HELPS_HUMANS.md`; D-APP-84 proposal Revisions 1
and 2; the App decision register; App loop receipt rules and latest valid
cursor; current Root Bash doctrine; Root DEL-02-06; and ordinary Root notice
conventions.

## Required outputs

1. A separate D-APP-84 Revision 2 ruling record with exact token, selected
   semantics, conditions, exclusions, and no-effect boundaries.
2. Only the D-APP-84 register row changed from `AWAITING_RULING` to `RULED`
   with a ruling link.
3. One ordinary Root coordination notice carrying the exact selection and
   requesting separate Root decisions/activation for generic per-run sandbox
   semantics, the native primitive contract, Pi `0.82.0` concordance,
   compatibility/sandbox identity and resume, DEL-02-06, and any successor to
   the current full-root plus serialized Bash rule. Use `TM-CANDIDATE` lines;
   do not write a Task Management register.
4. Versioned RunID records and one minimal App-loop receipt.

## Constraints

Preserve both proposal revisions byte-for-byte. Infer no implementation,
Root, SCOPE_CHANGE, lifecycle, release, parity, Task Management, historical-
UNKNOWN, or Git authority. Implementation remains held until Root acts and a
later App SCOPE_CHANGE is accepted. Validate origin-main drift as scoped-
disjoint and use a fresh read-only Agent 2 verifier.
