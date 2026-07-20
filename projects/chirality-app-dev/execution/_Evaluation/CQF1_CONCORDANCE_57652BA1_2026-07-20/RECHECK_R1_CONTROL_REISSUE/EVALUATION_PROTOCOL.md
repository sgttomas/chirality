# Evaluation Protocol — CQ-F1 R1-CONTROL-REISSUE V1-RECHECK3

- **Instance:** `V1-RECHECK3`
- **Manager:** EVALUATION, dispatched by HELP_HUMAN
- **Basis:** `57652ba1cd0905e8f47131e4c4ebf518272f7c16`
- **Subject:** unchanged activated CQ-F1 derivative `ACTIVATED_57652BA1/`
- **Corrected control:** `instances/R1-CONTROL-REISSUE/`
- **Manifest:** 22 unique existing paths; ordered hash
  `2e314f3f601350736032ace2730492c2afa6ab5b21fe26465d799470a195fc36`
- **Scoring:** none requested
- **Subject posture:** read-only
- **Write roots:** only this evaluation root and `instances/V1-RECHECK3/`

## Preflight

Preflight passed before this protocol or any child brief was written. HEAD and
`origin/main` equal the exact basis; the evaluation root was empty; the
instance contained only launch/status; 30 corrected-control, predecessor,
child, evaluation, and 14-file package bindings matched; all 22 source and
five Remaining inputs were exact. The corrected status contains exactly one
`control_label_erratum` member and no duplicate at any object depth. Strict
Python, ordinary Python, Node `JSON.parse`, and jq expose the exact same
structured object and path order.

## Decision rule and toolbelt

Return `ACCEPT` only if the additive control record repairs V1R2-001 without
altering immutable predecessor evidence; all parser representations are
equivalent; the 14-file derivative, 14×19 fidelity result, 22 rows, nine
groups, classifications, authority, preservation, and containment remain
exact; and no new blocker exists. Otherwise return `BLOCK`.

The manager uses deterministic read-only Git/content/hash/CSV/JSON checks and
two fresh disjoint read-only Agent-2 confirmations:

1. `control_parser_confirmation` — unique-member, strict/ordinary parser,
   provenance, predecessor-defect preservation, and downstream-state audit.
2. `substantive_preservation_confirmation` — unchanged package hashes,
   source/row/group/fidelity/classification evidence, authority, EOF, and
   containment audit.

Children write only unique returns. The manager validates both and remains
sole evaluation-package author. Neither verdict accepts or routes a mapping,
group, or slate; W1 remains blocked pending HELP_HUMAN action.

## Rerun triggers

Rerun from the earliest affected node on any control parser divergence,
duplicate, source/Remaining/authority drift, child/package/predecessor hash
change, fidelity loss, containment escape, or downstream-state change.
