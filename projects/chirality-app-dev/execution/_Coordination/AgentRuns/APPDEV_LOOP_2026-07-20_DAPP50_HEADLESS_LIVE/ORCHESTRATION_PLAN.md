# Orchestration Plan — D-APP-50 Headless Preview Live Transport

- **RunID:** `APPDEV_LOOP_2026-07-20_DAPP50_HEADLESS_LIVE`
- **Plan:** v1, frozen at `bc35e3b0049d990f494dd3610603be285c7aa9ed`
- **Pattern:** one serialized integration owner; no fan-out
- **Released node:** `W1-DAPP50-HEADLESS-LIVE` / WORKING_ITEMS

## Objective

Make only `mcp__chirality__domain_headless_preview_run` live for the ruled
`open_pipe_stress` profile by adapting the final local DEC-065
`openpipestress-runner solve` process. Preserve the harness as the governance,
audit, redaction, and adapter layer; do not reproduce piping mechanics.

## Required implementation outcome

The transport is configured with both an absolute executable path and its
expected SHA-256. Before every invocation it resolves the executable realpath
and verifies absolute path, regular-file status, executable permission, and
exact hash. It never searches `PATH`, invokes a shell, edits piping, or treats
a configured string as trusted. It launches one foreground process with a
sanitized environment, sends the complete DEC-065 JSON request on stdin,
reads structured JSON only from stdout, applies a bounded timeout and separate
2 MiB stdout/stderr caps, and maps DEC-065 exits 0/1/2 without converting a
blocking diagnostic into transport success.

The MCP input uses a project-root-contained `runnerInputRef` whose referenced
file contains the complete DEC-065 JSON request. The stale
`modelInputPath` descriptor/input concept is removed, with the rationale
recorded in the deliverable run record. Profile gating is exact:
`open_pipe_stress` only; `pec` and every unregistered profile refuse. The tool
remains read-only and exclusive and flows through the normal read-MCP
permission, path, event, redaction, result-budget, and artifact pipeline.

## Gates

W1 returns `ACCEPT` only after focused tests and the applicable app-dev
typecheck, Vitest, build/premerge, generated-doc, authority-corpus, receipt,
repository self-check, full practitioner-harness pytest, and scope/diff checks
pass. Only then may it remove the exact live-flip Remaining bullet from
DEL-10-01, append history, create one run record, and append exactly one loop
receipt. No lifecycle state or Checking Approval SHA changes.

EVALUATION and CHANGE are not released. Git is not released.
