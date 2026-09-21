# DEL-06-03 Initial Chirality MCP Read Tools: forward-pass notes

Run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`, PKG-06, R2 pass 1 (forward). Frozen basis `00115c719`.
Ledger: `DEL-06-03_claims.csv` (61 rows plus `#END`). Validator: `RESULT PASS errors=0 warnings=0`.

## 1. Census

**Coverage and splitting.** The index has 39 units: SEC-1..3, CLM-001..035 and REM-1.

- 3 of the 39 units are split (7.7%):
  - SEC-2 into `.1`..`.3`, one row per numbered acceptance obligation;
  - CLM-010 into `.1`..`.15`, one row per REQ-06-03-001..015;
  - CLM-035 into `.1` (AC-002) and `.2` (VER-002), as V-SUBITEMS requires.
- The 3 split units produce 20 rows, and the other 36 units produce one row each (56 indexed rows).
- CLM-016 (AC-001) and CLM-024 (VER-001) each list one sub-item, so each keeps a single row that names its item.
- There are 5 run-local rows: REGISTER-1..3 and STATE-1..2.

**By ClaimType.**

| ClaimType | Rows |
|---|---:|
| REQUIREMENT | 25 |
| CONTEXT_CLAIM | 13 |
| STATE_ASSERTION | 10 |
| ACCEPTANCE | 8 |
| REGISTER_DEFECT | 3 |
| EXCLUSION | 1 |
| REMAINING_WORK | 1 |

**By Disposition.** The table counts every row, SEE rows included. The next table breaks out the SEE rows.

| Disposition | All rows | SEE rows | Non-SEE rows |
|---|---:|---:|---:|
| STALE_SPECIFICATION | 15 | 7 | 8 |
| AUTHORITY_CONFLICT | 13 | 5 | 8 |
| PARTIALLY_IMPLEMENTED | 11 | 2 | 9 |
| NOT_AUDITABLE | 10 | 0 | 10 |
| ALIGNED | 6 | 0 | 6 |
| DOCUMENTED_UNIMPLEMENTED | 4 | 0 | 4 |
| IMPLEMENTED_DIFFERENTLY | 1 | 0 | 1 |
| REMAINING_STATE_MISMATCH | 1 | 0 | 1 |
| **Total** | **61** | **14** | **47** |

**SEE rows (14, counted separately, MR-4).**

- 7 rows restate REF-006 MATCH and point to REGISTER-1: CLM-001, 008, 015, 017, 025, 029 and 033.
- 3 rows restate the in-process wrapper claim and point to SEC-1: SEC-2.1, CLM-009 and STATE-2.
- 2 rows point to CLM-003: CLM-010.1 and CLM-010.4.
- 2 rows point to CLM-004: CLM-010.8 and CLM-010.9.

**Confidence.** HIGH 30, MEDIUM 31, LOW 0.

No errata file exists yet, so there are no sealed and errata-applied figures to compare.

## 2. Least-confident rows

No row is LOW. These MEDIUM rows are the most sensitive to a different reading:

- **AUTHORITY_CONFLICT on the SDK-mechanism rows.** These are SEC-1, CLM-004, CLM-005, CLM-010.2/.5/.6/.7/.8/.9 and REM-1.
  - My reading: the governing clauses these rows restate are still unamended, and they prescribe Claude-SDK in-process mechanics:
    - PRD FR-119, `createSdkMcpServer`;
    - K-TOOL-1, "SDK version, MCP server set";
    - K-PERM-3, SPEC §14.3 and FR-081, `allowedTools`, `canUseTool` and `dontAsk`;
    - K-PERM-4, readOnly.
  - D-GOV-43 amended CONTRACT/SPEC elsewhere without naming these clauses. It re-expressed K-RUNTIME-1 so that the Runtime service owns tools, and it leaves approval and sandbox policy to the user. Under that ruling, the live path carries no Chirality MCP server: `runtime-service.ts:580` records `mcpServers: []`, and no App application-tool registration was found.
  - Alternative reading: treat these rows as `DOCUMENTED_UNIMPLEMENTED` under the live-path rule. Codex supports dynamic and MCP tools (the runtime `application-tools` contract exists), so the clauses could still be met live and are not strictly undercut.
  - Both readings route to `R4-Q1`.
