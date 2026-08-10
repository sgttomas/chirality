# Attempt-6 preparation command outcomes

- C217: `PASS`. `/usr/bin/xcrun lldb --no-lldbinit` started in a PTY with no
  target. LLDB printed `Could not load history file` and the `(lldb)` prompt;
  no privilege or entitlement prompt appeared.
- C218: `PASS`. Exact bytes `help process attach\n` returned public command
  help and another `(lldb)` prompt. No attach command or target was supplied.
- C219: `PASS`. Exact bytes `quit\n` terminated LLDB with exit code `0`.
- C220: `PASS`, exit code `0`; fixed mock root was absent.
- C221: `PASS`, exit code `0`; fixed mock root was created.
- C222: `FAIL_TERMINAL`. Session A created its controller record and direct
  child PID `4457`, then terminated with exit code `1` and exact error
  `exact second-session sentinel was not received within 5 seconds`.
- C223: `PASS`, exit code `0`; controller-record SHA-256 was
  `5b794e9a460b522e88910a40b77010e9fade519d042b3b131796ee64d4cbe535`.
- C224: `PASS`, exit code `0`; session B validated the controller record and
  wrote a sentinel carrying matching direct-child PID `4457` and state
  `SECOND_SESSION_ACKNOWLEDGED`.
- C225: `FAIL`; the polled C222 session was already terminal with exit code
  `1`. The matching sentinel was not consumed within the controller's frozen
  five-second window. No retry or causal inference beyond this order evidence
  is made.
- C226-C228: `NOT_EXECUTED_STOP_CONDITION`; no protocol result existed to copy
  or hash.
- C229: `PASS`, exit code `0`; mandatory cleanup removed only the fixed mock
  root.
- C230: `PASS`, exit code `0`; fixed mock root absence was proven.

The mock child natural-exit condition was not established by a protocol
result. No target, attach, privilege or entitlement prompt, package, cache,
network, helper, GUI, signal, replay, credential, release, Git, Task
Management, or foreign-loop action occurred.

The only supported repair candidate is timing/order preparation: increase or
otherwise safely coordinate the mock controller's sentinel wait so session B
can acknowledge within the bounded window despite orchestration latency. This
is a candidate only; no retry or command amendment is authorized here.
