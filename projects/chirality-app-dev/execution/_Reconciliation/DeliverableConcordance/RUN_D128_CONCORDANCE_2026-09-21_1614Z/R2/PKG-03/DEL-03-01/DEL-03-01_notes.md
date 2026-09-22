# DEL-03-01 — R2 forward-pass notes (PKG-03, RUN_D128)

Basis: frozen tree `00115c719`. Ledger: `DEL-03-01_claims.csv`, 105 rows. Validator: `RESULT PASS errors=0 warnings=0`.
Owner-direction additions received before sealing (RUN_BASIS Addenda 4–5) were applied: the
STALE_SPECIFICATION / REMAINING_STATE_MISMATCH tie-break (with `ALSO:` notes), and R4-Q4. No row
turns on R4-Q4.

## 1. Census

**Units:** 28 indexed (26 CLM + 2 REM), all covered, plus 9 run-local rows (REGISTER-1..7, STATE-1..2).
**Split rate:** 12 of 26 CLM units split (46%): CLM-003 (9), 004 (7), 005 (7), 006 (7), 009 (15, one per
REQ-001..015), 011 (6, one per indexed SubItem), 013 (2: warning text + AC-001), 016 (6), 018 (8),
019 (2: records + VER-001), 022 (6), 024 (5). The table units were split because their rows
disposition differently.

**Rows by Disposition (all rows / excluding SEE rows):**

| Disposition | All | Non-SEE |
|---|---:|---:|
| ALIGNED | 35 | 29 |
| STALE_SPECIFICATION | 39 | 22 |
| PARTIALLY_IMPLEMENTED | 10 | 10 |
| DOCUMENTED_UNIMPLEMENTED | 7 | 3 |
| AUTHORITY_CONFLICT | 7 | 2 |
| REMAINING_STATE_MISMATCH | 3 | 3 |
| NOT_AUDITABLE | 4 | 4 |
| **Total** | **105** | **73** |

**SEE rows (counted separately, MR-4):** 32.

**By ClaimType × Disposition:**
- REQUIREMENT (68): ALIGNED 30, STALE_SPECIFICATION 15, PARTIALLY_IMPLEMENTED 9, DOCUMENTED_UNIMPLEMENTED 7, AUTHORITY_CONFLICT 7.
- STATE_ASSERTION (19): STALE_SPECIFICATION 15, ALIGNED 4.
- CONTEXT_CLAIM (8): NOT_AUDITABLE 4 (headings), STALE_SPECIFICATION 4.
- REGISTER_DEFECT (7): STALE_SPECIFICATION 5, REMAINING_STATE_MISMATCH 2.
- REMAINING_WORK (2): ALIGNED 1 (REM-1), REMAINING_STATE_MISMATCH 1 (REM-2).
- ACCEPTANCE (1): PARTIALLY_IMPLEMENTED 1 (AC-001).

**HumanDecisionNeeded:** NO 82; R4-Q2 12; R4 8; `R4-Q2; R4` 2; D-APP-118 1.
**Confidence:** HIGH 59, MEDIUM 45, LOW 1. **PostReleaseBasis:** all NO.
No errata file (forward pass only).

## 2. Least-confident rows (with alternative readings)

- **CLM-018.7 (LOW): redaction.** No API key is in Chirality's custody on the Codex path, and
  App Server stderr is redacted (`codex-app-server-client.ts:44-45,70`). I found no structural
  redaction of `codex.notification` params before `persistEvent`. The search was `redact` in
  `packages/core/src` and `session-store.ts`. *Alternative:* ALIGNED, if Codex payloads never carry
  secrets or if redaction lives in a file I did not search.
- **CLM-003.9 / CLM-009.8 / CLM-011.3 / CLM-018.4 / CLM-022.2 (MEDIUM): conformance before the
  production default.** I chose DOCUMENTED_UNIMPLEMENTED with R4-Q2: unamended K-ENGINE-2 requires
  the suite, and Codex, the live default, never ran it. *Alternative:* AUTHORITY_CONFLICT, if
  D-GOV-43's sole-engine direction is read as displacing K-ENGINE-2 without naming it.
