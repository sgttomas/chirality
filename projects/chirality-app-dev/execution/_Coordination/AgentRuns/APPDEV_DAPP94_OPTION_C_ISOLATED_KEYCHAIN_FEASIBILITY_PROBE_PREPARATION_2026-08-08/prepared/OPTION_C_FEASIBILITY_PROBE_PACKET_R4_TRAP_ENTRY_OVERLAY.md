# D-APP-94 Option C feasibility-probe packet R4 trap-entry overlay

Status: `FROZEN R4 SUCCESSOR CANDIDATE — OWNER APPROVAL AND NEW FRESH VERIFIER PASS REQUIRED`

Accepted R3 overlay:
`OPTION_C_FEASIBILITY_PROBE_PACKET_R3_SIGNAL_CONTINUITY_OVERLAY.md`, SHA-256
`f4ed4355fb68b95daa8a85e10fd16e33a430c477ab3a6c7295146798549d14fa`.
Its predecessor bindings, commands, operands, order, evidence names, scope,
retention, cleanup, exclusions, and lack of execution authority remain
unchanged except for the exact trap-entry replacement below.

R4 repair authority:
`R4_TRAP_ENTRY_REPAIR_AUTHORITY_ADOPTION.md`, SHA-256
`66a6ec9178494d98d0c0fb86ae0b2a24e5900d1802c73ba3d3a1fad476cf52cb`.

R4 driver:
`prepared/run-dapp94-option-c-probe-r4.zsh`, SHA-256
`1d87db1d5f0d283a231c78dd8a84160844cc28f0467dfa324b7eb9053f233538`.

The complete semantic driver delta from R3 is confined to
`fail_closed_trap`: replace `trap - EXIT INT TERM HUP` with, in this exact
order, `trap '' INT TERM HUP` followed immediately by `trap - EXIT`. An EXIT-
or signal-triggered handler therefore ignores operational signals before any
evidence write, state check, or restoration call, while removing the EXIT trap
so a later exit cannot re-enter it. The R3 restoration function then retains
signal ignores before publishing `IN_PROGRESS` and through terminal state.
Every other R3 byte is preserved.

Exact future owner-personal invocation, only if separately approved after the
new verifier PASS:

`/bin/zsh projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP94_OPTION_C_ISOLATED_KEYCHAIN_FEASIBILITY_PROBE_PREPARATION_2026-08-08/prepared/run-dapp94-option-c-probe-r4.zsh`

No candidate command was executed during R4 preparation.
