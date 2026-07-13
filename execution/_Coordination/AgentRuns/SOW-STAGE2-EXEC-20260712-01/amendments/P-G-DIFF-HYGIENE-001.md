# P-G Diff-Hygiene Classification Amendment 001

Status: `ACTIVE — NON-SEMANTIC EVIDENCE CLASSIFICATION`

## Trigger

The accepted pilot evidence binding contains intentional Markdown two-space
hard breaks. A raw PR-range `git diff --check` classifies those byte-bound
line endings as trailing whitespace. Normalizing an accepted byte would break
its immutable hash binding and trigger a substantive evidence rerun even
though the characters are intentional Markdown layout syntax.

## Exact disposition

CHANGE-P-G may classify only exact two-space end-of-line findings in committed,
byte-bound Markdown evidence as `INTENTIONAL_MARKDOWN_HARD_BREAK`. It must list
every allowed path and line in its readiness/check evidence and prove the full
PR-range diff contains no other whitespace finding.

This classification does not waive diff hygiene for a deliverable commit or
for mutable integration evidence. Each of the ten five-path deliverable
commits must pass strict `git diff --check` with zero output. Mutable readiness,
receipt, integration, return, and handoff prose must be normalized before its
binding commit. Any finding other than an exhaustively enumerated intentional
two-space hard break in already byte-bound Markdown evidence blocks P-G.

## Boundary

Do not edit, normalize, amend, or rebind the accepted preintegration bytes or
the existing evidence-binding commit. This amendment changes no candidate,
source, status, lifecycle, manifest operation, acceptance criterion, authority,
risk, commit architecture, H1/H2 posture, ISSUED boundary, release state, or
retirement state. It is a deterministic classification of known evidence
formatting only and does not require a new human ruling.
