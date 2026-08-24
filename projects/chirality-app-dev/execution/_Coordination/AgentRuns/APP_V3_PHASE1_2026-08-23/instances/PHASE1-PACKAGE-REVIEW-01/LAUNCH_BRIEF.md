# Launch Brief — App v3 Phase-1 Package Review 01

**Run:** `APP_V3_PHASE1_2026-08-23`
**Instance:** `PHASE1-PACKAGE-REVIEW-01`
**Role:** fresh independent `REVIEW` Agent 1
**Review class:** evidence-only package review; not a deliverable lifecycle review
**Basis commit:** `f485b5d3b663f42be8f8cab8432ced9024d7381b`
**Branch:** `codex/app-v3-phase1-2026-08-23`

## Objective

Independently review the complete SCA-APP-008 Gate-3/Gate-4 drafting package after N1, N2, and N3 fan-in. Return `PASS` or `RETURN_FOR_REPAIR` without modifying candidate content, accepted assessment bytes, lifecycle state, shared run-root files, or receipts.

## Required evidence

- root `AGENTS.md` and `agents/AGENT_REVIEW.md` in full;
- Phase-1 steer SHA-256 `7d700af0b05c754e468d958a7580fff713f743ad789540d8c4176bf8711ed394`;
- A2 SHA-256 `37e6b6d60874ded0727cf65f25aea09cc961bd35b135b5b8eb33c0d20c1f6158`, G0 SHA-256 `86b9877c6bea08a9f79c2af2378d5d38722a09c1a10deb37f87211c76d2c290b`, and A1 SHA-256 `f9b02806eeab1a578e6729c41fc367074758a2b95cc0eda9c8d2edbda446f314`;
- all eleven A2-frozen assessment files;
- final candidates: Gate 3 `1a8048f4840cffd9932202d1822f497de5f7aa07aa1872e250c6e870846cf6df`, Gate 4 `47daaedf84ba4e9450bef3c12be3d1ab42316e0e3daabc37641d06f1040fd8d6`, and Concordance `c747a81b7fcca88dfebab8e2ed2345247af23063d9f48e3dd2e4bfa0a5af4185`;
- orchestration plan/work graph, all three node briefs/returns/status records, both V2 amendments, and the N1 mechanical validator;
- live target preimages and all protected surface identities.

## Review gates

1. Basis, authority, and frozen-input identities.
2. Additions-only write containment and absence of effective-truth writes.
3. N1 exact candidate coverage and authority calibration.
4. Independent reconstruction of both complete target post-images.
5. N2 file-by-file propagation, ordering, validation, rerun, SCC, pointer, and rollback completeness.
6. N3's three unresolved concordance inputs and non-routing posture.
7. Candidate state, four-state handoff, and absence of false approval/acceptance/release effect.
8. Mechanical validation: whitespace, diff, JSON, protected identities, frozen bytes, and empty Git index.

## Write boundary

Write only `LAUNCH_BRIEF.md`, `REVIEW.md`, `RETURN.md`, `STATUS.json`, and optional read-only evidence logs in this instance directory. Candidate repair, lifecycle transition, staging, commit, push, merge, receipt, shared run-root, and authoritative-surface writes are prohibited.
