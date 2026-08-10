# D-APP-94 Option C fresh verifier return

Verdict: `BLOCK_DAPP94_OPTION_C_PROBE_PREPARATION`

Role: exactly one genuinely fresh read-only ephemeral Agent 2 verifier.
Candidate execution: none.
Repair or delegation: none.

## Findings

1. **PASS — freeze-bound identity.** Every object bound by
   `MANAGER_FREEZE.md` matched its frozen SHA-256 both at initial review and in
   the final pre-return recheck. The manager freeze remained
   `3ff6a6cd0b49d8a743578b03ab2274b57c9ea9811e1c1d64b16790b1f17a83ee`,
   the verifier brief remained
   `db0c3c53b00c945b5e4e14bd995481eef04dfef52679fa03ebd1c20c8ec42932`,
   and the exact driver remained
   `35ceb467a30bd3736c15958b3f99203a385b5f2e8a153c80478d3663dbd481f0`.
2. **PASS — owner capture.** Both exact authorized commands have complete,
   54-byte, one-line LF-terminated stdout objects and `0\n` exit-status
   objects. Each stdout is the literal one-element path/list
   `/Users/ryan/Library/Keychains/login.keychain-db`.
3. **PASS — pre-mutation gates.** The frozen driver byte-compares current
   default/search responses, requires the literal owner login-keychain path to
   exist before mutation, requires the fixed root and return destination to be
   absent, checks the frozen host, archive, executable member, and probe
   identities, and parses under `/bin/zsh -n`. The final static check found the
   login-keychain path present, both destinations absent, the archive at
   122090802 bytes with its frozen hash, and the executable member at its
   frozen hash.
4. **PASS — HOME boundary.** The driver compares isolated-filesystem-HOME
   observations with the accepted user-domain state and explicitly records
   that `HOME` alone does not change the user security domain.
5. **PASS — mutation scope.** The security mutations are limited to isolated
   create/unlock, sole user-domain search-list/default binding, literal owner
   restoration, and successful-path deletion of only the isolated keychain.
6. **BLOCK — restoration idempotence.** See the smallest blocker below.
7. **PASS — prompt rule.** No approval or credential input is permitted;
   `SHOWN_CANCELLED` routes immediately to restoration and failure retention,
   and the packet prohibits signal, retry, and process-inspection fallback if
   cancellation does not return control.
8. **PASS — material classification.** Literal `-p ''` is expressly classified
   as public zero-length mechanics, the fixed plaintext as a public constant,
   and any Electron-generated safeStorage key as disposable generated
   cryptographic probe state rather than an owner/provider credential.
9. **PASS — runtime scope.** The only candidate runtime is bare hash-bound
   Electron 43.2.0 with activation policy `prohibited`, no window, and no
   product, package, trace, C1114/C1117, C196/C197, or network path.
10. **PASS — evidence design.** The passing path retains bounded
    stdout/stderr/status, restoration, prompt, probe, and cleanup evidence,
    byte-copies every source primary, and creates adjacent whole-file sidecars,
    including for SHA-named primaries. Failure retains source state; a partial
    return cannot be reused because invocation requires the return destination
    to be absent.
11. **PASS — prohibited outputs/claims.** No environment, memory, Keychain-item,
    key, ciphertext, credential, owner-login-keychain item, product, causal,
    release, or reliance output or claim is authorized by the frozen packet.
12. **PASS — token boundary.** The withheld token binds only driver SHA-256
    `35ceb467a30bd3736c15958b3f99203a385b5f2e8a153c80478d3663dbd481f0`;
    it supplies no hidden execution authority and remains withheld under this
    BLOCK.

## Smallest material blocker

`restore_owner_state` does not set `RESTORING=1` around its ordinary calls from
`fail_after_mutation` or the successful path. Consequently, an `INT`, `TERM`,
or `HUP` arriving during an ordinary restoration sees `MUTATED=1`,
`RESTORED=0`, and `RESTORING=0`; the signal trap can enter
`restore_owner_state` a second time. Separately, if an ordinary restoration
fails and the driver exits `90`, the still-active `EXIT` trap sees the same
state and attempts restoration again. The guard therefore prevents recursion
only for restoration initiated by `fail_closed_trap`; it does not guarantee the
brief's required no-double-restoration behavior for all restoration paths.

This is a material reversibility defect in a user-domain default/search-list
mutation packet. The future owner-personal token must remain withheld. No
second verifier or repair is requested or performed.
