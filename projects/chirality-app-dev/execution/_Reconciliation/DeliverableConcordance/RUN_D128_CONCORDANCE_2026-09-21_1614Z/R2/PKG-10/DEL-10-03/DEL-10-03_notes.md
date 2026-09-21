# DEL-10-03 — forward-pass notes (R2, PKG-10)

Deliverable: DEL-10-03 OperationProposal Record and Human Gate Workflow. Basis: frozen tree at
`00115c719`. Ledger: `DEL-10-03_claims.csv` (55 rows, validator PASS 0/0). Addenda 4 and 5
(R4-Q4; STALE_SPECIFICATION/REMAINING_STATE_MISMATCH tie-break) were applied before sealing.

## 1. Census

**Rows:** 55 in total.
- 49 rows come from the 31 indexed units (30 CLM and 1 REM).
- 6 rows are run-local: REGISTER-1..5 and STATE-1.

**Split rate:** 8 of the 31 units are split (26%).

| Unit | Rows | Why it is split |
|---|---|---|
| CLM-010 | 10 | REQ-10-03-001..010 |
| CLM-003 | 3 | Table: general, protected-path and professional-boundary rows |
| CLM-026 | 3 | Guidance rows / boundary row / TBD paragraph |
| CLM-012, CLM-019, CLM-020, CLM-025, CLM-029 | 2 each | Separates the professional-boundary item |

- The index lists two SubItems, AC-001 (CLM-015) and VER-001 (CLM-022). Each unit has k = 1, and
  each item is named in Notes.

**By Disposition (sealed):**

| Disposition | All rows | of which SEE rows |
|---|---:|---:|
| ALIGNED | 23 | 3 (CLM-014, CLM-022, CLM-030 → CLM-007) |
| STALE_SPECIFICATION | 15 | 4 (CLM-011 → CLM-004; CLM-026.3, CLM-028 → CLM-010.10; CLM-027 → CLM-005) |
| PARTIALLY_IMPLEMENTED | 10 | 8 (CLM-010.8 → CLM-003.2; CLM-010.9, CLM-012.2, CLM-019.2, CLM-020.2, CLM-025.2, CLM-026.2, CLM-029.2 → CLM-003.3) |
| NOT_AUDITABLE | 5 | 0 |
| AUTHORITY_CONFLICT | 1 | 0 |
| REMAINING_STATE_MISMATCH | 1 | 0 |

**SEE rows:** 15 are counted separately under MR-4. Leaving them out gives 40 distinct
dispositions: ALIGNED 20, STALE 11, PARTIAL 2, NOT_AUDITABLE 5, AUTHORITY_CONFLICT 1, RSM 1.

**By ClaimType:**

| ClaimType | Rows | Dispositions |
|---|---:|---|
| REQUIREMENT | 21 | 12 ALIGNED / 7 PARTIAL / 2 STALE |
| STATE_ASSERTION | 15 | 8 ALIGNED / 7 STALE |
| CONTEXT_CLAIM | 6 | 5 NOT_AUDITABLE / 1 STALE |
| ACCEPTANCE | 6 | 3 ALIGNED / 3 PARTIAL |
| REGISTER_DEFECT | 5 | 4 STALE / 1 RSM |
| EXCLUSION | 1 | 1 STALE |
| REMAINING_WORK | 1 | 1 AUTHORITY_CONFLICT |

No errata file exists (forward pass only).

**Measure used on every REQ/ACCEPTANCE row.** Each row is judged on two axes. The row takes the
weaker result of the two.

1. The deliverable's own documentary artifact (record shape, workflow, checklist) against the
   GOVERNING text.
2. For present-tense GOVERNING behaviour: whether the outcome the invariant forbids can be
   reached on the live Codex path.

| Rows | Result | Why |
|---|---|---|
| REQ-003/004/005 | ALIGNED | No apply or lifecycle-transition path exists on any path. |
| REQ-008 / CLM-003.2 | PARTIAL | Codex turns can write profile protected paths, and no Chirality quarantine exists. |
| REQ-009 / CLM-003.3 | PARTIAL | Documentary: "ready-for-construction status" is omitted. |

- Contract types in `projects/chirality-runtime/packages/contracts/src/harness/operation-proposal.ts`
  are tagged `REACH=LIVE` (module map) and noted as inert: no runtime consumer.
- The legacy tool modules (`frontend/src/lib/harness/mcp/**`) are `REACH=LEGACY_ONLY`. Claims about
  them (CLM-015, CLM-007) are judged at module level and carry `R4-Q1`.

## 2. Least-confident rows

