# DEL-04-01 — reverse-pass notes (RUN_D128, R2, PKG-04)

- **Sealed ledger:** `DEL-04-01_claims.csv`, SHA-256
  `f74e258973e139d053fb1c9ba5ad490f2bb3f85ca1f00edec7c7c01a9512808b`. I recomputed it after the
  reverse pass and it is unchanged.
- **Capability input:** `_reverse_inputs/DEL-04-01_capabilities.csv` (SHA-256 `5fdf52ea…`),
  291 rows across the six areas BUILD, HARNESS, RTCONTRACT, RTCORE, SETTINGS and SHELL.

## Responses

| Response | Rows |
|---|---:|
| CLAIMED_BY | 3 |
| PARTIAL | 12 |
| NOT_MINE | 276 |

**CLAIMED_BY (3).** The three are the probe tooling that produced this deliverable's D-APP-52
evidence:

- CAP-BUILD-031: the packaged-SDK proof (→ CLM-013.8);
- CAP-BUILD-032: the live packaged read-tool proof (→ CLM-010.11);
- CAP-BUILD-041: the live SDK probe (→ CLM-010.3).

All three are `REACH=LEGACY_ONLY`. Two are `STATE=DISABLED` under the A2 packaged boundary. The
third, the live SDK probe, is manual and needs a live key.

**PARTIAL (12).** Each of these is an implementation or live-path fact that a probe requirement or
a state row covers only in part:

- the SDK adapter, mapper and permission overlay: CLM-004.1, CLM-010.3, CLM-010.6;
- redaction: CLM-010.12;
- the SDK version pins: CLM-010.2 (package.json pin, and the `CLAUDE_AGENT_SDK_PACKAGE_VERSION`
  constant);
- AgentEnginePort: CLM-024;
- engine-claude: STATE-2;
- Codex as the sole engine: CLM-003;
- the Codex app-server host, the pinned `codex --version` gate and the Codex pin verifier:
  STATE-1 (the SOW-079 App Server observation).

**NOT_MINE (276).** DEL-04-01 is a documentary probe and decision slice, and it excludes
implementation (CLM-009). For each NOT_MINE row I named the evident owner where there is one:

- PKG-09 for packaging and release tooling;
- downstream PKG-04 deliverables for the adapter, provider selection and the key bridge;
- PKG-06 for tools, MCP and hooks;
- PKG-02/07 for the shell and settings UI;
- Runtime-facing deliverables for Runtime core and contracts.

## Errata

**None.** I checked every REACH tag in the sealed ledger against the capability files:

- `claude-agent-sdk-manager`, `sdk-options-builder`, `sdk-message-mapper`, `permission-overlay`,
  `mcp/read-tools` and `chirality-hooks` are LEGACY_ONLY (CAP-HARNESS-031/032/043/050/047);
- `run-logger.ts` is LIVE (CAP-HARNESS-027);
- `agent-engine-port.ts` is LIVE, type-only (CAP-RTCONTRACT-036);
- `codex-app-server-client.ts` is LIVE (CAP-RTCORE-004);
- `engine-claude` is LEGACY_ONLY and unreached (CAP-RTCONTRACT-053).

No tag is contradicted. None of the tags I used depends on a barrel re-export: agent-engine-port
is consumed directly by the Runtime core delegated engine adapter (type-only).

**Census:** the sealed figures and the errata-applied figures are identical. Dispositions are
ALIGNED 35, REMAINING_STATE_MISMATCH 12, STALE_SPECIFICATION 6, PARTIALLY_IMPLEMENTED 6,
NOT_AUDITABLE 4, AUTHORITY_CONFLICT 1, over 64 rows.

## Coverage gaps (no forward row; not expressible as errata)

- **Codex pin and host observation.** The live Codex pin and host (CAP-BUILD-012, CAP-RTCORE-002,
  CAP-RTCORE-004) have no DEL-04-01 requirement row. The forward ledger covers them only as a
  missing-carrier state (STATE-1), because the SoW never seated SOW-079. I don't consider this a
  worker gap: the unit does not exist in the SoW. It is flagged for the manager because it is the
  deliverable's live-path obligation under the current decomposition.
- **SDK version constant.** CAP-RTCONTRACT-045 (`CLAUDE_AGENT_SDK_PACKAGE_VERSION`) is inside the
  subject of REQ-002 but was not cited in the forward row. The disposition would not change.

## Capability-file observations

- **CAP-BUILD-031** records `STATE=DISABLED` because the release workflow blocks before the step
  and the A2 boundary forbids the SDK in `app.asar`. This agrees with the ledger's reading of
  REQ-011 and VER-008 as historical proofs.
- **CAP-HARNESS-027:** live redaction runs, but no key source is populated in the renderer. This
  supports keeping CLM-010.12 at module level.
- **CAP-HARNESS-018** refers to legacy adapters needing "provider session evidence". This is not
  owned here and is noted only for consistency with CLM-010.8.
- I found no REACH or STATE tag contradicted by code in the rows I relied on.

## Effort

- One read of the brief and the areas file.
- The capability listing: 291 rows, read in full at summary width, with 15 rows read in full.
- No new frozen-tree reads were needed; the evidence came from the forward pass.
- The context budget was adequate.
