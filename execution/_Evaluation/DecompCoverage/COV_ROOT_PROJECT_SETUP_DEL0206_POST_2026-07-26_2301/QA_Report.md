# AUDIT_DECOMP QA Report

## Deterministic scan coverage

| Surface | Result |
|---|---|
| Git basis | `ff04694afa709856a58f9f54a79ca2056b8e0b4e` |
| Instruction package | `agents/AGENT_AUDIT_DECOMP.md` v2.1 read completely |
| Markdown semantic bindings | Unique bindings resolved for Ledger, Objectives, Packages, Deliverables |
| Package scan | 6 declared; 6 filesystem folders; 0 missing; 0 reverse-only |
| Deliverable scan | 46 declared; 46 register rows; 46 filesystem folders; 0 missing; 0 reverse-only |
| Context scan | 46 present; 46 exact matches; 0 missing or divergent fields |
| Contract scan | 45 present; 45 `SOW_V1` validators exit 0; DEL-02-06 absent at `OPEN` |
| Ledger scan | 104 unique rows; 95 IN; 9 OUT; every PackageID, DeliverableID, and ObjectiveID resolves |
| Objective scan | 7 unique objectives; register-to-deliverable mapping parity; every mapped folder exists |
| Forward trace scan | 85 rows; every scope, package, deliverable, and objective reference resolves |
| Reverse trace scan | 52 unique units = 6 packages + 46 deliverables; every parent and scope reference resolves |
| ID scan | No duplicates or reused IDs in Markdown topology, deliverable register, ledger, objective register, filesystem, or reverse trace |
| Active snapshot scan | `_ScopeChange/_LATEST.md` uniquely resolves to the expected snapshot; required closure artifacts present |
| Lifecycle scan | 45 `INITIALIZED`; 1 `OPEN`; 0 `IN_PROGRESS` or later |

## Input SHA-256

| Input | SHA-256 |
|---|---|
| `agents/AGENT_AUDIT_DECOMP.md` | `1f12e86e2f1dd3506fe1d1e46caf7f9be2d1b4b8acd75427f2876593dc2015cb` |
| `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` | `2dd37e20d8175eec3a7a926dcf454fbee5065d076fc59eac6ead82e911192c18` |
| `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv` | `ec32b36fdc078e44a7ca094e9c854a3be6b7d5917360fe5ef5f22ff3702a13b8` |
| `execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv` | `0d48abe08aa336ac5e495650451f286b4b717606f047adff931c45dacc8531a4` |
| `execution/_Decomposition/chirality_root_objective_register_v1_0.csv` | `c645c3bd5457f3922640d2e9dfc4f315923a412fc098ad2d3bb9b2d0f8521f55` |
| `execution/_Decomposition/chirality_root_prd_coverage_forward_v1_0.csv` | `adde466ac0b7ea708084ed08ab16f10c5710473fd0c53a68e32c3eb53496cb84` |
| `execution/_Decomposition/chirality_root_trace_reverse_v1_0.csv` | `6cce13b19f27c3638fce5bd383423ee79e872bb5b1080441c3b525424e8ec3b0` |
| `execution/_Decomposition/chirality_root_coverage_telemetry_v1_0.md` | `6882c713763d31613ab22fe8122baf9d98739fe7cc8dbfdfead5bb84255da282` |
| `execution/_ScopeChange/_LATEST.md` | `d3071d717c81d94406a1a216b72c60160c8bfc20fc38dab88c93596796cc036e` |
| `execution/_ScopeChange/SCA-001_2026-07-26_1454/RUN_SUMMARY.md` | `4ff127c9b61bcbe0024b12d22a411731492a2d9f32b9fd5e3b19dfed3f866a46` |
| `execution/_ScopeChange/SCA-001_2026-07-26_1454/Handoff_State.md` | `8663fc22faa6dcdd34684c4adfa8d8d87a900d94d8fa0cea8b155afd09eead2d` |

## Parse issues and limits

- Parse issues: none.
- Ambiguous semantic heading bindings: none.
- Fuzzy context judgments required: none; all compared fields were exact after
  schema-aware list and package-name parsing.
- Artifact filename coverage is `0/137`. This is not a lifecycle defect because
  every deliverable is pre-production (`INITIALIZED` or `OPEN`).
- The audit did not assess implementation quality or authorize production work.
- Output hashes are computed after immutable publication and returned to
  PROJECT_SETUP; embedding an artifact's own hash inside itself would be
  self-referential.
