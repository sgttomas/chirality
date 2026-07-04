# Brief - PEC tier-0 registration prep

| Field | Value |
|---|---|
| **Human request** | Create a new development loop to implement `plans/pec_bridge_integration_plan_2026-07-04.md` for registering `projects/pec/` as a domain engine. |
| **Normalized action type** | `PROFILE_ADOPTION` prep + `FRAMEWORK_EXTENSION` + `BOUNDARY_AUDIT` |
| **Run nature** | Root-governance authoring plus the three sanctioned PEC-side coordination files. Not PEC runtime work and not a professional approval act. |
| **WORKING_ROOT** | `{REPO_ROOT}` resolved by `git rev-parse --show-toplevel` |
| **DOMAIN_ENGINE_ID** | `pec` |
| **Profile** | `_DomainEngines/pec/profile/pec.DRAFT.yaml` |
| **Integration level** | `MANUAL_BRIDGE` (L0) today |
| **Tools invoked** | Repo-wide harness self-check; profile validator; closeout tests listed in `RUN_SUMMARY.md`. No PEC server and no non-scratch PEC DB command. |
| **Write scope this run** | Tier-0 registration surfaces under `_DomainEngines/pec/**`, `_DomainEngines/proposals/pec/**`, `_DomainEngines/_DECISIONS/**`, `DOMAIN_ENGINE_INDEX.md`, harness backlog/live-baseline pins, plus `projects/pec/AGENTS.md`, `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md`, and one `projects/pec/docs/STATUS.md` pointer section. |
| **Permissions** | DRAFT/PROPOSAL authoring only. Owner gates remain open. No `HumanRuling` filled. No profile adoption. No release, residency, or harness-tranche execution. |
| **Expected outputs** | Staged DRAFT profile, validation report, prep snapshot, six D-T0 packets, tier-0 register rows, PEC-side register, PEC AGENTS, STATUS pointer, proposals surface, and harness-tranche backlog/brief. |

## Inputs read

- Loop protocol and receipts: `_DomainEngines/pec/LOOP_INIT.md`,
  `_DomainEngines/pec/WORKPLAN_2026-07-04_pec_loop.md`,
  `_DomainEngines/pec/LOOP_RECEIPTS.md`.
- Work specification: `plans/pec_bridge_integration_plan_2026-07-04.md`.
- Tier-0 governance: `_DomainEngines/DOMAIN_ENGINE_INDEX.md`,
  `_DomainEngines/_DECISIONS/_REGISTER.md`,
  `_DomainEngines/profiles/open_pipe_stress.yaml`.
- Cross-loop scope awareness: `_DomainEngines/bridge/LOOP_RECEIPTS.md`.
- Harness implementation facts: `tools/practitioner_harness/adapter_domain_engines.py`,
  `tools/practitioner_harness/harness.py`,
  `tools/practitioner_harness/cmd_bridge_status.py`,
  `tools/practitioner_harness/cmd_self_check.py`,
  `tools/practitioner_harness/test_live_baseline.py`.
- PEC project facts: `projects/pec/docs/STATUS.md`, `projects/pec/docs/SPEC.md`,
  `projects/pec/docs/TRACEABILITY.md`, `projects/pec/package.json`,
  `projects/pec/server/src/index.ts`, `projects/pec/server/src/import/index.ts`,
  `projects/pec/tools/backup.ts`, `projects/pec/tools/pilot-drill.ts`,
  and `projects/pec/core/src/lifecycles.ts`.

## Live deltas recorded by this prep

- `init/init-prompt.md` already had the PEC launcher as ACTIVE in the live tree,
  ahead of the older plan row that expected a STAGED label.
- The companion plan path named by `plans/pec_bridge_integration_plan_2026-07-04.md`
  is absent in this tree; this package relies on the surviving registration plan
  plus live sources.
- Repo self-check is invoked through `python3 tools/practitioner_harness/harness.py self-check`;
  there is no standalone `tools/practitioner_harness/self_check.py`.

