# Sealed Launch Brief — N1 Notice Ingestion

## Role and non-delegation

You are the Root loop's ordinary session acting as one bounded instance. Do not delegate or create another orchestration layer. K-SUBAGENT non-delegation is instruction-asserted. The same instance later acts as Root `TASK_MANAGEMENT` for N2 and publishes the R18 pair for N3; those nodes leave their evidence at their governed paths.

## Accepted basis

- Repository basis: `8140daec7ab7165f8972451dbdd3a67b8bb2fd38` (PR #680 merge commit; equals `origin/main` at branch time)
- Ruling record R18: `plans/steers/chirality_app_v3_root_ruling_record_r18_2026-09-03.md` (published with this run; SHA-256 recorded in Receipt 131)
- Steer: `plans/steers/chirality_app_v3_r18_notice_ingestion_steer_root_2026-09-03.md` (published with this run; SHA-256 recorded in Receipt 131)
- A11 SHA-256: `6197bae1aad25e6fd7dfa6befb0212acb5da24654f49f97536dbc2d365aeca27`
- Source notice SHA-256: `b68ed592b310fa996bb10d2aaf6889a25eb0481e6a57ce3fb2e414b775e4ee2b` (5228 bytes)
- D-APP-98 SHA-256: `71dfc1ae6369acea1e49f71d68e45aaf9da8f14c5f6a77733845c43f3ee7c020`

## Objective

Record the routed App Electron-authority disposition notice on the Root coordination surface — a Root ingestion header naming the PR #680 merge identity and Root's `ADOPTED_AS_COORDINATION_INPUT` disposition, followed by the App body as exact bytes — and produce read-only evidence of whether any factual claim in the notice diverges from live bytes at the basis.

## Read scope

- The source notice on the App coordination surface
- `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-98_RULING_ELECTRON_AUTHORITY_2026-08-17.md` and `D-APP-72_RULING_2026-07-21.md`
- `projects/chirality-app-dev/frontend/package.json`, `package-lock.json`, and `frontend/scripts/verify-electron-dist.mjs`
- The eight App documents the notice lists with post-image SHA-256 values
- `projects/chirality-app-dev/execution/_Reconciliation/References/AUTHORITY_CORPUS.json`
- The 2026-08-24 App candidate file and the Root 2026-08-03 notice on the App surface
- Git ancestry of the notice's content commit and stated basis relative to the PR #680 merge
- The 2026-08-24 Root ingestion precedent, A11, R11, R16, R17, and the R18 pair

## Write scope, exactly

- `execution/_Coordination/NOTICE_2026-09-03_APP_TM-ROOT-122_ELECTRON_AUTHORITY_DISPOSITION.md`
- New files only inside `execution/_Coordination/AgentRuns/ROOT_NOTICE_INGESTION_2026-09-03/instances/N1_NOTICE_INGESTION/`

Do not write App paths, the Root contract, any register (N2 owns the register act), any receipt, the live Root handoff, or any other path.

## Method

1. Reverify the basis: PR #680 `MERGED`; `HEAD` = `origin/main` = the merge commit; source notice, A11, and D-APP-98 hashes; destination absence.
2. Build the destination as UTF-8 header bytes followed by the source file's raw bytes read in binary. Do not re-type, reflow, annotate, or patch the body.
3. Require that the trailing 5228 bytes of the destination compare equal to the source (`cmp`), and record the destination SHA-256.
4. Recompute every identity the notice asserts and confirm its Git claims; tabulate observed versus claimed. Any exact mismatch: stop, report, repair nothing.
5. Write `CONTRACT_DRIFT_CHECK.md`, `RETURN.md`, and terminal `STATUS.json` inside the instance folder.

## Return contract

Return exact observed hashes, a per-claim drift table with a verdict, the destination identity, changed paths, and any blocker. Stop without repair on any divergence or identity disagreement.

## Acceptance checks

- Trailing 5228 bytes of the destination are byte-identical to the source; the header names the PR #680 merge commit and `ADOPTED_AS_COORDINATION_INPUT`.
- No App path or Root governed content outside the declared destination changes in N1.
- Drift evidence cites exact observed values and concludes either `NO_EXACT_DIVERGENCE` or records the exact divergence and stops.
- Status is terminal and the return is self-contained.
