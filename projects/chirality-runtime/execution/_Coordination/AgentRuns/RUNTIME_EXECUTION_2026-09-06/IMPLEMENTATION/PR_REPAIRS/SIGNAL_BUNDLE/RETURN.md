# Signal fixture bundle repair return

Reproduced exact Dynamic require of child_process unsupported failure in focused runtime-daemon-signal test (repro.log). Daemon barrel exports standalone, pulling unused Pi/cross-spawn CommonJS initialization into the fixture ESM bundle. Fixed only tests/fixtures/runtime-daemon-signal-child.ts: import RuntimeDaemon and installRuntimeDaemonSignalShutdown directly from their owning source modules.

Focused validation: 2 tests PASS, real SIGTERM/incomplete-request child test 2149ms (tests.log). Existing assertions retain 1900ms lower bound, 4000ms upper bound, exit0, STOPPED/listener restoration and socket/owner-file removal. No mocks, timeout changes, test assertion changes, product index changes, compatibility bypass, startup inventory workaround or build action. No live provider/supplier/account invocation. Approved socket/process test escalation only.

Source frozen for parent full-suite fan-in. OpenAI GPT-6 specialist; exact serving ID unavailable. Agent2 role instruction-asserted, not mechanically enforced. No authority move, Git commit or merge.
