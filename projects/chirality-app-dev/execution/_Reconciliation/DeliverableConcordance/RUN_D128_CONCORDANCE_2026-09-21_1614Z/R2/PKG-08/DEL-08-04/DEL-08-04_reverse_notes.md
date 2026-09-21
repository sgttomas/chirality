# DEL-08-04 reverse notes (RUN_D128, R2 PKG-08)

- **Input:** 320 capability rows in `REVERSE_INPUT_capabilities.csv`, concatenated from seven areas: BUILD, ELECTRON, HARNESS, RTCONTRACT, RTCORE, SETTINGS, WORKSPACE. I read the area files and the relevant `<AREA>_notes.md` sections.
- **Sealed ledger:** unchanged. SHA-256 `9f0081348675b4f1c8aa13b2556aec335c6d3f2cd0b1d1c8ce91af6e45211267`, re-checked after the reverse pass.

## Responses

The file has 320 responses:

- **CLAIMED_BY (5):**
  - HARNESS-056 → CLM-003.2
  - HARNESS-058 → CLM-010.1
  - RTCORE-042 → CLM-016.2
  - RTCORE-043 → SEC-2.3
  - SETTINGS-017 → SEC-2.3
- **PARTIAL (18):** the legacy harness pieces that carry admission or bridge-fence behaviour, and the Runtime live-path analogues:
  - Agent 1 runs and the Agent 2 direct-entry refusal;
  - the route label, the supervisor's native descendant tracking, the fixed delegation-policy string;
  - the governed-workflow policy vocabulary.
- **NOT_MINE (297):** build, Electron, generic harness/Runtime, account and consent, and workspace behaviours.

## Errata (19 rows; validator PASS)

Rows by Field: ImplementationEvidence 9, Notes 2, Disposition 2, CauseTag 2, DirectionEvidence 2, RemainingWork 2.

1. **Native-role configuration evidence** (ImplementationEvidence on SEC-1, SEC-2.1, CLM-003.2, CLM-033, CLM-010.2, CLM-016.2, CLM-016.3, CLM-016.7, REM-2; Notes on CLM-003.2, CLM-010.1).
   - The forward pass cited `native-role-config.ts:141-143` (maxDepth 2 pins) as REACH=LIVE, following the pack's static map. But `loadTrustedNativeRoleConfiguration` and `codexNativeRoleConfigOverrides` have no product caller; only the core `index.ts` re-export reaches them.
   - The live path supplies native roles through `product-native-role-config.ts:33-34`, imported at `delegated-engine-adapter.ts:20` (CAP-RTCORE-042).
   - For CLM-016.2, `descendant-tracker.ts` is also re-tagged TEST_ONLY (CAP-RTCORE-047).
   - No Disposition changes. The live path still uses Codex-native descent. The claim that the product pins `maxDepth 2` is withdrawn; the actual depth is Codex's own `[agents]` behaviour.
2. **SEC-2.3 and its SEE row CLM-016.4:** ALIGNED → PARTIALLY_IMPLEMENTED; CauseTag CREDENTIAL_CUSTODY; DirectionEvidence `GOV:D-APP-127`.
   - The UI labels in `account-consent-settings.tsx` and `hosted-engine-consent-port.ts` are statically LIVE, but the panel is never rendered. `shell-frame.tsx:377` supplies a null consent port, and `settings-view.tsx:31-32` shows it only when the hosted controller is absent, which never happens (L404).
   - The labels therefore exist only in Runtime role evidence (`role-policy.ts:33-34`).
   - Role entry is live through Runtime roles. Agent 2 direct entry is refused (`runtime-service.ts:223`).

**Errata-applied census:**

| Disposition | Sealed | Errata-applied |
|---|---|---|
| ALIGNED | 11 | 9 |
| PARTIALLY_IMPLEMENTED | 10 | 12 |

Every other count is unchanged. SEE rows stay at 14, and the SEC-2.3 / CLM-016.4 pair keeps the same Disposition.

## Coverage gaps and explanations (no forward row exists)

- **CAP-HARNESS-019 / CAP-WORKSPACE-006:** the live Toolkit still collects `contextSealed`, `pipelineRunApproved` and `approvalRef`, and attaches them as `opts.subagentGovernance` to every turn request (`toolkit.ts:150-160`; `chat-panel.tsx` reads `optsPayload`).
  - Only the LEGACY_ONLY gate consumes these inputs, so on the live path the UI collects governance inputs that have no effect.
  - The forward ledger has no row for this live-but-inert input surface. A manager may add one, for example a STATE row or a PARTIAL link to CLM-003.2 as given here.
- **CAP-RTCORE-024 / CAP-RTCONTRACT-048:** the RTCORE area classifies `agent1-run-coordinator.ts` as TEST_ONLY, and the runs route as STATE=DISABLED (no Agent1RunPort; `runtime-service.ts:664-670` throws REQUIRED_DELEGATION_MISSING).
  - The forward rows keep REACH=LIVE as the pack's static map gives it, and their Notes already record that nothing outside tests constructs it. No erratum was raised because the static tag follows the rulebook.
  - The disabled route strengthens the PARTIALLY_IMPLEMENTED readings of SEC-1, CLM-016.1 and CLM-016.7.
- **CAP-RTCONTRACT-027:** `DelegatedRoleEvidence` has no consumer outside contracts. The forward CLM-011 cites it only as an analogue, so no change is needed.

## Validators

| Mode | Result |
|---|---|
| reverse | `RULES errors none / warnings none`; `RESULT PASS errors=0 warnings=0` |
| errata | `RULES errors none / warnings none`; `RESULT PASS errors=0 warnings=0` |
