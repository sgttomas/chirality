# Interpretation — App Agentic Runtime and Failure Properties

Claim posture: `DESCRIPTIVE INFERENCE FROM ONE GOVERNED SESSION`.

The deterministic source is `snapshot/summary.json`; the event-level evidence
is `snapshot/events.csv`. This interpretation does not change the accepted
Stage-2 plan or authorize a workflow change.

## What the run establishes

The App ordinary-conversion population closed 47/47 candidates, 1,428 claim
mappings, 15,386 source lines, and 47/47 isolated apply/rollback simulations.
No cataloged episode changed candidate meaning or produced a substantive
candidate rejection. A zero count in 47 observations has a 95% Wilson upper
bound of 7.6%; it is evidence of high observed reliability, not proof that the
true failure probability is zero.

The three Git-bounded activation-to-merge envelopes total 46,420 seconds
(12.894 hours), or 3.645 accepted members per elapsed hour. Preparation to
evidence binding accounts for 43,903 seconds (12.195 hours); merge/CI lag is
2,517 seconds (41.95 minutes). A1 achieved 4.010 members/hour; A2 and A3 were
3.509 and 3.483. A2 and A3 are effectively flat, while A1 was about 13% faster
than A3. Package composition, concurrency, evidence schema changes, and
runtime pressure are confounded, so this is not evidence of model-context
drift by itself.

## Failure shape

The catalog binds 43 abnormal episodes:

- evidence terminalization: 16 episodes;
- evidence portability: 11;
- project-check substrate: 7;
- brief/input binding: 5;
- tool invocation: 2;
- malformed negative fixture: 1; and
- suspected terminal defect not reproduced: 1.

Terminalization plus portability account for 27/43 episodes (62.8%). Adding
the missing-server project-check failures yields 34/43 (79.1%) in evidence or
execution substrate rather than candidate semantics. Portability rework
appeared in nine of ten packages. Fourteen child statuses explicitly record
manager evidence closeout; all fourteen are in A3, equal to 43.8% of A3's 32
baseline author/verifier roles. Earlier waves used heterogeneous status
schemas, so that late-wave concentration is real for the explicit label but
must not be treated as a clean longitudinal failure-rate comparison.

Manager fan-in/supervision detected or disposed 26/43 episodes. RECON detected
one package-level portability defect that survived an earlier normalization.
The latter is a small count but direct evidence that aggregate independent
reproduction was not redundant in this run.

## Test runtime and redundancy

The ten packages recorded 67 project-check invocations: 60 PASS and seven
FAIL. Every failure was `frontend-premerge` running without its required local
server; all seven ran zero tests and passed after the server-backed rerun. The
six timed failures consumed only 0.995 seconds. The expensive cost was the
successful repeated suite: 951.714 recorded seconds across 60 timed
invocations, with seven additional untimed invocations. `harness-pytest`
alone consumed 620.446 seconds (65.2% of recorded check time).

A counterfactual cache retaining one successful invocation per wave/check
would reduce 67 invocations to 18 (73.1%) and avoid at least 620.653 measured
seconds (10.34 minutes). Even if fully serial, that lower-bound saving is only
1.34% of the 12.894-hour wave envelope. Therefore project-test deduplication
is worthwhile hygiene but is not the main runtime opportunity.

## Perspective and recommended optimization order

1. Make terminalization deterministic. A registered finalizer should validate
   required terminal fields, construct the self-excluding manifest, rehash it,
   and fail before an agent returns. This targets the largest recurring defect
   class and the strongest late-session symptom.
2. Emit portable evidence natively. Evidence writers should use repository
   relative or declared portable anchors at creation time. Reversible
   after-the-fact normalization should become exceptional.
3. Make the premerge runner own its substrate. Start/health-check/stop the
   required stub server inside the registered check so a missing listener is
   not rediscovered in 70% of packages.
4. Batch author and verifier sessions by package while preserving fresh
   verifier judgment. Method #1 required 94 baseline child roles and produced
   99 documented attempt directories. A two-session-per-package posture would
   nominally reduce the baseline from 94 to 20 sessions (78.7%), far larger
   than test-command caching, subject to the already demonstrated context-size
   limit and full per-member evidence.
5. Cache unchanged project checks once per exact wave input/environment and
   retain a complete post-integration run. Do not cache semantic review,
   member-specific preservation, apply/rollback simulations, or aggregate
   evidence integrity.
6. Preserve RECON but narrow it to high-value seams: full manifest rehash,
   cross-package aggregation, portability, apply/rollback, and selected
   independent member reproduction. Its one caught escape demonstrates why
   removing the layer outright would be premature.

The fresh per-deliverable verifiers rejected no accepted candidate for a
semantic or preservation defect. That supports batching the verifier work; it
does not yet support deleting independent verification. The observed zero has
limited power, and the verifier also supplies a fresh no-repair judgment that
the author cannot provide about itself.
