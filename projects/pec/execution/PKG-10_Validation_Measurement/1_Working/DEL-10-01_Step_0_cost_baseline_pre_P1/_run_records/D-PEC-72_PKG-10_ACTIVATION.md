# D-PEC-72 — PKG-10 activation record

- RunID: `D-PEC-72-PRE-P1-FOUNDATION`
- InstanceID: `D-PEC-72-PKG-10-WI-01`
- PackageID: `PKG-10`
- Package path: `projects/pec/execution/PKG-10_Validation_Measurement`
- Selected deliverable: `DEL-10-01`
- Accepted basis: `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md`, revision 1.3, accepted through SCA-003
- Approval reference: D-PEC-72, owner-ruled O-B on 2026-08-01
- ResponsibleParty: `TBD` (the owner named no accountable human)
- Execution posture: serialized single-operator integration; no child session

## Objective

Publish a repeatable Step-0 token-cost method and a pre-P1 baseline report.
Report the PRD metric and the practitioner harness's original `self-check`
latency observation as distinct measures. Exact per-orientation token
telemetry is mandatory; absence is recorded as a limitation and blocks
acceptance without permitting estimates.

## Allowed writes

- `DEL-10-01.../artifacts/STEP0_COST_BASELINE_METHOD.md`
- `DEL-10-01.../artifacts/STEP0_COST_BASELINE.md`
- `DEL-10-01.../_run_records/D-PEC-72_*.md`
- D-PEC-72 shared coordination targets named by the ruling packet

No harness source, cache, behavior-owning package, lifecycle file, dependency
register, decomposition surface, PRD, or implementation source is open.

## Work graph v1

Posture: serialized direct production and package fan-in. Nodes:

1. `M-METHOD`: freeze the PEC-loop-only sampling and token-boundary method.
2. `M-CAPTURE`: attempt exact token capture and separately measure current
   `self-check` latency; depends on `M-METHOD`.
3. `M-REPORT`: publish observed values and explicit limitations; depends on
   `M-CAPTURE`.
4. `V-PKG10`: validate classification, citations, path containment, and the
   prohibition on fabricated token counts; depends on `M-REPORT`.

Missing exact token telemetry holds DEL-10-01 at candidate/unaccepted and
therefore leaves C-05 open. It does not invalidate the latency observation or
the method artifact.

## Entry gate

`pec_reliance_hold.py --operation dispatch-for-production` returned `ALLOW`
for the selected contract on 2026-08-01. Fan-in requires the same preflight.
