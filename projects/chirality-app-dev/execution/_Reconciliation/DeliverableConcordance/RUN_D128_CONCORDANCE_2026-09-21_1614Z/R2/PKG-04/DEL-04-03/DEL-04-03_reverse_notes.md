# DEL-04-03 — reverse-pass notes (RUN_D128, R2, PKG-04)

## Hashes and validation

| File | SHA-256 |
|---|---|
| `DEL-04-03_claims.csv` (sealed, re-hashed after this pass, unchanged) | `09cd5f5799b97d43a9e52489cf026b0f1e47dc66a0e68ed3eb62506ce728c605` |
| `DEL-04-03_reverse.csv` | `1035e27fbb3b81b20ff17a4067c27327cc92e3af5d897fd2152d5b88cb1db688` |
| `DEL-04-03_errata.csv` | `2388947499b1003f0750251de8719ed093c3149ab0f82677a4683ba87a84d493` |

- **Areas:** BUILD, ELECTRON, HARNESS, ROUTES, RTCONTRACT, RTCORE and WORKSPACE. The capabilities come from the concatenated manager input `_reverse_inputs/DEL-04-03_capabilities.csv` (322 rows).
- **Validators:** `reverse` and `errata` both report `RESULT PASS errors=0 warnings=0`.

## Response counts

322 capability rows were answered: 1 CLAIMED_BY, 12 PARTIAL and 309 NOT_MINE.

**CLAIMED_BY (1):** CAP-HARNESS-032 (the SDK message mapper) → CLM-005.

**PARTIAL (12):**

| Capability | Ledger row | What the row covers |
|---|---|---|
| CAP-HARNESS-048 | CLM-009.9 | the tool evidence used by the mapper |
| CAP-HARNESS-034 | STATE-2 | Pi event mapping, which `_STATUS` records as completed here |
| CAP-HARNESS-027 | CLM-009.12 | redaction |
| CAP-HARNESS-024 | CLM-004.1 | the SSE proxy |
| CAP-ROUTES-007 | CLM-004.1 | the turn route |
| CAP-RTCORE-025 | CLM-004.2 | the live Codex adapter |
| CAP-RTCORE-029 | CLM-004.5 | notification pass-through |
| CAP-RTCONTRACT-022 | CLM-009.5 | the HarnessEvent envelope |
| CAP-RTCONTRACT-023 | CLM-004.3 | the UIEvent type |
| CAP-RTCONTRACT-036 | CLM-009.4 | the public UI event names |
| CAP-RTCONTRACT-039 | CLM-004.6 | the conformance suite |
| CAP-BUILD-027 | CLM-010 | the section 9 check |

**NOT_MINE (309):** mostly whole areas the mapper does not touch: BUILD, ELECTRON, WORKSPACE, most of ROUTES, RTCORE and RTCONTRACT, and the non-mapping parts of HARNESS.

## Errata (1 row key, 2 fields)

The corrections are to `DEL-04-03#CLM-004.5` (redaction of runtime event data and logs):
- `ImplementationEvidence`: add `runtime-daemon.ts:65-88`. The daemon host logger emits only a bounded, control-character-free projection of fields, and its interface contract excludes bearers, proofs and other secrets. `REACH=LIVE`.
- `Disposition`: DOCUMENTED_UNIMPLEMENTED → PARTIALLY_IMPLEMENTED.

The capability row CAP-RTCORE-013 led me to this evidence. The forward search missed it because it grepped for `redact|scrub|sanitiz|mask`, and the logger uses different words.

- The clause covers both runtime logs and event data.
- Logs now have a live mechanism that keeps secrets out.
- Event data is still forwarded unredacted (CAP-RTCORE-029).
- The cited lines blame to `d29f78d95` and `eff0c9bda`, so PostReleaseBasis stays NO.

**REACH tags re-checked at symbol level against the capability notes:** no errata were needed.