- **CLM-010.11 / .12 / .13 (ALIGNED).**
  - My reading: the live readers behind `/api/working-root/deliverable/status`, `/dependencies` and `/scope` satisfy REQ-011/012/013, which are phrased as reader "behavior".
  - Alternative reading: these REQs are about the agent tool. That makes them `PARTIALLY_IMPLEMENTED`, since the reader is live but the tool is legacy.
- **CLM-010.3 (DOCUMENTED_UNIMPLEMENTED).**
  - `scaffold.ts` is LIVE in the map only through a type-only import. The symbol `previewScaffoldExecutionRoot` is called only from `read-tools.ts:775` (LEGACY_ONLY).
  - Alternative reading: follow the module-level map and call it `PARTIALLY_IMPLEMENTED`.
- **CLM-035.1 (IMPLEMENTED_DIFFERENTLY, NATIVE_DELEGATION).**
  - Alternative reading: `AUTHORITY_CONFLICT`. D-APP-68 (GOVERNING) assigned the composition, and D-GOV-43/SPEC §25.7 moved delegation to Codex native without naming D-APP-68.
- **CLM-035.2 (ALIGNED).**
  - This is a module-level verification of legacy code.
  - Alternative reading: the same as CLM-035.1, if the verifier judges VER-002 on the live path.
- **REGISTER-1 DirectionEvidence `GOV:D-GOV-43`.**
  - The 2026-09-12 amendments explain the CONTRACT/SPEC drift. The PRD drift may have other causes.

## 3. Register-defect summary

- **REGISTER-1.**
  - Defect: the `_REFERENCES.md` MATCH hashes for REF-002 (CONTRACT), REF-003 (SPEC) and REF-006 (PRD) do not reproduce.
  - Evidence: `HASH-RECOMPUTE@00115c719`, `REFERENCE_HASHES.csv` rows `Match=NO`.
  - Seven SoW notes restate it as SEE rows. Six other units carry it in part.
- **REGISTER-2.**
  - Defect: the `_DEPENDENCIES.md` "Declared Upstream/Downstream" sections still read "TBD - no accepted dependency edges have been extracted yet", but the register holds 18 ACTIVE rows.
  - Disposition: STALE_SPECIFICATION.
- **REGISTER-3.**
  - Defect: the `_DEPENDENCIES.md` D-APP-56 P45 block still calls itself the "current structured-register mirror" (ACTIVE 9), although its own preview note says it becomes history after the DEP-015/016 write, which landed under D-APP-109/110.
  - Disposition: REMAINING_STATE_MISMATCH.
- **Related state rows:**
  - SEC-3: the seating note says DEP-015/016 "await" a pass that was applied on 2026-09-05.
  - STATE-1: `_CONTEXT.md` still says the Claude SDK is the current path.
  - CLM-013, 019 and 020: acceptance-evidence and location TBDs that are stale since 2026-06.
- **INSP-03 assessment.**
  - It cites `frontend/src/lib/harness/tool-descriptor.ts` and `frontend/src/lib/harness/mcp/tool-names.ts`. Neither exists at the frozen basis: both moved to `projects/chirality-runtime/packages/contracts/src/harness/`.
  - Its REQ PASS conclusions are marked OVERTAKEN, except REQ-011/012/013/015, which still reproduce on the live readers.

## 4. Direction and cause

**Main CauseTags.**

- CODEX_SOLE_ENGINE (27 rows): the tool surface is `LEGACY_ONLY` and the live path exposes no Chirality MCP tools.
- DOC_HYGIENE (10 rows): REF-006 and the register defects.
- PRE_V3_DRIFT (4 rows): TBD cells that predate the 2026-06 implementation.
- LIFECYCLE_GATE_PENDING (2 rows): the propose tool and the VER-001 human review.
- CARRIER_PROPAGATION (1 row): SEC-3.
- NATIVE_DELEGATION (1 row): CLM-035.1.

