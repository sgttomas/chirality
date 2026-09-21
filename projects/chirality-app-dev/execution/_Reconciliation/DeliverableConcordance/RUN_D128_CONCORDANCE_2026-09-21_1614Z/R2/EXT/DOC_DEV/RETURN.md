# RETURN — EXT worker W_DOC_DEV (items 6 and 7, audit-only)

- **Mechanism:** TASK (Type 2), dispatched by the EXT WORKING_ITEMS manager (wave 5). No delegation.
- **Basis:** read only from the frozen tree at `00115c719`. Git was used read-only (`log`, `blame -L`) against that tree. Nothing was run, installed or tested.
- **Folder:** `R2/EXT/DOC_DEV/`. It holds six ledgers, each with its notes file. There are no errata files.
- **Coverage:** 41 units, 41 rows, no split rows.
- **Validation:** each ledger was validated on its own, with 0 errors and 0 warnings. The six ledgers are now sealed.

| Ledger | Rows | Dispositions | HumanDecisionNeeded | Validator | SHA-256 |
|---|---|---|---|---|---|
| `DOC-PRODAGENTS_claims.csv` | 9 | NOT_AUDITABLE 5, ALIGNED 4 | NO ×9 | `RESULT PASS errors=0 warnings=0` | `5922918e54fb35e9a8e50f2e83dc62d6aeb20e81ed567c3350360da4a9723cf0` |
| `DOC-README_claims.csv` | 7 | ALIGNED 3, STALE_SPECIFICATION 3, PARTIALLY_IMPLEMENTED 1 | R4-Q5 ×1 | `RESULT PASS errors=0 warnings=0` | `598f7d995079cc6e8ac8dbecc1a3f206dda1c7a7fa98e4a652682ed7b2e7eeb9` |
| `DOC-TRACEABILITY_claims.csv` | 2 | STALE_SPECIFICATION 1, PARTIALLY_IMPLEMENTED 1 | R4-Q5 ×1 | `RESULT PASS errors=0 warnings=0` | `6845b3551352f7eb20b60257dcbf61e35db1297ecbf0b9841be9aa333c0aaa0e` |
| `DOC-ADDING_A_TOOL_claims.csv` | 8 | ACCEPTED_DIVERGENCE 4, STALE_SPECIFICATION 2, ALIGNED 2 | R4-Q1 ×5 | `RESULT PASS errors=0 warnings=0` | `9d4d67c34cde60217e66ad1fa3ab4e6ab08283c002450c8231137fe17bb7586a` |
| `DOC-RUNTIME_ENGINE_CONTRACT_claims.csv` | 11 | PARTIALLY_IMPLEMENTED 3, ACCEPTED_DIVERGENCE 3, IMPLEMENTED_DIFFERENTLY 2, ALIGNED 2, STALE_SPECIFICATION 1 | R4-Q1 ×6, R4-Q5 ×4, R4-Q2 ×1 | `RESULT PASS errors=0 warnings=0` | `07363fdaabdf119d01fdb1929716d4539ae500d1b34c0dcb3cfce44ad80976fc` |
| `DOC-TOOL_CATALOG_claims.csv` | 4 | IMPLEMENTED_DIFFERENTLY 3, ALIGNED 1 | R4-Q1 ×3 | `RESULT PASS errors=0 warnings=0` | `e74c2bf5d03091929b7cd874cc6b6b9a56f872915233152bba3c477857bc2edb` |

## Key findings

- **Item 6 (product guidance).** `instructions/AGENTS.md` is accurate about how the product behaves at the frozen basis. No row needs a Root route.
  - Two of its statements are guidance to the agent, not controls the product enforces:
    - "TASK does not delegate": no live code limits delegation depth.
    - "Use a fresh child context": this is advisory only.
- **The UIEvent envelope is still the live stream (R4-Q5).** The D-GOV-43 notes in README, TRACEABILITY and RUNTIME_ENGINE_CONTRACT say the eight-name `UIEvent` set is "compatibility history". That is not what the code does:
  - The live Codex adapter and the browser SSE stream still use `UIEvent`.
  - Upstream method names and parameters travel nested inside `harness:event` / `codex.notification`.
  - The required premerge check `section8.sdk_native_stream` asserts `chat:complete` and `process:exit` on the live route.
- **The Codex adapter was never run through conformance (R4-Q2).** The conformance evaluator checks only the eight `UIEvent` names, and its fixtures exercise only `ClaudeAgentSdkManager` (RUNTIME_ENGINE_CONTRACT#9).
- **Stale text predating v3:**
  - Removed paths are still cited:
    - `frontend/src/lib/harness/tool-descriptor.ts`, `mcp/tool-names.ts` and `engine-conformance.ts` (moved under D-APP-47);
    - `examples/example-project`.
  - The network-policy proof's output folder is wrong (README#5).
  - TRACEABILITY is still titled DEL-07-01; its content belongs to DEL-09-01. Its REQ-17 lists 13 Section 9 IDs; the validator runs 16.
  - The Pi "pattern corpus only" sentences are false: a Pi adapter and the pi packages are present, and D-APP-72 ruled a bounded Pi engine.

## For the manager to resolve

1. **ACCEPTED_DIVERGENCE vs IMPLEMENTED_DIFFERENTLY.** I used one reading throughout:
   - Where a file's own D-GOV-43 note names a section's subject as compatibility history, the row is ACCEPTED_DIVERGENCE, because D-GOV-43 is GOVERNING.
   - Otherwise the row is IMPLEMENTED_DIFFERENTLY.
   - This produced 7 ACCEPTED_DIVERGENCE rows. The verifier may prefer IMPLEMENTED_DIFFERENTLY.
   - Two LOW rows flag the choice: ADDING_A_TOOL#3 and RUNTIME_ENGINE_CONTRACT#4.
2. **R4-Q1 and barrel-only LIVE tags.** The pack tags the runtime-contracts tool-descriptor registry LIVE only because the contracts barrel re-exports it. Its only importers are legacy modules.
   - I cited R4-Q1 on three rows (ADDING_A_TOOL#1, RUNTIME_ENGINE_CONTRACT#6, TOOL_CATALOG#3). On each, the exposure or enforcement part of the claim is met only by LEGACY_ONLY code.
   - This follows Addendum 8's reading. A strictly literal rule 3 would drop R4-Q1 on these rows.
3. **REACH tag for tooling.** Validation and build scripts sit outside the static reach map. I tagged them `REACH=TEST_ONLY` as verification tooling. The notes propose a `TOOLING` value instead.
4. **CauseTag.** No OTHER tokens were used.
