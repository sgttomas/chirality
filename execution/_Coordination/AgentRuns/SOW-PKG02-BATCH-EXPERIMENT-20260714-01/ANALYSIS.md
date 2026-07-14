# PKG-02 Batch Experiment — Consolidated Analysis

Status: `COMPLETE — PASS_WITH_RETAINED_PROCESS_FINDINGS`

## Answer

Method #2 again met the previously defined sufficient-quality level. One
package-wide author and one fresh package-wide verifier processed five related
deliverables with complete, independently reconciled faithful-representation
evidence. No candidate-quality failure, source loss, clean-finalization
mismatch, semantic expansion, cross-member contamination, project write, or
late-batch degradation was observed.

This result extends the empirical bound from PKG-01's three members / 727
source lines to five members / 2,053 source lines. It does not establish an
unbounded safe package size because native token/context occupancy remained
unavailable.

## Comparative statistics

| Measure | PKG-01 | PKG-02 | Combined |
|---|---:|---:|---:|
| Members | 3 | 5 | 8 |
| Mappings | 88 | 186 | 274 |
| Source lines | 727 | 2,053 | 2,780 |
| Replacement/inverse rows | 15 | 25 | 40 |
| Simulations | 3 | 5 | 8 |
| Actual Agent-2 sessions | 2 | 2 | 4 |
| Nominal per-deliverable sessions | 6 | 10 | 16 |
| Session reduction | 66.7% | 80.0% | 75.0% |
| Candidate-quality failures | 0 | 0 | 0 |
| Observable late-member retries | 0 | 0 | 0 |

PKG-02 was 1.67 times larger by member count, 2.11 times larger by mappings,
and 2.82 times larger by source lines than PKG-01. It preserved the same
quality outcome while using the same two Agent-2 sessions.

The PKG-02 verifier's successful per-member durations were 0.874, 1.021,
1.011, 1.043, and 1.014 seconds. There is no increasing position trend.
Position five was also the largest member at 455 source lines and retained its
complete evidence family without slowdown or abbreviation.

## Failure properties

PKG-02 retained seven grouped process findings / nine atomic items. Eight
atomic items were actual runtime/process defects; the remaining item was a
non-failing portable-manifest style variance. They consisted of shell/platform
assumptions, one telemetry-integrity correction, three verifier harness-schema
assumptions, one event-schema assumption, and one incorrect negative fixture.

These are real efficiency costs, but they are not evidence of context drift:

- all verifier retries and the manager fixture stop occurred at member one;
- members two through five had zero verifier failures and retries;
- no defect changed a candidate, weakened a gate, or affected project state;
- fresh exception-member and final/largest-member reproduction passed
  byte-for-byte; and
- the full 264-test harness and all five apply/rollback simulations passed.

PKG-01 recorded five contained setup/harness findings under a coarser taxonomy.
The two raw finding counts are therefore not a reliable comparative defect
rate. The common pattern—startup/interface defects with zero late-member
quality degradation—is the defensible cross-run inference.

The root runtime ledger undercounts child-local defects and must not be used as
the total failure count. Likewise, the author, verifier, and manager session
envelopes overlap and must not be summed. PKG-01 lacks comparable runtime
telemetry, so no statistically sound wall-clock, token, or cost saving is
claimed.

## Independent evidence

RECONCILIATION rehashed all 1,811 upstream manifest rows, reproduced all 186
mappings and 2,053 source lines, verified exact 25-row replacement/inverse
closure and 5/5 simulations, and found zero scoped project diff. It fully
reproduced the exception-bearing first member and final/largest fifth member;
both matched evidence, clean output, and finalization reports byte-for-byte.
All 14 fresh negative probes failed closed.

## Inference and recommendation

The evidence now supports adopting the package-wide author plus fresh
package-wide verifier pattern for related packages up to the observed bound of
five members / approximately 2,053 source lines, while retaining:

1. complete per-member deterministic evidence rather than sampling;
2. numeric sequential processing and brief rereads at member boundaries;
3. a fresh verifier prohibited from repair;
4. explicit runtime/attempt telemetry with append-only corrections;
5. independent RECONCILIATION of all exceptions plus the final clean member;
6. automatic package-wide expansion on any sampled or aggregate failure; and
7. a hold or explicit continuation checkpoint when a package exceeds the
   observed five-member bound.

The remaining optimization opportunity is harness productization, not removal
of the fresh verifier. Most retained failures came from ad hoc shell/schema
assumptions that should be moved into registered, tested deterministic tools.
The verifier continued to supply independent value by proving unchanged
reconstruction and localizing failures to its own harness rather than the
candidate corpus.

This is a recommendation only. The standing Stage-2 plan and instructions were
not amended by this experiment.
