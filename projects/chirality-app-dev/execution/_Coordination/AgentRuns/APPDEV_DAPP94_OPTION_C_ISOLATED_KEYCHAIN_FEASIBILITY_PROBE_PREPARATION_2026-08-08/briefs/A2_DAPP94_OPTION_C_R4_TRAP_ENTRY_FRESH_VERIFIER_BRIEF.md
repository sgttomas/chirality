# Sealed brief — D-APP-94 Option C R4 trap-entry fresh verifier

Role: exactly one new genuinely fresh read-only ephemeral Agent 2 verifier.
Do not delegate, repair, or execute the candidate.

Sole write:
`reviews/A2_DAPP94_OPTION_C_R4_TRAP_ENTRY_FRESH_VERIFIER_RETURN.md`.

Frozen manager basis: `MANAGER_FREEZE_R4_TRAP_ENTRY.md`, SHA-256
`47d39a4512816adddae5def9f79453c9b7c724f08dcc4f406815314c85f646ef`.

No security/keychain command, process inspection, runtime, Electron launch,
GUI, credential, product, package, trace, network, Git, Task Management,
foreign-loop, or other execution action is permitted. Static file reads,
hashing, textual comparison, and `/bin/zsh -n` syntax parsing are allowed.

Verify all bound identities initially and immediately before return. Return
explicit PASS/BLOCK findings for:

1. verbatim R4 authority and preservation of the R3 freeze/BLOCK return/driver
   and the complete predecessor chain;
2. exact authorized delta only: in `fail_closed_trap`, R3's single
   `trap - EXIT INT TERM HUP` becomes `trap '' INT TERM HUP` immediately
   followed by `trap - EXIT`, with no other driver byte, command, operand,
   order, evidence, namespace, route, scope, or exclusion change;
3. EXIT-triggered entry ignores INT/TERM/HUP before any state/evidence/callee
   work, then removes EXIT reentry, and reaches the R3 restoration entry without
   an interruptible default-disposition window;
4. INT/TERM/HUP-triggered entry and repeated operational signals cannot exit
   the shell before restoration entry or interrupt restoration children;
5. ordinary restoration retains R3 signal-before-IN_PROGRESS continuity;
   ordinary and trap callers cannot overlap or execute restoration twice;
6. failure publishes `FAILED` before exit, EXIT cannot retry, all isolated
   state/evidence remain, and no cleanup occurs; success publishes
   `RESTORED=1`/`SUCCEEDED` before re-arming signals and before cleanup;
7. all prior PASS boundaries remain intact: syntax, command identities,
   namespaces, owner-state gates, evidence contract, prompt rule,
   no-credential classification, bare Electron scope, retention, cleanup order,
   exclusions, and no hidden execution authority;
8. R4 overlay/validation/freeze/token hashes and claims are exact; the future
   token remains unapproved and becomes presentable only on PASS.

Return `PASS_DAPP94_OPTION_C_R4_TRAP_ENTRY` only if the R3 trap-entry blocker
and all earlier restoration blockers are closed without scope drift. Otherwise
return `BLOCK_DAPP94_OPTION_C_R4_TRAP_ENTRY` with the smallest material
blocker. Do not repair or request a second verifier. Report the sole-return
SHA-256 after writing it.
