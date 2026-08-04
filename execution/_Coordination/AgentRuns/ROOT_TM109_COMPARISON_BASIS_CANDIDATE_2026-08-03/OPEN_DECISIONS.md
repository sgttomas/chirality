# TM109-A open semantic decisions

Status: `DECISION PREPARATION ONLY — NOTHING SELECTED`

The signed TM109-A ruling authorizes preparation of this candidate, not these
semantic choices. The candidate column is an authored proposal. Every choice
remains subject to a later accountable-human act over frozen exact bytes.

| ID | Question | Candidate choice in prepared bytes | Bounded alternatives | Consequence of no decision |
|---|---|---|---|---|
| OD109-01 | Is the companion schema identity/version acceptable? | Use the dated candidate URN only as schema `$id`; do not put schema identity into instance bytes | Add an instance schema ID/version; use another external schema ID; return for revision | No accepted envelope contract |
| OD109-02 | Which basis fields are mandatory? | Require basis ID version and four-part canonical hash | Make hash optional only for `MISSING`; require another accepted basis identity shape | Cannot validate a governed basis consistently |
| OD109-03 | How much subject identity is mandatory? | Require subject ID; make version and hashes optional | Require version; require at least one hash; define consumer profiles with stronger local rules | Consumers cannot rely on generic completeness |
| OD109-04 | How are hash inputs represented? | Require algorithm canonicalization-method ID payload-scope ID and digest; select no values | Select governed enums later; bind exact methods only in consumer profiles | Matching digest text remains uninterpretable |
| OD109-05 | Which activity identities are mandatory? | Require at least one operation or tool identity | Require both; require operation only; require tool only by profile | Activity may be underidentified for some consumers |
| OD109-06 | Are consumer sandbox and policy identities mandatory? | Require all three | Make sandbox/policy optional only with explicit missing outcome; require hashes/versions | Carrier cannot support consistent provenance checks |
| OD109-07 | Should unit/tolerance refs be present? | Optional opaque ID/version/hash only | Require one/both by consumer profile; exclude them from generic carrier | Generic schema never indicates whether local comparison inputs were named |
| OD109-08 | Is the outcome vocabulary acceptable? | Closed nine-label set including explicit `MISSING` `INCOMPATIBLE` `BUDGET_EXHAUSTED` | Reduce or extend labels; use consumer-qualified status refs | No accepted common carriage labels |
| OD109-09 | Are diagnostics adequately bounded? | Require code/message; optional severity/source/subjects/evidence | Require stronger provenance; drop generic severity; use consumer-qualified diagnostic refs | Diagnostic carriage remains inconsistent |
| OD109-10 | What evidence/provenance minimum is required? | At least one top-level evidence ref and one source-linked provenance record | Permit empty evidence only for explicit missing outcomes; require hash/version on every ref | Structurally valid records may be unevidenced or overburdened |
| OD109-11 | Must claimant and caller both be present? | Require separate claimant and caller identities | Permit same explicit identity; allow missing caller under named local rule | Assertion and causation can be ambiguous |
| OD109-12 | Which timestamp semantics apply? | Require an RFC 3339 date-time shape only | Require trusted-clock evidence; define ordering locally; make optional on missing outcomes | Timestamp cannot support freshness or sequence claims |
| OD109-13 | Are objects closed? | Reject undeclared properties at every candidate object | Permit namespaced extensions under a separately governed extension point | Silent semantic extension risk or reduced evolvability |
| OD109-14 | How does the contract evolve? | No evolution rule selected | Human-select exact versioning/supersession rules before implementation; decline generic evolution | No safe compatibility claim between future schema versions |
| OD109-15 | Which validators and format assertions are authoritative? | JSON Schema draft 2020-12 shape; format behavior remains validator-dependent | Select validator/version and format assertion profile | Deterministic conformance cannot be claimed |
| OD109-16 | What proves external identities/evidence? | Nothing generically; consumers validate locally | Add a separately ruled resolver/trust profile; keep fully local | Carrier remains non-self-authenticating by design |

## Decisions explicitly out of scope

No TM109-A semantic-acceptance act may silently decide:

- Piping equality, mapping, normalization, dimensions, units, tolerances,
  solver/rule meaning, engineering meaning, privacy, professional, or review
  semantics;
- App parity, durable-resume equality, replay, model/residency binding, or
  affected-client acceptance;
- Root runtime compatibility identity, grammar, preflight order, header,
  mismatch envelope, epoch, binding lifecycle, or affected-client disposition;
- sandbox containment, tool authorization, policy evaluation, budget amounts,
  interruption, implementation-family selection, or fail-closed execution;
- a canonical JSON or other serialization algorithm;
- a digest algorithm; or
- implementation, source/test writes, lifecycle, release, publication,
  reliance, commit, push, or merge.

## Required next gate

HELPS_HUMANS must freeze the exact candidate package and its hashes after
refutation/repair, then present one of the bounded options in
`NEXT_HUMAN_ACCEPTANCE_FORM.md`. An acceptance may establish semantic contract
design bytes only. Implementation requires another separately sealed and
authorized tranche.
