# D-PEC-69 — PRD v2.2 / SCA-003 ScopeOfWork reconciliation activation

**Status:** RULED AND EFFECTIVE ON MERGE
**Date:** 2026-07-28
**Activation basis:** `main@b0b673dc3d65a4cfff9a045fda6c1fefa060645c`
**Method:** `docs/DELIVERABLE_CONCORDANCE_METHOD.md` revision 1,
SHA-256 `abf3e78fce606c4557d61cdbfbdb7292a3d858838f6526da6b433d1bcd0ef627`
**Manager:** `RECONCILIATION` (`agents/AGENT_RECONCILIATION.md`,
SHA-256 `46bca06f907c4da765b1b1177ecd51c6858fdf45bf7620341175c3b847a3e4f7`)
**RunID:** `PEC_SOW_V22_SCA003_RECON_2026-07-28`

## Purpose

Activate one bounded deliverable-corpus reconciliation over the complete
current PEC `ScopeOfWork.md` contracts affected by PRD v2.2 and SCA-003.
Execution-time claim extraction and semantic comparison govern the final
population. The expected population is:

- `DEL-00-01`
- `DEL-03-06`
- `DEL-04-01`
- `DEL-04-02`
- `DEL-08-01`
- `DEL-08-03`
- `DEL-08-04`
- `DEL-10-01`
- `DEL-10-10`
- `DEL-10-11`

The run must prove that DEL-00-01 no longer asserts the retired ADR-014
PEC-project-adapter allocation and that PEC-K-03/-11 consumer-interface
boundaries are reflected without adding product scope, receiving-loop duty,
cadence, injection requirement, or conformance condition.

## Frozen basis at activation

| Surface | Identity |
|---|---|
| PRD v2.2 | `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba` |
| SOFTWARE_DECOMP revision 1.3 | `3f65ea0e47036a2baa66cb60923f8b779525ae00d747425f93f8b69431151787` |
| ScopeLedger.csv | `3cca281f7019a4544b6d4e6ab631a30125429525106f5d65b16aac270ebd50f5` |
| Deliverables.csv | `b27ff4631f4966931990bbf9c033d2593d3dd8ac51b09e0d5112002b98afbc40` |
| Active reliance-hold register | `d92d134bdfe4466dc06292fa53fa44cf368d6be1dfeb04fefa6ce188bba8002a` |
| SCA-003 durable merge | `11a494e9ae0cca795aa460deec19b9eac4d922a8` |

Execution-time scans must re-measure these inputs and stop on material drift.

## Approved recommendations

Under the owner’s standing direction below, the following RECONCILIATION /
Agent 0 recommendations stand as the owner-approved calibration and routing
choices:

1. **R0:** activate the exact run and freeze the basis above; use current PEC
   contract schema/conventions and preserve contract structure.
2. **R1:** inventory all 64 deliverables and all complete active
   `ScopeOfWork.md` contracts; derive the affected population from claim text,
   accepted PRD/decomposition sources, and semantic comparison.
3. **R2:** use one bounded ten-member contract wave unless the execution-time
   scan changes the population; record claim-level findings and independent
   deterministic/semantic fan-in evidence.
4. **R3:** treat duplicate stale wording, retired ownership/allocation claims,
   forced polling/cadence/injection claims, and receiving-loop conformance as
   cross-contract defects; do not alter dependencies or deliverable identity.
5. **R4:** approve the smallest exact whole-contract repairs required to make
   the affected contracts concordant, with no new scope.
6. **R5:** authorize whole-contract rewrites only for contracts proven
   affected; preserve stable claim/requirement/acceptance/verification IDs and
   contract semantics not implicated by PRD v2.2 / SCA-003.
7. **R6:** backcheck every changed claim, validate the full active SOW
   population, strict registers, hold negative tests, manifests, containment,
   and a corpus-wide Remaining census; close only as evidence coherence.

## Exact write fence

- the execution-time-confirmed affected
  `projects/pec/execution/PKG-*/1_Working/DEL-*/ScopeOfWork.md` files;
- `projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_SOW_V22_SCA003_RECON_2026-07-28/**`;
- this decision record and its single register row;
- Git branch/commit/push/PR metadata for the activation and later repair
  tranches.

No `_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`, `Dependencies.csv`,
decomposition, PRD, implementation, runtime, lifecycle, release, estimate, or
schedule write is authorized.

## Reliance hold

`PEC-HOLD-001` remains active. Before dispatch, fan-in, review, promotion, or
reliance, the run must execute `pec_reliance_hold.py`. Only read-only
inspection and exact correction preparation permitted by the hold may
proceed. This decision does not release or weaken the hold.

## Verification and closure

- validate every complete active PEC SOW contract with the registered
  contract validators and full-population semantic checks;
- run strict decomposition-register validation;
- run the hold script’s negative tests and verify the active register is
  byte-identical;
- produce exact pre/post manifests, changed-claim multiset evidence,
  containment evidence, Remaining census, backcheck and handoff state;
- require clean candidate-whitespace and repository checks;
- open the repair PR against `main`, wait for required checks to be green, and
  stop before merge.

Closure creates no implementation, runtime, lifecycle, release, dependency,
estimate, schedule, professional-approval, or reliance authority.

## Human ruling

Owner direction of record:

> “Finish out your plan now (attaining your goal) with self merge of PRs and
> auto approve for owners rulings, which should still be recorded in the usual
> manner with your recommendation standing as what I approved.”

Agent 0 applied that standing direction to this exact PEC reconciliation:
reconcile the complete current affected contract population, preserve the
active hold and stated exclusions, record recommendations as approved, and
perform Git closeout with a stop before final merge.

Accordingly, the seven recommendations above are the owner-approved
activation ruling. The ruling becomes effective when this record and register
row are durable on shared `main`; no target-contract discovery or repair may
precede that merge.

## Rollback

Before activation merge, remove this new record and register row. After merge,
use a separately approved successor decision; do not rewrite this ruling.
