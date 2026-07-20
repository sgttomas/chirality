# Evaluation Protocol — CQ-F1 R1-REPAIR V1-RECHECK

- **Instance:** `V1-RECHECK`
- **Manager:** EVALUATION, dispatched by HELP_HUMAN
- **Basis:** `57652ba1cd0905e8f47131e4c4ebf518272f7c16`
- **Subject:** repaired activated CQ-F1 derivative `ACTIVATED_57652BA1/`
- **Manifest:** 22 unique existing paths; ordered hash
  `2e314f3f601350736032ace2730492c2afa6ab5b21fe26465d799470a195fc36`
- **Scoring:** none requested
- **Subject posture:** read-only
- **Write roots:** only this additive evaluation root and `instances/V1-RECHECK/`

## Decision rule

Return `ACCEPT` only if V1-001 through V1-004 are fully repaired; the v8
control-label erratum is genuinely nonconsequential; all 22 rows, source
bindings, classifications, alternatives, and nine groups are accurate and
decision-ready; the fresh R1 child and package fan-in are valid; all declared
hashes, schemas, EOF and containment claims reproduce; and every predecessor
remains immutable. Any defect requires `BLOCK`.

Neither verdict accepts a mapping or owner slate. W1 remains blocked until a
terminal `ACCEPT` is accepted by HELP_HUMAN.

## Toolbelt and fan-out

The manager uses read-only Git/content inspection, hashes, CSV/JSON parsing,
caller/import/test search, authority and deliverable inspection, and per-file
no-index hygiene. The sealed brief authorizes two fresh concurrent disjoint
audits:

1. `technical_recheck` — all source/caller/test evidence, 22 rows, fresh-child
   fidelity, V1-001..003, alternatives, and the two-path erratum execution.
2. `governance_package_recheck` — SOW/status/dependency/authority,
   classification, nine groups, V1-004, hashes/schemas/EOF, predecessor
   preservation, mutation, and containment.

Children may share reads but write only their unique return. The manager
validates both returns, preserves disagreements, and remains sole integration
author.

## Rerun triggers

Rerun from the earliest affected node if any source blob, caller, test,
Remaining entry, deliverable scope, authority, R1 child/package byte,
predecessor binding, or evaluation question changes.
