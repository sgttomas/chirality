# R7 — D-APP-93 owner trace evidence handoff (2026-08-11)

Status: `EVIDENCE LANDED; DISPOSITION RESERVED TO OWNER`

The owner froze and executed the D-APP-93 packet at aggregate SHA-256
`db704c969143dad9ddfe832fa630748e091cb8a9b1524bb3d30d28dc74c56f83`.
Step 0 passed, the LLDB trace completed with zero stop rules, and the capture
script bound the transcript. The exact evidence and records are preserved at
`execution/_Coordination/AgentRuns/APPDEV_DAPP93_OWNER_TRACE_2026-08-11/`;
the facts-only synthesis is `records/OWNER_TRACE_EXECUTION_RECORD.md`.

The trace records SIGTERM landing on `CrBrowserMain` in
`mach_msg2_trap` under the AppKit event loop while two accepted control-socket
connections were live. No Node/libuv/V8 signal-handler frames were present at
the stop instant. LLDB intercepted the signal with `PASS=false`, so the packet
did not test unintercepted signal processing. The helper was alive after
detach and continued serving.

This handoff does not close DEL-09-04 or D-APP-88, accept a remedy, change the
lifecycle or Checking Approval SHA, or decide the evidence's disposition.
Those acts remain reserved to the owner.
