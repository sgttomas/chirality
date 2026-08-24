# Sealed Launch Brief — N2 SCOPE_CHANGE

**Run:** `APP_V3_PHASE2_2026-08-23`
**Instance:** `N2-SCOPE-CHANGE-01`
**Requested by:** HELP_HUMAN under Ryan Tufts's Phase-2 direction
**Role:** Agent 1 `SCOPE_CHANGE`
**Basis:** exact commit `4c9fdb4cc9031b376f220ceb5c34afa3874eacb7`
**Branch:** `codex/app-v3-phase2-2026-08-23`

## Objective

Rebuild the exact full-file companion invariant-coverage register candidate for the resolved SCA-APP-008 amendment set. Consume N1 only at SHA-256 `779d4874adc2fc3669078a0431f676fe50d31acbd2dd82c8c405714343fa1df0` and resolved full App-contract candidate SHA-256 `a79282970bbd96d27e28846605be2ce0b3433c0f6c991bbc5911548c6f7e56c8`. Preserve complete invariant accounting and mark K-CONTROL-1 exactly `PENDING_ROOT_AMENDMENT`, with no stale coverage or Gate-5 eligibility claim.

## Required reads

- root `AGENTS.md` and `agents/AGENT_SCOPE_CHANGE.md` in full;
- Phase-2 steer and owner ruling records A4 and A5;
- Phase-1 Gate-3, Gate-4, and concordance package;
- the N1 resolved K-EVENT-4 candidate at its fixed identity;
- live App contract, live companion register, and the accepted carrier map.

## Allowed writes

1. New files only under `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/Phase2/` for the raw companion-register post-image candidate and its transaction evidence.
2. This instance's `LAUNCH_BRIEF.md`, `STATUS.json`, `RETURN.md`, and strictly necessary N2 evidence.

No shared orchestration file, N1 file, previously approved SCA file, live contract/register, receipt, pointer, register, decomposition, docs, frontend, lifecycle, SOW, Root, plan, or foreign-project surface may be modified.

## Tools and environment

- Read-only shell and Git inspection.
- Deterministic local CSV reconstruction and validation.
- `apply_patch` for authored repository records; the raw full-file CSV is a deterministic bulk mechanical rewrite of the exact pre-image.
- No network, subagent dispatch, Git stage, commit, push, rebase, merge, or force operation.

## Acceptance checks

- N1 and the live register match their fixed SHA-256 identities.
- Candidate whitespace runs after the raw candidate is written and before any artifact pins its hash.
- Pre-image census is 81 unique IDs / 48 unique families; post-image census is 83 / 50 with only K-CONSENT-1 and K-UNTYPED-1 added.
- Every row points to resolved contract candidate `a7928297...` and decomposition candidate `932b890e...`; every line anchor resolves.
- Changed/new rows cover the exact Gate-3 amendment and consequential enforcement-map set.
- K-CONTROL-1 is exactly `PENDING_ROOT_AMENDMENT`; no field claims that the Root amendment, Gate-5 eligibility, implementation coverage, or application exists.
- CSV parses, IDs are unique, write containment passes, and protected surfaces remain exact.

## Escalation conditions

Stop and report if N1, the live register, the exact amendment set, source anchors, accounting, or a protected surface differs; if K-CONTROL-1 cannot be represented as ineligible without a stale claim; or if another writer overlaps N2's fixed paths.