**CAUSE2 secondaries.**

- FACADE_DEPRECATION: CLM-003, CLM-010.1 and CLM-010.4. The descriptors and names moved to runtime-contracts.
- PRE_V3_DRIFT: CLM-005, 010.6, 012, 016 and 021.
- LIFECYCLE_GATE_PENDING: SEC-1, CLM-022 and REM-1.
- CODEX_SOLE_ENGINE: CLM-024.
- CARRIER_PROPAGATION: STATE-1.
- DOC_HYGIENE: CLM-014.

**Records used.**

- `GOV:D-APP-127` and `GOV:D-GOV-43`:
  - the CONTRACT amendment header at line 7;
  - K-RUNTIME-1 as re-expressed;
  - SPEC §25.7, retired to Codex native sub-agents.
- `GOV:D-APP-108`: the seating of V3-01 and its write locus.
- `GOV:D-APP-109` and `GOV:D-APP-110`: the dependency extraction and the decompose.
- `GOV:D-APP-43`: the ADQ-11 closure of the dependency fallback.
- No CONTEXT (`CTX:`) record was needed. The GOVERNING rulings explain every divergence I cite.

**Searches behind NONE_FOUND (CLM-019, CLM-020, REGISTER-2).**

- `_DECISIONS/_REGISTER.md` rows that name DEL-06-03 or MCP: D-APP-13, 50, 51, 68, 109 and 110. None of them addresses keeping these TBD or placeholder cells.
- The RUN_BASIS §5 CONTEXT set: the v3 release plan and the g0/app ruling steers.
- The pack's `DECISION_HITS.csv` for DEL-06-03 (REGISTER/RULING hits: D-APP-109 and D-APP-110 only).
- Result: no record explains leaving these cells unrefreshed.

**Carrier propagation.** `D-APP-127_APPLICATION_MAP.csv` shows that no DEL-06-03 carrier cites D-APP-127 or D-GOV-43. The SoW, `_CONTEXT` and `_STATUS` (the V3-01 write locus) still describe the pre-D-GOV-43 Claude-SDK in-process topology.

## 5. Method friction

- **Module-level REACH hides symbol-level reach.** `scaffold.ts` is LIVE only through a type-only import, which is the map's known limit. I tagged the module per the map and put the symbol-level fact in Notes. Proposal: let workers append `SYMBOL-REACH=` when the two differ.
- **Build-script evidence has no REACH vocabulary.** `harness-section9-manifest.json` is outside the map, so I tagged it `REACH=TEST_ONLY` and said so in Notes. Proposal: define a `BUILD_ONLY` note convention.
- **MR-8(iv) and MR-4 SEE interact awkwardly.** The SoW rows that restate the register fact use `SEE:REGISTER-1` with REGISTER-1's STALE_SPECIFICATION, but MR-8(iv) says such a claim "is a REGISTER row, not STALE_SPECIFICATION". Proposal: state explicitly that SoW restatements inherit the REGISTER row's disposition through SEE.
- **The AUTHORITY_CONFLICT versus live-path boundary is judgment-heavy.** I used this rule: a clause that names the Claude-SDK mechanism gets AUTHORITY_CONFLICT; a mechanism-neutral clause is judged on the live path. The verifier should check that I applied it consistently.

## 6. Effort

- **Files read:**
  - all 9 carrier files in full or in large part: SoW, `_STATUS`, `_CONTEXT`, MEMORY, `_REFERENCES`, `_DEPENDENCIES` and `Dependencies.csv`, and the INSP-03 assessment (`_SEMANTIC*` and `_run_records` were not needed);
  - about 12 code and test files by line range;
  - SPEC §14, the CONTRACT K-rows, the PRD FR-rows, the D-APP-127 grep and the register grep.
- **Context budget:** moderate. PREGATHER saved the broad code sweep, and every anchor I cite was re-verified.
