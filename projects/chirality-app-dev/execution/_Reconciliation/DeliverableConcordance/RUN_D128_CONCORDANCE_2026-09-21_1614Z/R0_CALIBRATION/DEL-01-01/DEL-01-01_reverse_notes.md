# DEL-01-01 — reverse-pass notes (RUN_D128 R0 calibration, unit F-01)

- **Forward ledger:** sealed at SHA-256 `6035419f6ccc58e43f49356b21d214e818b3e189fa05cd9d62e3e8dbe0976947`, not modified.
- **Capability file:** `R0_CALIBRATION/SURFACES/HARNESS_capabilities.csv`, 60 rows.
- **Responses:** 2 PARTIAL, 58 NOT_MINE, 0 CLAIMED_BY.

DEL-01-01 is a governance DOC_UPDATE deliverable, so it owns no HARNESS implementation capability. The two PARTIAL rows are enforcement surfaces for boundaries it states:

- **CAP-HARNESS-038** (legacy project-local `events.jsonl` writer) maps to CLM-009.11.
- **CAP-HARNESS-051** (MCP `status_transition`) maps to CLM-009.2.

## Forward-row error exposed by the reverse pass

**Affected rows:**

- CLM-009.2 (REQ-002 human-only gates);
- CLM-004.1 (human-authority condition);
- CLM-004.5 (lifecycle condition).

All three are ALIGNED/HIGH. Their evidence was only `frontend/src/lib/lifecycle/transition.ts` and its tests.

**What the forward pass missed.** CAP-HARNESS-051 shows a second entry to the same lifecycle engine: the agent-callable MCP tool `status_transition`, in `projects/chirality-app-dev/frontend/src/lib/harness/mcp/read-tools.ts` (around lines 925-944 and 1125-1136).

- The tool takes `actor` as a free string supplied by the calling agent.
- `normalizeActor` in `transition.ts` maps `HUMAN`, `USER` or `OPERATOR` to HUMAN.
- The approval-SHA check tests only the format (7-64 hex characters).
- So an agent session running in `workspaceWrite` mode with the tool requested can move a deliverable to CHECKING or ISSUED by declaring itself HUMAN.
- The frontend test `src/__tests__/lib/chirality-mutating-mcp.test.ts` 'allows HUMAN approvalSha transitions through the lifecycle engine' shows exactly this path. It is covered by `GATE-TRANSCRIPT(APP@00115c719)`.

**What limits it.** `src/__tests__/lib/sdk-options-builder.test.ts` shows the tool is disallowed by default and attached only when requested in `workspaceWrite`. It also sits on the legacy Claude-SDK harness path, not the Codex sole-engine path.

**Suggested correction, for the verifier or manager:**

- CLM-009.2 and CLM-004.1 are better read as PARTIALLY_IMPLEMENTED, or at least ALIGNED/MEDIUM with this caveat.
- Human-only authority is enforced as a declared-actor check, not as a verified human identity. That falls short of CONTRACT K-AUTH-1 and K-RELIANCE-2 as P0 boundaries.
- CauseTag: `UNRECORDED_JUDGMENT`, since no direction record explaining the self-declared actor was found. `PRE_V3_DRIFT` is also plausible, because the tool predates v3.
- CLM-004.5 is less affected; its statement concerns `_STATUS.md` canonicality.

## PostReleaseBasis revisit (calibration finding)

**Method.** I read the four post-v3.0.1 commits with `git -C <frozen tree> show --name-only` and `show <commit> -- <file>`.

- **One method departure to report:** I also ran one read-only `git blame` over the cited line ranges of `session-store.ts`. That goes beyond the log/show allowance.

**What the four commits touched:**

| Commit | Date | Summary | Touches cited files? |
|---|---|---|---|
| `da95ec194` | 2026-09-19 | application-owned dynamic tools | Yes: `session-store.ts` and `codex-supervisor.ts` |
| `cb08dbe2f` | 2026-09-19 | dynamic tool cancellation | Yes: `codex-supervisor.ts` |
| `9ecbdecdf` | 2026-09-20 | desktop Codex MCP V2 observation | No cited file |
| `ccb95e06a` | 2026-09-20 | public export fix | No cited file |

None of the four touches the App governing docs, `AUTHORITY_CORPUS.json`, the deliverable folder, `transition.ts`, the reliance register or the cited tests.

**Assessment:**

- **`session-store.ts`.** `da95ec194` added about 31-33 lines of application-tool catalog code near line 125. The content relied on predates the post-v3.0.1 commits (blame: `8b3643e6c`, 2026-07-22):
  - `sessionsDirectory`, `eventsFile`;
  - the legacy `events.jsonl` copy.

  The line numbers cited in the forward ledger (`:1113`, `:1125`, `:969-974`) are numbered after this commit's shift. The substance does not rely on it.
- **`codex-supervisor.ts`.** Rows CLM-009.7, CLM-023 and STATE-1 cite it only to show a stock Codex App Server child exists, which predates both commits.

**Result: 0 rows would change to `PostReleaseBasis = YES`.**

**Method note for the gate:** line-number citations can shift because of post-release commits even when the relied-upon content does not. Consider whether PostReleaseBasis should also flag these "line anchors shifted" cases (7 forward rows cite `session-store.ts` line numbers).
