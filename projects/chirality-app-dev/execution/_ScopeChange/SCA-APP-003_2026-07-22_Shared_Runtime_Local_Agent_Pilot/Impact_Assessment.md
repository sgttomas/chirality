# SCA-APP-003 Impact Assessment

## Authority and implementation impact

| Surface | Impact |
|---|---|
| Root governance | D-GOV-20 establishes shared runtime authority and public boundary. |
| App authority | D-APP-73 and six authority docs govern extraction, daemon, client, CLI, central sessions, residency, and pilot. |
| D-APP-41 | Historical record preserved; eager project-local migration is prospectively extended to lazy non-destructive cross-store migration. |
| D-APP-72 | Historical record preserved; loopback exception expands only to status/load/unload and explicit one-primary-model residency. |
| Tier-0 domain | D-T0-23 shares runtime infrastructure without merging project/domain authority. |
| PEC | D-PEC-56 retires independent LLM/session/delegation ownership prospectively while preserving acts, RBAC, human gates, and scratch/demo fence. |
| Public export | Generic runtime/CLI/contracts/safe adapters become eligible after validation; secrets, machine state, and private adapters remain excluded. |
| Topology/lifecycle | Existing 10 packages and 51 deliverables are reused; no lifecycle state or Checking Approval SHA changes. |

## Principal risks

- Duplicate runtime ownership: fail closed and prove Desktop/CLI/PEC share one daemon.
- Local control exposure: Unix socket only, strict permissions, project authorization, no TCP listener.
- User-data authority drift: manifest hash/re-registration and checkout-contained governance/evidence.
- Session loss or rewriting: lazy reads, non-destructive migration, replay/restart tests.
- Residency disruption: explicit activation, drain, no force, no fallback, `NO_MODEL`.
- PEC authority erosion: project adapter retains RBAC and human-only acts; scratch/demo pilot only.
- Export leakage: allowlist, secret scan, machine-state/private-adapter exclusions.
