# DEL-04-03 — forward-pass notes (R2, PKG-04, rerun)

Ledger: `DEL-04-03_claims.csv`, 64 rows plus `#END`. Validator: `RULES errors none | warnings none`, `RESULT PASS errors=0 warnings=0`.
Sealed SHA-256: `f2e6c8475bcc21717d2b8a790a7d41b7ccdef9858a6079b60f8eb9c014b211eb`.

## 1. Census

**By Disposition (sealed):** STALE_SPECIFICATION 22, ALIGNED 19, PARTIALLY_IMPLEMENTED 10,
NOT_AUDITABLE 7, IMPLEMENTED_DIFFERENTLY 4, REMAINING_STATE_MISMATCH 1,
LIFECYCLE_REASSESSMENT_REQUIRED 1.

**By ClaimType:** REQUIREMENT 38, STATE_ASSERTION 13, CONTEXT_CLAIM 8, REGISTER_DEFECT 3, ACCEPTANCE 2.

**By CauseTag:** NONE 26, PRE_V3_DRIFT 20, CODEX_SOLE_ENGINE 15, DOC_HYGIENE 3.

**Confidence:** HIGH 33, MEDIUM 31, LOW 0.

**HumanDecisionNeeded other than NO (6):** R4-Q1 on CLM-008, CLM-015, CLM-021 and STATE-1; R4-Q2 on CLM-004.6 and CLM-011.7.

**Coverage and split rate:** all 27 indexed units covered. Six units are split (22%):
- CLM-003, 6 rows, attribute table;
- CLM-004, 7 rows, conditions table;
- CLM-009, 14 rows, REQ001–REQ014;
- CLM-011, 8 rows, verification table;
- CLM-013, 2 rows, the amendment plus AC-001;
- CLM-019, 2 rows, the records plus VER-001.

The index lists SubItems only for CLM-013 (AC-001) and CLM-019 (VER-001). Each has its own row.
The ledger also has four run-local rows: REGISTER-1..3 and STATE-1.

**SEE rows (6, counted separately):**
- CLM-009.3 and CLM-025 point to CLM-003.4;
- CLM-011.5 points to CLM-003.6;
- CLM-011.7 points to CLM-004.6;
- CLM-015 and CLM-021 point to CLM-008.

With the SEE rows removed, the ledger has 58 independently dispositioned rows.

**Errata:** none (forward pass only).

**Readings applied (brief reminder 2).** When a requirement's subject is the mapper itself
(REQ001–003, 005–010, 012–014, CLM-003.4/.5, CLM-005, CLM-012, CLM-013.1, CLM-017/018/019.1,
CLM-025), the row is judged at **module level** against `sdk-message-mapper.ts`, tagged
`REACH=LEGACY_ONLY`. When a unit describes product behaviour, it is judged on the **live path**:
the browser contract, route/SSE compatibility, the model/tool loop, conformance before production
default, and the deliverable scope/purpose (CLM-003.2, CLM-004.1–.4, .6, CLM-008, CLM-015,
CLM-021, REQ004, REQ011). The live path is the Codex App Server via the Runtime
`delegated-engine-adapter.ts`, `REACH=LIVE`. Each row's Notes names the reading applied.

## 2. Least-confident rows (with alternative readings)

There are no LOW rows. The MEDIUM rows most open to refutation are these:

- **CLM-003.4 / CLM-009.3 / CLM-025 (PARTIALLY_IMPLEMENTED).**
  - Ledger reading: raw SDK tool names appear in `tool:result.data.name` and in HarnessEvent
    `data.toolName` beside `adapterToolName`. `claudeSessionId` appears in `session:init`.
  - Alternative: the `UIEvent` type in `runtime-contracts` declares `claudeSessionId` and
    `tool:result.name`, and HarnessEvent `data` is open. Under that reading these fields are
    accepted Chirality contract fields, REQ003 is met, and the row is ALIGNED; this matches the
    INSP-03 PASS. Under the ledger reading, the assessment is marked OVERTAKEN. The code has not
    changed since 2026-05-24; only the reading differs.
