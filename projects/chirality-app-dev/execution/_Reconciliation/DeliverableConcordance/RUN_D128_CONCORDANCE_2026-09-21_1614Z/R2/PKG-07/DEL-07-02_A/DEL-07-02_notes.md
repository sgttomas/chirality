# DEL-07-02 — forward-pass notes (worker A, PKG-07 wave 3)

Ledger: `DEL-07-02_claims.csv` (53 rows, sealed after validation). Basis: frozen tree at
`00115c719`. Reverse pass not yet run, so there is no errata file.

## 1. Census

**Rows by ClaimType × Disposition**

| ClaimType | ALIGNED | DOCUMENTED_UNIMPLEMENTED | PARTIALLY_IMPLEMENTED | STALE_SPECIFICATION | REMAINING_STATE_MISMATCH | NOT_AUDITABLE | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| REQUIREMENT | 3 | 15 | 10 | 0 | 0 | 0 | 28 |
| ACCEPTANCE | 0 | 1 | 1 | 0 | 0 | 0 | 2 |
| CONTEXT_CLAIM | 0 | 0 | 0 | 7 | 0 | 5 | 12 |
| STATE_ASSERTION | 1 | 0 | 0 | 6 | 1 | 0 | 8 |
| REGISTER_DEFECT | 0 | 0 | 0 | 3 | 0 | 0 | 3 |
| **Total** | **4** | **16** | **11** | **16** | **1** | **5** | **53** |

- **Coverage:** all 31 indexed units (CLM-001..CLM-031) are present. Run-local rows: REGISTER-1..3 and STATE-1.
- **Split rate:** 7 of 31 units split (22.6%), giving 49 unit rows.
  - CLM-009 is split into 13 rows, one per `DEL-07-02-REQ-001..013`.
  - CLM-004, 013, 020 and 025 each split in two (content row versus REF-006 row).
  - CLM-014 splits into the TBD table and AC-001.
  - CLM-021 splits into the Open Items table and VER-001.
  - SubItems: CLM-014 lists AC-001 and CLM-021 lists VER-001. Each has k = 1, and each has its own row naming the item.
- **SEE rows, counted separately:** 14.
  - The REF-006 chain has 11 rows: CLM-001 anchors on REGISTER-1, and CLM-004.2, 006, 007, 011, 013.2, 015, 020.2, 022, 025.2 and 031 point to CLM-001.
  - CLM-017 → CLM-009.11.
  - CLM-019 → CLM-012.
  - CLM-021.2 → CLM-012.
  - Non-SEE rows: 39.
- **HumanDecisionNeeded:** `NO` on all 53 rows.
  - No R4-Q1 appears. The code meeting the scaffold requirements is `REACH=TEST_ONLY`, not `LEGACY_ONLY` (see §5).
- **Confidence:** HIGH 37, MEDIUM 16, LOW 0.

## 2. Least-confident rows (with alternative readings)

There are no LOW rows. These MEDIUM rows are the most arguable:

- **CLM-009.x `HumanDecisionNeeded = NO`** (the product-behaviour DOCUMENTED_UNIMPLEMENTED rows).
  - *My reading:* SPEC §17.1 still lists `/api/harness/scaffold`, and SPEC §17 was re-expressed under D-GOV-43. The missing Runtime adapter is therefore an implementation gap.
  - *Alternative:* removing the in-process host that composed scaffolding is the R4-Q1 question in another form. On that view these rows would need an owner ruling (`R4` or `R4-Q1`) on whether scaffolding is still a live-product obligation.
  - Rule 3 cites R4-Q1 only for `LEGACY_ONLY` evidence. `scaffoldExecutionRoot` is test-only, so I did not cite it.
- **CLM-010 PARTIALLY_IMPLEMENTED (module-level API contract).**
  - *Alternative:* the claim is about the route's behaviour. On that reading it would be DOCUMENTED_UNIMPLEMENTED, because the live route only ever answers 501.
- **CLM-014.1 and CLM-021.1 STALE_SPECIFICATION.**
  - The "field names TBD" item is behind the code, because the typed contract now fixes the names.
  - *Alternative:* a lagging TBD placeholder under tie-break rule 2(b) gives REMAINING_STATE_MISMATCH. Both rows record this as `ALSO:`.
