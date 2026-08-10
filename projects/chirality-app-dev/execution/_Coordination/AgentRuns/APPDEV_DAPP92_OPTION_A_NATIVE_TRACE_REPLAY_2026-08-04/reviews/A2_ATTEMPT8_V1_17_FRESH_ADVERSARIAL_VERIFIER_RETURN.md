# A2 Attempt-8 v1.17 fresh adversarial verifier return

Status: `COMPLETE`

Verdict: `BLOCK_PACKET_REPAIR_REQUIRED`

The v1.17 packet is not decision-ready. Its frozen top-level bytes reproduce
and all three scripts parse, but it still violates D-APP-92's mandatory
individual-enumeration rule and has terminal-path cleanup and evidence-freeze
defects. No proposed runtime command was executed.

## Frozen-byte and static checks

- Accepted R2 verifier:
  `ebb81fb33524eb68ef0a3435d5e594a17f13044420330570cbcf9b114955a2d8`.
- `COMMAND_REGISTER_AMENDMENT_V1_17_PROPOSED.md`:
  `94309f250bc5a8489c34e5328c920ff66c19a89a9c08e5e348fce76335be39df`.
- `ATTEMPT_8_REAL_RUNTIME_COMMAND_APPROVAL_REQUEST_R2.md`:
  `9bdb19de6944205435485350d7533b1a2d03646cb436005e4248a02803f0f5a4`.
- `real-runtime-controller-r2.mjs`:
  `6da4821fb04550af01e4deaf0c05c398f93267f1c75e7c764f660e50c8c02059`.
- `real-second-session-sentinel-r2.mjs`:
  `30f8bd60858a4c86fb7cb8ca0a4350b41b8c69ac78116c1d9fbcb2768c726213`.
- `real-runtime-cleanup-verifier-r2.mjs`:
  `690b1b10d0afa48fc9963d4e4722121032880b15b8eb97c5f53a5be2a298ba26`.
- Packet-02 return:
  `b88659a52763f166808ec5209e9df637429e26e59c515cae8293c8dd0b2049bd`.
- LLDB command file:
  `720ad198b99c45737564ed596147ca438e60586b5b5241cd6852a49838f245f8`.

All stated v1.17/request/script hashes match current bytes. `node --check`
passes for each of the three R2 scripts. The proposal has 41 unique top-level
rows: C336-C374 plus C196 and C197, each exactly once. C196's executable bytes
match v1.9; C197 preserves the same interrupt/detach/quit byte sequence and
does not add debugger commands. The fixed temporary root and proposed durable
evidence target are absent, and the frontend is Git-clean. No network
primitive appears in the three R2 scripts.

## Blocking findings

### 1. Critical — 44 commands are hidden behind five aggregate rows

D-APP-92 requires every tool and command to be individually enumerated in the
sealed brief before invocation. The verification brief expressly disallows an
aggregate row that points to commands in another proposal unless every
underlying full command is literally present and separately owner-gated in
v1.17. v1.17 fails this rule:

- C348 abbreviates v1.16 C261-C272: 12 `cp` commands;
- C351 abbreviates v1.16 C275-C281: one `rm` and six `ln` commands;
- C355 abbreviates v1.16 C286-C291: six commands;
- C358 abbreviates v1.16 C293-C298: six commands; and
- C372 abbreviates v1.16 C320-C332: 13 rollback/check commands.

Those 44 full commands are not literally present as separately identified
rows in v1.17. The requested owner token gates only C336-C374 and cannot cure
the missing individual enumeration. This defect alone requires packet repair.

### 2. Critical — internal tools and signals are not individually gated, and
the inventory is materially incomplete

C359 is one script-invocation row, while the controller executes multiple
`/usr/bin/env`, `/bin/ps`, `/usr/sbin/lsof`, `/usr/bin/stat`, and
`/usr/bin/shasum` commands. They are summarized in prose rather than assigned
literal, separately owner-gated command identities. The same defect applies
to the sentinel's five exact-PID subprocess commands and the controller's
individual `ChildProcess.kill` calls.

Worse, the inventory's statement that signals are only stale-helper
`SIGKILL`, final-helper `SIGTERM`, GUI `SIGTERM`, and bounded cleanup
`SIGKILL` is false. `runRegistration` contains two additional
`child.kill('SIGKILL')` paths when stdout or stderr exceeds 1 MiB. Those calls
are neither enumerated nor preceded by the promised PID/PPID/start/command/
text identity guard. This is an executable authorization mismatch, not a
documentation-only defect.

### 3. Critical — the registration direct child can escape every cleanup path

