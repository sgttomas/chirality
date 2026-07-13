# P4 Ten-Pilot Package Fan-In

Snapshot status: CANDIDATE — AWAITING HELP_HUMAN P-F FAN-IN
Verdict: BLOCKED

## Accepted population and substantive results

The exact population is six App PKG-07 members and four Piping PKG-13 members.
Both package managers are terminal PASS. Ten accepted child returns are
terminal PASS. The abandoned App DEL-07-01 attempt remains nonterminal,
unaccepted substrate evidence; only fresh TASK-APP-DEL-07-01-R1 counts.

Independent reconciliation passed 40/40 live legacy source hashes, 10/10
status hashes, ten IN_PROGRESS states, ten byte-exact Stage-1 candidates, ten
current LEGACY_FOUR_DOC states, ten isolated SOW_V1 target states, 325/325
PRESERVED mappings, 3,466/3,466 preserved source lines, all map targets and
parity rows, all repeated checklists/renders, all 30 child verdict classes, 50
unique replacement paths, exact 50-row rollback inversion, and 10/10 apply
plus 10/10 rollback simulations. There are zero unresolved targets, parity
issues, semantic additions, lifecycle/control deltas, missing members, or
waivers.

## Blocking portability finding

PF-PORT-001 is a required-gate failure. The literal checkout prefix
/Users/ryan/ai-env/projects/chirality/ occurs 46 times across 17 package
evidence paths. /var/folders/ occurs zero times.

- accepted App child evidence: 32 occurrences across 12 paths
- accepted Piping child evidence: 10 occurrences across four paths
- abandoned App DEL-07-01 attempt: four occurrences in one unaccepted run record
- parent-owned RECON-PF brief, both manager launch briefs, package
  manifests/checks/handoffs, candidate blobs, and amendment: zero

Accepted terminal evidence alone contains 42 non-portable occurrences across
16 paths. Exact affected inventory:

- execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-01-R1/RETURN.md — 2 occurrences
- execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-06/RETURN.md — 2 occurrences
- execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-02/RETURN.md — 2 occurrences
- execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-05/RETURN.md — 2 occurrences
- execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-04/RETURN.md — 2 occurrences
- execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-03/RETURN.md — 2 occurrences
- execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-03/workspace/target_state/_run_records/TASK_RUN_2026-07-13_0402.md — 3 occurrences
- execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-04/workspace/target_state/_run_records/TASK_RUN_2026-07-13_0408.md — 3 occurrences
- execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-05/workspace/target_state/_run_records/TASK_RUN_2026-07-13_0412.md — 3 occurrences
- execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-02/workspace/target_state/_run_records/TASK_RUN_2026-07-13_0400.md — 3 occurrences
- execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-01/workspace/target_state/_run_records/TASK_RUN_2026-07-13_0339.md — 4 occurrences
- execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-06/workspace/target_state/_run_records/TASK_RUN_2026-07-13_0417.md — 4 occurrences
- execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-01-R1/workspace/target_state/_run_records/TASK_RUN_2026-07-13_0351.md — 4 occurrences
- execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-P/children/TASK-PIP-13-01/workspace/_run_records/TASK_RUN_2026-07-13_0432.md — 1 occurrence
- execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-P/children/TASK-PIP-13-04/workspace/_run_records/TASK_RUN_2026-07-13_0441.md — 3 occurrences
- execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-P/children/TASK-PIP-13-03/workspace/_run_records/TASK_RUN_workspace_2026-07-13_0440.md — 3 occurrences
- execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-P/children/TASK-PIP-13-02/workspace/_run_records/TASK_RUN_2026-07-13_0432.md — 3 occurrences

RECONCILIATION has no repair authority for these manager/child artifacts. P-G
remains blocked. HELP_HUMAN must route evidence-only portability remediation
and hash rebinding, followed by a complete RECON-PF rerun.