- **CLM-004.1, CLM-008 and CLM-024 PARTIALLY_IMPLEMENTED.**
  - Only the live App port's project-containment check (`runtime-daemon-harness-port.ts:606-616`) counts as live realisation.
  - *Alternative:* the operation never runs on the live path. On that view the rows are DOCUMENTED_UNIMPLEMENTED, and containment is incidental.
- **CLM-013.1, CLM-020.1 and CLM-025.1 ALIGNED at module level.**
  - These claims name artifacts or service design only.
  - *Alternative:* under rule 2 they are product behaviour and would follow CLM-009.x (DOCUMENTED_UNIMPLEMENTED).
- **STATE-1 REMAINING_STATE_MISMATCH.**
  - `## Remaining` is empty and there is no item whose status is contradicted, so I used rule 2(b), a lagging status carrier.
  - *Alternative:* a coverage-style finding with no row.

## 3. Register-defect summary

- **REGISTER-1 — hash drift.** In `_REFERENCES.md`, REF-002 (CONTRACT), REF-003 (SPEC) and REF-006 (PRD) record MATCH, but none reproduces at `00115c719`. Cited as `HASH-RECOMPUTE@00115c719` from the pack's `REFERENCE_HASHES.csv`.
  - REF-001, REF-004 and REF-005 (DIRECTIVE, TYPES, PLAN) recompute as MATCH.
  - REF-007, REF-009 and REF-010 are Root `workflows/` paths outside the evidence roots and were not checked.
  - Three different PRD hashes are in play: 8649cc… in `_REFERENCES.md`, ac35fba… in the Assessment line-77 annotation, and 17ca3f… recomputed.
  - Eleven SoW units repeat "REF-006 is MATCH under D-APP-38" as current state and point here through the CLM-001 SEE chain.
- **REGISTER-2 — dependency counts.** The `_DEPENDENCIES.md` Lifecycle Summary gives RequiredMaturity TBD = 7, SEMANTIC_READY = 4. That totals 11 against 7 rows, and `Dependencies.csv` has 3 TBD. The 2026-07-12 D-APP-56 annotation says the counts reflect the CSV, which is false.
- **REGISTER-3 — missing evidence files.**
  - `Dependencies.csv` EvidenceFile/SourceRef cite `Datasheet.md`, `Procedure.md` and `Specification.md`. None of them exists in the folder; they were removed by `a5bd9c408` (2026-07-13) when the SoW replaced the four-document kit.
  - DEP-07-02-004 TargetLocation holds a machine-specific absolute path. It is not reproduced here.
- **Also seen:**
  - `_STATUS.md` keeps the D-APP-19 authorization and Checking Approval SHA header. D-APP-54 preserves this as history, so it is not a defect row.
  - STATE-1 records that the status carrier lags the live-path change.

## 4. Direction and cause

- **Main CauseTags:**
  - `A2_TOPOLOGY` on 21 rows: the live scaffold gap, with `CAUSE2:RUNTIME_EXTRACTION` on most.
  - `PRE_V3_DRIFT` on 22 rows: the REF-006 chain, register defects, test and parser-boundary gaps, and REQ-011. The secondaries are `CAUSE2:DOC_HYGIENE` or `CAUSE2:A2_TOPOLOGY`.
  - `CARRIER_PROPAGATION` on 1 row: STATE-1.
- **Mechanism, established from code and git at the frozen basis:**
  - `route.ts` → routing port → `RuntimeDaemonHarnessPort.scaffold` (containment check) → `RuntimeClient.scaffold` → daemon `POST /v1/projects/:id/scaffold` → `RuntimeService.scaffold`.
  - `RuntimeService.scaffold` throws `ENGINE_UNAVAILABLE` 501 because `app-owned-composition.ts:226` passes `scaffoldPort = undefined`.
  - The only adapter that bound `scaffoldExecutionRoot` lived in `electron/runtime-host.ts`. `2f825f180` (2026-09-10) moved it to `runtime-host-legacy.ts`, and `39c0bb6ab` (2026-09-12, D-GOV-43 A2) deleted it.
  - Blame of `app-owned-composition.ts:226` → `9eaddb596` (2026-09-12), which is not a post-release commit.
- **CONTEXT records used:**
  - `APP_V3_CODEX_HOST_REPLATFORM_20260912/spike/W3_RETURN.md` §3 records that `runtime-host-legacy.ts` was deleted.
  - `W2_RETURN.md` §3 records that the scaffold route is "unchanged in shape".
  - Neither record says scaffolding becomes unavailable. They explain the mechanism, not a decision to drop it.
