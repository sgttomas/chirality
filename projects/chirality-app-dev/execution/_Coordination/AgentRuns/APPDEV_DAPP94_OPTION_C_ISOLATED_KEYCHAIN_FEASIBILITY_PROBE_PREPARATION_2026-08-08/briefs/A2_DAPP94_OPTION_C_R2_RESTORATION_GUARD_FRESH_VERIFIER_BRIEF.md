# Sealed brief — D-APP-94 Option C R2 restoration-guard fresh verifier

Role: exactly one new genuinely fresh read-only ephemeral Agent 2 verifier.
Do not delegate, repair, or execute the candidate.

Sole write:
`reviews/A2_DAPP94_OPTION_C_R2_RESTORATION_GUARD_FRESH_VERIFIER_RETURN.md`.

Frozen manager basis:
`MANAGER_FREEZE_R2_RESTORATION_GUARD.md`, SHA-256
`5ab689e62c4e92074a8989a9de4ddfc7224aebcf55a4fe14704f463b89e4aecb`.

No security/keychain command, process inspection, runtime, Electron launch,
GUI, credential, product, package, trace, network, Git, Task Management,
foreign-loop, or other execution action is permitted. Static file reads,
hashing, textual comparison, and `/bin/zsh -n` syntax parsing are allowed.

Verify every bound hash initially and immediately before the return, then
return explicit PASS/BLOCK findings for:

1. exact verbatim repair authority and preservation of the predecessor freeze,
   predecessor verifier BLOCK return, predecessor driver, and all unchanged
   predecessor-bound operational identities;
2. exact authorized delta only: the driver change is confined to the
   restoration state/guard and mechanically necessary helper/trap wiring; all
   non-guard commands, operands, order, evidence names, namespaces, routes,
   cleanup, and exclusions remain identical;
3. a single owner of restoration across ordinary, EXIT, INT, TERM, and HUP
   paths: only `NOT_STARTED` can enter commands; `IN_PROGRESS`, `SUCCEEDED`,
   and `FAILED` cannot enter commands again;
4. `INT`, `TERM`, and `HUP` cannot interrupt the shell or any restoration
   child command while state is `IN_PROGRESS` because their dispositions are
   ignored before the first restoration command and until the terminal state
   is published; no handler can exit the shell mid-restoration;
5. ordinary and trap callers cannot overlap; an ordinary restoration failure
   publishes `FAILED` before exit and the following EXIT trap cannot retry;
   trap-initiated failure likewise cannot retry;
6. success sets `RESTORED=1` and `SUCCEEDED` before operational signal traps
   are re-armed, returns exactly once, and precedes all evidence copy/deletion;
7. failure retains the isolated keychain, fixed root, and evidence and performs
   no delete/root cleanup; restoration failure remains exit `90`;
8. static syntax PASS and truthful unchanged-preamble, unchanged-post-guard,
   and ordered-restoration-command digest claims;
9. packet overlay, validation, freeze, and withheld R2 token bind only the new
   driver/path/hash and accurately preserve all other scope/authority bytes;
10. the exact future token is merely presentable if PASS, remains unapproved,
    and supplies no hidden execution authority.

Return `PASS_DAPP94_OPTION_C_R2_RESTORATION_GUARD` only if the original
non-reentrancy blocker is closed across every listed path without scope drift.
Otherwise return `BLOCK_DAPP94_OPTION_C_R2_RESTORATION_GUARD` with the
smallest material blocker. Do not repair or request a second verifier. Report
the sole-return SHA-256 after writing it.
