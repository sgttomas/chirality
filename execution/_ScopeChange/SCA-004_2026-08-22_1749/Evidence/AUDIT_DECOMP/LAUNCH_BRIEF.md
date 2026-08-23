# Sealed launch brief — SCA-004 Gate-1 AUDIT_DECOMP baseline

- Parent: `SCOPE_CHANGE`, N3, run `ROOT_V3_PHASE0_2026-08-22`
- Construction: dedicated Agent 2 `AUDIT_DECOMP`; no delegation permitted
- Requested by: `SCOPE_CHANGE`
- Run label: `SCA-004-GATE1-PRECHANGE-ROOT-SOFTWARE`
- Purpose: fresh read-only pre-change decomposition coverage baseline required
  by SOFTWARE SCOPE_CHANGE Gate 1
- Repository basis: `main@6b0c5219b6a2653e2fc491b1d998abcf78fcf776`
- `EXECUTION_ROOT`: `execution/`
- `DECOMPOSITION_PATH`:
  `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`
- `DECOMP_VARIANT`: `SOFTWARE`
- `SCOPE`: `DEL-02-06`, `DEL-04-05`, `DEL-05-02`
- Scope reason: these are the affected live Root carriers at Gate 1. The six
  candidate PKG-02 additions and candidate DEL-04-11 are not live
  decomposition entities and therefore are not audit inputs.
- Expected source snapshot:
  `execution/_ScopeChange/SCA-002_2026-07-29_0800/`
- Expected handoff phase: `SCA-004_GATE_1_OWNER_CONSIDERATION`

## Exact input bindings

| Input | SHA-256 |
|---|---|
| `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` | `23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d` |
| `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv` | `a29759be51aa749ebad22fd3f4d08a1c12ef8f477ae95b846cfc880cc2241395` |
| `execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv` | `3deed192a6f760708f552891b74285f0157e66a9f86e25a1b3cecebf0baf59c2` |
| `execution/_ScopeChange/_LATEST.md` | `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1` |

## Human-authorized output override

The owner fenced this tranche to the SCA-004 folder. This sealed brief
therefore overrides `AGENT_AUDIT_DECOMP.md`'s default tool-root snapshot and
pointer instructions. Write all durable audit evidence only under:

`execution/_ScopeChange/SCA-004_2026-08-22_1749/Evidence/AUDIT_DECOMP/`

Do not create or modify anything under `execution/_Evaluation/`. Do not
create or update any `_LATEST.md` pointer. Do not modify this launch brief,
the decomposition, companion registers, deliverable files, SCA manager files,
or any path outside the authorized evidence folder. This override changes
only the output location and pointer behavior, not audit semantics.

## Required outputs

- `RUN_SUMMARY.md`
- `QA_Report.md`
- `Decision_Log.md`, explicitly recording this output override
- `Decomp_Coverage_Report.md`
- `Decomp_Coverage_IssueLog.csv`
- `Decomp_Coverage_Matrix.csv`
- `coverage_summary.json`
- `RETURN.md`

Run all twelve checks, marking a check `SKIPPED` or `INCOMPLETE` with reason
when the scoped SOFTWARE run makes it inapplicable. Report exact scoped
coverage, telemetry, issue counts, lifecycle distribution, evidence paths,
input/output hashes, and a non-blocking audit verdict. Do not interpret Gate 1
or authorize Gate 2. Do not repair any finding. Use no network and do not
delegate.
