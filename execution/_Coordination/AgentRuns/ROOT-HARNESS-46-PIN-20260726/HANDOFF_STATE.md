# Handoff State — ROOT-HARNESS-46-PIN-20260726

- Accepted instruction basis:
  `ff04694afa709856a58f9f54a79ca2056b8e0b4e`
- Project Setup predecessor candidate:
  `dd28d201b8bc7c7fb534cf6ff75817da25023120`
- Candidate branch: `codex/root-project-setup-del-02-06`
- Pull request: `#369`
- Authority status: bounded owner-directed M2 candidate; not integrated by
  this return
- Derivative-package status: run records and manifest current for the
  candidate bytes; public-export regeneration explicitly deferred
- Closure verdict: `READY_FOR_CHANGE_CLOSEOUT`
- Blockers: none within the authorized M2 pin refresh

## Accepted upstream and SCC posture

The pin consumes the 46-file Project Setup candidate and the accepted
instruction basis at `ff04694`. The state and static pin form an atomic
acceptance SCC: the state-only candidate fails its old 45-file pins, and the
46-file pin cannot pass against the 45-file accepted base. The change must be
a separate commit within PR #369; neither half may merge independently.

## Rerun requirements

Before Git closeout:

1. verify the working-tree writes are exactly the one bounded test file, one
   G4 manifest, and this run-record directory;
2. rerun the complete practitioner-harness suite;
3. rerun all G0–G4 tests and live validators;
4. directly validate the new manifest;
5. prove actual instruction-path coverage with the G4 predicates;
6. exercise the pin-only candidate against `ff04694` and require failure;
7. require `git diff --check` to pass; and
8. record exact SHA-256 hashes and the read-only adversarial verdict.

After those checks, HELP_HUMAN may create one separate pin-refresh commit,
push the existing branch, and continue PR #369's human-gated closeout. This
handoff authorizes no change to the prior Project Setup commit or its
execution/audit/scaffold state.

## Recorded non-gating residual

`execution/_harness/adapter.yaml` retains a preamble line attributing the
repin to D-GOV-21 step-9 materialization on 2026-07-25 immediately before its
correct SCA-001 revision-1.1 / DEL-02-06 facts. Adapter-state edits are
expressly excluded from this M2 lane. PROJECT_SETUP owns any later
owner-authorized prose-only correction; the live values `46`, `0`, and
`2db2c712...` are correct and all deterministic adapter checks pass.
