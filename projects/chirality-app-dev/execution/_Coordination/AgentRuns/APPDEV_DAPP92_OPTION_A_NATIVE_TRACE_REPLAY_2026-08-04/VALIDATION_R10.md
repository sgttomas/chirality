# Validation R10 — D-APP-92 Attempt-8 v1.21 fresh-verifier stop

Verdict: `BLOCK_PACKET_REPAIR_REQUIRED`

## Frozen basis

- Receipt 129 remains historical and was not rewritten.
- The v1.21 manager freeze is immutable at SHA-256
  `2040199d4d8a3431c021086d9689da018fef45a47943716c5163667badd23789`.
- The fresh-verifier brief is immutable at SHA-256
  `ba31666c2a022e16fe8578bf990620370540aed3bb6026739fc0fe8654ac0cd9`.
- The genuinely fresh verifier return is immutable at SHA-256
  `8a765c15ac195661ec8e82da874fec5ef8981f083c135f6e02378673b82fe423`
  and returns `BLOCK_PACKET_REPAIR_REQUIRED`.
- The verifier reproduced every v1.21 identity on its first and final passes,
  reproduced C787's literal ordered list, and confirmed no v1.20/R5 drift.

## Material blocking result

The packet is not safe for owner presentation because four material defects
remain:

1. C1015 ignores the `Writable.end` completion callback's error argument and
   can falsely set `inputWriteCompleted=true`.
2. C847 compares selected parsed fields but does not bind exact accepted
   controller/attach-intent bytes or hashes; pre-`try` read/parse failure also
   cannot produce the promised typed fail-closed receipt.
3. LLDB stdout/stderr callbacks synchronously retain unbounded file and memory
   output on the timer event loop, so the +149,000/+149,900 ms cap is unproved.
4. C1066 enumerates exit 4 only for identity-unsafe failure, while the script
   also executes exit 4 for accepted-C1018/no-close.

The v1.20 child-`error` defect is repaired: `error` no longer resolves
terminal promises, and drained `close` is required for terminal-safe proof.
That partial repair does not cure the four blockers above. No prospective
owner token may be presented and no recursive repair follows in this manager
turn.

## Closeout checks

The following passed without executing a proposed R6 operation:

- exact C787-C1066 accounting: 280 unique contiguous rows;
- all ten R6 scripts: static `node --check` only;
- authority corpus v18 status with no drift;
- practitioner status and repo-wide self-check;
- 349-test practitioner-harness suite;
- candidate-whitespace validation against
  `7aada3fbadf340a07ef828cc18b350c8c01b517d`;
- `git diff --check`;
- exact frontend Git cleanliness;
- fixed temporary-root and durable R6 evidence-target absence; and
- App-only write containment.

Receipt validation is rerun after the single terminal Receipt 130 append.
Frontend runtime gates were not repeated because no product byte changed and
the entire R6 packet remains proposal-only. No runtime, package, cache,
network, helper, GUI, LLDB, attach, signal, replay, credential, cleanup,
rollback, deletion, release, Git, Task Management, or foreign-loop operation
was executed.