- **CLM-011** (LOW, STALE_SPECIFICATION, SEE:CLM-004).
  - Reading taken: the claim "TYPES §11.2 conforms to framework canon" is false for `status`.
    - The pinned persona `agents/AGENT_DOMAIN_ENGINE.md@77a327727` (lines 406-407) says
      `proposal_only` holds "until validated ... and human-accepted", and that `proposal_only`
      "covers draft and ready_for_review".
    - TYPES:641 and the code make it a constant.
  - Alternative reading: the canon phrase describes non-binding character, not a field
    transition. Then TYPES conforms and the row is NOT_AUDITABLE.
- **Medium-confidence judgement calls:**
  - **CLM-015** (ALIGNED at module level vs AUTHORITY_CONFLICT). Alternative: treat ownership of a
    LEGACY_ONLY surface that PRD §8.17 still calls "live" as a conflict. The conflict sits in
    governing docs, not in DEL-10-03's text, so I kept ALIGNED + R4-Q1.
  - **REM-1** (AUTHORITY_CONFLICT). Alternative: ALIGNED as an accurately open item. It is
    contested because its only host is the legacy in-process MCP server under D-GOV-43.
  - **CLM-010.8 / CLM-003.2** (PARTIAL). Alternative: ALIGNED as documentary-only, with
    enforcement owned by DEL-10-02 and hooks kept future by PRD §8.17. I rejected this because
    K-DOMAIN-2 is present tense and the forbidden outcome can be reached on the live path.
  - **CLM-009** (STALE vs ALIGNED). The exclusions hold. The "outside this four-document contract"
    sentence contradicts the D-APP-56 ownership ruling.

## 3. Register-defect summary

- **REGISTER-1:** the `_REFERENCES.md` CONTRACT/SPEC/PRD MATCH hashes do not reproduce
  (HASH-RECOMPUTE; pack rows Match=NO).
  - They were set in `23b3879b3` on 2026-09-12, and the documents changed again later that day.
  - DIRECTIVE, TYPES, PLAN and REF-007..012 do reproduce.
- **REGISTER-2:** REF-008 identity drift.
  - `_REFERENCES.md` REF-008 points to `workflows/domain-engine/WORKFLOW.md` (changed by
    `9b005c23a`, 2026-09-09).
  - SoW and MEMORY cite REF-008 as `agents/AGENT_DOMAIN_ENGINE.md@77a327727`, which is absent from
    the frozen tree's `agents/`. The field table now lives in REF-011 `resources/contract.md`.
  - HumanDecisionNeeded is R4-Q4 (four-role adoption as amendment).
- **REGISTER-3:** `_STATUS.md` `Last Updated: 2026-07-12` lags its 2026-07-18 history lines.
  REMAINING_STATE_MISMATCH under tie-break rule 2b.
- **REGISTER-4:** `_DEPENDENCIES.md` still says "TBD - no accepted dependency edges have been
  extracted yet", against its own 8-row register. STALE under tie-break rule 1, with
  ALSO:REMAINING_STATE_MISMATCH.
- **REGISTER-5:** `Dependencies.csv` DEP-10-03-008 cites
  `frontend/packages/harness-contract/src/operation-proposal.ts:77, 22-23`.
  - That file is now a 2-line deprecated facade; the content is in runtime-contracts.
  - The CONTRACT line 140 and TYPES line 565 anchors have moved to 151 and 653.
  - DEP-005/-007 call the legacy tools "live".
- **STATE-1:** the `_CONTEXT.md` SCA-APP-001 paragraph still names Claude Agent SDK as the current
  path (D-APP-127 application map: `_CONTEXT.md` Revised=NO).
- **Also stale in the SoW text itself:**
  - CLM-005, CLM-013, CLM-027: hook fields "await tier-0 CHANGE". They were bound on 2026-07-02
    (`d70d8df92`), and the line anchors 81/88/101/115 are now 83/90/103/117.
  - CLM-010.10, CLM-018, CLM-026.3, CLM-028: profile instance, adapter and schema refs still
    listed as TBD.

## 4. Direction and cause

**Main CauseTags:**

| CauseTag | Rows | Where |
|---|---:|---|
| PRE_V3_DRIFT | 22 | Most stale text dates from July 2026 (D-APP-53/56 reconciliations left older sentences in place). The ready-for-construction omission dates from the 2026-06-21 canon tranche. |
| CODEX_SOLE_ENGINE | 2 | REM-1, STATE-1 |
| DOC_HYGIENE | 1 | REGISTER-1 |
| CARRIER_PROPAGATION | 1 | REGISTER-2 |
| FACADE_DEPRECATION | 1 | REGISTER-5 |

