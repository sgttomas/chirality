---
run_id: PEC_SOW_V22_SCA003_RECON_2026-07-28
doc_kind: deliverable_concordance.run_basis
status: frozen
created: 2026-07-28
activation: D-PEC-69
source_commit: 404e47c16a88e7ffdc6d1fc5fac61ebb6864211e
---

# PEC PRD v2.2 / SCA-003 ScopeOfWork reconciliation — run basis

## Activation

D-PEC-69 is durable on shared `main` at merge
`404e47c16a88e7ffdc6d1fc5fac61ebb6864211e`. It activates this exact run
under the owner's standing completion direction and records R0–R6
recommendations as owner-approved.

## Frozen source state

| Surface | SHA-256 |
|---|---|
| `docs/DELIVERABLE_CONCORDANCE_METHOD.md` revision 1 | `abf3e78fce606c4557d61cdbfbdb7292a3d858838f6526da6b433d1bcd0ef627` |
| `agents/AGENT_RECONCILIATION.md` | `46bca06f907c4da765b1b1177ecd51c6858fdf45bf7620341175c3b847a3e4f7` |
| `projects/pec/docs/PRD.md` v2.2 | `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba` |
| `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.3 | `3f65ea0e47036a2baa66cb60923f8b779525ae00d747425f93f8b69431151787` |
| `execution/_Decomposition/ScopeLedger.csv` | `3cca281f7019a4544b6d4e6ab631a30125429525106f5d65b16aac270ebd50f5` |
| `execution/_Decomposition/Deliverables.csv` | `b27ff4631f4966931990bbf9c033d2593d3dd8ac51b09e0d5112002b98afbc40` |
| `execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv` | `d92d134bdfe4466dc06292fa53fa44cf368d6be1dfeb04fefa6ce188bba8002a` |
| D-PEC-69 | `e6453ef467e71d7bb8548bf6fa36bb01affb73462cc9cdb54192585a520e4e0b` |
| Decision register | `434f93f2a6496b17687db6087748bb3590f9bea58d245fda2a400a405abb5202` |

The SCA-003 durable merge
`11a494e9ae0cca795aa460deec19b9eac4d922a8` is an ancestor of this basis.

## Corpus census at freeze

- 64 deliverable directories.
- 32 complete active `SOW_V1` contracts and 32 `OPEN` deliverables with no
  production contract.
- Lifecycle: 32 `INITIALIZED`, 32 `OPEN`.
- Pre-repair sorted SOW manifest:
  `33a2f54646d74d12bf619ec039dc69ecb403ffd7e0acc5e17d0b558220f31547`.
- Decomposition: 94 scope rows, 11 packages, 64 deliverables, 6 objectives.
- Dependencies: 64 registers, 254 rows; topology is excluded from repair.

## Reliability and authority

Accepted PRD/decomposition/decision records define scope. Current complete
ScopeOfWork contracts are declared production contracts being reconciled.
Implementation, tests, frozen v0.4 code, generated views and prior run
artifacts are evidence only and cannot create scope. Historical ADR-014 is
lineage only; ADR-002 remains live.

## Hold and fences

`PEC-HOLD-001` is active over DEL-00-01 `CLM-005` / `REQ-004`.
The deterministic preflight returned `ALLOW` for:

- `historical-read-only-inspection`;
- `exact-correction-preparation`;
- `candidate-validation`.

It remains a hard block on production reliance, production dispatch,
promotion and consumption. No hold release occurs in this run.

Only execution-time-confirmed affected `ScopeOfWork.md` contracts and this
run directory are writable. `_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`,
dependencies, decomposition, PRD, implementation, runtime, lifecycle,
release, estimates and schedules are read-only/excluded.

## Concurrent work and source drift

This run uses the isolated worktree
`/private/tmp/chirality-pec-sow-reconciliation-run` on branch
`codex/pec-sow-v2-2-reconciliation`, created clean from the D-PEC-69 merge.
Unrelated worktrees and branches are outside this run. Any material change to
the frozen PEC authority or target-contract population before integration
requires rebase plus source-state revalidation.
