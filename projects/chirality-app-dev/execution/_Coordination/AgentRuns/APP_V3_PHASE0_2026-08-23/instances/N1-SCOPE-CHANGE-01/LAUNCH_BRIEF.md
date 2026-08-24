# N1 SCOPE_CHANGE — Sealed Launch Brief

- `RunID`: `APP_V3_PHASE0_2026-08-23`
- `Node`: `N1`
- `Instance`: `N1-SCOPE-CHANGE-01`
- `Role`: `SCOPE_CHANGE` (Agent 1)
- `RequestedBy`: `HELP_HUMAN`
- `SelectionAuthority`: `HUMAN` — Ryan Tufts, App Session Init of 2026-08-23
- `AcceptedBasis`: `3af765222bbd4f43a52dcbe17bd151c13942e5ac`
- `Branch`: `codex/app-v3-phase0-2026-08-23`
- `Purpose`: produce the assessment-only SCA-APP-008 Gate-1 package and App objective-relative DAG directed by the re-issued v3 Phase-0 steer; no amendment is applied.

## Declared read scope

Read-only access is allowed to the repository at the accepted basis, limited in use to the owner-supplied Phase-0 steer and records, Root/App instruction packages, existing App decomposition, scope-change, deliverable, decision, Task Management, release-quality, runtime/frontend implementation, and coordination evidence needed to trace the requested assessment and DAG. Root surfaces are evidence inputs only. No network access is authorized.

## Exact write roots

1. Content: `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/**`
2. Control plane: `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_PHASE0_2026-08-23/instances/N1-SCOPE-CHANGE-01/**`

Every other path is read-only. In particular, `_ScopeChange/_LATEST.md`, decomposition truth, contracts, code, registers, lifecycle/status files, pointers, `docs/**`, `frontend/**`, `runtime/**`, `plans/**`, Root-loop surfaces, and other nodes' run instances are immutable for this node.

## Required outputs

- `Brief.md`
- `Impact_Assessment.md`
- `Carrier_Map.md`
- `Contract_Amendments.proposed.md`
- `WORK_GRAPH.json`
- `DAG.md`
- `Handoff_State.md` in the required four-state form
- draft reciprocal Root notice retained inside the SCA folder
- validated `AUDIT_DEP_CLOSURE` return/evidence
- fresh independent review evidence
- this instance's `RETURN.md` and final `STATUS.json`

The SCA package status is `AWAITING_OWNER_ACCEPTANCE`. It is an immutable assessment candidate, not active decomposition truth; `_LATEST.md` remains untouched.

## Acceptance checks

- Every N1 item and owner amendment in the re-issued steer is seated without invention or omitted constraint.
- D-APP-103 interaction statement is exactly one sentence containing the disposition `defers` and creates no new instrument.
- Root cross-loop relationships are notice edges citing the landed D-GOV-35 notice path/SHA and Root SCA-004 Gate-5 merge.
- SCC cycle edges are non-gating until a proposed cycle-resolution move is owner-accepted.
- `WORK_GRAPH.json` parses and every App node resolves to a live App deliverable folder or an explicitly typed Root notice edge.
- A fresh `AUDIT_DEP_CLOSURE` return is present and PASS/non-blocking for the assessment package.
- A fresh independent reviewer returns PASS after any required repair.
- `_ScopeChange/_LATEST.md` remains SHA-256 `a0298fdc5709181119d4c645b72b72f07b0c3b14904da67043d9de1f7ee01794`.
- No node write occurs under `docs/**`, `frontend/**`, Root surfaces, or any undeclared path.

## Dependency assumptions

- Basis gate and owner-supplied instrument hashes were verified by HELP_HUMAN before dispatch.
- Root D-GOV-35 is ruled/applied and its App notice is admitted evidence, not re-derived authority.
- Root SCA-004 is applied/confirmed at Gate-5 merge `6d4438d8d3a580b65d6d50ad497dadfe07f177f2`.
- N1 has no execution dependency on N2 or N3. It may be enriched at fan-in by an accepted N3 report without reopening this sealed write set.

## Escalation conditions

Stop and return a blocker if the accepted basis or required evidence cannot be verified; a requested node cannot be resolved to a live App deliverable or named Root notice edge; satisfying a requirement would require a write outside the two roots; an SCC requires a human-gated cut/merge to become gating; or fresh audit/review cannot pass after unlimited in-scope repair. No scope widening, sync, rebase, commit, push, merge, acceptance, or lifecycle transition is authorized.
