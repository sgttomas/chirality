# R4.4.6 current-attempt cleanup-observation addendum

Status: `FROZEN CANDIDATE — OWNER TOKEN WITHHELD PENDING VERIFIER`

This addendum supplements only the active R4.4.6 current-attempt failure route.
It changes no prepared/frozen byte and preserves the exact C1128 and C1129
signal literals. The reported state—not a manager observation—is: preservation
has not started; `returned_r4_4_6/` is absent; helper PID 92988 remains alive;
the GUI is open; the fixed root/evidence and frontend candidate state remain;
C1117's launch literal ran, but its exact PID-capture line did not; `gui.pid`,
C1146.15, and C1146.16 are absent; and no later CONTROL input occurred.

## Delayed C1117 closure

The first new CONTROL input must be the byte-exact already-frozen C1117 capture
line:

`gui_pid=$!; printf '%s\n' "$gui_pid" > /private/tmp/chirality-dapp93-owner-operated-20260807/evidence/gui.pid`

It is lawful only because the owner attests that no CONTROL input and no other
background launch occurred after the C1117 GUI launch. Thus `$!` still denotes
that launch's direct child. Immediately enter unchanged C1146.15:

`d93_rc=$?; /usr/bin/printf 'DAPP93-CONTROL|STEP-15|command_exit=%d\\n' "$d93_rc"`

The form records step 15 `DEVIATION`. Step 16 is `NOT_RUN`; never enter
C1146.16. Then execute addendum observation A1117.ID exactly once:

`/bin/ps -o pid=,ppid=,command= -p "$gui_pid"`

Continue only if it emits exactly one row whose decimal PID equals `$gui_pid`
and `gui.pid`, whose PPID is the unchanged CONTROL shell, and whose command is
the exact frozen C1117 GUI executable/arguments. Any missing, extra, stale, or
mismatching row fails closed before preservation or signal.

## Distinct cleanup observations

These are new, read-only, exact-PID observations. They are not C1119 or C1125,
perform no search, and confer no causal credit.

- A1128.PRE, immediately before C1128:
  `/bin/ps -o pid=,ppid=,command= -p "$gui_pid"`
- A1129.H, immediately before the helper-target C1129 literal:
  `/bin/ps -o pid=,ppid=,command= -p "$helper_pid"`
- A1129.G, immediately before an applicable GUI-target C1129 literal:
  `/bin/ps -o pid=,ppid=,command= -p "$gui_pid"`

Each observation must emit exactly one matching run-owned row. Its signal may
follow only immediately, with no intervening input. A nonzero, absent, extra,
or mismatching result prohibits that signal and selects the existing
cleanup-failure retention route. C1128 remains exactly
`/bin/kill -TERM "$gui_pid"`. The helper C1129 remains exactly
`/bin/kill -KILL "$helper_pid"`; the GUI C1129, only if still applicable,
remains exactly `/bin/kill -KILL "$gui_pid"`.

## Complete future order

After delayed capture, C1146.15, and successful A1117.ID:

1. C1147.01, C1147.02, then immediate C1146.23.
2. C1150.R; C1151.T; C1148 with its outcome entered in the now-existing
   writable form; applicable produced/cleared C1149.01-C1149.17 in order;
   immediate C1146.25; then C1153.01 while its source remains live.
3. A1128.PRE, then immediately unchanged C1128; immediate C1146.26.
4. A1129.H, then immediately unchanged helper C1129. If the GUI fallback is
   applicable, A1129.G then immediately unchanged GUI C1129. Enter C1146.27
   immediately after the last applicable step-27 input.
5. C1131-C1139 in order, then immediate C1146.28; C1140-C1141, then immediate
   C1146.29.
6. Only after all applicable return copies, PID cleanup, rollback, cleanup,
   and proof prerequisites succeed, C1142-C1143, then terminal C1146.30.
7. C1151.F and no further CONTROL input.
8. Outside CONTROL, C1152; C1154.03 first; C1154.02; applicable
   C1155.01-C1155.06; C1156.01-C1156.08; and C1157.01-C1157.04. C1154.01 is
   `NOT_RUN` because C196/C197 and an LLDB transcript never occurred.

No C1146.16-C1146.22 or C1146.24 is entered. No C1118-C1127, C196/C197,
C1144, C1130, causal signal, retry, alternate PID, or search is authorized.
Every occupied/prohibited/copy/identity/signal/rollback/cleanup/hash failure
retains state and follows the frozen fail-closed route without retry.
