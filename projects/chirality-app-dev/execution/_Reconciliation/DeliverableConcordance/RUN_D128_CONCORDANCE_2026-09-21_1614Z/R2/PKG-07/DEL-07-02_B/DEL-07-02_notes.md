# DEL-07-02 — forward-pass notes (worker B, pass 1)

Deliverable: `DEL-07-02_Execution_Root_Scaffolding_from_Decomposition` (PKG-07). Basis: frozen tree `00115c719`.
Ledger: `DEL-07-02_claims.csv` (53 rows). Validator: `RESULT PASS errors=0 warnings=0`.

## 1. Census

Rows: 53 in total. That is 47 rows covering the 31 indexed units, plus 6 run-local rows (`REGISTER-1..5`, `STATE-1`).

| Disposition | Rows |
|---|---:|
| DOCUMENTED_UNIMPLEMENTED | 19 |
| STALE_SPECIFICATION | 13 |
| PARTIALLY_IMPLEMENTED | 11 |
| NOT_AUDITABLE | 7 |
| REMAINING_STATE_MISMATCH | 2 |
| ALIGNED | 1 |

| ClaimType × Disposition | Rows |
|---|---:|
| REQUIREMENT × DOCUMENTED_UNIMPLEMENTED | 18 |
| REQUIREMENT × PARTIALLY_IMPLEMENTED | 10 |
| ACCEPTANCE × DOCUMENTED_UNIMPLEMENTED | 1 |
| ACCEPTANCE × PARTIALLY_IMPLEMENTED | 1 |
| CONTEXT_CLAIM × NOT_AUDITABLE | 7 |
| CONTEXT_CLAIM × STALE_SPECIFICATION | 4 |
| STATE_ASSERTION × STALE_SPECIFICATION | 5 |
| STATE_ASSERTION × ALIGNED | 1 |
| STATE_ASSERTION × REMAINING_STATE_MISMATCH | 1 |
| REGISTER_DEFECT × STALE_SPECIFICATION | 4 |
| REGISTER_DEFECT × REMAINING_STATE_MISMATCH | 1 |

- **SEE rows, counted separately:** 13. Ten point to `REGISTER-1`: CLM-001, 004.3, 006, 007, 011.2, 015, 022, 025, 031 and REGISTER-5. The other three are CLM-017 → CLM-004.1, CLM-028 → CLM-003 and CLM-029 → CLM-004.2. Without them, 40 rows carry their own disposition.
- **Split rate:** 4 of 31 units were split, which is 12.9%.
  - CLM-009 has 13 rows, one for each DEL-07-02-REQ-001..013 in the table.
  - CLM-004 has 3 rows, splitting the Conditions table into containment, idempotence/recovery/lifecycle, and the source-warning row.
  - CLM-011 has 2 rows: the applicability rows, and the rows citing REF-006.
  - CLM-014 has 2 rows: AC-001, and the TBD table.
  - The `SubItems` column lists AC-001 (CLM-014) and VER-001 (CLM-021), one item each. CLM-021 therefore has a single row.
- **HumanDecisionNeeded:** `R4-Q1` on 22 rows; `NO` on 31 rows.
- **Errata:** none. This is pass 1.

## 2. Least-confident rows

There are no LOW rows. The MEDIUM rows most open to another reading are these:

- **CLM-009.11 (REQ-011) and CLM-004.1 / CLM-017: PARTIALLY_IMPLEMENTED with `NO`.**
  - What the code does: the LIVE App port checks that both paths are inside the configured project root (`runtime-daemon-harness-port.ts:602-616`). No scaffold path excludes the instruction root.
  - Alternative reading: cite `R4-Q1`, because R4-Q1 names K-ROOT.
  - Why I did not: the guard is App-side and LIVE. R4-Q1 is cited by evidence only where the sole code meeting the claim is LEGACY_ONLY.
- **CLM-009.9 (REQ-009) and CLM-008: PARTIALLY_IMPLEMENTED with `R4-Q1`.**
  - What the code does: the LIVE route exists and forwards to the Runtime, as the amended SPEC §17.1 requires, but the Runtime returns 501.
  - Alternative reading 1: DOCUMENTED_UNIMPLEMENTED, because the operation the route exposes never runs.
  - Alternative reading 2: omit R4-Q1, because the route code is LIVE.
  - Why I cited R4-Q1: the scaffolding behaviour the route should expose is met only by the unreached legacy module.
- **CLM-005 (Construction): PARTIALLY_IMPLEMENTED, judged at module level.**
  - Alternative reading: treat it as product behaviour, which would make it DOCUMENTED_UNIMPLEMENTED on the live path.
  - Why I chose module level: the table names components and their contracts.
