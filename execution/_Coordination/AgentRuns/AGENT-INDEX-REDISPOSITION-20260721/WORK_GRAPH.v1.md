# Work Graph v1 — Agent-Index Re-disposition

Run: `AGENT-INDEX-REDISPOSITION-20260721`
Basis: `main@0c066652cd527eb1559f715e914262d2bda42602`

All subagent nodes: Opus model, high reasoning effort, sealed brief, disjoint
write scope. CHANGE is the sole Git closeout; the human approves every merge.
Nodes within a PR share a governance/authority boundary and run under one
integration owner; PRs are sequenced, not concurrent.

## PR-level nodes

| Node | Owner | Depends on | Write scope | Gate |
|---|---|---|---|---|
| PR-0 | HELPS_HUMANS | owner direction 2026-07-21; D-GOV-11 | D-GOV-18 record, `_REGISTER.md` (1 row), `AGENT_DISPOSITION_MATRIX.md` (2 rows annotated), this run scaffold | ruling record + scaffold drafted PROPOSED; no role change; no fabricated ruling |
| PR-1 | CHANGE | owner ruling of D-GOV-18 | `agents/AGENT_CHANGE.md` | CHANGE slimmed to authority semantics; `change-method` recorded as Reuse Candidate only |
| PR-2 | EVALUATION shell | PR-1; **App Dev in-flight EVALUATION fan-in closure** | `agents/AGENT_EVALUATION.md`, new `skills/evaluation-protocol/` | thin shell retains name/allowlist/quarantine/fan-in; skill holds method, no write authority |
| PR-3 | HELPS_HUMANS | PR-2 | `agents/AGENT_ORCHESTRATOR.md`→`agents/AGENT_PROJECT_SETUP.md`, `AGENTS.md`, validators, skills, docs (per sub-nodes) | atomic rename; all callers/keys carried; validators PASS |
| PR-4 | HELPS_HUMANS | PR-3 | `agents/AGENT_PROJECT_SETUP.md`, `agents/AGENT_HELPS_HUMANS.md` | Function 5 (control-loop artifacts) moved to HELPS_HUMANS; Function 3 stays in PROJECT_SETUP |

## Per-PR subagent nodes

| Node | PR | Owner | Depends on | Write scope | Gate |
|---|---|---|---|---|---|
| SA-DRAFT | PR-0 | HELPS_HUMANS (this brief) | owner direction | D-GOV-18 record, register row, matrix annotations, run scaffold | drafted PROPOSED; precise citations; no fabricated ruling/SHA |
| SA-CHANGE-SLIM | PR-1 | CHANGE | D-GOV-18 ruling | `agents/AGENT_CHANGE.md` | authority semantics retained; mechanics to agent judgment |
| SA-EVAL-SHELL | PR-2 | HELPS_HUMANS | App Dev EVALUATION fan-in closure | `agents/AGENT_EVALUATION.md`, `AGENTS.md` EVALUATION row | shell retains name, subagents allowlist (TASK + 8 AUDIT_*/EVALUATION_*), `_Evaluation/` quarantine, fan-in validation |
| SA-EVAL-SKILL | PR-2 | HELPS_HUMANS | App Dev EVALUATION fan-in closure | new `skills/evaluation-protocol/SKILL.md` (+ folder) | method captured as skill; no write authority; validator metadata PASS |
| SA-A G-AGENTS | PR-3 | HELPS_HUMANS | PR-2 | `agents/AGENT_ORCHESTRATOR.md`→`agents/AGENT_PROJECT_SETUP.md`, `AGENTS.md` role rows | atomic file rename + charter narrow; index rows updated |
| SA-B G-VALIDATORS | PR-3 | HELPS_HUMANS | PR-2 | `tools/validation/validate_agent_instructions.py` (`REQUIRED_DELEGATION_EDGES` key), `tools/validation/validate_scc_resolution_case.py` (`OWNER_WORKFLOWS` legacy-accepting shim) | key renamed; shim accepts old+new name across transition; suite PASS |
| SA-C G-SKILLS | PR-3 | HELPS_HUMANS | PR-2 | `skills/` dispatch references naming ORCHESTRATOR | skill-side references carry the rename; `skills/README.md` currency preserved |
| SA-D G-DOCS | PR-3 | HELPS_HUMANS | PR-2 | governance/docs references to ORCHESTRATOR (live surfaces only; not historical evidence) | live-doc references updated; `execution/`, decision records, thesis, `domains/`, `projects/` provenance untouched |
| SA-F5-MOVE | PR-4 | HELPS_HUMANS | PR-3 | `agents/AGENT_PROJECT_SETUP.md`, `agents/AGENT_HELPS_HUMANS.md` | Function 5 artifact creation moved; Function 3 scan-and-report stays |

## Concurrency and dependency notes

- PR-2 explicitly depends on **App Dev in-flight EVALUATION fan-in closure**;
  it does not start until that fan-in closes.
- PR-3 sub-nodes SA-A..SA-D have disjoint write scopes but share the atomic
  rename; one integration owner serializes them and CHANGE performs closeout so
  the rename lands as a single consistent change.
- App Dev couplings (persona-resolution.ts `ORCHESTRATE → 'ORCHESTRATOR'` and
  its Jest test; App Dev `AGENTS.md` wording) are NOT nodes in this graph; they
  are deferred to the App Dev project loop by owner consent (D-GOV-18 Item 6)
  via the handoff notice in `HANDOFF_STATE.md`.
