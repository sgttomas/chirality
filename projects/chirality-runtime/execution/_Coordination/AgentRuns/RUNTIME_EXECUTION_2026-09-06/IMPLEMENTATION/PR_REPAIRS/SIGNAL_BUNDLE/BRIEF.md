# Signal fixture bundle repair brief

Parent PR-closeout release: only tests/runtime-daemon-signal.test.ts and tests/fixtures/runtime-daemon-signal-child.ts plus this evidence. OpenAI GPT-6 specialist, exact serving ID unavailable; Agent2 instruction-asserted, not mechanically enforced. No product/index changes, Git, supplier/account/canary calls.

Observed registered-attempt-1 default suite failure: ESM signal child bundle loads transitive Pi/cross-spawn through daemon index/standalone export, leading to Dynamic require of child_process unsupported before fixture ARMED. Reproduce focused test, then narrow fixture imports to actual RuntimeDaemon and signal-shutdown modules used by this test, preserving real child process, request-held-open, SIGTERM, 2s production grace and 4s upper bound assertions. Do not mock signal behavior or broaden timeouts. Preserve production startup inventory semantics; if another startup issue remains, coordinate owning manager.
