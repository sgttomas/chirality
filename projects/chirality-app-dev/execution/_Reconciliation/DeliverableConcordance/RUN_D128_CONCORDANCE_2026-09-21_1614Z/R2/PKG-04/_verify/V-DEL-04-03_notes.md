# V-DEL-04-03 — verifier shard notes (R2, PKG-04)

The shard was graded against the shared `GRADING_KEY.md`, with the frozen tree at `00115c719` as the only evidence basis.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a | 2 | 0 | 0 | 2 |
| n | 12 | 12 | 0 | 0 |
| b | 3 | 2 | 0 | 1 |
| c | 3 | 3 | 0 | 0 |
| e | 2 | 1 | 0 | 1 |
| **Total** | **22** | **18** | **0** | **4** |

- There are 19 distinct ledger keys.
- No item is REFUTED on a verdict field or on any other field.

## (ii) Patterns

1. **Live-path versus module-level subject within one SoW table (GRADING_KEY 2).**
   - The worker read CLM-004.1, .2, .3, .5 and .6 on the live Codex path.
   - It read CLM-004.4 at module level, although that row sits in the same Conditions table and FR-083 is a P0 product requirement.
   - Both readings are defensible, so the item is CONTESTED: ALIGNED || IMPLEMENTED_DIFFERENTLY.
   - The mapper-subject REQ rows (CLM-009.12, CLM-018 and CLM-024) are correctly module-level.
   - Example key: DEL-04-03#CLM-004.4.
2. **What counts as partial secret redaction on the live Runtime sinks.**
   - CLM-004.5 and its Disposition erratum turn on one question: does the daemon logger's bounded, control-character-free field projection count as partial secret exclusion? It is `safeDiagnosticText` and `describeRuntimeFailure` in `runtime-daemon.ts:65-88`.
   - The projection never copies error details wholesale, which is structural. It does not scrub secret values out of the messages it keeps.
   - Event data is plainly unredacted: `delegated-engine-adapter.ts:282,289` forwards raw params. CONTRACT K-EVENT-6, as amended under D-GOV-43, requires structural redaction before every sink.
   - Both DOCUMENTED_UNIMPLEMENTED and PARTIALLY_IMPLEMENTED are defensible, so both the class-a row and the class-e erratum are CONTESTED.
   - The ImplementationEvidence erratum is accurate. It is CONFIRMED: the lines exist, the reach is LIVE, and blame goes to d29f78d95/eff0c9bda, outside the TOUCHED_PATHS ranges.
   - Keys: DEL-04-03#CLM-004.5 (class a and class e).
3. **Terminal-outcome ownership (REQ013).**
   - The mapper translates the SDK success and failure results and passes `terminal_reason`.
   - The claude-agent-sdk-manager emits the interruption (`exitCode 130`), and the TurnEngine does cancellation classification.
   - The ALIGNED reading, that the MUST NOT clause assigns this split, and the literal PARTIALLY_IMPLEMENTED reading are both defensible. The worker flagged this itself (LEAST-CONFIDENT).
   - Key: DEL-04-03#CLM-009.13.

Checks that held:

- **REACH at symbol level:** `runEngineConformance` is imported only by the App tests `engine-conformance.test.ts` and `pi-omlx-wire.integration.test.ts`, so its TEST_ONLY tag holds even though the module is LIVE.
- **Other tags and reach:**
  - The UIEvent and HarnessEvent types are LIVE TYPE-ONLY.
  - The mapper is LEGACY_ONLY; its only non-test importer is `claude-agent-sdk-manager.ts`.
- **PostReleaseBasis:** NO holds for every cited touched file (`app-owned-composition.ts:13,214`; `runtime-daemon.ts:65-88`). Neither the deliverable files nor the mapper are on TOUCHED_PATHS.
- **DirectionEvidence NONE_FOUND on CLM-004.6:** holds. Neither the register nor the done-declaration candidate mentions K-ENGINE-2 or engine conformance.
- **CLM-002 and CLM-027:** the reading holds. `_REFERENCES.md` REF-006 has read MATCH since 3ea604e8f (2026-07-23). The present PRD hash drift is a separate REGISTER-3 row.

## (iii) Capability-file accuracy

- CAP-BUILD-027, CAP-HARNESS-024 and CAP-RTCONTRACT-023 hold at the frozen tree:
  - `TURN_STREAM_KEEPALIVE_MS = 15_000` is at `http.ts:54`;
  - `turnStreamResponse` is used by both named routes;
  - the harness `types.ts` has no value exports;
  - the section 9 manifest entry is at `:24-27`.
- No inaccuracy was seen.

## (iv) Effort

- About 25 targeted reads and greps in the frozen tree: the mapper, the delegated adapter, runtime-daemon, the composition, CONTRACT/PRD/TYPES/SPEC, and the deliverable SoW, _STATUS, _REFERENCES and Dependencies.
- Plus the rulebook, the key, the evidence pack and the capability rows.
- The context budget was not tight.