- **CLM-009.13 (REQ013, PARTIALLY_IMPLEMENTED).**
  - Alternative: IMPLEMENTED_DIFFERENTLY. Interruption and cancellation are emitted by the same
    legacy adapter (`claude-agent-sdk-manager.ts`), not by the mapper, so the information exists
    at a different layer.
- **CLM-009.6 (REQ006, ALIGNED).**
  - Alternative: PARTIALLY_IMPLEMENTED. The mapper emits no `session.*` or `turn.cancelled`
    events, and it maps SDK init to `adapter.initialized`, not the `sdk.system.init` named in
    Steps. The ledger relies on the "where corresponding source inputs are present" qualifier.
- **CLM-004.6 / CLM-011.7 (STALE_SPECIFICATION, R4-Q2).**
  - Alternative: DOCUMENTED_UNIMPLEMENTED on the live path. The Codex production default has not
    been run through the conformance suite. The ledger treats the SDK-named condition as stale
    and routes the Codex conformance gap to the framed question R4-Q2.
- **CLM-008 (IMPLEMENTED_DIFFERENTLY, R4-Q1).**
  - Alternative: STALE_SPECIFICATION with HumanDecisionNeeded NO. The PRD/CONTRACT/SPEC
    preamble already makes the Claude path compatibility history, so the scope text only needs
    repair.
  - The ledger keeps R4-Q1 for two reasons. No ruling names DEL-04-03. The live translation is
    Runtime-owned code, so whether DEL-04-03 is retired or re-scoped is an owner matter.
- **CLM-022 / CLM-024 (STALE_SPECIFICATION).**
  - These are mixed guidance units, and most of their items still hold at module level.
  - Alternative: PARTIALLY_IMPLEMENTED.
- **CLM-002 (ALIGNED).**
  - Alternative: STALE_SPECIFICATION, because `_REFERENCES.md` now records REF-006 as MATCH.
  - The ledger keeps ALIGNED because the PRD hash mismatch still holds at the frozen basis.

## 3. Register-defect summary

- **REGISTER-1 (STALE_SPECIFICATION).** `_REFERENCES.md` records MATCH for REF-002 CONTRACT,
  REF-003 SPEC and REF-006 PRD. None of the three reproduces at `00115c719`
  (`REFERENCE_HASHES.csv` Match=NO). CLM-002 and CLM-027 cite it.
- **REGISTER-2 (REMAINING_STATE_MISMATCH).** `_DEPENDENCIES.md` still says "Declared Upstream/Downstream: TBD - no accepted dependency edges extracted", although the same file and `Dependencies.csv` list 11 ACTIVE rows.
- **REGISTER-3 (STALE_SPECIFICATION).** `_CONTEXT.md` still names Claude Agent SDK/Anthropic as
  the current path and uses daemon wording.
  - `D-APP-127_APPLICATION_MAP.csv` shows none of this deliverable's five carriers revised for
    D-APP-127/D-GOV-43.
- **Other carrier lag.** `Dependencies.csv` DEP-04-03-007 closed SATISFIED on 2026-07-18 (live
  probe). The SoW still states that the probe is TBD, in CLM-003.6, CLM-004.7, CLM-009.14,
  CLM-011.5, CLM-016 and CLM-023.

## 4. Direction and cause

- **CODEX_SOLE_ENGINE (15).**
  - Direction: `GOV:D-GOV-43`. Rows cite the App SPEC §11 / TYPES §7.4 revision, which
    supersedes the fixed eight-name UIEvent set, or the PRD/CONTRACT/SPEC "Current Codex-only
    MVP release basis" preamble.
  - Direction: `GOV:D-APP-127`, which retires the closed event vocabulary.
  - MR-11 applies because the SPEC §11 / TYPES §7.4 revisions name the superseded set
    explicitly.
  - DIRECTIVE §0's order resolves the Claude-SDK restatements through the preamble, so no
    AUTHORITY_CONFLICT was needed.
  - Secondary causes: `CAUSE2:A2_TOPOLOGY` on the SSE/browser rows and `CAUSE2:RUNTIME_EXTRACTION`
    on CLM-004.4 and CLM-008 (live translation moved to the Runtime core).
