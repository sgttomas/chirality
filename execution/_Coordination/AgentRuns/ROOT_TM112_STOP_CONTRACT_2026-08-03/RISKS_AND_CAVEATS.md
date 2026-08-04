# Risks and platform/version caveats

Status: `DERIVATIVE DECISION SUPPORT`

1. **Node version range.** Root declares Node `>=22.19.0`; executed N1 and the
   present local API inspection are Node v24.18.0 on macOS arm64. The later
   implementation must test the supported-floor behavior or narrow/qualify the
   support claim. Presence on v24 is not proof for every later Node release.
2. **Node connection classes.** `closeAllConnections()` is a force operation,
   not graceful drain. Both E1 v24.18.0 runs left an upgraded connection open,
   and the installed public declarations make no upgrade guarantee; this is why
   F1 keeps a daemon-owned socket registry. The present daemon exposes no upgrade
   route, but the registry prevents that assumption becoming a hidden future
   leak.
3. **Unix socket pathname.** N1 observed the socket pathname absent while
   `server.close()` and `RuntimeDaemon.stop()` were still pending. That is an
   environment-specific observation, not a portable completion signal.
4. **Interruption acknowledgement.** The core aborts its controller and then
   awaits engine interruption. A provider could acknowledge slowly or never.
   The proposed force boundary deliberately prevents that acknowledgement from
   holding transport shutdown open; this means forced process teardown can
   precede canonical terminal persistence in a pathological adapter. No current
   execution establishes 2,000 ms as sufficient for every real provider; it is
   a recommended product policy, not an empirical provider bound.
5. **Pre-identity Agent 1 stream.** A high-level run's manager session ID is
   learned from its first harness event. C1 latches early shutdown and retries
   canonical interruption only if identity becomes known before force. At force
   the latch expires with a recorded failure; later identity cannot trigger an
   interrupt into a new generation. A source that never yields identity cannot
   be canonically targeted through the current daemon-only seam.
6. **Timer precision.** Production grace is a semantic deadline, not a claim
   that an event loop under starvation executes a timer at an exact microsecond.
   Tests need a small observation tolerance while preserving the exact 2,000 ms
   production value. The additional 500 ms force-settle cap is also a proposed
   human policy, not an E1-derived Node bound: it may reject stop under severe
   scheduling delay even after sockets were forcibly destroyed.
7. **External process budget.** App evidence recorded an approximately 5.06 s
   launchd escalation in one scenario. It is not a Root contract or a portable
   deadline. G2 leaves empirical margin but cannot guarantee external delivery,
   Electron's quit funnel, or process-manager patience.
8. **App causality.** Root reproduced a mechanism, not the exact App R2 causal
   chain. Even an accepted repair requires App's own post-GUI first-signal parity
   rerun under TM-APP-036/D-APP-88 evidence requirements.
9. **Error aggregation compatibility.** Exact error type/message is an
   implementation detail unless the owner separately makes it public contract.
   The candidate fixes only the semantic consequence: attempt all cleanup,
   report failures, and remain fail-closed for restart after incomplete cleanup.
10. **Degraded stop recovery.** An interruption error with clean transport and
    metadata blocks reuse of the same daemon/runtime-service instance because
    application work may remain unresolved. Its operational recovery is
    process/runtime-service replacement. A cleanup failure instead has the
    explicit repeated-stop retry path.
