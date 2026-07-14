# Manager Reproduction Attempts

## Runtime telemetry interface attempt

The manager's first root-ledger call used the unsupported event type
`SESSION_START`. The registered telemetry tool rejected it before writing an
event. The corrected call used schema event type `START` and succeeded. This
is retained as an interface-lookup/setup finding with no governed-state or
acceptance effect.

## Attempt 1 — retained failed harness assumption

The first manager reproduction stopped during `DEL-02-01` before package
manifests or simulations were emitted. It invoked checklist derivation on the
evidence-rich file in its isolated candidate-only directory and expected a
dual-state rejection. Without the co-located legacy kit, that path resolves as
a standalone `SOW_V1` input and the registered tool correctly succeeds.

The manager gate was corrected to exercise the evidence-rich SOW in the fresh
complete dual workspace without migration authority. This represents the
actual forbidden-consumer state and must fail before checklist/render output.
The entire manager reproduction is rerun from fresh snapshot inputs. No
candidate, child evidence, live/project file, gate, or experiment topology was
changed.
