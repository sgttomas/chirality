# Launch Brief — A2-IMPLEMENT-R2

RunID: `TM-FEDERATION-SURVEY-20260802`
Parent: `HELPS_HUMANS`
Construction: `sealed ephemeral Agent 2 generalist implementing the generic TASK contract`
Status: `SEALED — HOLD FOR VALIDATED A2-INVENTORY-R2`

## Purpose

Implement the frozen Task Management federation-survey command and exhaustive
focused tests after HELPS_HUMANS accepts the R2 inventory.

## Governing context

Read `AGENTS.md`, `agents/AGENT_TASK.md`, the authorized implementation plan,
the frozen `COMPONENT_DESIGN.md`, `BASELINE.md`, and the accepted
`A2-INVENTORY-R2/RETURN.md`. Existing partial edits, if any, are unaccepted
evidence and must be inspected rather than assumed correct.

## Read scope

The governing files above, `.gitignore`, the four live registers and cited
notices for read-only fixture understanding, and existing
`tools/taskmgmt/taskmgmt.py` / `test_taskmgmt.py`.

## Write scope

Exactly:

- `tools/taskmgmt/taskmgmt.py`;
- `tools/taskmgmt/test_taskmgmt.py`;
- this instance's `RETURN.md` and `STATUS.json`.

## Tasks

1. Add `federation --register PATH [--out PATH]` without regressing existing
   `validate` or `scan` commands.
2. Implement exact Git-tracked sanctioned-path discovery, validator reuse,
   namespace inference, typed-field joining, notice resolution, all twelve
   finding classes, COMPLETE/PARTIAL/operational semantics, Root/global versus
   non-Root relevance, deterministic JSON/console output, and register
   before/after hashes with zero-write proof as frozen in COMPONENT_DESIGN.
3. Default output beside the invoking register under
   `.candidates/federation.json`; permit explicit `--out` for tests.
4. Add exhaustive unit tests for every discovery path/form, excluded tracked
   and untracked lookalikes, every finding class, notice-list/anchor behavior,
   determinism, exit semantics, presentation, CLI compatibility, and zero
   register writes.
5. Run the focused suite and a live read-only survey against Root and App
   using an explicit temporary output outside the repository when practical.
6. Report exact modified paths and prove no register or other file changed.

## Exclusions

No delegation; no agent, governance, manifest, notice, ignore, register,
loop, CI, schema, CONTRACT/PRD, receipt, handoff, commit, push, or merge edit.

## Required return

Write `RETURN.md` with status, design traceability, changed paths, test and live
command results, coverage/findings, before/after hashes, limitations/H1 needs,
and write-containment proof. Update `STATUS.json` to terminal state.
