# D-APP-94 Option C restoration-guard repair authority adoption

Owner authority adopted verbatim:

> AUTHORIZE D-APP-94 OPTION C PROBE PACKET RESTORATION-GUARD REPAIR ONLY — MAKE OWNER-STATE RESTORATION NON-REENTRANT ACROSS ORDINARY, EXIT, INT, TERM, AND HUP PATHS; ENSURE A SIGNAL DURING RESTORATION CANNOT INTERRUPT IT OR CAUSE A SECOND RESTORATION; PRESERVE EVERY OTHER FROZEN COMMAND, EVIDENCE, SCOPE, AND AUTHORITY BYTE; FREEZE THE SUCCESSOR AND DISPATCH ONE NEW GENUINELY FRESH READ-ONLY VERIFIER — NO KEYCHAIN, SECURITY, ELECTRON, PROCESS, RUNTIME, GUI, PRODUCT, PACKAGE, TRACE, CREDENTIAL, NETWORK, GIT, OR OTHER EXECUTION AUTHORITY

Adoption scope: prepare and statically verify only the successor restoration
guard, mechanically update its bound hash/cross-references, freeze it, and
dispatch exactly one new genuinely fresh read-only verifier. This adoption is
not authority to execute the probe or any candidate command.
