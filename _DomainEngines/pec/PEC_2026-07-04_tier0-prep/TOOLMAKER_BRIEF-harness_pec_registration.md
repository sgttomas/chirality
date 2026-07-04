# TOOLMAKER Brief - PEC harness registration tranche

**Status:** AUTHORIZED by D-T0-16, execution-held until PR #51 merges and the
D-T0-11/D-T0-12 ruling records are published. Do not execute this brief in the
registration PR.

## Goal

Make the practitioner harness safe for multiple domain-engine profiles, then
register PEC in the harness read/status surfaces without giving PEC full
`status`/`drift`/`next`/`brief --project pec` citizenship prematurely.

## Required changes

| Surface | Candidate change |
|---|---|
| `tools/practitioner_harness/adapter_domain_engines.py` | Replace the single-observation overwrite behavior with keyed observations per profile id. Preserve `open_pipe_stress` behavior and make adapter facts profile-scoped. |
| `tools/practitioner_harness/harness.py` | Add project aliases `pec` and `chirality-pec` for `projects/pec`. |
| `tools/practitioner_harness/cmd_bridge_status.py` | Add the PEC decision register, staged/adopted profile candidates, and `projects/pec` to the bridge-status awareness set. Extend decision ID detection to include `D-PEC-XX`. |
| `tools/practitioner_harness/cmd_self_check.py` | Add `projects/pec` to scoped checks and reference resolution. Keep detect-never-rewrite posture. |
| `_DomainEngines/pec/profile/pec.DRAFT.yaml` | Move to `_DomainEngines/profiles/pec.yaml` only inside the authorized follow-on tranche, only after PR #51 has merged, and only after multi-profile safety is in place. The move must not imply adoption. |
| Tests | Extend bridge-status/self-check fixtures and update `test_live_baseline.py` pins consciously at the same final SHA, including assertions that PEC reports as DRAFT with Gate 2 open. |

## D-T0-16 owner riders

1. **Sequencing:** execute only after PR #51 merges and D-T0-11/D-T0-12 are
   ruled/published. The tranche moves the profile into `profiles/`, which
   presupposes the accepted registration shape and lifecycle rulings.
2. **DRAFT-in-`profiles/` representation:** bridge-status/self-check tests must
   assert PEC reports as DRAFT, Gate 2 open. Location in
   `_DomainEngines/profiles/` must never infer ADOPTED status.

## Explicitly out of scope

- No `cmd_status`, `cmd_drift`, `cmd_next`, or `brief --project pec` support
  unless a later PEC adapter/status convention exists.
- No PEC runtime dependency, no server start, no non-scratch DB mutation, and no
  release/egress act.
- No owner-ruling fields filled by the agent.

## Related future candidates

- `pec_drill_report_json`: machine-readable `npm run drill` report.
- `pec_import_report_schema`: publish ImportReport and Explain payload schemas.
- `pec_api_adapter`: bounded read-only capture CLI that requires project id,
  requested registers/reports, actor/visibility basis, approved immutable output
  directory, and byte-identical source DB proof.
- `pec_register_review`: recurring review method for the PEC-local decision
  register, writing only under `_DomainEngines/pec/**` unless otherwise ruled.

## Acceptance checks

- Existing bridge-status and self-check behavior remains green.
- `open_pipe_stress` live-baseline assertions remain intentional.
- PEC profile validation remains VALID after move.
- PEC is rendered as DRAFT with Gate 2 open after the profile move.
- Full practitioner harness pytest passes at the final commit SHA.
