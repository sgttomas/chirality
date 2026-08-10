# R4.4.6 attempt-2 dispositions and causal matrix

Status: `STOP_INCOMPLETE — EIGHT SIGNAL-PATH CELLS UNKNOWN; LAUNCH IDENTITY SUPPORTED`

- Steps 1-13: derived PASS for their returned operation/output gates.
- Step 14: derived FAIL. C1116 reported both socket/owner paths missing and
  marker exit 1; the frozen runbook required a stop on missing paths.
- Step 15: `DEVIATION`; it was entered after the step-14 stop condition, and
  its delayed PID capture is separately disclosed and addendum-bound. Returned
  evidence records GUI PID 93012, PPID 90439, and the exact executable.
- Step 16/C1118: `NOT_RUN`. The owner dismissed the “Keychain Not Found” modal
  with Cancel, entered no keychain credential, and attests no modification.
- Steps 17-22 and 24: `NOT_RUN`; C196/C197 and C1121 were unused.
- Steps 23, 25, 26, 28-31: derived PASS for this failure route.
- Step 27: derived PASS for truthful cleanup routing despite marker exit 1:
  A1129.H matched helper PID 92988 before exact helper cleanup; A1129.G returned
  zero rows after GUI exit, making GUI-target C1129 inapplicable.
- C1105-C1108: each exact sidecar is `command_exit=0`, `tee_exit=0` and has a
  complete output primary. Package preparation therefore passed before the
  later C1118 environment stop.

Immutable `gui.stdout.txt` and `gui.stderr.txt` both contain corresponding
records at `2026-08-08T05:57:26.027Z` matching the previously accepted
`Unknown project: chirality-app-dev` authenticated-contact signature. The form's
stderr attribution is supported. The records are supporting evidence only:
C1118 was not entered, they do not satisfy a future attempt's fresh C1118
owner-contact requirement, and they give no causal credit.

The completed form's runbook identity is stale: it records predecessor R4.4.5
SHA `6f825681...e5ac`, while executed R4.4.6 reproduces as
`9fda14d7...193d8`. The immutable mismatch is retained as a form deviation.

| D-APP-88 proposition | Status | Reason |
|---|---|---|
| SIGTERM reached native `__sigtramp` | UNKNOWN | C196/C1121 not run |
| libuv signal handler ran | UNKNOWN | no LLDB trace |
| Node SignalWrap callback ran | UNKNOWN | no LLDB trace |
| Electron quit path ran | UNKNOWN | no causal trace |
| App shutdown path completed | UNKNOWN | cleanup signals are non-causal |
| active GUI connection held Root stop pending | UNKNOWN | C1118 not performed |
| socket/owner removed after first signal | UNKNOWN | no first causal signal |
| GUI transport followed helper transition | UNKNOWN | no causal sequence |
| package/runtime identity matched frozen inputs | SUPPORTED AT LAUNCH | C1108 package, C1109-C1113 topology, C1115 helper identity, and A1117.ID GUI identity match; C1119 pre-attach revalidation was not run, so this grants no later attach/signal identity credit |

No D-APP-88, product, remedy, release, or reliance conclusion follows.
