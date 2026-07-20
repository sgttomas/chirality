# Evaluation Protocol — CQ-F1 R1-REPAIR2 V1-RECHECK2

- **Instance:** `V1-RECHECK2`
- **Manager:** EVALUATION, dispatched by HELP_HUMAN
- **Basis:** `57652ba1cd0905e8f47131e4c4ebf518272f7c16`
- **Subject:** repaired activated CQ-F1 derivative `ACTIVATED_57652BA1/`
- **Manifest:** 22 unique existing paths; ordered hash
  `2e314f3f601350736032ace2730492c2afa6ab5b21fe26465d799470a195fc36`
- **Scoring:** none requested
- **Subject posture:** read-only
- **Write roots:** only this additive evaluation root and `instances/V1-RECHECK2/`

## Preflight

Preflight passed before this protocol or any child brief was written. HEAD and
`origin/main` equal the exact basis; the additive evaluation root was empty;
the instance contained only its launch brief and initial status; the manifest,
Remaining populations/statuses, 28 frozen package/predecessor/child bindings,
14-row sealed-child schema/order/source bindings, and 22-row ledger source
bindings reproduced. The raw R1-REPAIR2 status contains exactly two ordered
`control_label_erratum` members: structured object first and matching string
second.

## Decision rule

Return `ACCEPT` only if all four repaired rows, every one of the 14 fidelity
matrix rows and 19 columns, all 22 proposals/classifications, all nine groups,
every material alternative and boundary, both errata, package hashes/schemas/
EOF, immutable predecessors, and containment independently pass. Any semantic,
provenance, schema, automation, path, authority, ownership, acceptance, or
downstream loss from the duplicate key is blocking. Any other defect also
requires `BLOCK`.

Neither verdict accepts a row, mapping, group, or owner slate. W1 and owner
routing remain blocked unless HELP_HUMAN later accepts a terminal `ACCEPT`.

## Toolbelt and bounded fan-out

The manager uses read-only Git/content inspection, hashes, CSV/JSON parsing
with duplicate detection, source/caller/test search, authority/deliverable
inspection, and per-file no-index hygiene. Two fresh concurrent disjoint
Agent-2 audits are authorized:

1. `technical_fidelity_recheck` — source, callers, tests, all 22 technical
   rows, full 14-row child/package fidelity, four repairs, alternatives,
   boundaries, and groups 1–3.
2. `governance_package_erratum_recheck` — D-APP-60/D-APP-64 classification,
   all nine groups, package hashes/schemas/EOF, preservation/containment, and
   both errata with raw duplicate-key parser/schema/automation analysis.

Children share read dependencies but write only their unique return. The
manager validates both returns, independently reopens material evidence,
preserves disagreements, and remains sole integration author.

## Rerun triggers

Rerun from the earliest affected node if any source blob, caller, test,
Remaining entry, SOW/dependency/authority input, sealed child, package byte,
predecessor binding, parser contract, or evaluation question changes.
