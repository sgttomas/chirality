# Artifact Inventory - PEC tier-0 registration prep

| Artifact | Role | Status |
|---|---|---|
| `_DomainEngines/pec/profile/pec.DRAFT.yaml` | Staged domain-engine profile | DRAFT |
| `_DomainEngines/pec/profile/_validation/pec.validation.json` | Deterministic validator report | Evidence; not adoption |
| `_DomainEngines/pec/PEC_2026-07-04_tier0-prep/` | Immutable prep snapshot | Derivative package |
| `_DomainEngines/_DECISIONS/D-T0-11_pec_registration_shape.md` | Owner decision packet | RULED O-A; publication pending PR #51 merge |
| `_DomainEngines/_DECISIONS/D-T0-12_pec_profile_lifecycle.md` | Owner decision packet | RULED O-A; Gate 2 remains open |
| `_DomainEngines/_DECISIONS/D-T0-13_pec_integration_staging.md` | Owner decision packet | RULED O-A; residency still gated by D-T0-14 |
| `_DomainEngines/_DECISIONS/D-T0-14_pec_data_residency.md` | Owner decision packet | RULED deferred; O-A CLOSED default |
| `_DomainEngines/_DECISIONS/D-T0-15_pec_loop_goal_fences.md` | Owner decision packet | RULED O-A |
| `_DomainEngines/_DECISIONS/D-T0-16_pec_harness_tranche_authorization.md` | Owner decision packet | RULED O-A; execution held for PR #51 merge and riders |
| `_DomainEngines/proposals/pec/.gitkeep` | Empty OperationProposal surface | Placeholder |
| `projects/pec/AGENTS.md` | PEC project agent index and domain-engine boundary | DRAFT |
| `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md` | PEC-local human decision tracking | Non-governing register |
| `projects/pec/docs/STATUS.md` | Existing PEC handoff file with governance pointer | One-time pointer edit |
| `tools/practitioner_harness/BACKLOG.md` | Queues D-T0-16 harness tranche | Authorized but held for PR #51 merge |

## Protected paths not touched

This prep does not write `projects/pec/pec.db*`, `projects/pec/backups/**`,
`projects/pec/core/**`, `projects/pec/server/**`, `projects/pec/web/**`,
`projects/pec/tools/**`, `projects/pec/fixtures/**`, root PEC manifests, the
adopted `open_pipe_stress` profile, `_DomainEngines/_LATEST.md`,
`_DomainEngines/RULINGS_PUBLISHED.md`, `_DomainEngines/NEXT_INSTANCE_PROMPT.md`,
or `_DomainEngines/bridge/**`.
