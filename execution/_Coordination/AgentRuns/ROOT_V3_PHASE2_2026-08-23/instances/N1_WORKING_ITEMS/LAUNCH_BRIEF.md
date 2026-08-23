# Sealed launch brief — N1 WORKING_ITEMS

- RequestedBy: `HELP_HUMAN`
- RunID: `ROOT_V3_PHASE2_2026-08-23`
- InstanceID: `N1_WORKING_ITEMS`
- Role: `WORKING_ITEMS` (Agent 1; role not mechanically enforced)
- Objective: manage seven independent SOW-candidate drafts and validate fan-in.
- AcceptedBasis: `origin/main@a7bf601cedda23b7fd2c99d4020f4b3c2a32654b`; Phase 2 steer SHA-256 `bf58c6224e4649038d6faafc4a5125c20042a741f521e992f26b77b00f41d0c3`.
- SelectedDeliverables: `DEL-02-07` through `DEL-02-12`, and `DEL-04-11`.
- Dependencies: basis gate and G0–G4 preflight passed before launch.
- DeclaredReads: Phase 2 steer; `AGENTS.md`; `agents/AGENT_WORKING_ITEMS.md`; applied register; each carrier `_CONTEXT.md`; SCA-004 `Propagation_Plan.md` §2; accepted G0 record; house SOW exemplars.
- AllowedTools: read-only shell inspection, `apply_patch`, SHA-256, and native child dispatch.
- AllowedWriteTargets: the seven new carrier `ScopeOfWork.md` files and this run's instance briefs/status/returns/reviews/handoff records only.
- Exclusions: every Phase 2 not-selectable path and all acceptance, lifecycle, dependency, estimate, schedule, implementation, activation, pin, hold-lift, App, and merge acts.
- ExpectedOutputs: seven SOWs, seven child returns with hashes, package-level validated return, and fresh consolidated review with zero actionable findings.
- AcceptanceCriteria: exact steer check surface; every child is a distinct sealed Agent 2 instance and does not delegate.
- Escalation: stop and return any grounding gap, authority conflict, unexpected pre-existing file, overlapping write, or required out-of-scope edit.
