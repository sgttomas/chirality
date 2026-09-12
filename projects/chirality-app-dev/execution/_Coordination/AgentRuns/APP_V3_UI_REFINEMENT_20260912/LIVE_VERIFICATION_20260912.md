# UI verification gap closure

The owner requested direct service-stall, service-loss, renderer-reload, and
panel checks after the first package had completed. That package and its evidence
are preserved. A replacement build follows reviewed repairs and merge.

## Setup and boundaries

Initial product basis: `85f19f019589b798331c804c4b206e34849eeab5`.
The supplied development launcher's source checkout has identical product files
at `cca1c652b793d0aed47516946f942a47f877d734`. No product edits were present
there. The owner-provided launcher and isolated spike-a2 profile/socket were used.
Computer Use operated the renderer at `http://localhost:3000`. The account UI
reported Signed in and Ready to work. No credentials, profile contents, saved
event files, trial installations, or owner project documents were inspected.

Service signals were limited to the Runtime child identified by launcher
ancestry, Electron parent, and an open `spike-a2.sock` descriptor. The test
commands used `/bin/sleep 70` followed by a unique printf marker, with explicit
instructions to execute once, read/write no files, and not delegate. Recorded
process output excludes lines containing `@`.

## Before repair

| Check | Direct observation | Disposition |
|---|---|---|
| Service stall | Owned service PID 45614, Electron parent 45609. SIGSTOP at 20:41:14Z, SIGCONT at 20:41:39Z. During the 25-second pause, sampled UI remained Working. Afterwards one action completed with STALL-CHECK-20260912; Completed, 77.1 seconds. | Defect: transport silence was not detected. No duplicate send observed. |
| Service loss | The same verified service received SIGTERM at 20:44:17Z during the LOSS-CHECK-20260912 turn. UI settled as Stopped, with one action and the sent message kept. | Defect: service shutdown was labelled as operator Stop. This was graceful SIGTERM, not an unhandled crash. |
| Loss replay | After stopping the owned dev command and relaunching through the supplied script, account remained Signed in / Ready. Reopening the chat still displayed Stopped, one user message, and an empty composer. | Confirms the misclassification also affects saved history. |
| Renderer reload | Reloaded during the RELOAD-CHECK-20260912 command. The running chat reattached, Stop was available, Send was disabled, and it completed with the marker, one action, and 77.8 seconds. | Pass. Replayed partial assistant commentary also appears in the continuing assistant bubble; retained as a presentation residual, not evidence of a second execution. |
| Panel at 1000 x 900 | With Navigator open, right panel constrained to 280 px; dragging stays at the permitted limit. With Navigator closed, dragging exercised 280 to 500 px. Expand/return and collapse/reopen worked. Six tab labels remained readable, wrapping when narrow. Tab entry, Right, End, Home, and Left wraparound moved focus and selection together. | Functional pass. Found an accessibility mismatch: constrained 280 px panel announced saved width 480 with min/max both 280. Repair included. |
| Panel at 760 x 900 | Stacked layout; right panel was 760 px wide and 520 px tall. Horizontal splitters are not present at this breakpoint. Collapse/reopen and expand/return worked. All six labels fit one row; keyboard Right, End, Home, and Left wraparound selected the expected tab with a visible focus outline. | Pass; horizontal dragging is not applicable to the stacked arrangement. |

Recorded logs: `/Users/ryan/.claude/chirality-build-ui-85f19f019-evidence/`
contains `live-dev-output.log`, `stall-signal.log`, `hard-loss-signal.log`, and
`live-dev-restart-1.log`. Browser observations above are direct UI evidence,
not conclusions from those process logs.

## Repair and recheck

The bounded repair separates Runtime stream byte health from model output and
from the App proxy's own keepalives. A real Runtime subscription clears
Reconnecting, and a lost observer never implicitly resends or interrupts work.
Recorded shutdown, restart, and operator-Stop causes remain distinct in live
display and replay. The panel correction reports its constrained visible width
while retaining the user's preferred widths for larger windows.

The fresh development launcher is
`/Users/ryan/.claude/chirality-build-ui-85f19f019-evidence/run-dev-recovery.sh`.
It changes only the source checkout and prepared instruction-root paths from
the supplied launcher; it retains the same isolated spike-a2 profile and socket.
No private profile file is read or modified directly.

