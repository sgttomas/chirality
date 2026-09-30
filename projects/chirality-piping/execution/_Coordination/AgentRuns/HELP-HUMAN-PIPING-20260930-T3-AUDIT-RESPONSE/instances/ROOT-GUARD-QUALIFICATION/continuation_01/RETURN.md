# Additive qualification-controller cleanup repair

The independent reviewer reproduced an unexercised error path in the executed
v2 controller: an exception after SIGSTOP but before monitor.kill reaches a
finalizer that sends TERM to a stopped monitor, then raises TimeoutExpired,
skipping sentinel cleanup and result persistence. No recorded live run took
that path; the successful eight-case evidence and guard core remain valid.

`qualify_case_v3.py` preserves v2 and changes only final cleanup: a dedicated
helper kills its own unreaped direct monitor handle, which also works while
stopped. Each child cleanup catches and records its own failure so the sentinel
and result-write paths are still attempted. A sentinel that does not terminate
gets a fallback kill through its retained unreaped direct handle. Unconfirmed
cleanup remains an error; no latch is cleared and no discovered PID is targeted.

Five pure fake-handle tests cover stopped monitor, injected wait failure,
stopped sentinel fallback, already reaped children and missing handles. All
pass; no live fixture or process signal ran for this repair. The original
controllers, 93-entry packet, raw outputs and their hashes are preserved.
Future replay should use v3 after independent backcheck. This changes the
qualification controller only, not host_guard_v2.py or the direct-compile path.

Author: ROOT / HELP_HUMAN; reviewer remains the separate guard reviewer.
Source basis: current coordination fe6ca966259d29d8d6ed2f05460400f6cb5d5de0;
new files are sealed here before the next commit. No product code changed.