- **REM-2 (MEDIUM): REMAINING_STATE_MISMATCH with MechanicallyUnblocked YES.** The gate names code
  landing on the App production path. At the frozen basis, Electron `main.ts:455-471` launches the
  packaged Runtime service, `app-owned-composition.ts` serves the socket API, and the SSE repairs
  (keepalive, unsubscribe-only cancel) are present. *Alternative:* if "production path" means a
  released, packaged build, gate status needs a release carrier, and the value would be UNKNOWN.
- **CLM-004.1 / CLM-004.6 and their SEE rows (MEDIUM): AUTHORITY_CONFLICT.** See §4.
  *Alternative:* D-APP-127 retires the "closed event vocabulary" and names the DEL-03-01
  architecture-bound clauses. Read broadly, MR-11 could apply, which would make these rows
  STALE_SPECIFICATION. I did not take that reading, because D-APP-127 does not name K-ENGINE-4,
  SPEC §10.3 or TYPES §7.1, and those clauses still require translation.
- **CLM-009.15 / CLM-011.6 (MEDIUM): REQ-015.** I chose DOCUMENTED_UNIMPLEMENTED because the
  requirement stands but the deliverable's REF-006 state is not current. *Alternative:*
  STALE_SPECIFICATION, reading the row as a state claim.
- **CLM-009.12 / CLM-022.3 (MEDIUM): thin route, ALIGNED.** The Runtime TurnCoordinator fills the
  TYPES §7.1 TurnEngine role. *Alternative:* IMPLEMENTED_DIFFERENTLY, because SPEC §10.4 still says
  the route "obtains session lock" and forwards to `TurnEngine`, and the App `TurnEngine` is
  LEGACY_ONLY.
- **CLM-018.3 (MEDIUM): stub conformance, ALIGNED.** A scripted port with subject `stub` passes
  `runEngineConformance`. `StubAgentSdkManager` itself is never run through the suite.
  *Alternative:* PARTIALLY_IMPLEMENTED.
- **STATE-1 (MEDIUM).** `_CONTEXT.md` mirrors the decomposition row, so the stale daemon-client text
  may need repair upstream in the decomposition rather than in the deliverable.

## 3. Register-defect summary

- **REGISTER-1:** the `_REFERENCES.md` MATCH hashes for REF-002 (CONTRACT), REF-003 (SPEC) and
  REF-006 (PRD) do not reproduce (`HASH-RECOMPUTE@00115c719`). I also recomputed REF-001 (DIRECTIVE),
  REF-004 (TYPES), REF-005 (PLAN) and REF-007 (`workflows/software-decomp/WORKFLOW.md`); all of those
  reproduce. SoW rows that restate REF-006 as current point here with `SEE:`: CLM-004.7, 006.2,
  006.3, 006.6, 010, 013.1, 016.3, 018.8 and 026.
- **REGISTER-2:** the `_DEPENDENCIES.md` mirror is stale. It lists DEP-03-01-006 as ACTIVE/PENDING
  (it is RETIRED in the CSV), shows TBD placeholders for declared upstream and downstream, and its
  D-APP-56 "current" summary predates DEP-03-01-009.
- **REGISTER-3:** DEP-03-01-009 still targets "API v2 and event schema v2", although D-APP-127 revised
  V3-01 to the repaired socket API.
- **REGISTER-4:** DEP-03-01-008 is still PENDING although `section9.runtime_engine_contract` exists
  and is linked. This is lagging status (REMAINING_STATE_MISMATCH).
- **REGISTER-5:** DEP-03-01-003 is still a PREREQUISITE on the retired Claude SDK probe (DEL-04-01).
- **REGISTER-6:** the `Dependencies.csv` EvidenceFile/SourceRef columns cite `Datasheet.md`,
  `Specification.md`, `Procedure.md` and `Guidance.md`. None of these exists in the folder.
- **REGISTER-7:** the `_STATUS.md` `blocked-on:` line lists D-APP-47 and D-APP-48. Both are RULED,
  and D-APP-47 has been executed.
- **Other stale SoW text:**
  - The SoW references table names REF-007 as `agents/AGENT_SOFTWARE_DECOMP.md`, which is absent
    (CLM-006.7).
  - The Conflict Table (CLM-026) records CT-001 as resolved and omits the live GOVERNING tension.
  - The CLM-012 TBD list is stale.