| Symbol | Capability row | Forward tag | Result |
|---|---|---|---|
| `event-schema.ts` HarnessEvent | CAP-RTCONTRACT-022 | LIVE TYPE-ONLY | confirmed |
| `types.ts` UIEvent | CAP-RTCONTRACT-023 | LIVE TYPE-ONLY | confirmed |
| `engine-conformance.ts` runEngineConformance | CAP-RTCONTRACT-039 | TEST_ONLY | confirmed |
| section 9 manifest | CAP-BUILD-027 | TEST_ONLY | confirmed |
| mapper, harness-ui-bridge, tool-evidence | CAP-HARNESS-032/039/048 | LEGACY_ONLY | confirmed |
| delegated adapter | CAP-RTCORE-025 | LIVE | confirmed |

### Census: sealed vs errata-applied

| Disposition | Sealed | Errata-applied |
|---|---|---|
| ALIGNED | 16 | 16 |
| STALE_SPECIFICATION | 14 | 14 |
| PARTIALLY_IMPLEMENTED | 12 | 13 |
| NOT_AUDITABLE | 8 | 8 |
| DOCUMENTED_UNIMPLEMENTED | 2 | 1 |
| REMAINING_STATE_MISMATCH | 2 | 2 |
| LIFECYCLE_REASSESSMENT_REQUIRED | 1 | 1 |
| **Total** | 55 | 55 |

## Coverage gaps (cannot be expressed as errata)

1. **Pi event translation.** `_STATUS.md` History records two things:
   - 2026-07-21: SCA-APP-002 added Pi event translation to DEL-04-03's Remaining.
   - 2026-07-22: under D-APP-72, the independent Pi event mapping was completed and conformance-tested (`frontend/src/lib/harness/pi-event-mapper.ts`, REACH=LEGACY_ONLY; the Runtime copy is at `engine-pi-omlx/src/pi-event-mapper.ts`, REACH=TEST_ONLY).

   No forward row dispositions this delivered work. STATE-2 only mentions it in its evidence, and the SoW has no Pi clause. The manager should consider adding a run-local STATE row to DEL-04-03. It would most likely be ALIGNED or IMPLEMENTED_UNDOCUMENTED at module level: the work was delivered but the SoW does not specify it. It may also turn on R4-Q1 (whether the retained Pi path is history, compatibility or obligation).
2. **No other gaps.** No other capability looked owned by DEL-04-03 but uncovered.

## Capabilities that look owned elsewhere

| Capability | Likely owner |
|---|---|
| CAP-HARNESS-031 (Claude SDK adapter, options and prompts) | DEL-04-02 / DEL-04-04 |
| CAP-HARNESS-038 (events.jsonl) and CAP-RTCORE-017 (event journal) | PKG-05 (DEP-04-03-010 handoff) |
| CAP-HARNESS-039 (harness-to-UI bridge), CAP-HARNESS-024 and CAP-ROUTES-007 (SSE and route) | DEL-03-03 |
| CAP-RTCORE-020 (turn coordination and terminal persistence) | DEL-03-02 / TurnEngine; REQ013 excludes it |
| CAP-RTCONTRACT-036 and 039 (port and conformance suite) | DEL-03-01 |
| CAP-RTCORE-025 and 029 (the live Codex translation) | Runtime-owned under SCA-APP-005 and D-GOV-43 |

**Ownership gap on the live path.** No App deliverable visibly owns "App UI-event mapping for Codex" on the live path. SCA-APP-005 moved DEL-04-03 to that App-client role, but the live translation lives entirely in Runtime core. This is relevant to the CLM-008 and STATE-1 findings.

## Capability-file accuracy observations

- **CAP-RTCORE-013** says "redacted diagnostic fields". The mechanism is actually bounded field projection plus a contract that excludes secrets (`safeDiagnosticText`), not pattern redaction. The substance is accurate but the wording could mislead.
- **CAP-HARNESS-027** notes that live `redactConfiguredApiKeys` has no populated key source. This supports the CREDENTIAL_CUSTODY alternative reading of CLM-004.5.

## Effort

- I read the capability file in full (as a compact listing) and 17 rows in detail.
- I made two targeted reads of the frozen tree: `runtime-daemon.ts:65-88` and its blame.
- The context budget was comfortable.
