# D-APP-94 Option C R4 trap-entry repair authority adoption

Owner authority adopted verbatim:

> AUTHORIZE D-APP-94 OPTION C R3 TRAP-ENTRY REPAIR ONLY — IN fail_closed_trap, REPLACE trap - EXIT INT TERM HUP WITH SIGNAL IGNORE FIRST (trap '' INT TERM HUP) FOLLOWED BY EXIT-TRAP REMOVAL (trap - EXIT), SO EXIT- AND SIGNAL-TRIGGERED RESTORATION CANNOT BE INTERRUPTED BEFORE ENTRY; PRESERVE EVERY OTHER R3 BYTE, COMMAND, SCOPE, AND EVIDENCE CONTRACT; FREEZE R4 AND DISPATCH ONE NEW GENUINELY FRESH READ-ONLY VERIFIER — NO KEYCHAIN, SECURITY, ELECTRON, PROCESS, RUNTIME, GUI, PRODUCT, PACKAGE, TRACE, CREDENTIAL, NETWORK, GIT, OR OTHER EXECUTION AUTHORITY

Adoption scope: prepare and statically verify only the R4 trap-entry successor,
mechanically update its driver hash/cross-references, freeze it, and dispatch
exactly one new genuinely fresh read-only verifier. This adoption is not
authority to execute the probe or any candidate command.
