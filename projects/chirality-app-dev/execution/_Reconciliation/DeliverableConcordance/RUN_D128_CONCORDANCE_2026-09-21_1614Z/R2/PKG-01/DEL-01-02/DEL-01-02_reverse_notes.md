# DEL-01-02 — reverse pass notes (RUN_D128, R2, PKG-01)

- **Scope.** One reverse file for the whole deliverable, answered against the merged sealed ledger
  `DEL-01-02_claims.csv` (131 rows, SHA-256 `59ad30af…2cb2bad`, unchanged).
- **Capability files**, concatenated in the order given: BUILD, ELECTRON, HARNESS, ROUTES, RTCONTRACT, RTCORE,
  SETTINGS, SHELL, WORKSPACE (409 capabilities).
- **Frozen reads.** I confirmed the following in the frozen tree:
  - `runtime-service.ts:664-670`;
  - `app-owned-composition.ts:226`, where RuntimeService is constructed without an Agent1RunPort.

## Responses

| Response | Count |
|---|---:|
| CLAIMED_BY | 0 |
| PARTIAL | 68 |
| NOT_MINE | 341 |

- **Why there is no CLAIMED_BY.** DEL-01-02 is a register. It maps boundaries to enforcement surfaces but owns no
  implementation, so a capability is at most PARTIAL to the boundary row that names or bears on it.
- **Where PARTIAL rows point:**
  - CLM-006.3 (permission/approvals) 13;
  - CLM-006.5 (lifecycle) 7;
  - CLM-006.4 (filesystem) 5;
  - CLM-006.8 (subagents) 5;
  - CLM-018.5 (event separation / R4-Q5) 5;
  - CLM-018.6 4;
  - CLM-006.1, CLM-006.7, CLM-006.10, CLM-006.12, CLM-013 and STATE-1 3 each;
  - the rest 1 or 2 each.
- **S2 rows.** No S2 row (CLM-024..060) was the best owner for any capability. S2's governance rows restate the
  S1 boundary rows.

## Errata

17 rows across 10 claims. Every row is a REACH or symbol-level correction taken from the capability Notes and
re-checked in the frozen tree.

| ClaimKey | Fields | Correction | Source |
|---|---|---|---|
| CLM-006.1, CLM-006.13 | ImplementationEvidence | `engine-conformance.ts` LIVE → TEST_ONLY | CAP-RTCONTRACT-039 |
| CLM-006.8, CLM-018.16 (SEE pair) | ImplementationEvidence, Disposition, HumanDecisionNeeded | See below | CAP-RTCORE-024, CAP-RTCONTRACT-048 |
| CLM-006.10 | ImplementationEvidence | `tool-descriptor.ts` LIVE → LEGACY_ONLY | CAP-RTCONTRACT-042 |
| CLM-006.12, CLM-018.19 | ImplementationEvidence | `redactJsonLike` (:95) LIVE → LEGACY_ONLY; `redactConfiguredApiKeys` stays LIVE (labels only) | CAP-HARNESS-027 |
| CLM-006.6, CLM-018.7, CLM-011.1 | ImplementationEvidence; for CLM-011.1 also RemainingWork and Notes | `FileSessionManager` LIVE → LEGACY_ONLY. CLM-011.1 now reads "all 13" evidence modules legacy-only, not "12 of 13". | CAP-HARNESS-037 |
| STATE-2 | ImplementationEvidence | harness-contract shim LIVE → TEST_ONLY. Its sole importer is a test. This agrees with S2's CLM-051/CLM-059.2. | CAP-SETTINGS-042 |

**CLM-006.8 and CLM-018.16 in detail:**
- The sealed rows cited `agent1-run-coordinator.ts:137-140` as LIVE partial subagent governance.
- In fact the runs route is disabled: no Agent1RunPort is composed, and `runAgent1` throws
  REQUIRED_DELEGATION_MISSING.
- The live mechanism is Codex-native descendants under the user-chosen policy (K-UNTYPED-1). The gates are met only
  by LEGACY_ONLY `subagent-governance.ts`.
- Proposed values: REACH TEST_ONLY; Disposition PARTIALLY_IMPLEMENTED → IMPLEMENTED_DIFFERENTLY; HumanDecisionNeeded
  NO → R4-Q1 (subject test, rule 3).
- The erratum changes both rows together, so the SEE pair still carries matching Dispositions.

### Sealed vs errata-applied census (merged ledger, 131 rows)

