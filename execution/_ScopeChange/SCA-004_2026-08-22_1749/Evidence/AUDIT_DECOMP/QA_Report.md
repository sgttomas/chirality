# AUDIT_DECOMP QA report

## Input integrity

| Input | Expected SHA-256 | Observed SHA-256 | Result |
|---|---|---|---|
| `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` | `23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d` | `23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d` | PASS |
| `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv` | `a29759be51aa749ebad22fd3f4d08a1c12ef8f477ae95b846cfc880cc2241395` | `a29759be51aa749ebad22fd3f4d08a1c12ef8f477ae95b846cfc880cc2241395` | PASS |
| `execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv` | `3deed192a6f760708f552891b74285f0157e66a9f86e25a1b3cecebf0baf59c2` | `3deed192a6f760708f552891b74285f0157e66a9f86e25a1b3cecebf0baf59c2` | PASS |
| `execution/_ScopeChange/_LATEST.md` | `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1` | `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1` | PASS |
| Git basis | `6b0c5219b6a2653e2fc491b1d998abcf78fcf776` | `6b0c5219b6a2653e2fc491b1d998abcf78fcf776` | PASS |

## Parse and discovery telemetry

| Probe | Result |
|---|---|
| Semantic heading binding | PASS — `Scope Ledger`, `Packages`, and `Deliverables` resolved by heading text; SOFTWARE objective evidence resolved from ledger `ObjectiveIDs` and cross-checked against the deliverable register |
| Whole topology | 6 packages; 46 deliverables; 7 objectives; 104 scope items / ledger rows (95 IN, 9 OUT, 0 TBD) |
| Scoped topology | 3 packages; 3 deliverables; 5 relevant objectives; 5 ledger rows, all IN |
| Folder discovery | 3/3 package folders and 3/3 deliverable folders |
| Context discovery | 3/3 `_CONTEXT.md` files |
| Lifecycle discovery | 3 `INITIALIZED`; no unknown state |
| Contract shape | 3/3 `ScopeOfWork.md` files; validator returned `PASS format=SOW_V1` for each |
| Active snapshot | `_LATEST.md` resolves to exactly `SCA-002_2026-07-29_0800/`; snapshot and required artifact set present |

## Determinism and limits

- Scope filtering was applied to the three IDs in the sealed brief. Reverse
  coverage considered only folders with those scoped stable IDs; repository
  topology remains reported separately as denominator context.
- Anticipated artifact matching used normalized filename terms and did not give
  production-artifact credit merely because `ScopeOfWork.md` describes an
  output. This yields exact coverage of `0/11` at `INITIALIZED`.
- Context fidelity compared name, parent package, type, responsible party,
  description, and SOFTWARE `ContextEnvelope` to the authoritative deliverable
  register. All fields match.
- Objective integrity used the authoritative ledger/register mappings. It did
  not reinterpret the dedicated objectives prose as SOFTWARE ledger truth.
- No prior run was named, so comparison mode was not run.
- No network, delegation, repair, lifecycle transition, or write outside this
  evidence folder occurred.

QA verdict: `PASS`.
