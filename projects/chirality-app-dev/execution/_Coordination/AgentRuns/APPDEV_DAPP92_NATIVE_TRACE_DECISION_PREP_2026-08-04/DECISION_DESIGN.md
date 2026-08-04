# Decision design — D-APP-92 native trace and replay

## Classification

This is an owner-class near miss under the standing App delegation instrument.
The proposed causal proof requires a new native tracing/tool surface and may
encounter macOS privilege or entitlement gates outside the current D-APP-88
authorization. Agent decision latitude stops before granting that exposure.

## Options

### A — bounded interactive trace plus sealed replay

Authorize a diagnostic-only tranche in an interactive macOS GUI session. It
reconstructs and seals the exact uninstrumented candidate/replay inputs, uses
only individually enumerated read-only native tracing commands, obtains any
required command-level privilege approval separately, and captures PID/time-
bound OS/libuv/Electron/teardown/Root-stop evidence. No credential value may
be accessed or recorded. This is the only option able to seek causal evidence.

### B — sealed uninstrumented repetition without tracing

Authorize exact repetition and ordinary process/socket/timing snapshots but no
new native tracer. This can measure recurrence or nondeterminism. It cannot by
itself distinguish signal delivery from callback/lifecycle entry and therefore
cannot support a remedy or D-APP-88 acceptance.

### C — defer/park

Authorize no next replay. D-APP-88 and DEL-09-04 remain open; the recovered
shared-identity baseline remains operative. A later exact trigger returns the
question to the owner.

## Recommendation

Recommend A. R3 exhausted the lawful source-instrumented comparison: the exact
uninstrumented failure and the both-pass instrumented controls are jointly
valid, and the common logger may change timing. A bounded out-of-process trace
paired with a sealed uninstrumented replay directly addresses that evidence
gap. B adds recurrence evidence without causal resolution; C is coherent if
the owner does not want the new exposure now.

## Non-effects

No option by itself selects a product remedy, closes D-APP-88 or DEL-09-04,
fires TM-APP-036, weakens the first-signal gate, changes Root semantics, or
creates product, release, lifecycle, reliance, or Git effect.
