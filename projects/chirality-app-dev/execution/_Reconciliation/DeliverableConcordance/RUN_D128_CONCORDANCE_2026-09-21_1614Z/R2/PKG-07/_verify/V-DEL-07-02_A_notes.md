# V-DEL-07-02_A — verifier shard notes (PKG-07, ledger of record DEL-07-02_A)

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a30 | 15 | 6 | 8 | 1 |
| b | 1 | 0 | 1 | 0 |
| c | 2 | 2 | 0 | 0 |
| **Total** | **18** | **8** | **9** | **1** |

Verdict-field refutations (Disposition / Response): **0 of 18**. All 9 REFUTED items are
field-only (CauseTag ×5, ImplementationEvidence REACH ×4) and belong in CORRECTIONS.csv under
RUN_BASIS Addendum 3. The one CONTESTED item is on Disposition (CLM-003).

## (ii) Systematic patterns

1. **REF-006 cluster, CauseTag PRE_V3_DRIFT is wrong** (CLM-001, CLM-004.2, CLM-006, CLM-007,
   CLM-022). The recorded REF-006 hash `8649ccba…` was written by `23b3879b3` (2026-09-12, the
   D-GOV-43 application tranche) and equals `docs/PRD.md` at that commit. PRD then changed in
   `9eaddb596` (#778, same day) to `17ca3f3c…`. So the divergence is post-v3. The Notes claim
   "PRD changed from 2026-07-22 (pre-v3)" is false, and so is "no later ruling refreshes DEL-07-02
   references". The correct primary tag is DOC_HYGIENE. Disposition STALE_SPECIFICATION holds
   (tie-break rule 3: current-tense MATCH with no named snapshot).
2. **scaffold.ts REACH at symbol level (CLM-005, CLM-009.11, CLM-009.12, CLM-013.1).**
   - The worker's reason for overriding the map's LIVE tag is correct: `route.ts` imports only
     the type `CoordinationMode`.
   - But the worker tagged every cited symbol TEST_ONLY. The parser, plan and path-check symbols
     (`requireAbsolutePath` 214, `parseDecomposition` 265-351, `buildPackagePlans` 379-409) run
     through `previewScaffoldExecutionRoot`. That function is called by the legacy
     `scaffold_preview` MCP tool (`mcp/read-tools.ts`, which only `sdk-options-builder.ts`
     imports), so these symbols are `REACH=LEGACY_ONLY`. This matches the HARNESS
     CAP-HARNESS-052 note.
   - Only the write and validate symbols (432-499, 547-954) are TEST_ONLY.
   - No Disposition changes. R4-Q1 is still not required, because the code meeting each of these
     claims is mixed TEST_ONLY / LEGACY_ONLY, never LEGACY_ONLY alone.
3. **Live-path finding confirmed.**
   - `app-owned-composition.ts:226` passes `undefined` as `scaffoldPort` (constructor
     `runtime-service.ts:118`), so `RuntimeService.scaffold` throws a 501 error.
   - The pre-A2 `runtime-host-legacy.ts:659` composed `scaffoldExecutionRoot`, and `39c0bb6ab`
     deleted it. This supports A2_TOPOLOGY and the W2/W3 CTX citations.
   - CONTESTED CLM-003: it is DOCUMENTED_UNIMPLEMENTED, while CLM-008 and CLM-009.9 are
     PARTIALLY_IMPLEMENTED on the same live route-surface evidence. The rulebook admits both
     readings.
4. Line anchors checked at the frozen tree all land on the stated content: `route.ts`,
   `runtime-daemon-harness-port.ts`, `runtime-daemon.ts`, `runtime-service.ts`, `client.ts`,
   `types.ts`, the test case names, and Assessment line 77. PostReleaseBasis NO is correct: no
   relied-on range overlaps TOUCHED_PATHS (`app-owned-composition.ts` touched rows are 228 and
   later, not 226).

## (iii) Effort

About 25 file reads and greps, and 6 read-only git log/show calls against the frozen tree.
Context was not tight.