- **Searches behind `NONE_FOUND`:**
  - `_DECISIONS/_REGISTER.md`: the only scaffold hits are D-APP-104 and D-APP-107, about DEL-09-07 preflight, not this deliverable.
  - D-APP-127 ruling record.
  - `APP_V3_*`, `APPDEV_V3_NODE_*`, `CHIRALITY_V3_APP_ADOPTION_20260909`, `SCA-APP-008_*` and `SCA-APP-010_*`.
  - The done-declaration candidate: no scaffold hits.
  - Root `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` and `plans/steers/chirality_app_v3_*`: no scaffold hits.
  - `NOTICE_2026-09-19_APP_LOOP_WORKGRAPH.md:27` records the authority-corpus drift. It is not a §5 CONTEXT source, so it is mentioned only in Notes.
- **PostReleaseBasis:** `NO` on all rows.
  - `route.ts`, `scaffold.ts`, `runtime-daemon-harness-port.ts`, `runtime-service.ts` and `contracts/src/harness/types.ts` are not in `TOUCHED_PATHS.csv`.
  - Cited lines in touched files fall outside the touched ranges: `app-owned-composition.ts:226` (touched 228), `runtime-daemon.ts:584-589`, `client.ts:613-622`. Blame confirms line 226.
- **How reach was confirmed.** `REACHABILITY.csv` tags `lib/harness/scaffold.ts` LIVE via `route.ts`. That is wrong for the symbol:
  - `route.ts` imports only the `CoordinationMode` type from `scaffold.ts`.
  - `scaffoldExecutionRoot` is called only from `harness-scaffold.test.ts` and `__tests__/api/harness/fake-daemon-harness-port.ts:262`, so it is **TEST_ONLY**.
  - `previewScaffoldExecutionRoot` is reached only through `mcp/read-tools.ts`, which is LEGACY_ONLY.
  - The UI caller `scaffoldHarnessExecutionRoot` (`lib/harness/client.ts:431`) is used only by `components/pipeline/pipeline-surface.tsx`. That component is mounted only through `legacy` props that `WovenDialogueRoute` discards (`void legacy`, `woven-dialogue-route.tsx:18`). No product UI issues the request.
  - Live tags were placed on the route, the App port, the client, the daemon route, `RuntimeService.scaffold` and the app-owned composition.

## 5. Method friction

- **Subject test and TEST_ONLY evidence.** Rule 3 ties R4-Q1 to `LEGACY_ONLY` only. Here the retained implementation is test-only, because the product composition that used it was deleted.
  - The finding is the same R4-Q1 subject: retained harness code whose product wiring was removed. The rule does not reach it.
  - *Proposed revision:* when TEST_ONLY code is the only code meeting a product-behaviour claim, and a v3 topology change removed its product composition, cite R4-Q1, or give the worker a named alternative.
- **REACHABILITY map.** The map follows type-only imports written without `import type`. The scaffold route is one case, and the map tags `scaffold.ts` LIVE. Excluding identifiers used only as types would prevent this.
- **Repeated REF-006 wording.** MR-4 SEE chains work, but splitting a content row from its REF-006 bullet (CLM-004/013/020/025) inflates the row count. A unit-level "partial SEE" token would be lighter.

## 6. Effort

- **Reading:** about 25 files read in part, including:
  - the deliverable folder (8 files);
  - `scaffold.ts` in full, by ranges;
  - `route.ts`, both runtime-client ports, and the runtime service, daemon, client and contracts excerpts;
  - four test files (case lists);
  - SPEC and PRD excerpts;
  - the register, the replatform CONTEXT returns, and the gate transcripts.
- **Git:** six read-only log, show and blame calls against the frozen tree.
- **Context budget:** comfortable, not tight.

## Coverage gaps

These SoW sections have no indexed unit:

- **`## Purpose and Objective Traceability` (OUT-001).** It claims idempotence evidence and diagnostics. Its substance is covered by CLM-009.x and CLM-014.2.
- **`## Output and Evaluation Matrix`.** It links OUT-001 to CLM-007, AC-001 and VER-001.
  - The matrix's requirement reference, "CLM-007", points at the Specification header note rather than the requirements (CLM-009). This is a minor traceability defect with no owning row.
