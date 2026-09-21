# DEL-07-05 — forward-pass notes (R2, PKG-07, wave 3)

Deliverable: `DEL-07-05_Dependencies_csv_v3_1_Reader_Writer_and_Linter`, read from the frozen tree at
`00115c719`. The ledger is `DEL-07-05_claims.csv` (58 rows). Validator result: `RESULT PASS errors=0 warnings=0`.

## 1. Census

**Rows by Disposition (sealed; there is no errata file yet)**

| Disposition | Rows |
|---|---:|
| ALIGNED | 18 |
| STALE_SPECIFICATION | 18 |
| PARTIALLY_IMPLEMENTED | 13 |
| NOT_AUDITABLE | 5 |
| DOCUMENTED_UNIMPLEMENTED | 2 |
| IMPLEMENTED_DIFFERENTLY | 2 |
| **Total** | **58** |

**Rows by ClaimType × Disposition**

| ClaimType | ALIGNED | STALE_SPEC | PARTIAL | DOC_UNIMPL | IMPL_DIFF | NOT_AUDITABLE | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| REQUIREMENT | 17 | 1 | 9 | 2 | 2 | 0 | 31 |
| ACCEPTANCE | 0 | 1 | 4 | 0 | 0 | 0 | 5 |
| STATE_ASSERTION | 1 | 9 | 0 | 0 | 0 | 0 | 10 |
| CONTEXT_CLAIM | 0 | 4 | 0 | 0 | 0 | 5 | 9 |
| REGISTER_DEFECT | 0 | 3 | 0 | 0 | 0 | 0 | 3 |

- **Coverage.** All 35 indexed units (CLM-001..035) are present. Run-local rows: REGISTER-1..3 and STATE-1.
- **Split rate.** 3 of 35 units were split (8.6%), giving 22 rows:
  - CLM-012 into `.1`–`.18`, one row per REQ-DEL-07-05-001..018;
  - CLM-017 into `.1` (UPD-133 and REF-006 text) and `.2` (AC-001);
  - CLM-024 into `.1` (worklist table) and `.2` (VER-001).
- **SEE rows (counted separately).** 13 rows carry `SEE:`:
  - 12 point to `REGISTER-1`, the REF-006 `MATCH` restatements: CLM-001, 008, 009, 010, 016, 017.1, 018, 020, 023, 024.1, 025 and 034;
  - 1 points to `CLM-012.10`: CLM-033.
  - Excluding SEE rows, the census is 45 rows: STALE_SPECIFICATION 6, ALIGNED 18, PARTIALLY_IMPLEMENTED 12, and the others unchanged.
- **Other figures.**
  - HumanDecisionNeeded: `R4-Q1` on 11 rows, `NO` on 47.
  - Confidence: HIGH 34, MEDIUM 23, LOW 1.

## 2. Least-confident rows

- **CLM-012.17 (REQ-017, unknown option keys; LOW).**
  - Ledger reading: `DOCUMENTED_UNIMPLEMENTED`. The dependency route ignores unknown body keys without a warning.
  - Alternative reading: SPEC §13.1 governs runtime turn options, which another deliverable owns. The dependency API has no "options", so the row is not this slice's to meet (`UNKNOWN`), or it needs re-binding.
- **CLM-012.14 (REQ-014, MCP policy parity; MEDIUM).**
  - Ledger reading: `DOCUMENTED_UNIMPLEMENTED` on the live path.
  - Alternative reading: `AUTHORITY_CONFLICT`. K-MCP-1 and SPEC §14.2 are unamended, and the Codex-only preamble in PRD/SPEC/CONTRACT does not name them.
  - I used the named R4-Q1 route because the only meeting code is `LEGACY_ONLY` (Addendum 6, rule 3).
- **REGISTER-3 (OBJ-006 row as `TargetType=UNKNOWN`; MEDIUM).**
  - Ledger reading: the "v3.1 has no OBJECTIVE TargetType" premise is false, because TYPES §6.5 files objectives under `REQUIREMENT`.
  - Alternative reading: the extractor made a conservative judgment rather than a false statement.
- **CLM-012.13 (API GET/PUT; MEDIUM).**
  - Ledger reading: `ALIGNED`, with the route tagged `REACH=LIVE` as an API entry.
  - Alternative reading: no rendered surface calls it, so reach could be argued as unexercised (see §5).
