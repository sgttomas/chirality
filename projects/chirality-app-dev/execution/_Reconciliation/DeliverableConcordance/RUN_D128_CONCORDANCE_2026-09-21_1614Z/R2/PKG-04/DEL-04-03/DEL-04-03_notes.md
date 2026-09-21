# DEL-04-03 — forward-pass notes (RUN_D128, R2, PKG-04)

- Sealed ledger: `DEL-04-03_claims.csv`, SHA-256 `09cd5f5799b97d43a9e52489cf026b0f1e47dc66a0e68ed3eb62506ce728c605`.
- Validator: `RULES errors none | warnings none`; `RESULT PASS errors=0 warnings=0`.
- Basis: frozen tree at `00115c719`. PostReleaseBasis is `NO` on every row:
  - the only touched file cited is `packages/daemon/src/app-owned-composition.ts`;
  - `git blame -L` on its lines 13 and 214 gives `95364569a` and `95b342519`, neither of which is one of the four post-release commits.

## 1. Census

### Totals

- 55 rows:
  - 48 rows cover the 27 indexed units;
  - 7 are run-local: REGISTER-1..5 and STATE-1..2.
- No errata yet. No errata file exists, so there are no errata-applied figures.

### Rows by ClaimType × Disposition

| ClaimType | ALIGNED | PARTIALLY_IMPL. | STALE_SPEC. | DOC_UNIMPL. | NOT_AUDITABLE | REM_STATE_MISMATCH | LIFECYCLE_REASSESS. | Total |
|---|---|---|---|---|---|---|---|---|
| REQUIREMENT | 14 | 11 | 4 | 2 | – | – | – | 31 |
| ACCEPTANCE | 2 | 1 | – | – | – | – | – | 3 |
| STATE_ASSERTION | – | – | 6 | – | – | – | 1 | 7 |
| CONTEXT_CLAIM | – | – | 1 | – | 8 | – | – | 9 |
| REGISTER_DEFECT | – | – | 3 | – | – | 2 | – | 5 |
| **Total** | 16 | 12 | 14 | 2 | 8 | 2 | 1 | 55 |

### Splits

- 4 of the 27 indexed units are split (14.8%), giving 25 rows:
  - CLM-004 → .1–.7, one row per Conditions table row;
  - CLM-009 → .1–.14, one per DEL-04-03-REQ001..REQ014;
  - CLM-013 → .1 for the amendment and .2 for AC-001;
  - CLM-019 → .1 for Records and .2 for VER-001.
- CLM-013 and CLM-019 each list one sub-item. They were split because the amendment and records text dispositions separately from the AC and VER item.

### SEE rows

There are 5 SEE rows, counted separately:

| Row | Points to |
|---|---|
| CLM-009.4 | CLM-003 |
| CLM-009.9 | CLM-004.4 |
| CLM-009.11 | CLM-004.1 |
| CLM-024 | CLM-022 |
| CLM-025 | CLM-009.3 |

### HumanDecisionNeeded other than NO

There are 2 such rows:

- CLM-004.6 → `R4-Q2`;
- STATE-2 → `R4-Q1`.

### Reading applied (rule §2.3 and reminder 4)

**Module-level reading.** Some clauses are about the Claude Agent SDK mapper:
- they name `sdk-message-mapper.ts`, or the SDK message types and categories;
- this applies to CLM-004.4, CLM-005, CLM-008 (partly), CLM-009 REQ001–003, REQ005–010 and REQ012–013, CLM-010 and CLM-012–CLM-025.

These clauses are judged at module level, with `REACH=LEGACY_ONLY`:
- the SoW's own subject is the retained module;
- the App CONTRACT, SPEC and PRD "Current Codex-only MVP release basis" preambles describe Claude material as compatibility history.

**Live-path reading.** Other clauses govern surfaces that do not depend on the engine: the route and SSE, the browser contract, the port boundary, event separation, runtime-event redaction and production-default conformance. These are:
- CLM-004.1–.3, CLM-004.5, CLM-004.6;
- REQ004 and REQ011.

They are judged on the Codex path, through `packages/core/src/delegated-engine-adapter.ts`, which is registered at `app-owned-composition.ts:214`.

## 2. Least-confident rows

- **CLM-004.5** (LOW, DOCUMENTED_UNIMPLEMENTED). This covers redaction of live runtime event data.
  - What I found: the Codex adapter forwards raw notification params into `codex.notification` HarnessEvents. I found no redaction step in Runtime `core/src` or `daemon/src`.
  - Alternative 1: a redaction sink exists outside the files I searched. The row would then be ALIGNED.
  - Alternative 2: Codex credential custody retires the premise about configured secrets. The row would then be STALE_SPECIFICATION.
- **CLM-009.13** (LOW, ALIGNED). This covers REQ013, terminal outcomes.
  - What the mapper does: it emits success and failure terminals. Interruption is emitted by `claude-agent-sdk-manager.ts`, and the SDK has no cancellation message.
  - Alternative: a literal reading of "mapper MUST expose … interruption and cancellation" makes the row PARTIALLY_IMPLEMENTED.
- **MEDIUM rows worth a second look:**
  - **CLM-002.** It is STALE because the cell restates the `_REFERENCES.md` status token, which has been MATCH since 2026-07-23. However, the PRD file really does mismatch at the frozen basis, as REGISTER-3 records. An ALIGNED reading is possible.
  - **CLM-004.1 / CLM-009.11.** These are ALIGNED because the legacy names are still emitted. REQ004 is STALE because it fixes the contract to the superseded closed set. The two readings are consistent but close to each other.
  - **CLM-008.** It is STALE against the accepted SCA-APP-005 App-client boundary. Another reading takes the SoW scope as a compatibility-history description of the retained module, which would make it ALIGNED.

