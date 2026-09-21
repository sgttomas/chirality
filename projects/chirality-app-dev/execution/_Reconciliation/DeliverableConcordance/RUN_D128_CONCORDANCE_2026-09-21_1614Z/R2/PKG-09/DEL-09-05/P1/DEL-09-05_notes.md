# DEL-09-05 — part P1 notes (forward pass)

Scope: SEC-1, CLM-001..CLM-016 and CLM-034 (the SoW "Current Codex MVP conformity", Ontology and Epistemology
sections), plus the run-local row STATE-1. Frozen basis `00115c719`. Rule notice RULE_NOTICE_ADDENDUM9 (R4-Q6)
arrived **before sealing**. No row turns on R4-Q6, which covers K-PERM, the API-key UI and `~/.codex`, so no row cites it.

## 1. Census

- Rows: 38 (18 indexed units; CLM-010 split into 15 rows, CLM-016 into 6 rows for REQ-001..004, AC-001, AC-002; 1 run-local row).
- Split rate: 2 of 18 units split (11%). CLM-010 was split as a table of independently dispositionable rows. CLM-016 was split per its SubItems.
- By ClaimType: REQUIREMENT 25, STATE_ASSERTION 7, CONTEXT_CLAIM 3, ACCEPTANCE 2, EXCLUSION 1.
- By Disposition: STALE_SPECIFICATION 14, ALIGNED 11, PARTIALLY_IMPLEMENTED 7, DOCUMENTED_UNIMPLEMENTED 3,
  NOT_AUDITABLE 2, AUTHORITY_CONFLICT 1.
- SEE rows, counted separately: 2. CLM-008 is a SEE row to CLM-001 (STALE_SPECIFICATION). CLM-015 is a SEE row to CLM-007 (ALIGNED).
  Excluding them: STALE_SPECIFICATION 13, ALIGNED 10.
- HumanDecisionNeeded: 2 rows cite `R4`: CLM-016.3 (AUTHORITY_CONFLICT on G6a) and CLM-016.6. No row cites R4-Q1: no
  claim here is met only by LEGACY_ONLY code, and the SDK items are contradicted by live packaging code.
- No errata file (pass 1).

## 2. Least-confident rows

- **CLM-010.7 (REQ-09-05-007), LOW.** Sealed as STALE_SPECIFICATION. The App CONTRACT preamble (line 17, from
  23b3879b3) reads K-RELEASE-1 with D-GOV-43 item 1, which covers bundle signing and notarization. SPEC 19.4 and
  PRD 12.8 name the signed and notarized consolidated candidate.
  *Alternative:* the K-RELEASE-1 row text (CONTRACT.md:138) is unamended, and D-APP-97 says F-APP-2 still fences
  signing. If the preamble reading is not an amendment, the row is AUTHORITY_CONFLICT / R4. Done-declaration Q-02
  asks exactly this.
- **STATE-1 (OUT-001), LOW.** Same question, same alternative.
- **CLM-016.3, MEDIUM.** Sealed as AUTHORITY_CONFLICT. The alternative reading is ACCEPTED_DIVERGENCE, if the owner
  treats D-GOV-43 as having retired G6a for DEL-09-05. Only the `_STATUS.md` carrier says so; D-APP-127 names
  DEL-09-05 as "revised" without naming G6a, and the Root D-GOV-43 record was not read (out of the evidence roots).
- **CLM-010.13 / CLM-016.5, MEDIUM.** Sealed as DOCUMENTED_UNIMPLEMENTED. The alternative is that the obligation
  has not yet been triggered, because the deliverable claims no readiness. I chose the sealed reading because a
  release was prepared (version 3.0.0, then 3.0.1).

## 3. Register-defect summary

None in P1. The `_REFERENCES.md` hash drift has one REGISTER row, which P2 owns. SoW rows that restate MATCH
(CLM-001, CLM-006, CLM-008, CLM-014) cite `HASH-RECOMPUTE@00115c719` and do not carry a SEE token, because the
target row is in the other part's ledger. The manager may add `SEE:` links when merging.

Related finding for P2: SoW REF-007 names `agents/AGENT_SOFTWARE_DECOMP.md`. That file was removed by d1166698d on
2026-09-09, while `_REFERENCES.md` now names `workflows/software-decomp/WORKFLOW.md`.

## 4. Direction and cause

- **CARRIER_PROPAGATION (7).** The SoW was not revised when D-APP-127 was applied. The carrier map lists SoW as NO;
  only `_STATUS.md` was revised. SEC-1 and the Codex wording in CLM-004/REQ-006/REQ-010 were written 2026-09-10
  (2f825f180), before D-GOV-43.
