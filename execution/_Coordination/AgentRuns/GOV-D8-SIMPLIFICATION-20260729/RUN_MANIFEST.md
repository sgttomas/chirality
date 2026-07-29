# Run Manifest — GOV-D8-SIMPLIFICATION-20260729

Status: `AUTHORED — HUMAN-GATED PR REQUIRED`
Parent: HELP_HUMAN (Agent 0, loop-readiness transition program session)
Lane: HELPS_HUMANS
Executor: bounded Agent 2 AUTHOR (this run; no delegation)
Accepted Git basis: `2dace6ec6e3342a415342a539d5630969cbba39c` (Receipt 63;
SCA-002 applied; PRD Rev 7 §5.3.1 live)
Branch: `gov/step4-sca-application`

## Objective

Apply the owner-directed simplification of the merge-execution policy: the
bounded-grant mechanism adopted through D-GOV-31 is replaced by the owner's
direction, recorded in the loop's ordinary closeout evidence (approved
source HEAD, owner direction, effective merge SHA). Default remains
human-gated PRs; standing prohibitions and K-MERGE-1 unchanged. Change
vehicle: PR review per the register's terminal-artifact rule; no new D-GOV
record; D-GOV-31's decision record is unedited and remains historical.

## Owner act of record (verified byte-exact before transcription)

| Act | Bytes | SHA-256 |
|---|---|---|
| Owner direction, in-session 2026-07-29 (transcribed verbatim in Receipt 64 and in the tranche manifest) | 181 | `d89bcdef36398ec7c345a48e0b3d65b30c635cf09aed0bf8f2a5a3c89c1b33d0` |

Earlier in the same session the owner stated the governing epistemology:
telling the agent to merge is sufficient; owner-typed and agent-as-proxy
execution carry the same authority; no grant record, registry, or log is
to exist.

## Exact write scope

Modified:

- `docs/PRD_ROOT.md` (D-8 row; annex §5.3.1 rewritten compactly)
- `execution/_Coordination/LOOP_INIT.md` (§7 closeout bullet)
- `agents/AGENT_CHANGE.md` (all grant-mechanism passages; new SHA-256
  `950e96f4cfff13af48b9edd93a4b47356e8b388a430d70977fd528ffbd4120fa`)
- `projects/chirality-app-dev/execution/_Coordination/NOTICE_D-GOV-31_MERGE_GATE_POLICY_SUCCESSION.md` (dated update appended)
- `projects/pec/execution/_Coordination/NOTICE_D-GOV-31_MERGE_GATE_POLICY_SUCCESSION.md` (dated update appended)
- `projects/chirality-piping/execution/_Coordination/NOTICE_D-GOV-31_MERGE_GATE_POLICY_SUCCESSION.md` (dated update appended)
- `execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv` (SOW-042
  statement cell; CRLF preserved)
- `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`
  (DEL-04-06 Description and AnticipatedArtifacts; LF preserved)
- `execution/PKG-04_Developmental_Machinery_and_Change_Control/1_Working/DEL-04-06_Change_Management_and_Human_Gated_Closeout/ScopeOfWork.md`
- `execution/PKG-04_Developmental_Machinery_and_Change_Control/1_Working/DEL-04-06_Change_Management_and_Human_Gated_Closeout/_CONTEXT.md`
- `tools/validation/validate_instruction_tranche_manifest.py`
  (`merge_execution_grant` semantics replaced by `m2_gate.owner_direction`)
- `tools/validation/test_validate_instruction_tranche_manifest.py`
- `execution/_Coordination/LOOP_RECEIPTS.md` (Receipt 64 appended)

Deleted:

- `docs/governance_harness/_PROPOSALS/GRANT-2026-07-29_transition_merge_execution/`
  (unruled draft, never issued; the owner rejected the mechanism it drafts)

Added:

- `docs/governance_harness/tranche_manifests/ROOT-D8-SIMPLIFICATION-20260729.yaml`
- `execution/_Coordination/AgentRuns/GOV-D8-SIMPLIFICATION-20260729/{RUN_MANIFEST,VALIDATION,HANDOFF_STATE}.md`

## Prohibitions honored

- No push, no merge, no PR creation; one commit on
  `gov/step4-sca-application` only.
- D-GOV-31 decision record, frozen proposal packages, receipts 0–63,
  prior snapshots, and SHA-pinned mirrors untouched.
- Notice updates are appends; existing notice text unedited.
- No new grant-style instrument of any kind is created.

## Engine identity

Provider: Anthropic
Engine: Claude Code (Agent SDK)
Model: claude-fable-5
