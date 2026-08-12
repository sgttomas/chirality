# D-APP-93 LLDB Trace Evidence Capture

This is a blank owner-fill form. Do not treat a blank field as a negative observation. Keep observed facts separate from interpretation.

## Run identity

- Owner/operator: Ryan C Tufts (owner), assisted by session minder (verification and command preparation only; all operative acts owner-performed)
- Date and time started: 2026-08-11 14:06 local (Step 0 preflight; MDT, UTC-6)
- Date and time completed or stopped: 2026-08-11 21:35 local / 2026-08-12T03:35Z (capture script bound transcript)
- Exact final frozen packet SHA-256 approved by owner: db704c969143dad9ddfe832fa630748e091cb8a9b1524bb3d30d28dc74c56f83
- Packet directory: /Users/ryan/dev/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_TWELFTH_PACKET_AUTHORING_2026-08-10/packet (main checkout at origin/main@43f89f96; six file identities re-verified against the owner freeze ruling manifest before execution)
- Evidence directory: /Users/ryan/dev/chirality-evidence/DAPP93_TRACE_20260811

## Host facts

- Host identifier: Ryan's MacBook Pro (Ryans-MBP)
- Operating-system version: macOS 26.6 (build 25G72)
- Architecture: arm64 (Apple silicon)
- Shell and working-directory facts: /bin/zsh interactive; trace terminal CWD = packet directory; runtime terminal CWD = rebuilt frontend in scratch worktree /Users/ryan/dev/chirality-dapp93-build (origin/main@43f89f96)
- Other relevant environment facts:
  - Target helper and GUI rebuilt from the frozen D-APP-88 R2 candidate source per the D-APP-92 register: all 12 candidate-source hashes reproduced the frozen SOURCE_MANIFEST.md values; current-main frontend baseline verified byte-identical to the D-APP-89 baseline before overlay.
  - Build toolchain: node v24.18.0 (mise), npm 11.16.0. Recorded deviations from the 2026-08-04 register: scratch-worktree rebuild location; owner-shell npm instead of the register's env-scrubbed /opt/homebrew/bin PATH (no homebrew node exists on this host); register row C037 (@chirality/policy projection) is stale — the package no longer exists and the projection used today's full @chirality symlink set into the main checkout; built .app binaries are not hash-identical to the 2026-08-04 replay's (builds are not byte-reproducible) — actual identities recorded below; fresh temp root /private/tmp/chirality-dapp93-trace-20260811.
  - Built artifact identities (SHA-256): helper app.asar 84fe57ddf9fd02690f2654ad521904bffa4792d69f973b6c9c89b33ef53c3c52; GUI app.asar 0b36e1dc64e2c5b958dbbd123b7dbec3806e4b10bda8354d54c648d1370700c0; helper Info.plist afd087f8c15e0b9c3ce9099ad19a293945a128c4b24e2b6c3c38db65e169d0e6. Helper and GUI Contents/MacOS executables hash identically (79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874) — both are the unmodified Electron shell binary; app identity lives in the asar archives.
  - desktop:pack chain: all steps passed; dependency-boundary verifier PASS; instruction-root integrity verifier initially received a stray "never" argument from npm passthrough (failed on unknown argument), re-run cleanly: integrity status pass, 43 files checked, source completeness status needs_remediation (recorded as observed).
  - Launches per register rows C044/C045: env -i PATH=/usr/bin:/bin:/usr/sbin:/sbin, HOME and CHIRALITY_USER_DATA under the temp root; helper --runtime-daemon (PID captured by launching shell), GUI --user-data-dir same temp user dir.
  - GUI keychain dialog "A keychain cannot be found to store chirality-runtime-helper Key" appeared under the scrubbed HOME; owner selected Cancel (no keychain change). GUI subsequently bound to the daemon (runtime.connectivity.state connected) after owner selected a working root; on the final relaunch it bound immediately with zero failed attempts.
  - GUI-daemon connection behavior observed: no persistent idle connection; connectivity supervisor polls on a ~10 s cycle holding each connection ~4 s. A raw silent client (nc) is closed by the daemon with HTTP/1.1 408 Request Timeout. A partial-HTTP-request client (headers never completed) is held ~60 s before 408 — used to guarantee live client connections at signal time.
  - Signal-time arming: SIGTERM was delivered while the helper held the listener plus TWO accepted client connections (GUI poll + partial-request holder), per pre-signal.lsof.helper.txt.

## Step 0 — exact commands and results

- Exact invocation: /bin/zsh ./scripts/OWNER_ENVIRONMENT_PREFLIGHT.zsh "$EVIDENCE_DIR" (from packet directory; EVIDENCE_DIR=/Users/ryan/dev/chirality-evidence/DAPP93_TRACE_20260811). A first attempt passed an empty argument due to a shell-expansion error in minder-prepared command text and was refused by the script's argument guard (exit 64, no writes); the corrected invocation ran once and passed.
- Exit code: 0
- Output path: /Users/ryan/dev/chirality-evidence/DAPP93_TRACE_20260811/STEP_ZERO_ENVIRONMENT_PREFLIGHT.txt (SHA-256 cda4b36b007ace33514a20479091a8053e6436c84f4cca36cca704878677f845)
- Output shape observed: five BINARY lines (expected=actual for all five), two PROBE lines (lldb exit 0 first_line lldb-2100.0.17.203; ps exit 0 numeric_output 26772), STEP_ZERO_RESULT PASS
- Step 0 overall result: PASS

