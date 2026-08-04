# E3 independent refutation — TM-ROOT-112 semantic packet

Status: `COMPLETE / BLOCK / RETURN FOR REVISION`

## Binding check

All twelve SHA-256 bindings in `DISPATCH_INPUT.md` matched exactly: the six
manager drafts, E1 `RETURN.md`/`EVIDENCE.md`/two probe results, and E2
`RETURN.md`/`SOURCE_CONTRACT_MAP.md`. Current `runtime-daemon.ts` and
`daemon.test.ts` also match the hashes stated in the packet. No input drift was
found.

## Findings

### BLOCK-01 — alternate grace selections contradict the fixed 2,500 ms consequence

Evidence:

- `SEMANTIC_OPTIONS.json` offers G1=1,000 ms, G2=2,000 ms, and G3=4,000 ms,
  while `fixedConsequences.connectionGovernedTerminationMs` is always `2500`
  and `postForceSettleMs` is always `500` (lines 8-14, 36-45).
- The packet calls 2,500 ms a shared consequence accepted with *any* selection
  (`OWNER_SEMANTIC_DECISION_PACKET.md:127-140`).
- The alternate return accepts the selected grace plus those fixed JSON
  consequences (`OWNER_RETURN_TEMPLATES.md:34-45`). G1+500 is 1,500 ms and
  G3+500 is 4,500 ms, not 2,500 ms.

Impact: the advertised exactly-one alternate path can produce a signed ruling
with two incompatible production bounds. It is not jointly usable as written.

Exact repair criterion: make the connection-governed bound explicitly derived
as `selected productionGraceMs + postForceSettleMs`, or regenerate and
hash-bind a selection-specific numeric bound before signature. Remove the
unconditional `2500` from shared consequences, and ensure the alternate return
cannot accept a stale G2-only number with G1 or G3.

### BLOCK-02 — failed-stop recovery is undefined for interruption failures after successful cleanup

Evidence:

- N-STOP-6 requires a pending interruption at grace to be recorded as a
  timeout and requires `stop()` to reject after cleanup
  (`CANDIDATE_NORMATIVE_CLAUSES.md:81-86`).
- N-STOP-5 can nevertheless already have established settled transport and
  absent owned socket/owner (`:69-77`).
- N-STOP-6 then says every failed stop remains fail-closed for restart until a
  “later cleanup retry” establishes that same completion condition (`:86-89`),
  but does not define the retry entry point or what can clear a non-cleanup
  interruption failure. The scope map tests restart only after successful
  cleanup (`IMPLEMENTATION_TEST_SCOPE_MAP.md:18`).

Impact: after an interruption timeout/error with complete transport and
metadata cleanup, an implementation cannot determine whether restart is
immediately permitted, permanently barred, or enabled by a repeated `stop()`.
Different compliant-looking implementations would expose different lifecycle
semantics.

Exact repair criterion: define explicit post-failure states by failure class;
name the retry operation (for example, a repeated `stop()`); state exactly what
it retries; state the condition that clears fail-closed; and add bounded tests
for (a) interruption timeout/error with successful transport/metadata cleanup
and (b) actual unlink/owner/close cleanup failure. If all failures block
restart, define how a later call can ever discharge an already-recorded
interruption failure.

### REVIEW-03 — the exact 500 ms force-settle cap is an uncalibrated policy value

Evidence:

- The packet explicitly labels 2,000 ms a product-policy recommendation rather
  than a measured provider cutoff (`OWNER_SEMANTIC_DECISION_PACKET.md:32-39`).
- It presents 500 ms as a fixed consequence without the same calibration or
  rationale (`:27-28,127-135`; `RISKS_AND_CAVEATS.md`).
- E1 used an 80 ms observation boundary and expressly makes no timing claim
  beyond settled/pending (`EVIDENCE.md:185-190,297-308`); it does not establish
  500 ms as a Node settlement bound.

Exact repair criterion: state beside the decision and in risks that 500 ms is
also a human-selected product-policy cap, not an empirical Node guarantee;
state its intended tradeoff and consequence (timeout/rejection despite forced
socket destruction); and ensure the signed return expressly accepts that
uncertainty. If it is meant to be evidence-derived, supply supporting executed
evidence instead.

### REVIEW-04 — `start()`-during-`start()` is normative but absent from the test map

Evidence:

- N-STOP-6 requires `start()` to reject while either start or stop is in flight
  (`CANDIDATE_NORMATIVE_CLAUSES.md:87-91`).
- The Restart row requires only rejection during stop and does not observe
  concurrent start (`IMPLEMENTATION_TEST_SCOPE_MAP.md:18`).
- Current `start()` performs several awaits before assigning `this.server`, so
  this is a real source-level race rather than a redundant assertion
  (`runtime-daemon.ts:49-75`).

Exact repair criterion: add an in-scope lifecycle test/observation proving a
second start rejects while the first is in flight and leaves one listener and
one valid owner record, or remove that unapproved/unmapped normative obligation
for a separate ruling.

### REVIEW-05 — the pre-identity interruption latch has no terminal/generation rule

Evidence:

- N-STOP-3 requires a pre-identity Agent 1 request to stay latched and invoke
  interruption whenever identity later becomes available
  (`CANDIDATE_NORMATIVE_CLAUSES.md:30-39`).
- N-STOP-4 forbids the response/interrupt promise from holding stop after force
  (`:46-67`), and E2 establishes that a run iterator may never yield identity
  (`SOURCE_CONTRACT_MAP.md:88-92`).
- N-STOP-6 protects a restarted generation only from late close/error events,
  not from a late prior-generation identity/interruption callback (`:89-95`).

Exact repair criterion: define whether the latch expires at force, survives as
a detached observed task, or is otherwise disposed; define its generation
ownership; and add never-yields and yields-after-force tests that prove no
unhandled rejection, no duplicate interrupt, and no mutation of a restarted
listener/owner generation.

## Attempted refutations that did not succeed

- The recommended G2+C1+F1 ordering is supported as an implementation shape on
  bound Node v24: close stops admission, bulk close covers tested ordinary HTTP,
  and tracked destruction covers the tested upgrade residual. The evidence does
  not establish the selected timing values, and the packet mostly preserves
  that distinction.
- Each dimension syntactically declares `EXACTLY_ONE`, and the three mechanisms
  within each dimension are distinguishable. BLOCK-01 concerns cross-document
  consequences, not duplicate option IDs.
- Root mechanism, App causality, and process/SIGTERM claims remain separated.
- The recommended signed return limits implementation to the already-approved
  contract/source/test surfaces. Implementation remains held before signature,
  and the Root-to-App notice remains held until semantic acceptance plus an
  accepted repair landing.

## Verdict

Do not present the current packet for signature or begin implementation. Repair
BLOCK-01 and BLOCK-02, address the review findings, regenerate affected drafts,
and hash-bind a fresh independent-refuter dispatch.
