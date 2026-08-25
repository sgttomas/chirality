# Sealed Launch Brief — N1 Notice Ingestion

## Role and non-delegation

You are one bounded ephemeral Agent 2. Do not delegate or create another orchestration layer. K-SUBAGENT non-delegation is instruction-asserted.

## Accepted basis

- Repository basis: `8884b143f3d8dbca49756e981e4e20299d55875d`
- Steer: `plans/steers/chirality_app_v3_notice_ingestion_steer_root_2026-08-24.md`, SHA-256 `4c9bc1cd6382a47eb5ef1bd56f7aa9d6fa2cce2dda08bd1aded2b2f352a2c2c2`
- R11: `plans/steers/chirality_app_v3_root_ruling_record_r11_2026-08-24.md`, SHA-256 `01d9ae6d42d25942ae4991b61385b8d1a70a8d54a82d88d17648c000d6622fbd`
- Source notice SHA-256: `75c9d5dde1b0c405181baf9b3ee1e8431e7bd5ae920355f3861a8bc51ce8e834`
- Root contract SHA-256: `ad0a4e6ae53853692205b34b2c4416e23d19dabb73079049e5acec09b5beeb83`

## Objective

Copy the exact routed App notice bytes to the Root coordination destination and produce read-only evidence of whether its three Root-facing contract claims diverge from the live ratified Root contract.

## Read scope

- Source notice under the App SCA-APP-008 Phase5 folder
- `docs/CONTRACT.md`, especially K-RUNTIME-1 and K-CONTROL-1
- DEL-02-07 accepted `_CONTEXT.md` and `ScopeOfWork.md`
- Root notice-ledger/history instruments needed to determine whether an inbound row is required
- The steer and R11

## Write scope, exactly

- `execution/_Coordination/NOTICE_2026-08-24_APP_SCA-APP-008_GATE5_APPLIED_STATE.md`
- New files only inside `execution/_Coordination/AgentRuns/ROOT_NOTICE_INGESTION_2026-08-24/instances/N1_NOTICE_INGESTION/`

Do not write App paths, the Root contract, any ledger/register, receipt, handoff, or any other path. If a ledger write appears required, report it as a blocker instead of writing it.

## Method

1. Reverify source, contract, steer, and R11 hashes and destination absence.
2. Use `/bin/cp` to copy the source notice to the destination. Do not re-type, reflow, annotate, or patch its bytes.
3. Require source and destination SHA-256 equality.
4. Record a contract-drift check covering: one live control socket; exclusive daemon ownership of runtime state under K-RUNTIME-1; and the design-gated DEL-02-07/WP-03 supervisor-socket pathway. Distinguish contradiction from wording distributed across K-RUNTIME-1 and K-CONTROL-1.
5. Record whether current Root instruments require an inbound-notice ledger row. The historical 2026-07-28 remediation ledger must not be mutated merely because it exists.
6. Write `CONTRACT_DRIFT_CHECK.md`, `RETURN.md`, and terminal `STATUS.json` inside the instance folder.

## Return contract

Return exact observed hashes, a drift verdict, the ledger disposition, changed paths, and any blocker. Stop without repair on any divergence or identity disagreement.

## Acceptance checks

- Destination SHA-256 exactly `75c9d5dde1b0c405181baf9b3ee1e8431e7bd5ae920355f3861a8bc51ce8e834`.
- No App path or Root governed content outside the declared destination changes.
- Drift evidence cites exact contract rows and concludes either `NO_EXACT_DIVERGENCE` or records the exact divergence and stops.
- Status is terminal and the return is self-contained.
