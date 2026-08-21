# Routed Change Notice — external working-root and domain repository separation

Routed by: Root loop, 2026-08-20, tranche
`ROOT-DOMAIN-REPOSITORY-SEPARATION-20260820`, under the `AGENTS.md`
agent-index change-notice rule because `agents/AGENT_TASK.md` changes.

This notice is coordination, never authority. The App loop adopts,
acknowledges, amends, declines, or defers any local response through its own
instruments and cadence.

## What changed

- Domain packs move from Chirality to private `sgttomas/chirality-domains`.
- Runtime manifest V2 resolves the read-only instruction surface from
  `CHIRALITY_INSTRUCTION_ROOT` and requires it to be disjoint from the working root.
- `AGENT_TASK.md` resolves skills/tools under `INSTRUCTION_ROOT` and contains
  scope/write paths inside `WORKING_ROOT`. SHA-256 `f53e52c245eecaf5e3323556e44b75bb2d9a5e1c58395d3937a930ba94c8d8a1`
  → `80ed9374095b65c8f0ee221ec674ae1a0fa41cbf9ad2727c46853dd7f9ce9983`.
- V1 project manifests remain supported unchanged.

Old hashes in immutable evaluation, packaged-proof, and run-evidence snapshots
remain historical evidence and are not rewritten. Rebuild and verify the
packaged instruction-root manifest after adoption; external V2 registration is additive.

Evidence: `docs/governance_harness/tranche_manifests/ROOT-DOMAIN-REPOSITORY-SEPARATION-20260820.yaml`.
