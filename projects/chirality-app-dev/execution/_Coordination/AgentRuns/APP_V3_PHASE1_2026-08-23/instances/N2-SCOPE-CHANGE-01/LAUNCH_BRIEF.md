# Launch Brief — N2 SCOPE_CHANGE Gate-4 Propagation Plan

**Run:** `N2-SCOPE-CHANGE-01`
**Role:** SCOPE_CHANGE, Agent 1
**State:** `EXECUTING_AMENDED_V2`
**Basis:** `f485b5d3b663f42be8f8cab8432ced9024d7381b`
**Amendment:** `../../amendments/N2-SCOPE-CHANGE-01/V2.md`

## Sealed objective

Produce only the exact, candidate-only Gate-4 file-by-file propagation plan for later owner-approved Gate-5 application of SCA-APP-008. Derive every pre-image to proposed post-image SHA-256 pair mechanically from the final frozen N1 Gate-3 package:

`projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/Gate3/GATE3_AMENDMENT_PACKAGE.md`

SHA-256 `1a8048f4840cffd9932202d1822f497de5f7aa07aa1872e250c6e870846cf6df`.

The plan must order every target, classify package roles, separate the concordance-gated contract group, name validators and post-application reruns, consume the three A2-B SCC orderings without lifting their downstream gates, specify abort/rollback, and keep `_LATEST.md` movement inside a separately owner-approved Gate-5 act.

## Authorized writes

- `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/Gate4/GATE4_PROPAGATION_PLAN.md` as a new file.
- This instance's `LAUNCH_BRIEF.md`, `STATUS.json`, `RETURN.md`, and evidence-only files.
- The V2 amendment record named above.

Everything else is read-only. No stage, commit, push, application, pointer move, or authority claim.

## Stop history

The first brief was stopped before any N2 write when N1 changed after release. V2 supersedes that brief and authorizes resumption only against the final N1 SHA-256 above.

## Acceptance checks

- Final N1 identity matches exactly.
- Every N1 target pre-image matches the basis.
- Mechanical reconstruction reproduces every N1 declared candidate post-image SHA-256.
- Plan covers ordering, package roles, validators, dependency re-extraction, fresh named `AUDIT_DEP_CLOSURE`, A2-B SCC gates, rollback, pointer posture, and candidate-only authority state.
- Frozen assessment pins and prohibited surface identities remain unchanged.
- Candidate whitespace and `git diff --check` pass after N2 writes.
- Return state is `AWAITING_OWNER_APPROVAL`; `ReadyForNextPhase = NO`.
