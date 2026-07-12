# DEL-09-06 concordance notes (R2 Wave-4, RUN_D55_CONCORDANCE_2026-07-11_1904Z)

Deliverable: DEL-09-06 Network, Key, Attachment, and Renderer Security Checks (PKG-09).
Source state: `frontend/` at fac46e33f (byte-identical fac46e33f..HEAD 6f7c06814; `git diff --stat` empty). Behavioral verification cites GATE-TRANSCRIPT(W1@fac46e33f) (typecheck exit 0; Vitest 667 passed/4 skipped) plus named test files/cases.

## Census

Rows: 21 total.

By ClaimType: REQUIREMENT 15 (REQ-001..015), EXCLUSION 3, ACCEPTANCE 1, REGISTER_DEFECT 1, REMAINING_WORK 1.

By Disposition:
- ALIGNED 16 (REQ-001,003,004,005,006,007,008,009,010,011,012,014; EXC-001,002,003; REMAINING-1)
- PARTIALLY_IMPLEMENTED 3 (REQ-002, REQ-013, REQ-015)
- STALE_SPECIFICATION 1 (ACC-001)
- REMAINING_STATE_MISMATCH 1 (REGISTER-1)

Assessment recency tokens (MR-1): OVERTAKEN on REQ-006 and ACC-001; NOT APPLICABLE on EXC-001/002/003, REGISTER-1, and REMAINING-1; STILL CURRENT on the remaining REQ rows.

## Method / mapping notes

- The INSP-03 assessment (2026-06-21, SHA d0766e0f2) labels requirements `REQ001`..`REQ015`, which map 1:1 to `DEL-09-06-REQ-001`..`015`. The Specification was not rewritten after INSP-03 (same REQ IDs, same order), so MR-9 old-ID mapping is not triggered.
- REQUIREMENT_INDEX.csv double-counts this deliverable (both `DEL-09-06-REQ-0nn` and bare `REQ-0nn` rows) — a known R1 parser artifact, not two requirement sets. The 15 canonical `DEL-09-06-REQ-0nn` IDs are the real claim set, re-derived from Specification.md lines 24-38. VERIFICATION_INDEX.csv and IMPLEMENTATION_SURFACES.csv scanned ZERO rows for DEL-09-06 (the parser gap the brief warns about); the real test/impl surfaces were re-derived by grep over `frontend/` (recorded in each row).
- Line anchors were re-read at the current worktree (`frontend/` under WORKING_ROOT = projects/chirality-app-dev/). The INSP-03 anchors had drifted a few lines since SHA d0766e0f2 (e.g. main.ts egress block cited 105-128 there, 124-147 now); rows carry the current fac46e33f anchors.
- Runtime under test is owned by feature deliverables, not DEL-09-06 (a SECURITY_CONTROL verification deliverable). `api-key-storage.ts` header names DEL-02-06; main.ts / attachment-resolver / anthropic manager are feature surfaces. DEL-09-06 owns the checks/fixtures. This is why no IMPLEMENTED_UNMAPPED rows were emitted: the material live behavior on these surfaces has accepted feature-deliverable mappings (cross-deliverable handle), so IMPLEMENTED_UNDOCUMENTED does not apply.
- REQ-015 carries a cross-deliverable handle to DEL-09-05 (CI, Artifact, and Release Verification Workflow), which owns release-evidence assembly. Recorded in the row, not raised as a defect.

## Register-defect summary

One REGISTER_DEFECT row: **REGISTER-1** (REMAINING_STATE_MISMATCH, HIGH). [Corrected at fan-in 2026-07-12: an earlier revision of these notes wrongly stated the stale REF-006 wording was "NOT in the live register".]
- `_DEPENDENCIES.md` line 61 still carries the `[WARNING] SOURCE_HASH_MISMATCH` REF-006 wording without a superseding annotation, and `Dependencies.csv` line 8 (DEP-09-06-007) Notes states, present tense, "PRD hash mismatch remains a warning". Both lag `_REFERENCES.md` line 12, which now records REF-006 as MATCH (Expected==Actual; live `shasum -a 256 docs/PRD.md` reproduces it) after D-APP-35/D-APP-38. Same defect class ledgered by siblings DEL-09-02/DEL-09-04 as REGISTER-1; class harmonization is an R3 item.
- The kit-document instances of the same stale wording (Datasheet/Specification/Guidance) remain carried on ACC-001 as STALE_SPECIFICATION; REGISTER-1 covers only the register-file metadata lag.
- Otherwise `Dependencies.csv` (10 rows) and `_DEPENDENCIES.md` Extracted register (10 rows) are internally consistent (IDs, classes, types, targets, counts all agree); all 10 carry SatisfactionStatus TBD, which is the normal extracted-register state for anchor + prerequisite edges, not a defect. The DepClosure baseline (`_LATEST.md` -> CLOSURE_D53A_...) coverage.csv row `DEL-09-06,Y,10,Y,Y` re-verifies against the live 10-row register.
- `_DEPENDENCIES.md` Declared Upstream/Downstream = TBD is human-owned by design (docs/SPEC.md §5.2 per the Wave-4 rule); not a defect.

