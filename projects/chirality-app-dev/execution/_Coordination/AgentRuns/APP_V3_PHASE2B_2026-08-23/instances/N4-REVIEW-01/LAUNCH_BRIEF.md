# Sealed Launch Brief — N4 Independent Review 01

**Run:** `APP_V3_PHASE2B_2026-08-23`
**Instance:** `N4-REVIEW-01`
**Role:** fresh independent Agent 1 `REVIEW`
**Review class:** evidence-only candidate-package review
**Basis:** exact commit `ef92fab10f40aa95da484701982d83fa1abca874`
**Branch:** `codex/app-v3-phase2b-2026-08-23`

## Objective

Independently review the Phase-2b regenerated K-CONTROL-1 and re-pinned
K-EVENT-4 row candidates, reconstruct both the Phase-2 control App-contract
image and the Phase-2b resolved image from exact transactions, and audit the
rebuilt companion invariant-coverage register without trusting producer
digests or counts. Return `PASS` or `RETURN_FOR_REPAIR` without changing any
candidate or authoritative surface.

## Required evidence and review gates

1. Read `agents/AGENT_REVIEW.md`, the complete Phase-2b steer, records A6, A4,
   and A5, Gate 3, Gate 4, the Phase-2 candidates and handoff, all Phase-2b
   candidates, and complete N1/N2/N3 briefs and returns.
2. Independently verify the ratified Root contract and its exact prior-to-
   current line-162-only delta, plus all four unchanged A4-A source blobs.
3. Replay Gate-3 C-01 through C-11 against the live App contract. First use
   the original C-01 plus resolved C-06 and reproduce Phase 2; then substitute
   only regenerated C-01 while retaining byte-identical C-06 and reproduce
   Phase 2b.
4. Verify N1 design-honest tense, Root ownership, App enforcement
   strengthenings, and live-versus-design-gated verification posture.
5. Verify N2 is a Root-contract re-grounding only and that its exact resolved
   LF-terminated C-06 row is byte-identical to Phase 2.
6. Parse and census the full N3 CSV; resolve every source anchor; compare it
   field-by-field with Phase 2; verify DEL-03-04 retention; and verify the
   K-CONTROL-1 six-field delta, Root provenance, open-issue posture, and lack
   of any live-second-socket or implementation-coverage claim.
7. Verify Gate-4 mechanics under A5-C's superseding single-Gate-5 sequencing,
   all protected/frozen identities, additions-only containment, attribution,
   candidate whitespace, and `git diff --check`.

## Write boundary

Write only this instance's sealed review records. If and only if the review
returns `PASS` with zero findings, add
`Phase2b/Handoff_State.md`. Do not modify candidates, prior run records,
shared run-control files, Receipt 198, any live contract/register/pointer,
decomposition, SOW, lifecycle, code, docs, frontend, Root, Git history, or
publication state. No commit, push, merge, acceptance, application, or Gate-5
act is permitted.