## 3. Register-defect summary

- **REGISTER-1..3.** In `_REFERENCES.md`, the recorded MATCH hashes for CONTRACT, SPEC and PRD (REF-002, REF-003, REF-006) do not reproduce.
  - They did reproduce at the v23 re-hash `23b3879b3` on 2026-09-12.
  - CONTRACT then changed in `95b342519` and `7f1e9f387`, and SPEC and PRD changed in `9eaddb596`.
  - DIRECTIVE, TYPES and PLAN still reproduce (`shasum`).
- **REGISTER-4.** In `_DEPENDENCIES.md`, the Declared Upstream and Downstream sections still read "TBD – no accepted edges", which contradicts its own 11-row register. Its REF-006 HASH_MISMATCH warning contradicts `_REFERENCES.md`.
- **REGISTER-5.** Several cells in `Dependencies.csv` have gone stale:
  - the DEP-04-03-001 EvidenceQuote no longer matches `_CONTEXT.md`, which was rewritten under SCA-APP-005;
  - DEP-04-03-008..011 cite the retired `Specification.md` in EvidenceFile, SourceRef or TargetLocation.
- **SoW rows that restate REF-006 hash state** cite REGISTER-3: CLM-002, CLM-016 and CLM-027.

## 4. Direction and cause

### CauseTags

| CauseTag | Rows | Notes |
|---|---|---|
| PRE_V3_DRIFT | 21 | Mapper gaps date from 2026-05-24 and 2026-06-13. Carrier lag follows the 2026-07-13 SoW migration and the 2026-07-18 probe closure. |
| A2_TOPOLOGY | 3 | CLM-003, CLM-009.4, STATE-1 |
| DOC_HYGIENE | 3 | REGISTER-1..3 |
| RUNTIME_EXTRACTION | 2 | CLM-008, CLM-004.5 |
| CODEX_SOLE_ENGINE | 2 | CLM-004.6, STATE-2 |

### CAUSE2 secondaries

| Secondary | Rows |
|---|---|
| CARRIER_PROPAGATION | CLM-002, CLM-004.7, CLM-008, CLM-009.14, CLM-011, CLM-016, CLM-023 |
| PRE_V3_DRIFT | CLM-003 |
| CODEX_SOLE_ENGINE | CLM-009.4, STATE-1 |
| CREDENTIAL_CUSTODY | CLM-004.5 |
| DOC_HYGIENE | REGISTER-4, REGISTER-5 |

### Records used

- **GOVERNING:**
  - `GOV:D-GOV-43` on CLM-003, CLM-009.4 and STATE-1: the amended CONTRACT K-EVENT-1, SPEC §11 and TYPES §7.4 supersede the fixed UIEvent set, and the daemon topology is retired;
  - `GOV:SCA-APP-005` on CLM-008, which qualified the DEL-04-03 work-product boundary to the App client.
- **CONTEXT:** `R0_DONE_DECLARATION/V3_DONE_DECLARATION_CANDIDATE.md` §2 OOS-01/OOS-02, on STATE-2. It explains the direction only and does not change the Disposition.

### Searches behind each NONE_FOUND

- **Register:** grep of `_DECISIONS/_REGISTER.md` for `DEL-04-03`, `mapper` and `Codex`.
  - No row names DEL-04-03 or the mapper.
  - D-APP-56 names DEL-04-03 in its ruling (P34, which is applied on CLM-013.1).
  - No ruling is recorded for the Codex-only preamble. It entered SPEC in `2f825f180` (2026-09-10).
- **DECISION_HITS.csv rows for DEL-04-03:** D-APP-06, 19, 52, 54, 55, 56 and 72. None explains the recorded divergences.
- **CONTEXT sources:** the done-declaration candidate (grep for DEL-04-03, mapper, conformance and PKG-04). The `plans/steers` folder is absent at the frozen basis, and grep of `plans/` finds no hits for DEL-04-03 or sdk-message-mapper.

## 5. Method friction

- **CLM-002 and CLM-027.** The SoW states a register status token (HASH_MISMATCH). The register later recorded MATCH, and the file has since drifted again.
  - The rules do not say whether a claim about a register token is judged against the register or against the recompute.
  - I judged it against the register and carried the recompute in REGISTER-3.
  - Proposal: add an MR-8 note that SoW restatements of register status are judged against the register.
- **MR-4 with table units.** The earliest unit restating a statement is often a multi-item Attributes or Conditions table, as with CLM-003 versus REQ004.
  - SEE rows then point at a unit whose Disposition is driven by several items.
  - I split CLM-004 so that its SEE targets are item-level. CLM-003 was left unsplit.
  - Proposal: when the earliest occurrence sits in a multi-item table, allow the SEE target to be the first single-item row instead.
- **An accepted SCA in DirectionEvidence.** `GOV:` expects a ruling. SCA-APP-005 is GOVERNING, as an accepted SCA under RUN_BASIS §5, but it has no D-APP ID, so I cited it by path.
- **Tier for PLAN.md.** PLAN ranks above PRD in DIRECTIVE §0, but the tier vocabulary has no value for it. CLM-004.5 cites PLAN §6.3 and PRD FR-075, and I tiered it PRD.

## 6. Effort

- About 30 files or slices read:
  - the deliverable carriers, the INSP-03 assessment, and slices of SPEC, TYPES, CONTRACT, DIRECTIVE and PRD;
  - the mapper and its test, the delegated adapter, contracts types and event-schema;
  - the pack CSVs, the SCA-APP-005 preview, and targeted `git log`, `show` and `blame`.
- The context budget was adequate but not loose. The redaction sweep of the live path was kept to grep over Runtime `core` and `daemon`, the live route and the App `lib`.
