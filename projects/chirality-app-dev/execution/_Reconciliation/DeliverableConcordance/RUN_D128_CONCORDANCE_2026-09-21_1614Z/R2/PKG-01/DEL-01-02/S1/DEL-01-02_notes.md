# DEL-01-02 — S1 forward-pass notes (RUN_D128, R2, PKG-01)

Split S1: SoW "Deliverable Definition — Ontology" and "Completion and Reliance Basis — Epistemology"
(CLM-001..CLM-023), REM-1, and the non-SoW carriers (`_STATUS.md`, `_CONTEXT.md`, `_DEPENDENCIES.md`,
`Dependencies.csv`, `_REFERENCES.md`, `MEMORY.md`). Frozen basis `00115c719`. Run-local keys:
REGISTER-1..5 and STATE-1..2.

## 1. Census

Rows: 87 (24 indexed units, 5 REGISTER rows, 2 STATE rows).

| ClaimType | Rows | Dispositions |
|---|---:|---|
| REQUIREMENT | 52 | ALIGNED 13, PARTIALLY_IMPLEMENTED 16, IMPLEMENTED_DIFFERENTLY 10, STALE_SPECIFICATION 6, AUTHORITY_CONFLICT 4, DOCUMENTED_UNIMPLEMENTED 2, STALE_VERIFICATION 1 |
| STATE_ASSERTION | 18 | STALE_SPECIFICATION 9, ALIGNED 5, IMPLEMENTED_DIFFERENTLY 2, REMAINING_STATE_MISMATCH 1, AUTHORITY_CONFLICT 1 |
| CONTEXT_CLAIM | 9 | NOT_AUDITABLE 6, STALE_SPECIFICATION 3 |
| REGISTER_DEFECT | 5 | STALE_SPECIFICATION 3, REMAINING_STATE_MISMATCH 2 |
| EXCLUSION | 1 | PARTIALLY_IMPLEMENTED 1 |
| ACCEPTANCE | 1 | ALIGNED 1 |
| REMAINING_WORK | 1 | STALE_SPECIFICATION 1 |

Disposition totals: STALE_SPECIFICATION 22, ALIGNED 19, PARTIALLY_IMPLEMENTED 17,
IMPLEMENTED_DIFFERENTLY 12, NOT_AUDITABLE 6, AUTHORITY_CONFLICT 5, REMAINING_STATE_MISMATCH 3,
DOCUMENTED_UNIMPLEMENTED 2, STALE_VERIFICATION 1.

- **SEE rows (MR-4), counted separately:** 25 of the 87 rows carry `SEE:`. Homes: CLM-006.1/.3/.4/.7/.8/.9/.10/.11/.12,
  CLM-006.2 (canonical path), CLM-013, CLM-018.3, REGISTER-1. Without SEE rows: 62 independently dispositioned rows.
- **Split rate:** 7 of 24 units split (29%): CLM-006 (13 taxonomy rows), CLM-007 (10 condition rows), CLM-010
  (5 deferred fields), CLM-011 (3: 13 implemented-ID rows grouped as .1, plus the two "not implemented" rows),
  CLM-018 (RBR-001..025 as .1..25), CLM-022 (OI-RBR-001..005), CLM-023 (.1 paragraph, .2 AC-001, the only
  indexed sub-item). 63 rows come from splits.
- **HumanDecisionNeeded:** NO 60; R4-Q1 19; `R4-Q1; R4` 4; `R4-Q2; R4-Q5` 2; `R4-Q1; R4-Q2` 1; R4-Q5 1.
- No errata (forward pass only).

## 2. Least-confident rows

- **CLM-006.13 (RB-FALLBACK), LOW.** Sealed: PARTIALLY_IMPLEMENTED. Alternative reading: ALIGNED. K-ENGINE-5
  asks only that a governed fallback path "remain available". The retained Claude and Pi adapters and the register's
  criteria row could satisfy that as a documented option. Whether retained code counts is R4-Q1.
- **CLM-018.15 (RBR-015, MCP through the same policy), LOW.** Sealed: IMPLEMENTED_DIFFERENTLY. Alternative:
  PARTIALLY_IMPLEMENTED, if request and request-resolved logging of dynamic-tool calls counts as the same event policy.
  I did not trace whether dynamic-tool calls reach the Runtime event log.
- **AUTHORITY_CONFLICT rows (CLM-006.7, CLM-007.3, CLM-018.8, STATE-1; CLM-018.5 on R4-Q5).** Alternative: apply
  DIRECTIVE §0 literally. Unamended DIRECTIVE §2.8 and §5 would then control. The Claude key-aware default and
  settings isolation would be current obligations, and the live path would be DOCUMENTED_UNIMPLEMENTED (STATE-1:
  ALIGNED text, nonconforming code). I did not take this route. The lower texts rest on a ruling: D-GOV-43, and the
  Codex-only basis it presupposes. That ruling undercuts DIRECTIVE §2.8 and §5 without naming them, which is route (a)
  of CONVENTIONS §1.
