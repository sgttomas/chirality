# DEL-06-02 — forward-pass notes (worker A, double-blind)

Deliverable: `DEL-06-02_SDK_Read_Tool_Surface_and_Tool_Validation` (PKG-06), read from the frozen tree at
`00115c719`. Ledger: `DEL-06-02_claims.csv` (sealed after validation; SHA-256 in the return).

## 1. Census

Rows: 57. That is 35 indexed units (all covered), 51 rows from those units, 4 `REGISTER-n` rows and 2 `STATE-n` rows.

| Disposition | Rows |
|---|---:|
| STALE_SPECIFICATION | 18 |
| IMPLEMENTED_DIFFERENTLY | 18 |
| NOT_AUDITABLE | 8 |
| PARTIALLY_IMPLEMENTED | 5 |
| AUTHORITY_CONFLICT | 3 |
| REMAINING_STATE_MISMATCH | 2 |
| ALIGNED | 2 |
| DOCUMENTED_UNIMPLEMENTED | 1 |

| ClaimType | Rows |
|---|---:|
| REQUIREMENT | 22 |
| STATE_ASSERTION | 13 |
| CONTEXT_CLAIM | 11 |
| ACCEPTANCE | 7 |
| REGISTER_DEFECT | 4 |

- **SEE rows (counted separately): 8.**
  - CLM-008, CLM-016, CLM-022 and CLM-029 → CLM-001. These restate the REF-006 MATCH note.
  - CLM-013 and CLM-021.1 → CLM-006. These restate "paths TBD".
  - CLM-020 → CLM-012.
  - CLM-027 → CLM-010.8.
  - All 8 are included in the 57 rows and in the census above.
- **Split rate:** 5 of 35 units (14%).
  - CLM-004 is a conditions table: 2 rows.
  - CLM-010 has REQ-001..REQ-013 as a table: 13 rows. The index gives no `SubItems` for it, but it is a table of separately numbered REQs.
  - CLM-015 holds the traceability table and AC-001: 2 rows.
  - CLM-021 holds the records list and VER-001: 2 rows.
  - CLM-035 holds AC-002 and VER-002: 2 rows. This satisfies V-SUBITEMS.
- **Errata:** none. This is pass 1, so there are no errata-applied figures.
- **CauseTag:**

| CauseTag | Rows |
|---|---:|
| CODEX_SOLE_ENGINE | 25 |
| DOC_HYGIENE | 13 |
| NONE | 10 |
| PRE_V3_DRIFT | 7 |
| RUNTIME_EXTRACTION | 2 |

- **Validator:** `RESULT PASS errors=0 warnings=0`.

## 2. Least-confident rows

- **STATE-2 (LOW).** This row covers the D-APP-80 SOW-064 note ("tool catalog, requested-tool validation, name-collision prevention"). I read the live Runtime application-tool catalog as a different mechanism for SOW-064:
  - `contracts/src/application-tools.ts` and the `codex-supervisor.ts` `dynamicTools` path both came after the release (`da95ec194`, confirmed by blame).
  - That catalog validates and rejects duplicate and unknown names.
  - No App code registers a catalog.

  Alternative readings:
  - `DOCUMENTED_UNIMPLEMENTED` for the App share;
  - the Runtime catalog is not this deliverable's surface at all.
- **CLM-010.4 (MEDIUM).** I chose `DOCUMENTED_UNIMPLEMENTED` because no `mcp__chirality__*` server is attached on the live Codex path. Alternative reading: `ALIGNED` at module level, since the registry's naming convention holds.
- **CLM-010.6, CLM-010.9 and CLM-024 (AUTHORITY_CONFLICT).** Alternative reading: `IMPLEMENTED_DIFFERENTLY`. That reading treats CONTRACT's "Current Codex-only MVP release basis" paragraph as already making the SDK-specific clauses compatibility history. I did not apply that reading, for two reasons:
  - K-TOOL-2 and K-PERM-3 are worded engine-neutrally and are unamended;
  - D-GOV-43 does not name them.
- **CLM-035.1 (MEDIUM).** Alternative reading: `ALIGNED` at module level. The four coordination descriptors do resolve through the registry. I chose `IMPLEMENTED_DIFFERENTLY` for three reasons:
  - the registry now lives in `projects/chirality-runtime`;
  - the cited `frontend/packages/harness-contract` paths are 2-line `@deprecated` facades;
  - only the legacy SDK path consumes the tools.
- **CLM-001 family (STALE_SPECIFICATION).** Alternative reading, under MR-8(iv): the note is true of the D-APP-38 snapshot, so the defect lives only in REGISTER-1. I kept `STALE_SPECIFICATION` because the note says outright that it describes the *current* source state.

## 3. Register-defect summary

- **REGISTER-1.** `_REFERENCES.md` records CONTRACT, SPEC and PRD as MATCH, but none of those hashes reproduces (`HASH-RECOMPUTE@00115c719`). DIRECTIVE, TYPES and PLAN still match; I recomputed them myself.
  - Restated by: CLM-001/008/016/022/029, CLM-004.1, CLM-007, CLM-011, CLM-014, CLM-018, CLM-019 and CLM-033.
- **REGISTER-2.** `_DEPENDENCIES.md` has three problems:
  - its "Declared Upstream/Downstream: TBD — no accepted edges" contradicts its own 11-row register;
  - the `Dependencies.csv` EvidenceFile column cites the retired four-document kit (Guidance.md, Procedure.md, Datasheet.md);
  - DEP-06-02-011 is marked SATISFIED because of REF-006 MATCH, which rests on a hash that no longer reproduces.
