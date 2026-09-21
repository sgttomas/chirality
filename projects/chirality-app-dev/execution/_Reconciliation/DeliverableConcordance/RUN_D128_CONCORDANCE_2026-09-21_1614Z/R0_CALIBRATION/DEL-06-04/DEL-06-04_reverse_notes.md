# DEL-06-04 — reverse-pass notes (RUN_D128 R0 calibration, unit F-06)

The capability file is `R0_CALIBRATION/SURFACES/HARNESS_capabilities.csv`, with 60 rows.

The forward ledger `DEL-06-04_claims.csv` is sealed and was not modified. Its SHA-256 is
`befbca640d50a66c5244ded461ee68d9f0e723b2c7af9efe215ad6b63642afa4`.

## 1. Response summary

| Response | Rows |
|---|---:|
| CLAIMED_BY | 2 |
| PARTIAL | 7 |
| NOT_MINE | 51 |

- **CLAIMED_BY:**
  - CAP-HARNESS-045 (tool path policy) → CLM-009.2;
  - CAP-HARNESS-051 (mutating MCP tools) → CLM-009.10.
- **PARTIAL:**
  - 025 (instruction-root containment helper) → CLM-009.3;
  - 031 (SDK options builder: allowedTools not the boundary) → CLM-009.8;
  - 043 (overlay hard-deny precedence) → CLM-009.7;
  - 047 (pre/post tool hooks) → CLM-009.1;
  - 050 (scaffold_preview classification) → CLM-027;
  - 056 (managed-child path enforcement) → CLM-032.
- **Every claimed capability is labelled `LEGACY-IN-PROCESS`** by the capability worker,
  except 025. This independently confirms the forward pass's main finding: the DEL-06-04
  gate is reached only through the retained Claude SDK path.

## 2. Forward-row errors exposed

No forward disposition is shown to be wrong. Two observations:

- **CAP-HARNESS-004 (answering approval requests).** This is the live, Codex-path
  surface that forward rows CLM-009.1/.7/.12 describe as the substitute gate. It is
  NOT_MINE because it is owned by DEL-06-01 approval mediation. The reverse pass therefore
  finds **no live-path capability owned by DEL-06-04**, which is consistent with the
  forward rows' IMPLEMENTED_DIFFERENTLY and R4.
- **Forward CLM-009.10 cited the post-release application-tool surface.** Its
  ImplementationEvidence rests partly on this surface
  (`codex-supervisor.ts:655` "Chirality registers no dynamic tools"). The Runtime surface
  for application-owned dynamic tools was added post-v3.0.1. So the App *can now* bind
  write-capable application tools to Codex. None are bound at `00115c719`, so the ALIGNED
  disposition holds at this basis. But a later binding would reopen REQ-010, because
  `application-tools.ts` applies no Chirality path policy. This is a precision note, not
  an error.

## 3. PostReleaseBasis revisit (calibration finding)

**Method.** I read the file lists and hunks of `da95ec194`, `cb08dbe2f`, `9ecbdecdf` and
`ccb95e06a` in the frozen tree, using read-only `git show` (permitted by Agent 0's
clarification).

**What each commit touched:**

| Commit | Files touched in the evidence roots |
|---|---|
| `da95ec194` | Runtime `codex-supervisor.ts` (application-tool dispatch, `handleApplicationTool`), `application-tools.ts`, `runtime-daemon.ts`, `app-owned-composition.ts`, `session-store.ts`, client and contracts |
| `cb08dbe2f` | `codex-supervisor.ts` (dynamic-tool cancellation) |
| `9ecbdecdf` | only `projects/chirality-runtime/execution/**` (out of bounds; not read) |
| `ccb95e06a` | only an Electron plan-export IPC contract and export files |

**What the forward rows relied on:**

- **Pre-dates all four commits.** The `sandboxPolicy` mapping (`writableRoots [cwd]`), the
  approval-request handling, `approvalDecision` and `cancelOutcome` in
  `codex-supervisor.ts`. Those hunks do not change them.
- **Not touched by `da95ec194`.** The `allowedWriteTargets` storage in `session-store.ts`.

**Rows that should have been `PostReleaseBasis = YES`: 1**

- **DEL-06-04#CLM-009.10.** Its evidence that the Codex path exposes no Chirality write
  tools relies on the application-tool surface added by `da95ec194` and `cb08dbe2f`.
  - Before those commits, dynamic tool requests were rejected by
    `handleServerRequest`, so the conclusion would have been the same.
  - The cited evidence, however, is post-release.

No other row changes. The forward NO values were correct by outcome, but they were set by
assumption. The calibration input: workers need either read-only git access or a
manager-supplied touched-path list.
