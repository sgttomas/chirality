# DEL-05-03 notes: Redacted RunLogger and Secret Hygiene (R2 forward pass)

Run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`, PKG-05 wave 2. Frozen basis `00115c719`. Ledger:
`DEL-05-03_claims.csv` (50 rows, sealed after validation).

## 1. Census

**Rows: 50.** That is 29 indexed units (28 CLM plus REM-1) giving 44 rows, plus 6 `REGISTER-n` rows. No `STATE-n` rows.

| Disposition | Rows |
|---|---:|
| STALE_SPECIFICATION | 19 |
| PARTIALLY_IMPLEMENTED | 9 |
| IMPLEMENTED_DIFFERENTLY | 6 |
| NOT_AUDITABLE | 6 |
| DOCUMENTED_UNIMPLEMENTED | 4 |
| ALIGNED | 3 |
| UNKNOWN | 2 |
| REMAINING_STATE_MISMATCH | 1 |

| ClaimType | Rows | Dispositions |
|---|---:|---|
| REQUIREMENT | 22 | PARTIALLY_IMPLEMENTED 7, IMPLEMENTED_DIFFERENTLY 5, DOCUMENTED_UNIMPLEMENTED 4, STALE_SPECIFICATION 3, ALIGNED 3 |
| STATE_ASSERTION | 9 | STALE_SPECIFICATION 8, IMPLEMENTED_DIFFERENTLY 1 |
| CONTEXT_CLAIM | 8 | NOT_AUDITABLE 6, STALE_SPECIFICATION 2 |
| REGISTER_DEFECT | 6 | STALE_SPECIFICATION 5, REMAINING_STATE_MISMATCH 1 |
| ACCEPTANCE | 4 | PARTIALLY_IMPLEMENTED 2, UNKNOWN 2 |
| REMAINING_WORK | 1 | STALE_SPECIFICATION 1 |

- **Split rate:** 3 of 29 units were split (10.3%).
  - CLM-010 was split into 14 rows because it is a table of independently dispositionable requirements R1–R14.
  - CLM-014 was split into `.1` (AC-001) and `.2` (the narrative).
  - CLM-020 was split into `.1` (VER-001) and `.2` (the Records list).
- **SEE rows (counted separately, MR-4):** 14.
  - `SEE:REGISTER-1`: CLM-001, CLM-008, CLM-011, CLM-021, CLM-027.
  - `SEE:CLM-005`: CLM-006, CLM-013, CLM-020.2.
  - `SEE:CLM-010.1`: CLM-022, CLM-024.
  - `SEE:CLM-010.11`: CLM-023.
  - `SEE:CLM-010.14`: CLM-014.2, CLM-028.
  - `SEE:CLM-012`: CLM-019.
  - There are 36 non-SEE rows.
- **HumanDecisionNeeded:** NO 39; R4-Q1 7; `R4-Q1; R4-Q5` 2 (CLM-003, CLM-010.7); R4-Q5 2 (REM-1, REGISTER-5).
  - R4-Q5 was applied before sealing, under the RUN_BASIS Addendum 7 notice (`BRIEFS/RULE_NOTICE_ADDENDUM7.md`), which arrived before sealing.
  - REM-1 and REGISTER-5 turn on whether Codex payloads are stored as received (the schema-v2 gate is moot) or translated. They were plain R4 before the notice.
- **Confidence:** HIGH 20, MEDIUM 25, LOW 5.
- **Validator:** `RESULT PASS errors=0 warnings=0`.
- **PostReleaseBasis:** `NO` on every row.
  - The only cited file on `TOUCHED_PATHS.csv` is `projects/chirality-runtime/packages/core/src/session-store.ts`.
  - I blamed the relied-on lines. Lines 654–668 blame to `8b3643e6c` and `9b005c23a`. Lines 813–822 blame to `8b3643e6c`, `9b005c23a`, `95364569a` and `9eaddb596`.
  - None of those is one of the four post-release commits. The touched ranges in that file are 6–8 and 128–158.

## 2. Least-confident rows

- **CLM-010.14, CLM-014.2, CLM-028** (IMPLEMENTED_DIFFERENTLY, LOW). The PEC credential/cookie hygiene rests on `mcp/pec-bridge-client.ts` and `domain-proposal-tools.ts`, which are LEGACY_ONLY. No PEC transport exists on the live Runtime/Codex path, so the exclusion holds by absence, not by envelope construction.
  - Alternative readings:
    - `ALIGNED`: the property holds vacuously.
    - `DOCUMENTED_UNIMPLEMENTED`: if the D-APP-52 lane is still a live obligation.
  - This turns on R4-Q1.
- **CLM-014.1 (AC-001) and CLM-020.1 (VER-001)** (UNKNOWN, LOW). The legacy Datasheet/Specification/Guidance/Procedure sources and any parity or validation output are absent from the deliverable folder. I could not recompute migration parity.
  - Alternative: `ALIGNED` if migration run evidence outside the folder holds.
- **CLM-010.3** (MEDIUM). I judge the live run-logger use (chat-title sanitizing in `chat-organization.ts`, imported by a `'use client'` shell) to be inert in the renderer. The Electron-main key globals and non-`NEXT_PUBLIC` env are not visible there.
  - This was inferred from the import graph and `api-key-store.ts:1-31`. It was not executed.
- **CLM-010.2 / CLM-004** (IMPLEMENTED_DIFFERENTLY, MEDIUM). Custody by construction (Codex `auth.json` is never opened; App keys are in safeStorage) could also be read as `PARTIALLY_IMPLEMENTED`: no live test proves credentials are absent from `events.jsonl`.
- **CLM-010.7** (MEDIUM). The live `summary` field is preview-like. `PARTIALLY_IMPLEMENTED` is the alternative, but the raw Codex params are persisted beside it.

## 3. Register-defect summary

- **REGISTER-1.** In `_REFERENCES.md`, CONTRACT, SPEC and PRD are recorded as MATCH with Expected=Actual hashes. All three fail to reproduce (`HASH-RECOMPUTE@00115c719`).
  - The INSP-03 P40 annotation records a third PRD hash (`ac35fba4…`). It differs from both the `_REFERENCES.md` hash (`8649ccba…`) and the recomputed hash (`17ca3f3c…`).
- **REGISTER-2.** `Dependencies.csv` DEP-006/007/009 are SATISFIED on the basis of those MATCH records.
- **REGISTER-3.** The `_DEPENDENCIES.md` mirror contradicts `Dependencies.csv`:
  - DEP-009 is PENDING in the mirror but SATISFIED in the CSV.
  - DEP-011 is ACTIVE in the mirror but RETIRED in the CSV.
  - The mirror says "no accepted edges".
  - Its "current counts" block predates DEP-014.
- **REGISTER-4.** DEP-010 is still an ACTIVE interface to the Anthropic key bridge (DEL-04-05), which now has only LEGACY_ONLY code.
- **REGISTER-5.** DEP-014 waits on the "closed field vocabulary", which D-APP-127 and the amended K-EVENT-6 retired.
- **REGISTER-6.** `_STATUS.md` records no D-APP-127 application: all carriers are `NO` in the application map. Last Updated is 2026-09-03.
- **Related SoW defects:**
  - CLM-011: the D-APP-56 P40 sweep overwrote the PRD §8.5 and §8.12 Standards "Applicability" cells with the MATCH sentence.
  - CLM-017 still says "PRD has HASH_MISMATCH warning" and "no accepted edges".
  - CLM-027 is a stale conflict table.
  - CLM-007 REF-007 names `AGENT_SOFTWARE_DECOMP.md`, which does not exist at the frozen basis.

## 4. Direction and cause

- **Main finding.** The live product path is Electron, then the App-owned Runtime service, then `codex app-server`.
  - Events are persisted verbatim by `projects/chirality-runtime/packages/core/src/session-store.ts` (`appendEvent` 654–668, `persistEvent` 813–822).
  - Codex notifications carry raw upstream `params` (`delegated-engine-adapter.ts:282,289`).
  - Live redaction is limited to e-mail tokens (`codex-app-server-client.ts:44-45,70`; `electron/desktop-log.ts:60-65`) and credential-ish phrases (`electron/runtime-connectivity.ts:88-93`, `runtime-control-ipc.ts:25`, `app-update.ts:346-356`).
  - The API-key redaction stack is LEGACY_ONLY in the in-process harness: `run-logger` via `session-events`, `harness-ui-bridge`, `tool-result-artifacts`, `sdk-message-mapper`, `chirality-hooks`, and the Claude/Anthropic managers.
  - Amended CONTRACT K-EVENT-6 at the frozen basis requires "structural redaction before every sink", so the live gap is a real obligation.
  - The comment at `projects/chirality-runtime/packages/contracts/src/harness/types.ts:336` ("redacted HarnessEvent") is not true of the live path.
- **CauseTags:**
  - DOC_HYGIENE 12
  - RUNTIME_EXTRACTION 10: the decomposition moved generic run-logger ownership out of the App; the Runtime lacks the control.
  - CODEX_SOLE_ENGINE 6
  - PRE_V3_DRIFT 5: SoW TBDs overtaken by `run-logger.ts` and D-APP-67 before 2026-08-22.
  - A2_TOPOLOGY 4
  - CREDENTIAL_CUSTODY 2
  - CARRIER_PROPAGATION 2: the CLM-009 scope was not rewritten at the v3 seating re-pin; the CLM-011 cells were clobbered by the P40 sweep.
- **CAUSE2 secondaries:** A2_TOPOLOGY on RUNTIME_EXTRACTION rows; RUNTIME_EXTRACTION on CLM-005 and CLM-009; DOC_HYGIENE on CLM-011; CARRIER_PROPAGATION on REGISTER-6.
- **Records used:**
  - `GOV:D-APP-127` (topology A2; D-APP-126 custody superseded; closed vocabulary and APP-HOLD-1 retired).
  - `GOV:D-APP-67` (helper API-key-specific).
  - `CTX:plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` G-WIRE AT-025 (open secret-scan gate).
  - `CTX:` the v3 pathway-seating AgentRun.
  - `CTX:` the D-APP-56 P40 run record (CLM-011; named in `_STATUS.md`, not re-read in full).
- **NONE_FOUND searches.** For every `NONE_FOUND` I searched `_DECISIONS/_REGISTER.md` (grep for `redact`, `secret`, `DEL-05-03`, which gave the D-APP-52/67/68 rows), the D-APP-127 record, and the RUN_BASIS §5 CONTEXT list.
  - No record explains the post-D-APP-56 hash drift, the dropping of FR-034/FR-075 classification and redaction on the Codex path, or the missing PEC transport on the live path.
- **Authority.** CONTRACT K-KEY-1 (amended for Codex custody) sits above unamended SPEC §12.3 and PRD FR-031/FR-075 under DIRECTIVE §0. I applied that order and did not use `AUTHORITY_CONFLICT`.

## 5. Method friction and coverage gaps

- **Reachability.** `REACHABILITY.csv` marks `run-logger.ts` LIVE only through `chat-organization.ts`, in a client component. The module-level tag overstates the live effect. I tagged it LIVE and explained the reach in Notes.
  - Proposal: add a "client-bundle-only" hint to the pack.
- **Evidence citations.** ORN-11 (`Evidence_ORN-11_Runtime_Redaction_Path_Matrix.md`) calls its paths "live". At the frozen basis they are LEGACY_ONLY. It also cites `frontend/src/__tests__/scripts/build-network-policy.test.ts`, which was removed (`4575c73f7`, consolidated into the contract-pins manifest). ORN-11 is assessment evidence, not declared state, so it has no row. It is flagged here.
- **Coverage gap: decomposition vs SoW.** Decomposition v3.2 (L211, L338) gives DEL-05-03 "App presentation redaction plus verification of Root-runtime records; no generic run-logger ownership". The SoW requirements R1/R3/R5/R11 still assign the App a run logger. The owner of live Runtime-side redaction (a Runtime deliverable versus DEL-05-03 conformance) is not stated on an App surface.
- **Coverage gap: `_CONTEXT.md`.** It still uses "daemon" and "Root-runtime" wording (application map `NO`). I did not give it a STATE row because the pinned decomposition row uses the same words and the Runtime package is still `packages/daemon`. Flagged for the manager.
- **Not read in full.** `_SEMANTIC.md` and `_SEMANTIC_LENSING.md`, which hold no indexed units. The `_run_records/**` files were listed but not read.

## 6. Effort

- About 45 files or file slices read. The deliverable's 8 core files were read in full.
- About 20 code and test files were read in line ranges, plus the evidence-pack CSVs by script, the D-APP-127 ruling (sections), CONTRACT K-EVENT-6/K-KEY-1, SPEC §12.3 and the v3 plan AT-025 row.
- The context budget was adequate, not tight.