- **CLM-006.8 / CLM-018.16 (subagents), MEDIUM.** Live reach of the `agent1-run-coordinator.ts` approval check
  comes from the pack's module chain (electron/main.ts). I did not trace the exact call site.
- **CLM-006.5 / CLM-006.9 / CLM-018.17 (human gate), ALIGNED at MEDIUM.** The actor is asserted by the caller in
  the transition route body, and the approval SHA is checked for format only. A stricter reading would give
  PARTIALLY_IMPLEMENTED. The live route does enforce what the SoW names (actor rule and SHA presence).

## 3. Register-defect summary

- **REGISTER-1:** `_REFERENCES.md` REF-002/003/006 (CONTRACT, SPEC, PRD) still read MATCH, but none of the three
  reproduces at `00115c719` (`HASH-RECOMPUTE@00115c719`). The rows were reconciled at corpus v23 (`23b3879b3`,
  2026-09-12). Later CONTRACT edits (`95b342519`, `7f1e9f387`) made them stale. DIRECTIVE, TYPES and PLAN do
  reproduce (own `shasum`). SoW CLM-004, 007.7, 010.4, 012, 019, 022.1, 022.5 and REGISTER-3 point here.
- **REGISTER-2:** REF-007 identity is inconsistent across the carriers:
  - SoW, `Dependencies.csv` and `_DEPENDENCIES.md` name `AGENT_SOFTWARE_DECOMP.md`, which is absent at the App
    and at Root `agents/`;
  - `MEMORY.md` says it was repointed to `agents/AGENT_SOFTWARE_DECOMP.md`, which is also absent;
  - `_REFERENCES.md` gives `workflows/software-decomp/WORKFLOW.md`, with REF-009/010 and no REF-008.
- **REGISTER-3:** `Dependencies.csv` REF rows restate "hash status MATCH" as current.
- **REGISTER-4:** `_STATUS.md` Last Updated (2026-07-22) lags its 2026-07-27 history entry.
- **REGISTER-5:** no carrier records the 2026-09-12 D-GOV-43 amendment to the primary artifact. This matches
  D-APP-127_APPLICATION_MAP, where every carrier is NO.
- **Observed but not rowed:**
  - `_DEPENDENCIES.md:28` contains a machine-absolute path in a 2026-05-20 run note (historical).
  - `_CONTEXT.md:52` names `Guidance.md`, `Specification.md`, `Procedure.md` and `Datasheet.md`, which were
    consolidated into `ScopeOfWork.md`. The sentence is past tense.

## 4. Direction and cause

- **Main CauseTags:**
  - CODEX_SOLE_ENGINE 27: live enforcement moved to Codex sandbox, approval policy and dynamic tools, and the
    SoW still names Claude-SDK and legacy-harness surfaces;
  - DOC_HYGIENE 16 (corpus drift, REF-007);
  - PRE_V3_DRIFT 6 (UPD-100/101 supersessions not carried into older rows);
  - CARRIER_PROPAGATION 5;
  - RUNTIME_EXTRACTION 2 (canonical session path);
  - NATIVE_DELEGATION 2, CREDENTIAL_CUSTODY 2, A2_TOPOLOGY 1, FACADE_DEPRECATION 1.
- **CAUSE2 secondaries:** A2_TOPOLOGY (CLM-006.2); CODEX_SOLE_ENGINE (CLM-006.8, 006.12, 010.2, 018.14, 018.24);
  CARRIER_PROPAGATION (CLM-007.1, 011.1, 016, REM-1, STATE-1); DOC_HYGIENE (CLM-020).
- **GOVERNING rulings used:**
  - D-GOV-43 and D-APP-127 (re-platform);
  - D-APP-56 (UPD-100/101; MR-11 on CLM-018.14);
  - D-APP-38 (corpus mechanism);
  - D-APP-77 (RB-PEC-ADAPTER; REM-1).
- **CONTEXT records used:**
  - `execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/tranche/APP_EXECUTION_RETURN.md`
    item 7. The register was flagged there as follow-up outside the 2026-09-12 write scope.
  - `…/tranche/APP_DOCS_RETURN.md`: the corpus v23 re-hash, and the addendum-only register revision.
- **Searches behind NONE_FOUND** (REGISTER-2, REGISTER-4, STATE-2):
  - `_DECISIONS/_REGISTER.md`, grepped for DEL-01-02, reliance, corpus/D-APP-38, Codex-only / sole engine,
    AGENT_SOFTWARE_DECOMP and harness-contract;
  - the replatform AgentRuns folder, grepped for reliance, corpus and in-process.
  - Root `plans/` CONTEXT sources are outside this worker's read roots and were not read.