## 4. Direction and cause

**Main CauseTags:**

| CauseTag | Rows | What it covers |
|---|---:|---|
| CODEX_SOLE_ENGINE | 33 | Claude SDK framing; the eight-name SSE set; the suite never run on Codex |
| DOC_HYGIENE | 19 | Hash drift and register lag |
| PRE_V3_DRIFT | 5 | SPEC §10.2 revision of 2026-07-22 not carried into the SoW |
| RUNTIME_EXTRACTION | 4 | SCA-APP-005 App-client scope not carried into the SoW |
| A2_TOPOLOGY | 3 | Topology A2 changes |
| FACADE_DEPRECATION | 1 | Harness-contract facade |
| CREDENTIAL_CUSTODY | 1 | Credential custody (CLM-018.7) |

**CAUSE2 secondaries:**
- CARRIER_PROPAGATION: CLM-003.6, 011.4, 016.5, REGISTER-3, REGISTER-5, STATE-1.
- PRE_V3_DRIFT: CLM-002, 005.7, 009.10.
- CODEX_SOLE_ENGINE: CLM-008, 017.
- RUNTIME_EXTRACTION: CLM-021, 025.
- DOC_HYGIENE: CLM-023, STATE-2.

**Key GOVERNING direction used:**
- **SCA-APP-005, `Handoff_State.md` derivative-state table.** It records "ScopeOfWork contracts and
  pins: FROZEN_STALE_REPAIR_REQUIRED". The decomposition row for DEL-03-01 was rewritten on
  2026-07-27 (`16f7ed612`) to App-client conformance against Root-owned contracts. The SoW was never
  rewritten; the A12 tranche of 2026-09-03 only re-pinned it.
- **D-APP-127.** It retires the closed event vocabulary, names the DEL-03-01 architecture-bound
  clauses as revised, and supports MR-11 for the SSE-names rows. The D-APP-127 application map shows
  that only `_STATUS.md` was revised.
- **D-APP-72.** SPEC §10.2 was revised on 2026-07-22 (blame `4412157d1`).
- **D-APP-47 / D-APP-89.** The shim was retired and the facade became a rollback re-export.

**CONTEXT source used:**
`execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/tranche/APP_EXECUTION_RETURN.md:45-47`.
It confirms that the D-GOV-43 tranche revised only `_STATUS.md` for DEL-03-01. This is the basis for
CARRIER_PROPAGATION. The V3-01 Remaining text (`_STATUS.md:15-22`) is cited as `CTX:` for the Codex
conformance rows.

**AUTHORITY_CONFLICT reasoning (CLM-004.1, primary; the others are SEE rows):**
- On the live path, canonical HarnessEvent types include `codex.notification`, `codex.request` and
  `codex.request.resolved`, carrying the upstream method and params (`event-schema.ts:44-47`;
  `delegated-engine-adapter.ts:282-308`). TurnCoordinator persists them.
- The amended texts require exactly this: K-EVENT-1 and K-EVENT-6, SPEC §11 and TYPES §7.4 (all
  D-GOV-43) say upstream names and payloads are preserved.
