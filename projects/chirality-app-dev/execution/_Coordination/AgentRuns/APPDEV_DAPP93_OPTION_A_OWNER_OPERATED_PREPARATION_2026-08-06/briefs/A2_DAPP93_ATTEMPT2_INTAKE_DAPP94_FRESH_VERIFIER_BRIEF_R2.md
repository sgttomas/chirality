# Sealed brief R2 — attempt-2 intake and D-APP-94 successor verifier

Role: genuinely fresh, read-only ephemeral Agent 2 adversarial verifier.

Objective: independently verify the bounded successor repair after predecessor
verifier BLOCK `03470896a831523f4f72b45222662fe61efe44ecaba0d045b3a5f11503f40ded`.
Return PASS or BLOCK. Do not repair or delegate.

Sole permitted write:
`reviews/A2_DAPP93_ATTEMPT2_INTAKE_DAPP94_FRESH_VERIFIER_RETURN_R2.md`.

No other file/state change and no runtime, process inspection, signal, package,
helper/GUI, keychain, credential, product, Git, Task Management, or foreign-loop
action is permitted.

## Candidate identities

- intake freeze:
  `R4_4_6_ATTEMPT2_INTAKE_FREEZE.md` SHA
  `8e318cdf39cc2eba5be6f565fb8cf829ee557fecc6fd93b0290e31c14802067a`;
- D-APP-94 freeze:
  `DAPP94_DECISION_PACKET_FREEZE.md` SHA
  `4644beb0068357d9598d9dc990d473a51cb7398d27ef9c6def80981c94a5e31f`;
- packet SHA:
  `87c26c6cab6c8f4928f7606632a208cb960b886527cf04f7191d5d0d4908687b`;
- register SHA:
  `5698122ebd7cdb8312b138d71c7c8439c3b2cf760f85fd9439825b8104f215ca`;
- repair record: compute and report its whole-file SHA.

## Checks

Re-run every material check in the predecessor brief. In particular:

1. Reproduce exactly 20 primaries, 20 paired sidecars, every sidecar, and the
   all-40 aggregate
   `97a9d3836b1b3a7557f4171f208a7ac55c4132a87d1a8ab956dc2fdef58c8110`.
2. Reproduce all 22 marker ranges/exits and terminal cut; confirm step 14 FAIL,
   step 15 DEVIATION, and STOP_INCOMPLETE.
3. Confirm the signature appears at the exact timestamp in both GUI stdout and
   stderr, and that the successor no longer claims otherwise.
4. Confirm the frozen form records R4.4.5 runbook SHA `6f825681...e5ac`, the
   R4.4.6 runbook is `9fda14d7...193d8`, and the mismatch is explicitly retained
   as a deviation without editing returned bytes.
5. Reproduce C1105-C1108 zero/zero exits, package output, launch identity,
   cleanup, rollback, C1141 emptiness, root absence, and C196/C197 non-use.
6. Confirm eight signal-path cells UNKNOWN and package/direct-child identity
   supported at launch only, without C1119/attach/signal credit.
7. Confirm D-APP-94 has one unique AWAITING_RULING row, neutral A/B/C choices,
   conditional A recommendation, preparation-only tokens, and a separate
   mandatory step-14 packet-repair gate before any future attempt.
8. Read the relevant safeStorage call-path surfaces enough to verify that A/B/C
   are plausible planning choices and no bypass is asserted as already proven.
9. Reproduce all initial identities again immediately before writing the sole
   return and report final stability.
