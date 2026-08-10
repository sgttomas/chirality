# D-APP-94 Option C R3 signal-continuity fresh verifier return

Verdict: `BLOCK_DAPP94_OPTION_C_R3_SIGNAL_CONTINUITY`

Role: exactly one new genuinely fresh read-only ephemeral Agent 2 verifier.
Candidate execution: none.
Repair or delegation: none.

## Findings

1. **PASS — R3 authority and immutable predecessor chain.** The R3 owner
   authority is adopted verbatim. The R2 freeze, R2 BLOCK return, R2 driver,
   both earlier freezes and BLOCK returns, all overlays, tokens, validations,
   owner-input objects, probe source, evidence contract, ruling/register, and
   external read-only identities matched their bound SHA-256 values on the
   initial and final checks. In particular, the R3 freeze is
   `fad857378c9184b576c98ff326cb63c0e28a4c37d0285138efd1c74216b0543f`,
   the R2 freeze is
   `5ab689e62c4e92074a8989a9de4ddfc7224aebcf55a4fe14704f463b89e4aecb`,
   the R2 BLOCK return is
   `fdab68863657a2093eaf21298a2a25589fbb7cf517b25dc1f9fe209d8936f0fb`,
   and the preserved R2 driver is
   `42d4206281afc0939f41c1bb03082162e4f3d978be8013e2edb37bb899f6a835`.
2. **PASS — exact authorized byte delta.** The complete unified R2-to-R3
   driver diff is one adjacent-line reorder: unchanged
   `trap '' INT TERM HUP` moves from immediately after to immediately before
   unchanged `RESTORE_STATE=IN_PROGRESS`. No other line, command, operand,
   namespace, order, evidence name, scope, or exclusion changes. The R3 driver
   is
   `91396b2549a4c93910864c513467dd79dc73d197659fe6299137d634e7134a3f`.
3. **PASS — the R2 published-state race is closed.** In an ordinary
   `restore_owner_state` entry that reaches the post-validation lines, ignore
   dispositions are installed before `IN_PROGRESS` is published and before
   the first restoration command. From publication of `IN_PROGRESS` through
   terminal `SUCCEEDED` or `FAILED`, INT/TERM/HUP stay ignored by the shell and
   inherited by restoration child commands. The exact R2 blocker between
   publication and ignore installation is therefore closed.
4. **BLOCK — trap-initiated pre-entry continuity remains open.** The unchanged
   `fail_closed_trap` begins with `trap - EXIT INT TERM HUP`, restoring default
   INT/TERM/HUP dispositions. It then evaluates state, may write two evidence
   lines, calls `restore_owner_state`, and that callee performs its case
   validation before reaching the new ignore command. Throughout this window
   `RESTORE_STATE` remains `NOT_STARTED`, but the operational handlers are no
   longer installed. During an EXIT-triggered restoration, one INT/TERM/HUP in
   that window can terminate the shell before owner-state restoration. During
   an INT/TERM/HUP-triggered restoration, a further such signal can do the
   same. Thus a signal before the R3 ignore does not necessarily use the
   unchanged operational handler to claim and complete the one restoration,
   contrary to sealed check 3.
5. **PASS — no double execution after ownership publication; BLOCK — entry
   continuity.** Only `NOT_STARTED` is admitted; `IN_PROGRESS` and `FAILED`
   reject, and `SUCCEEDED` returns without restoration commands. Ordinary and
   trap callers therefore cannot overlap or run the restoration sequence
   twice once ownership reaches the R3 ignore/publication boundary. The
   default-disposition gap before that boundary can instead terminate without
   any restoration, which remains a material reversibility failure even
   though it is not a double-restoration path.
6. **PASS — terminal failure and retention after entry.** Once the restoration
   sequence is entered, any unsuccessful mutation/re-observation/comparison
   publishes `FAILED` before return. EXIT cannot retry; the fixed root,
   isolated keychain, and evidence are retained; and no cleanup runs. The
   pre-entry default-signal termination in finding 4 can bypass this terminal
   publication, which is why the overall verdict remains BLOCK.
7. **PASS — terminal success and cleanup ordering.** A successful restoration
   publishes `RESTORED=1` and `SUCCEEDED` before operational traps are re-armed,
   before evidence copy, and before deletion. The restoration commands run
   exactly once on every path that reaches this terminal state.
8. **PASS — preserved operational boundaries.** R3 parses under `/bin/zsh -n`.
   The command identities, fixed namespaces, exact owner-state checks, isolated
   HOME comparison, evidence-return contract, prompt/cancel rule,
   no-credential classification, bare hash-bound Electron scope, failure
   retention, successful cleanup order, and all product/network/credential/
   reliance/Git/Task-Management/foreign-loop exclusions remain intact. The
   local archive remains 122090802 bytes at
   `ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28`,
   its 33968-byte Electron member remains
   `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`,
   and no hidden execution authority exists.
9. **PASS — mechanical R3 identities; BLOCK — continuity claims and token
   gate.** The R3 authority, overlay, token, validation, freeze, and driver
   hashes are mechanically accurate. The overlay/validation claim that
   operational signal handling remains continuous before the ignore is not
   accurate for `fail_closed_trap` because it resets those dispositions. The
   future R3 owner token remains unapproved, withheld, and not presentable
   under this verdict.

## Smallest material blocker

R3 moves the ignore command ahead of `IN_PROGRESS` inside
`restore_owner_state`, but the unchanged trap caller first resets INT/TERM/HUP
to default and only later reaches that ignore. A signal in this trap-entry
window can terminate the shell while the owner security domain is mutated and
before restoration begins. The exact R2 published-state race is closed, but
end-to-end fail-closed signal continuity is not. No repair or second verifier
is requested or performed.

## Final freeze stability

- R3 manager freeze:
  `fad857378c9184b576c98ff326cb63c0e28a4c37d0285138efd1c74216b0543f`;
- R3 driver:
  `91396b2549a4c93910864c513467dd79dc73d197659fe6299137d634e7134a3f`;
- R3 overlay:
  `f4ed4355fb68b95daa8a85e10fd16e33a430c477ab3a6c7295146798549d14fa`;
- withheld R3 token:
  `dc5833b46b18cf20f94330e6880ea6841cac0e2515546e8bc10e35cc8c61293d`;
- R3 validation:
  `f7f284c9c4ec2885f8becde25150c9d43c512ffecfec59696b0d402aa584d72b`;
- R3 authority adoption:
  `24e7c061dd2952e25f578864ad79326afb118b10e28467f7c6ec21063970fabe`;
- R3 verifier brief:
  `a00d7b73aba46aabe61eb34fc8c794f88f57bb628a0019e0acca46b488afcc48`.

All bound identities remained byte-stable through the final pre-return check.
