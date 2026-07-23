# G1 Return — Shared Runtime

Status: `COMPLETED`

Implemented root-owned provider-neutral contracts, session/project registries,
engine registry, turn coordination, governed Agent 1 delegation, oMLX residency,
Unix-socket daemon, authenticated client, CLI, and safe engine adapters.

The runtime now enforces private socket/token permissions, project-scoped
authorization, lazy session migration, strict engine-stream conformance,
non-forgeable in-process tool receipts, one active turn per session, explicit
model residency, and redacted evidence.

Validation: runtime typecheck passed; 43/43 runtime tests passed.
