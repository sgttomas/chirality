# Launch Brief — A2-INVENTORY-R2

RunID: `TM-FEDERATION-SURVEY-20260802`
Parent: `HELPS_HUMANS`
Construction: `sealed ephemeral Agent 2 generalist`
Status: `SEALED`

## Purpose

Freshly inventory the live canonical Task Management federation and assess
the frozen component design before any R2 write-capable implementation.

## Governing context

Read `AGENTS.md`, `agents/AGENT_TASK.md`, the authorized implementation plan,
`execution/_Coordination/AgentRuns/TM-FEDERATION-SURVEY-20260802/BASELINE.md`,
and the frozen `COMPONENT_DESIGN.md`. Treat partial candidate edits from other
lanes as unaccepted evidence. Report contradictions; do not change design.

## Read scope

Repository-wide read-only access needed to inspect Git tracking state,
canonical Task Management registers, cited notices, the existing validator,
tool/tests, and adoption decisions.

## Write scope

Only this instance's `RETURN.md` and `STATUS.json`.

## Tasks

1. Enumerate every tracked canonical register and every tracked/untracked
   `_TaskManagement/REGISTER.csv` lookalike excluded by the frozen patterns.
2. Validate every canonical register and infer its loop namespace.
3. Inventory exact cross-register tokens from `ActionItemID`, `SourceRef`,
   `NoticeRef`, `ElevatedTo`, `Status`, and `Disposition`.
4. Identify duplicate IDs, missing/ambiguous notices, closure echoes,
   unsupported shapes, and H1 risks with exact path/row evidence.
5. Produce an exhaustive fixture/acceptance matrix for the implementation.
6. Hash every canonical register and prove this run wrote none.

## Exclusions

No delegation, register mutation, semantic disposition, tool/agent/test edit,
schema proposal, or write outside the two instance record files.

## Required return

Write a structured `RETURN.md` with status, commands, complete inventory,
live findings, fixture matrix, compatibility/H1 assessment, before/after
hashes, and write-containment proof. Update `STATUS.json` to terminal state.