| Recheck | Result |
|---|---|
| Repaired stall | Verified service PID 50646, parent 50641. SIGSTOP 21:03:42Z to 21:04:12Z. Observed Reconnecting, then the one RECOVERY-PASS-20260912 action completed, 80.5 seconds. |
| Healthy quiet recovery and reload | A sleep-120 turn with RECOVERY-LIVE-20260912 was paused from 21:05:20Z to 21:05:50Z. Afterwards Working was observed while the command still ran. Reload reattached with Stop available and Send disabled. Completed with one action, 125.9 seconds. The sampled second pause did not itself capture the brief Reconnecting interval; that phase was directly observed in the preceding recheck. |
| First shutdown repair attempt | SIGTERM 50646 at 21:08:23Z still produced Stopped, 39.6 seconds. Investigation reproduced that the supplier supplied a terminal without Runtime's shutdown reason. The coordinator now adds its known cause before both persistence and publication. |
| Complete shutdown repair | New verified service PID 54848, parent 54844. SIGTERM 21:13:33Z during SHUTDOWN-CAUSE-20260912. Failed, one action, 57.4 seconds; one kept user message and empty composer. |
| Shutdown replay | After restarting through the same development launcher and reloading the renderer, the chat retained its single sent message and showed Failed with “Chirality’s runtime stopped before this turn finished. Nothing was re-sent.” Account remained Signed in / Ready to work. No credential reset or resend was used. |
| Panel accessibility | At 1000 px with Navigator open, separator now announces 280, agreeing with the constrained panel. At 1440 px it restores preferred width 480. Prior direct six-tab/drag/collapse/expand checks remain applicable; layout calculations were preserved. |

Final checks after the coordinator repair: Runtime build passed; full Runtime
suite 34 files / 320 tests passed; full App suite 212 files passed, one skipped,
2175 tests passed and four skipped. Frontend typecheck passed. Logs are
`runtime-full-cause-final.log`, `frontend-full-cause-final.log`, and
`frontend-typecheck-recovery-final.log` in the evidence directory above.

The first full App run caught seven old fixture assertions. Known rejections
were modelled as generic transport errors, and two route fixtures did not expect
the added subscription notification. Typed rejection fixtures preserve every
draft/method/attachment assertion; an additional test covers ambiguous loss and
no resend. Original semantic event/cancellation assertions remain. The corrected
full suite passed. One neighboring Runtime restart-simulation test failed during
the author's combined focused run with STOPPED_DEGRADED and passed alone; it
also passed in the parent's final full suite. That intermittent observation is
retained as a residual, not declared fixed.

## Submission-identity verification

Candidate `cf3b1338b38c855bd2e92bf790076d6982f15678` preallocates the
Runtime turn identity before POST, attaches only to the matching retained turn,
and scopes replay to that identity. Regressions cover an old retained turn,
expired old history, a matching active stream, and matching completed replay.
These are controlled tests, not live network fault injection.

Parent Runtime build and full one-worker Runtime suite passed, 321 tests.
Frontend and Electron typechecks passed. The default-concurrency frontend run
had 2178 passes, four skips and one failure in the retained Pi/oMLX compatibility
fixture's 200 ms provider deadline. This source is outside the repair and Codex
package. A full one-worker run passed 2179 tests, four skipped. The load-sensitive
failure remains recorded, not declared fixed. Logs are
`runtime-build-identity-final.log`, `runtime-full-identity-final.log`,
`frontend-typecheck-identity-final.log`, `frontend-full-identity-final.log`, and
`frontend-full-identity-serial.log` in the evidence directory.

The same isolated dev launcher ran source cf3b1338b with wrapper 61091,
concurrently 61116, Electron 61237 and Runtime 61241, verified by ancestry and
the spike-a2 socket. Account remained Signed in / Ready. A new sleep-70 turn
started the IDENTITY-RELOAD-20260912 command at 21:37:34Z. After renderer reload,
the running turn reattached with one Stop control and Send disabled. The command
finished at 21:38:44Z; direct UI inspection at 21:39:06Z showed Completed, the
correct marker, one action and 77.3 seconds. No second POST or command was
observed. Partial commentary is still shown twice after reload, as previously
recorded. The owned concurrently process was stopped at 21:40:20Z after a fresh
working-directory check. Its recorder exited 0. Filtered dev log:
`dev-identity-reload-filtered.log`.

The independent full-diff review still found a plan-attempt persistence gap,
recorded verbatim in `returns/REVIEW_LIVE_RECOVERY_2.md`. The ordinary live
reload pass does not establish that this plan-specific failure is resolved.
That bounded repair and its review precede integration and replacement packaging.

## Owner update test status

The install-over acceptance remains unperformed. `OWNER_HANDOFF_20260912.md`
will carry the six manual steps and both complete installer paths. A source
restart, live recovery, or offline inventory test is not an install-over test.