**CAUSE2 secondaries:**
- CARRIER_PROPAGATION on the SoW stale rows and on REGISTER-1 and STATE-1.
- CODEX_SOLE_ENGINE on CLM-003.2, CLM-010.8 and REGISTER-5.
- DOC_HYGIENE on REGISTER-2..4.

**GOV records used:**
- D-APP-53 (dependency reconciliation), D-APP-56 (R5 P45 UPD-150 and R4-P27 ownership), D-APP-65
  (precursors-not-amendment).
- D-APP-89 (facade), D-GOV-41/42 (four-role and workflow adoption), D-GOV-43 / D-APP-127 (Codex host).
- D-APP-52 is cited for the staged-surface framing.

**NONE_FOUND searches:**
- **Rows:** CLM-003.3 and its SEE rows, CLM-011, REGISTER-1, REGISTER-3.
- **Registers and rulings grepped:** `_DECISIONS/_REGISTER.md` rows D-APP-39/45/49-53/56/65/70/76/89/127
  and the ruling records they point to (D-APP-70 §9, D-APP-127 body).
- **Decomposition v3.2:** SOW-069 and DEC-006.
- **Reliance register:** `docs/harness/reliance_boundary_register.md` (domain rows RB-HOOKS,
  `section9.domain_profile_validation`).
- **GOVERNING K-rows:** CONTRACT §1.10 K-DOMAIN-1..4 and K-AUTH-2.
- **Other governing text:** TYPES §11, PRD §8.17, SPEC §18 and PLAN R7.
- **REM-1 gate status:** searched the App execution tree for "transport soundness". It appears only
  in closed concordance runs, so MechanicallyUnblocked is UNKNOWN.

**Cross-deliverable observations (governing docs, not audited):**
- PRD §8.17, SPEC §18, PLAN R7 and the runtime `tool-catalog.ts:133-142` call the pec
  propose/refresh/validate tools "live". At the frozen basis they are hosted only by the legacy
  in-process MCP server, so this is R4-Q1.
- TYPES §11 forward note still cites `frontend/packages/harness-contract/src/*` (now facades).
- TYPES §11 header claims canon conformance that fails on `status` constancy.

## 5. Method friction

- **MR-4 with composite units.** The boundary list that omits "ready-for-construction" recurs
  inside seven composite tables and lists. Applying SEE literally forced splits of CLM-012/019/020/
  025/026/029, which inflates PARTIAL counts (8 SEE rows) for one documentary defect.
  - Proposal: allow a single `REPEATS:<key>` note on an otherwise-dispositioned composite row,
    without splitting.
- **REACH for inert contract types.** A `LIVE` module map tag on types with no runtime consumer
  overstates what is exercised.
  - Proposal: add `INERT` as a Notes qualifier convention.
- **Canon vs App authority.** RUN_BASIS §5 does not place the framework persona (tier-0 D-T0-01
  canon) in the map, whereas DIRECTIVE §0 ranks `agents/AGENT_*` at 7. I applied DIRECTIVE §0.
  - Proposal: state this explicitly for PKG-10.
- **Assessment mapping (MR-9).** The old INSP-03 PARTIAL findings about the absence of concrete
  instances or a store collide with the "ALIGNED + STILL CURRENT" consistency check on the
  shape-level REQ rows. I mapped them to the TBD-carrying row (CLM-010.10) and gave shape rows
  "no direct conclusion" (REQ-006) or OVERTAKEN (REQ-003, per the D-APP-56 P43 annotation).

## 6. Effort

- **Deliverable files read:** SoW, `_STATUS`, `_CONTEXT`, `MEMORY`, `_DEPENDENCIES`,
  `Dependencies.csv`, `_REFERENCES`, the INSP-03 assessment, and the `_run_records` listing.
  `_SEMANTIC*.md` and the Evidence files were only skimmed through DECISION_HITS; their bodies were
  not read.
- **Code and governing text read (about 12 files):** runtime `operation-proposal.ts` and
  `domain-profile.ts` (partial), `domain-proposal-tools.ts` (partial), `read-tools.ts` (registration
  lines), `domain-profile-registry.ts` (grep), `tool-catalog.ts` (lines), two test files (case
  names), `open_pipe_stress.yaml` / `pec.yaml` (grep), and TYPES/CONTRACT/PRD/SPEC/PLAN/DIRECTIVE
  slices.
- **Git:** `log`, `show` and `blame -L` on the frozen tree for dating. The legacy four documents
  were extracted from `da17cb495^` for the VER-001/AC-001 parity check (scratch only).
- **Context budget:** moderate, not tight.