- **CLM-010 (API result contract): PARTIALLY_IMPLEMENTED.**
  - Alternative reading: ALIGNED at the contract-type level, since `runtime-contracts` types.ts:137-151 carries every field group.
  - Why not ALIGNED: the response has no explicit "already existing" indicator, and on the live path it returns an error.
- **CLM-012 and CLM-021: PARTIALLY_IMPLEMENTED with `NO`.**
  - Alternative reading: `R4-Q1`, because every scaffold test exercises legacy code through a fake daemon port.
  - Why not: the claim is about tests, which are TEST_ONLY, not about product behaviour.

## 3. Register-defect summary

- **REGISTER-1 (STALE_SPECIFICATION): three `_REFERENCES.md` hashes marked MATCH do not reproduce.**
  - Affected: REF-002 CONTRACT, REF-003 SPEC and REF-006 PRD (`HASH-RECOMPUTE@00115c719`, pack rows `Match=NO`).
  - Hashes that do reproduce (my own `shasum -a 256` at the frozen tree): REF-001 DIRECTIVE, REF-004 TYPES, REF-005 PLAN.
  - Not checked: REF-007/009/010 are Root `workflows/` paths, outside the evidence roots.
  - How the drift happened: the D-GOV-43 tranche `23b3879b3` (2026-09-12) refreshed these hashes. Three later commits the same day then changed CONTRACT, SPEC and PRD again: `9eaddb596`, `95b342519`, `7f1e9f387`.
  - The assessment annotation (line 77) records a third REF-006 value, `ac35fba4…`.
  - REF-008 is missing from the numbering.
- **REGISTER-2 (REMAINING_STATE_MISMATCH): `_STATUS.md` header lags.**
  - It still shows Authorization Basis D-APP-19 and a CHECKING approval SHA while the state is IN_PROGRESS. D-APP-54 superseded D-APP-19 by name.
  - Last Updated is 2026-07-12.
  - There is no D-APP-127 carrier note; the application map gives `Revised=NO`.
- **REGISTER-3 (STALE_SPECIFICATION): wrong RequiredMaturity summary in `_DEPENDENCIES.md`.**
  - The summary says SEMANTIC_READY 4 and TBD 7. That totals 11 for 7 rows; the CSV has TBD 3.
  - Line 69 asserts that the counts reflect the CSV.
- **REGISTER-4 (STALE_SPECIFICATION): `Dependencies.csv` evidence references name files that do not exist.**
  - EvidenceFile and SourceRef cite `Datasheet.md`, `Procedure.md` and `Specification.md`. None of these is in the folder; the content was consolidated into `ScopeOfWork.md`.
  - DEP-07-02-004 `TargetLocation` holds a machine-specific absolute path. I have not reproduced it here.
- **REGISTER-5 (STALE_SPECIFICATION, `SEE:REGISTER-1`):** `Dependencies.csv` DEP-07-02-007 and `_DEPENDENCIES.md:44` and `:69` restate REF-006 MATCH as current.
- **Carrier propagation:** no DEL-07-02 carrier cites D-APP-127 or D-GOV-43. The SoW still describes `/api/harness/scaffold` as a working scaffold surface; see the next section.

## 4. Direction and cause

**Main finding: the product-path scaffold is not wired.**

- The chain on the live path:
  - `POST /api/harness/scaffold` (LIVE route) forwards to `RuntimeDaemonHarnessPort.scaffold`, which checks path containment.
  - That calls Runtime `/v1/projects/:id/scaffold`, which reaches `RuntimeService.scaffold`.
  - `RuntimeService.scaffold` throws `ENGINE_UNAVAILABLE` 501 because `scaffoldPort` is `undefined`. The App-owned composition leaves it undefined at `app-owned-composition.ts:226`.
- No `ProjectScaffoldPort` implementation exists anywhere under `projects/chirality-runtime/packages`.
- **How the live path lost it:**
  - The route stopped calling `scaffoldExecutionRoot` in `99fe2edae` (2026-07-23, daemon pilot). The in-process runtime host supplied the adapter from then on.
  - That host was demoted to `runtime-host-legacy.ts` ("production does not import it") in `2f825f180` (2026-09-10).
  - It was deleted in `39c0bb6ab` (2026-09-12, D-GOV-43 A2).