- **CLM-012.3 (REQ-003, linter; MEDIUM).**
  - Ledger reading: `PARTIALLY_IMPLEMENTED`. Validation happens only when a write is rejected, and GET exposes no lint findings (FR-055).
  - Alternative reading: INSP-03 read write-time validation as a full PASS.
- **CLM-028 and CLM-029 (`IMPLEMENTED_DIFFERENTLY`; MEDIUM).**
  - Ledger reading: the code normalizes legacy DependencyType values without authority from TYPES or SPEC, and it enforces provenance on every ACTIVE row.
  - Alternative reading: the first is a harmless undocumented extra (`IMPLEMENTED_UNDOCUMENTED`), and the second follows UPD-133 (CLM-017), so only the SoW guidance text is stale.

## 3. Register-defect summary

- **REGISTER-1: `_REFERENCES.md`.** The REF-002 (CONTRACT), REF-003 (SPEC) and REF-006 (PRD) rows record MATCH, but none of those hashes reproduces (`HASH-RECOMPUTE@00115c719`, evidence-pack `REFERENCE_HASHES.csv`).
  - REF-001 DIRECTIVE, REF-004 TYPES and REF-005 PLAN still match (recomputed with shasum).
  - REF-007..010 are Root workflows outside the evidence roots and were not recomputed.
  - The same `MATCH` claim is repeated in 12 SoW units, in `_DEPENDENCIES.md:93,115` and in `Dependencies.csv` DEP-07-05-026 `Statement`.
- **REGISTER-2: `Dependencies.csv` provenance.** 25 ACTIVE rows cite `Datasheet.md`, `Specification.md` and `Procedure.md`. Those files were deleted on 2026-07-13 by `8cb9cdaf0`, which replaced them with `ScopeOfWork.md`. The provenance fields therefore name files that do not exist, and the writer's non-empty check cannot detect it.
- **REGISTER-3: `Dependencies.csv` DEP-07-05-002 and `_DEPENDENCIES.md:91`.** The OBJ-006 row was kept as `UNKNOWN` on the claim that no objective TargetType exists. TYPES §6.5 says it does.
- **Also observed (not rows).**
  - `_DEPENDENCIES.md:86` records a machine-specific absolute decomposition path in dated run notes.
  - The CLM-034 conflict table is incoherent: its mismatch premise was rewritten to "MATCH", but the ruling cell is still "TBD".
  - The SoW cites "PRD §17.2" for the endpoint; the correct locations are PRD §9.2 (line 881) and SPEC §17.2. This is recorded on CLM-012.13.

## 4. Direction and cause

- **Main CauseTags.**
  - `PRE_V3_DRIFT` (14): the reader, writer and schema code blames to `7bee9ae41` (2026-05-18). The provenance files were removed on 2026-07-13.
  - `DOC_HYGIENE` (13): the REF-006 restatements and REGISTER-1.
  - `CODEX_SOLE_ENGINE` (7): the MCP, hook and permission surfaces live only on the legacy Claude-SDK path. On the live Codex runtime, `runtime-service.ts:580` exposes `mcpServers: []`; that line blames to `2d75d7364` (2026-09-12).
  - `CARRIER_PROPAGATION` (1): STATE-1.
- **`CAUSE2:` secondaries.**
  - `CARRIER_PROPAGATION` on the REF-006 and REQ-014 rows.
  - `PRE_V3_DRIFT` on the mixed CODEX_SOLE_ENGINE rows.
  - `CODEX_SOLE_ENGINE` on REQ-015, CLM-014, CLM-024.2 and STATE-1.
  - `DOC_HYGIENE` on REGISTER-2 and CLM-035.
- **Records used.** Only GOVERNING records: `GOV:D-GOV-43` (PRD, CONTRACT and SPEC headers "Amended under D-GOV-43", plus the Codex-only preamble) and `GOV:D-APP-127`. No CONTEXT record was used.
- **Searches behind each `NONE_FOUND`.**
  - I grepped `execution/_Coordination/_DECISIONS/_REGISTER.md` for Dependencies.csv, `deps_`, COORDINATION, target resolution and OBJECTIVE_TARGET. The only related hits are D-APP-13 (gating of the mutating MCP `deps_write`, pre-v3), D-APP-38 (reference model) and D-APP-56 (UPD-077/133). None explains the target-resolution, header-reporting, normalization or provenance-file gaps.
  - The CONTEXT sources in `plans/` and `plans/steers/` (v3 release plan, steers) are not present in the App tree at the frozen basis; the find returned nothing.
  - `execution/_ScopeChange` names DEL-07-05 only through the SCA-APP-008 and SCA-APP-010 coverage matrices (K-PATH-2 mapping). Neither changes this slice.