- **PRE_V3_DRIFT (20).** These divergences date from before 2026-08-22.
  - Tool-name exposure and the silent empty mapping for unknown SDK inputs: blame 2026-05-24
    (`d1e3d6b68`).
  - Determinism test gap: INSP-03, 2026-06-20.
  - Stale TBD status cells.
  - Carrier lag after the 2026-07-18 probe closure; these rows add `CAUSE2:CARRIER_PROPAGATION`.
  - CLM-011.8 adds `CAUSE2:RUNTIME_EXTRACTION`; CLM-022 adds `CAUSE2:PRE_V3_DRIFT` under a
    CODEX primary.
- **DOC_HYGIENE (3):** REGISTER-1, REGISTER-2 and CLM-027.
- **No CONTEXT (`CTX:`) record was needed.** Every explained divergence is covered by a
  GOVERNING ruling.
- **Searches behind each `NONE_FOUND`.**
  - The App `_DECISIONS/_REGISTER.md` was grepped for `DEL-04-03`, `mapper`, `SdkMessageMapper`
    and `sdk-message`. No row matched.
  - D-APP-06 names DEL-04-03 only in an SCC dependency package. D-APP-56 names it in the
    R4-P34 lane.
  - CONTEXT sources grepped for `mapper` and `DEL-04-03`, with no hits: the v3 final plan HTML,
    `chirality_app_v3_g0_record`, the `chirality_app_v3_*` steers, and the Codex host
    re-platform direction steer.
  - `DECISION_HITS.csv` was used as the starting list.
- **PostReleaseBasis** is NO on every row. None of the cited files appears in
  `TOUCHED_PATHS.csv`.
- **Note on D-APP-52.** The register describes D-APP-52 as the pec-transport ruling, with the
  "live-LLM demonstration deferred". `Dependencies.csv` credits the 2026-07-18 live `query()`
  probe closure to D-APP-52, so the ledger cites D-APP-52 only as context.

## 5. Method friction

- **Mixed guidance units.** Principles, Considerations and Trade-offs have no REQ numbering, so
  §2.2 does not allow a split. Each holds items that are aligned, stale and pre-v3 at once, so
  one Disposition loses information.
  - Proposal: allow a split for numbered principle lists, or add a "mixed" note token.
- **Module-level versus live-path readings.** Both readings are allowed, and the choice alone
  can flip ALIGNED to STALE. A standard `READING:MODULE` / `READING:LIVE` Notes token would let
  the verifier grade the same way.
- **Script evidence.** `validate-harness-section9.mjs` is not a product entry. The validator
  still requires a REACH tag on it, so it is tagged `LEGACY_ONLY` under Addendum 1 (UNREACHED).
  A `REACH=SCRIPT` value, or an exemption for it, would read more accurately.

## 6. Effort

- **Read in full:** the deliverable files (SoW, _STATUS, _CONTEXT, MEMORY, _REFERENCES,
  Dependencies.csv, _DEPENDENCIES, Assessment, one run record) and the rulebook.
- **Read as targeted ranges:**
  - code: `sdk-message-mapper.ts`, `delegated-engine-adapter.ts`, the runtime contract types and
    event schema, `claude-agent-sdk-manager.ts` (grep only) and `event-factory.ts`;
  - tests: the mapper test and the engine-conformance and native-event-adapter test headers;
  - App SPEC/TYPES/PRD/CONTRACT sections;
  - the D-APP-127, D-APP-52 and D-APP-56 records.
- **Git:** blame on three mapper ranges and one manager range, and `git show 603384787^` of the
  four legacy documents for the AC-001/VER-001 parity check.
- **Total:** about 30 file reads or greps. The context budget was adequate, not tight.
