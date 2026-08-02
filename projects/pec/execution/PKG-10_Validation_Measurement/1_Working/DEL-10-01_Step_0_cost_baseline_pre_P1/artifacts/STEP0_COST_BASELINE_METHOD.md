# PEC Step-0 cost baseline method

**Artifact authority boundary:** repeatable measurement method v1.0. Lifecycle
and artifact-fitness state are recorded by their owning governance surfaces.

**Deliverable:** DEL-10-01; **scope item:** SOW-058; **basis:** PRD v2.2 §11
metric 1 and accepted decomposition revision 1.3.

[METHOD] Classification rule: prose, tables, and list items inherit the most
recent `[METHOD]`, `[VALUE]`, or `[LIMIT]` label within their section until a
new label appears.

## 1. Measurement questions

[METHOD] This method reports two different observations without substituting
one for the other:

1. the PRD metric: exact LLM tokens used for one PEC loop-iteration
   orientation; and
2. the practitioner harness's original query-pain observation: wall-clock
   latency of `self-check`, recorded at approximately four seconds on
   2026-07-02 (`tools/practitioner_harness/README.md` §Cache contract;
   `projects/pec/docs/PRD.md` §§2, 11, and 15).

The token observation is the baseline required to compare pre-P1 with post-P1.
The command-latency observation is a re-test of the historical precondition;
it is not a token proxy and does not direct or open the harness cache.

## 2. Unit and sampling population

[METHOD] One measurement unit is one **PEC loop-iteration orientation**: the
interval beginning when a fresh operator receives the instruction to resume
the PEC loop and begins LOOP_INIT Step 0, and ending when that operator emits
the first substantive live orientation return naming Git state, applicable
receipt, owner directions, live gates, lawful tranches, and parked lanes.

[METHOD] The sampling population is PEC-loop-only. It excludes Root, App,
Piping, Task Management, and domain-application orientations and creates no
duty for those loops.

[METHOD] The pre-P1 baseline design uses one eligible PEC orientation
(`n = 1`) captured before any P1 node begins. The post-P1 comparison must use
the same unit, the same inclusion boundary, and one or more PEC orientations;
it must report its own sample count and may compare only like-for-like rows.

## 3. Exact token-counting boundary

[METHOD] For each orientation, obtain the provider/runtime's exact usage
record for every model call whose content contributes to the defined interval.
Record, without estimation:

- `input_tokens_total`, including instruction stack, conversation context,
  tool results returned to the model, and any other provider-counted input;
- `cached_input_tokens` as a disclosed subset of input when the runtime
  exposes it;
- `output_tokens`, including tool-call arguments and the orientation return;
- `logical_total_tokens = input_tokens_total + output_tokens`.

[METHOD] Do not add cached input twice. When a provider reports uncached input
and cached input as disjoint classes, first form
`input_tokens_total = uncached_input_tokens + cached_input_tokens`, then add
output. Preserve the provider's raw class names beside the normalized fields.

[METHOD] Exclude calls wholly before the loop-resume instruction and calls
wholly after the first substantive orientation return. Do not subtract system
instructions, tool results, retries, or failed calls that the provider counts
inside the interval; they are part of the orientation cost. Record the exact
Git SHA, UTC window, loop/scope, provider/model/runtime identifier, and usage
record locator for every row.

[LIMIT] If the runtime does not expose exact usage for every counted call and
token class, the row is `NOT_OBSERVED`. Estimates, word-to-token conversion,
context-window backsolves, billing approximations, and fabricated zeroes are
prohibited. Any `NOT_OBSERVED` token row blocks baseline acceptance and leaves
C-05 open.

## 4. Capture procedure

[METHOD]

1. Confirm that no P1 node has started and record the current Git SHA.
2. Identify one fresh PEC-loop orientation and record its UTC start/end.
3. Export or cite the runtime's exact per-call usage records for the interval.
4. Normalize input, cached-input, and output classes under §3 without
   estimation; retain the raw values and class names.
5. Publish one table row per orientation and compute summary statistics only
   over exact observed rows.
6. Separately run five sequential read-only invocations of
   `python3 tools/practitioner_harness/harness.py self-check` from the same
   checkout, measuring wall time with `/usr/bin/time -p` and discarding the
   generated stdout report. Record all five values, median, range, Git SHA,
   Python version, OS/kernel, and UTC capture time.
7. Compare the latency distribution descriptively with the historical
   approximately-four-second observation. Because the historical source
   records no numerical pain threshold, do not invent one or make a new cache
   decision.

## 5. Repeatability and comparison

[METHOD] A second party repeats the token measurement by applying §§2–4 to a
fresh PEC orientation and retrieving exact provider/runtime usage for the same
interval. The post-P1 measurement uses this method unchanged. Report corpus
SHA, model/runtime, cache class, sample count, and observation window so model,
corpus, or runtime changes remain visible rather than silently normalized.

[METHOD] A second party repeats the latency observation from the repository
root with the exact command and five-run sequence in §4. The latency measure
is reported separately in seconds and is never converted into tokens.

## 6. Declared limitations

[LIMIT]

- One pre-P1 orientation is a baseline observation, not a population estimate.
- Token cost varies with instruction stack, prior context, model/runtime,
  provider caching, tool output size, corpus state, and the live gate surface.
- The method does not measure correctness, operator elapsed time, API latency,
  PEC adoption, or another loop's cost.
- `self-check` wall time measures a deterministic harness command, not LLM
  orientation cost. The 2026-07-02 record supplies no formal pain threshold.
- A missing exact token record is evidence of a measurement limitation, not
  evidence of zero tokens.

## 7. Acceptance boundary

[LIMIT] The method can be reviewed independently of a successful capture, but
DEL-10-01 cannot be accepted until every baseline sample contains exact token
values and the owner confirms the baseline is fit as the PRD §11 “before” leg.
No output of this method changes the harness, another package, lifecycle state,
or the PRD falsification verdict.
