# VERIFICATION — RUN_D128_CONCORDANCE_2026-09-21_1614Z, R0 calibration, unit V

> **Epistemic status:** verification evidence only. This file is **not a ruling**. It
> changes no Disposition, no ledger and no convention. CONVENTIONS_CANDIDATE.md stays a
> candidate until the owner rules at the R0 gate. Verifier verdicts are one agent reading
> checked against the frozen tree. They are not acceptance.

## Header

### Roster

All agents are Opus 5, run as Claude Code harness-native descendants (D-GOV-35) and
dispatched by the WORKING_ITEMS R0 calibration manager. The manager records parentage and
dispatch details in `RUN_STATE.jsonl` and in its returns. Every agent was fresh and
evidence-only, and none delegated.

| Agent | Unit(s) | Items | Output | Output SHA-256 |
|---|---|---:|---|---|
| V shard 1 | DEL-01-01 | 34 | `_verify/V-DEL-01-01.csv` | `8f31083f780ef89753edd610018099da6dbbbe627e1b94e5fe18a6b790fadc2f` |
| V shard 2 | DEL-02-05 | 57 | `_verify/V-DEL-02-05.csv` | `1ce31b408225fd275db059b611358f2dc9f67a6ef4347caf20fc97f520253386` |
| V shard 3 | DEL-03-01_A (double-blind side A) | 51 | `_verify/V-DEL-03-01_A.csv` | `9d4566e6def0ea452be2a96521108544bacb1cea9fdc89e8117e7a85faf6a388` |
| V shard 4 | DEL-03-01_B (double-blind side B) | 58 | `_verify/V-DEL-03-01_B.csv` | `c401df99255e5cd86068cb1c37c5aa7382c49e04748b64b6789a3d6b257e493c` |
| V shard 5 | DEL-04-05 | 61 | `_verify/V-DEL-04-05.csv` | `8bc12780b438f4c647f9d57fdef6c60a49fd63fc2f7497bcca5b2560837473fa` |
| V shard 6 | DEL-06-04 | 55 | `_verify/V-DEL-06-04.csv` | `283df94110e09892438a30c4c34de03d6d191b86af9334097d31bededfb0d075` |
| V shard 7 | DEL-08-04 | 66 | `_verify/V-DEL-08-04.csv` | `ae34207847864727c446928d6e10d6f06b61c98b9caefb43e12ab481622d493a` |
| V shard 8 | DEL-09-07 and SURFACES (class d, d+) | 41 | `_verify/V-DEL-09-07.csv` | `92e939aa4ef730803ffcec9aaa7efb7f7e6255e72d242ad017d157c0df1e9e03` |
| V shard 9 | DEL-10-01 | 43 | `_verify/V-DEL-10-01.csv` | `3a988a6ac62f0db880a2d4c1ef8dca61b2cedbc34b14d82ed8062eff3fa64cf9` |
| V aggregator (this file) | all | — | `VERIFICATION.md` | returned to manager (a file cannot contain its own hash) |

- `AGG_TABLES.md` lists the shard CSV hashes as 16-hex prefixes. The aggregator recomputed
  the full SHA-256 values above, and each one matches its AGG_TABLES prefix.
- Each shard also wrote a notes file, `_verify/V-<Unit>_notes.md`.
- Other inputs to this file:
  - `_verify/SELECTION.csv`, SHA-256 `15e10d85cdd39b0cb9470c56da907fe9fcb7b14bb4694c11d041bae5ce954db4`
    (465 items);
  - `_verify/AGG_TABLES.md`, SHA-256 `f0988e58b9e6e9c8ccf6457562f82c74e0c2fb08bc2941be30701149a7d28449`;
  - `_verify/SHARD_BRIEF.md`;
  - the run's `CONVENTIONS_CANDIDATE.md`;
  - `RUN_BASIS.md` §5.

### Source-state binding

- **Source state under review:** `main` `00115c71931bcae79909602d653740d3bb72dfa1`.
  - Every shard and the aggregator read the detached frozen reading tree at that SHA.
  - The aggregator confirmed `HEAD` = `00115c719…` on that tree.
- **Sealed inputs:** the ledger, reverse and capability files verified are the sealed files,
  with the SHA-256 values in §1.
  - The aggregator recomputed all 19 of them on 2026-09-21 and each matched §1.
  - So no sealed file changed between validation and verification.
- **Git use:** read-only `log`, `show` and `blame` on the frozen tree only.
- **Fences:** no ledger, notes, reverse, capability or shard file was edited.

### Sharding adaptation (stated plainly)

- **What the brief specified:** one fresh verifier V.
- **Why that was not feasible:** the deterministic selection (`_scripts/select_rechecks.py`)
  produced 465 recheck items, which is more than one context can check against evidence.
- **What the manager ran instead:**
  - **Nine fresh evidence-only V shards,** one per ledger unit. The double-blind DEL-03-01
    sides A and B were separate shards, and neither read the other side's folder. The
    SURFACES class d rows rode with DEL-09-07.
  - **This fresh aggregator.**
- **What did not change:** selection, verdict vocabulary (CONFIRMED / REFUTED / CONTESTED)
  and outputs are exactly the brief's.
- **One added row:** CAP-HARNESS-058 (class `d+`), added after the DEL-08-04 worker reported
  it. It makes the total 466 checks.
- **Duplicate keys:** DEL-08-04 SEC-1.1 and CLM-010.3 each appear twice (class a/b and
  class c). Each appearance is counted as a separate check.
- **Consequence:** a verdict is one shard's reading, and shards did not see each other's
  work. §4.10 records where two shards graded the same fact pattern differently.

## §1 Structural validator

The validator is `_scripts/validate_ledger.py`, run from `projects/chirality-app-dev`. The
results below are transcribed from `AGG_TABLES.md` §1. The SHA-256 values are the sealed
hashes, and the aggregator re-confirmed each one at write time.

| File | Mode | SHA-256 | Result |
|---|---|---|---|
| SURFACES/HARNESS_capabilities.csv | capabilities | `86a73c63e9539c49e016229e799eca4163d8d2afe8cc2e22bbcec80c4d15857d` | PASS, errors=0, warnings=0 |
| DEL-01-01/DEL-01-01_claims.csv | ledger | `6035419f6ccc58e43f49356b21d214e818b3e189fa05cd9d62e3e8dbe0976947` | PASS, errors=0, warnings=0 |
| DEL-02-05/DEL-02-05_claims.csv | ledger | `e923997986940bef902fb3ee5ca8fe5c20b388bc325ef41c6ce66b53da15ee89` | PASS, errors=0, warnings=0 |
| DEL-03-01_A/DEL-03-01_claims.csv | ledger | `1c922fa150d1e8246028ee47f1b321cfc2492e20778bd10045a6c969109848ec` | PASS, errors=0, warnings=0 |
| DEL-03-01_B/DEL-03-01_claims.csv | ledger | `90dd4ce1bfb3e9a622d184b7ba4057699e3a39793ea2a1ee443e263722c0478d` | PASS, errors=0, warnings=0 |
| DEL-04-05/DEL-04-05_claims.csv | ledger | `30f979c6c62af94ad27b7317c6080548e8b2f2bd13194d195b5cea39616fa737` | PASS, errors=0, warnings=0 |
| DEL-06-04/DEL-06-04_claims.csv | ledger | `befbca640d50a66c5244ded461ee68d9f0e723b2c7af9efe215ad6b63642afa4` | PASS, errors=0, warnings=0 |
| DEL-08-04/DEL-08-04_claims.csv | ledger | `243730d85a3aee2b997ae5498f2317dcafd1c2f19e62962dfe5cf220fdbbfdc8` | PASS, errors=0, warnings=0 |
| DEL-09-07/DEL-09-07_claims.csv | ledger | `f6a8363934d2a515a7a7da1d0514068dd9e7e813f364119ff7593611e520b479` | PASS, errors=0, warnings=0 |
| DEL-10-01/DEL-10-01_claims.csv | ledger | `9a646f5897ce7abfede33ed12bab48cb343a95deafe89fedb37fea4e6d348599` | PASS, errors=0, warnings=0 |
| DEL-01-01/DEL-01-01_reverse.csv | reverse | `d79a9d449e51d7f1d5a9b7372c873bb6c0c887e0764165816f355965a8d2d692` | PASS, errors=0, warnings=0 |
| DEL-02-05/DEL-02-05_reverse.csv | reverse | `5e8babbef8d787df36b94d7d9a8fd50eecaa6f1f43204ae97cc47f8df480aa6c` | PASS, errors=0, warnings=0 |
| DEL-03-01_A/DEL-03-01_reverse.csv | reverse | `ede7666f719b748b3a162baaf59382334ba10b1908e3028f6a7d254840a5f46f` | PASS, errors=0, warnings=0 |
| DEL-03-01_B/DEL-03-01_reverse.csv | reverse | `0a5997d1bc50f341f8591a842ec9065d8652192e4ab1c5945513ae5498082e8f` | PASS, errors=0, warnings=0 |
| DEL-04-05/DEL-04-05_reverse.csv | reverse | `aa538c6a16afa0946ddf27fc4a145b21e30ceb20f5ede4e6ef15c75128cb9096` | PASS, errors=0, warnings=0 |
| DEL-06-04/DEL-06-04_reverse.csv | reverse | `0c7d4d039b7d962687c6a4e65ce1199a87105de56e2961997b4984e5be4619ac` | PASS, errors=0, warnings=0 |
| DEL-08-04/DEL-08-04_reverse.csv | reverse | `8502d29db7d095e097090522f2dad98cb98bbcc518ef150c553ed8cf8d0a8f64` | PASS, errors=0, warnings=0 |
| DEL-09-07/DEL-09-07_reverse.csv | reverse | `943ab2611b478cf46da9bb5c9cd6082cfc0d7b41a257a05b35fbc31a8c45bb9a` | PASS, errors=0, warnings=0 |
| DEL-10-01/DEL-10-01_reverse.csv | reverse | `508938eeadf6be9091d7f77d7067f0f9e125b966d80e6963861e67b29d30aefa` | PASS, errors=0, warnings=0 |

**All 19 files pass structurally, with 0 errors and 0 warnings.** Structural validity does
not imply semantic correctness. §2 and §3 cover semantic correctness.

## §2 Recheck results

### Per unit

These counts were recomputed from the nine shard CSVs and agree with `AGG_TABLES.md` §2.

| Unit | Class a | Class b | Class c | Class d / d+ | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| DEL-01-01 | 28 | 5 | 1 | — | 34 | 22 | 3 | 9 |
| DEL-02-05 | 52 | 3 | 2 | — | 57 | 41 | 0 | 16 |
| DEL-03-01_A | 47 | 3 | 1 | — | 51 | 40 | 7 | 4 |
| DEL-03-01_B | 53 | 3 | 2 | — | 58 | 46 | 2 | 10 |
| DEL-04-05 | 58 | 1 | 2 | — | 61 | 56 | 3 | 2 |
| DEL-06-04 | 51 | 2 | 2 | — | 55 | 49 | 2 | 4 |
| DEL-08-04 | 57 | 7 | 2 | — | 66 | 48 | 4 | 14 |
| DEL-09-07 | 28 | 2 | — | — | 30 | 25 | 1 | 4 |
| SURFACES (HARNESS capabilities) | — | — | — | 10 + 1 | 11 | 8 | 1 | 2 |
| DEL-10-01 | 35 | 7 | 1 | — | 43 | 36 | 2 | 5 |
| **TOTAL** | **409** | **33** | **13** | **11** | **466** | **371 (79.6%)** | **25 (5.4%)** | **70 (15.0%)** |

### By selection class

| Class | Meaning | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---:|---:|---:|---:|
| a | non-ALIGNED, LOW, self-flagged or named in reverse_notes | 409 | 327 | 22 | 60 |
| b | 15% ALIGNED sample (sha256 of ClaimKey) | 33 | 25 | 2 | 6 |
| c | 20% CLAIMED_BY/PARTIAL sample | 13 | 11 | 0 | 2 |
| d | 10 capability rows | 10 | 8 | 0 | 2 |
| d+ | CAP-HARNESS-058 (added) | 1 | 0 | 1 | 0 |

### Disposition-level refutation compared with field-level refutation

442 ledger rows were checked (classes a and b).

| Level | Count | Share of 442 ledger rows | Items |
|---|---:|---:|---|
| **Disposition REFUTED** | 6 | 1.4% | DEL-03-01_B `#CLM-009.13`; DEL-04-05 `#CLM-009.14`; DEL-08-04 `#SEC-1.2` and `#CLM-016.3`; DEL-09-07 `#STATE-2`; DEL-10-01 `#REM-1` |
| **Field-level REFUTED** (Disposition holds) | 18 | 4.1% | 7 DirectionEvidence; 3 ImplementationEvidence (one also RemainingWork); 2 VerificationEvidence; 2 CauseTag; 2 AuthorityTier; 1 AssessmentEvidence; 1 PostReleaseBasis |
| **Disposition CONTESTED** | 60 | 13.6% | 59 on Disposition alone, plus DEL-03-01_B `#REM-2` (MechanicallyUnblocked and Disposition) |
| **Other field CONTESTED** | 6 | 1.4% | 3 CauseTag; 2 MechanicallyUnblocked; 1 AssessmentEvidence |

- **Capability and reverse items** (classes c, d and d+, 24 items):
  - **1 REFUTED:** CAP-HARNESS-058, whose capability text is wrong.
  - **4 CONTESTED:** 2 reverse Responses (CLAIMED_BY or PARTIAL) and 2 on granularity.
- **Reading the rates:**
  - Outright Disposition errors are rare: 6 in 442, or 1.4%.
  - Evidence-field errors are about three times as common, at 4.1%.
  - The largest category is Disposition CONTESTED, at 13.6%. It is concentrated in a few
    convention ambiguities (§4.1 and §4.5), not spread evenly.
- **The ALIGNED sample (class b):**
  - It had 0 Disposition refutations out of 33.
  - Its 2 refutations were citation-level: DEL-01-01 `#CLM-009.4` VerificationEvidence and
    DEL-08-04 `#CLM-010.3` ImplementationEvidence.
- **By unit:**
  - DEL-02-05 has the most CONTESTED items relative to its size (16), and 0 REFUTED.
  - DEL-04-05 is the cleanest unit (56 of 61 CONFIRMED).

### Aggregator spot-checks (read-only, frozen tree)

The aggregator reopened the most consequential REFUTED and CONTESTED items at `00115c719`.
Every shard reading below was reproduced.