- The unamended texts require translation instead: K-ENGINE-4 ("must not become provider-shaped
  except as adapter metadata"), SPEC §10.3 ("MUST translate external message names…") and TYPES §7.1
  (EngineAdapter).
- The conflict is within CONTRACT, SPEC and TYPES themselves, so the DIRECTIVE §0 tier order does not
  resolve it. It stays AUTHORITY_CONFLICT with R4 (plain R4, since no named question fits).

**R4 citations:**
- R4-Q2 applies to every row that turns on Codex never having been run through K-ENGINE-2.
- R4-Q1 and R4-Q3 are not used. No DEL-03-01 row turns on keeping legacy harness code as an
  obligation or on the `status_transition` actor check.
- R4-Q4 is not relevant.

**NONE_FOUND searches:**
- I searched the App `_REGISTER.md` for these strings: `DEP-03-01`, `_DEPENDENCIES`,
  `AGENT_SOFTWARE_DECOMP`, `software-decomp`, `section9`, `Datasheet.md`, `Specification.md`,
  `four-document` and `DEL-03-01`.
  - `DEL-03-01` hits only rows 62, 104, 116 and 129 (D-APP-47, 89, 101, 114).
  - `_DEPENDENCIES` hits only D-APP-62, 109 and 110, none of which is specific to DEL-03-01.
- I searched these CONTEXT sources for `DEL-03-01`: `plans/steers`, the v3 release plan HTML and
  `AgentRuns/APP_V3_*`. The only relevant hit is the APP_EXECUTION_RETURN line cited above.
- These searches back NONE_FOUND on CLM-006.7, 016.2, 016.4, REGISTER-2, REGISTER-4 and REGISTER-6.

**Reach confirmation:**
- **Codex adapter (LIVE).** The live engine is `createDelegatedEngineAdapter`, registered in
  `app-owned-composition.ts:214`. The chain is `standalone-bin` → `standalone` →
  `app-owned-composition`, and the App launches it from Electron `main.ts:455-471` as the packaged
  `runtime-service/standalone-bin`. Turn policy runs in `TurnCoordinator`, reached from the
  `/api/harness/turn` route through `daemon-harness-port` to the Runtime socket.
- **`engine-conformance.ts` (map says LIVE; I tag TEST_ONLY).** REACHABILITY.csv reaches it only
  through the contracts barrel re-export. Nothing on the product path calls `runEngineConformance`;
  its only callers are App tests.
- **`frontend/packages/harness-contract` (TEST_ONLY).** It is outside the map. It is imported only by
  `harness-contract-rollback.test.ts` and by tooling scripts.
- **LEGACY_ONLY / UNREACHED, as the map says.** App `turn-engine.ts`, `runtime.ts`,
  `claude-agent-sdk-manager.ts` and `agent-sdk-manager.ts` are LEGACY_ONLY. `engine-claude` is
  UNREACHED.

**PostReleaseBasis:** the only touched file I cite is `app-owned-composition.ts`. I ran `blame -L` on
lines 33, 179, 214 and 226; they blame to `fca60696d`, `95364569a`, `95b342519` and `9eaddb596`. None
of these is one of the four release commits, so every row is NO. No App `frontend/**` path appears in
TOUCHED_PATHS.

## 5. Method friction

- **SEE precedence for table-first SoWs.** MR-4 disposes a statement on its earliest unit. In this
  SoW the Datasheet tables (CLM-003/004) come before the numbered REQ table (CLM-009), so REQ rows
  become SEE rows of table sub-rows. *Proposal:* allow the numbered REQ row to be the primary, with
  the earlier Datasheet restatement taking the SEE.
- **CLM-013 and CLM-019 each hold one indexed item plus unrelated prose.** I split them (`.1` prose,
  `.2` the AC/VER item). The splitting rule literally permits a split only for units with separately
  numbered items. *Proposal:* allow a prose/item split when k = 1.
- **CLM-011 SubItems list only the first REQ ID of each row** (for example, REQ-001 for the row
  covering REQ-001/002/007/013). I gave one row per SubItem and named the covered group in Notes.
- **`_REFERENCES.md` MATCH as a STATE_ASSERTION.** A literal CONTEXT_CLAIM rule would make a true
  MATCH row NOT_AUDITABLE, so I typed the CLM-006 rows as STATE_ASSERTION so that a true MATCH can be
  ALIGNED. *Proposal:* say explicitly that register MATCH restatements are STATE_ASSERTION.

## 6. Effort

- **Files read:** about 45, in full or by line range:
  - the whole deliverable folder except `_SEMANTIC*.md` and the run records;
  - the App DIRECTIVE §0, CONTRACT, SPEC §9–11 and TYPES §7;
  - the D-APP-127 ruling;
  - the SCA-APP-005 handoff;
  - Runtime contracts, core and daemon files;
  - App route, http, port and tests;
  - the evidence pack and gate transcripts.
- **Not read:** `_SEMANTIC.md` and `_SEMANTIC_LENSING.md` (85 KB, derivative lensing). The
  `_run_records/**` files were checked by name only.
- **Budget:** the context budget was adequate and not tight.
