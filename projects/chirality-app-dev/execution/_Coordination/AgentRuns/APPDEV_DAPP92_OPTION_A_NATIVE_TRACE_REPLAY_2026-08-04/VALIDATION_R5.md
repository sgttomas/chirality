# Validation R5 — D-APP-92 Option A Attempt 6 preparation

Status: `PASS_FOR_BOUNDED_TIMING_REPAIR_ONLY — REAL RUNTIME BLOCKED`

## Bound evidence

| Evidence | SHA-256 | Result |
|---|---|---|
| owner Attempt-6 approval adoption | `2f227cdc52e905b5bcd28c7c51801a23a77aed4dad3b3a19d9260bfa2cbfd41c` | exact token and exact C217-C230 fence |
| immutable command-register amendment v1.14 | `8d3adbcede92f812235406c11a68563e8fa2d52dc1bcf51ef2eba0bcbed07319` | bound proposed graph only |
| sealed Attempt-6 executor brief | `43863537562a254478b830ceec241b937ec7422d84a577c705c71109f9d58c32` | bounded Agent-2 contract |
| command outcomes | `0428fe13ef089deec333e67076f3a4530d4c4eebfa72789c7da7813cc79393f1` | complete C217-C230 disposition |
| no-target LLDB transcript | `34edf7ebf1466083e3a508db7d925e803f4222ec30696a26255ac2f66e86efac` | help/quit only; no target or attach |
| executor terminal return | `93c93a318f4ca715bc1454bfc8b0549c6b01089ac1fb1a68b4fd54f6ca8a420f` | stopped timing failure; cleanup pass |
| fresh adversarial verifier | `fed5aa422277720f2d74d8cfefe042f82ba76b7a8b05ac9d05889c143c91a5b5` | timing repair only; real runtime blocked |
| proposed v1.15 timing repair | `5f4d65f1c44caae38e7ae7499b2cff2c2e489338f67c2decb394f09c1f6677aa` | exact C231-C244 graph; unexecuted |
| Attempt-7 approval request | `f147259fef667d81285aaae25bd0909e22c59d00b176da4fdef6d0a6f1083061` | exact owner token; unexecuted |
| v2 controller script | `9a756a7eb272bcc270e3a482f2664b8290cffac5f236230ccf7a4dfe38ebb9c4` | syntax-clean, hash-bound candidate |
| runtime events | `0d661b044b2adf471ed7237de5b99f8cd970d85ed2e1ca86bb0f5172be44d9e7` | paired Attempt-6 closeout; execution timing limitation explicit |
| runtime summary | `39fa2c3d8b713566e968ae2c3f0be624d176ae133e819a20df6a3169fb01d0ad` | PASS; four paired sessions, no unmatched session |

## Accepted findings

- C217-C219 passed. LLDB opened with no target, returned only public
  `process attach` help, and exited cleanly on `quit`. No attach command, PID,
  privilege, or entitlement prompt occurred.
- C220-C224 passed individually. Session A froze direct-child PID `4457`;
  session B later wrote a schema-valid sentinel carrying the same PID.
- C225 correctly exposed the terminal stop: session A had already exited `1`
  because the five-second sentinel window expired before consumption.
- C226-C228 were correctly skipped because no successful protocol result
  existed. No retry was inferred or attempted.
- Mandatory C229-C230 passed. The fixed mock root is absent and frontend Git
  state is clean.
- Cleanup removed the ephemeral controller/sentinel bytes. Their reported PID
  and controller hash are therefore accepted only as mutually consistent
  executor/outcomes evidence interpreted through the frozen script semantics,
  not as independently recomputable live bytes.

## Gate disposition

The fresh verifier permits only a bounded timing/order repair. It does not
accept the mock handshake and blocks any real-runtime packet until a repaired
mock produces a bound result proving matching PID/sentinel, controller
consumption, and natural direct-child exit.

Proposed v1.15 changes only the mock controller. It durably emits an immediate
`ATTACH_READY` line, registers child exit before waiting, uses direct-child
`/bin/sleep 35`, permits a bounded 30-second sentinel window, rejects late or
post-exit acknowledgment, and requires a bounded no-bytes/no-signal session-A
terminal confirmation before root removal. A quiescence timeout blocks root
removal rather than deleting beneath a possibly live controller.
The existing second-session script remains byte-identical at
`02d651afbc13e7145de744977673aa54f4e9d7dd2411c06e2665537550ade11b`.
No C231-C244 command has run.

## Preserved state

C196/C197 remains separately approved but unused. No package/reconstruction,
cache seed, network, helper, GUI, real-process attach, signal, replay,
credential, memory or environment dump, process inspection, product remedy,
release, Git, Task Management, or foreign-loop effect occurred. D-APP-88 and
DEL-09-04 remain open; TM-APP-036 remains unfired.
