# DEL-08-04 — reverse-pass notes

Capability file: `R0_CALIBRATION/SURFACES/HARNESS_capabilities.csv` (60 rows).

| Response | Rows |
|---|---:|
| CLAIMED_BY | 2 |
| PARTIAL | 5 |
| NOT_MINE | 53 |

The sealed forward ledger (`DEL-08-04_claims.csv`, sha256 `243730d8…fdc8`) was not modified.

## 1. Forward-row errors exposed

**Effect on dispositions: none.** The capability file confirms the forward pass's main finding independently. Each DEL-08-04-related capability (CAP-HARNESS-019, 041, 046, 047, 056–060) is tagged `LEGACY-IN-PROCESS: no production importer outside lib/harness; reachable only from scripts/ or tests`. That matches SEC-1.1 and CLM-003.1. CAP-HARNESS-056 also names `NATIVE_DELEGATION` as a candidate CauseTag, consistent with the forward rows.

**Minor evidence omissions.** These do not change any disposition:

- **Missing test file.** `frontend/src/__tests__/lib/coordination-tools.test.ts` (listed for CAP-HARNESS-056/057) is a covering test for the coordination-tool registration. It should have been cited in the VerificationEvidence of CLM-005.1 and CLM-014.
- **Unclaimed capabilities.** No forward row claims the coordination notice/update/acknowledgment tools (CAP-HARNESS-057). I answered NOT_MINE and routed them to DEL-08-05 (K-SUBAGENT-3 evidence).
  - Alternative reading: they live in `managed-delegation.ts` and belong to the SCA-APP-008 "multi-child managed execution" carrier. On that reading CLM-016.2 would be a PARTIAL owner. The verifier may want to adjudicate.
- **Capability description.** CAP-HARNESS-058 calls the bridge an "executable subagent bridge (D-APP-10 Option C)". At `00115c719` that bridge is disabled (`subagent-bridge.ts:5-9`, policy `subagent-bridge.v4.disabled-after-managed-delegation`). This is a capability-description issue, not a forward-row error.

**Not in the HARNESS area.** Several claimed behaviors are outside this area:

- Runtime native-role configuration;
- role-policy labels;
- App consent-settings labels (SEC-1.2, SEC-1.3, CLM-016.3, CLM-016.5).

No reverse row could confirm or contradict them.

## 2. PostReleaseBasis revisit (calibration finding)

**Method.** Read-only `git -C <frozen tree> show --stat` on the four post-v3.0.1 commits:

- **`da95ec194`:** Runtime application dynamic tools. Touches `contracts/application-tools.ts`, `daemon/application-tools.ts`, `daemon/codex-supervisor.ts`, `runtime-daemon.ts`, `session-store.ts`, `client.ts` and three tests.
- **`cb08dbe2f`:** `daemon/codex-supervisor.ts` plus a test.
- **`9ecbdecdf`:** evidence files only.
- **`ccb95e06a`:** export manifest, plus a single-line change to `frontend/electron/plan-export-ipc-contract.ts`.

**Evidence the forward ledger relied on:**

- `frontend/src/lib/harness/{managed-delegation,subagent-governance,subagent-bridge,agent-runtime-contract,turn-engine}.ts` and their tests;
- `frontend/src/lib/consent/hosted-engine-consent-port.ts` and `components/settings/account-consent-settings.tsx`;
- `frontend/src/lib/shell/harness-event-views.ts`;
- `frontend/src/app/api/harness/turn/route.ts`;
- Runtime `core/src/{role-policy,native-role-config,delegated-runtime,agent1-run-coordinator,runtime-service}.ts` and the tests `role-policy`, `native-role-config` and `stagec-native-child-history`.

**Result.** None of the four commits touches any file the forward ledger relied on, so **0 rows would change**. The `NO` values set by assumption in the forward pass turn out to be correct for all 80 rows.
