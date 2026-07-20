# W1-DAPP50-HEADLESS-LIVE — Sealed WORKING_ITEMS Brief

## Identity and authority

- **Role:** WORKING_ITEMS (Agent 1), one serialized integration owner
- **Parent control:** ORCHESTRATOR control package for HELP_HUMAN
- **RunID:** `APPDEV_LOOP_2026-07-20_DAPP50_HEADLESS_LIVE`
- **Basis commit:** `bc35e3b0049d990f494dd3610603be285c7aa9ed`
- **Required branch:** `codex/app-dev-dapp50-headless-live-20260720`
- **Authority:** D-APP-50 Option A and riders; only the already-ruled
  `domain_headless_preview_run` read-side live flip
- **Delegation:** prohibited
- **Git:** prohibited

Read full `AGENTS.md`, `agents/AGENT_WORKING_ITEMS.md`, the run `BASIS.json`,
D-APP-50 packet/ruling, D-APP-53 packet, DEL-10-01 `_STATUS.md`, piping D-33 /
DEC-065 and TP-RUNNER-015 record before editing. Reproduce branch, HEAD, basis
hashes, Receipt-82, receipt validation, and clean-start containment. Return
`BLOCK` on mismatch; do not repair the basis.

## Objective

Implement a configured local `openpipestress-runner solve` child-process
transport and flip only
`mcp__chirality__domain_headless_preview_run` from descriptor-only to live for
`profileId: "open_pipe_stress"`. This is an adapter over piping's DEC-065
runner, not a solver or standalone harness.

## Required behavior

1. Require two explicit local configuration values: runner executable path and
   expected lowercase/normalized SHA-256. The executable path must be absolute.
   Resolve it with filesystem realpath and verify that the resolved target is a
   regular file, has executable permission (`X_OK`), and hashes exactly to the
   configured expected SHA-256 immediately before spawn. No `PATH` lookup,
   shell, command string, package-script discovery, repository scan, or
   fallback binary is allowed. Refuse missing, relative, nonexistent,
   non-regular, non-executable, malformed-hash, and hash-mismatch cases.
2. Spawn the verified absolute realpath directly as one foreground child with
   argv exactly `solve`; use a deliberately sanitized/minimal environment;
   never inherit secrets or broad ambient environment by default. No network,
   daemon, telemetry, hidden filesystem mutation, SQL/SQLite access, output
   path, or sidecar.
3. Replace the stale `modelInputPath` tool-input/descriptor concept with
   `runnerInputRef`. Resolve the ref through existing project-root read
   containment (including realpath/symlink escape refusal). The referenced
   regular file must contain the complete schema-first DEC-065 JSON request,
   not a preview fragment and not a generated command. Pass its exact validated
   bytes to stdin; use stdout as the sole result channel. Record why the old
   field became false once the final DEC-065 request envelope superseded the
   provisional TP-RUNNER-014 model-only fixture.
4. Enforce a deterministic timeout and independent hard caps of 2 MiB each on
   stdout and stderr. Terminate/reap on timeout or cap breach. Parse exactly one
   JSON result from stdout only after bounded collection. Never include raw
   stderr, executable paths, ambient config, or secrets in model-visible
   errors/events/artifacts.
5. Preserve DEC-065 exit semantics: exit 0 means completed with no blocking
   runner diagnostics; exit 1 is a structured blocking/validation outcome and
   must remain visibly non-successful without being misreported as a transport
   crash; exit 2 is usage/malformed/unsupported and is a transport/input
   refusal. Signals, spawn errors, timeouts, oversize, invalid JSON, and schema
   mismatches fail closed with stable sanitized error codes.
6. Gate the live handler and descriptor to exactly `open_pipe_stress`.
   Explicitly refuse `pec`, unknown, missing, or mismatched profiles. Do not
   modify the pec proposal tools. Keep the descriptor read-only,
   `project-root-read`, exclusive, input-dependent, with truthful local-process
   transport and no human confirmation. No apply/accept/refresh/propose path.
7. Route invocation through the existing read-MCP path policy, permission,
   permission-event, redaction, result-budget, tool-evidence, and artifact
   handling instead of inventing a parallel event/log channel. Generated tool
   catalog and runtime/adding-a-tool documentation must state the exact
   configured-local transport and its limitations without capability or
   professional claims.
8. If and only if harness-contract exports/descriptors change, bump
   `HARNESS_TOOL_REGISTRY_VERSION` consistently and repin/revalidate the
   D-APP-48 pull contract using the established mechanism. Do not edit piping
   consumption records.

## Mandatory tests

Add hermetic tests using temporary executable fixtures or equivalent
controlled local processes. Cover at least: successful exit-0 JSON; exit-1
blocking diagnostics; unset config; relative path; missing/bad path; malformed
expected hash; hash mismatch; non-regular/non-executable target; timeout;
stdout oversize; stderr oversize; invalid/non-single JSON; runnerInputRef
missing/outside/symlink escape/non-file; complete input bytes delivered on
stdin; `pec` refusal; unknown-profile refusal; read-only/exclusive descriptor;
and proof the normal event/redaction/artifact pipeline is used. Tests must not
depend on a built piping binary or edit/read private external data.

Run focused tests first, then every applicable command named by
`docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`, and
`docs/BUILD_AND_RELEASE.md`, including typecheck, full Vitest, build/premerge,
generated catalog checks, instruction-root integrity as applicable, D-APP-48
contract validation if changed, authority-corpus status, receipt validator,
repo-wide practitioner `self-check`, full practitioner-harness pytest, and Git
diff/whitespace/scope checks. Stop the dev server before commands that own it.

## Write scope

Because Bash is needed, W1 is the serialized integration owner with explicit
read/write scope over `projects/chirality-app-dev/**`, narrowed as follows:

- runtime/contract/tests/generated docs under
  `projects/chirality-app-dev/frontend/**` that are necessary for this one tool;
- conditional D-APP-48 pull-contract repin only if contract exports change;
- DEL-10-01 `_STATUS.md` and exactly one new DEL-10-01 `_run_records/**` record;
- `projects/chirality-app-dev/loop/LOOP_RECEIPTS.md`, one appended receipt only;
- this instance subtree for `RETURN.md`, `HANDOFF.md`, and terminal
  `STATUS.json`.

All other app-dev paths are read-only. Never edit the parent control files.

## Prohibitions

No files under `projects/chirality-piping/**`, `_DomainEngines/**`, or
`projects/pec/**`; no bundling, packaging, signing, notarization, publication,
distribution, release-readiness, professional, certification, sealing,
authentication, code-compliance, or solver-truth claim; no endpoint/public
transport; no provider/network expansion; no apply-class tool or tool name;
no `domain_proposal_validate` open_pipe_stress transport; no pec changes; no
lifecycle state or Checking Approval SHA change; no decision/register edits;
no waiver; no Git action.

## Closeout and return

Only after all mandatory checks pass:

- remove exactly the DEL-10-01 Remaining bullet for the headless-preview live
  flip, preserving the separate new-owner-ruling bullet byte-for-byte;
- append one dated history line, without lifecycle change;
- create one run record with authority, design rationale, changed paths,
  rejected alternatives, test evidence, boundaries, and residuals;
- append exactly one minimal Receipt-83 under the ledger's local rules and
  rerun its validator.

Write `RETURN.md`, `HANDOFF.md`, and terminal `STATUS.json`. Return exactly
`ACCEPT` or `BLOCK`, with exact changed/untracked/staged path accounting,
checks, hashes, receipt number/hash, preserved-boundary proof, blockers,
unknowns, waivers, and recommended next gate. Do not release EVALUATION or
CHANGE.