| Item | Shard claim | Aggregator observation |
|---|---|---|
| DEL-06-04 `#CLM-009.10` PostReleaseBasis | cited Codex-path line is post-release | `git blame` of `projects/chirality-runtime/packages/daemon/src/codex-supervisor.ts:650-656` shows every line authored by `da95ec194` (2026-09-19). PostReleaseBasis should be `YES`. The shard's REFUTED holds. |
| CAP-HARNESS-058 | text describes disabled code as an executable bridge | `projects/chirality-app-dev/frontend/src/lib/harness/subagent-bridge.ts:5-9` has policy version `subagent-bridge.v4.disabled-after-managed-delegation` and a denial reason pointing to `delegate_agent`. `:84-90` shows `createExecutableSubagentBridge` returns `undefined`. `:92-116` shows the preflight always returns `allowed: false`, `hard-denied`, `executableBridge: false`. `docs/CONTRACT.md:125` (K-SUBAGENT-1) itself says "the legacy SDK adapter is disabled and fails closed". The shard's REFUTED holds. |
| DEL-03-01_A HANDOFF DirectionEvidence (6 rows) | HANDOFF L126-128 does not explain the Codex engine-conformance gap | `HANDOFF.md:126-128` removes the core "conformance, exact-supply and private-home checks" (`runtime-conformance-v2.ts` …). `git show 95364569a^:…/runtime-conformance-v2.ts` has 0 matches for `runEngineConformance` or `AgentEnginePort`. The sibling `runtime-conformance.ts` is a Runtime admission record (`ENGINE_UNAVAILABLE`), not the K-ENGINE-2 evaluator. The misgloss is real. The 95364569a commit also deleted `exact-codex-conformance.test.ts`, so a reader could argue that HANDOFF gives partial direction. The shard's reading holds, but at a lower severity (see §4.10). |
| DEL-08-04 Agent 0 hierarchy cluster | GOVERNING K-SUBAGENT-1 still says 0→1 / 1→2 | `projects/chirality-app-dev/docs/CONTRACT.md:125` reads "the 0→1 or 1→2 hierarchy". CONTESTED is appropriate. |
| DEL-02-05 Anthropic rows | GOVERNING preamble already demotes Claude/Anthropic text | `projects/chirality-app-dev/docs/PRD.md:15` and `docs/CONTRACT.md:15`: "Claude/Anthropic … describe compatibility history; they do not require shipping". CONTESTED is appropriate. |
| DEL-06-04 `#CLM-009.2`; DEL-04-05 `#CLM-009.14` | unamended K-rows versus D-GOV-43 | Three rows in `docs/CONTRACT.md` were checked. K-PATH-2 (`:100`) is unamended ("reject writes outside the active project root"). K-ENGINE-4 (`:64`) is unamended. K-EVENT-6 (`:83`) preserves upstream method names under D-GOV-43. The conflicts sit inside the GOVERNING corpus, as the shards say. |
| DEL-10-01 `#REM-1` | D-T0-23/D-PEC-56 do appear on App governing surfaces | Decomposition `DEC-019` is at `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md:628`. `projects/chirality-app-dev/docs/harness/reliance_boundary_register.md:148` marks RB-PEC-ADAPTER RETIRED, and `:169` names D-PEC-56. The shard's REFUTED holds. |

The aggregator did not re-verify the other 459 items.

## §3 Every REFUTED and CONTESTED item (95)

This section lists all 25 REFUTED and all 70 CONTESTED items, grouped by unit. No item is
dropped.

**How the table was built:**

- It was generated mechanically from the shard CSVs. Row order follows SELECTION order.
- **Key:** within a unit, `#` stands for that unit's `DEL-xx-yy#` prefix. The DEL-03-01_A
  and DEL-03-01_B keys refer to two *different* independent ledgers, so an identical key
  can name different row content.
- **Verifier reading:** for CONTESTED items it gives both readings, separated by `‖`.
  - Readings longer than about 420 characters are trimmed, marked `…`. The full text is in
    the shard CSV named in each heading.
  - The ConventionIssue column is trimmed the same way.
- **Evidence paths are kept in full,** with three prefix abbreviations:
  - `APP/` = `projects/chirality-app-dev/`;
  - `RT/` = `projects/chirality-runtime/`;
  - `DELDIR/` = the unit's own deliverable folder, given under each heading.

### DEL-01-01 (shard `V-DEL-01-01`) — 12 items

`DELDIR/` = `APP/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-01_Governance_Alignment_Human_Authority_and_Project_Truth/`

| # | Cl | Key | Verdict | Field | Ledger value | Verifier reading (CONTESTED: reading A ‖ reading B) | Evidence | Convention issue |
|---|---|---|---|---|---|---|---|---|
| 1 | a | `#CLM-003.2` | CONTESTED | Disposition | STALE_SPECIFICATION (HIGH) | STALE_SPECIFICATION (implied live PRD match false: PRD at frozen tree 17ca3f3c vs pinned 8649ccba) ‖ ALIGNED-literal: both clauses are literally true (AUTHORITY_CORPUS v23 pins 8649ccba; _REFERENCES REF-006 reads MATCH); the defect sits in the corpus snapshot and REGISTER-2; HIGH is overstated given the worker rated the parallel CLM-017.2 LOW | DELDIR/ScopeOfWork.md:57; DELDIR/_REFERENCES.md:12; APP/execution/_Reconciliation/References/AUTHORITY_CORPUS.json (current_version v23); APP/docs/PRD.md (sha256 17ca3f3c) | MR-8 ambiguous for literally-true snapshot claims; worker inconsistent vs CLM-017.2 |
| 2 | a | `#CLM-004.1` | CONTESTED | Disposition | ALIGNED (HIGH) | ALIGNED/HIGH (documentary requirement; transition rules HUMAN-only) ‖ PARTIALLY_IMPLEMENTED or ALIGNED/MEDIUM: human-only is a declared-actor check (normalizeActor maps HUMAN/USER/OPERATOR; approvalSha checked for hex format only) and the legacy MCP status_transition tool accepts an agent-supplied actor string; that tool has no production importer outside lib/harness (CAP-HARNESS-051 LEGACY-IN-PROCESS) so live exposu … | APP/frontend/src/lib/lifecycle/transition.ts:24-29; APP/frontend/src/lib/lifecycle/transition.ts:65-72; APP/frontend/src/lib/lifecycle/transition.ts:170-175; APP/frontend/src/lib/harness/mcp/read-tools.ts:934-942; APP/frontend/src/lib/harness/mcp/read-tools.ts:1125-1136; APP/frontend/src/__tests__/lib/chirality-mutating-mcp.test.ts:206 | reverse-notes correction not in sealed ledger (by design) |
| 3 | a | `#CLM-008` | REFUTED | DirectionEvidence | projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-09-19_APP_LOOP_WORKGRAPH.md | NONE_FOUND: the notice is not a RUN_BASIS s5 CONTEXT source (worker says so itself); Disposition PARTIALLY_IMPLEMENTED and CauseTag A2_TOPOLOGY otherwise hold (K-EVENT-4 vs SPEC s8.2/PRD FR-121 inconsistency and corpus drift verified) | DELDIR/ScopeOfWork.md:113; APP/docs/CONTRACT.md:81; APP/docs/SPEC.md:506-509; APP/docs/PRD.md:819; APP/execution/_Coordination/NOTICE_2026-09-19_APP_LOOP_WORKGRAPH.md:27 | CONTEXT-only DirectionEvidence |
| 4 | a | `#CLM-009.2` | CONTESTED | Disposition | ALIGNED (HIGH) | ALIGNED/HIGH (documentary requirement; transition rules HUMAN-only) ‖ PARTIALLY_IMPLEMENTED or ALIGNED/MEDIUM: human-only is a declared-actor check (normalizeActor maps HUMAN/USER/OPERATOR; approvalSha checked for hex format only) and the legacy MCP status_transition tool accepts an agent-supplied actor string; that tool has no production importer outside lib/harness (CAP-HARNESS-051 LEGACY-IN-PROCESS) so live exposu … | APP/frontend/src/lib/lifecycle/transition.ts:24-29; APP/frontend/src/lib/lifecycle/transition.ts:65-72; APP/frontend/src/lib/lifecycle/transition.ts:170-175; APP/frontend/src/lib/harness/mcp/read-tools.ts:934-942; APP/frontend/src/lib/harness/mcp/read-tools.ts:1125-1136; APP/frontend/src/__tests__/lib/chirality-mutating-mcp.test.ts:206; APP/docs/CONTRACT.md:41 | reverse-notes correction not in sealed ledger (by design) |
| 5 | a | `#CLM-009.7` | CONTESTED | Disposition | ALIGNED (LOW) | ALIGNED (K-ENGINE-4 keeps HarnessEvent/governance records Chirality-owned) ‖ STALE_SPECIFICATION/CODEX_SOLE_ENGINE (K-EVENT-1 browser stream preserves upstream Codex method names and payloads; privileged-but-replaceable SDK framing vs Codex sole engine K-ENGINE-3); VerificationEvidence also cites the legacy frontend session-events test rather than a Runtime event-schema test | DELDIR/ScopeOfWork.md:132; APP/docs/CONTRACT.md:63-64; APP/docs/CONTRACT.md:78; APP/frontend/src/__tests__/lib/session-events.test.ts:21 | - |
| 6 | a | `#CLM-009.11` | REFUTED | AssessmentEvidence | STILL CURRENT (INSP-03 REQ-005 PASS cited project-local path) | NOT APPLICABLE (no direct conclusion on the path clause): INSP-03 REQ-005 PASS cites CONTRACT lines 69-75 and runtime_engine_contract only and does not cite the events.jsonl path; STILL CURRENT also contradicts the row own STALE_SPECIFICATION of that clause. Disposition STALE_SPECIFICATION and CauseTag A2_TOPOLOGY hold | DELDIR/Assessment_INSP-03_DEL-01-01.md:27; DELDIR/ScopeOfWork.md:130; APP/docs/CONTRACT.md:81 | MR-1 AssessmentEvidence token |
| 7 | a | `#CLM-015` | CONTESTED | Disposition | STALE_SPECIFICATION (MEDIUM) | STALE_SPECIFICATION (implied live PRD match false: PRD at frozen tree 17ca3f3c vs pinned 8649ccba) ‖ ALIGNED-literal: both clauses are literally true (AUTHORITY_CORPUS v23 pins 8649ccba; _REFERENCES REF-006 reads MATCH); the defect sits in the corpus snapshot and REGISTER-2; MEDIUM is apt | DELDIR/ScopeOfWork.md:210; DELDIR/_REFERENCES.md:12 | MR-8 ambiguous for literally-true snapshot claims |
| 8 | a | `#CLM-017.2` | CONTESTED | Disposition | STALE_VERIFICATION (LOW) | STALE_VERIFICATION (cell no longer reflects the tree) ‖ ALIGNED (pass condition only requires the _REFERENCES cell to read MATCH which it does); worker self-flag stands | DELDIR/ScopeOfWork.md:274; DELDIR/_REFERENCES.md:12 | MR-8 / STALE_VERIFICATION boundary |
| 9 | a | `#CLM-017.3` | CONTESTED | Disposition | DOCUMENTED_UNIMPLEMENTED / OTHER:PENDING_HUMAN_GATE | DOCUMENTED_UNIMPLEMENTED (no human approval record exists) ‖ NOT_AUDITABLE or ALIGNED: the pass condition is conditional on outputs being used as acceptance evidence; none is (artifacts self-label as agent findings; lifecycle IN_PROGRESS); worker own note says not a defect. Evidence cited (Checking Approval SHA 8c6d55d3 is D-APP-19 basis) verified | DELDIR/ScopeOfWork.md:279; DELDIR/_STATUS.md:5-7; DELDIR/Checklist_Runtime_Audit_DEL-01-01.md:10-12 | OTHER token PENDING_HUMAN_GATE (report); conditional pass conditions |
| 10 | a | `#CLM-023` | CONTESTED | Disposition | STALE_SPECIFICATION / CODEX_SOLE_ENGINE (LOW) | STALE_SPECIFICATION (stock Codex App Server; user-chosen policy) ‖ ALIGNED: governing CONTRACT K-PERM-2/K-PERM-3 still name permission overlay and hooks as enforcement and delegated.ts keeps a Chirality-owned fixed mode-to-policy mapping; the stale reading rests on a CONTEXT steer and the text is a recommended posture not a flat state assertion; cited anchor delegated.ts:317-329 is actually 316-329 | DELDIR/ScopeOfWork.md:345; APP/docs/CONTRACT.md:91-92; RT/packages/contracts/src/delegated.ts:316-329; plans/steers/chirality_app_v3_codex_host_replatform_direction_2026-09-11.md | CONTEXT must not drive Disposition; MR-8 for guidance rows |
| 11 | b | `#CLM-009.4` | REFUTED | VerificationEvidence | DOC-BASIS(D-APP-127) | DOC-BASIS naming the decision behind the current K-FS-1/K-NOMEM-1 wording (blame 416b29033 2026-07-23; D-APP-127 publication is 2026-09-12 and does not touch these rows); Disposition ALIGNED and the CONTRACT citation hold | APP/docs/CONTRACT.md:33; APP/docs/CONTRACT.md:35 | MR-10 DOC-BASIS token misattributed |
| 12 | b | `#CLM-021` | CONTESTED | Disposition | ALIGNED (MEDIUM) | ALIGNED/MEDIUM (principles documented; P1 enforced by HUMAN-only transition rules) ‖ PARTIALLY_IMPLEMENTED or ALIGNED/MEDIUM: human-only is a declared-actor check (normalizeActor maps HUMAN/USER/OPERATOR; approvalSha checked for hex format only) and the legacy MCP status_transition tool accepts an agent-supplied actor string; that tool has no production importer outside lib/harness (CAP-HARNESS-051 LEGACY-IN-PROCESS) … | APP/frontend/src/lib/lifecycle/transition.ts:24-29; APP/frontend/src/lib/lifecycle/transition.ts:65-72; APP/frontend/src/lib/lifecycle/transition.ts:170-175; APP/frontend/src/lib/harness/mcp/read-tools.ts:934-942; APP/frontend/src/lib/harness/mcp/read-tools.ts:1125-1136; APP/frontend/src/__tests__/lib/chirality-mutating-mcp.test.ts:206 | - |

### DEL-02-05 (shard `V-DEL-02-05`) — 16 items

`DELDIR/` = `APP/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback/`

