# DEL-09-02 notes (worker A, pass 1)

Ledger: `DEL-09-02_claims.csv`, 53 rows. Sealed SHA-256
`3fa55fc71056ae01311b84316dc61015a065f6c4efec17251441c2ed8ba65cc7`. Validator: `RESULT PASS errors=0 warnings=0`.
No errata file exists yet.

## 1. Census

Indexed units: 29 (CLM-001..CLM-028 and REM-1), all covered. Run-local rows: REGISTER-1..4 and STATE-1..2.

| Disposition | Rows |
|---|---:|
| STALE_SPECIFICATION | 23 |
| ALIGNED | 9 |
| NOT_AUDITABLE | 5 |
| DOCUMENTED_UNIMPLEMENTED | 4 |
| IMPLEMENTED_DIFFERENTLY | 4 |
| PARTIALLY_IMPLEMENTED | 4 |
| AUTHORITY_CONFLICT | 2 |
| REMAINING_STATE_MISMATCH | 2 |

| ClaimType | Rows |
|---|---:|
| REQUIREMENT | 24 |
| STATE_ASSERTION | 12 |
| CONTEXT_CLAIM | 8 |
| REGISTER_DEFECT | 4 |
| ACCEPTANCE | 3 |
| EXCLUSION | 1 |
| REMAINING_WORK | 1 |

- **SEE rows, counted separately:** 10 (CLM-001, 006, 011, 013, 017 → REGISTER-1; CLM-008, 015, 021 → CLM-001;
  CLM-025 → CLM-024; CLM-028 → CLM-007). Without them there are 43 primary rows: 13 STALE_SPECIFICATION and 8 ALIGNED, with the other dispositions unchanged.
- **Split rate:** 3 of 29 units were split (10%), giving 21 rows. CLM-010 has 16 rows (DEL-09-02-RQ-001..016,
  separately numbered). CLM-012 has 3 rows (verification-table row groups). CLM-020 has 2 rows (the Records list and VER-001).
  CLM-014 has one row, which names AC-001.
- **HumanDecisionNeeded:** R4-Q1 on 14 rows (10 R4-Q1 only, 3 with R4-Q5, 1 with R4-Q2). No plain R4.
- **Confidence:** 29 HIGH, 23 MEDIUM, 1 LOW.

## 2. Least-confident rows (with the alternative reading)

- **CLM-010.10 (RQ-010 compaction), LOW.** I read it as DOCUMENTED_UNIMPLEMENTED on the live path because a grep
  of Runtime `core`/`daemon` found no compaction mirror. The alternative: the Runtime may persist Codex compaction
  notifications as received (R4-Q5), which would make the row IMPLEMENTED_DIFFERENTLY.
- **CLM-010.9 (RQ-009 tool-result budget), MEDIUM.** The same alternative applies (IMPLEMENTED_DIFFERENTLY if Codex's own
  output handling counts as the live mechanism).
- **CLM-010.2 (RQ-002 engine contract), MEDIUM.** The alternative is PARTIALLY_IMPLEMENTED: the Runtime
  `contracts/src/harness/engine-conformance.ts` suite definition is LIVE, but no Section 9 ID runs it against Codex (R4-Q2).
- **CLM-010.4 and CLM-010.11 (replay, subagents).** The LIVE Runtime code meets part of the underlying behaviour
  (session-store malformed-line tolerance; descendant-tracker), but no Section 9 check validates it. I cited R4-Q1
  because the only code meeting the *validation* claim is legacy. The alternative reading, that live behaviour code
  counts as "met by LIVE code", would drop R4-Q1 on these two rows.
- **CLM-010.6 and CLM-010.8 (AUTHORITY_CONFLICT).** K-PERM-1..4, K-HOOK-1 and K-PATH-2/3 are unamended for D-GOV-43.
  The alternative is IMPLEMENTED_DIFFERENTLY with GOV:D-GOV-43, if the owner treats D-GOV-43 items 4/10 as amending those clauses.
- **CLM-014 (AC-001), ALIGNED, MEDIUM.** The capability is present on live scripts, but no Section 9 runner output is
  recorded at `00115c719`, and every passing ID attests legacy fixtures. The alternative is PARTIALLY_IMPLEMENTED on proof grounds.
- **CLM-004, MEDIUM.** The alternative is REMAINING_STATE_MISMATCH, because the P40 note already calls the warning dated history.

## 3. Register-defect summary

- **REGISTER-1:** `_REFERENCES.md` records CONTRACT, SPEC and PRD as MATCH, and none of them reproduces at `00115c719`
  (HASH-RECOMPUTE). DIRECTIVE, TYPES and PLAN, recomputed by this worker, still match. Seven SoW and header rows
  restate MATCH as current and point here with SEE.