### Actual binary identities

| Absolute path | Expected SHA-256 | Actual SHA-256 | Match |
| --- | --- | --- | --- |
| `/bin/zsh` | `528da649cc69510bd3c0bc565298cb602076b74a8ac3f18e793211b2a3c725e8` | `528da649cc69510bd3c0bc565298cb602076b74a8ac3f18e793211b2a3c725e8` | YES |
| `/usr/bin/lldb` | `44a68ddc1983d6cff3fd35ba3f9ba5f82004216f1dcde69892b3d1b06e408698` | `44a68ddc1983d6cff3fd35ba3f9ba5f82004216f1dcde69892b3d1b06e408698` | YES |
| `/bin/ps` | `a1d8c4a0a96fb6159f09d8f520f54df829db5f2eae9b9f3448e18f0bee61115c` | `a1d8c4a0a96fb6159f09d8f520f54df829db5f2eae9b9f3448e18f0bee61115c` | YES |
| `/usr/bin/shasum` | `0812595f981a26f813d98dc380af14d4af427626c9339eda29eb849ae13de1e3` | `0812595f981a26f813d98dc380af14d4af427626c9339eda29eb849ae13de1e3` | YES |
| `/usr/bin/perl` | `626702a74f85d2664872f6a7aa9b639306a2035211d442a24ea32ef0d48c8afd` | `626702a74f85d2664872f6a7aa9b639306a2035211d442a24ea32ef0d48c8afd` | YES |

### Probe results

- LLDB version command, exit code, and first line: /usr/bin/lldb --version, exit 0, first line lldb-2100.0.17.203
- Owner-side process-list command, exit code, and numeric output: /bin/ps -p $$ -o pid=, exit 0, numeric output 26772
- Any mismatch or variance: none. Developer mode was initially disabled on the host (attach denied with "Not allowed to attach to process"); owner enabled it via sudo DevToolsSecurity -enable before any operative act, verified by a scratch attach to an owner-launched node process. SIP restriction on debugging Apple platform binaries confirmed separately against /bin/sleep (attach denied; expected; not part of the trace).

## Target selected at execution time

- Owner-supplied target PID: 44712
- Pre-attach PID identity output: `44712 44492 ./dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service --ru` (command truncated by ps display width; full launch command recorded in the runtime terminal transcript; PPID 44492 is the launching zsh in the runtime terminal)
- Parent/process topology observed: helper PID 44712 and GUI PID 45065 both children of the launching shell; helper held listener FD 38u on /private/tmp/chirality-dapp93-trace-20260811/user/runtime/control.sock (pre-attach.lsof.helper.txt, SHA-256 ee0c1fb9ced1d8c289d1f95b800413b2772d2a0fa8a960cf87fd73a300864ded; pre-attach.lsof.gui.txt ca1e590194a35e3ebaf6ff3eebff64ce33c6f47f89017734744b03f8a8dc45f0)
- Basis for selecting this process: the helper launched directly by the owner per D-APP-92 register row C044 from the verified candidate rebuild, PID captured by the launching shell at launch ([1] 44712) and re-verified by /bin/ps immediately before attach

## LLDB transcript