- **DOC_HYGIENE (6):** hash, reference and TBD-path statements.
- **CODEX_SOLE_ENGINE (5):** the secret scanner and network proof are still Anthropic-specific
  (`scan-secret-evidence.mjs:50`, `run-network-policy-proof.mjs:20`), and the SDK packaged-turn checklist items
  conflict with the Codex-only package boundary.
- **A2_TOPOLOGY (4):** the D-GOV-43 short packaging procedure replaces the G6a/WP-11 release spine and the evidence
  matrix. This tag is the closest vocabulary fit. The mechanism is D-GOV-43 generally, not topology specifically.
- **PRE_V3_DRIFT (3):** the in-root workflow is unchanged since 7bee9ae41, and the INSP-03 gaps of 2026-06-21 are
  unchanged.
- **CAUSE2 secondaries:** A2_TOPOLOGY (SEC-1), CARRIER_PROPAGATION (CLM-004, CLM-005, CLM-010.10, CLM-013,
  CLM-016.3), CODEX_SOLE_ENGINE (CLM-010.6), OTHER:V3_ROLE_ADOPTION (CLM-006), PRE_V3_DRIFT (CLM-016.5).
- **CONTEXT records used:** `execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/`
  `BUILD_EVIDENCE_20260912.md` (Developer ID signing on 2026-09-12; notarization, S-6/S-8 and publishing not done by the agent),
  `PACKAGING_PROCEDURE.md` and `NATIVE_CHECKLIST.md`. `V3_DONE_DECLARATION_CANDIDATE` Q-01, Q-02, Q-04 and Q-13 are
  noted on rows only.
- **Searches behind NONE_FOUND:**
  - `_REGISTER.md`: G6a has 0 hits; F-APP-2 appears only in the D-APP-97 row; D-APP-38, D-APP-56 and D-APP-127
    rows were checked.
  - D-APP-127 record.
  - CONTEXT: BUILD_EVIDENCE and PACKAGING_PROCEDURE, which record no secret or network inspection and no
    ten-step CI review.

## 5. Method friction

- **Repo-root `.github/workflows/**` is out of root.** Most CI claims can be seen only through the in-root
  `contract-pins.manifest.ts` and `desktop-release-workflow.test.ts`. Those tests read the repo-root files, and
  the suite passes in the gate transcript. I cited them as TEST_ONLY evidence of workflow content and wrote
  `OUT_OF_ROOT:` in Notes. The artifact name `harness-validation-summaries` is not verifiable in root.
- **REACH for build scripts.** Manual npm verification scripts (`verify:version-identity`, `proof:secret-scan`,
  `proof:network-policy`) are tagged LIVE as package.json entries, with "manual; not chained from desktop:dist" in
  the text. A stricter reading would treat them as not live.
  - Proposal: add a `REACH=MANUAL_ENTRY` qualifier, or state the rule explicitly.
- **Cross-part SEE.** SEE targets must be in the same ledger, so SoW restatements of the P2-owned hash REGISTER
  row cannot carry `SEE:`. The merge step could add them.
- **CLM-010 has no SubItems but is a 15-row requirement table.** I split it under the "table of independently
  dispositionable rows" rule.

## 6. Effort

About 35 files or ranges read:
- SoW; `_STATUS`, `_REFERENCES`, `_CONTEXT`, INSP-03, Dependencies.csv summary;
- D-APP-127 in full, plus parts of D-APP-56, D-APP-97 and the register;
- CONTRACT, SPEC 19, PRD 12, PLAN 7, DIRECTIVE §0;
- package.json, the in-root workflow, 8 scripts and 8 test files (in part);
- BUILD_EVIDENCE, and parts of the NATIVE_CHECKLIST and PACKAGING_PROCEDURE.

The context budget was adequate but not tight.

## Coverage gaps

- **Purpose section (ScopeOfWork.md:18-23).** OUT-001 and OUT-002 fall outside every indexed unit. OUT-001 is
  recorded here as STATE-1 (stale release-target wording). OUT-002 cites decomposition line 368 at d6f6cadb2,
  which is correct at that commit (the row is now at line 382). No row was needed for it.
- **Retirement of V3-04 and the G6a/G6b/G-KEY/G7/G8 gates.** These appear only in `_STATUS.md`. P2 owns
  `_STATUS`/Remaining; the governing question is raised here on CLM-016.3.