- **Authority routes (governance-invariant rows that turn on authority):**
  - **AUTHORITY_CONFLICT:** CLM-006.7, CLM-007.3, CLM-018.8 and STATE-1. On one side, unamended DIRECTIVE §2.8
    and §5 (Claude key-aware default; ambient settings cannot alter shipped behaviour). On the other, the Codex-only
    basis applied under D-GOV-43: amended CONTRACT K-ENGINE-3, and a host run against the user's shared Codex
    configuration. D-GOV-43 and D-APP-127 do not name these App DIRECTIVE clauses. The shared-configuration
    question is wider than R4-Q1, hence `R4-Q1; R4`.
  - **AUTHORITY_CONFLICT on R4-Q5:** CLM-018.5. Amended K-EVENT-1 conflicts with unamended K-ENGINE-4, both in
    CONTRACT, so the §0 order cannot resolve it.
  - **MR-11:**
    - CLM-018.14: D-APP-56 UPD-101 explicitly superseded flat Bash default-deny;
    - REM-1: D-GOV-43 explicitly supersedes D-GOV-20 items 2-4 on the App path.
  - **No authority question:** the other invariant rows. Their clauses are unamended and do not conflict with a
    ruling as text. The legacy-versus-live obligation question is carried as R4-Q1 by evidence (subject test,
    rule 3).
- **R4-Q1 application:**
  - Cited on every row where the only code meeting the claim is LEGACY_ONLY: hooks, hard-deny precedence,
    instruction-root and symlink protection, the Bash posture, settingSources, the Section 9 evidence modules, and
    the core register surfaces.
  - `ALSO_MODULE:ALIGNED` is recorded on the product-behaviour rows.
  - Rows met partly by LIVE Runtime code (subagents, redaction, dynamic tools, transcripts) do not cite R4-Q1.

## 5. Method friction

- **Brief versus CONVENTIONS on authority.** "Do not assume the Codex-only preambles override a higher unamended
  source" and "apply §0 where it resolves" pull against the AUTHORITY_CONFLICT test (a) when the lower preamble rests
  on a ruling. I took route (a). Proposed revision: state that a lower amended text which applies a GOVERNING
  ruling counts as "the ruling" for route (a).
- **CONTEXT_CLAIM dispositions.** They permit only STALE_SPECIFICATION or NOT_AUDITABLE. Identity and trace tables
  that are checkable and true (CLM-002, CLM-005) therefore get NOT_AUDITABLE, which reads oddly. Proposed: allow
  ALIGNED on CONTEXT_CLAIM when a check was made.
- **Pregather accuracy.** Two pregather glosses were misleading, and I corrected both in the rows:
  - `session-store.ts:969-974` is the legacy migration copy, not the live writer (the live writer is `:654-668`);
  - `runtime-service.ts:592-598` `isContained` is agent-file listing, not write containment.
- **REACH tag for dev scripts.** `validate-harness-section9.mjs` and the manifest have no REACH row. I tagged them
  TEST_ONLY and noted that they run from an npm script.
- **Suite-level gate transcripts.** The transcripts carry no per-case lines. The cited case names were verified in
  the test sources, but individual case results cannot be verified beyond the suite PASS. Two rows name a test file
  without a case.

## 6. Effort

About 45 files or line ranges read:
- the deliverable carriers;
- App CONTRACT and DIRECTIVE excerpts;
- the D-APP-127 ruling;
- the D-GOV-43 packet README and IMPACT;
- the replatform tranche returns;
- about 15 Runtime and frontend source ranges;
- about 10 test files (case names only);
- the evidence pack and pregather.

The context budget was adequate but tight around the SoW plus register reads.

## Coverage gaps

- **Live-path boundaries with no DEL-01-02 row.** Codex approval policy and sandbox selection, Codex-native
  descendants, and Codex-home thread storage are live product boundaries. No SoW taxonomy row owns them. They
  appear only partially in the register's SCA-APP-003 addendum (RB-ROLE-MODEL), which is outside S1's SoW range
  and belongs to the extension item for the register document.
- **Register addendum rows outside the SoW.** The SCA-APP-003/004 rows (RB-DAEMON, RB-CONTROL-SOCKET,
  RB-COORDINATION-PROJECTION, …) and RB-LOCAL-PROVIDER have no SoW requirement anchoring them. Their ownership in the
  deliverable's scope text is unclear.
- **`section9.domain_profile_validation`.** It is implemented and registered (manifest `:115`), but the SoW
  validation index (CLM-011) has no row for it. It is named only in the CLM-013/023 prose.
