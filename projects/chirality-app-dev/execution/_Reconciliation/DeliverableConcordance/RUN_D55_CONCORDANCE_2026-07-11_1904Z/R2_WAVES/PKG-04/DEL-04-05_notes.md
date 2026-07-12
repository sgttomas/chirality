# R2 Wave-2 notes — DEL-04-05 Anthropic Provider Key, Base URL, and Network Bridge

Run: `RUN_D55_CONCORDANCE_2026-07-11_1904Z`. Source state: `main` = `fac46e33f`
(frontend/ byte-identical through HEAD `1625b396a`; `git diff fac46e33f HEAD -- frontend/`
empty). Verification bound via `GATE-TRANSCRIPT(W1@fac46e33f)` (typecheck exit 0;
Vitest 667 passed/4 skipped). INSP-03 reviewed `ce0ab70933` — the Specification was NOT
rewritten after INSP-03 (stable RQ-001..017 IDs), so no MR-9 old-ID remapping is needed;
line anchors shifted with unchanged behavior.

## R1 index gap (recorded per dispatch)
`R1_INVENTORY/REQUIREMENT_INDEX.csv`, `IMPLEMENTATION_SURFACES.csv`, and
`VERIFICATION_INDEX.csv` contain ZERO rows for DEL-04-05 (`grep DEL-04-05` empty in all
three). This is the known R1 regex parser gap, NOT absence of requirements. The claim set
below was RE-DERIVED directly from `Specification.md` (17 requirements + 5 scope
exclusions), the Datasheet/Guidance/Procedure kit, and live source. Only
`ASSESSMENT_INDEX.csv` and `REMAINING_INVENTORY.csv` carry DEL-04-05 rows.

## Census (post fan-in revision)
- Total rows: 25 (excl. header).
- ClaimType: REQUIREMENT 17, EXCLUSION 5, ACCEPTANCE 1, REMAINING_WORK 1,
  REGISTER_DEFECT 1. (No IMPLEMENTED_UNMAPPED rows after the UNMAPPED-1 retraction below.)
- Disposition: ALIGNED 22, PARTIALLY_IMPLEMENTED 1 (RQ-002), STALE_SPECIFICATION 1
  (ACC-001), REMAINING_STATE_MISMATCH 1 (REGISTER-1).
- SelectableUnderCurrentLoop = YES on exactly one row (REMAINING-1); all others NO (MR-2 ok).
- AssessmentEvidence MR-1 token present exactly once per row.

