# App v3 Phase 2 — Orchestration Plan

**Selection:** `HUMAN_SELECTED`
**Execution shape:** `N1_THEN_N2_THEN_INDEPENDENT_N3_REVIEW`
**Basis:** `4c9fdb4cc9031b376f220ceb5c34afa3874eacb7`
**Branch:** `codex/app-v3-phase2-2026-08-23`
**Steer:** `plans/steers/chirality_app_v3_phase2_steer_app_2026-08-23.md`, SHA-256 `5cd8e4ac4b6d77a2672f70218e27e18bfd3ac7cf5d1ddc57af608991260d9a5e`

## Execution graph

1. N1 verifies the five A4-A Root source blobs and regenerates the exact resolved K-EVENT-4 transaction candidate.
2. Candidate whitespace runs after N1 content is complete and before any N1 return or downstream artifact pins its hash.
3. N2 rebuilds the exact companion invariant-coverage register post-image from the whitespace-clean resolved amendment set, retaining K-CONTROL-1 as `PENDING_ROOT_AMENDMENT`.
4. N3 independently reviews the exact N1 and N2 candidate bytes. Any repair requires a fresh review.
5. HELP_HUMAN byte-verifies fan-in and owns the four-state handoff and Receipt 197.

## Dependency statement

```text
N1 -> CANDIDATE_WHITESPACE -> N2 -> N3_REVIEW -> HELP_HUMAN
```

## Fixed fences

- Candidate content: new files only beneath the existing SCA-APP-008 snapshot, under `Phase2/`.
- Run evidence: this run root only.
- Every previously approved or frozen SCA-APP-008 file is immutable.
- No live contract, companion register, `_LATEST.md`, Task Management register, SOW, status, dependency, decomposition, docs, frontend, Root, plan, or foreign-project write.
- No staging, commit, push, merge, or network access by N1.

## Close condition

Fan-in is eligible only when both exact candidates exist, N3 returns a fresh independent PASS, candidate whitespace and the full steer validator set pass, protected identities remain exact, and Receipt 197 records the evidence. Candidate approval and Gate-5 application remain owner acts. K-CONTROL-1 remains ineligible until the Root amendment is ratified.
