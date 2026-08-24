# Sealed brief — N3 immutable snapshot review and sealing

You are a bounded, fresh Agent 2 reviewer/assembler. You did not author N1 or N2. Role entry is instruction-asserted. Do not delegate.

## Basis and dependency

- Repository root: `/Users/ryan/.codex/worktrees/0b6e/chirality`
- Basis: `origin/main@7974f2d4a456777f2132fb5726a67a042137ca78`, plus terminal N1 and N2 outputs.
- Do not begin until HELP_HUMAN confirms N1 and N2 terminal PASS.

Read root `AGENTS.md`, the Phase 4 steer, R7 record, Receipt 123, all eight estimate files and `ESTIMATE_METHOD.md`, and every accepted input they cite. Use the provenance/no-invention/immutability discipline of `skills/estimate-snapshot/SKILL.md`, with the steer controlling the hours-only form and exact snapshot path.

## Objective and write scope

Independently review, repair where necessary, and seal the package strictly inside `execution/_ScopeChange/SCA-004_2026-08-22_1749/Evidence/ESTIMATE_SNAPSHOT_POST_PHASE3/`. You may edit N1/N2 files only to repair actionable findings, and every repair must be disclosed. Add exactly:

- `SUMMARY.md`
- `INPUT_HASHES.csv`
- `REVIEW.md`
- `RETURN.md`
- `ARTIFACT_HASHES.csv`

You may additionally write only this instance's `RETURN.md` and `STATUS.json`. Use `apply_patch` for all file writes. Do not edit any accepted source or any path outside the snapshot and this instance record.

## Review and sealing contract

1. Verify every estimate element traces to an accepted SOW output/requirement/gate/check, the applied register row, `_CONTEXT.md`, or Phase-3 `_DEPENDENCIES.md`; reject invented scope.
2. Recalculate every line range and per-deliverable/package total from the declared deterministic uncertainty bands.
3. Verify the ten held bindings, TM-ROOT-106/122, C1, and App-owned obligations are exclusions, not assumptions or priced work.
4. Verify dependency text describes risk only and computes no schedule.
5. Check cross-file consistency, no carrier-production double counting in DEL-02-06, and no authority/acceptance implication.
6. Repair under unlimited repair, then perform a fresh review cycle. `REVIEW.md` discloses every finding and repair; terminal review must have zero actionable findings.
7. `INPUT_HASHES.csv` pins every consumed accepted input required by the steer: seven SOWs, the applied register, seven `_CONTEXT.md`, seven `_DEPENDENCIES.md`, DEL-02-06 accepted sources used by N2, and the R7 record. Include other controlling inputs actually consumed, including Phase 4 steer and `ESTIMATE_METHOD.md`, clearly classifying derivative inputs.
8. `SUMMARY.md` defines derivative decision-support status, cites Receipt 123 and the steer, shows the uncertainty classes, per-deliverable base/low/high totals, aggregate totals, exclusions, sequencing-risk summary, and no-schedule/no-acceptance boundary.
9. Package `RETURN.md` closes exactly `AWAITING_OWNER_ACCEPTANCE`, names rerun triggers, remaining gates, and zero granted authority.
10. Generate `ARTIFACT_HASHES.csv` last, sorted by path, hashing every package artifact except itself. State the self-exclusion explicitly in its header/comment convention. If any pinned artifact changes afterward, regenerate it.

## Return contract

Report package inventory and hashes, repairs, review-cycle verdict, input-pin coverage, per-deliverable and aggregate totals, exclusion checks, changed paths, and terminal status `COMPLETE` or `BLOCKED`.
