# DOC-TOOL_CATALOG notes (RUN_D128 R2 EXT, item 7, audit-only)

Ledger: `DOC-TOOL_CATALOG_claims.csv`, 4 rows, validator `RESULT PASS errors=0 warnings=0`. This ledger is audit-only (CONVENTIONS §8): nothing is repaired by this run.

## 1. Census

STATE_ASSERTION 4: ALIGNED 1 (#0); IMPLEMENTED_DIFFERENTLY 3 (#1-#3). Split rate 0/4: the 27-row catalog table in #3 was not split, because every row turns on the same live-path finding. SEE rows 0. No errata. R4-Q1 on 3 rows.

## 2. Least-confident rows

- `DOC:TOOL_CATALOG#3` (MEDIUM). Alternative: ALIGNED at module level. The table equals the registry render, and tool-catalog.test.ts passes. Addendum 6 rule 1 makes 'Exposed to model' and the hook-requirement columns product-behaviour claims, and those are met only by legacy code. Unlike its siblings, the generated catalog has no D-GOV-43 note, so it cannot take ACCEPTED_DIVERGENCE.
- `DOC:TOOL_CATALOG#1` (MEDIUM). Alternative: ALIGNED as a description of the retained domain MCP modules (ALSO_MODULE:ALIGNED recorded).

## 3. Register-defect summary

None.

## 4. Direction and cause

CODEX_SOLE_ENGINE (#1, #3); NATIVE_DELEGATION (#2, CAUSE2:CODEX_SOLE_ENGINE); direction GOV:D-GOV-43; GOV:D-APP-127. No OTHER tokens.

## 5. Method friction

- Scripts under `frontend/scripts/**` and `frontend/package.json` sit outside the static reach map but match the validator's code-path pattern, so they must carry a REACH tag. I tagged them `REACH=TEST_ONLY` as verification tooling. Proposal: add `REACH=TOOLING` (or seed the pack from package.json scripts) so tooling is not conflated with test-only product code.
- The runtime-contracts descriptor registry is tagged LIVE by the pack only through the contracts barrel; its sole importers are legacy `lib/harness` modules. Under a literal rule 3 that LIVE tag would suppress R4-Q1 on exposure claims. I cited R4-Q1 where the exposure/enforcement part of the claim is met only by LEGACY_ONLY code and the LIVE module supplies metadata only (ADDING_A_TOOL#1, RUNTIME_ENGINE_CONTRACT#6, TOOL_CATALOG#3). Proposal: the pack could mark barrel-only reach as `LIVE(barrel)` so R3 can re-derive consistently.
- The catalog is generated, so its missing D-GOV-43 banner is a generator matter (runtime-contracts tool-catalog.ts renders the header). An audit-only repair would go to the renderer, not to the markdown.

## 6. Effort

About 6 files (catalog, generator, runtime-contracts tool-catalog/tool-descriptor, tool-catalog test, HARNESS capabilities). Context comfortable.
