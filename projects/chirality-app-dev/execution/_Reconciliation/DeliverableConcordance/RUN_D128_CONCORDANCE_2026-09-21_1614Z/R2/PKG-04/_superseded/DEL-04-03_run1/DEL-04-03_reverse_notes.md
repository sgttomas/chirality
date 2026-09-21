# DEL-04-03 — reverse-pass notes (RUN_D128, R2, PKG-04)

- **Areas:** BUILD 41, ELECTRON 35, HARNESS 60, ROUTES 44, RTCONTRACT 53, RTCORE 50 and WORKSPACE 39, a total of 322 capability rows.
- **Seal:** the sealed ledger is unchanged, with SHA-256 `1a21af4a1ec27edc89ad3b60c22160cf89041169089325574856f19584d0d745`.
- **Validator:** the reverse file and the errata file each returned `RESULT PASS errors=0 warnings=0`.

## Response counts

| Response | Rows |
|---|---|
| CLAIMED_BY | 1 |
| PARTIAL | 13 |
| NOT_MINE | 308 |

- **CLAIMED_BY:** CAP-HARNESS-032, the retained SDK mapper, maps to CLM-005.
- **PARTIAL, live Codex translation:**
  - CAP-RTCORE-025, the delegated adapter, maps to CLM-008.
  - CAP-RTCORE-029, the Codex notification pass-through, maps to CLM-009.2.
  - CAP-RTCORE-020, which derives the message.delta lane and persists terminal events, maps to CLM-009.6.
- **PARTIAL, contract targets:**
  - CAP-RTCONTRACT-022 (HarnessEvent) maps to CLM-009.5.
  - CAP-RTCONTRACT-023 (UIEvent) maps to CLM-009.4.
  - CAP-RTCONTRACT-036 (AgentEnginePort) maps to CLM-004.2.
  - CAP-RTCONTRACT-039 (conformance) maps to CLM-004.6.
- **PARTIAL, peripheral:**
  - CAP-BUILD-027 (the section9 ID) maps to CLM-010.
  - CAP-HARNESS-027 (redaction) maps to CLM-004.5.
  - CAP-HARNESS-039 (the legacy UI bridge) maps to CLM-005.
  - CAP-ROUTES-007 (the turn route) maps to CLM-004.1.
- **PARTIAL, Pi mapping:** CAP-HARNESS-034 and CAP-RTCONTRACT-051 both map to CLM-008.

## Errata

There are 5 errata rows. No Disposition, CauseTag or HumanDecisionNeeded changes.

- **CLM-004.6, ImplementationEvidence.**
  - Sealed: `engine-conformance.ts` is tagged REACH=LIVE.
  - Correction: REACH=TEST_ONLY. Its only non-test importer is the `contracts/src/harness/index.ts` barrel. This is the module-level-map limit the brief warned about, and CAP-RTCONTRACT-039 agrees.
- **CLM-010 and CLM-012, ImplementationEvidence and Notes (4 rows).**
  - Sealed: `validate-harness-section9.mjs` is tagged REACH=LEGACY_ONLY (UNREACHED).
  - Correction: REACH=TEST_ONLY. The script is reached by `src/__tests__/scripts/validate-harness-section9.test.ts` and the npm script `harness:validate:section9`, and the shared manifest's limit 3 says a test-reached script is not UNREACHED (CAP-BUILD-027).

**Census:** the sealed and errata-applied figures are identical, because no Disposition, CauseTag, Confidence or HumanDecisionNeeded changed. Both are:

- 53 rows;
- STALE_SPECIFICATION 14, ALIGNED 9, IMPLEMENTED_DIFFERENTLY 9, NOT_AUDITABLE 9, PARTIALLY_IMPLEMENTED 6, DOCUMENTED_UNIMPLEMENTED 3, REMAINING_STATE_MISMATCH 3;
- HumanDecisionNeeded R4-Q1 20, R4-Q2 2, NO 31.

## Coverage gaps (missing forward rows; not errata)

- **Pi event mapping.** No forward row covers it, although the `_STATUS.md` History (2026-07-22) records "D-APP-72 independent Pi event mapping completed and conformance-tested" under this deliverable.
  - The code is `frontend/src/lib/harness/pi-event-mapper.ts` (LEGACY_ONLY) and `chirality-runtime/packages/engine-pi-omlx/src/pi-event-mapper.ts` (TEST_ONLY; retained engine, forbidden from the bundles).
  - The missing row would be a STATE row on the `_STATUS.md` History claim: accurate as history, with the code now non-live under the Codex-only basis, citing R4-Q1.
  - For now, CAP-HARNESS-034 and CAP-RTCONTRACT-051 are answered PARTIAL against CLM-008.
- **Live App-side event views.** They are not mapped to this deliverable: CAP-WORKSPACE-004 (the live harness event buffer) and the harness-event views. Those are UI projection (PKG-02/PKG-07), not translation, so I do not count this as a gap.

## Capabilities likely owned elsewhere

- **The Runtime event journal and replay** (CAP-RTCORE-017) and the legacy `session-events.ts`/`event-factory.ts` (CAP-HARNESS-038) belong to PKG-05, likely DEL-05-02.
- **The SSE proxy and turn route** (CAP-HARNESS-024 and CAP-ROUTES-007) belong to DEL-03-03.
- **The AgentEnginePort and conformance harness** (CAP-RTCONTRACT-036 and CAP-RTCONTRACT-039) belong to DEL-03-01.
- **The Claude engine package** (CAP-RTCONTRACT-053, UNREACHED) belongs to DEL-04-01 or DEL-04-02.

## Capability-file accuracy

- **CAP-HARNESS-027:** accurate as written. Live redaction runs only on chat titles and first-message text, and every `redactJsonLike` caller is legacy. This supports the forward CLM-004.5 finding that the live event path has no redaction, and strengthens its LEAST-CONFIDENT alternative, since no App key source is populated.
- **Other tags:** no REACH or STATE tag I checked was contradicted by the code (RTCORE-025, RTCORE-029, RTCONTRACT-022, 023, 036 and 039, HARNESS-032 and 039, BUILD-027).

## Effort

About 8 additional reads: the capability rows for the relevant areas (read by script, filtered by keyword), greps for the importers of `engine-conformance` and the section9 script, and the sealed-row lookups. Most rows were answered NOT_MINE by area after a keyword screen for mapping, event, SSE, redaction and conformance terms. Context was not tight.
