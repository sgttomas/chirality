# Launch Brief — N3 RECONCILIATION

**Run ID:** `N3-RECONCILIATION-01`
**Role:** RECONCILIATION (Agent 1), supervised by HELP_HUMAN
**Basis:** `f485b5d3b663f42be8f8cab8432ced9024d7381b`
**Branch:** `codex/app-v3-phase1-2026-08-23`
**Authority:** A2-C authorizes drafting only. No concordance activation, discovery wave, repair, acceptance, application, or notice routing is authorized.

## Objective

Add one short candidate workplan identifying the Root/App concordance decisions required before the SCA-APP-008 contract candidates may be accepted:

1. the exact live Root session path required by K-EVENT-4;
2. any cross-loop invariant-ID collision; and
3. the routing moment for the frozen `DRAFT_NOTICE_TO_ROOT.md`.

Each item must remain an owner/HELP_HUMAN decision input. The workplan must name its inputs, required evidence, decision owner, PASS/HOLD output, sequence, and non-effects.

## Write boundary

Allowed project output:

- `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/Concordance/CONCORDANCE_WORKPLAN.md` (new file only).

Allowed run evidence:

- this instance directory only: `LAUNCH_BRIEF.md`, `STATUS.json`, `RETURN.md`, plus evidence-only files if needed.

Everything else is read-only. In particular, the 11 accepted assessment files, `_ScopeChange/_LATEST.md`, registers, contracts, SOWs, status/dependency/lifecycle files, code, docs, frontend, plans, Root paths, and other projects are frozen.

## Acceptance checks

- exact branch and basis commit;
- Phase-1 steer/A2/G0/A1 identities match the owner pins;
- all 11 accepted assessment files match A2's SHA-256 identities before and after the write;
- only the one new workplan and this instance's three control files are written by N3;
- the workplan is candidate-only, `AWAITING_OWNER_APPROVAL`, and `ReadyForNextPhase = NO`;
- candidate whitespace and `git diff --check` pass before `RETURN.md` pins the workplan hash.

## Return contract

Return the exact file list and SHA-256 identities, validation evidence, unresolved questions, containment result, frozen-byte result, and candidate handoff state. Do not stage, commit, push, or merge.
