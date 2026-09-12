# TASK: diagnose live recovery presentation

Parent: HELP_HUMAN, direct App tester. Type 2: gpt-6-astra, medium, no delegation.
Read-only diagnosis while the parent completes the other native checks.

Read Root/App AGENTS and TASK. Work from this fresh checkout, source basis
85f19f019; subsequent commits currently contain build/hand-off records only.
Read the stream attach/reconnect tests and implementation, turn-phase,
turn-activity, live-work-store, chat-panel, and the Runtime client/service
stream/heartbeat path as necessary. No broad architecture study.

Direct observation: the supplied isolated dev launcher ran the identical
merged product source. The parent identified the service by its Electron
parent and spike-a2.sock descriptor, then SIGSTOP for exactly 25 seconds and
SIGCONT. During the suspension UI samples at roughly 10 and 20 seconds still
said Working. Reconnecting was not seen. The single sleep-70 command then
finished and the UI showed Completed, one action, duration 77.1 seconds.
Owner expects Reconnecting during the 20-30 second stall, Working after it,
and Completed at the genuine end. Diagnose the cause, whether the expected
bound is represented in current code, and the smallest sound repair. Distinguish
transport health from absence of model output. No short turn timeout or
interruption on observer disconnect is permitted.

Return exact source locations, a bounded change/test proposal, and any relevant
shared hard-loss/reload concern. Do not write or run tests/builds/Apps. Never
read identity/auth/token/binding/keychain/Codex-home/session/event files,
intro-rehearsal, or live logs. No security commands or process signals.
The parent will supply further direct findings before authorizing repairs.
