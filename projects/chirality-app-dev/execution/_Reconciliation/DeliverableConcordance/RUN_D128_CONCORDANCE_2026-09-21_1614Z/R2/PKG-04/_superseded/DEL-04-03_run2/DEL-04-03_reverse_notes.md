# DEL-04-03 — reverse-pass notes (R2, PKG-04)

## Inputs and outputs

- **Sealed ledger:** `DEL-04-03_claims.csv`. SHA-256 `f2e6c8475bcc21717d2b8a790a7d41b7ccdef9858a6079b60f8eb9c014b211eb`, unchanged after this pass.
- **Areas:** BUILD 41, ELECTRON 35, HARNESS 60, ROUTES 44, RTCONTRACT 53, RTCORE 50, WORKSPACE 39. Total 322 capabilities, read from the manager's concatenated `_reverse_inputs/DEL-04-03_capabilities.csv`.
- **`DEL-04-03_reverse.csv`:** 322 rows plus `#END`. Validator `RESULT PASS errors=0 warnings=0`.
- **`DEL-04-03_errata.csv`:** 2 rows plus `#END`. Validator `RESULT PASS errors=0 warnings=0`.

## Response counts

| Response | Count |
|---|---|
| CLAIMED_BY | 1 |
| PARTIAL | 9 |
| NOT_MINE | 312 |

**CLAIMED_BY:** CAP-HARNESS-032 → CLM-003.1. This is the SDK message mapper, `sdk-message-mapper.ts`, `REACH=LEGACY_ONLY`.

**PARTIAL (capability → forward row):**
- CAP-HARNESS-027 → CLM-009.12
- CAP-HARNESS-034 → STATE-1
- CAP-ROUTES-007 → CLM-004.1
- CAP-RTCONTRACT-022 → CLM-003.3
- CAP-RTCONTRACT-023 → CLM-003.2
- CAP-RTCONTRACT-036 → CLM-004.2
- CAP-RTCONTRACT-039 → CLM-004.6
- CAP-RTCORE-025 → CLM-004.4
- CAP-RTCORE-029 → CLM-008

The BUILD, ELECTRON and WORKSPACE areas contain no capability this deliverable owns. They were selected through hint-file token noise and through cited paths such as `validate-harness-section9.mjs`.

## Errata

There are 2 rows, both in the `ImplementationEvidence` field: CLM-004.6 and CLM-011.7.

- **What changes:** `engine-conformance.ts:483` was tagged `REACH=LIVE`. The proposed tag is `REACH=TEST_ONLY`.
- **Why:** `REACHABILITY.csv` marks the module LIVE only because the `contracts` barrel re-exports it (known limit 1). CAP-RTCONTRACT-039 tags it TEST_ONLY.
- **Confirmed at the frozen basis:** a grep finds no non-test importer apart from the `contracts/src/harness/index.ts` barrel.
- **No Disposition change.** Both rows stay STALE_SPECIFICATION with R4-Q2. The finding that no Codex conformance run exists is unaffected.

**Census, sealed versus errata-applied:** the two are identical, because neither erratum touches Disposition, CauseTag, Confidence or HumanDecisionNeeded.
- STALE_SPECIFICATION 22
- ALIGNED 19
- PARTIALLY_IMPLEMENTED 10
- NOT_AUDITABLE 7
- IMPLEMENTED_DIFFERENTLY 4
- REMAINING_STATE_MISMATCH 1
- LIFECYCLE_REASSESSMENT_REQUIRED 1

Six rows carry HumanDecisionNeeded other than NO.

## Coverage gaps (missing forward rows; not expressible as errata)

1. **Pi event mapping recorded as delivered under DEL-04-03.**
   - `_STATUS.md` History, 2026-07-22: "D-APP-72 independent Pi event mapping completed and conformance-tested while the Claude mapper remains adapter-specific".
   - `_STATUS.md` History, 2026-07-21: "SCA-APP-002 added Pi event translation to Remaining". That item is no longer in Remaining.
   - The work is `frontend/src/lib/harness/pi-event-mapper.ts` (CAP-HARNESS-034, `REACH=LEGACY_ONLY`). The Runtime has a counterpart, `engine-pi-omlx/src/pi-event-mapper.ts` (CAP-RTCONTRACT-051, `REACH=TEST_ONLY`).
   - No SoW unit describes Pi mapping, and no forward row covers it. The SoW text has no SCA-APP-002 amendment.
   - Suggested manager row: STATE-n or REGISTER-n. The _STATUS records delivered work outside the SoW.
     - Likely Disposition: IMPLEMENTED_UNDOCUMENTED at module level, `REACH=LEGACY_ONLY`.
     - Cause: CODEX_SOLE_ENGINE. Pi/oMLX is compatibility history under the preamble.
     - HumanDecisionNeeded: R4-Q1.
2. **Removal of the SCA-APP-002 Remaining item.** `_STATUS.md` does not record when or why the Pi Remaining item was removed. History only says the Pi work was completed on 2026-07-22.
   - This is a minor carrier gap. It could be folded into the row above.

## Capabilities owned elsewhere

- **DEL-03-03 (SSE/UIEvent compatibility, DEP-04-03-009):** CAP-HARNESS-024 and CAP-HARNESS-002.
- **DEL-03-01 (AgentEnginePort, DEP-04-03-008):** CAP-RTCONTRACT-036.
- **PKG-05 (event log, replay and tool-result records):**
  - CAP-HARNESS-038
  - CAP-HARNESS-048
  - CAP-RTCONTRACT-021
  - CAP-RTCONTRACT-024
  - CAP-RTCORE-017
- **DEL-04-01 / DEL-04-02:** CAP-HARNESS-031, the Claude SDK adapter.
- **Runtime-owned live translation (ownership is R4-Q1):** CAP-RTCORE-025 and CAP-RTCORE-029.

## Capability-file accuracy

- **No contradictions found in the rows inspected.** CAP-HARNESS-032 (LEGACY_ONLY) and CAP-RTCORE-029 (LIVE, unchanged pass-through) agree with the forward-pass code reading.
- **Stale capability text in CAP-HARNESS-032.** Its note says the mapper is "reachable only from scripts/ or tests". Its real importer is `claude-agent-sdk-manager.ts`, which is itself LEGACY_ONLY. The REACH tag is still correct.

## Effort

- **Read:** the brief, the areas file, the 322-row concatenated capability file (all Capability and Paths text, with Notes for about 40 rows), and one frozen-tree grep to confirm the engine-conformance importers.
- **Context budget:** adequate.