- **REGISTER-3.** `_STATUS.md` says Last Updated 2026-07-12, but its History holds entries from 2026-07-19 and 2026-07-20. The 2026-07-20 entry is also listed first, out of order.
- **REGISTER-4.** `_CONTEXT.md` still describes the state before D-GOV-43:
  - "Claude Agent SDK / Anthropic remains the first concrete/current path";
  - "daemon read-tool exposure";
  - retired kit files.

  No PKG-06 carrier cites D-APP-127 or D-GOV-43.
- **Stale conflict table (CLM-033).** It says "no direct source conflict". In fact SPEC §14 and CONTRACT K-TOOL-1/K-TOOL-2/K-PERM-3 (SDK-framed and unamended) now conflict with the live Codex path, and nothing records that conflict.

## 4. Direction and cause

- **CODEX_SOLE_ENGINE (primary).** The whole requirement set is framed around resolving `opts.tools` into Claude Agent SDK options, and that is met only by the retained in-process path:
  - `frontend/src/lib/harness/tool-pool.ts`, `turn-engine.ts` and `sdk-options-builder.ts` are all `LEGACY_ONLY`.

  On the live path, things work differently:
  - Runtime `restrictRequestedTools` filters `opts.tools` by the readOnly regex, the role and the method capabilities. It uses no registry and no `UNKNOWN_TOOL` error.
  - The Codex adapter then ignores `opts.tools`. It reads only the model and the mode.
  - The mode maps to the Codex sandbox and approval policy (`contracts/src/delegated.ts:322-331`).
  - Direction: `GOV:D-GOV-43`, together with CONTRACT's Codex-only basis paragraph. The rows turning on this cite `R4-Q1`.
- **Secondary causes:**
  - `CAUSE2:RUNTIME_EXTRACTION`: the registry moved to `projects/chirality-runtime/packages/contracts/src/harness/`.
  - `CAUSE2:FACADE_DEPRECATION`: CLM-035.1.
  - `CAUSE2:CARRIER_PROPAGATION`: the REF-006 MATCH restatements.
  - `CAUSE2:PRE_V3_DRIFT`: there is no canonical-order normalization and no permuted-order fixture. Also, the `--check` generator mode was removed on 2026-07-31.
- **Findings independent of the Codex re-platform:**
  1. The legacy resolver keeps the request order and never sorts (`tool-pool.ts:41-45,100-110`). This goes against the SoW's canonical-ordering construction (CLM-005, CLM-019 step 6, CLM-026), and there is no permuted-input ordering fixture.
  2. The registry defines many implicit aliases, contrary to CLM-019 step 1 and CLM-026.
  3. The live boot fingerprint (`runtime-service.ts:559-584`) carries the placeholder `toolRegistryVersion: "shared-runtime/v1"` and `mcpServers: []`. REQ-012 is therefore only partly met live.
  4. The D-APP-70 "generator/check" mapping: the check now lives only in `tool-catalog.test.ts`.
- **Searches behind each `NONE_FOUND`:**
  - I grepped `_DECISIONS/_REGISTER.md` for `DEL-06-02`. The only hit is the D-APP-55 row.
  - I grepped the register for `generate-tool-catalog` and `alias`, and read the D-APP-70 ruling §5.
  - I reviewed the R1 DECISION_HITS for DEL-06-02 (D-APP-14/19/38/43/54/55/56/68/70/80) and read D-APP-56 line 59 and D-APP-68 lines 82-83.
  - None of these records the TBD-path staleness, the dropped `--check`, or the alias policy.
- **CONTEXT records used:** none were cited as `CTX:`. Every explaining record used is GOVERNING: D-GOV-43, D-GOV-35 and CONTRACT's Codex-only basis.

## 5. Method friction

- **SubItems gap.** CLM-010 is a table of 13 separately numbered REQs (`DEL-06-02-REQ-001..013`), but the index `SubItems` column is empty because the IDs use the table format. I split it anyway under §2.2. Proposal: have R1 also emit table-form `DEL-xx-yy-REQ-nnn` IDs as SubItems.
- **Legacy versus live judging.** Judging every SDK-framed requirement on the live path gives near-uniform `IMPLEMENTED_DIFFERENTLY` with `R4-Q1`. That hides the module-level quality findings: ordering, aliases, missing fixtures. I put those in Notes and added `CAUSE2:PRE_V3_DRIFT`. Proposal: a module-level sub-field, or permission to split legacy and live `.n` rows.
- **Barrel-only reach.** REACHABILITY marks `runtime-contracts` `tool-descriptor.ts` and `tool-names.ts` as `LIVE`, but only through the contracts barrel re-export from `daemon/standalone-bin.ts`. No live consumer calls them. I tagged them `REACH=LIVE` as the map requires and noted the barrel-only reach. Proposal: symbol-level reach, or a `LIVE(barrel)` note.
- **The D-APP-127 map is not a CONTEXT source.** I cited it only in a GOV prose parenthetical.

## 6. Effort

- **Files read:**
  - About 12 deliverable files, read in full or in part: ScopeOfWork, `_STATUS`, `_CONTEXT`, MEMORY, `_REFERENCES`, `_DEPENDENCIES`, `Dependencies.csv` and the Assessment. `_SEMANTIC*` and `_run_records` were not read in depth.
  - About 15 code and test files, read by line range.
  - 3 ruling records, read by line.
  - The evidence-pack CSVs, read by grep.
- **Context budget:** moderate, not tight.
