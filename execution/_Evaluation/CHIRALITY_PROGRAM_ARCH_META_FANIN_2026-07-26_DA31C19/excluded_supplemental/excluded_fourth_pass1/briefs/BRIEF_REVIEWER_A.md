# Sealed Brief — Reviewer A (Pass 1, Independent)

You are Reviewer A of the Chirality Program tandem architecture review.

Common brief (binding, read it first and in full):
`plans/reviews/tandem_2026-07-26/briefs/BRIEF_COMMON.md`
(repository-relative to `/Users/ryan/dev/chirality/.claude/worktrees/help-human-chirality-app-99df76`)

Your report file (the ONLY file you may write):
`/Users/ryan/dev/chirality/.claude/worktrees/help-human-chirality-app-99df76/plans/reviews/tandem_2026-07-26/reports/REVIEWER_A_PASS1_REPORT.md`

FindingID prefix: `A-F-` (A-F-001, A-F-002, …).
Frontmatter: `reviewer: A`, `lens: vertical-authority-trace`.

## Assigned lens — vertical: authority, intent, and traceability

You still assess Root, App, and PEC on both depth and breadth (Common Brief §3);
this lens sets your emphasis:

- **Status and provenance**: for every accepted instrument, who accepted it, through
  what act, on what recorded basis, and whether the acceptance chain is internally
  consistent (adoption rulings, EffectiveSHAs, pointer blocks, amendment provenance).
- **Trace**: PRD commitment → objective → package → deliverable → ScopeOfWork, both
  forward and reverse. Use the trace/coverage registers and test them rather than
  trusting them. Identify commitments without executable coverage and coverage
  without a warranted commitment.
- **Human gates**: where acceptance, issuance, reliance, and release judgments sit;
  whether any machine gate, validator, or convention has silently acquired the force
  of a human decision.
- **Non-goals and falsifiers**: whether PRD non-goals are respected downstream;
  whether acceptance criteria are checkable and falsifiable rather than rhetorical.
- **Accepted-versus-proposed discipline**: whether candidate, superseded, or proposed
  material is anywhere treated as accepted (and the reverse); whether supersession is
  discoverable by a reader following the governed pointers.
- **Stable identity**: IDs, SHAs, versions, and register keys — stability, collision,
  drift between surfaces, machine-checkability.
- **Preservation of owner intent**: whether each decomposition preserved rather than
  replaced the owner's PRD intent, and whether SOW prose stays within accepted scope.

Execute the Common Brief in full and deliver your report to the exact path above.
