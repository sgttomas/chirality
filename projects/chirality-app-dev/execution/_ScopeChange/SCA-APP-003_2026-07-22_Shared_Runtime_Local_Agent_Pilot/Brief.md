# SCA-APP-003 Brief — Shared Runtime and Local-Agent Pilot

**Status:** `GATE_4_APPROVED_IMPLEMENTATION_PENDING`
**Date:** 2026-07-22
**Authority:** D-GOV-20, D-APP-73, D-T0-23, D-PEC-56
**Decomposition:** `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`

## Change request

Promote the provider-neutral executable harness into root `runtime/`, then
introduce one per-user headless daemon, authenticated Unix-socket clients,
bundled CLI, explicit one-primary-model oMLX residency, an app-dev Agent 1 →
local Agent 2 pilot, PEC agent-path migration, and generic public export.

Runtime user-data state remains operational and non-authoritative. Project
truth stays checkout-contained. Agent roles remain authority contracts
independent of engines and models.

## Atomic actions

| ID | Action | Result |
|---|---|---|
| A001 | Record root ruling | D-GOV-20 establishes shared-runtime authority, registration, role independence, and public boundary. |
| A002 | Record app ruling | D-APP-73 governs extraction, daemon/client/CLI, lazy session migration, and explicit residency. |
| A003 | Record cross-domain ruling | D-T0-23 preserves independent project/domain authority while converging runtime infrastructure. |
| A004 | Record PEC ruling | D-PEC-56 retires independent PEC LLM/session/delegation ownership prospectively and preserves deterministic acts/RBAC/human gates. |
| A005 | Align app authority | Six authority docs, AGENTS, decomposition, reliance, validation, build, and affected status records carry the accepted amendment. |
| A006 | Align domain and PEC surfaces | Profile/index/workplan/receipts/bridge and PEC governance/architecture/status/traceability/runbook/sidecar docs carry the migration boundary. |
| A007 | Record public-export policy | Generic runtime/CLI/contracts/safe adapters are in; credentials, machine state, and private adapters are out. |
| A008 | Reconcile authority corpus | Mint the next D-APP-38 corpus version and regenerate governed references after all authority edits. |
| A009 | Hand off implementation | G1+ owners execute behavior-preserving extraction, daemon/client/CLI, pilots, PEC migration, validation, and export. |

## Scope boundary

This governance tranche changes no runtime, Desktop, PEC implementation,
package manifest, lockfile, database, project data, lifecycle state, release,
publication, issuance, or professional-reliance state.
