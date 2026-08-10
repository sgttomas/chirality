# D-APP-94 Option C feasibility-probe packet R3 signal-continuity overlay

Status: `FROZEN R3 SUCCESSOR CANDIDATE — OWNER APPROVAL AND NEW FRESH VERIFIER PASS REQUIRED`

Accepted R2 overlay:
`OPTION_C_FEASIBILITY_PROBE_PACKET_R2_RESTORATION_GUARD_OVERLAY.md`, SHA-256
`4472af19a4f7b9433052e21bb7efca747cdbc42a58c5d9f9678e330da1a82a8f`.
Its predecessor bindings, commands, operands, order, evidence names, scope,
prompt rules, retention, cleanup order, exclusions, and lack of execution
authority remain unchanged except for the single ordering replacement below.

R3 repair authority:
`R3_SIGNAL_CONTINUITY_REPAIR_AUTHORITY_ADOPTION.md`, SHA-256
`24e7c061dd2952e25f578864ad79326afb118b10e28467f7c6ec21063970fabe`.

R3 driver:
`prepared/run-dapp94-option-c-probe-r3.zsh`, SHA-256
`91396b2549a4c93910864c513467dd79dc73d197659fe6299137d634e7134a3f`.

The complete semantic delta from R2 is exactly one adjacent-line reordering
after the `RESTORE_STATE` case validation:

1. execute `trap '' INT TERM HUP`;
2. then publish `RESTORE_STATE=IN_PROGRESS`;
3. then execute the unchanged first restoration command.

Thus operational signal handlers remain active while state validation chooses
the restoration owner; after validated entry, signals are ignored before
`IN_PROGRESS` becomes externally observable and remain ignored until the
unchanged `SUCCEEDED` or `FAILED` terminal publication. Every other R2 byte is
preserved.

Exact future owner-personal invocation, only if separately approved after the
new verifier PASS:

`/bin/zsh projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP94_OPTION_C_ISOLATED_KEYCHAIN_FEASIBILITY_PROBE_PREPARATION_2026-08-08/prepared/run-dapp94-option-c-probe-r3.zsh`

No command in this overlay, R2, or the predecessor packet was executed during
R3 preparation.