- **CauseTag:** `A2_TOPOLOGY` (22 rows) is the primary cause. `CAUSE2:PRE_V3_DRIFT` marks gaps that also existed before v3.
- **Parser finding (static reading, not a test run):**
  - The heading regex at `scaffold.ts:273` requires `— ` or `- ` after the package ID.
  - Every package heading in the accepted `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (for example line 353) lacks that separator.
  - Deliverable rows are attributed only under a matched heading (`:306`). The accepted decomposition therefore parses to 0 deliverables and is rejected (`:339-344`).
  - Tests use dash-heading fixtures only.
  - Cause: `PRE_V3_DRIFT`. The assessment's "accepted table shape is parsed" (REQ-013 PARTIAL) is `OVERTAKEN`.
- **Reach, and how I confirmed it:**
  - `scaffoldExecutionRoot` has no non-test caller. The route imports only the `CoordinationMode` type; `fake-daemon-harness-port.ts` is a test double.
  - `previewScaffoldExecutionRoot` is reached only from `mcp/read-tools.ts`, which the map tags LEGACY_ONLY (the Claude SDK MCP server).
  - `PipelineSurface`, the only UI caller of `scaffoldHarnessExecutionRoot`, is never rendered: `WovenDialogueRoute` discards its `legacy` element (`woven-dialogue-route.tsx:16-19`).
  - I tagged `scaffold.ts` `REACH=LEGACY_ONLY` with UNREACHED in Notes. `REACHABILITY.csv` tags it LIVE through the type-only import, so I disagree with the map.
  - Runtime-service reach follows the pack chain `standalone-bin > standalone > app-owned-composition`.
- **DirectionEvidence searches** behind the `NONE_FOUND` values:
  - `grep -i scaffold` over `_Coordination/_DECISIONS/_REGISTER.md`. It hits only D-APP-104 and D-APP-107, which are unrelated.
  - The ruling records. D-APP-29 defers a CoordinationMode/scaffold UI seed; D-APP-127 does not name scaffold.
  - CONTEXT AgentRuns: `APP_V3_*`, `APPDEV_V3_NODE_*` and `CHIRALITY_V3_APP_ADOPTION_20260909`. `APP_V3_CODEX_HOST_REPLATFORM_20260912/spike/W2_RETURN.md` lists the scaffold route as "unchanged in shape" and does not dispose of the adapter.
  - `plans/steers` and the `chirality_app_v3_*` steers do not exist in the frozen App tree.
  - `SCA-APP-008_*` has no scaffold hit.
  - Result: no record explains dropping the scaffold adapter.
  - The one GOV citation is REGISTER-2 (`GOV:D-APP-54`).
- **Authority:** amended SPEC §17.1 (D-GOV-43) still lists `/api/harness/scaffold` as a thin adapter over the Runtime socket API. PRD §7.3 and NFR-011 are unamended. So the requirement stands, and I found no AUTHORITY_CONFLICT.
- **PostReleaseBasis:** `NO` on every row.
  - None of the App files I cite appears in `TOUCHED_PATHS.csv`.
  - For the Runtime files on that list, the cited lines do not blame to any of the four commits: `app-owned-composition.ts:226` blames to `9eaddb596`; `runtime-daemon.ts:584-590`, `client.ts:613-622` and `protocol.ts:83` blame to `8b3643e6c`.

## 5. Method friction

- **Route-only claims.** A claim like "the route MUST expose X" (REQ-009) has a LIVE route that forwards to an operation met only by legacy code. Rule 3 of the subject test does not say whether "only code meeting the claim" covers a LIVE pass-through that meets part of the claim.
  - Proposal: cite R4-Q1 when the substantive behaviour is met only by LEGACY_ONLY code, even if a LIVE adapter meets the interface part.
- **Import-based reach.** `REACHABILITY.csv` treats an unmarked type-only import (`import { CoordinationMode }`) as reach.
  - Proposal: the map builder should ignore identifiers used only in type positions, or flag such modules as "type-only reach".
- **ALSO_MODULE where the module fails the accepted input.** When the legacy module works only on fixture shapes and rejects the accepted input, `ALSO_MODULE:ALIGNED` can mislead.
  - What I did: qualified it in Notes ("for parseable fixture shapes").
  - Proposal: allow `ALSO_MODULE:<verdict>(fixture)`.

## 6. Effort

- **Files read:** about 30. That includes all DEL-07-02 files except `_SEMANTIC*.md` and run records other than the 2026-07-12 one.
- **Code:** `scaffold.ts` in full, plus targeted ranges of route, port, runtime-service, composition, daemon, read-tools, woven route and the tests.
- **Governance:** SPEC §2–§3, §17.1 and §17.9, and PRD §7.3.
- **Git:** about 10 read-only `log`, `show` and `blame` calls against the frozen tree.
- **Context budget:** moderate, not tight.

## Coverage gaps

- **Output and Evaluation Matrix.** The SoW section `## Output and Evaluation Matrix` (OUT-001 → CLM-007 / AC-001 / VER-001) is not an indexed unit. Its substance is covered by CLM-014.1 (AC-001) and CLM-021 (VER-001). It maps OUT-001 to CLM-007, which is only the REF-006 header note.
- **MEMORY.md and the ADQ-06 evidence.** The 2026-06-21 entry in `MEMORY.md` and `Evidence_ADQ-06_Scaffold_Baseline_Seeding.md` state that the route is compatible. At the time the route called the module directly, so this held then; it is dated history, and no forward row owns it.
