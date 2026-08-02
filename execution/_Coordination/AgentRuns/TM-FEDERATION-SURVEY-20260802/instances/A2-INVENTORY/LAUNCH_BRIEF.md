# Launch Brief — A2-INVENTORY

RunID: `TM-FEDERATION-SURVEY-20260802`
Parent: `HELPS_HUMANS`
Construction: `sealed ephemeral Agent 2 generalist`
Status: `SEALED`

## Purpose

Inventory the live canonical Task Management federation before implementation.

## Governing context

Read `AGENTS.md`, `agents/AGENT_TASK.md`, the authorized implementation plan,
and `execution/_Coordination/AgentRuns/TM-FEDERATION-SURVEY-20260802/COMPONENT_DESIGN.md`.
The component design is frozen; report contradictions rather than changing it.

## Read scope

Repository-wide read-only access needed to inspect tracked Task Management
registers, cited notices, existing validator/tool/tests, Git tracking state, and
applicable adoption decisions.

## Write scope

Only this instance's `RETURN.md` and `STATUS.json`. No other file writes.

## Tasks

1. Identify every canonical tracked Task Management register and loop namespace.
2. Validate every register with the existing validator.
3. Inventory exact uses of `ActionItemID`, `SourceRef`, `NoticeRef`,
   `ElevatedTo`, `Status`, and `Disposition`.
4. Identify cross-register links, missing/ambiguous notices, duplicate IDs,
   unsupported shapes, and compatibility risks.
5. Propose the exact fixture matrix required by the frozen design.
6. Report any H1 expansion need; do not resolve it.

## Exclusions

No register mutation, semantic disposition, tool/agent/test edits, delegation,
schema proposal, or write outside the two instance return files.

## Required return

A structured `RETURN.md` with status, commands, complete register inventory,
path/row evidence for every assertion, live relationships/findings, fixture
matrix, compatibility risks, H1 requests, and write-containment statement.
Update `STATUS.json` to terminal state.