`runRegistration` creates an untracked direct child. It races that child with
a ten-second timer and helper exit, but on either losing path it neither
signals nor awaits the registration child. The handle is local to
`runRegistration` and is never passed into the final cleanup. Consequently a
registration timeout, helper exit, JSON/exit validation failure, or stream
overflow can leave that child running outside the claimed
`ALL_CONTROLLER_CHILDREN_REAPED` set. The cleanup receipt can therefore state
that all controller children were reaped while omitting a real controller
child.

### 4. Critical — one cleanup exception skips later owned children

The finalizer performs GUI, helper, and stale settlement inside one `try`.
Any exception from `waitSentinel` or the first `settleOwned` jumps directly to
the single `catch`; no `finally`-per-child or best-effort continuation settles
the remaining live handles. A natural GUI exit while waiting for `detached`
is itself raced as an exception and can therefore skip helper/stale cleanup.
Similarly, an identity race, rejected signal, or reap timeout for the GUI can
leave the helper untouched. This does not meet exhaustive cleanup on every
C359-or-later terminal path.

The stale-helper success path also uses an unbounded `await stale.exit`
immediately after `SIGKILL`. If the exit event does not arrive, the controller
never reaches its finalizer or emits the pre-controller cleanup-safe receipt.

### 5. High — the durable copy omits core raw protocol and trace evidence

C371 copies only
`/private/tmp/.../evidence/attempt8-runtime`. It does not copy the sibling
`protocol/` directory containing `controller.json`, `attach-started.json`,
`trace-ready.json`, `signal-armed.json`, `trace-live.json`, `detached.json`,
`replay-terminal.json`, or the pre-controller cleanup-safe receipt. C373 then
deletes all of those raw binding/ordering records.

The package transcript is also outside the copied subtree at
`evidence/attempt8-package.stdout-stderr.txt`, so it is deleted. No row freezes
C357's status-1/zero-byte network-scan result. Finally, neither the C196 LLDB
PTY transcript nor session-A transcript is copied to the durable evidence
target. The required sealed replay transcript, raw trace evidence, exact
identity binding, network-scan proof, and deviations therefore cannot be
returned from the specified graph.

### 6. High — the 150-second cap is a policy statement, not a mechanically
bounded LLDB process

The ready+139.5-second replay and ready+148.0-second detach targets have
internally coherent nominal arithmetic: attach occurs after ready, so a
successful detach by ready+148.0 seconds is inside 150 seconds from attach.
However, C196 itself has no timeout wrapper, and C366 only says to poll until
terminal. If C197 does not make LLDB terminal, the packet supplies no
enumerated operation that mechanically terminates the LLDB process at 150
seconds. The controller deadline only stops waiting for `detached.json`; it
cannot terminate C196. Thus the inherited absolute maximum is not guaranteed
on the failure path.

### 7. High — the detached sentinel does not prove detach or terminality

For `detached`, the sentinel deliberately performs no live identity check and
only writes a file. It does not verify that `attach-started.json` exists, that
C197 bytes were sent, or that the C196 PTY is terminal. C367's prose ordering
is the only link. Because the controller trusts this file to enter child
cleanup, a mistaken/out-of-order invocation can claim
`LLDB_DETACHED_AND_TERMINAL` while LLDB remains attached. A fail-closed
cross-session handshake needs an observable, bounded terminal proof rather
than an unverified assertion file.

## Prior-blocker disposition

- Live PID/PPID/start/command/text checks before attach and signal are present,
  but they do not overcome the unenumerated internal commands or unverified
  detach transition.
- Static-PID fallback signaling was removed, but exhaustive child cleanup is
  still false because the registration child is omitted and cleanup short
  circuits on the first exception.
- The stale child is outer-scoped, but its normal SIGKILL reap is unbounded.
- The nominal 139.5/148.0 timing arithmetic is improved, but the LLDB process
  itself remains mechanically unbounded on failure.
- C357 now performs a pre-runtime textual network-attempt scan, but its result
  and package transcript are not durably retained.
- Cleanup receipts now precede C371, but core protocol, package, scan, and PTY
  evidence remain outside the copied subtree.
- The mutation marker gives a coherent pre/post-mutation branch concept, but
  C372 still violates individual enumeration by importing 13 other-proposal
  commands.

## Required repair

Freeze a new proposal that literally lists and separately gates every
underlying command and internal executable/API action; accounts for and
reaps the registration child; settles every owned child independently even
after another cleanup failure; bounds stale reap and LLDB terminality;
mechanically proves the detached transition; and copies the protocol tree,
package/network-scan proof, both PTY transcripts, cleanup receipts, and all
other raw evidence before deleting the temporary root. Recompute every hash
and obtain another genuinely fresh adversarial verification.

No package, helper, GUI, LLDB, attach, signal, replay, credential, network,
product, release, Git, Task Management, or foreign-loop action was performed.