| Disposition | Sealed | Errata-applied |
|---|---:|---:|
| STALE_SPECIFICATION | 33 | 33 |
| NOT_AUDITABLE | 25 | 25 |
| ALIGNED | 23 | 23 |
| PARTIALLY_IMPLEMENTED | 23 | 21 |
| IMPLEMENTED_DIFFERENTLY | 12 | 14 |
| AUTHORITY_CONFLICT | 7 | 7 |
| REMAINING_STATE_MISMATCH | 5 | 5 |
| DOCUMENTED_UNIMPLEMENTED | 2 | 2 |
| STALE_VERIFICATION | 1 | 1 |

HumanDecisionNeeded: NO 96 → 94; R4-Q1 26 → 28. The other values are unchanged.

## REACH disagreements

These are cases where capability Notes (symbol level) differ from REACHABILITY.csv (module level) or from a ledger
tag.

- **Filed as errata** (all in the table above):
  - `engine-conformance.ts`, `tool-descriptor.ts` and `agent1-run-coordinator.ts`: the pack marks each LIVE only
    through a barrel;
  - `session-manager.ts` `FileSessionManager`: the module is LIVE only through `assertProjectRootAccessible`;
  - `run-logger.ts` `redactJsonLike`;
  - the harness-contract shim.
- **Noted, no erratum:**
  - CAP-RTCONTRACT-036 marks `agent-engine-port.ts` TYPE-ONLY for live consumers. The ledger's REACH=LIVE on the port
    stays correct: the live Codex adapter implements it.
  - CAP-RTCONTRACT-022 marks `event-schema.ts` TYPE-ONLY live.
- **Pack vs reality (S2 rows, no erratum filed).** The pack's LIVE tag on `engine-claude`-adjacent barrels, and
  S2's `app-owned-composition.ts` citations, agree with the capability files.

## Observations that support sealed verdicts (no erratum)

- **Human-gate rows stay ALIGNED at MEDIUM** (CLM-006.5 / 006.9 / 018.17). CAP-SETTINGS-025 and CAP-WORKSPACE-026
  show the transition route is served, but its only renderer caller (`pipeline-surface.tsx`) is not rendered. The
  gate is enforced wherever the API is called; there is simply no live UI to call it.
- **Redaction (CLM-006.12, CLM-018.19).** CAP-HARNESS-027 and CAP-HARNESS-036 show no key source is populated in the
  renderer, so live redaction has nothing to redact. This supports the CREDENTIAL_CUSTODY cause: Codex custodies the
  credentials.
- **Bash posture (CLM-013, CLM-023.1).** CAP-SHELL-025 shows `DEFAULT_OPERATOR_MODE` is `workspaceWrite`
  (`chat-panel.tsx:136`). That maps to approvalPolicy `never` with a workspace-write sandbox, so by default shell runs
  without approval on the live path. This strengthens IMPLEMENTED_DIFFERENTLY + R4-Q1.
- **Claude path not shipped (CLM-006.7, STATE-1 AUTHORITY_CONFLICT).**
  - CAP-BUILD-015 verifies that app.asar carries no Claude SDK or Pi packages.
  - CAP-RTCORE-003 registers Codex as the only engine.
  - The settings answer on the live path is CAP-RTCORE-005: the effective Codex home symlinks the user's `~/.codex`
    configuration.

## Coverage gaps (live controls with no DEL-01-02 row)

- **Codex approval policy and sandbox selection** (CAP-RTCONTRACT-019, CAP-SHELL-025). This is the primary live
  permission, filesystem and shell control. No SoW taxonomy row names it as an enforcement surface; register
  RB-ROLE-MODEL mentions it only as recorded policy.
- **Effective Codex home configuration sharing** (CAP-RTCORE-005). This is a live settings-source boundary, and it
  inverts RB-SETTINGS. There is no row.
- **Renderer hardening, egress allowlist, IPC sender-origin checks and CSP** (CAP-ELECTRON-014/016/018/020). These
  are P0-style safety boundaries with no reliance-register row. Ownership probably sits with PKG-09 or DEL-09-06.
- **Packaged dependency boundary and Codex pin/signature verification** (CAP-BUILD-011/012/015/017). There is no
  RB-FALLBACK or engine-identity row for the packaged supply boundary.
- **Application-owned dynamic tools** (CAP-RTCORE-033). These are registered only for the owning application client,
  and no App code registers any tools. They are a live tool-surface control with no register row.
- **Reference hash warnings** (CAP-WORKSPACE-017). A live App surface already detects `_REFERENCES.md` drift, but
  the deliverable's RBR-021/022 do not cite it.
