# Evaluation Protocol — CQ-F1 Concordance V1-RETRY

- **Evaluation instance:** `V1-RETRY`
- **Manager:** EVALUATION (Agent 1), dispatched by HELP_HUMAN
- **RunID:** `APPDEV_LOOP_2026-07-19_CQF1_CONCORDANCE`
- **Accepted source basis:**
  `57652ba1cd0905e8f47131e4c4ebf518272f7c16`
- **Evaluated derivative:**
  `execution/_Reconciliation/DeliverableConcordance/SCOPED_CQF1_POST_DAPP68_CONCORDANCE_2026-07-19/ACTIVATED_57652BA1/`
- **Protocol authority:** the sealed `instances/V1-RETRY/LAUNCH_BRIEF.md`
  and live disposition `updates/v6.md`
- **Scoring:** none requested
- **Subject posture:** read-only
- **Evaluator writes:** only this evaluation root and the V1-RETRY instance
  root authorized by the sealed brief

## Questions and decision rule

The audit independently tests exact 22-path source binding; the five child
returns and 14/1/1/4/2 fan-in; all evidence, tests, callers, affinities,
candidate mappings, shared boundaries, alternatives, and rejections; the
22-row D-APP-60/D-APP-64 classification; nine-group slate completeness and
truthful proposal-only attribution; subject and historical immutability; and
all R1 QA claims, including terminal-LF/no-index hygiene.

The result is `ACCEPT` only if the R1 derivative is materially accurate and
decision-ready for possible HELP_HUMAN owner routing. Any invalid fan-in,
stale or unsupported claim, materially incomplete group, scope escape, or
misleading QA statement requires `BLOCK`. Neither result accepts a mapping or
owner slate, and W1 remains blocked.

## Accepted toolbelt and fan-out

The manager uses read-only Git/content inspection, CSV/JSON/hash checks, code
and test search, and repository-native read-only validators. The sealed brief
authorizes two concurrent, disjoint Agent-2 audits:

1. `technical_evidence` — code, calls/imports, tests, source hashes, row-level
   evidence, implementation affinity, and technical alternatives.
2. `governance_slate` — deliverable/governance/dependency evidence,
   classification, coverage/fan-in, grouped owner questions, attribution, and
   QA/containment.

They may share reads but have disjoint questions and may write only their
individual V1 child return. This manager validates both returns and remains
sole integration author.

## Rerun triggers

Rerun from the earliest affected step if any scoped source blob, Remaining
entry, authority, R1 derivative or child return changes; if a repair alters
the exact R1 publication candidate; or if HELP_HUMAN amends the questions or
owner-routing boundary.
