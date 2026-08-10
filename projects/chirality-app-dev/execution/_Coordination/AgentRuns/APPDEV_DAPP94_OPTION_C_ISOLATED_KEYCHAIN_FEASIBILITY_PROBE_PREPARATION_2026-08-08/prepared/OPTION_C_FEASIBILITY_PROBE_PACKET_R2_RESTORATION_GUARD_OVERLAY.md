# D-APP-94 Option C feasibility-probe packet R2 restoration-guard overlay

Status: `FROZEN SUCCESSOR CANDIDATE — OWNER APPROVAL AND NEW FRESH VERIFIER PASS REQUIRED`

Accepted predecessor packet:
`OPTION_C_FEASIBILITY_PROBE_PACKET.md`, SHA-256
`f9674e9988e94c03473a20b54fac3efff099f30d1c0fad2b8f6d46b602f2e89b`.
Its evidence, scope, command operands/order, prompt rules, failure retention,
cleanup order, exclusions, and lack of execution authority remain byte-exact.

Owner repair authority:
`RESTORATION_GUARD_REPAIR_AUTHORITY_ADOPTION.md`, SHA-256
`6452e0e29e27915ad73e25572c3767491c79ae656450d981fcdc4331269428ab`.

This successor replaces only the predecessor driver identity and its
restoration/trap-guard description:

- successor driver:
  `prepared/run-dapp94-option-c-probe-r2.zsh`, SHA-256
  `42d4206281afc0939f41c1bb03082162e4f3d978be8013e2edb37bb899f6a835`;
- the single-owner state is `NOT_STARTED`, `IN_PROGRESS`, `SUCCEEDED`, or
  `FAILED`;
- only `NOT_STARTED` may enter restoration; repeated calls after `SUCCEEDED`
  return success without commands, and calls while `IN_PROGRESS` or after
  `FAILED` return failure without commands;
- restoration changes state to `IN_PROGRESS` before its first command and
  ignores `INT`, `TERM`, and `HUP` for the shell and restoration children until
  the complete mutation/re-observation/comparison sequence has terminated;
- success sets `RESTORED=1` and `RESTORE_STATE=SUCCEEDED` before normal signal
  traps are re-armed and before any cleanup;
- failure sets `RESTORE_STATE=FAILED` before normal signal traps are re-armed,
  so the following failure exit/EXIT trap cannot make a second attempt;
- EXIT/INT/TERM/HUP trap entry may initiate restoration only from
  `NOT_STARTED`; it never overlaps an ordinary caller and never deletes state.

Exact future owner-personal invocation, if and only if separately approved
after verifier PASS:

`/bin/zsh projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP94_OPTION_C_ISOLATED_KEYCHAIN_FEASIBILITY_PROBE_PREPARATION_2026-08-08/prepared/run-dapp94-option-c-probe-r2.zsh`

No command in this overlay or its predecessor was executed during repair.
