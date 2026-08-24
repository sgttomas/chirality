# Sealed Launch Brief — N3 Independent Review 01

**Run:** `APP_V3_PHASE2_2026-08-23`
**Instance:** `N3-REVIEW-01`
**Role:** fresh independent Agent 1 `REVIEW`
**Review class:** evidence-only candidate-package review
**Basis:** exact commit `4c9fdb4cc9031b376f220ceb5c34afa3874eacb7`
**Branch:** `codex/app-v3-phase2-2026-08-23`

## Objective

Independently review the resolved K-EVENT-4 transaction candidate and the
complete companion invariant-coverage register post-image. Reconstruct the
resolved App-contract candidate from the live contract and approved Gate-3
transactions rather than trusting producer hashes; parse and census the raw
CSV; verify every source anchor, changed/new row, and consequential
enforcement relationship; and return `PASS` or `RETURN_FOR_REPAIR` without
modifying candidate content or authoritative truth.

## Fixed candidate identities

- N1 K-EVENT-4 transaction artifact:
  `779d4874adc2fc3669078a0431f676fe50d31acbd2dd82c8c405714343fa1df0`.
- N2 full companion-register post-image:
  `26ffe13b3c53130e44e4acaf6ab0aecadf0be853757c8a9678a54b80426b67c2`.

## Required evidence and review gates

1. Read `agents/AGENT_REVIEW.md`, the Phase-2 steer, A4, A5, the concordance
   decision input, approved Gate-3/Gate-4/concordance records, the live App
   contract and register, all five A4-A Root sources, and complete N1/N2
   briefs, candidates, returns, status, and validation evidence.
2. Re-hash every governing and protected input, including the eleven
   A2-frozen assessment files.
3. Independently apply Gate-3 C-01 through C-11 to the exact live App contract,
   substituting only the resolved C-06 post-image, and reproduce the complete
   post-image identity.
4. Independently parse the candidate CSV, reproduce the 81/48 to 83/50 census,
   resolve every source anchor against the reconstructed contract, compare all
   existing rows and the two new rows, and verify all six exact enforcement
   relationships.
5. Verify A4-A and all five Root pins; enforce A4-B/A5-B
   `PENDING_ROOT_AMENDMENT` treatment for K-CONTROL-1 and A5-C's single
   Gate-5 condition.
6. Verify additions-only containment, immutable/protected identities,
   candidate whitespace, and `git diff --check`.

## Write boundary

Write only sealed review artifacts in this instance directory. If any finding
exists, do not modify N1/N2 outputs, do not create the Phase-2 handoff, and
return exact repair requirements for a fresh re-review. No contract, register,
pointer, decomposition, SOW, lifecycle, code, docs, frontend, Root, receipt,
shared-run-root, Git, publication, or release write is permitted.