## Fan-in verification resolution (revision record)
- **UNMAPPED-1 RETRACTED (REFUTED verdict accepted).** The originally flagged
  `CHIRALITY_SDK_SETTING_SOURCES='project'` escape hatch is NOT unmapped behavior. All
  three refutation grounds independently re-verified this session: (a) ratified
  `docs/SPEC.md` §12.2 (lines 673-681) expressly authorizes "Development-only project
  settings MAY use `['project']` behind explicit environment configuration"; (b) sibling
  requirement DEL-04-02-REQ-004 (DEL-04-02 Specification.md line 31) states the hatch
  verbatim, with DEL-04-02-VER-002 as its verification row, so the behavior has a
  requirement owner; (c) my factual predicate "no test exercises the 'project' branch"
  was FALSE — `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 309-328
  assert both `'user,local,project'` rejection to `[]` and `'project'` acceptance to
  `['project']`. Row dropped (retaining it would duplicate DEL-04-02's requirement
  surface); the NEW-PACKET flag is withdrawn.
- **RQ-015 corrected; confidence raised MEDIUM -> HIGH.** The same false "no test
  exercises the escape hatch" statement was removed from its VerificationEvidence and
  replaced with the lines 309-328 test citation; NormativeSource now carries the SPEC
  §12.2 MAY-use-['project'] sentence. The strict-wording tension I originally hedged on
  does not exist — §12.2 itself grants the dev-only latitude. RemainingWork is now
  NONE_OBSERVED.
- **RQ-011 kept ALIGNED (CONTESTED verdict acknowledged, not flipped).** The facts are
  undisputed: all seven category literals implemented
  (anthropic-agent-sdk-manager.ts lines 189-976); only INVALID_BASE_URL,
  NETWORK_POLICY_VIOLATION, INVALID_API_KEY asserted by name in tests; INSP-03 rated
  PARTIAL. My reasoning on the deciding question: the requirement as written ("failures
  must be classified at least as [seven classes]") is a property of the implementation,
  which is fully present at source level — PARTIALLY_IMPLEMENTED would assert that some
  classes are not classified, which is false. The per-class assertion gap is a
  verification-granularity residual, kept explicit in the row's RemainingWork. The
  per-class reading of the §6 behavioral-verification bar is defensible; this contest
  note stands for the run record and does not override the verifier's verdict.

## Least-confident rows (self-flagged; fan-in should recheck these + all non-ALIGNED)
- **RQ-011 (ALIGNED, MEDIUM).** All seven error classes exist in source
  (`anthropic-agent-sdk-manager.ts`: INVALID_BASE_URL, NETWORK_POLICY_VIOLATION,
  INVALID_API_KEY, RATE_LIMITED, API_RESPONSE_ERROR, NETWORK_ERROR, REQUEST_TIMEOUT), but
  the test suite asserts only three by category name (NETWORK_POLICY_VIOLATION,
  INVALID_BASE_URL, INVALID_API_KEY). Alternative reading that would flip it:
  PARTIALLY_IMPLEMENTED or STALE_VERIFICATION, on the view that a behavioral "must be
  classified" requirement is not fully satisfied until timeout/rate-limit/network/API
  classes are test-pinned. I chose ALIGNED because implementation is complete and the gap
  is coverage-only (matches INSP-03's Low-severity gap, kept as RemainingWork).
- ~~RQ-015 + UNMAPPED-1~~ — originally self-flagged here; resolved at fan-in (see "Fan-in
  verification resolution" above: UNMAPPED-1 retracted, RQ-015 corrected and raised to
  HIGH). The original hedge rested on a false factual predicate about test coverage and a
  misread of SPEC §12.2's scope.
- **RQ-002 (PARTIALLY_IMPLEMENTED, MEDIUM).** Provider-boundary redaction + encrypted
  storage are proven here; the whole-product "no key in ANY log/tool-artifact" proof is
  owned by DEL-05-03/PKG-05 (DEP-04-05-011 retired toward DEP-05-03-010). Alternative
  reading: ALIGNED for the provider-boundary slice with the rest simply out of scope. I
  kept PARTIALLY_IMPLEMENTED because the requirement text is written broadly (working root,
  docs, logs, events, git files, tool artifacts) and only part is discharged on this
  surface — matching the INSP-03 PARTIAL.
- **ACC-001 (STALE_SPECIFICATION, HIGH).** Confident: live `_REFERENCES.md` shows REF-006
  MATCH and I recomputed `shasum -a 256 docs/PRD.md` = `ac35fba40...` at fac46e33f. The
  only judgment is disposition shape — STALE_SPECIFICATION (kit flatly asserts a now-false
  HASH_MISMATCH state, MR-8 repair-shaped) vs ACCEPTED_DIVERGENCE. MR-8 tie-break selects
  STALE_SPECIFICATION because no ruling permits the stale wording; the mismatch is simply
  resolved and the kit lags.

## Register-defect summary (MR-5)
- **REGISTER-1** — `Dependencies.csv` DEP-04-05-012 (REF-006 CONSTRAINT) is still
  `ACTIVE` / SatisfactionStatus `TBD`, encoding a PRD-revalidation-before-acceptance
  constraint that is now discharged (REF-006 MATCH, live-reverified). Disposition
  REMAINING_STATE_MISMATCH; R5 register repair = mark SATISFIED/RETIRED.
- Not defects (legitimately open): DEP-04-05-007 (DEL-04-01 first-adapter probe, TBD),
  DEP-04-05-008 (DEL-04-02 interface), DEP-04-05-009 (DEL-04-03 interface), DEP-04-05-010
  (DEL-02-05 interface) — all correctly ACTIVE/TBD. DEP-04-05-011 correctly RETIRED via
  RUL-SCC-001-TRANCHE-001 with a live active-edge pointer.

## Cross-reference / decision notes (MR-7)
- No ruling GOVERNS a DEL-04-05 requirement (DECISION_INDEX shows no deliverable/package
  named for DEL-04-05). Context rulings cited: D-APP-44 (F1 network-expansion fence amended
  to owner-permitted, default-closed, posture-only — RQ-006..009); D-APP-03 and D-APP-52
  (provider generality / governed localhost domain MCP — RQ-010); D-APP-12/D-APP-18 (SDK
  default cutover, settings isolation — RQ-013/015); D-APP-25 (redacted provider metadata
  to events — RQ-005/014/017); D-APP-38 (versioned corpus refresh — ACC-001/REGISTER-1);
  D-APP-46 (harness-contract package extraction — explains tool-descriptor.ts relocation).
- Cross-package (no other project's tree read, F-APP-3): W1's `R2_WAVES/PKG-02/DEL-02-05`
  covers the API-key UI surface. Its R03 note that the ANTHROPIC-before-CHIRALITY env
  tie-break lives in the provider layer is confirmed here at
  `anthropic-agent-sdk-manager.ts:264-266` (RQ-001). EXC-003 explicitly leaves the UI-side
  rows to DEL-02-05; no UI-side rows duplicated.
- Stale evidence pointer (noted, not a separate defect row): INSP-03's RQ-010 citation
  `frontend/src/lib/harness/tool-descriptor.ts` is now
  `frontend/packages/harness-contract/src/tool-descriptor.ts` (D-APP-46). Behavior
  unchanged; flagged as optional R5 pointer refresh under RQ-010 RemainingWork.

## Secrets discipline
No key values or secrets copied into any cell. Redaction/storage/precedence behavior cited
by file + line only.

## Method deviations
None. 19-column §6 header verbatim; MR-1..MR-11 applied; discovery read-only (no source,
test, or kit edits); only the two authorized wave artifacts written.
