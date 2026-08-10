# D-APP-94 Option C R4 trap-entry fresh verifier return

Verdict: `PASS_DAPP94_OPTION_C_R4_TRAP_ENTRY`

Role: exactly one new genuinely fresh read-only ephemeral Agent 2 verifier.
Candidate execution: none.
Repair or delegation: none.

## Findings

1. **PASS — R4 authority and complete immutable predecessor chain.** The R4
   authority adoption contains the owner authority verbatim and is
   `66a6ec9178494d98d0c0fb86ae0b2a24e5900d1802c73ba3d3a1fad476cf52cb`.
   The R3 freeze, R3 BLOCK return, R3 driver, all R3/R2/predecessor overlays,
   tokens, validations, freezes, verifier returns, briefs, authority adoptions,
   owner-input objects, ruling/register, probe source, evidence contract, and
   external read-only bindings matched their frozen SHA-256 identities on the
   initial and final checks. In particular, the R3 freeze remained
   `fad857378c9184b576c98ff326cb63c0e28a4c37d0285138efd1c74216b0543f`,
   its BLOCK return remained
   `08abcf32958ad2e4484f80626e1a9f5d74144dc0e24a1956776482f682ccb7d7`,
   and its preserved driver remained
   `91396b2549a4c93910864c513467dd79dc73d197659fe6299137d634e7134a3f`.
2. **PASS — exact authorized delta only.** The complete R3-to-R4 unified
   driver diff replaces only the single line `trap - EXIT INT TERM HUP` in
   `fail_closed_trap` with adjacent, ordered lines `trap '' INT TERM HUP` and
   `trap - EXIT`. No other byte, command, operand, order, evidence name,
   namespace, route, scope, or exclusion changes. The R4 driver is
   `1d87db1d5f0d283a231c78dd8a84160844cc28f0467dfa324b7eb9053f233538`.
3. **PASS — EXIT-triggered trap entry.** On entry from EXIT, the operational
   signal dispositions are still the armed handlers until the R4 first trap
   command atomically changes INT/TERM/HUP to ignore; there is no restoration
   to default dispositions. The next command removes EXIT re-entry before any
   restoration-state test, evidence write, or callee work. A signal arriving
   before the ignore command remains governed by an operational handler rather
   than a default disposition; that handler takes the same fail-closed route.
   Thus EXIT-triggered restoration reaches the R3 callee entry without the R3
   interruptible default-disposition window.
4. **PASS — operational-signal entry and repeated signals.** INT, TERM, and HUP
   handlers enter with all operational handlers still armed. The first R4 trap
   command ignores all three before state/evidence/callee work; signals after
   that command cannot interrupt the shell or its subsequently exec'd
   restoration children. A signal arriving before that command invokes an
   armed handler, not default termination; nested/repeated delivery cannot run
   an `exit` until the innermost taken handler has installed ignores and
   completed or terminally failed the one restoration. No operational-signal
   route can therefore exit through the former pre-restoration gap.
5. **PASS — ordinary restoration and single ownership.** R3's ordinary entry
   still validates `RESTORE_STATE`, installs signal ignores, and only then
   publishes `IN_PROGRESS`. A signal before ordinary entry ownership invokes
   the R4 handler, which claims and completes that restoration before its trap
   action exits; a signal after ignores is inert. Only `NOT_STARTED` admits the
   command sequence, `IN_PROGRESS|FAILED` reject, and `SUCCEEDED` returns
   without commands. Ordinary and trap callers therefore neither overlap nor
   execute restoration twice.
6. **PASS — terminal publication, no retry, and retention/cleanup ordering.**
   Any restoration-command or comparison failure publishes `FAILED` before
   returning. EXIT either was removed by the trap caller or observes `FAILED`
   and cannot retry; the isolated keychain, fixed root, and evidence remain,
   with no cleanup. Success publishes both `RESTORED=1` and `SUCCEEDED` before
   re-arming operational signals, before returned-evidence copy, and before
   isolated-keychain or fixed-root deletion. A later signal can no longer
   cause restoration re-entry.
7. **PASS — all preserved operational boundaries.** R4 parses under
   `/bin/zsh -n`. Command identities, fixed namespaces, literal owner target,
   owner-state byte-comparison gates, isolated-HOME boundary measurement,
   exact mutation/restoration scope, prompt-cancel rule, public empty-password
   and disposable generated-key classification, bare hash-bound Electron
   scope, bounded evidence and adjacent sidecars, failure retention, successful
   cleanup order, and all credential/product/package/trace/network/reliance/
   Git/Task-Management/foreign-loop exclusions remain intact. The fixed root
   and return destination were absent, the literal owner restoration target
   was present, the 122090802-byte Electron archive remained
   `ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28`,
   and the frozen archive identity preserves its previously verified 33968-byte
   Electron member at
   `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`.
   No hidden execution authority exists.
8. **PASS — R4 overlay, validation, freeze, and token gate.** The R4 overlay is
   `b206362710c48c38b5513a49803afbc05b2ed590974b7c1f94881605b8d30ee2`,
   validation is
   `dd4a5b34d5d3ac3ce85de8bf4e1b25661799a9adb634fcb0a0de5ec823d48c8b`,
   manager freeze is
   `47d39a4512816adddae5def9f79453c9b7c724f08dcc4f406815314c85f646ef`,
   and the withheld token is
   `8ebb438933c877bbfe131f783e08b6857c3c501f0e9260faad2a699cda2f6f97`.
   Their identities and claims are exact. The token remains unapproved; this
   PASS makes it presentable to the owner but supplies no execution authority.

## Closure verdict

The R4 trap-entry ordering closes the R3 pre-entry default-disposition blocker
without reopening the original double-restoration defect or the R2
signal-before-`IN_PROGRESS` defect. Restoration is single-owner,
non-reentrant, signal-excluded from the first claimed entry through terminal
publication, no-retry on failure, and restoration-before-cleanup on success.

## Final freeze stability

- R4 manager freeze:
  `47d39a4512816adddae5def9f79453c9b7c724f08dcc4f406815314c85f646ef`;
- R4 driver:
  `1d87db1d5f0d283a231c78dd8a84160844cc28f0467dfa324b7eb9053f233538`;
- R4 overlay:
  `b206362710c48c38b5513a49803afbc05b2ed590974b7c1f94881605b8d30ee2`;
- withheld R4 token:
  `8ebb438933c877bbfe131f783e08b6857c3c501f0e9260faad2a699cda2f6f97`;
- R4 validation:
  `dd4a5b34d5d3ac3ce85de8bf4e1b25661799a9adb634fcb0a0de5ec823d48c8b`;
- R4 authority adoption:
  `66a6ec9178494d98d0c0fb86ae0b2a24e5900d1802c73ba3d3a1fad476cf52cb`;
- R4 verifier brief:
  `ed2fb4ffc5cc3272556d0ca0c04a1952580e71566afda7700b72b10783c81d66`.

All bound identities remained byte-stable through the final pre-return check.
