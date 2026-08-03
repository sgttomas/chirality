# DEL-02-06 amendment/activation handoff — TM-ROOT-108

Status: **PREPARED ROUTED HANDOFF — NO DELIVERABLE WRITE OR ACTIVATION**
Prepared by: Root TASK_MANAGEMENT
Addressee: the DEL-02-06 owning workflow / activated WORKING_ITEMS lane,
through the human or Agent 0
Owning register row: `TM-ROOT-108`

## Exact target concern

The generic runtime records `turn.accepted` before terminal evidence but does
not reconcile accepted, unterminated turns across daemon restart before new
admission or model activation. This can lose drain accounting and violate the
exactly-one-terminal-outcome claim.

## Requested amendment and evidence

Amend the DEL-02-06 runtime/activation work so restart recovery:

1. discovers persisted accepted turns lacking terminal evidence;
2. reconciles each turn idempotently to the ruled terminal/recovery state;
3. completes reconciliation before admission or model activation;
4. preserves audit and replay evidence across repeated restart/replay; and
5. proves drain accounting and exactly-one-terminal-outcome behavior.

Closure evidence must include the applied Root runtime change and executable
restart/replay evidence demonstrating idempotence. Present source bytes or a
design-only record are insufficient.

## Basis

- Inbound report:
  `execution/_Coordination/NOTICE_D-APP-85_C06_DAEMON_RECOVERY_ROOT_ROUTE_2026-08-02.md`,
  SHA-256 `0b34cefdc9abd5927db1b6bdda07225c37c42806ff5b3f946bb182227f08dc41`.
- Owner ruling:
  `execution/_Coordination/_TaskManagement/RULING_2026-08-02_ROOT_HARVEST_SLATE.md`,
  SHA-256 `9fde04e411f1839c6b37ae09e7fba0e8b60a6dd54e434b2bbf2d570e854520d8`.

## Nine-domain completeness scan

| Domain | Handoff result |
|---|---|
| Action Item | `TM-ROOT-108`; restart reconciliation is the exact concern. |
| Assignment | Human A remains unset; the DEL-02-06 owner/WORKING_ITEMS lane supplies R/S/C/I. |
| Prioritization | `TBD`; no priority was supplied in the promotion ruling. |
| Deliverables | DEL-02-06 runtime amendment and activation evidence. |
| Work | Implement recovery, tests, replay fixtures, and evidence capture. |
| Planning | Reconcile before admission/activation; coordinate any SCA effects from `TM-ROOT-107`. |
| Approval | Owning deliverable gates and human activation/acceptance instruments. |
| Checking | Restart/replay tests, repeated-run idempotence, drain accounting, exactly-one-terminal proof. |
| Decisions | Record any semantic choice in the owning decision instrument and return exact refs. |

## Return contract

Return change refs and SHAs, test commands/results, replay evidence refs and
SHAs, owning approval/activation refs, and unresolved blockers. TASK_MANAGEMENT
does not close `TM-ROOT-108` without owner acceptance of that evidence.