| # | Cl | Key | Verdict | Field | Ledger value | Verifier reading (CONTESTED: reading A ‖ reading B) | Evidence | Convention issue |
|---|---|---|---|---|---|---|---|---|
| 13 | a | `#SEC-1.4` | CONTESTED | Disposition | PARTIALLY_IMPLEMENTED / UNRECORDED_JUDGMENT | PARTIALLY_IMPLEMENTED / UNRECORDED_JUDGMENT (labels only in the unmounted consent module) ‖ UNKNOWN: the K-ROLE-2 label obligation is conditional on G-ROLE failing, which the row could not establish; Opt-in Preview appears only in the decomposition row and SoW, not in CONTRACT/PRD; D-APP-127 keeps the labelled fake states as presentation, so absence may reflect the retired consent module (A2_TOPOLOGY) | APP/docs/CONTRACT.md:229; APP/frontend/src/lib/consent/hosted-engine-consent-port.ts:42,188; APP/frontend/src/components/settings/settings-view.tsx:31-35 | LOW self-flag justified; UNRECORDED_JUDGMENT vs UNKNOWN ambiguity when a conditional obligation cannot be evaluated |
| 14 | a | `#SEC-2.2` | CONTESTED | Disposition | IMPLEMENTED_DIFFERENTLY / CODEX_SOLE_ENGINE / R4 | IMPLEMENTED_DIFFERENTLY + R4 (Q7 barred an OpenAI status indicator and the hosted row shows Signed in plus readiness) ‖ STALE_SPECIFICATION / A2_TOPOLOGY + D-APP-127: the GOVERNING D-APP-127 replacement of D-APP-122 says the account row and Settings act on Codex own login flow, and local-model status is compatibility history under the sole-engine preamble | APP/frontend/src/components/shell/account-row.tsx:57-68; APP/frontend/src/components/settings/hosted-bootstrap-view.tsx:92-103; APP/execution/_Coordination/_DECISIONS/D-APP-127_RULING_APPLICATION_D-GOV-43_CODEX_HOST_REPLATFORM_A2_2026-09-12.md:105-117 | LOW self-flag justified |
| 15 | a | `#SEC-2.5` | CONTESTED | Disposition | PARTIALLY_IMPLEMENTED / UNRECORDED_JUDGMENT | PARTIALLY_IMPLEMENTED / UNRECORDED_JUDGMENT (labels only in the unmounted consent module) ‖ UNKNOWN: the K-ROLE-2 label obligation is conditional on G-ROLE failing, which the row could not establish; Opt-in Preview appears only in the decomposition row and SoW, not in CONTRACT/PRD; D-APP-127 keeps the labelled fake states as presentation, so absence may reflect the retired consent module (A2_TOPOLOGY) | APP/docs/CONTRACT.md:229; APP/frontend/src/lib/consent/hosted-engine-consent-port.ts:42,188; APP/frontend/src/components/settings/settings-view.tsx:31-35 | LOW self-flag justified; same ambiguity as SEC-1.4 |
| 16 | a | `#CLM-001` | CONTESTED | Disposition | NOT_AUDITABLE / NONE | NOT_AUDITABLE as a dated 2026-07-12 note ‖ STALE_SPECIFICATION / DOC_HYGIENE: the note asserts REF-006 docs/PRD.md is MATCH, but at 00115c719 docs/PRD.md hashes 17ca3f3c... against expected 8649ccba... in _REFERENCES.md (REF-002 CONTRACT and REF-003 SPEC also mismatch); checkable, not nothing-to-check | DELDIR/_REFERENCES.md:8-12; APP/docs/PRD.md (sha256 17ca3f3c at 00115c719) | AssessmentEvidence: assessment discussed REF-006 HASH_MISMATCH (Assessment_INSP-03_DEL-02-05.md:45) so OVERTAKEN not NOT APPLICABLE (as CLM-027 did); missed register defe … |
| 17 | a | `#CLM-003` | CONTESTED | Disposition | IMPLEMENTED_DIFFERENTLY / R4 | STALE_SPECIFICATION (CODEX_SOLE_ENGINE; HumanDecisionNeeded NO) because the GOVERNING PRD preamble and CONTRACT preamble already declare Anthropic key descriptions compatibility history that need not ship, so the SoW wording is stale against the governing map (MR-11) ‖ IMPLEMENTED_DIFFERENTLY + R4 as recorded (panel exists but unmounted on the hosted path) | APP/docs/PRD.md:15; APP/docs/CONTRACT.md:15; APP/frontend/src/components/settings/settings-view.tsx:31-35; APP/frontend/electron/api-key-storage.ts:227-251 | AuthorityTier: cited SPEC/TYPES sections make the highest restated tier GOVERNANCE_INVARIANT, not PRD; R4 rationale (PRD FR-030 still carries the requirement) omits the g … |
| 18 | a | `#CLM-006` | CONTESTED | Disposition | NOT_AUDITABLE / NONE | NOT_AUDITABLE as a dated 2026-07-12 note ‖ STALE_SPECIFICATION / DOC_HYGIENE: the note asserts REF-006 docs/PRD.md is MATCH, but at 00115c719 docs/PRD.md hashes 17ca3f3c... against expected 8649ccba... in _REFERENCES.md (REF-002 CONTRACT and REF-003 SPEC also mismatch); checkable, not nothing-to-check | DELDIR/_REFERENCES.md:8-12; APP/docs/PRD.md (sha256 17ca3f3c at 00115c719); DELDIR/ScopeOfWork.md:167 | AssessmentEvidence: assessment discussed REF-006 HASH_MISMATCH (Assessment_INSP-03_DEL-02-05.md:45) so OVERTAKEN not NOT APPLICABLE (as CLM-027 did); missed register defe … |
| 19 | a | `#CLM-009.1` | CONTESTED | Disposition | IMPLEMENTED_DIFFERENTLY / R4 | STALE_SPECIFICATION (CODEX_SOLE_ENGINE; HumanDecisionNeeded NO) because the GOVERNING PRD preamble and CONTRACT preamble already declare Anthropic key descriptions compatibility history that need not ship, so the SoW wording is stale against the governing map (MR-11) ‖ IMPLEMENTED_DIFFERENTLY + R4 as recorded (panel exists but unmounted on the hosted path) | APP/docs/PRD.md:15; APP/frontend/src/components/settings/settings-view.tsx:31-35; DELDIR/ScopeOfWork.md:203-209 | - |
| 20 | a | `#CLM-010.1` | CONTESTED | Disposition | IMPLEMENTED_DIFFERENTLY / R4 | STALE_SPECIFICATION (CODEX_SOLE_ENGINE; HumanDecisionNeeded NO) because the GOVERNING PRD preamble and CONTRACT preamble already declare Anthropic key descriptions compatibility history that need not ship, so the SoW wording is stale against the governing map (MR-11) ‖ IMPLEMENTED_DIFFERENTLY + R4 as recorded (panel exists but unmounted on the hosted path) | APP/docs/PRD.md:15; APP/frontend/electron/api-key-ipc.ts:204-218; APP/frontend/src/components/settings/settings-view.tsx:31-35 | AuthorityTier: cited SPEC/TYPES sections make the highest restated tier GOVERNANCE_INVARIANT, not PRD (SPEC 16.2) |
| 21 | a | `#CLM-010.2` | CONTESTED | Disposition | IMPLEMENTED_DIFFERENTLY / R4 | STALE_SPECIFICATION (CODEX_SOLE_ENGINE; HumanDecisionNeeded NO) because the GOVERNING PRD preamble and CONTRACT preamble already declare Anthropic key descriptions compatibility history that need not ship, so the SoW wording is stale against the governing map (MR-11) ‖ IMPLEMENTED_DIFFERENTLY + R4 as recorded (panel exists but unmounted on the hosted path) | APP/docs/PRD.md:15; APP/frontend/src/components/settings/api-key-settings.tsx:10,255-268; APP/frontend/src/components/settings/settings-view.tsx:31-35 | AuthorityTier: cited SPEC/TYPES sections make the highest restated tier GOVERNANCE_INVARIANT, not PRD (SPEC 16.2) |
| 22 | a | `#CLM-010.3` | CONTESTED | Disposition | IMPLEMENTED_DIFFERENTLY / R4 | STALE_SPECIFICATION (CODEX_SOLE_ENGINE; HumanDecisionNeeded NO) because the GOVERNING PRD preamble and CONTRACT preamble already declare Anthropic key descriptions compatibility history that need not ship, so the SoW wording is stale against the governing map (MR-11) ‖ IMPLEMENTED_DIFFERENTLY + R4 as recorded (panel exists but unmounted on the hosted path); reverse note (second resolver in lib/harness/api-key-store.t … | APP/docs/PRD.md:15; APP/frontend/electron/api-key-storage.ts:227-251; APP/docs/PRD.md:640 | AuthorityTier: cited SPEC/TYPES sections make the highest restated tier GOVERNANCE_INVARIANT, not PRD (SPEC 12.3) |
| 23 | a | `#CLM-010.10` | CONTESTED | Disposition | STALE_SPECIFICATION / FACADE_DEPRECATION / HIGH / HDN NO | STALE_SPECIFICATION (FACADE_DEPRECATION) ‖ ALIGNED in substance: @chirality/harness-contract still exists as a deprecated re-export of the same type and D-APP-118 facade retirement is AWAITING_RULING, so the text is not flatly false; LatestDecision should cite D-APP-118 (context) and HumanDecisionNeeded D-APP-118; HIGH confidence overstated | APP/frontend/packages/harness-contract/src/types.ts:1-2; APP/frontend/src/lib/harness/error-display.ts:2; APP/execution/_Coordination/_DECISIONS/_REGISTER.md:135 | MR-8: STALE_SPECIFICATION needs a now-false state; a deprecated-but-live facade is not |
| 24 | a | `#CLM-013.4` | CONTESTED | Disposition | STALE_SPECIFICATION / A2_TOPOLOGY (RemainingWork: remove or mark retired) | STALE_SPECIFICATION for the per-root form ‖ IMPLEMENTED_DIFFERENTLY: GOVERNING K-NET-1 keeps the three postures, read as the user Codex configuration and sandbox choice shown in the composer, and the composer permission selector implements that; RemainingWork should be restate, not remove; ImplementationEvidence misses the composer selector | APP/docs/CONTRACT.md:134; APP/frontend/src/components/shell/chat-panel.tsx:119-139; APP/frontend/src/lib/consent/hosted-engine-consent-port.ts | Deliverable text judged against GOVERNING map: K-NET-1 adapts (family 3) rather than retires the postures |
| 25 | a | `#CLM-013.5` | CONTESTED | Disposition | PARTIALLY_IMPLEMENTED / UNRECORDED_JUDGMENT | PARTIALLY_IMPLEMENTED / UNRECORDED_JUDGMENT (labels only in the unmounted consent module) ‖ UNKNOWN: the K-ROLE-2 label obligation is conditional on G-ROLE failing, which the row could not establish; Opt-in Preview appears only in the decomposition row and SoW, not in CONTRACT/PRD; D-APP-127 keeps the labelled fake states as presentation, so absence may reflect the retired consent module (A2_TOPOLOGY) | APP/docs/CONTRACT.md:229; APP/frontend/src/lib/consent/hosted-engine-consent-port.ts:42,188; APP/frontend/src/components/settings/settings-view.tsx:31-35 | LOW self-flag justified; same ambiguity as SEC-1.4 |
| 26 | a | `#CLM-014` | CONTESTED | Disposition | NOT_AUDITABLE / NONE | NOT_AUDITABLE as a dated 2026-07-12 note ‖ STALE_SPECIFICATION / DOC_HYGIENE: the note asserts REF-006 docs/PRD.md is MATCH, but at 00115c719 docs/PRD.md hashes 17ca3f3c... against expected 8649ccba... in _REFERENCES.md (REF-002 CONTRACT and REF-003 SPEC also mismatch); checkable, not nothing-to-check | DELDIR/_REFERENCES.md:8-12; APP/docs/PRD.md (sha256 17ca3f3c at 00115c719); DELDIR/ScopeOfWork.md:305 | AssessmentEvidence: assessment discussed REF-006 HASH_MISMATCH (Assessment_INSP-03_DEL-02-05.md:45) so OVERTAKEN not NOT APPLICABLE (as CLM-027 did); missed register defe … |
| 27 | a | `#CLM-021` | CONTESTED | Disposition | NOT_AUDITABLE / NONE | NOT_AUDITABLE as a dated 2026-07-12 note ‖ STALE_SPECIFICATION / DOC_HYGIENE: the note asserts REF-006 docs/PRD.md is MATCH, but at 00115c719 docs/PRD.md hashes 17ca3f3c... against expected 8649ccba... in _REFERENCES.md (REF-002 CONTRACT and REF-003 SPEC also mismatch); checkable, not nothing-to-check | DELDIR/_REFERENCES.md:8-12; APP/docs/PRD.md (sha256 17ca3f3c at 00115c719); DELDIR/ScopeOfWork.md:417 | AssessmentEvidence: assessment discussed REF-006 HASH_MISMATCH (Assessment_INSP-03_DEL-02-05.md:45) so OVERTAKEN not NOT APPLICABLE (as CLM-027 did); missed register defe … |
| 28 | c | `#CLM-010.6 / CAP-HARNESS-013` | CONTESTED | Response | CLAIMED_BY DEL-02-05#CLM-010.6 | CLAIMED_BY ‖ PARTIAL: the capability also persists per-chat model/reasoning pair, unsent permission and interaction mode, which R06 retry preservation does not own | APP/frontend/src/lib/harness/chat-draft.ts; APP/execution/_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/R0_CALIBRATION/SURFACES/HARNESS_capabilities.csv (CAP-HARNESS-013) | Capability granularity broader than the claim; PARTIAL criterion unclear |

### DEL-03-01_A (shard `V-DEL-03-01_A`) — 11 items

`DELDIR/` = `APP/execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/DEL-03-01_AgentEnginePort_and_Engine_Conformance_Suite/`

| # | Cl | Key | Verdict | Field | Ledger value | Verifier reading (CONTESTED: reading A ‖ reading B) | Evidence | Convention issue |
|---|---|---|---|---|---|---|---|---|
| 29 | a | `#CLM-003.4` | REFUTED | DirectionEvidence | projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/HANDOFF.md … | NONE_FOUND; HANDOFF L126-128 removed core runtime-conformance-v2.ts, which (git show 95364569a^) is payload/native-profile/supply conformance with no engine-conformance content; it does not explain why the Codex adapter is not an engine-conformance subject. DirectionEvidence should be NONE_FOUND (GOVERNING replacement: K-ENGINE-3 and VALIDATION_STRATEGY S-1..S-8 on the production path). Disposition and CauseTag CODEX … | DELDIR/ScopeOfWork.md:60-61; RT/packages/contracts/src/harness/engine-conformance.ts:483,502; RT/packages/daemon/src/app-owned-composition.ts:214; APP/execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/HANDOFF.md:126-128; APP/docs/CONTRACT.md:62-63; APP/docs/VALIDATION_STRATEGY.md:125 | CONTEXT DirectionEvidence misattributed |
| 30 | a | `#CLM-009.8` | CONTESTED | Disposition | DOCUMENTED_UNIMPLEMENTED | DOCUMENTED_UNIMPLEMENTED (K-ENGINE-2 unmet: Codex default never run through runEngineConformance) ‖ PARTIALLY_IMPLEMENTED (GOVERNING K-ENGINE-3 and VALIDATION_STRATEGY name the S-1..S-8 functional checks on the production path as the Codex-era enforcement; Runtime native-event/codex-attachment adapter tests exist). Either way DirectionEvidence is wrong: HANDOFF L126-128 removed core runtime-conformance-v2.ts, which ( … | DELDIR/ScopeOfWork.md:152; APP/docs/CONTRACT.md:62-63; APP/docs/VALIDATION_STRATEGY.md:125; RT/packages/daemon/src/app-owned-composition.ts:214; APP/execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/HANDOFF.md:126-128 | CONTEXT DirectionEvidence misattributed; LOW self-flag genuinely two-sided |
| 31 | a | `#CLM-009.10` | CONTESTED | CauseTag | CODEX_SOLE_ENGINE | CODEX_SOLE_ENGINE (Codex adapter not a subject) ‖ PRE_V3_DRIFT (the missing session-resume case predates v3; INSP-03 REQ-010 was already PARTIAL on 2026-06-20) | DELDIR/ScopeOfWork.md:154; RT/packages/contracts/src/harness/engine-conformance.ts:11-44 (no resume code); DELDIR/Assessment_INSP-03_DEL-03-01.md:53 | Single CauseTag cannot express a residual with two causes |
| 32 | a | `#CLM-010` | CONTESTED | Disposition | NOT_AUDITABLE | NOT_AUDITABLE (applicability list) ‖ STALE_SPECIFICATION/DOC_HYGIENE (the PRD row asserts 'REF-006 is reconciled under D-APP-38' which is false by hash, same fact as CLM-004.6; worker treated similar CONTEXT_CLAIM assertions in CLM-023/025 as STALE) | DELDIR/ScopeOfWork.md:173; DELDIR/_REFERENCES.md:12 | CONTEXT_CLAIM with embedded state assertion; NOT_AUDITABLE vs STALE inconsistently applied |
| 33 | a | `#CLM-011` | REFUTED | DirectionEvidence | projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/HANDOFF.md … | NONE_FOUND; HANDOFF L126-128 removed core runtime-conformance-v2.ts, which (git show 95364569a^) is payload/native-profile/supply conformance with no engine-conformance content; it does not explain why the Codex adapter is not an engine-conformance subject. DirectionEvidence should be NONE_FOUND (GOVERNING replacement: K-ENGINE-3 and VALIDATION_STRATEGY S-1..S-8 on the production path). Disposition and CauseTag CODEX … | DELDIR/ScopeOfWork.md:184; APP/execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/HANDOFF.md:126-128; APP/docs/CONTRACT.md:62-63; APP/docs/VALIDATION_STRATEGY.md:125 | CONTEXT DirectionEvidence misattributed |
| 34 | a | `#CLM-013.2` | REFUTED | DirectionEvidence | projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/HANDOFF.md … | NONE_FOUND; HANDOFF L126-128 removed core runtime-conformance-v2.ts, which (git show 95364569a^) is payload/native-profile/supply conformance with no engine-conformance content; it does not explain why the Codex adapter is not an engine-conformance subject. DirectionEvidence should be NONE_FOUND (GOVERNING replacement: K-ENGINE-3 and VALIDATION_STRATEGY S-1..S-8 on the production path). Disposition and CauseTag CODEX … | DELDIR/ScopeOfWork.md:223; RT/packages/daemon/src/app-owned-composition.ts:214; APP/execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/HANDOFF.md:126-128; APP/docs/CONTRACT.md:62-63; APP/docs/VALIDATION_STRATEGY.md:125 | CONTEXT DirectionEvidence misattributed |
| 35 | a | `#CLM-018` | REFUTED | DirectionEvidence | projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/HANDOFF.md … | NONE_FOUND; HANDOFF L126-128 removed core runtime-conformance-v2.ts, which (git show 95364569a^) is payload/native-profile/supply conformance with no engine-conformance content; it does not explain why the Codex adapter is not an engine-conformance subject. DirectionEvidence should be NONE_FOUND (GOVERNING replacement: K-ENGINE-3 and VALIDATION_STRATEGY S-1..S-8 on the production path). Disposition and CauseTag CODEX … | DELDIR/ScopeOfWork.md:303-312; RT/packages/contracts/src/harness/engine-conformance.ts:468; APP/execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/HANDOFF.md:126-128; APP/docs/CONTRACT.md:62-63; APP/docs/VALIDATION_STRATEGY.md:125 | CONTEXT DirectionEvidence misattributed |
| 36 | a | `#CLM-019` | REFUTED | DirectionEvidence | projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/HANDOFF.md … | NONE_FOUND; HANDOFF L126-128 removed core runtime-conformance-v2.ts, which (git show 95364569a^) is payload/native-profile/supply conformance with no engine-conformance content; it does not explain why the Codex adapter is not an engine-conformance subject. DirectionEvidence should be NONE_FOUND (GOVERNING replacement: K-ENGINE-3 and VALIDATION_STRATEGY S-1..S-8 on the production path). Disposition and CauseTag CODEX … | DELDIR/ScopeOfWork.md:319-327; APP/frontend/scripts/harness-section9-manifest.json:10-14; APP/execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/HANDOFF.md:126-128; APP/docs/CONTRACT.md:62-63; APP/docs/VALIDATION_STRATEGY.md:125 | CONTEXT DirectionEvidence misattributed |
| 37 | a | `#CLM-022` | REFUTED | DirectionEvidence | projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/HANDOFF.md … | NONE_FOUND; HANDOFF L126-128 removed core runtime-conformance-v2.ts, which (git show 95364569a^) is payload/native-profile/supply conformance with no engine-conformance content; it does not explain why the Codex adapter is not an engine-conformance subject. DirectionEvidence should be NONE_FOUND (GOVERNING replacement: K-ENGINE-3 and VALIDATION_STRATEGY S-1..S-8 on the production path). Disposition and CauseTag CODEX … | DELDIR/ScopeOfWork.md:356; APP/execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/HANDOFF.md:126-128; APP/docs/CONTRACT.md:62-63; APP/docs/VALIDATION_STRATEGY.md:125 | CONTEXT DirectionEvidence misattributed |
| 38 | a | `#CLM-025` | REFUTED | CauseTag | A2_TOPOLOGY | PRE_V3_DRIFT: the stale parts are the optional interrupt? (SPEC 10.2 made interrupt required on 2026-07-22, git 4412157d1, same cause as CLM-003.2/009.4) and adapter-side turn.accepted (TurnEngine/coordinator placement recorded pre-v3 in SPEC 10.2 and runtime_engine_contract.md L3-6); nothing in the example depends on the A2 topology | DELDIR/ScopeOfWork.md:393-403; APP/docs/SPEC.md:667,671; RT/packages/core/src/turn-coordinator.ts:228-234 | CauseTag vocabulary misapplied (A2_TOPOLOGY is App-owned service topology) |
| 39 | a | `#REM-2` | CONTESTED | MechanicallyUnblocked | YES | YES (gate 'socket API lands on the production path' verified in App code: runtime-service-host.ts control.sock, turn route via getDaemonHarnessPort, composition :214) ‖ UNKNOWN (MR-6: gate status for Runtime-owned work only from App status surfaces; no App status surface records the gate satisfied and _STATUS still carries NOT_SELECTABLE_UNTIL). Disposition REMAINING_STATE_MISMATCH and A2_TOPOLOGY hold | DELDIR/_STATUS.md:15-22; APP/frontend/electron/runtime-service-host.ts:37; APP/frontend/src/app/api/harness/turn/route.ts:13-23; RT/packages/daemon/src/app-owned-composition.ts:214 | MR-2/MR-6 ambiguity: does App code count as an App surface for a Runtime-owned gate (worker self-flagged) |

### DEL-03-01_B (shard `V-DEL-03-01_B`) — 12 items

`DELDIR/` = `APP/execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/DEL-03-01_AgentEnginePort_and_Engine_Conformance_Suite/`

| # | Cl | Key | Verdict | Field | Ledger value | Verifier reading (CONTESTED: reading A ‖ reading B) | Evidence | Convention issue |
|---|---|---|---|---|---|---|---|---|
| 40 | a | `#CLM-004.1` | CONTESTED | Disposition | AUTHORITY_CONFLICT | AUTHORITY_CONFLICT/R4: unamended CONTRACT K-ENGINE-4 vs amended SPEC 11 and CONTRACT K-EVENT-1 (upstream method names preserved) ‖ no conflict: under D-APP-127 codex.* are Chirality-named HarnessEvent categories whose upstream method/ids/params ride in data.codex/method/params, which SPEC 10.3 permits as explicit adapter metadata; row would then be STALE_SPECIFICATION (SoW wording) or ALIGNED | APP/docs/CONTRACT.md:64; APP/docs/CONTRACT.md:78; APP/docs/SPEC.md:677-679; APP/docs/SPEC.md:695-704; RT/packages/contracts/src/harness/event-schema.ts:44-47; RT/packages/core/src/delegated-engine-adapter.ts:255-289 | MR-11 generalized unclear whether later-amended GOVERNING text (K-EVENT-1/SPEC 11) prevails over unamended K-ENGINE-4 |
| 41 | a | `#CLM-009.2` | CONTESTED | Disposition | AUTHORITY_CONFLICT | AUTHORITY_CONFLICT/R4: unamended CONTRACT K-ENGINE-4 vs amended SPEC 11 and CONTRACT K-EVENT-1 (upstream method names preserved) ‖ no conflict: under D-APP-127 codex.* are Chirality-named HarnessEvent categories whose upstream method/ids/params ride in data.codex/method/params, which SPEC 10.3 permits as explicit adapter metadata; row would then be STALE_SPECIFICATION (SoW wording) or ALIGNED | DELDIR/ScopeOfWork.md:146; APP/docs/CONTRACT.md:61; APP/docs/CONTRACT.md:64; APP/docs/CONTRACT.md:78; APP/docs/SPEC.md:677-679; APP/docs/SPEC.md:695-704; RT/packages/contracts/src/harness/event-schema.ts:44-47; RT/packages/core/src/delegated-engine-adapter.ts:255-289 | MR-11 generalized unclear whether later-amended GOVERNING text (K-EVENT-1/SPEC 11) prevails over unamended K-ENGINE-4 |
| 42 | a | `#CLM-009.5` | CONTESTED | Disposition | IMPLEMENTED_DIFFERENTLY (UNRECORDED_JUDGMENT) | IMPLEMENTED_DIFFERENTLY/UNRECORDED_JUDGMENT: in-band signal?: AbortSignal added by 364796528 (2026-09-11) with no direction record while SPEC 10.2 still says cancellation is out of band ‖ ALIGNED: the SHALL fields are carried; SoW CLM-005 turn-input row itself requires a cancellation signal and INSP-03 REQ-005 PARTIAL faulted its absence, so the SoW is internally split and the code satisfies both | DELDIR/ScopeOfWork.md:87; DELDIR/ScopeOfWork.md:149; APP/docs/SPEC.md:671; RT/packages/contracts/src/harness/agent-engine-port.ts:36-37; DELDIR/Assessment_INSP-03_DEL-03-01.md:48 | AuthorityTier PRD should be GOVERNANCE_INVARIANT (row restates SPEC; highest tier restated) |
| 43 | a | `#CLM-009.7` | CONTESTED | Disposition | AUTHORITY_CONFLICT | AUTHORITY_CONFLICT/R4: unamended CONTRACT K-ENGINE-4 vs amended SPEC 11 and CONTRACT K-EVENT-1 (upstream method names preserved) ‖ no conflict: under D-APP-127 codex.* are Chirality-named HarnessEvent categories whose upstream method/ids/params ride in data.codex/method/params, which SPEC 10.3 permits as explicit adapter metadata; row would then be STALE_SPECIFICATION (SoW wording) or ALIGNED | DELDIR/ScopeOfWork.md:151; RT/packages/core/src/delegated-engine-adapter.ts:241; RT/packages/core/src/delegated-engine-adapter.ts:255; APP/docs/CONTRACT.md:64; APP/docs/CONTRACT.md:78; APP/docs/SPEC.md:677-679; APP/docs/SPEC.md:695-704; RT/packages/contracts/src/harness/event-schema.ts:44-47; RT/packages/core/src/delegated-engine-adapter.ts:255-289 | MR-11 generalized unclear whether later-amended GOVERNING text (K-EVENT-1/SPEC 11) prevails over unamended K-ENGINE-4 |
| 44 | a | `#CLM-009.13` | REFUTED | Disposition | AUTHORITY_CONFLICT (CODEX_SOLE_ENGINE) | PARTIALLY_IMPLEMENTED / PRE_V3_DRIFT: evaluator checks only public UI event names and forbidden evidence values, never canonical HarnessEvent types or fields; INSP-03 REQ-013 (2026-06-20) already rested on UI names only; the gap holds under either reading of the codex.* conflict, so the disposition does not turn on the unruled question | DELDIR/ScopeOfWork.md:157; RT/packages/contracts/src/harness/engine-conformance.ts:186-195; RT/packages/contracts/src/harness/engine-conformance.ts:464-471; DELDIR/Assessment_INSP-03_DEL-03-01.md:56 | AUTHORITY_CONFLICT used where the finding does not depend on the conflicting sources |
| 45 | a | `#CLM-010` | CONTESTED | Disposition | NOT_AUDITABLE | NOT_AUDITABLE (standards list; REF-006 remark covered by CLM-006) ‖ STALE_SPECIFICATION/DOC_HYGIENE: the row flatly asserts 'REF-006 is reconciled under D-APP-38', false at 00115c719 | DELDIR/ScopeOfWork.md:173; DELDIR/_REFERENCES.md:12 | NOT_AUDITABLE applied to a CONTEXT_CLAIM that contains a checkable state assertion |
| 46 | a | `#CLM-013.1` | CONTESTED | Disposition | STALE_SPECIFICATION | STALE_SPECIFICATION/DOC_HYGIENE (implied reconciled state is false) ‖ ALIGNED: the sentence accurately reports what _REFERENCES.md records; the defect is the register's (REGISTER-4) | DELDIR/ScopeOfWork.md:221; DELDIR/_REFERENCES.md:12 | MR-8 'flatly asserts a now-false state' ambiguous for statements about a record's content |
| 47 | a | `#CLM-018.2` | CONTESTED | Disposition | AUTHORITY_CONFLICT | AUTHORITY_CONFLICT/R4: unamended CONTRACT K-ENGINE-4 vs amended SPEC 11 and CONTRACT K-EVENT-1 (upstream method names preserved) ‖ no conflict: under D-APP-127 codex.* are Chirality-named HarnessEvent categories whose upstream method/ids/params ride in data.codex/method/params, which SPEC 10.3 permits as explicit adapter metadata; row would then be STALE_SPECIFICATION (SoW wording) or ALIGNED | DELDIR/ScopeOfWork.md:306; APP/docs/CONTRACT.md:64; APP/docs/CONTRACT.md:78; APP/docs/SPEC.md:677-679; APP/docs/SPEC.md:695-704; RT/packages/contracts/src/harness/event-schema.ts:44-47; RT/packages/core/src/delegated-engine-adapter.ts:255-289 | MR-11 generalized unclear whether later-amended GOVERNING text (K-EVENT-1/SPEC 11) prevails over unamended K-ENGINE-4 |
| 48 | a | `#CLM-022.2` | CONTESTED | Disposition | AUTHORITY_CONFLICT | AUTHORITY_CONFLICT/R4: unamended CONTRACT K-ENGINE-4 vs amended SPEC 11 and CONTRACT K-EVENT-1 (upstream method names preserved) ‖ no conflict: under D-APP-127 codex.* are Chirality-named HarnessEvent categories whose upstream method/ids/params ride in data.codex/method/params, which SPEC 10.3 permits as explicit adapter metadata; row would then be STALE_SPECIFICATION (SoW wording) or ALIGNED | DELDIR/ScopeOfWork.md:355; DELDIR/ScopeOfWork.md:359; APP/docs/CONTRACT.md:64; APP/docs/CONTRACT.md:78; APP/docs/SPEC.md:677-679; APP/docs/SPEC.md:695-704; RT/packages/contracts/src/harness/event-schema.ts:44-47; RT/packages/core/src/delegated-engine-adapter.ts:255-289 | MR-11 generalized unclear whether later-amended GOVERNING text (K-EVENT-1/SPEC 11) prevails over unamended K-ENGINE-4 |
| 49 | a | `#REM-2` | CONTESTED | MechanicallyUnblocked; Disposition | YES; REMAINING_STATE_MISMATCH (CARRIER_PROPAGATION) | MU YES + REMAINING_STATE_MISMATCH: App-owned Runtime service with its socket API and the Codex adapter are the production path at 00115c719, so the NOT_SELECTABLE_UNTIL marker is stale ‖ MU UNKNOWN (MR-6: the socket API is Runtime-owned and the gate names D-GOV-43, not a verification surface; 'production path' may mean a released build) with Disposition ALIGNED | DELDIR/_STATUS.md:15; DELDIR/_STATUS.md:18; APP/frontend/electron/main.ts:860-866; RT/packages/daemon/src/app-owned-composition.ts:214; DELDIR/Dependencies.csv DEP-03-01-005 INTERFACE and DEP-03-01-008 HANDOVER (neither PREREQUISITE) | MR-2/MR-6 'source the gate itself names' ambiguous for ruling-named gates; VerificationEvidence cites runtime-service-host.test.ts without a named case |
| 50 | a | `#REGISTER-3` | REFUTED | ImplementationEvidence; RemainingWork | ...the DEL-03-01 decomposition row is at line 317 in the frozen file; correct line anchor | Disposition STALE_SPECIFICATION/CARRIER_PROPAGATION holds for DEP-03-01-009 (still targets Root API v2 / event schema v2, retired by D-APP-127 and CONTRACT K-EVENT-3), but the V3-01 anchor L303 is correct at the SoW's pinned decomposition_basis d6f6cadb2 (row at line 303 there); line 317 is the known basis-pin drift, not a register defect | DELDIR/_STATUS.md:16; DELDIR/ScopeOfWork.md:5; git show d6f6cadb2:APP/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md line 303; APP/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md:317; DELDIR/Dependencies.csv DEP-03-01-009; APP/docs/CONTRACT.md:80 | Line anchors should be checked against the pinned basis, not only the frozen tree |
| 51 | b | `#CLM-003.1` | CONTESTED | Disposition | ALIGNED | ALIGNED (port, adapter behind port, startTurn and HarnessEvent record present) ‖ AUTHORITY_CONFLICT/R4: the grouped 'Contract ownership' row (K-ENGINE-1: SDK APIs do not define public semantics) and canonical-record row restate REQ-002, which the same ledger places in the codex.* conflict cluster (CLM-009.2) | DELDIR/ScopeOfWork.md:53-59; RT/packages/contracts/src/harness/agent-engine-port.ts:77-94; RT/packages/core/src/delegated-engine-adapter.ts:92; RT/packages/contracts/src/harness/event-schema.ts:44-47 | Split inconsistency: same normative statement dispositioned ALIGNED here and AUTHORITY_CONFLICT at CLM-009.2 |

### DEL-04-05 (shard `V-DEL-04-05`) — 5 items

`DELDIR/` = `APP/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-05_Anthropic_Provider_Key_Base_URL_and_Network_Bridge/`

| # | Cl | Key | Verdict | Field | Ledger value | Verifier reading (CONTESTED: reading A ‖ reading B) | Evidence | Convention issue |
|---|---|---|---|---|---|---|---|---|
| 52 | a | `#CLM-009.9` | CONTESTED | Disposition | PARTIALLY_IMPLEMENTED | PARTIALLY_IMPLEMENTED (A2_TOPOLOGY): no product-owned egress evidence for the Runtime child/codex app-server ‖ ALIGNED: K-NET-1 (GOVERNING, post-D-GOV-43) makes command network follow the user-chosen labelled sandbox posture (default no network; Full access labelled in composer) and enumerates Codex account/model/turn endpoints, so broadening is not silent; residual is verification only | APP/docs/CONTRACT.md:134; RT/packages/daemon/src/codex-supervisor.ts:104-108; APP/frontend/src/components/shell/chat-panel.tsx:133 | LOW self-flag; cited line ranges drift by 1-6 lines (claude-agent-sdk-manager.ts readSdkApiKeyForTurn 53-59 / install 61-80; codex-supervisor.ts sandboxPolicy 104-108); i … |
| 53 | a | `#CLM-009.14` | REFUTED | Disposition | UNKNOWN | IMPLEMENTED_DIFFERENTLY (CauseTag CODEX_SOLE_ENGINE or A2_TOPOLOGY; Confidence MEDIUM): the public Runtime event contract carries stock Codex notifications/requests with upstream method names and raw params (codex.notification/codex.request), i.e. provider-shaped public events by D-GOV-43 design per K-EVENT-6; alternatively AUTHORITY_CONFLICT K-ENGINE-4 (no provider-shaped public events) vs K-EVENT-6 (upstream names/ … | RT/packages/contracts/src/v2-events.ts:22-27,56-57; RT/packages/contracts/src/delegated.ts:260-261,315; APP/docs/CONTRACT.md:64,83 | worker left UNKNOWN without inspecting (self-declared out of unit); DirectionEvidence should cite K-EVENT-6/D-APP-127 |
| 54 | a | `#CLM-010` | REFUTED | AuthorityTier | GOVERNANCE_INVARIANT | NOT_APPLICABLE (ClaimType CONTEXT_CLAIM requires NOT_APPLICABLE) - or reclassify ClaimType to REQUIREMENT if the Standards row is treated as restating CONTRACT 1.9; Disposition STALE_SPECIFICATION/CODEX_SOLE_ENGINE holds | DELDIR/ScopeOfWork.md:171; APP/docs/CONTRACT.md:134 | AuthorityTier rule (NOT_APPLICABLE for CONTEXT_CLAIM) |
| 55 | a | `#CLM-012` | REFUTED | AuthorityTier | LOCAL_DESIGN | NOT_APPLICABLE (CONTEXT_CLAIM); Disposition STALE_SPECIFICATION/DOC_HYGIENE holds (TBD paths now selected) | DELDIR/ScopeOfWork.md:196-210; DELDIR/Assessment_INSP-03_DEL-04-05.md:24-38 | AuthorityTier rule (NOT_APPLICABLE for CONTEXT_CLAIM) |
| 56 | b | `#CLM-028` | CONTESTED | Disposition | ALIGNED | ALIGNED (renderer fail-closed live at main.ts:292-310; principle-level claim) ‖ PARTIALLY_IMPLEMENTED (CODEX_SOLE_ENGINE): the base-URL and provider-failure parts rest on the unwired Anthropic manager that the same ledger treats as IMPLEMENTED_DIFFERENTLY at CLM-009.6/.7/.11; client.ts:695-698 validates the Codex login authUrl, not a provider base URL | APP/frontend/electron/main.ts:248-310; APP/frontend/src/lib/harness/anthropic-agent-sdk-manager.ts:181-257; APP/frontend/src/lib/harness/runtime.ts:1-3; RT/packages/client/src/client.ts:695-698 | intra-ledger inconsistency: same code counted as shipped here, unwired elsewhere |

### DEL-06-04 (shard `V-DEL-06-04`) — 6 items

`DELDIR/` = `APP/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-04_Write_Edit_Surface_and_Path_Hooks/`

| # | Cl | Key | Verdict | Field | Ledger value | Verifier reading (CONTESTED: reading A ‖ reading B) | Evidence | Convention issue |
|---|---|---|---|---|---|---|---|---|
| 57 | a | `#CLM-009.2` | CONTESTED | Disposition | IMPLEMENTED_DIFFERENTLY | IMPLEMENTED_DIFFERENTLY (code fact + R4 as recorded) ‖ AUTHORITY_CONFLICT: unamended GOVERNING CONTRACT K-PATH-2 (runtime tools must reject writes outside the active project root) directly conflicts with GOVERNING D-GOV-43 item 4 making danger-full-access an explicit user choice that lifts containment | DELDIR/ScopeOfWork.md:150; APP/frontend/src/lib/harness/tool-path-policy.ts:251; APP/docs/CONTRACT.md:100; docs/governance_harness/_PROPOSALS/D-GOV-43_2026-09-11_codex_host_replatform/D-GOV-43.proposed.md:187-195; RT/packages/daemon/src/codex-supervisor.ts:107-108 | MR-11 vs AUTHORITY_CONFLICT: conflict is direct for K-PATH-2 |
| 58 | a | `#CLM-009.5` | CONTESTED | Disposition | PARTIALLY_IMPLEMENTED | PARTIALLY_IMPLEMENTED (no Chirality exact-edit check on Codex-native edits) ‖ IMPLEMENTED_DIFFERENTLY (upstream apply_patch context matching may be an equivalent exact precondition; behavior outside evidence roots) - worker's own LOW self-flag is reasonable | DELDIR/ScopeOfWork.md:153; APP/frontend/src/lib/harness/chirality-hooks.ts:236-267; APP/execution/_Coordination/_DECISIONS/D-APP-43_RULING_2026-06-21.md:28-30; RT/packages/daemon/src/codex-supervisor.ts:40 | Evidence outside §3 roots (Codex binary) cannot resolve |
| 59 | a | `#CLM-009.6` | REFUTED | VerificationEvidence | GATE-TRANSCRIPT(APP@00115c719) chirality-hooks.test.ts 'blocks outside-root, instruction-root, and symlink wri … | Disposition/CauseTag hold, but the cited test exercises policy denials, not hook failure; no test in chirality-hooks.test.ts injects a hook exception (catch-and-block is code-only at chirality-hooks.ts:592-603, not 589-600). VerificationEvidence should be NONE_FOUND for a hook-failure fail-closed test. Also cancelOutcome returns 'cancel' (not decline) for item/fileChange | APP/frontend/src/lib/harness/chirality-hooks.ts:592-603; APP/frontend/src/__tests__/lib/chirality-hooks.test.ts:45,167,261,310,351,460,541 (test list); RT/packages/daemon/src/codex-supervisor.ts:729-734 | Evidence citation precision |
| 60 | a | `#CLM-009.10` | REFUTED | PostReleaseBasis | NO | YES. Disposition ALIGNED and ClaimType hold, but the cited Codex-path evidence (projects/chirality-runtime/packages/daemon/src/codex-supervisor.ts:653, cited as :655) is authored by da95ec194 (git blame), and at the frozen basis app-owned-composition.ts:170-171 wires an ApplicationToolRegistry (da95ec194) so the operative reply is 'No active application tool binding', not the quoted string; the load-bearing fact is t … | RT/packages/daemon/src/codex-supervisor.ts:653; RT/packages/daemon/src/app-owned-composition.ts:170-171; RT/packages/core/src/runtime-service.ts:580; APP/frontend/src/lib/harness/mcp/read-tools.ts:233,319-324 | PostReleaseBasis set by assumption (worker friction item 3); reverse_notes correctly revisited |
| 61 | a | `#CLM-018.2` | CONTESTED | Disposition | STALE_SPECIFICATION | STALE_SPECIFICATION (register records REF-006 MATCH under D-APP-38, so the HASH_MISMATCH traceability row is outdated) ‖ effectively current / REMAINING_STATE-type: the frozen PRD no longer matches the recorded hash (REGISTER-1), so a warning-qualification until reconciliation is substantively required again; the stale element is the register, not this row | DELDIR/ScopeOfWork.md:333; DELDIR/_REFERENCES.md:8-9,12 (recorded fa8fc9dc/01e1c75c/8649ccba) vs frozen shasum APP/docs/CONTRACT.md 57411f8d, SPEC.md 8b0d805b, PRD.md 17ca3f3c; git log: last touched 2026-09-12 by 23b3879b3 (D-GOV-43 tranche) plus 9eaddb596/7f1e9f387/95b342519 | MR-8: 'flatly asserts a now-false state' is unclear when the premise flipped twice (mismatch -> MATCH -> drift) |
| 62 | b | `#CLM-009.11` | CONTESTED | Disposition | ALIGNED | ALIGNED (atomic-write used by live working-root routes; SHOULD-level atomicity; Codex fileChange items reach the event stream) ‖ IMPLEMENTED_DIFFERENTLY: for Codex-native writes the MUST-emit diff/summary is only the upstream fileChange item (App code at harness-event-views.ts:17 is a comment, no Chirality summary), which CLM-009.13 treats as IMPLEMENTED_DIFFERENTLY for the parallel provenance clause | DELDIR/ScopeOfWork.md:159; APP/frontend/src/lib/atomic-write.ts:10; APP/frontend/src/lib/lifecycle/transition.ts:210; APP/frontend/src/app/api/working-root/deliverable/status/transition/route.ts; APP/frontend/src/lib/shell/harness-event-views.ts:17; APP/frontend/src/lib/harness/chirality-hooks.ts:645-674 | Inconsistent treatment of Codex-native evidence between REQ-011 and REQ-013 |

### DEL-08-04 (shard `V-DEL-08-04`) — 18 items

`DELDIR/` = `APP/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-04_Type_2_Subagent_Governance_Bridge/`

| # | Cl | Key | Verdict | Field | Ledger value | Verifier reading (CONTESTED: reading A ‖ reading B) | Evidence | Convention issue |
|---|---|---|---|---|---|---|---|---|
| 63 | a | `#SEC-1.2` | REFUTED | Disposition | IMPLEMENTED_DIFFERENTLY (CauseTag NATIVE_DELEGATION) | ALIGNED with CauseTag NONE for the no-role-by-descent half (GOVERNING App CONTRACT K-UNTYPED-1 and K-ROLE-2 state the same rule and the Runtime records it: delegationPolicy string says native descent does not assign a role; nativeDescendant kept separate; role-policy test proves no inference). Role chosen through a configured [agents] type is selection not descent. If the App bridge itself must consume the class then … | APP/docs/CONTRACT.md:128;APP/docs/CONTRACT.md:229;RT/packages/core/src/delegated-runtime.ts:321;RT/packages/core/src/role-policy.ts:30-44;RT/tests/role-policy.test.ts:10 | MR-8 / GOVERNING map: divergence claimed against text that the GOVERNING contract itself restates |
| 64 | a | `#CLM-003.1` | REFUTED | ImplementationEvidence | managed-delegation.ts:552-760 ManagedDelegationService.delegate; subagent-governance.ts:195-310 (as the gate o … | Disposition IMPLEMENTED_DIFFERENTLY/CODEX_SOLE_ENGINE stands but the evidence overstates module-level conformance: delegate_agent (coordination-tools.ts:269-297) calls ManagedDelegationService.delegate which applies its own seal/approvalRef/hierarchy checks and never calls evaluateSubagentGovernance; the gate is called only by TurnEngine for the legacy SDK subagent path (turn-engine.ts:232). AssessmentEvidence STILL … | APP/frontend/src/lib/harness/mcp/coordination-tools.ts:269-297;APP/frontend/src/lib/harness/turn-engine.ts:232-235;APP/frontend/src/lib/harness/managed-delegation.ts:558-560 | - |
| 65 | a | `#CLM-005.2` | CONTESTED | Disposition | STALE_SPECIFICATION (LOW) | STALE_SPECIFICATION: the named modules are not on the production path ‖ ALIGNED: the cell is an implementation-path record (Construction table; same list is Resolved at CLM-030.1 which the ledger marks ALIGNED) and all named paths exist; production reachability is already carried at SEC-1.1/CLM-003.1 | DELDIR/ScopeOfWork.md:138;DELDIR/ScopeOfWork.md:478;APP/frontend/src/lib/harness/managed-delegation.ts;APP/frontend/src/lib/harness/subagent-bridge.ts;APP/frontend/src/lib/harness/mcp/coordination-tools.ts:269 | Internal inconsistency with CLM-030.1 (same path list; ALIGNED) |
| 66 | a | `#CLM-010.5` | CONTESTED | Disposition | STALE_SPECIFICATION (PRE_V3_DRIFT) | STALE_SPECIFICATION: root AGENTS.md lets HELP_HUMAN dispatch Type 2 directly and the 2026-08-16 repair is owner-integrated (TM-ROOT-125 INCORPORATED) ‖ IMPLEMENTED_DIFFERENTLY or AUTHORITY_CONFLICT: the GOVERNING App CONTRACT K-SUBAGENT-1 still says 0->1 or 1->2, matching the SoW; root AGENTS.md is execution protocol under RUN_BASIS s5 and no D-APP ruling for the repair was found, so the SoW text agrees with the GOVE … | APP/frontend/src/lib/harness/managed-delegation.ts:291-303;APP/docs/CONTRACT.md:125;AGENTS.md:29;DELDIR/_STATUS.md:65 | MR-8 / GOVERNING map (judge text against GOVERNING docs, not execution-protocol files) |
| 67 | a | `#CLM-013.2` | CONTESTED | Disposition | STALE_SPECIFICATION (PRE_V3_DRIFT) | STALE_SPECIFICATION ‖ IMPLEMENTED_DIFFERENTLY/AUTHORITY_CONFLICT (see CLM-010.5: GOVERNING K-SUBAGENT-1 still 0->1) | DELDIR/ScopeOfWork.md:260;APP/frontend/src/__tests__/lib/managed-delegation.test.ts:127;APP/docs/CONTRACT.md:125 | MR-8 / GOVERNING map |
| 68 | a | `#CLM-016.3` | REFUTED | Disposition | IMPLEMENTED_DIFFERENTLY (CauseTag NATIVE_DELEGATION) | ALIGNED/NONE (see SEC-1.2): GOVERNING K-UNTYPED-1 and K-ROLE-2 restate REQ-002 and Runtime implements no-role-by-descent; Root owns native semantics | APP/docs/CONTRACT.md:128;APP/docs/CONTRACT.md:229;RT/packages/core/src/delegated-runtime.ts:321;RT/tests/role-policy.test.ts:10 | MR-8 / GOVERNING map |
| 69 | a | `#CLM-016.6` | CONTESTED | Disposition | STALE_SPECIFICATION (A2_TOPOLOGY) | STALE_SPECIFICATION: K-CONTROL-1 retires the supervisor-socket design through DEL-02-07 ‖ UNKNOWN/ALIGNED: REQ-005 names only WP-03/05 fixtures (the DEL-02-07 wording is _STATUS gate text, not REQ-005); the A2 supplement retains the Runtime supervisor module; no App surface states WP-03/05 retired | DELDIR/ScopeOfWork.md:304;docs/CONTRACT.md:169;docs/governance_harness/_DECISIONS/D-GOV-43_supplement_topology_A2.md:43-50;DELDIR/_STATUS.md:17 | DeclaredState imports _STATUS gate wording into the REQ row |
| 70 | a | `#CLM-020` | CONTESTED | Disposition | STALE_SPECIFICATION (PRE_V3_DRIFT) | STALE_SPECIFICATION ‖ IMPLEMENTED_DIFFERENTLY/AUTHORITY_CONFLICT for step 5 (GOVERNING K-SUBAGENT-1 still 0->1); also step 1/8 call-the-gate-before-creation is not how delegate_agent works (no evaluateSubagentGovernance call) | DELDIR/ScopeOfWork.md:344;APP/frontend/src/lib/harness/managed-delegation.ts:291-303;APP/docs/CONTRACT.md:125;APP/frontend/src/lib/harness/mcp/coordination-tools.ts:269-297 | MR-8 / GOVERNING map |
| 71 | a | `#CLM-025.2` | CONTESTED | Disposition | STALE_SPECIFICATION (PRE_V3_DRIFT) | STALE_SPECIFICATION ‖ IMPLEMENTED_DIFFERENTLY/AUTHORITY_CONFLICT (see CLM-010.5) | DELDIR/ScopeOfWork.md:415;APP/frontend/src/lib/harness/managed-delegation.ts:291-303;APP/docs/CONTRACT.md:125 | MR-8 / GOVERNING map |
| 72 | a | `#CLM-028.2` | CONTESTED | Disposition | STALE_SPECIFICATION (PRE_V3_DRIFT) | STALE_SPECIFICATION ‖ IMPLEMENTED_DIFFERENTLY/AUTHORITY_CONFLICT (see CLM-010.5) | DELDIR/ScopeOfWork.md:455;APP/frontend/src/lib/harness/managed-delegation.ts:291-303;APP/docs/CONTRACT.md:125 | MR-8 / GOVERNING map |
| 73 | a | `#CLM-030.3` | CONTESTED | Disposition | REMAINING_STATE_MISMATCH (LOW) | REMAINING_STATE_MISMATCH: open TBD with no Remaining entry ‖ ALIGNED: CLM-032 (2026-07-19) names the separately gated item as the per-attempt decision-replay artifact, which REM-1 tracks under D-APP-117; code already fixes a partial format (non-empty string; dedicated Agent 2 D-GOV-nn RULED) | DELDIR/ScopeOfWork.md:480;DELDIR/ScopeOfWork.md:495;DELDIR/_STATUS.md:11-15;APP/frontend/src/lib/harness/managed-delegation.ts:311-326;APP/frontend/src/lib/harness/subagent-governance.ts:280-285 | - |
| 74 | a | `#CLM-032` | CONTESTED | CauseTag | PRE_V3_DRIFT | PRE_V3_DRIFT (Agent 0 clause; repair 2026-08-16) ‖ NATIVE_DELEGATION (sole-path clause; the row cites the Codex re-platform steer as DirectionEvidence, which explains the native half, not the pre-v3 drift); the Agent 0 half is also subject to the CLM-010.5 GOVERNING-map question | DELDIR/ScopeOfWork.md:495;APP/frontend/src/lib/harness/managed-delegation.ts:291-303;RT/packages/core/src/native-role-config.ts:156-199;APP/docs/CONTRACT.md:125 | CauseTag single-valued for a two-cause row |
| 75 | a | `#REM-2` | CONTESTED | Disposition | REMAINING_STATE_MISMATCH (MechanicallyUnblocked UNKNOWN) | REMAINING_STATE_MISMATCH: the gate names the DEL-02-07 supervisor return whose socket design K-CONTROL-1 retires ‖ ALIGNED as a Remaining record: the work is genuinely open (no class-aware code), the gate text is verbatim and its cross-project status is correctly UNKNOWN under MR-6; the staleness belongs to REGISTER-1 not to the Remaining state | DELDIR/_STATUS.md:17-24;docs/CONTRACT.md:169;docs/governance_harness/_DECISIONS/D-GOV-43_supplement_topology_A2.md:43-50;APP/frontend/src/lib/harness/subagent-governance.ts | MR-6 applied correctly (UNKNOWN) |
| 76 | a | `#REM-3` | CONTESTED | MechanicallyUnblocked | NO | NO: DEL-02-02 still writes V3-04 as NOT_SELECTABLE_UNTIL V3-03 and DEL-07-03-V3-01 landed ‖ YES: a bounded V3-04 slice was implemented 2026-09-06 (so V3-04 was selected) and the only named Depends edge DEP-08-04-013 is INTERFACE not PREREQUISITE; Disposition REMAINING_STATE_MISMATCH/CARRIER_PROPAGATION is itself weakly grounded (item text has no daemon wording; the mismatch cited is DEP-014) | DELDIR/_STATUS.md:26-33;APP/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-02_Workbench_and_Pipeline_Selection_UX/_STATUS.md:42;APP/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-02_Workbench_and_Pipeline_Selection_UX/_STATUS.md:52-53;DELDIR/Dependencies.csv:14 | MR-2/MR-6 MechanicallyUnblocked: meaning of "selected" gate undefined |
| 77 | a | `#REGISTER-1` | CONTESTED | Disposition | STALE_SPECIFICATION (A2_TOPOLOGY) | STALE_SPECIFICATION: K-CONTROL-1 retires the supervisor-socket design through DEL-02-07 ‖ defect weaker than stated: the A2 supplement re-expresses item 7 and retains the Runtime supervisor module, so an accepted DEL-02-07 return is not clearly moot; record as DOC_HYGIENE wording defect pending Root routing | DELDIR/Dependencies.csv:12;docs/CONTRACT.md:169;docs/governance_harness/_DECISIONS/D-GOV-43_supplement_topology_A2.md:43-50 | - |
| 78 | b | `#CLM-010.3` | REFUTED | ImplementationEvidence | subagent-governance.ts:270-290 | Disposition ALIGNED holds but the missing-metadata denial is at subagent-governance.ts:250-257 (METADATA_PRESENCE); 270-290 are the pipeline-approval and approvalRef checks. Also the managed delegate_agent path denies missing seal/approval at managed-delegation.ts:559-560 and is the more relevant evidence for R03 under D-APP-68 | APP/frontend/src/lib/harness/subagent-governance.ts:250-257;APP/frontend/src/lib/harness/managed-delegation.ts:559-560;APP/frontend/src/__tests__/lib/harness-subagent-governance.test.ts:124 | Evidence line accuracy |
| 79 | b | `#CLM-025.1` | CONTESTED | Disposition | ALIGNED | ALIGNED for deny-first, sealed context, no inheritance, separate persistence ‖ PARTIALLY_IMPLEMENTED: the approval-is-evidence principle asks that ambiguous, mutable or SDK-only approval data deny, but both gates accept any non-empty approvalRef string (only dedicated named Agent 2 roles get a RULED D-GOV check), and the toolkit supplies approvalRef as free UI text | DELDIR/ScopeOfWork.md:418;APP/frontend/src/lib/harness/subagent-governance.ts:280-285;APP/frontend/src/lib/harness/managed-delegation.ts:559-560;APP/frontend/src/lib/harness/managed-delegation.ts:311-326;APP/frontend/src/lib/harness/toolkit.ts:156-158 | - |
| 80 | c | `#SEC-1.1 / CAP-HARNESS-056` | CONTESTED | Response | CLAIMED_BY | CLAIMED_BY: admission/launch via delegate_agent is DEL-08-04 output ‖ PARTIAL: the capability also names orchestration records, atomic replacement and handoff state, which D-APP-68 disposition 4 assigns to DEL-08-05 (the Rationale itself says shared with DEL-08-05) | DELDIR/ScopeOfWork.md:495;APP/frontend/src/lib/harness/managed-delegation.ts:401-465;APP/frontend/src/lib/harness/managed-delegation.ts:552-760 | Reverse-pass rule: shared ownership stated in Rationale points to PARTIAL |

### DEL-09-07 (shard `V-DEL-09-07`) — 5 items

`DELDIR/` = `APP/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-07_Two-Job_Runtime-Control_Installer_Migration_and_Rollback/`

| # | Cl | Key | Verdict | Field | Ledger value | Verifier reading (CONTESTED: reading A ‖ reading B) | Evidence | Convention issue |
|---|---|---|---|---|---|---|---|---|
| 81 | a | `#SEC-2.1` | CONTESTED | Disposition | ACCEPTED_DIVERGENCE | ACCEPTED_DIVERGENCE (ownership map overtaken by A2) ‖ NOT_AUDITABLE or ALIGNED (CLM-001 is a CONTEXT_CLAIM that accurately reports what [D] and [R7] say; [D] still says it at basis; the divergence already lives in REGISTER-2) | DELDIR/ScopeOfWork.md:49; APP/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md:384; APP/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md:601; APP/docs/CONTRACT.md:224; APP/docs/SPEC.md:1248 | NOT_AUDITABLE vs ACCEPTED_DIVERGENCE for CONTEXT_CLAIM rows describing source content is undefined |
| 82 | a | `#SEC-2.5` | CONTESTED | Disposition | ACCEPTED_DIVERGENCE | ACCEPTED_DIVERGENCE (A2 moves supervision to the App so the owner partition is overtaken) ‖ ALIGNED (deliverable performed no act; boundary vacuously kept, as the worker itself ruled for SEC-1.5) | DELDIR/ScopeOfWork.md:53; APP/frontend/electron/runtime-service-host.ts:1-9; APP/docs/CONTRACT.md:224; APP/execution/_Coordination/_DECISIONS/D-APP-127_RULING_APPLICATION_D-GOV-43_CODEX_HOST_REPLATFORM_A2_2026-09-12.md:44 | Vacuous-satisfaction rule absent (SEC-1.5 ALIGNED vs SEC-2.5 ACCEPTED_DIVERGENCE); AuthorityTier GOVERNANCE_INVARIANT doubtful: REQ-004 restates [D]/Root SoW ownership, n … |
| 83 | a | `#SEC-2.13` | CONTESTED | Disposition | ACCEPTED_DIVERGENCE | ACCEPTED_DIVERGENCE for the OI-003 transaction-verification half ‖ split: gate half (F-APP-2, D-APP-97, G6a remain applicable) ALIGNED - D-APP-97 is still RULED and G6a is kept by IMPACT; the ImplementationEvidence rationale "5 retires as gates" misreads IMPACT family 5 (process hygiene, not release gates) | DELDIR/ScopeOfWork.md:62-69; APP/execution/_Coordination/_DECISIONS/D-APP-127_RULING_APPLICATION_D-GOV-43_CODEX_HOST_REPLATFORM_A2_2026-09-12.md:47-48; docs/governance_harness/_PROPOSALS/D-GOV-43_2026-09-11_codex_host_replatform/IMPACT.md:168; docs/governance_harness/_PROPOSALS/D-GOV-43_2026-09-11_codex_host_replatform/IMPACT.md:121; APP/execution/_Coordination/_DECISIONS/_REGISTER.md:112 | Split rule for mixed-validity paragraphs; AuthorityTier GOVERNANCE_INVARIANT doubtful (F-APP-2/D-APP-97 are App decisions) |
| 84 | a | `#STATE-2` | REFUTED | Disposition | STALE_SPECIFICATION (HumanDecisionNeeded R4) | ACCEPTED_DIVERGENCE, HumanDecisionNeeded NO: D-APP-127 preserves "the DEL-09-07 folder" (which contains _CONTEXT.md) as immutable history, and _CONTEXT.md acknowledges the gate exactly as the SoW does (no implementation act authorized); the Notes misread the ruling as not covering it; treatment inconsistent with the 24 SoW rows | APP/execution/_Coordination/_DECISIONS/D-APP-127_RULING_APPLICATION_D-GOV-43_CODEX_HOST_REPLATFORM_A2_2026-09-12.md:172-173; DELDIR/_CONTEXT.md:24-27; DELDIR/_STATUS.md:9 | MR-8 applied inconsistently across files in one preserved-history folder |
| 85 | a | `#REGISTER-1` | CONTESTED | Disposition | STALE_SPECIFICATION | STALE_SPECIFICATION (Dependencies.csv is a machine register with a RETIRED lifecycle; live ACTIVE/PENDING prerequisites for a retired subject can feed dependency tooling) ‖ ACCEPTED_DIVERGENCE (D-APP-127 keeps the whole folder immutable history, so a register retirement would itself need owner direction) | DELDIR/Dependencies.csv; DELDIR/_DEPENDENCIES.md:18; DELDIR/_DEPENDENCIES.md:78-79; APP/execution/_Coordination/_DECISIONS/D-APP-127_RULING_APPLICATION_D-GOV-43_CODEX_HOST_REPLATFORM_A2_2026-09-12.md:172-173 | MR-5/MR-8 interplay for registers inside a ruling-preserved folder undefined; R4 is right under either reading |

### SURFACES (shard `V-DEL-09-07`) — 3 items

| # | Cl | Key | Verdict | Field | Ledger value | Verifier reading (CONTESTED: reading A ‖ reading B) | Evidence | Convention issue |
|---|---|---|---|---|---|---|---|---|
| 86 | d | `CAP-HARNESS-011` | CONTESTED | Granularity | separate row (8-line native-plan-text.ts, one function) | keep (distinct display-only projection a deliverable could own) ‖ fold into CAP-HARNESS-010 native plan client (per-file/per-function row contrary to §5, and inconsistent with the notes folding other small helpers) | APP/frontend/src/lib/harness/native-plan-text.ts:2; APP/frontend/src/__tests__/lib/plan-export-dialog.test.ts:6-14 | §5 granularity |
| 87 | d | `CAP-HARNESS-021` | CONTESTED | Granularity | separate row (11-line prompt helper) | keep (user-observable prefilled chat prompt) ‖ fold into CAP-HARNESS-020 workflow draft review (per-function row); also EntryPoint workflow-draft-review.tsx imports only the type (real consumer is chat-panel.tsx:1673); CoveringTests NONE_FOUND verified correct | APP/frontend/src/lib/harness/workflow-feedback.ts:8-11; APP/frontend/src/components/shell/chat-panel.tsx:52; APP/frontend/src/components/woven-dialogue/workflow-draft-review.tsx:5; APP/frontend/src/__tests__/components/workflow-draft-review.test.tsx:28 | §5 granularity; EntryPoints definition loose |
| 88 | d+ | `CAP-HARNESS-058` | REFUTED | Capability | ... and executable subagent bridge (D-APP-10 Option C) | Subagent governance gates plus a DISABLED legacy SDK Agent bridge: createExecutableSubagentBridge returns undefined, evaluateSubagentPreflight always returns allowed=false with executionPosture hard-denied and directs to delegate_agent; only createExecutableAgentDefinition remains as a builder. LEGACY-IN-PROCESS tag and PostReleaseBasis NO verified | APP/frontend/src/lib/harness/subagent-bridge.ts:5-9; APP/frontend/src/lib/harness/subagent-bridge.ts:84-116; APP/frontend/src/__tests__/lib/subagent-bridge.test.ts:54-65 | Accuracy: capability text taken from symbol names/ruling ref rather than behavior |

### DEL-10-01 (shard `V-DEL-10-01`) — 7 items

`DELDIR/` = `APP/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-01_DomainEngineProfile_Contract_Draft/`

| # | Cl | Key | Verdict | Field | Ledger value | Verifier reading (CONTESTED: reading A ‖ reading B) | Evidence | Convention issue |
|---|---|---|---|---|---|---|---|---|
| 89 | a | `#CLM-004.5` | CONTESTED | Disposition | ALIGNED | ALIGNED (SoW:65 and :184 keep direct protected-path writes/hooks future; type separates roles at projects/chirality-runtime/packages/contracts/src/harness/domain-profile.ts:120-121) ‖ DOCUMENTED_UNIMPLEMENTED (K-DOMAIN-2 is present-tense; no enforcement of protected_write_paths/agent_writable_paths anywhere outside the type; assessment REQ006 PARTIAL still current) | DELDIR/ScopeOfWork.md:68; RT/packages/contracts/src/harness/domain-profile.ts:120-121; DELDIR/Assessment_INSP-03_DEL-10-01.md:24 | Row internally inconsistent: ALIGNED with RemainingWork UNKNOWN and AssessmentEvidence STILL CURRENT of a PARTIAL finding |
| 90 | a | `#CLM-007.1` | CONTESTED | CauseTag | UNRECORDED_JUDGMENT | UNRECORDED_JUDGMENT (no record reconciles the SoW draft rule with the optional fields) ‖ PRE_V3_DRIFT with recorded mechanism: guard optionality present since f4d7deb28 (2026-07-04) and follows the ruled D-APP-49 mitigation to mirror the validator, whose status/integration enums are required=False | RT/packages/contracts/src/harness/domain-profile.ts:105-116,220-228; APP/execution/_Coordination/_DECISIONS/D-APP-49_PACKET_F3_SOURCE_TYPES_2026-07-04.md:104-106; tools/validation/validate_domain_engine_profile.py:525-526 | CauseTag precedence: UNRECORDED_JUDGMENT vs PRE_V3_DRIFT overlap (worker used PRE_V3_DRIFT on CLM-028.1 on the same timing basis); GOVERNING packet mitigation not conside … |
| 91 | a | `#CLM-016.1` | REFUTED | CauseTag | UNRECORDED_JUDGMENT | RUNTIME_EXTRACTION (mechanism FACADE_DEPRECATION) with recorded GOVERNING direction: D-APP-73 RULED 2026-07-22 extracts the harness to root runtime; D-APP-76 RULED recognizes the D-APP-73 prospective rehome of the D-APP-49 modules; D-APP-89 RULED Option B migrates importers to @chirality/runtime-contracts with the facade retained; D-APP-118 (facade retirement) AWAITING_RULING. LatestDecision should be D-APP-89 (or D- … | APP/execution/_Coordination/_DECISIONS/_REGISTER.md:88,91,104,135; APP/execution/_Coordination/_DECISIONS/D-APP-76_RULING_2026-07-27.md:38; APP/execution/_Coordination/_DECISIONS/D-APP-89_RULING_COMPATIBILITY_FACADE_MIGRATION_2026-08-02.md:32-41; APP/frontend/packages/harness-contract/src/domain-profile.ts:1-2; git log 8b3643e6c 99fe2edae df7d62308 | UNRECORDED_JUDGMENT applied without searching GOVERNING register rows (only CONTEXT searched); DirectionEvidence column is CONTEXT-only so a GOVERNING explanation has no … |
| 92 | a | `#CLM-026.2` | CONTESTED | AssessmentEvidence | STILL CURRENT (old REQ003 guidance lines) | STILL CURRENT ‖ OVERTAKEN: old REQ003 PASS rested on Guidance keeping OpenPipeStress fixture-level; the registry now registers open_pipe_stress and the headless tool is open_pipe_stress-only. Disposition/CauseTag hold | DELDIR/Assessment_INSP-03_DEL-10-01.md:21; DELDIR/ScopeOfWork.md:414; APP/frontend/src/lib/harness/mcp/domain-profile-registry.ts:53-83; APP/frontend/src/lib/harness/mcp/read-tools.ts:1195 | MR-1 ambiguity when the assessed guidance line itself is stale |
| 93 | a | `#CLM-028.1` | CONTESTED | Disposition | IMPLEMENTED_DIFFERENTLY | IMPLEMENTED_DIFFERENTLY/PRE_V3_DRIFT (skeleton would fail isDomainEngineProfile) ‖ NOT_AUDITABLE (SoW:465 disclaims it as illustrative, SoW:467 keeps it as-is by design) or STALE_SPECIFICATION/DOC_HYGIENE (skeleton omits risk_classes and accepted_or_applied_requires that its own canonical shape at SoW:107-113 carries; the code matches CLM-006) | DELDIR/ScopeOfWork.md:431-467 vs DELDIR/ScopeOfWork.md:107-113; RT/packages/contracts/src/harness/domain-profile.ts:185-199,229-241 | AuthorityTier LOCAL_DESIGN on a CONTEXT_CLAIM row (must be NOT_APPLICABLE). Note: ScopeOfWork.md created 2026-07-13 (d19ee4d30) from the legacy kit; PRE_V3 timing still h … |
| 94 | a | `#REM-1` | REFUTED | Disposition | ALIGNED | REMAINING_STATE_MISMATCH, CauseTag A2_TOPOLOGY, LatestDecision D-APP-127 (D-GOV-43). The shared-runtime project-client lane (DEC-019: one per-user daemon, Unix-socket clients, PEC client migration) is superseded on the App path; App docs record RB-PEC-ADAPTER adapter-service/RBAC/scratch-demo/pilot assertions as retired v0.4 allocation, D-PEC-56 partially superseded, PEC socket compatibility not an MVP prerequisite. … | APP/docs/harness/reliance_boundary_register.md:150-178; APP/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md:628; APP/execution/_Coordination/_DECISIONS/D-APP-127_RULING_APPLICATION_D-GOV-43_CODEX_HOST_REPLATFORM_A2_2026-09-12.md:36-48; DELDIR/_STATUS.md:12 | MR-6 UNKNOWN used after an incomplete search; LOW self-flag alternative was correct |
| 95 | b | `#CLM-002` | CONTESTED | Disposition | ALIGNED | ALIGNED (identity fields match _CONTEXT.md:5-16) ‖ STALE_SPECIFICATION/CARRIER_PROPAGATION for the Current posture row (not current implementation) - the deliverable owns a live mirror and registry (SoW:260), consistent with the worker treating CLM-024 as stale; also _CONTEXT.md has no Current posture field so field-for-field overstates | DELDIR/ScopeOfWork.md:40; DELDIR/_CONTEXT.md:5-16; DELDIR/ScopeOfWork.md:260 | Split rule: the posture row is independently dispositionable and was not split |

## §4 Systematic patterns

The patterns are ranked by consequence, weighted by frequency:

- whether the pattern can change a Disposition or route (HumanDecisionNeeded, R4);
- how many items and units it touches.

Each pattern gives example keys across units and a candidate convention repair for the R0
gate. The repairs are proposals, not rulings.

### 4.1 MR-11 compared with AUTHORITY_CONFLICT when a ruling undercuts GOVERNING clauses that were never amended

*Highest consequence. About 30 contested or refuted items in 6 units. It moves
Dispositions and R4 routing.*

MR-11 (generalized) says a ruled decision stands over untranscribed corpus wording. It does
not say what happens when the "older wording" is itself **GOVERNING** and still in force,
or when the GOVERNING corpus contradicts itself after a partial amendment. Workers and
shards split three ways.

**(a) The ruling was treated as overriding a clause it does not name.**

- DEL-06-04 `#CLM-009.2`:
  - unamended K-PATH-2 (`docs/CONTRACT.md:100`) requires rejecting writes outside the
    project root;
  - D-GOV-43 item 4 makes danger-full-access a user choice.
- The same family: `#CLM-009.1`, `.3` to `.7`, `.12` and `.13`.
- The AGG_TABLES token "D-GOV-43 item 4 does not name K-PATH/K-ROOT/K-HOOK" appears on 12
  items.

**(b) A conflict inside the GOVERNING corpus was read as untranscribed wording.**

- DEL-04-05 `#CLM-004.2`, `#CLM-009.10` and `#CLM-009.9`:
  - K-NET-1 (`CONTRACT.md:134`) is post-D-GOV-43 text, yet it still says remote MCP and
    providers "fail closed";
  - SPEC §25.1 shares the user's MCP definitions.
- DEL-03-01_B codex.* cluster: `#CLM-004.1`, `#CLM-009.2`, `#CLM-009.7`, `#CLM-018.2` and
  `#CLM-022.2`.
  - Unamended K-ENGINE-4 (`:64`) is set against amended K-EVENT-1, K-EVENT-6 and SPEC 11.
  - These rows are CONTESTED, because under D-APP-127 the `codex.*` categories may be
    adapter metadata.
- DEL-03-01_B `#CLM-009.13` was REFUTED, because its finding does not depend on the
  conflict.
- DEL-03-01_B `#CLM-003.1` was dispositioned ALIGNED, but the same statement at
  `#CLM-009.2` was AUTHORITY_CONFLICT.

**(c) The GOVERNING text was not applied at all.**

- DEL-02-05 `#CLM-003`, `#CLM-009.1` and `#CLM-010.1` to `.3`:
  - these rows are IMPLEMENTED_DIFFERENTLY with R4;
  - but the GOVERNING preamble (`docs/PRD.md:15`, `docs/CONTRACT.md:15`) already demotes
    Anthropic text to compatibility history;
  - so they are arguably STALE_SPECIFICATION with HumanDecisionNeeded NO.
- DEL-02-05 `#CLM-013.4`: K-NET-1 adapts the postures rather than retiring them.
- DEL-08-04 Agent 0 cluster: `#CLM-010.5`, `#CLM-013.2`, `#CLM-020`, `#CLM-025.2`,
  `#CLM-028.2` and half of `#CLM-032`.
  - The SoW agrees with GOVERNING K-SUBAGENT-1 (`:125`, 0→1 / 1→2).
  - The rows were judged stale against root `AGENTS.md`, which is *execution protocol*
    under RUN_BASIS §5.
- DEL-08-04 `#SEC-1.2` and `#CLM-016.3` were REFUTED. GOVERNING K-UNTYPED-1 and K-ROLE-2
  restate the claim.
- DEL-01-01 `#CLM-023`: a CONTEXT steer drove a stale reading against K-PERM-2 and K-PERM-3.

**Candidate repair.** Write MR-11 as an explicit precedence rule:

1. A ruling overrides a GOVERNING clause only if one of these holds:
   - the ruling names the clause or its family;
   - the clause has since been amended to match.
2. Otherwise, apply both of these:
   - where two GOVERNING statements in force disagree → AUTHORITY_CONFLICT with R4;
   - text is judged against GOVERNING docs, never against execution-protocol files.
3. State whether a later-amended clause prevails over an unamended sibling in the same
   document.

### 4.2 DirectionEvidence: CONTEXT-only compared with GOVERNING explanations

*High frequency. 7 REFUTED, plus about 30 items with a ConventionIssue note, in 6 units.
It does not change Dispositions by itself, but it feeds §4.3.*

The rulebook defines DirectionEvidence as the CONTEXT record that explains a divergence.
Three failure modes appeared.

**(a) A source that is not in RUN_BASIS §5 was cited as CONTEXT.**

- DEL-01-01 `#CLM-008` (REFUTED) cites `NOTICE_2026-09-19_APP_LOOP_WORKGRAPH.md`, and the
  worker itself notes the notice is outside §5.
- DEL-08-04's DirectionEvidence uses an App-relative path, not a repo-relative one.

**(b) A §5 CONTEXT source was misglossed.**

- DEL-03-01_A `#CLM-003.4`, `#CLM-011`, `#CLM-013.2`, `#CLM-018`, `#CLM-019` and `#CLM-022`
  are REFUTED. `#CLM-009.8` is CONTESTED.
- They cite HANDOFF L126-128 as the reason the Codex adapter is not an engine-conformance
  subject. The removed file was supply and admission conformance.
- DEL-03-01_B used the same citation on `#CLM-003.4`, `#CLM-009.8/.10`, `#CLM-011` and
  `#CLM-012.1`.

**(c) GOVERNING records were placed in a CONTEXT-only field, because there is no other slot.**

- DEL-03-01_A: 11 keys cite D-APP-127 or the decomposition, including `#CLM-002`, `#CLM-021`
  and `#REGISTER-3`.
- DEL-03-01_B: `#CLM-002`, `#CLM-008`, `#CLM-003.2` and `#CLM-005.2`.
- DEL-06-04 mixes the steer and D-GOV-43 in one field, and cites the D-GOV-43 *proposal*
  path. The ruling record is `docs/governance_harness/_DECISIONS/D-GOV-43_codex_host_replatform.md`.
- DEL-09-07 appends "GOVERNING basis D-APP-127" to every ACCEPTED_DIVERGENCE row.
- In mode (c) the worker was substantively right. The field definition forced either a
  misfiled citation or a false NONE_FOUND.

**Candidate repair.** Add a `GoverningExplanation` column, or let `LatestDecision` carry the
ruling that explains a divergence. Keep DirectionEvidence strictly for §5 CONTEXT records.
State that a GOVERNING explanation defeats UNRECORDED_JUDGMENT.

### 4.3 "No direction found" declared without checking the decision register

*Medium frequency, high consequence. It produced 2 of the 6 Disposition-level refutations.*

- **DEL-10-01 `#CLM-016.1` (REFUTED CauseTag).**
  - The row has UNRECORDED_JUDGMENT.
  - RULED D-APP-73, D-APP-76 and D-APP-89 record the harness extraction and the facade
    migration.
  - The relocation is pre-v3: `8b3643e6c`, 2026-07-22.
- **DEL-10-01 `#REM-1` (REFUTED Disposition).**
  - The row says D-T0-23 and D-PEC-56 appear on no App governing surface.
  - Decomposition `DEC-019` and `reliance_boundary_register.md:148-178` show they do.
  - The row should be REMAINING_STATE_MISMATCH / A2_TOPOLOGY.
- **DEL-10-01 `#CLM-007.1` (CONTESTED).** The ruled D-APP-49 mitigation (mirror the
  validator) was not considered.
- **DEL-04-05 `#CLM-009.14` (REFUTED).** The row was left UNKNOWN without inspecting
  `projects/chirality-runtime/packages/contracts/src/v2-events.ts:22-27`.
- **DEL-02-05 `#SEC-1.4`, `#SEC-2.5` and `#CLM-013.5` (CONTESTED).**
  - The rows use UNRECORDED_JUDGMENT for a conditional obligation (K-ROLE-2 when G-ROLE
    fails) that cannot be evaluated.
  - The rulebook has no slot for "trigger not evaluable".

**Candidate repair.** UNRECORDED_JUDGMENT, UNKNOWN and MR-6 UNKNOWN each require a stated
search. That search must cover all of these:

- a `_REGISTER.md` grep;
- decomposition DEC rows;
- `docs/harness/*register*`;
- the GOVERNING K-rows for the clause.

The search is recorded in Notes. UNKNOWN is reserved for evidence outside the §3 roots
(for example DEL-06-04 `#CLM-009.5`, which depends on Codex binary behavior).

### 4.4 Legacy or unreachable code ("implemented only on a retained path") handled inconsistently

*High frequency across 6 units. It moves Dispositions within one ledger.*

The same fact appears again and again: a full implementation exists on the retained Claude
SDK or in-process path (`lib/harness/runtime.ts` has no non-test importer), while the live
Codex path has nothing, or only an upstream substitute. The ledgers disposition that fact
in several ways.

- **DEL-06-04:**
  - IMPLEMENTED_DIFFERENTLY: `#CLM-009.1`, `.6`, `.7`, `.12` and `.13`;
  - PARTIALLY_IMPLEMENTED: `#CLM-009.3`, `.4` and `.5`;
  - ALIGNED: `#CLM-009.11` (CONTESTED).
- **DEL-04-05:**
  - `#CLM-028` is ALIGNED on unwired base-URL code, while `#CLM-009.6`, `.7` and `.11`
    treat the same code as unwired;
  - `#CLM-004.1` and `#CLM-009.15` carry different CauseTags for the same substance.
- **DEL-01-01 `#CLM-004.1`, `#CLM-009.2` and `#CLM-021` (CONTESTED).** The legacy MCP
  `status_transition` accepts an agent-supplied actor. It is not reachable in production.
- **DEL-08-04:**
  - `#CLM-003.1` and `#CLM-010.3` are REFUTED on evidence, because `evaluateSubagentGovernance`
    is called only by the legacy `turn-engine.ts:232`;
  - `#CLM-005.2` (stale) conflicts with `#CLM-030.1` (ALIGNED) over the same path list.
- **DEL-10-01:** `#CLM-004.1` is measured against product reachability, while `#CLM-021.4`,
  `#CLM-024` and `#CLM-002` are measured against the code surface.
- **SURFACES:** CAP-HARNESS-058 describes disabled legacy code as live (§4.8).

**Candidate repair.**

- Add `ImplementationReach = LIVE | LEGACY_ONLY | BOTH | NONE` to the ledger. Proposed
  independently by the DEL-06-04 worker and shard, and by the DEL-04-05 shard.
- Add one rule: a requirement met only on a LEGACY_ONLY path is PARTIALLY_IMPLEMENTED (or
  IMPLEMENTED_DIFFERENTLY where the live path substitutes upstream behavior), with a single
  CauseTag.

### 4.5 MR-8 on retired deliverables and on claims that are true of a snapshot (RETIRED_BY_RULING candidate)

*High frequency. About 25 CONTESTED items and 1 REFUTED item in 6 units.*

**(a) Retired deliverable (DEL-09-07).**

- The 24 ACCEPTED_DIVERGENCE rows were tested against MR-8's two limbs.
  - The GOVERNING-ruling limb is satisfied on all 24. D-APP-127 names DEL-09-07 retired
    and preserves the folder as immutable history.
  - The text limb is satisfied by the SoW itself (`ScopeOfWork.md:19-20`, `:66-69`,
    `:86-87`). The worker's premise that only `_STATUS.md` acknowledges the gate was wrong.
  - Result: 21 rows hold, and 3 are CONTESTED (`#SEC-2.1`, `#SEC-2.5`, `#SEC-2.13`).
- `#STATE-2` (`_CONTEXT.md`) is REFUTED. It should be ACCEPTED_DIVERGENCE with
  HumanDecisionNeeded NO, because it sits in the same preserved folder.
- `#REGISTER-1` (`Dependencies.csv`) is CONTESTED.
- No rule covers vacuous satisfaction (an exclusion that holds only because nothing was
  built). `#SEC-1.5` is ALIGNED, while `#SEC-2.5` and `#SEC-4.2` are ACCEPTED_DIVERGENCE.
- The V-DEL-09-07 shard assessed the **RETIRED_BY_RULING** candidate as adding real signal.
  - It separates "withdrawn in whole" from "legitimately differs".
  - It would have made STATE-2 consistent with the SoW rows.
  - It could collapse about 27 rows to about 4.
- **Suggested definition:** a GOVERNING ruling names the deliverable or scope item retired
  **and** preserves its text as history. The MR-8 text limb is then waived only for text
  inside the preserved set.
- **Open owner question:** machine registers inside a preserved folder, which can still
  feed dependency tooling.
- **Alternative:** a one-sentence MR-8 clarification.

**(b) Claims that are literally true of a stale snapshot or record.**

These are the REF-006 "MATCH" and "reconciled under D-APP-38" clauses. At `00115c719`,
`docs/PRD.md` hashes to `17ca3f3c…`, while `_REFERENCES.md` and corpus v23 record
`8649ccba…`. The ledgers dispositioned this three ways:

- **STALE_SPECIFICATION:** DEL-01-01 `#CLM-003.2` (HIGH) and `#CLM-015`, and DEL-03-01_B
  `#CLM-013.1`;
- **STALE_VERIFICATION:** DEL-01-01 `#CLM-017.2` (LOW);
- **NOT_AUDITABLE:** DEL-02-05 `#CLM-001`, `#CLM-006`, `#CLM-014` and `#CLM-021`, and
  DEL-03-01 A and B `#CLM-010`.

Two further findings sit here:

- DEL-06-04 `#CLM-018.2` relies on a premise that flipped twice (mismatch → MATCH →
  drift), and `#CLM-016` reasons circularly from the stale MATCH record.
- DEL-02-05 `#CLM-010.10` marks a facade that is deprecated but still live as
  STALE_SPECIFICATION, although D-APP-118 is AWAITING_RULING.

**(c) Stale CONTEXT_CLAIM and dated-history rows.**

- DEL-03-01_A `#CLM-023` and `#CLM-025` are STALE_SPECIFICATION, but `#CLM-010` and
  `#CLM-024` are NOT_AUDITABLE.
- DEL-08-04 `#CLM-033` (NOT_AUDITABLE) differs from `#CLM-007`, `#CLM-016.1`, `#CLM-031`
  and `#CLM-032`.
- DEL-10-01 `#CLM-028.1`.
- DEL-09-07 `#SEC-2.1`.

**Candidate repair.**

- Adopt RETIRED_BY_RULING, scoped to the preserved-history set.
- Route a clause that is literally true of a stale record to a REGISTER-n defect on that
  record. Reserve STALE_SPECIFICATION for flat present-tense assertions.
- State that a CONTEXT_CLAIM containing a checkable state assertion is split, with the
  assertion typed as STATE_ASSERTION.
- State which wins when a SoW self-labels earlier sections "dated history".

### 4.6 AuthorityTier drift

*High frequency (about 35 rows noted). 2 REFUTED. Metadata only: no Disposition changes.*

- **PRD was used where the row restates SPEC or TYPES,** so it should be
  GOVERNANCE_INVARIANT under "highest tier restated":
  - DEL-02-05 `#CLM-003`, `#CLM-005`, `#CLM-010.1` to `.3`;
  - DEL-03-01_B `#CLM-003.2`, `.3`, `#CLM-005.1`, `#CLM-009.5`, `.9`, `.11`, `#CLM-018.4`,
    `#CLM-004.2` and `#CLM-018.1`;
  - DEL-10-01 `#CLM-004.1` and `#CLM-014.2` (SPEC §18 rows are PRD, while CONTRACT
    K-DOMAIN rows are GOVERNANCE_INVARIANT);
  - DEL-06-04 `#CLM-005` and `#CLM-025` (tagged LOCAL_DESIGN).
- **CONTEXT_CLAIM rows were not given NOT_APPLICABLE:**
  - DEL-04-05 `#CLM-010` (GOVERNANCE_INVARIANT) and `#CLM-012` (LOCAL_DESIGN), both REFUTED;
  - DEL-06-04 `#CLM-017`, `#CLM-024`, `#CLM-026` and `#CLM-029`;
  - DEL-10-01 `#CLM-028.1`.
- **NOT_APPLICABLE was used on STATE_ASSERTION rows,** which the rule neither permits nor
  forbids:
  - DEL-04-05 `#CLM-001`, `#CLM-007`, `#CLM-015`, `#CLM-023`, `#CLM-004.4` and `#CLM-014.1`;
  - DEL-06-04 `#STATE-1` (GOVERNANCE_INVARIANT, while its sibling STATE_ASSERTION rows are
    NOT_APPLICABLE).
- **GOVERNANCE_INVARIANT was stretched to App decisions and ownership partitions:**
  - DEL-09-07 `#SEC-2.5` and `#SEC-2.13`;
  - DEL-09-07 `#REGISTER-2` has PRD for a decomposition register defect.

**Candidate repair.**

- State that App `docs/{DIRECTIVE,CONTRACT,SPEC,TYPES}.md` count as GOVERNANCE_INVARIANT.
- Add a tier for decomposition and App-decision authority (for example `APP_DECISION`).
- Say explicitly whether STATE_ASSERTION takes NOT_APPLICABLE.
- Have the validator enforce CONTEXT_CLAIM ⇒ NOT_APPLICABLE.

### 4.7 PostReleaseBasis set by assumption

*Every unit. The outcome was 1 row wrong.*

- **How the workers set it:** several forward workers set `NO` on every row by assumption.
  DEL-04-05, DEL-08-04 (all 80 rows) and DEL-03-01_B did so, and DEL-06-04 said so in its
  friction item 3.
- **How the shards checked it:** every shard checked the four post-v3.0.1 commits
  (`da95ec194`, `cb08dbe2f`, `9ecbdecdf`, `ccb95e06a`) with `git show --stat` or `blame`.
- **Result:** exactly **one** row is wrong. DEL-06-04 `#CLM-009.10` relies on
  `codex-supervisor.ts:653` (cited as `:655`), which `da95ec194` authored. The aggregator
  confirmed this by blame (§2).
  - Its Disposition, ALIGNED, is unaffected. The parent of `da95ec194` returned the same
    refusal.
  - The load-bearing fact is that the frontend binds no application tools
    (`runtime-service.ts:580` passes `mcpServers: []`).
- **How it was caught:** the reverse notes already caught it, but it could not be written
  back (§4.9).
- **Near misses:** `da95ec194` also touches `session-store.ts` and
  `app-owned-composition.ts`, which several rows cite. The relied-on lines predate it.

**Candidate repair.** Compute PostReleaseBasis mechanically: a script blames each cited
`path:line` range against the four commits. Alternatively, require a per-row blame
statement. It should never be set by assumption.

### 4.8 Capability-file accuracy and granularity

*Low frequency, but it affects every reverse pass that uses the file.*

**Accuracy.**

- **CAP-HARNESS-058 is REFUTED** (spot-checked, §2).
  - The capability text "executable subagent bridge (D-APP-10 Option C)" was taken from
    symbol names and the ruling reference.
  - In fact the bridge is disabled: `createExecutableSubagentBridge` returns `undefined`,
    and the preflight is hard-denied.
  - The `LEGACY-IN-PROCESS` tag was correct. So the reachability tag does not prevent a
    behavior misdescription.
- **Nits** (none blocking):
  - 016: an EntryPoint is missing;
  - 021: the EntryPoint is a type-only importer, and the real consumer is `chat-panel.tsx:1673`;
  - 024: CoveringTests is incomplete;
  - 028: the Notes invert the direction of the fake-port import.

**Granularity.**

- CAP-HARNESS-011 and 021 are CONTESTED as per-function rows. Each is an 8- or 11-line file.
- The 60-row ceiling was hit because the area mixes a thin live layer (001–027) with a
  legacy engine (028–060).

**Response rule.**

- CAP-HARNESS-013 → DEL-02-05 `#CLM-010.6`, and CAP-HARNESS-056 → DEL-08-04 `#SEC-1.1`,
  are CONTESTED as CLAIMED_BY versus PARTIAL. In both, the capability is broader than the
  claim, or the Rationale itself says ownership is shared.
- CAP-HARNESS-057: the DEL-08-04 shard reads it as PARTIAL, with CLM-014 or CLM-005.1 as
  the covering key, not NOT_MINE.

**Candidate repair.**

- Add capability columns `Reachability` (PRODUCTION / SCRIPT_ONLY / TEST_ONLY / TYPE_ONLY)
  and `BehaviorStatus` (LIVE / DISABLED / RETIRED). BehaviorStatus is verified from code
  paths, not names.
- Alternatively, add a `HARNESS_LEGACY` sub-area.
- Add a rule: shared ownership stated in the Rationale, or a capability broader than the
  claim, ⇒ PARTIAL.

### 4.9 The reverse pass exposed forward errors that have no route back into a sealed ledger

*Structural. Several units.*

The sealed-ledger rule (§5) is doing its job: no sealed file changed (§1). But corrections
found in reverse notes have no defined route into the effective ledger. Examples:

- DEL-01-01 `#CLM-004.1`, `#CLM-009.2` and `#CLM-021`: declared-actor check. The reverse pass
  found it, and the shard marked the rows CONTESTED with "reverse-notes correction not in
  sealed ledger".
- DEL-06-04 `#CLM-009.10`: the PostReleaseBasis error.
- DEL-04-05 reverse E-1: the oMLX D-APP-72 scope was delivered but has no forward row, a
  coverage gap. Reverse E-2 is an uncited `api-key-store.ts:33-45`.
- DEL-03-01_A: the reverse-notes revisits (`#CLM-012.2`, `#CLM-019`, `#REGISTER-1`,
  `#CLM-009.9`, `#CLM-021/003.4`) were accepted by the shard.
- DEL-10-01: the reverse notes misdate the facade relocation.

**Candidate repair.** Add an append-only `<DEL-ID>_errata.csv` next to the sealed ledger:

- Columns: `ClaimKey, Field, SealedValue, CorrectedValue, Source (REVERSE | VERIFIER), Evidence, VerifierVerdict`.
- The effective ledger is the sealed ledger with the verified errata applied.
- The verifier confirms each erratum.
- The manager merges errata at R-stage close.
- New rows found in reverse (coverage gaps) enter as errata rows with a run-local key.

### 4.10 Lesser patterns, and a verifier-calibration note

**CauseTag on rows with two causes.**

- These rows carry one CauseTag although two causes apply:
  - DEL-03-01_A `#CLM-009.10`, `#CLM-017` and `#CLM-025`. `#CLM-025` is REFUTED to
    PRE_V3_DRIFT: `4412157d1`, 2026-07-22.
  - DEL-03-01_B `#CLM-016` and `#CLM-018.4`.
  - DEL-08-04 `#CLM-032` and `#CLM-016.8`.
  - DEL-10-01 `#CLM-007.1`, `#CLM-016.1` and `#CLM-028.1`, where PRE_V3_DRIFT and
    UNRECORDED_JUDGMENT overlap.
- The REF hash drift is split across tags: CARRIER_PROPAGATION versus DOC_HYGIENE in
  DEL-06-04.
- Proposal: a precedence rule (mechanism tag > PRE_V3_DRIFT > UNRECORDED_JUDGMENT), or a
  secondary-cause field.

**Gate semantics under MR-2 and MR-6.**

- DEL-03-01 `#REM-2` is CONTESTED in *both* shards: does App code count as an "App
  surface" for a Runtime-owned gate?
- DEL-08-04 `#REM-3`: the meaning of a gate that says an item is "selected" is undefined.
- DEL-08-04 `#REM-2`: MR-6 UNKNOWN was applied correctly.

**Split inconsistency.**

- DEL-03-01_B `#CLM-003.1` versus `#CLM-009.2`.
- DEL-10-01 `#CLM-002`: an unsplit posture row.
- DEL-09-07 `#SEC-2.13`: a paragraph that is part valid, part moot.

**Evidence and verification precision.**

- DEL-06-04 `#CLM-009.6`: the cited test covers policy denials, not hook failure.
- DEL-01-01 `#CLM-009.4`: the `DOC-BASIS(D-APP-127)` token is misattributed.
- DEL-01-01 `#CLM-009.11`: the MR-1 token contradicts the row's own Disposition.
- DEL-01-01 `#CLM-009.7`: the evidence is a legacy test.
- Line drift of 1–6 lines appears in several units. It is immaterial.

**OTHER token.**

- DEL-01-01 `#CLM-017.3` introduces `OTHER:PENDING_HUMAN_GATE`. The manager must report it
  (CONVENTIONS §4).

**Missed register defects.**

- DEL-02-05: the `_REFERENCES.md` hash rows.
- DEL-08-04: the stale DEP-08-04-012 note (`_CONTEXT.md:58` lists SOW-063 and SOW-083).
- DEL-01-01: `Table_Conflict_Source_Warnings_DEL-01-01.md:18` still carries C002 OPEN.

**Verifier-calibration note: shards differed in severity.**

- **HANDOFF misgloss.** The same HANDOFF L126-128 misgloss appears in both double-blind
  ledgers.
  - Shard A graded it **REFUTED** on DirectionEvidence (6 rows).
  - Shard B graded the parallel rows **CONFIRMED**, with a ConventionIssue note.
- **Line anchors.** The shards also disagreed on the basis to check them against.
  - Shard A treated the decomposition L303-versus-L317 difference as minor drift.
  - Shard B REFUTED `#REGISTER-3`'s line anchor, holding that L303 is correct at the
    SoW's pinned `decomposition_basis` `d6f6cadb2`.
- **Consequence.** Per-shard REFUTED counts are therefore not strictly comparable across
  units.
- **Proposal for the verifier brief:**
  - a wrong citation or gloss whose Disposition holds is REFUTED on that field;
  - line anchors are checked against the pinned basis named in the deliverable, with the
    frozen-tree line also given.

### Pattern ranking summary

| Rank | Pattern | Items (approx.) | Units | Can change Disposition or route? |
|---:|---|---:|---:|---|
| 1 | MR-11 vs AUTHORITY_CONFLICT (4.1) | ~30 | 6 | Yes (Disposition and R4) |
| 2 | Legacy/unreachable path inconsistency (4.4) | ~20 | 6 | Yes |
| 3 | MR-8: retired deliverables, snapshot-true claims, stale CONTEXT_CLAIM (4.5) | ~26 | 6 | Yes |
| 4 | Missing register search before UNRECORDED_JUDGMENT / UNKNOWN (4.3) | 7 | 3 | Yes (2 Disposition refutations) |
| 5 | DirectionEvidence CONTEXT vs GOVERNING (4.2) | ~37 | 6 | Indirectly |
| 6 | Reverse→ledger route missing (4.9) | ~10 | 5 | Blocks correction |
| 7 | Capability accuracy and granularity (4.8) | 5 | 1 area | Affects reverse ownership |
| 8 | PostReleaseBasis by assumption (4.7) | 1 wrong | all | No (in this sample) |
| 9 | AuthorityTier drift (4.6) | ~35 | 7 | No (metadata) |

*End of VERIFICATION.md. This is verification evidence for the R0 gate, not a ruling.*