- **R4-Q1.** It is cited on 11 rows (CLM-003, 004, 011, 012.14, 012.15, 014, 017.2, 021, 024.2, 027 and STATE-1), where the MCP, permission, hook or instruction-root part is met only by `REACH=LEGACY_ONLY` code: `lib/harness/mcp/read-tools.ts`, registered only by `lib/harness/sdk-options-builder.ts`.
  - On partially met rows the LIVE route covers the other parts, so rule 3 is applied per part and the reason is stated in each row's Notes.
  - `ALSO_MODULE:` is given on the product-behaviour rows.
- **No `AUTHORITY_CONFLICT` rows.** K-MCP-1 and SPEC §14.2/§15.2 are unamended for D-GOV-43, and I routed those rows to R4-Q1 as the brief directs.

## 5. Method friction

- **Reach of API routes without a rendered caller.** `app/api/working-root/deliverable/dependencies/route.ts` is a product entry under CONVENTIONS §9, so I tagged it `REACH=LIVE`.
  - Its only UI callers, `pipeline-surface.tsx:407` and `workbench-surface.tsx:264` via `deliverable-api.ts:242`, sit under `LoopShell` and `PortalLoopShell`.
  - `WovenDialogueRoute` discards both (`woven-dialogue-route.tsx:18`, `void legacy`, `9b005c23a`).
  - `REACHABILITY.csv` tags `deliverable-api.ts` LIVE via `chat/page>loop-shell`. That disagrees with the rendered tree.
  - **Proposed:** add a note value such as `ENTRY_ONLY` for handlers that are served but not invoked by the shipped UI, keeping the tag vocabulary unchanged.
- **Mixed rows under Addendum 6 rule 3.** The rule speaks of rows where the "only code" meeting the claim is legacy. It does not say how to treat a row that LIVE code meets in part and legacy code meets for the hook or MCP part. I cited R4-Q1 per part.
  - **Proposed:** say explicitly that R4-Q1 applies whenever any required component is met only by `LEGACY_ONLY` code.
- **SoW units mixing a substantive table with a REF-006 line** (CLM-003, CLM-016, CLM-028). One Disposition per unit forces a choice. I disposed on the substance where it diverges (CLM-003, CLM-028) and on the stale line where the substance holds (CLM-016).
- **How reach was confirmed.**
  - I followed the imports from `app/api/.../dependencies/route.ts` to `lib/workspace/deliverable-contracts.ts` to `lib/dependencies/*`.
  - For MCP, I followed `read-tools.ts` to its only importer, `sdk-options-builder.ts` (LEGACY_ONLY in the map), and checked the live Runtime: the `runtime-service.ts` fingerprint reports `mcpServers: []`, and no Runtime package registers Chirality MCP tools. A grep of `projects/chirality-runtime/packages` for `mcpServers`, `mcp_servers` and the tool-name arrays found only contracts.
  - For the UI, I checked `app/page.tsx` and `app/chat/page.tsx`, both of which pass through `WovenDialogueRoute`.

## 6. Effort

- **Files read.** About 30 files:
  - the deliverable's SoW, `_STATUS`, `_CONTEXT`, `MEMORY`, `_REFERENCES`, `_DEPENDENCIES`, `Dependencies.csv` (by script) and the INSP-03 assessment;
  - 4 dependency modules, `deliverable-contracts.ts`, the route and parts of `read-tools.ts`;
  - the shell and route files needed for the reach check;
  - slices of SPEC, CONTRACT, TYPES and PRD;
  - the evidence pack, R1 inventories (by script), the gate transcript and the validator.
- **Not read.** `_SEMANTIC.md`, `_SEMANTIC_LENSING.md` and the `_run_records/**` bodies; the decision-hit rows were enough.
- **Budget.** The context budget was comfortable, not tight.
