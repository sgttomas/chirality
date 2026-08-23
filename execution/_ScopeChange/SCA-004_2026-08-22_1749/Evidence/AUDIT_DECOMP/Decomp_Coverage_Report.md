# SOFTWARE decomposition coverage report

## Audit identity

- Run: `SCA-004-GATE1-PRECHANGE-ROOT-SOFTWARE`
- Source basis: `execution/_ScopeChange/SCA-002_2026-07-29_0800/`
- Handoff phase supported: `SCA-004_GATE_1_OWNER_CONSIDERATION`
- Scope: `DEL-02-06`, `DEL-04-05`, `DEL-05-02`
- Derivative status: read-only pre-change audit evidence; not decomposition truth
- Overall verdict: `OK` (non-blocking)

## Exact coverage summary

| Metric | Result |
|---|---:|
| Scoped packages found | 3/3 (100.0%) |
| Scoped deliverables found | 3/3 (100.0%) |
| Reverse folder coverage | 3/3 (100.0%) |
| Context fidelity | 3/3 (100.0%) |
| Anticipated production artifacts present | 0/11 (0.0%) |
| Relevant objectives with scoped live support | 5/5 (100.0%) |
| Scoped deliverables without objective mapping | 0 |
| Scoped IN-ledger rows without objective mapping | 0/5 |
| Lifecycle distribution | `INITIALIZED`: 3 |
| Issues | 0 BLOCKER; 0 WARNING; 11 INFO |

The 0.0% artifact-presence value is expected pre-production telemetry, not a
coverage defect: all three carriers are `INITIALIZED`, and each valid
`ScopeOfWork.md` describes outputs not yet produced.

## Twelve checks

| Check | Verdict | Evidence |
|---|---|---|
| 1 — Forward coverage: packages | PASS | `PKG-02`, `PKG-04`, and `PKG-05` are declared in decomposition §8 and each matching `execution/PKG-*` folder exists. |
| 2 — Forward coverage: deliverables | PASS | All three deliverables are declared in §9 / the deliverable register and each exact `1_Working/DEL-*` folder exists under its declared parent. |
| 3 — Reverse coverage: folders | PASS | Each scoped discovered folder maps to one declared stable ID; no reverse-only scoped package or deliverable exists. |
| 4 — ID consistency | PASS | Folder prefixes are exactly `DEL-02-06`, `DEL-04-05`, and `DEL-05-02`; each first pair matches its parent package. |
| 5 — Context fidelity | PASS | All three `_CONTEXT.md` files match register name, parent, type, owner, description, and `ContextEnvelope=M`. |
| 6 — Artifact presence | PASS_WITH_INFO | All three folders conform to `SOW_V1`. The 11 anticipated production artifacts have no filename match: 5 for DEL-02-06, 3 for DEL-04-05, 3 for DEL-05-02. At `INITIALIZED`, each absence is INFO. |
| 7 — Objective mapping | PASS | Scoped mappings resolve to five unique objectives. Every referenced objective has at least one existing scoped deliverable; no scoped support is retired; counts agree between the register, ledger, and main summary. |
| 8 — Ledger integrity | PASS | SOW-009, SOW-021, SOW-041, SOW-053, and SOW-104 are IN. Their package, deliverable, and objective references resolve; SOW-009's additional DEL-05-08 reference also exists in the whole decomposition. |
| 9 — Derivative-package parity | SKIPPED | The protocol assigns this check to DOMAIN; it is not variant-owned by SOFTWARE. |
| 9b — Package-shape conformance | PASS | Main document §3 is an explicit companion inventory with role and authority labels. Heavy ledger and deliverable truth lives in companion CSVs; no derived publication artifact is treated as authoritative. |
| 10 — Active snapshot and handoff | PASS | `_LATEST.md` points uniquely to existing SCA-002. The required SCOPE_CHANGE artifact set is present. The application append, applied-hash evidence, live revision, and pointer agree; no later-phase overclaim was found. |
| 11 — Lifecycle distribution | PASS | All three `_STATUS.md` files report recognized state `INITIALIZED`; tally is 3. |

## Per-carrier evidence

### DEL-02-06

Declared by deliverable-register record 14 (CSV line 15) under PKG-02;
filesystem folder exists with matching context and valid `SOW_V1`. It maps
SOW-104 to OBJ-001, OBJ-002, OBJ-004, and OBJ-007. Lifecycle is `INITIALIZED`.
Artifact presence is 0/5, producing INFO COV-001 through COV-005.

### DEL-04-05

Declared by deliverable-register record 25 (CSV line 26) under PKG-04;
filesystem folder exists with matching context and valid `SOW_V1`. It maps
SOW-009 and SOW-041 to OBJ-003. Lifecycle is `INITIALIZED`. Artifact presence
is 0/3, producing INFO COV-006 through COV-008.

### DEL-05-02

Declared by deliverable-register record 32 (CSV line 33) under PKG-05;
filesystem folder exists with matching context and valid `SOW_V1`. It maps
SOW-021 and SOW-053 to OBJ-003. Lifecycle is `INITIALIZED`. Artifact presence
is 0/3, producing INFO COV-009 through COV-011.

## What to fix for a cleaner rerun

No decomposition/filesystem correction is required. A later production-stage
rerun can replace the eleven INFO findings with filename-backed artifact
evidence as outputs are lawfully produced. Any post-acceptance SCA-004 run must
use the then-current decomposition and pointer bytes rather than reusing this
pre-change baseline.

This report is evidence for the invoking manager. It makes no owner decision,
Gate-1 interpretation, Gate-2 authorization, lifecycle transition, or repair.
