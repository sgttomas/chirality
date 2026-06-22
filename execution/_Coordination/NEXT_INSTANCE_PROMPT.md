# Profile-Schema Validator — TOOLMAKER Handoff (build the DomainEngineProfile validator)

> **This is the active `NEXT_INSTANCE_PROMPT`.** It supersedes the framework-maintenance handoff (FM-01..04), which is **complete** at commit `77a327727` and preserved in git history. Launch with the **TOOLMAKER** init-prompt (persona must match — see end).

**For:** the next agent, in a **new session**. **Author:** DOMAIN_ENGINE (tier-0), 2026-06-22.

Build the deterministic **DomainEngineProfile schema validator**. It is the single thing gating the OpenPipeStress profile's `DRAFT → VALIDATED` transition (D-T0-06); building it unblocks tier-0 adoption (the 1st of the 4 live-build conditions). The full requirement is in `_DomainEngines/bridge/BRIDGE_2026-06-21_tier0-prep/TOOLMAKER_BRIEF-profile_schema_validator.md`.

---

## 0. Posture & scope

- **Act as `TOOLMAKER`** (`agents/AGENT_TOOLMAKER.md`) — the Type-1 manager owning deterministic tools and `tools/REGISTRY.md`. `WORKING_ROOT = REPO_ROOT`.
- Build a **deterministic, LLM-independent** tool under `tools/` (HELPS_HUMANS R11/R12: if it needs inference it's a skill — but this is pure schema/enum validation, so it's a tool).
- **You MAY write** under `tools/` (+ a `tools/REGISTRY.md` entry) and write the tool's **output report** to a declared path under `_DomainEngines/`. **You MUST NOT** mutate the profile, edit canon (`agents/`, root `docs/`), or touch `projects/**`.

## 1. Authorization

- **D-T0-06** (owner-ruled): `ProfileStatus = VALIDATED` is gated on a deterministic profile-schema validator. See `_DomainEngines/_DECISIONS/D-T0-06_profile_adoption_lifecycle.md` + `_DomainEngines/RULINGS_PUBLISHED.md`.
- The contract the validator checks is **now canon** (post FM-01..04, commit `77a327727`): the Minimal Profile Shape, the "Valid Domain Engine Profile" SPEC, the "Valid Operation Proposal" field table, and the `operation_proposal_contract` block in `agents/AGENT_DOMAIN_ENGINE.md`. (Canon is DRAFT-pending-ratification; validate against the documented shape regardless.)

## 2. What to build (full contract in the requirement brief)

A validator (e.g. `tools/validation/validate_domain_engine_profile.py`) that deterministically checks a `DomainEngineProfile` YAML against the canonical contract:

- **Required fields:** `schema_version`, `id`, `name`, `engine_type`, `profile_version`, `domain_root_patterns`, the **4-class path taxonomy** (`authoritative_artifacts` / `chirality_readable_artifacts` / `protected_write_paths` / `agent_writable_paths`), `deterministic_tools[]` (each with `id`, `mode`, `requires_human_confirmation`, and the `validate_result_schema`/`apply_result_schema` refs or `TBD`), `professional_boundary` (structured `agent_must_not_claim` list).
- **Enum membership:** `profile_status ∈ {NONE,DRAFT,VALIDATED,ADOPTED,STALE,INVALID,UNKNOWN}`; `integration_level ∈ {MANUAL_BRIDGE,READ_ONLY,DOMAIN_CONTROLLED_WRITE,OPERATION_PROPOSAL,EXTERNAL_RESULT_STATE}`; `deterministic_tools[].mode` ∈ the persona's tool-mode taxonomy; `operation_risk_class ∈ {engine_checkable,engine_silent}` where present.
- **`operation_proposal_contract` block** shape (lifecycle, risk_classes, deterministic_check_result_schema, accepted_or_applied_requires).
- **Output:** exit `0` (VALID) / non-zero (INVALID) + a machine-readable JSON report with per-field findings, written to a declared path under `_DomainEngines/` (e.g. `_DomainEngines/profiles/_validation/<id>_<ts>.json`).
- **Behavior:** fail-fast with exit code + stderr; **never** auto-fix, mutate the profile, or mark `ADOPTED`.

## 3. Read cold (verify, don't trust)

- `agents/AGENT_DOMAIN_ENGINE.md` @ `77a327727` — Minimal Profile Shape, Valid Domain Engine Profile, Valid Operation Proposal field table, `operation_proposal_contract`.
- `_DomainEngines/bridge/BRIDGE_2026-06-21_tier0-prep/TOOLMAKER_BRIEF-profile_schema_validator.md` — the requirement brief.
- `_DomainEngines/profiles/open_pipe_stress.DRAFT.yaml` — the profile to validate.
- Governing: `agents/AGENT_TOOLMAKER.md`, `agents/AGENT_HELPS_HUMANS.md` (R10–R12 tool contract + skill/tool boundary).

## 4. Deliverables

1. The validator tool under `tools/`, with input/output contract as script-header comments (args, file format, exit codes), idempotence posture, scope boundary, fail-fast errors. No LLM dependency.
2. A `tools/REGISTRY.md` entry (one row in the appropriate category table).
3. Deterministic tests: a valid profile, each required-field-missing case, each enum-violation case.
4. Run it on `_DomainEngines/profiles/open_pipe_stress.DRAFT.yaml` and capture the report.
5. Hand the file list + a PROPOSAL commit note to **CHANGE** — you do not push.

## 5. Downstream (NOT yours — next owner)

Once the validator exists and passes on the profile: **DOMAIN_ENGINE** moves `ProfileStatus DRAFT → VALIDATED`, then the human Gate 2 takes `VALIDATED → ADOPTED`. That completes **tier-0 adoption** (1 of 4 live-build conditions; the others — app-dev F3, piping D-21, DEC-041 — remain).

## 6. Closeout

Record the tool path, registry entry, test results, the profile validation result, and the next owner (DOMAIN_ENGINE for `VALIDATED → ADOPTED`). Profile stays **DRAFT / not ADOPTED** until then.

---

### Launch init-prompt (persona must be TOOLMAKER, not HELPS_HUMANS)

```
Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`.
Set `WORKING_ROOT` to `{REPO_ROOT}`.
Read `{REPO_ROOT}/agents/AGENT_TOOLMAKER.md`.
Read `{WORKING_ROOT}/AGENTS.md`.
Act in the `TOOLMAKER` persona for `{WORKING_ROOT}`.
Then read `{WORKING_ROOT}/execution/_Coordination/NEXT_INSTANCE_PROMPT.md` and follow the instructions.
```
