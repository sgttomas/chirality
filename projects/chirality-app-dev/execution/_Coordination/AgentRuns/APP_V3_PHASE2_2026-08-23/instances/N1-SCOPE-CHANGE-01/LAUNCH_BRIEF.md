# Sealed Launch Brief — N1 SCOPE_CHANGE

**Run:** `APP_V3_PHASE2_2026-08-23`
**Instance:** `N1-SCOPE-CHANGE-01`
**Requested by:** HELP_HUMAN under Ryan Tufts's Phase-2 direction
**Role:** Agent 1 `SCOPE_CHANGE`
**Basis:** exact commit `4c9fdb4cc9031b376f220ceb5c34afa3874eacb7`
**Branch:** `codex/app-v3-phase2-2026-08-23`

## Objective

Regenerate the exact K-EVENT-4 contract-row candidate from the A4-A selected Root session-store identity. Produce an additions-only transaction artifact with the live App row pre-image, exact replacement bytes, full-file pre/post identities, A4-A authority binding, and all five pinned Root source identities. The output remains `AWAITING_OWNER_APPROVAL` and applies no truth.

## Required reads

- root `AGENTS.md` and `agents/AGENT_SCOPE_CHANGE.md` in full;
- Phase-2 steer and owner ruling records A4 and A5;
- decision-input package SHA-256 `4d16cefae5dc672376a62ae00437c27ff857e7d994206549e888da3409f40c2a`;
- Phase-1 Gate-3, Gate-4, and concordance candidates;
- live App contract row K-EVENT-4;
- pinned Root `docs/CONTRACT.md`, CLI config, session store, event schema, and session schema sources.

## Allowed writes

1. Exactly one new content file: `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/Phase2/K_EVENT_4_RESOLVED_CONTRACT_ROW_CANDIDATE.md`.
2. This instance's `LAUNCH_BRIEF.md`, `STATUS.json`, `RETURN.md`, and strictly necessary N1 evidence.
3. As N1 run integration owner only: run-root `ORCHESTRATION_PLAN.md` and `WORK_GRAPH.json`.

No existing SCA file or authoritative surface may be modified. No other write is allowed.

## Tools and environment

- Read-only shell and Git inspection.
- `apply_patch` only for repository writes.
- Deterministic local validation commands.
- No network and no subagent dispatch.
- No Git stage, commit, push, rebase, merge, or force operation.

## Acceptance checks

- All five A4-A Root source SHA-256 identities match the Phase-2 steer exactly.
- The live App contract is SHA-256 `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7`, and K-EVENT-4 occurs exactly once at line 72.
- The replacement names the selected canonical path, `chirality.event/v1`, adjacent `session.json` with `chirality.session/v2`, Root-daemon one-writer semantics, Root K-STORE-2 lazy non-destructive legacy migration, and projection-only App `UIEvent` streaming/replay.
- Mechanical application of the approved Phase-1 contract transaction set with only the resolved C-06 bytes yields one exact full-file post-image SHA-256.
- Candidate whitespace passes against basis before `RETURN.md` or `STATUS.json` pins the candidate identity.
- The write set is contained and all protected surfaces remain byte-identical.

## Escalation conditions

Stop and report if any Root blob, App contract pre-image, live line, approved Phase-1 transaction, or selected A4-A value differs; if the candidate would create a second writer or authority replacement; or if another writer overlaps N1's fixed paths.
