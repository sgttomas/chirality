# Sealed brief — D-APP-94 Option C R3 signal-continuity fresh verifier

Role: exactly one new genuinely fresh read-only ephemeral Agent 2 verifier.
Do not delegate, repair, or execute the candidate.

Sole write:
`reviews/A2_DAPP94_OPTION_C_R3_SIGNAL_CONTINUITY_FRESH_VERIFIER_RETURN.md`.

Frozen manager basis: `MANAGER_FREEZE_R3_SIGNAL_CONTINUITY.md`, SHA-256
`fad857378c9184b576c98ff326cb63c0e28a4c37d0285138efd1c74216b0543f`.

No security/keychain command, process inspection, runtime, Electron launch,
GUI, credential, product, package, trace, network, Git, Task Management,
foreign-loop, or other execution action is permitted. Static file reads,
hashing, textual comparison, and `/bin/zsh -n` syntax parsing are allowed.

Verify all bound identities initially and immediately before return. Return
explicit PASS/BLOCK findings for:

1. verbatim R3 authority and preservation of the R2 freeze, R2 BLOCK return,
   R2 driver, and complete predecessor-bound chain;
2. exact authorized delta: the R2-to-R3 driver diff is only moving
   `trap '' INT TERM HUP` immediately before `RESTORE_STATE=IN_PROGRESS` after
   state validation, without any other byte/command/operand/order/evidence/
   scope change;
3. signal-before-entry continuity: after a `NOT_STARTED` validation, ignores
   are established before `IN_PROGRESS` is observable and before the first
   restoration command; a signal before the ignore instead uses the unchanged
   operational handler while state remains `NOT_STARTED`, which may claim and
   complete the one restoration;
4. INT/TERM/HUP cannot exit or interrupt the shell or restoration child
   commands from publication of `IN_PROGRESS` through terminal
   `SUCCEEDED`/`FAILED` publication;
5. ordinary and EXIT/INT/TERM/HUP callers cannot overlap or run restoration
   twice; only `NOT_STARTED` enters, and the unchanged terminal states block
   later entry;
6. ordinary or trap restoration failure publishes `FAILED` before exit, EXIT
   cannot retry, state/evidence/keychain are retained, and no cleanup runs;
7. success publishes `RESTORED=1`/`SUCCEEDED` before re-arming operational
   traps, evidence copy, or deletion, and restoration commands run exactly
   once;
8. all prior PASS boundaries remain intact: syntax, command identities,
   namespaces, owner-state checks, evidence contract, prompt rule,
   no-credential classification, bare Electron scope, failure retention,
   cleanup order, exclusions, and no hidden execution authority;
9. R3 overlay/validation/freeze/token hashes and claims are accurate; the
   future token remains unapproved and becomes presentable only on PASS.

Return `PASS_DAPP94_OPTION_C_R3_SIGNAL_CONTINUITY` only if the R2 continuity
blocker is closed without scope drift. Otherwise return
`BLOCK_DAPP94_OPTION_C_R3_SIGNAL_CONTINUITY` with the smallest material
blocker. Do not repair or request a second verifier. Report the sole-return
SHA-256 after writing it.
