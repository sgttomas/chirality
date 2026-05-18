# Docs Resolution Report

Date: 2026-05-18

## Scope

This pass resolved active `docs/` placement using only these source repositories:

- `/Users/ryan/ai-env/projects/chirality-app`
- `/Users/ryan/ai-env/projects/chirality-app-test`
- `/Users/ryan/ai-env/projects/chirality-piping`

The rule applied was:

- root `docs/` holds common Chirality-wide governance/specification/thesis material;
- `projects/<project>/docs/` holds only docs that pertain to that project;
- project-local copies of common root docs are removed unless that project copy is clearly the newest intended common version.

## Root Docs Decision

The active root `docs/` set remains aligned with the current `chirality-app` public export.

The `chirality-app-test` and `chirality-piping` copies of several Chirality-wide docs include now-retired references to `docs/REPO_INVENTORY.md` and `appendix_b_agent_inventory.md`. Because `docs/REPO_INVENTORY.md` was intentionally deleted, those copies were not promoted into root even when their file timestamps or source commits were newer.

Root inventory/count authority is now:

- indexed agents: `AGENTS.md`;
- repo-native skills: live `skills/*/SKILL.md` folders;
- registered deterministic tools: `tools/REGISTRY.md`.

## Project Docs Cleanup

Removed active common Chirality docs from `projects/chirality-piping/docs/`:

- `DBM_Agent_Instruction_Architecture.md`
- `PLAN.md`
- `PRD_CANDIDATE.md`
- `SE_Design_Analysis.md`
- `WHAT-IS-AN-AGENT.md`
- `rubrics/AUDIT_AGENT.md`
- `templates/MEMORY_TEMPLATE.md`
- `thesis/`

Also removed project-root common duplicates:

- `projects/chirality-piping/CHIRALITY_FRAMEWORK.md`
- `projects/chirality-piping/PROFESSIONAL_ENGINEERING.md`

## Project Docs Retained

Retained `projects/chirality-piping/docs/` files that are OpenPipeStress-specific, including:

- OPS governance docs: `DIRECTIVE.md`, `CONTRACT.md`, `SPEC.md`, `TYPES.md`;
- OPS product and boundary docs: `PRD.md`, `INTENT.md`, `IP_AND_DATA_BOUNDARY.md`, `PROFESSIONAL_BOUNDARY.md`;
- OPS release, validation, architecture, security, user/developer guide, and local-analysis docs;
- OPS scope-change records and registers.

## Quarantined Reference Corpus

Retained `projects/chirality-piping/docs/_ScopeChange/chirality-app-docs/`.

Reason: OpenPipeStress records explicitly classify this folder as a quarantined reference corpus for SCA-002. It is not active project documentation and is not used as authority for current root `docs/`.

## Verification

- Active `projects/chirality-piping/docs/` no longer contains exact duplicates of root `docs/`.
- Active `projects/chirality-piping/docs/` files are OPS-specific by title, metadata, or content.
- `REPO_INVENTORY.md` and `appendix_b_agent_inventory.md` remain absent from active root/public docs.
