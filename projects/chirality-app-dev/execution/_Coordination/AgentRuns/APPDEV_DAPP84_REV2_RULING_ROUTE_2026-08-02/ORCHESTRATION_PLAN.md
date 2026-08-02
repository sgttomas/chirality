# Orchestration Plan — D-APP-84 Revision 2 Ruling and Root Route

Status: `COMPLETE / VALIDATED`

RunID: `APPDEV_DAPP84_REV2_RULING_ROUTE_2026-08-02`

Version: `1`

Parent: `HELP_HUMAN` (`Agent 0`)

Manager: `HELPS_HUMANS` (`Agent 1`)

AcceptedBranchBasis: `codex/appdev-pi-agent2-capability-packet@fc06b3388de17dcd5fc65eb29bf77c7f551a64cc`

SelectedProposalSHA256: `59e3f668f742bc8e100630781da3be975c0c6861410d06ee2ed019d5c79cf5d9`

PreservedRevision1SHA256: `0f4ddfb3c71b1862225ce35430fc18b275588b2dfafbca7d884aaef524a9830e`

## Objective

Record the owner's exact D-APP-84 Revision 2 ruling, update only the D-APP-84
decision-register row, route the Root-owned consequences through one ordinary
coordination notice, validate the control-plane tranche with a fresh read-only
Agent 2, and append one minimal versioned App-loop receipt.

## Exact owner token

```text
APPROVE D-APP-84 REVISION 2: B1 + V1 + P1 + X1 + H1 + R1.
```

No omitted or broader authority is inferred.

## Work graph and ownership

The manager is the serialized integration owner for this control-plane stage.
It authors the ruling, register-row transition, Root notice, run records, and
receipt. A fresh Agent 2 receives read-only access after those outputs are
materialized and checks exact selection, hashes, links, containment, no-effect
boundaries, and receipt structure. The manager accepts or rejects the return
before closing this RunID.

## Write scope

- this RunID directory;
- `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/` for the
  separate D-APP-84 ruling and the single existing D-APP-84 register row;
- root `execution/_Coordination/` for one ordinary notice; and
- `projects/chirality-app-dev/loop/LOOP_RECEIPTS.md` for one receipt.

## Exclusions

No proposal-packet edit; authority, agent-instruction, source/runtime/frontend,
decomposition, deliverable, SCOPE_CHANGE, Task Management-register, parity,
historical-UNKNOWN, lifecycle, release, reliance, commit, push, or merge write.
Implementation remains held pending separate Root decisions/activation and a
later App SCOPE_CHANGE.

## Fan-in gate

Close this RunID only if the exact ruling token and selected semantics are
preserved, both proposal hashes are unchanged, the D-APP-84 row alone becomes
`RULED`, the Root notice is coordination rather than authority and contains
harvestable `TM-CANDIDATE` lines without a register write, origin-main drift is
scoped-disjoint, the fresh Agent-2 return is accepted, and the receipt validator
passes after exactly one appended receipt.
