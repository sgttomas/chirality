# Agent Disposition Matrix — D-GOV-11

> **Status:** Current migration record. `PENDING EVIDENCE` is deliberately not a live-role decision.

| Role / family | Disposition | Destination or basis | Current state |
|---|---|---|---|
| HELP_HUMAN | REWRITE | Sole Agent 0 Supervising Architect | Implemented; durable launch-brief fallback remains until runtime bridge |
| HELPS_HUMANS | EXPAND | Agent 1 component-design manager | Implemented |
| DECOMP_BASE | EXTRACT | `docs/DECOMPOSITION_STANDARD.md`; design assistance to HELPS_HUMANS | Implemented; persona removed |
| SKILLMAKER | MERGE | HELPS_HUMANS skill-design mode | Implemented; persona removed, skill standards retained |
| TOOLMAKER | MERGE | HELPS_HUMANS tool-design mode | Implemented; persona removed, tool registry/contracts retained |
| CONTEXT_TRANSPOSE | MERGE | HELPS_HUMANS component/migration design; bounded run work uses TASK or ephemeral generalist | Implemented; persona removed |
| SCHEDULING | MERGE | ORCHESTRATOR schedule workflow; calculation/rendering downward | Implemented at instruction layer; persona removed |
| EVALUATION | EXPAND | Generic audit orchestration plus old RECONCILIATION audit/coherence semantics | Implemented |
| RECONCILIATION | RECREATE | Deliverable-corpus concordance from ratified method and two accepted calibrations | Reserved fail-closed; pending external handoffs |
| PDF2MD | RETAIN / SLIM | Agent 1 source-contract manager; page work to TASK/generalist, deterministic work to tools | Manager boundary implemented; further slimming incremental |
| DRAWING_EXTRACT | RETAIN / SLIM | Agent 1 target/schema manager; sheet work to TASK/generalist, deterministic work to tools | Manager boundary implemented; further slimming incremental |
| ORCHESTRATOR | RETAIN / EXPAND | Setup, coordination, control loops, scheduling gates | Implemented at instruction layer |
| WORKING_ITEMS | EXPAND | Package-level Agent 1; manages one activated package, its deliverable work graph, Agent 2 delegation, notices, and package fan-in | D-GOV-12 instruction migration in progress |
| SOFTWARE_DEV | DEFER | First use WORKING_ITEMS plus software activation profiles, TASK skills, tools, and ephemeral generalists | Reconsider only after app-dev and piping trials demonstrate persistent manager semantics |
| REVIEW, CHANGE, RESEARCH | RETAIN / SLIM | Human decisions and formal handoffs remain manager semantics | Re-audit in progress |
| PROJECT_DECOMP, SOFTWARE_DECOMP, DOMAIN_DECOMP | RETAIN / REBIND | Consume external decomposition standard | Implemented |
| SCOPE_CHANGE, DOMAIN_ENGINE, DBM_PUBLISHER, EQUATION_AUDIT | RETAIN / SLIM | Preserve human/domain gates; move repetition downward | Re-audit in progress |
| PREPARATION, RESEARCHER, AGGREGATION, DOMAIN_HYPERGRAPH, AUDIT_*, EVALUATION_* | REQUALIFY | TASK skill, tool, ephemeral generalist, or approved dedicated Agent 2 | Pending per-role evidence; existing files remain compatibility-capable |
| TASK | RETAIN | Default recurring-method Agent 2 shell | Live |

## Removal Rule

No remaining dedicated Agent 2 file is removed until its replacement, callers, compatibility behavior, validation, and tests land together. A retained dedicated package still requires an explicit D-GOV-11 qualification record and human approval.

## External Dependencies

The final RECONCILIATION contract depends on stable, accepted concordance handoffs from `chirality-piping` and `chirality-app-dev`. Managed nested delegation depends on integrating those branches, rebasing this tranche, and then changing the app-dev runtime against the accepted instruction roster.
