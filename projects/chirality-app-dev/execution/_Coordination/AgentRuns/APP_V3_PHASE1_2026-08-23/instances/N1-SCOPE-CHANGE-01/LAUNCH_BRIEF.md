# Sealed Launch Brief — N1 SCOPE_CHANGE

**Run:** `APP_V3_PHASE1_2026-08-23`
**Instance:** `N1-SCOPE-CHANGE-01`
**Requested by:** HELP_HUMAN under Ryan Tufts's Phase-1 direction
**Role:** Agent 1 `SCOPE_CHANGE`
**Basis:** exact commit `f485b5d3b663f42be8f8cab8432ced9024d7381b`
**Branch:** `codex/app-v3-phase1-2026-08-23`

## Objective

Produce the exact Gate-3 amendment package for SCA-APP-008 as an addition-only, mechanically applicable candidate. The package remains `AWAITING_OWNER_APPROVAL`; it applies no truth and grants no implementation, lifecycle, release, or foreign-loop authority.

## Required reads

- root `AGENTS.md` and `agents/AGENT_SCOPE_CHANGE.md` in full;
- App `LOOP_INIT.md` and the selected committed workplan;
- Phase-1 steer SHA-256 `7d700af0b05c754e468d958a7580fff713f743ad789540d8c4176bf8711ed394`;
- A2 ruling SHA-256 `37e6b6d60874ded0727cf65f25aea09cc961bd35b135b5b8eb33c0d20c1f6158`;
- G0 and A1 records;
- all eleven frozen SCA-APP-008 assessment files;
- live decomposition, contract, invariant coverage register, and exact target lines required to construct post-image candidates.

## Allowed writes

1. Exactly one new content file: `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/Gate3/GATE3_AMENDMENT_PACKAGE.md`.
2. This instance's `LAUNCH_BRIEF.md`, `STATUS.json`, `RETURN.md`, and evidence-only working files if strictly necessary.
3. As run integration owner only: run-root `ORCHESTRATION_PLAN.md` and `WORK_GRAPH.json`.

No existing SCA assessment file may be modified. No other write is allowed.

## Tools and environment

- Read-only shell and Git inspection.
- `apply_patch` only for repository writes.
- Deterministic local validation commands.
- No network.
- No subagent dispatch required by this sealed N1 brief.
- No git stage, commit, push, rebase, merge, or force operation.

## Outputs

The Gate-3 package must provide exact target paths, basis SHA-256 values, current line citations, and full-file candidate bytes or byte-precise replacement hunks for:

- stable-ID/no-topology carrier amendments for DEL-02-05, DEL-08-04, DEL-08-05, and DEL-09-05;
- strict WP-09 authoring versus WP-11 owner-act separation;
- contract candidates K-CONTROL-1, K-ROLE-2, K-NET-1, K-KEY-1, K-EVENT-3/4/6, K-CONSENT-1, K-UNTYPED-1, plus consequential enforcement-map rows, all labelled `CONCORDANCE_GATED_CANDIDATE`;
- K-EVENT-4's exact live Root session path as an unresolved question, never an invented answer;
- unchanged D-APP-103 deferral semantics, with no decision-replay packet.

## Acceptance checks

- Basis pins and all eleven frozen assessment hashes match A2.
- Proposed hunks apply mechanically to the exact basis pre-images.
- Stable IDs and 10-package/51-deliverable topology remain unchanged.
- Every required contract candidate and consequential enforcement row is present and visibly concordance-gated.
- K-EVENT-4 remains a question.
- D-APP-103 deferral is unchanged and no packet exists.
- Only the allowed new content file and run evidence paths are written.
- `_LATEST.md`, App register, frontend tree, existing SCA files, contract, decomposition, SOWs, status/dependencies/lifecycle, Root, docs, plans, and other projects remain unchanged.
- Candidate whitespace and `git diff --check` pass for N1 outputs.

## Escalation conditions

Stop and report if any basis pin, frozen file, target pre-image, or live line differs; if exact contract/concordance semantics cannot be expressed without answering an owner/Root question; if the target set is ambiguous in a way that changes candidate semantics; or if another writer overlaps N1's fixed paths.
