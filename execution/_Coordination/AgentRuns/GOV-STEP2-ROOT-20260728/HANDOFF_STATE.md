# Handoff — GOV-STEP2-ROOT-20260728

Status: `READY_FOR_OWNER_RULING_SESSION`

## Candidate identity

- Frozen candidate basis:
  `main@85ea0628fa4e57dd6aae53b06139b2b8734a9612`
- Candidate branch: `gov/step2-root-disclosure`
- CandidateSubjectSHA256 (PACKET.md bytes):
  `32b4afbfb402d65fecc14558bca79f5b83fc5690bd0b4f56cc9a656ced6c35e3`
- Decision record:
  `docs/governance_harness/_DECISIONS/D-GOV-30_program_disclosure_and_ratification.md`
  (AWAITING_RULING)
- Receipt candidate: Root Receipt 60, dependent on durable Receipt 59;
  drafted in packet §10, not appended.
- Companion evidence: separate PR on `gov/step1-evidence-landing`
  (commit `02b1f091a`), cited content-addressed by manifest SHA-256.

## Closure posture

Authoring is complete. The candidate is immutable-before-ruling: every
ruling slot holds the fenced placeholder, the packet is hashed and was
not edited afterward, and no owner ruling, cure claim, or loop-local
substance is contained. The disclosure facts are stated exactly as
evidenced by the frozen matrix, including the unreconciled D-8 conflict,
the ten NOT_EVIDENCED K-MERGE-1 rows, the #398 citation gap, and the
#408 self-ratification structure.

This package is a proposal. It binds nothing (K-AUTH-1) and is not a
substitute for decomposition truth or live governed state.

## Remaining blockers

1. Owner session: per-item verbatim returns for R-1..R-4 (each
   individually declinable) and the Step-2 authorization quote for the
   tranche manifest.
2. Completion commit: transcribe returns, fill the manifest
   authorization, append Receipt 60 after cursor rescan, backfill the
   four PENDING SHA fields per convention, complete the M6 disposition.
3. Evidence PR merge, which resolves the four expected WARN references
   documented in `VALIDATION.md`.
4. Human-gated PR merge; no self-merge.
