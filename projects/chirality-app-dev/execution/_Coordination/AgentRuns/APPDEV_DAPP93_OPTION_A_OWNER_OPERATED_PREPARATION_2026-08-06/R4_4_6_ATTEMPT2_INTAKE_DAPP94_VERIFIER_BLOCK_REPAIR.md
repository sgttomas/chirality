# R4.4.6 attempt-2 intake / D-APP-94 verifier-block repair

Status: `BOUNDED DERIVATIVE SUCCESSOR — NO RETURNED-BYTE CHANGE`

Accepted predecessor verifier BLOCK:
`reviews/A2_DAPP93_ATTEMPT2_INTAKE_DAPP94_FRESH_VERIFIER_RETURN.md`,
SHA-256
`03470896a831523f4f72b45222662fe61efe44ecaba0d045b3a5f11503f40ded`.

The repair changes only derivative intake and decision-packet statements:

1. The `2026-08-08T05:57:26.027Z` `Unknown project: chirality-app-dev`
   signature is recorded as present in both immutable `gui.stdout.txt` and
   `gui.stderr.txt`. The completed form's stderr attribution is supported.
2. The completed form's runbook hash is explicitly calibrated as stale:
   predecessor R4.4.5 `6f825681...e5ac` was entered, while executed R4.4.6
   reproduces as `9fda14d7...193d8`. The form remains immutable; the mismatch
   is a deviation and independently prohibits PASS_COMPLETE.

The returned 40 objects remain byte-identical with ordered aggregate
`97a9d3836b1b3a7557f4171f208a7ac55c4132a87d1a8ab956dc2fdef58c8110`.
No runtime, process, keychain, credential, product, Git, Task Management, or
foreign-loop action occurred.

Successor freezes:

- intake: `8e318cdf39cc2eba5be6f565fb8cf829ee557fecc6fd93b0290e31c14802067a`;
- D-APP-94: `4644beb0068357d9598d9dc990d473a51cb7398d27ef9c6def80981c94a5e31f`.