## Least-confident rows (self-flagged; fan-in should recheck these plus all non-ALIGNED rows)

1. **REQ-002 (PARTIALLY_IMPLEMENTED).** Enumerated-sink redaction and safeStorage-outside-projectRoot are implemented and unit-tested (bound to W1), but no whole-worktree/log/event/artifact secret scan is archived bound to fac46e33f (the ADQ-16 `proof:secret-scan` PASS ran on branch codex/fuwenc-24554 base 2e98d998f, not this state). Alternative reading that would flip it: treat the tested enumerated sinks as full coverage of the negative property -> **ALIGNED** with a freshness caveat. I kept PARTIALLY_IMPLEMENTED because the requirement is an all-sinks property and the whole-artifact scan (the assessment's High gap) is not closed at the source state.

2. **REQ-005 (ALIGNED, MEDIUM).** The renderer egress policy is verified only by a source-TEXT assertion in build-network-policy.test.ts (it reads main.ts as a string and `.toContain`s the allowlist/log constructs); `evaluateRendererEgressPolicy` is not exported or behaviorally invoked. Spec REQ-005 permits an "equivalent test seam," so I called it ALIGNED. Alternative reading: a source-string check is not a behavioral test -> **PARTIALLY_IMPLEMENTED** or **STALE_VERIFICATION**.

3. **REQ-006 (ALIGNED, MEDIUM; assessment OVERTAKEN).** The INSP-03 PARTIAL ("query/userinfo sanitization not independently proven") is overtaken because build-network-policy.test.ts lines 50-54 now assert the log emits only summarized hostname/port/protocol and explicitly `not.toContain('url: details.url')`. Same source-text-seam caveat as REQ-005. Alternative reading: seam weakness keeps it **PARTIALLY_IMPLEMENTED** / assessment STILL CURRENT.

4. **REQ-007 (ALIGNED, MEDIUM).** Provider-constraint mechanism (base URL validation) is behaviorally tested and the scripted-proof no-broaden mode is source-asserted, but no source-state-bound live/packaged network-proof artifact exists at fac46e33f. Alternative reading: treat the missing fresh proof artifact as a coverage gap -> **PARTIALLY_IMPLEMENTED** / **STALE_VERIFICATION**.

5. **REQ-013 (PARTIALLY_IMPLEMENTED).** Draft/attachment persistence+sanitization helpers are tested, but no end-to-end failed-send retry workflow test proves preservation across an API failure. Alternative reading: helper-level tests satisfy "where attachment failure recovery is exercised" -> **ALIGNED**.

6. **REQ-015 (PARTIALLY_IMPLEMENTED).** Command family exists and exact spellings are now resolvable, but the Specification itself still holds test-file/artifact paths as TBD (C-001/D-001) and no consolidated source-state-bound evidence package exists. Alternative reading: since REQ-015 explicitly defers exact spelling/artifacts to TBD by design, the present command family could read as **ALIGNED** against the requirement's own deferral.

7. **ACC-001 (STALE_SPECIFICATION, HIGH).** High confidence (live hash recompute == recorded MATCH; D-APP-35/38 govern). Flagged only because it is non-ALIGNED and drives an R5 doc-repair recommendation across four kit locations.

8. **REGISTER-1 (REMAINING_STATE_MISMATCH, HIGH; added at fan-in correction).** The `_DEPENDENCIES.md` line 61 warning sits under a dated heading ("Run Notes - 2026-05-20 Dependency Extract"), so an alternative reading treats it as a dated historical run note needing no defect row (the DEL-09-03 dated-correction model). I ledgered it anyway because (a) the wording carries no superseding annotation and remains readable as current caveat, and (b) the `Dependencies.csv` DEP-09-06-007 Notes cell repeats it in present tense in the live structured register, which the dated-run-note reading cannot excuse. Class harmonization across DEL-09-02/03/04/06 is an R3 item.

## Method deviations

None. Read-only throughout; no tests executed (GATE-TRANSCRIPT(W1@fac46e33f) used per MR-3); no secret/key values copied into any cell or note (only document SHA-256 hashes, which are not secrets, appear). Write scope limited to this file and DEL-09-06_claims.csv.
