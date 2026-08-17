# PIN_SEARCH — surfaces that pin or mirror `agents/AGENT_HELP_HUMAN.md`

Run: `ROOT_AGENT0_DIRECT_A2_ALIGN_2026-08-16`
Searched ref: `origin/main` = `b67197f5b647fbf0b972eee158e94c7215db9e6c`
Purpose: root `AGENTS.md` agent-index change-notice rule (identify pinning or
mirroring project surfaces before shipping notices).

## Commands and outputs (exact)

```text
$ git grep -l AGENT_HELP_HUMAN origin/main -- "projects/*/execution/_Reconciliation/References" "projects/*/_harness" "_DomainEngines" "*_CORPUS.json"
rc=1        (no matches)

$ git grep -c AGENT_HELP_HUMAN origin/main -- projects/chirality-app-dev/execution/_Reconciliation/References/AUTHORITY_CORPUS.json
rc=1        (0 occurrences — App AUTHORITY_CORPUS.json does NOT pin this file; confirmed)

$ git grep -l 503f70dbc origin/main
origin/main:execution/_Evaluation/CHIRALITY_PROGRAM_ARCH_META_FANIN_2026-07-26_DA31C19/source_reviews/independent_managed/FROZEN_BASIS_MANIFEST.json

$ git grep -l AGENT_HELP_HUMAN origin/main -- ":(glob)**/*.json" ":(glob)**/*.ts" ":(glob)**/*.py" ":(glob)**/*.yml" ":(glob)**/*.yaml"
origin/main:domains/chirality/_Decomposition/source_asset_manifests/SRC-AGENTS-AGENT-HELP-HUMAN_assets_manifest.json
origin/main:domains/chirality/_Decomposition/source_dispatch_plans/SRC-AGENTS-AGENT-HELP-HUMAN_dispatch_plan.json
origin/main:domains/chirality/_Decomposition/source_skeletons/SRC-AGENTS-AGENT-HELP-HUMAN_skeleton.json
origin/main:execution/_Evaluation/CHIRALITY_PROGRAM_ARCH_META_FANIN_2026-07-26_DA31C19/source_reviews/independent_managed/FROZEN_BASIS_MANIFEST.json
origin/main:projects/chirality-app-dev/frontend/src/__tests__/integration/runtime-desktop-cli-shared-daemon.integration.test.ts
origin/main:projects/chirality-app-dev/frontend/src/__tests__/lib/coordination-tools.test.ts
origin/main:runtime/tests/helpers.ts
origin/main:tools/validation/test_validate_agent_instructions.py
origin/main:tools/validation/validate_instruction_entrypoints.py

$ git ls-tree --name-only origin/main _DomainEngines/_Coordination/
_DomainEngines/_Coordination/NOTICE_2026-07-27_PIPING_SCA-008_CURRENT_EFFECT_RECONCILIATION.md
_DomainEngines/_Coordination/NOTICE_2026-07-27_SCA-APP-005_APP_CLIENT_BOUNDARY.md

$ git ls-tree --name-only origin/main _DomainEngines/pec/ | grep -iv "^_DomainEngines/pec/PEC_"
_DomainEngines/pec/.archive
_DomainEngines/pec/LOOP_INIT.md
_DomainEngines/pec/LOOP_RECEIPTS.md
_DomainEngines/pec/PLAN_CURRENCY_NOTE_2026-08-09_D-T0-27.md
_DomainEngines/pec/WORKPLAN_2026-07-09_pec_sponsor_demo_stabilization.md
_DomainEngines/pec/WORKPLAN_2026-07-09_pec_team_information_hub.md
_DomainEngines/pec/WORKPLAN_2026-07-24_pec_coordination_plane.md
_DomainEngines/pec/_TaskManagement
```

## Findings

- SHA/blob pins: exactly one, `execution/_Evaluation/CHIRALITY_PROGRAM_ARCH_META_FANIN_2026-07-26_DA31C19/source_reviews/independent_managed/FROZEN_BASIS_MANIFEST.json`
  (`git_blob` `503f70dbc00127d844e3a0327ed47655a9142278`). It is a frozen
  historical evaluation basis, not a live mirror; it must not be edited.
- No pins under `projects/*/execution/_Reconciliation/References/**`,
  `projects/*/_harness/**`, or `_DomainEngines/**` (no `_harness` directory
  exists under `_DomainEngines`). App `AUTHORITY_CORPUS.json` does not
  reference the file (0 occurrences).
- Non-pin path references (tests/tools that read the live file by name,
  not by hash): `runtime/tests/helpers.ts:9`;
  `projects/chirality-app-dev/frontend/src/__tests__/lib/coordination-tools.test.ts:31`;
  `projects/chirality-app-dev/frontend/src/__tests__/integration/runtime-desktop-cli-shared-daemon.integration.test.ts:74,88`;
  `tools/validation/validate_instruction_entrypoints.py:239`;
  `tools/validation/test_validate_agent_instructions.py:160,179` (fixtures);
  `domains/chirality/_Decomposition/source_*/SRC-AGENTS-AGENT-HELP-HUMAN_*.json`
  (decomposition dispatch artifacts).
- PEC coordination surface: `_DomainEngines/pec/` has no notice inbox
  (`LOOP_INIT.md`, `LOOP_RECEIPTS.md`, workplans, `_TaskManagement` only).
  Prior root notices addressed to domain engines were placed at
  `_DomainEngines/_Coordination/`, so this tranche's domain-engine notice is
  written there:
  `_DomainEngines/_Coordination/NOTICE_2026-08-16_ROOT_AGENT0_DIRECT_A2_DISPATCH_ALIGNMENT.md`.

## Notices shipped

- `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-16_ROOT_AGENT0_DIRECT_A2_DISPATCH_ALIGNMENT.md`
- `projects/chirality-piping/execution/_Coordination/NOTICE_2026-08-16_ROOT_AGENT0_DIRECT_A2_DISPATCH_ALIGNMENT.md`
- `_DomainEngines/_Coordination/NOTICE_2026-08-16_ROOT_AGENT0_DIRECT_A2_DISPATCH_ALIGNMENT.md`
