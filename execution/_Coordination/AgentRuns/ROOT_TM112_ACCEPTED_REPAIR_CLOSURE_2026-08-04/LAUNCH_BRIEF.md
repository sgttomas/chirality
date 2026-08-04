# Launch brief — Root TM-ROOT-112 accepted-repair closure

RunID: `ROOT_TM112_ACCEPTED_REPAIR_CLOSURE_2026-08-04`

Parent: `HELP_HUMAN`

Manager: `TASK_MANAGEMENT` (Agent 1)

Invoking loop: Root

## Objective

Apply the exact lawful Root register consequence of the accountable human's
accepted TM-ROOT-112 final-hash repair: close and archive only `TM-ROOT-112`
as `RESOLVED_WITH_CHANGE`, then run mandatory final federation, validation,
staleness, and closure-echo checks.

## Authority and accepted evidence

- Signed return:
  `execution/_Coordination/AgentRuns/ROOT_TM112_IMPLEMENTATION_ACCEPTANCE_2026-08-04/OWNER_RETURN_TRANSCRIPT_2026-08-04.txt`,
  SHA-256
  `a10bda1c05fe1e1249a7efa266401ddf71752e4d9a8ab0448ec96251d5973046`.
- Acceptance-carrier manifest SHA-256:
  `73ae77fe496731987ea49170fad45a9d1297bc263c5ba1d8050631da58efcea2`.
- Exact accepted product hashes: `docs/SPEC.md`
  `647eee2d8e68da9d6a4f7935b781b6b98c874ba696c824dd6d6a8f6c1b8d6a7f`;
  `runtime/packages/daemon/src/runtime-daemon.ts`
  `224403008e5ff072f1f614801afe4cedba6d3ade3c000c90ce1602ae8e27ddf2`;
  `runtime/tests/daemon.test.ts`
  `c853f20726c8633207246a90e79ac89122b651a15e6e0f9976b15f1910acb352`.

## Write scope

- `execution/_Coordination/_TaskManagement/REGISTER.csv`, only the fields of
  `TM-ROOT-112` required to record human-ruled closure before archival;
- `execution/_Coordination/_TaskManagement/REGISTER_CLOSED.csv`, only the
  mechanical addition of that closed row through `taskmgmt archive`;
- the Root Task Management session report and Root Receipt 96; and
- this RunID.

No other register row, foreign-loop surface, product/candidate carrier,
lifecycle surface, Root `HANDOFF_STATE.md`, or Git operation is authorized.

## Acceptance checks

1. Mandatory preflight and final federation are `COMPLETE` over all canonical
   registers with zero register writes.
2. `TM-ROOT-112` alone moves live to archive and closes
   `RESOLVED_WITH_CHANGE`; every other row and field is unchanged.
3. Closure Notes preserve all three accepted hashes, accepted Node 24
   evidence, the Node 22.19 unexecuted gap, App-notice release, and every
   excluded claim.
4. Root counts become 23 live (`OPEN=12`, `DEFERRED=11`) and 99 archived.
5. Live/archive validation, transcript and product hashes, source/evidence
   staleness, closure echo, foreign-register containment, receipt continuity,
   and whitespace checks pass.
