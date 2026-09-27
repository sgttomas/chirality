# Receipt — APP-EXECUTION-ROOT-2026-09-27

Derivative account of a review repair to the App recorded-register read
([FU5 receipt](../APP-RECORDED-REGISTER-2026-09-26/RECEIPT.md)). The sources
below keep their authority.

## Owner direction

CHAT_TRANSCRIPTION — EVIDENCE, NOT RULING. Ryan Tufts, 2026-09-27, Claude Code
conversation. The parent session asked:

> Fix for the symlink target path: make the App use the project's actual
> execution root (outermost execution/ folder, checked against the adapter
> manifest) instead of guessing it from the path shape. Proceed?

Selected option: "Yes, as proposed (Recommended)", which said: "Deliverables
not at <execution root>/PKG-*/<lifecycle>/DEL-* get NOT_ASSESSED with a
reason. This matches the Root reopening check's rule."

## Problem

`executionRootForDeliverable` in
`frontend/src/lib/dependencies/recorded-register.ts` took the execution root
from the shape of the deliverable path (three folders up). A reviewer showed a
request that names a deliverable at the real path behind a linked package
folder, for example `<project>/store/PKG-07_Graph/1_Working/DEL-07-01`. The
read treated `store/` as an execution root and returned a verdict with no
warning. The FU5 `SYMLINKED_UNIT_PATH` check caught only a request made
through the link.

## What changed

- `frontend/src/lib/lifecycle/amendment-reopen.ts` exports
  `resolveExecutionRoot`, the execution-root part of the ported Root checker
  (`_execution_root` in `tools/validation/check_amendment_reopen.py`). It
  returns the root or the reason there is none. The reopening check wraps it
  and keeps its `SCOPE_CHANGE_ROOT_NOT_FOUND` refusals and messages.
- `readDeliverableRecordedRegister` uses that function. The execution root is
  the deliverable's outermost `execution/` ancestor below the canonical
  project root, and an adapter manifest (`_harness/adapter.yaml`) found
  walking up must imply the same folder. The canonical deliverable folder must
  then sit exactly at `<execution root>/PKG-*/<lifecycle folder>/DEL-*` (or
  `CAT-*`/`KTY-*`), compared with `executionRootForDeliverable`, which is now
  only the shape check. Otherwise the judgment is `NOT_ASSESSED` with reason
  `EXECUTION_ROOT_NOT_RESOLVED` (no `execution` ancestor, or the adapter
  manifest disagrees), `DELIVERABLE_OUTSIDE_EXECUTION_ROOT` or
  `EXECUTION_ROOT_OUTSIDE_PROJECT_ROOT`. The reason is also a warning. The
  deliverable's own register is still read.
- `SYMLINKED_UNIT_PATH` and the read containment are unchanged. Both App
  callers read through `readDeliverableDependencies`: the working-root
  dependencies API and the MCP `deps_read` tool. Neither needed a source
  change. The Workbench and Pipeline forms and the HTTP route sources were not
  touched.
- App SPEC §5.2 states the rule.
- The FU5 receipt's Limits carry a dated note pointing here. DEL-07-05 MEMORY
  has a run row.

## Parity

The Root tools take the execution root as `--execution-root`, and the parity
comparison (`actual()` in `recorded-register-parity.test.ts`) calls the
queue functions with the case folder as the root. Those results are unchanged,
and `generate_expected.py --check` passes with no fixture edits.

The fixture case folders are execution roots that are not named `execution`.
For these, `readDeliverableRecordedRegister` takes an optional `executionRoot`
input, the counterpart of `--execution-root`. The tests that read a fixture in
place pass it. It is still held to the containment and exact-position checks.
App callers never pass it. The containment tests now copy each case to
`<project>/execution/` and read with the project as the containment root, so
they exercise the production resolution; their expected warning paths gain
the `execution/` prefix. The working-root contracts and read-MCP test
fixtures moved their deliverable under `execution/` for the same reason.

## Tests added

In `recorded-register-parity.test.ts`:

- the reviewer's case: a linked package requested at its target outside
  `execution/` gives `EXECUTION_ROOT_NOT_RESOLVED`; requested through the
  link, it still gives `SYMLINKED_UNIT_PATH`;
- a linked package whose target is inside `execution/` but off the unit shape
  gives `DELIVERABLE_OUTSIDE_EXECUTION_ROOT`;
- a deliverable outside any `execution/` folder gives no verdict;
- the outermost `execution/` folder governs;
- an adapter manifest that implies another root gives no verdict, and one
  beside the root is judged;
- a normal deliverable under `<project>/execution/`, with an agreeing adapter
  manifest, gets the same judgment, rows and disagreements as the fixture read
  with its root named. An adapter manifest inside the execution root is
  accepted.

The reviewer's case is also covered through the working-root dependencies
route (`deliverable-contracts.test.ts`) and the MCP `deps_read` tool
(`chirality-read-mcp.test.ts`).

## Checks (worktree candidate)

The commit hand-off to the parent session records each command and its exit
status:

- typecheck;
- focused Vitest (recorded-register parity, working-root contracts, read MCP,
  amendment-reopen parity, lifecycle-status);
- full Vitest, where the only failure is the known uid-0
  `harness-attachment-resolver` case;
- the parity generator `--check`;
- export regeneration;
- the G0–G3 Root validators, this ledger's receipt validator, the
  tranche-manifest validator, conflict-marker and leak scans, and
  `git diff --check`.

Independent review and actual-candidate CI remain merge gates.

## Limits

- The execution root is resolved when the read starts. A link swapped in
  after that point is not detected, the same limit FU5 records for each read.
- App SPEC §2 names the root `{EXECUTION_ROOT}` without fixing its folder
  name. A project whose deliverables are not under a folder named
  `execution`, for example a bare `PKG-*` tree at the project root, now gets
  no verdict from the App, as the reopening check already refuses it. The
  Root tools can still be run on it with `--execution-root`.
- No lifecycle transition, dependency acceptance, DAG acceptance,
  authority-corpus repin, Runtime change or release.

Execution: a Claude Code subagent (TASK-type executor, no delegation) in an
isolated worktree for the parent session. Model identifiers are withheld at
the dispatching session's instruction; the commit's session trailer identifies
the run.