- Transcript path: /Users/ryan/dev/chirality-evidence/DAPP93_TRACE_20260811/LLDB_TRANSCRIPT.txt
- Transcript SHA-256: 43763e06b4d3536f48713cfc5b5d4a69b496d3fd4057212b5da3694262740536
- Recording facility: /usr/bin/script (BSD script(1)); raw capture includes ANSI color escape sequences emitted by LLDB
- Attach command and exit/result: /usr/bin/lldb -p "$OWNER_SUPPLIED_PID" → process attach --pid 44712 → "Process 44712 stopped" (initial stop reason signal SIGSTOP, thread #1 CrBrowserMain); executable binary and arm64-apple-macosx architecture reported; attach succeeded
- LLDB signal-handling confirmation: process handle SIGTERM -s true -n true -p false → table row "SIGTERM false true true" (PASS=false, STOP=true, NOTIFY=true)

## Observed process, thread, and backtrace facts

- Pre-continue process status: Process 44712 stopped; thread #1 CrBrowserMain, queue com.apple.main-thread, stop reason signal SIGSTOP, frame 0 libsystem_kernel mach_msg2_trap+8
- Pre-continue thread list: 31 threads. Notable named threads: CrBrowserMain (#1), NSEventThread (#2), PerfettoTrace (#3), ThreadPool workers, Chrome_IOThread (#8), DelayedTaskSchedulerWorker (#10), V8Worker (#11–13), SignalInspector (#14, semaphore_wait_trap), NetworkConfigWatcher (#15, #17), CrShutdownDetector (#16, blocked in read), Chrome_InProcGpuThread (#20), Chrome_ChildIOThread (#21), NetworkService (#25), libuv-worker (#27–30)
- Pre-continue backtrace facts: thread #1 blocked in mach_msg2_trap under CFRunLoop → HIToolbox → AppKit -[NSApplication run] → Electron Framework frames; libuv workers idle in pthread_cond_wait; CrShutdownDetector in read; full backtraces in transcript
- Stop banner and reported stop reason: "Process 44712 stopped; * thread #1, name = 'CrBrowserMain', queue = 'com.apple.main-thread', stop reason = signal SIGTERM" (transcript line 272 after escape stripping)
- Thread that stopped: thread #1 (CrBrowserMain, com.apple.main-thread) — SIGTERM delivered to the main thread
- Process state after stop: stopped under debugger; signal intercepted, not forwarded (PASS=false)
- Thread state after stop: 32 threads. Thread #1 unchanged at mach_msg2_trap in the AppKit event loop
- Backtrace observations after stop: thread #1 backtrace identical shape to pre-signal (mach_msg2_trap under -[NSApplication run]); no Node/libuv/V8 signal-handler frames present on any thread at the stop instant
- Helper topology observations: post-stop deltas vs pre-signal — thread #31 now shows CoreAnalytics (anonymous namespace)::atExitHandler() executing os_transaction_create on dispatch queue 'com.apple.CoreAnalytics::Client Exit Queue' (previously an idle workqueue thread); new thread #32 present in libsystem_kernel getentropy under Electron Framework frames. Recorded as observed; no interpretation attached
- Signal-stop observations: signal delivered while helper held listener plus two accepted client connections (GUI poll connection and owner-held partial-HTTP-request connection), per pre-signal.lsof.helper.txt (SHA-256 cfa4128caa6108e6aaf29b264150c06b12fdf35d1f951f740d9d83d5be293d59). Signal source: /bin/kill -TERM 44712 from the runtime terminal (register row C054 form), guarded to fire only with a verified held connection

## Stop, detach, and cleanup

- Stop rule triggered (`none` or exact rule): none
- Point at which work stopped, if applicable: not applicable — full specified observation completed
- Detach command response: "Process 44712 detached"
- Quit response: LLDB exited to shell prompt without further output
- Post-detach PID identity output: `44712 44492 ./dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service --ru` — helper alive after detach (SIGTERM was never forwarded; expected)
- Transcript finalization evidence: script(1) reported "Script done, output file is …/LLDB_TRANSCRIPT.txt"; capture script bound path and SHA-256 into this record (final row below)
- Cleanup evidence: deferred by owner direction pending post-trace review; helper (44712) and GUI (45065) left running; scratch worktree and temp root retained
- Cleanup failure or variance: none at time of recording

## Unresolved variance or evidence gaps

- Variance: the approved aggregate SHA-256 was recorded into this form after the Step 0 preflight ran rather than before it (runbook Step 0 ordered recording first); the gap was identified and closed before any operative act, within the runbook's "stop before any operative act if the recording is incomplete" gate. The register's post-daemon socket-path expectation (runtime.sock / runtime.owner.json, row C049) does not match the current daemon's control.sock; recorded as register staleness, not a runtime defect. The transcript contains raw ANSI escape sequences from LLDB color output; content is intact (verified by escape-stripped search).
- Missing evidence: none against the runbook's specified observation set. Out of scope by design: the helper's behavior on an unintercepted SIGTERM (PASS=false suppressed delivery), and any JS-level handler execution — this trace pins delivery topology, not processing.
- Consequence for reliance: the trace evidences where SIGTERM lands (main thread, AppKit event loop) and complete thread state under held client connections. Conclusions about the D-APP-88 graceful-stop stall mechanism require pairing with the D-APP-88 log evidence and/or a future unintercepted-signal observation.

## Observed facts

- SIGTERM, delivered while two client connections were held open on the helper's control socket, was received by thread #1 (CrBrowserMain) blocked in mach_msg2_trap inside the AppKit/NSApplication event loop; no other thread stopped and no signal-handler frames appeared at the stop instant.
- The helper survived attach, intercepted SIGTERM, and detach; after detach the daemon answered the expired holder connection with HTTP/1.1 408 and the GUI reconnected (post-detach.lsof.helper.txt SHA-256 ee0c1fb9ced1d8c289d1f95b800413b2772d2a0fa8a960cf87fd73a300864ded: listener plus one re-established GUI connection).
- Step 0 environment identities matched the packet's pins exactly on the execution host.

## Owner interpretation

- 

The owner interpretation above is separate from the observed facts and does not replace the transcript or hashed outputs.

## Transcript identity row appended by capture script
LLDB transcript | path=/Users/ryan/dev/chirality-evidence/DAPP93_TRACE_20260811/LLDB_TRANSCRIPT.txt | sha256=43763e06b4d3536f48713cfc5b5d4a69b496d3fd4057212b5da3694262740536
