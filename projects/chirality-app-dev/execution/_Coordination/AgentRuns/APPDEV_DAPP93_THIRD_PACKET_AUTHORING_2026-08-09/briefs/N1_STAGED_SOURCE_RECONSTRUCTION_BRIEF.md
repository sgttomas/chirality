# Sealed brief — N1 staged source reconstruction and fresh ledger

RequestedBy: `WI-PKG09-DAPP93-THIRD-01`
RunID: `APPDEV_DAPP93_THIRD_PACKET_AUTHORING_2026-08-09`
ParentInstanceID: `WI-PKG09-DAPP93-THIRD-01`
ChildInstanceID: `A2-DAPP93-THIRD-N1-01`
PackageID: `PKG-09`; DeliverableID: `DEL-09-04`

## Objective

Reconstruct from accepted non-draft sources a complete, fresh command-
authority ledger for a future owner-operated D-APP-93 packet under D-APP-94
Final Posture Option A. Use the new contiguous namespace `L3-CMD-001` upward.
Do not author packet files. Do not execute any represented command.

## Declared reads

- `AGENTS.md`, `agents/AGENT_TASK.md`, this brief, `ACTIVATION.md`,
  `WORK_GRAPH.md`, and `HISTORICAL_ID_REJECTION.md`;
- the D-APP-93 and D-APP-94 rows in `_DECISIONS/_REGISTER.md`, their selected
  packets, and their final ruling records;
- accepted D-APP-92 Attempt-5 evidence only: `HANDOFF_STATE_R5.md`,
  `MANAGER_RETURN_R5.md`, `VALIDATION_R5.md`, `evidence/attempt5/**`, and
  `proposed/attempt5/apply-local-electron-dist-overlay.mjs` in
  `APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/`;
- accepted D-APP-94 R8/final-adoption basis only:
  `HANDOFF_STATE_R8_POST_PROBE_DECISION_READY.md`,
  `HANDOFF_STATE_DAPP94_FINAL_POSTURE_OPTION_A_ADOPTION.md`,
  `MANAGER_FREEZE_R8_INTAKE_POST_PROBE_DECISION_PACKET.md`,
  `STATIC_VALIDATION_R8_INTAKE_POST_PROBE_DECISION_PACKET.md`,
  `prepared/OPTION_C_FEASIBILITY_PROBE_PACKET_R8_NO_EXPLICIT_UNLOCK.md`,
  `prepared/run-dapp94-option-c-probe-r8.zsh`, and
  `prepared/dapp94-safe-storage-probe.cjs` in the D-APP-94 Option-C probe root;
- current static repository bytes needed to bind paths, packages, scripts,
  hashes, or validation commands, limited to `projects/chirality-app-dev/**`
  outside every excluded blocked root.

The three blocked roots in `validation/HISTORICAL_ROOT_PRESERVATION.md` are
absolute read/write exclusions. Do not open, search, copy, or cite them.

## Allowed tools and writes

Read-only shell discovery and hashing; `apply_patch` for writes. Writes are
limited to the seven named durable outputs below. No network, execution of a
packet/probe/build/runtime/debugger command, package/build, Security/Keychain,
credential, GUI/helper, signal, product, Git, or foreign-loop action.

## Stages, outputs, and shared clock

1. Source inventory, 10 minutes:
   `source_reconstruction/STAGE_1_SOURCE_INVENTORY.md`.
2. Authority semantics, 12 minutes:
   `source_reconstruction/STAGE_2_AUTHORITY_SEMANTICS.md`.
3. Core command extraction, 15 minutes:
   `source_reconstruction/STAGE_3_COMMAND_EXTRACTION_CORE.csv`.
4. Safety/stop/return/cleanup extraction, 15 minutes:
   `source_reconstruction/STAGE_4_COMMAND_EXTRACTION_SAFETY.csv`.
5. Complete ledger assembly, 18 minutes:
   `source_reconstruction/STAGE_5_COMMAND_AUTHORITY_LEDGER.csv`.
6. Alignment and completeness check, 12 minutes:
   `source_reconstruction/STAGE_6_LEDGER_ALIGNMENT_CHECK.md`.
7. Terminal child return, 8 minutes:
   `returns/N1_TERMINAL_RETURN.md`.

Total expected duration: 90 minutes. Write each output immediately when its
stage completes; never accumulate stages in memory for a terminal dump.
Notify the manager after every durable write, naming path, byte count, stage,
coverage, and next stage. The manager's cumulative checkpoints are 10, 22,
37, 52, 70, 82, and 90 minutes. Progress is durable-output growth, not chat.
Mere quietness is not a failure. Interruption is allowed only after one full
declared interval with zero new durable output.

## Ledger contract and acceptance

The final CSV has one row per exact literal shell/LLDB/operator-input or
evidence-producing command and at least these columns:
`command_id,phase,actor,exact_command,purpose,preconditions,authority_class,
required_owner_approval,expected_outputs,success_gate,failure_route,
cleanup_or_rollback,source_basis`.

It must be internally complete across preflight, reconstruction, dependency
projection, local offline package construction, identity/topology capture,
sealed-HOME/keychain preparation, helper/GUI launch, exact direct-child PID
binding, LLDB attach/input, first signal, bounded observations, evidence
returns, stop/deviation retention, cleanup/rollback, ingestion preparation,
and terminal status. Historical IDs may be read only in accepted sources to
recover semantics; they must never appear in any new output. Source citations
use paths/section names and hashes, not historical command identities.

Run the manager-defined historical-ID scan over the final ledger and report
the exact zero-hit result. Escalate any source contradiction, inability to
state an exact command safely, noncontiguous ID, missing failure route,
historical-ID hit, excluded-root need, or authority ambiguity. Do not invent
execution authority. Return PASS only if coverage is complete and all checks
are evidenced; otherwise return a precise BLOCK and preserve completed stages.
