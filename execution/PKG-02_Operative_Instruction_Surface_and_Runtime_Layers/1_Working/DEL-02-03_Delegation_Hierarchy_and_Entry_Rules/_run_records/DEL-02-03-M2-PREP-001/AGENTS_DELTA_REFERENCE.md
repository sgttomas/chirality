# Exact `AGENTS.md` Delta Reference

Status: `INACTIVE — REFERENCE ONLY`

The exact proposed `AGENTS.md` delta is not duplicated in this package. Its
single controlling artifact is:

- path:
  `docs/governance_harness/_PROPOSALS/D-GOV-35_2026-08-22_delegated_harness_native_class/AGENTS.proposed.patch`
- SHA-256:
  `4455adda4199be5493e1f8d2171ebb4641f40666c35cf09e90adc935ff6355ee`
- expected pre-application `AGENTS.md` SHA-256:
  `268becd0bac9da8421b30089e4e4167a5e5f79bf3892d0f72ad41a63180a3aeb`
- N1 packet status: `PROPOSED — AWAITING OWNER RULING`

The patch proposes only the `## Delegation and Entry Rules` change described
by D-GOV-35: two executable delegation classes; untyped, Agent 0, and Agent 1
primary native entry; no automatic role assignment by native descent; Codex
Agent 0/1/2 entry parity; the exact `role not mechanically enforced` and
`instruction-asserted` labels; and the instruction+config-asserted rather than
mechanism-proven K-SUBAGENT boundary. This prose is a semantic index, not a
second patch representation.

Before application, the integration owner must reproduce the patch hash, the
pre-application `AGENTS.md` hash, and literal
`git apply --check <path>`. Any hash mismatch or content change invalidates
this reference and requires a fresh proposal/application review. The patch is
not applied by this preparation package.
