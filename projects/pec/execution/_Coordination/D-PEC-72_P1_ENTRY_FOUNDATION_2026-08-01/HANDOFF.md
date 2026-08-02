# D-PEC-72 execution handoff — P1-entry foundation

**Handoff state:** PARTIAL CANDIDATE FAN-IN; REVIEW NOT LAUNCHED; C-05 OPEN.

**Accepted upstream snapshots:** PEC PRD v2.2; SOFTWARE_DECOMP revision 1.3
accepted through SCA-003 at `11a494e9a`.

**Derivative-package status:** this handoff and its manifest are derivative
execution evidence. They do not replace the selected deliverables' contracts,
the accepted decomposition, or the PRD.

## Authority and execution commits

| Act | Commit |
|---|---|
| D-PEC-72 O-B ruling + activation records | `19404e7bd2f1b365452114ad75aef042fa02b180` |
| PKG-00 candidate production | `5942c50333c5cbd1e9b77e72c79c11bf46051040` |
| PKG-10 candidate production / limitation record | `5d3fd5bb3537de484b98dd101881ae426e0d0f8a` |

## Candidate fan-in

| Deliverable | Output | Producer-side result | Remaining gate |
|---|---|---|---|
| DEL-00-01 | `.../DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/artifacts/v2/ADRs.md` | Candidate validation PASS; O-B selection recorded; no lifecycle effect | Formal REVIEW, then owner fitness acceptance of the authored bytes |
| DEL-00-03 | `.../DEL-00-03_v2_SPEC_seed/artifacts/v2/SPEC.md` | Candidate validation PASS; all explicit identifiers resolved; no lifecycle effect | Formal REVIEW, then owner confirmation as SPEC of record including LOW-confidence OBJ-001 attribution |
| DEL-10-01 | `.../DEL-10-01_Step_0_cost_baseline_pre_P1/artifacts/STEP0_COST_BASELINE_METHOD.md` and `STEP0_COST_BASELINE.md` | Method and latency evidence candidate PASS; exact token baseline BLOCKED (`NOT_OBSERVED`) | Rerun in a runtime exposing exact interval-bound usage, then REVIEW and owner acceptance |

The abbreviated paths above all resolve under
`projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/` or
`projects/pec/execution/PKG-10_Validation_Measurement/1_Working/` respectively.
Exact paths and hashes are in `MANIFEST.sha256`.

## Architecture disposition

The PEC ADR selects ports-and-adapters / hexagonal isolation at PEC's bounded
application boundary. Capability-shaped typed contracts isolate the core from
transport, persistence, filesystem/Git, runtime-client, event, and presentation
adapters. Functional-core / imperative-shell remains compatible inside the
bounded application. The entity schema is core-facing and physical store
persistence is an adapter inside the PKG-01 seam.

The owner's broader goal—interchangeable App, Root, PEC, Task Management, and
domain applications communicating through typed contracts—is recorded as the
selection rationale. D-PEC-72 creates no cross-loop mandate; each other loop
needs its own owning instrument.

## Measurement limitation

The method requires exact provider/runtime input, cached-input, and output
usage for the orientation interval. The live task exposed no such ledger and no
exact interval locator. The report therefore records `NOT_OBSERVED`, never an
estimate. The separate harness re-test recorded five `self-check` wall times:
3.34, 2.81, 2.78, 2.70, and 2.64 seconds (median 2.78; mean 2.854). The
historical source has no numerical pain threshold, so the result does not
re-rule or direct the harness cache.

## Validation summary

- Reliance-hold preflight: `dispatch-for-production` ALLOW ×3;
  `candidate-validation` ALLOW ×3.
- All three `ScopeOfWork.md` contracts: valid `SOW_V1`; deterministic REVIEW
  checklists derived (7, 11, and 8 criteria).
- SPEC identifier resolution: zero unresolved identifiers.
- Strict decomposition registers: 64 registers / 254 rows / zero findings.
- Dependency closure: 64 files / 254 rows / 119 execution edges / zero SCCs.
- Practitioner-harness `self-check`: exit 0; unchanged baseline
  INFO=15 / NOT_APPLICABLE=1 / REVIEW=5 / WARN=28.
- Preliminary committed-range `coord-check`
  (`90c2c4727..5d3fd5bb3`): no D-PEC-72 packet/register-coverage,
  precedent, or absolute-path finding; two REVIEW findings are carried from
  pre-existing register rows (`projects/pec/pilot-scratch/reports/` and
  `SEED_D-PEC-62/RUN_LOG.md`), the same inherited pair recorded by Receipt 121.
- Package production commits are disjoint and path-contained; no frozen source,
  profile, dependency, decomposition, PRD, lifecycle, runtime, or P1 source
  path changed.

## Rerun and next gates

1. For DEL-00-01 and DEL-00-03, the owner selects the REVIEW type at Gate 1;
   `PEER_REVIEW` is the non-binding recommendation. Both are currently
   `INITIALIZED`, so formal REVIEW also requires the owner's explicit Gate-1
   override to review candidate outputs from that state.
2. DEL-10-01 reruns only when exact token telemetry is available. A revised
   packet would be required to waive or replace that accepted criterion; this
   run does not propose such a waiver.
3. Only after REVIEW and separate owner acceptance of all three deliverables
   may lifecycle changes and C-05 closure be proposed.
4. The first P1 source slice remains a successor D-PEC packet and must name
   the v2 source tree and project-local `software-workflow.json`.

No `docs/STATUS.md` update is made because D-PEC-72 permits it only after all
three owner acceptances.
