# Return — H1-A2-G4-VERIFY

Status: **COMPLETE — READ-ONLY REVIEW**

No file was changed by the Agent 2 reviewer.

## Findings

1. The canonical existing workflow convention is the pull-request base SHA or
   push-event `before` SHA as base, with the checked-out `HEAD` as candidate;
   the existing candidate-whitespace step supplies the same fallback pattern.
2. Unqualified legacy diff mode unions all historical manifests. Several
   accepted historical manifests already name the exact G4 workflow,
   validator, and test paths, so that mode alone cannot prove that a candidate
   tranche carries a new manifest.
3. The smallest compatible contract is an opt-in candidate-range selector:
   preserve no-argument whole-corpus schema validation, legacy all-manifest
   diff behavior, and `--tranche`; permit CI coverage only from candidate
   manifests newly added in the base-to-head range.
4. A selector accepting modified manifests would allow reuse of an accepted
   historical manifest. The reviewer therefore required an added-only rule
   and a negative regression for historical-manifest modification.

## Required proof

- positive: a newly added self-covering manifest plus a protected change;
- negative: a protected change with only an unchanged historical exact-path
  manifest;
- negative: a protected change plus modification of that historical manifest;
- static workflow assertions for the event base, `HEAD`, selector, and
  fallback; and
- the full focused G4 suite, demonstrating that existing schema and caller
  behavior remain green.

## Risk disposition

The added-only correction is required for readiness. No other blocker was
identified.