- **REGISTER-2:** the `_STATUS.md` `Last Updated` date (2026-09-03) lags its 2026-09-05 History entry.
- **REGISTER-3:** in `_DEPENDENCIES.md`, the `[WARNING] TBD_SURFACES` note still says the registry, runner, command and
  schema paths are TBD, and the Declared sections say no edges have been extracted. All of these surfaces now exist.
- **REGISTER-4:** in `Dependencies.csv`, all 25 rows are SatisfactionStatus TBD. The rows date from the 2026-05-20 extraction, their SDK-era
  framing is unchanged, and the D-APP-127 map marks the file Revised=NO.
- **Other stale state:** the Conflict table (CLM-027: CONFLICT-002 still shows the ruling as TBD, although the SoW's own P45 note records
  the ruling) and the `_CONTEXT.md` engine statement (STATE-1).

## 4. Direction and cause

- **Main CauseTags.** DOC_HYGIENE (15: hash, register and conflict-table text), CODEX_SOLE_ENGINE (11: Section 9 behavioural
  checks validate only the retained in-process Claude-SDK harness), and PRE_V3_DRIFT (10: registry, manifest and ID-name
  changes that landed 2026-06-13 to 2026-07-10 but never reached the SoW text; each carries `CAUSE2:CARRIER_PROPAGATION`).
  One row each takes RUNTIME_EXTRACTION, NATIVE_DELEGATION and LIFECYCLE_GATE_PENDING.
- **Secondary causes.** CARRIER_PROPAGATION (SoW re-pinned 2026-09-03 without the manifest or ID rename), CODEX_SOLE_ENGINE
  (CLM-010.4, CLM-023), NATIVE_DELEGATION (REM-1).
- **Records used.**
  - GOV: D-GOV-43 (PRD.md:13-17 and FR-027; CONTRACT.md:78, K-EVENT-1 amended), D-APP-38, D-APP-56 (P23 option A;
    UPD-143/144), D-APP-114, and SCA-APP-001 (ID rename in commit 29ebbea2f).
  - CTX: `APP_V3_PATHWAY_SEATING_2026-09-03` for REM-1, and the V3 done-declaration candidate, used as context
    only. Q-06 (sole engine), Q-07 (containment) and Q-11 (managed multi-child delegation) are mentioned in Notes.
- **NONE_FOUND searches.** I grepped `_DECISIONS/_REGISTER.md` for DEL-09-02, "Section 9", section9 and domain-profile.
  Only D-APP-114 (row 129) names DEL-09-02. I also checked the DECISION_HITS rows for DEL-09-02 and the done-declaration
  candidate. No record explains why the SoW kept its TBD, path and ID-name text after the manifest landed.
- **Git.** `git log -S adapter_message_mapper` dates the ID rename to 29ebbea2f (2026-06-13). The manifest landed in
  da5a8f803 (2026-07-10).

## 5. Method friction

- **R4-Q1 on validation claims.** A "Validation for X MUST confirm P" requirement has two code layers: the validator,
  which is a LIVE script, and the validated module, which is LEGACY_ONLY. Rule 3 does not say which layer "meets the
  claim". I applied it to the validated behaviour. Proposal: for TEST_SUITE deliverables, add one sentence that R4-Q1
  follows the reach of the module under test, not the runner.
- **Script reach.** REACHABILITY.csv omits `frontend/scripts/**`. I stated script reach in Notes from `package.json:20,21,29`
  and the in-root workflow.
- **CLM-020 and VER-001.** The unit combines a Records list with VER-001. I split it so that VER-001 has its own row. The splitting rule
  allows this only loosely, because the unit lists just one sub-item.

## 6. Effort

I read about 30 files or ranges: the deliverable folder in full (except the bodies of `_SEMANTIC*` and the run records,
which I only sampled), the Section 9, premerge and release-quality scripts, the manifest, `package.json`, the in-root
workflow, PRD §12.3–12.4 and §0–1 excerpts, SPEC §19.3, CONTRACT K-rows, the D-APP-56 ruling excerpt, register rows, and
Runtime `session-store.ts` excerpts and greps. The context budget was moderate, not tight.

## Coverage gaps

- The SoW `OUT-001` bullet (ScopeOfWork.md:16) and the Output and Evaluation Matrix (lines 396-400) are not indexed
  units. Their content is covered in substance by CLM-003, CLM-014 and CLM-020.2.
- There are no Section 9 IDs for the live Codex/Runtime path. The IDs that DEL-09-02-V3-01 (REM-1) would add cover only
  descendants, role attribution, closed schema and cancellation. Engine conformance, permission/containment, tool
  budgets and compaction on the Codex path have no owning Remaining item in this deliverable, and it is unclear whether
  this deliverable or R4-Q1/R4-Q2 should own them.
- `MEMORY.md`, `_run_records/**` and the package-level `Evidence_ADQ-14` (13 Section 9 IDs, 2026-06-21) are dated
  evidence and were not given rows. ADQ-14's 13-ID count is overtaken by the 16-ID manifest (reflected in the AssessmentEvidence cells).
