# Context: DEL-07-01 Working Root Validation and Instruction Root Protection

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-07 |
| PackageName | Filesystem Execution, Lifecycle, and Dependencies |
| DeliverableID | DEL-07-01 |
| DeliverableName | Working Root Validation and Instruction Root Protection |
| ResponsibleParty | TBD |
| Type | SECURITY_CONTROL |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** Working-root truth, execution-root scaffolding, deliverable files, `_STATUS.md`, `Dependencies.csv`, snapshots.

**InclusionCriteria:** Project file mechanics and deterministic filesystem APIs.

**Exclusions:** UI presentation except scope scan results.

## Deliverable Scope

Enforce working-root validity, root separation, path containment, and
instruction-root write protection for both the bundled base and the
client-owned, hash-pinned organisation layer.

Applied decomposition row L357 (SCA-APP-010 Gate 5, 2026-09-04) notes:
Filesystem policy slice with security acceptance.

## Anticipated Artifacts

Root validation tests; path policy helpers; instruction-root protection
fixtures; organisation-layer pin and protection fixtures

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-002, SOW-027, SOW-075, SOW-084 |
| SupportsObjectives | OBJ-006, OBJ-008 |
| ContextEnvelopeNotes | Filesystem policy slice with security acceptance. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## Current execution basis — 2026-09-22

Codex is the sole current MVP engine, hosted as stock app-server under the application-owned Runtime service (D-GOV-43/D-APP-127). ScopeOfWork.md carries the current production claims. Legacy provider/daemon/four-document statements above retain their historical basis and do not qualify the live path. Existing scope, decomposition identity, responsible-party assignment and domain/professional boundaries are unchanged; current obligations and gaps are in `_STATUS.md`.
