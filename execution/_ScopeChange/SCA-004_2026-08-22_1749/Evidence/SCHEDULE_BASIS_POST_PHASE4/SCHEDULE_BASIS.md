# SCA-004 Schedule-Basis Candidate — Post Phase 4

- **Status:** `AWAITING_OWNER_ACCEPTANCE`
- **Package posture:** immutable derivative candidate
- **Objective:** effort-hours-and-ordering-only basis for the accepted SCA-004
  carrier slice
- **Substance boundary:** only the R8-accepted estimate snapshot and the eight
  Phase-3 deliverable-local dependency declarations supply schedule substance

This candidate is not schedule truth, a commitment, a staffing plan, an
elapsed-time promise, a lifecycle act, an implementation dispatch, a pin
decision, a hold lift, or App authority. Owner acceptance is a later separate
act against the independently reviewed and sealed package bytes.

## Accepted effort profile

| Work stream | Base effort-hours | Low effort-hours | High effort-hours |
|---|---:|---:|---:|
| DEL-02-07 carrier production and local verification | 180 | 94 | 266 |
| DEL-02-08 carrier production and locally estimable fixture work | 100 | 57 | 143 |
| DEL-02-09 carrier production and local verification | 148 | 82 | 214 |
| DEL-02-10 carrier production and local verification | 144 | 88 | 200 |
| DEL-02-11 carrier production and local verification | 136 | 72 | 200 |
| DEL-02-12 currently estimable Root-owned, hold-preserving portions | 96 | 51 | 141 |
| DEL-04-11 carrier production and local verification | 92 | 53 | 131 |
| DEL-02-06 incremental integration and fan-in reassessment | 116 | 63 | 169 |
| **Total** | **1012** | **560** | **1464** |

The seven carrier arithmetic is:

- base: `180 + 100 + 148 + 144 + 136 + 96 + 92 = 896`;
- low: `94 + 57 + 82 + 88 + 72 + 51 + 53 = 497`; and
- high: `266 + 143 + 214 + 200 + 200 + 141 + 131 = 1295`.

DEL-02-06 adds only its accepted incremental intake, reconciliation,
hold-aware integration, and handoff work: `896 + 116 = 1012`, `497 + 63 =
560`, and `1295 + 169 = 1464`. The six DEL-02-07..12 carrier-production
estimates are not repeated inside DEL-02-06.

These values are aggregate work effort. They are not elapsed time. This
candidate contains no calendar plan, workforce allocation, productivity
assumption, completion promise, or implementation assignment.

## Ordering derivation

The accepted strict Root ordering layer contains exactly eight gating edges:

1. DEL-02-07 `EVIDENCE_FAN_IN` -> DEL-02-06 final fan-in closure.
2. DEL-02-08 `EVIDENCE_FAN_IN` -> DEL-02-06 final fan-in closure.
3. DEL-02-09 `EVIDENCE_FAN_IN` -> DEL-02-06 final fan-in closure.
4. DEL-02-10 `EVIDENCE_FAN_IN` -> DEL-02-06 final fan-in closure.
5. DEL-02-11 `EVIDENCE_FAN_IN` -> DEL-02-06 final fan-in closure.
6. DEL-02-12 `EVIDENCE_FAN_IN` -> DEL-02-06 final fan-in closure.
7. DEL-04-05 `DOCTRINE_INPUT` -> DEL-04-11 closure.
8. DEL-05-02 `EVIDENCE_CROSSCHECK_INPUT` -> DEL-04-11 closure.

The Phase-3 truth declares no gating edge among DEL-02-07..DEL-02-12.
Accordingly, those six carrier streams are parallelizable relative to one
another for this objective. Their semantic overlap does not create an order.
Each carrier's separately produced and accepted evidence strictly precedes
closure of its corresponding DEL-02-06 intake, and accepted evidence from all
six strictly precedes DEL-02-06 final fan-in closure. Stable DEL-02-06 intake
preparation may proceed without claiming that an unavailable carrier result
exists, but an intake remains unresolved until its corresponding evidence is
separately accepted.

DEL-04-11 is a separate branch. Its closure follows the accepted DEL-04-05
doctrine input and DEL-05-02 evidence-crosscheck input. The accepted
DEL-04-11 `VALIDATION_RELATIONSHIP` -> DEL-02-06 relationship is explicitly
non-gating: it neither precedes nor delays DEL-02-06 final fan-in closure. A
DEL-04-11 report may be evaluated only if separately authorized, produced,
and accepted; its absence remains unresolved support, not a new gate.

The two App notice/fan-in relationships are also non-gating coordination
only. They confer no foreign authority and do not add an ordering edge.

## Blocker and exclusion effect

`BLOCKER_REGISTER.md` preserves TM-ROOT-106, TM-ROOT-122, C1, all ten exact
`HELD_UNAVAILABLE` DEL-02-06 bindings, all estimate-package App-owned
obligation categories, the separate DEL-04-11 `tools/**` authority, and the
owner-acceptance boundary. None is treated as resolved or as priced
zero-effort work. A blocked or excluded item is a grounding gap outside the
accepted 1,012 / 560–1,464 effort envelope.

## Candidate disposition and rerun triggers

Independent review has sealed this derivative candidate with zero actionable
findings. It remains a candidate until explicit owner acceptance of the exact
sealed bytes. Rebuild and independently review it after any change to a pinned
estimate artifact, dependency declaration, applied register, R8 ruling,
owner-acceptance transcription,
TM-ROOT-106 or TM-ROOT-122 disposition, C1 status, held binding, App-owned
input, accepted evidence posture, or owner correction. No later act may rely
on this candidate as schedule truth before that gate.
