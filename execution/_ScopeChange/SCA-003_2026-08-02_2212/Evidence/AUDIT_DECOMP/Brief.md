# Brief — SCA-003 Gate-1 decomposition baseline

This file preserves the normalized execution parameters for the sealed launch
brief at `LAUNCH_BRIEF.md` (SHA-256
`8344e4277ae2964da91efe11044ae33a3cc46a052bd0cfa7e47ca4bb132d5dba`).
The launch brief is incorporated verbatim by reference and remains the exact
dispatch surface.

| Parameter | Normalized value |
|---|---|
| Parent | Root `SCOPE_CHANGE`, `SCA-003`, HELP_HUMAN run `ROOT_FOUR_LANES_2026-08-02`, node `S1` |
| Role | `AUDIT_DECOMP` Agent 2 |
| Requested by | `SCOPE_CHANGE` |
| Run label | `SCA003_GATE1_PRECHANGE` |
| Repository basis | `97678a841ef58345c73d3470ed8de57c9b1405d2` |
| Execution root | `execution/` |
| Decomposition path | `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` |
| Decomposition SHA-256 | `6f43f3fbc25e0663697464a7a20f3b1bac4b731b01efbe473642e238b93a4d49` |
| Variant | `SOFTWARE` |
| Scope | Target carriers `DEL-02-04`, `DEL-02-06`, `DEL-03-01`, `DEL-06-04`; package-integrity context `PKG-02`, `PKG-03`, `PKG-06` |
| Expected source snapshot | `execution/_ScopeChange/SCA-002_2026-07-29_0800/` plus the current accepted decomposition package it applied |
| Expected handoff phase | `SCA-003 Gate 1 pre-change baseline` |
| Write zone | `execution/_ScopeChange/SCA-003_2026-08-02_2212/Evidence/AUDIT_DECOMP/` only |

The standard AUDIT_DECOMP tool-root snapshot and `_LATEST.md` update are
suppressed by the more specific sealed write boundary. This evidence folder
is the immutable run snapshot for this dispatch.
