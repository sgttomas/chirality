# DEL-05-01 concordance notes — R2 Wave-2 (RUN_D55_CONCORDANCE_2026-07-11_1904Z)

Source-state binding: `frontend/` at `fac46e33f` (byte-identical to `4c8ed8907`/`61d70bdb0`
through HEAD `1625b396a`; `git diff fac46e33f HEAD` empty for session-manager.ts,
session-manager.test.ts, and packages/harness-contract/src/types.ts). Behavioral rows cite
`GATE-TRANSCRIPT(W1@fac46e33f)` (typecheck exit 0; Vitest 667 passed/4 skipped) plus the named
test file/case per MR-3.

## R1 REQUIREMENT_INDEX parser gap (recorded per dispatch)
REQUIREMENT_INDEX.csv contains ZERO rows for DEL-05-01, while sibling deliverables DEL-05-04
(13 rows) and DEL-05-05 parsed normally. Cause: DEL-05-01 numbers its requirements `DEL-05-01-R001`
.. `DEL-05-01-R016`, whereas the R1 regex expects the `-REQ-nnn` form. The claim set here was
re-derived directly from Specification.md Requirements table (R001-R016), Standards, and the
Verification table (A-001/B-001/F-001/E-002 review checks). ASSESSMENT_INDEX, REMAINING_INVENTORY,
IMPLEMENTATION_SURFACES (session-manager.ts, 252 lines) and VERIFICATION_INDEX
(session-manager.test.ts, 226 lines) all carry correct DEL-05-01 rows; only REQUIREMENT_INDEX is affected.

## Census
- Rows total: 28 claim rows (+ header).
- By ClaimType: REQUIREMENT 16 (R001-R016); ACCEPTANCE 4 (A-001/B-001/F-001/E-002); EXCLUSION 5
  (the five Specification "Out of scope" bullets); IMPLEMENTED_UNMAPPED 2; REMAINING_WORK 1.
- By Disposition: ALIGNED 24; PARTIALLY_IMPLEMENTED 2 (R002, R013);
  IMPLEMENTED_UNDOCUMENTED 2 (UNMAPPED-1, UNMAPPED-2).
- Fan-in correction (accepted): R009 and ACC-004 flipped ACCEPTED_DIVERGENCE -> ALIGNED and R013
  flipped ACCEPTED_DIVERGENCE -> PARTIALLY_IMPLEMENTED per verifier root cause. D-APP-41's Scope
  Boundaries clause ("This ruling does not authorize ... SDK transcript placement finalization",
  re-verified in D-APP-41_RULING_2026-06-21.md lines 40-45) is a WITHHELD authorization, not a human
  decision deliberately permitting a divergence, so it cannot anchor §7 ACCEPTED_DIVERGENCE; R013's
  LatestDecision is NONE_FOUND, making that disposition definitionally unavailable there.
- REGISTER_DEFECT rows: 0 (see register-defect summary).

## Key findings
- Implementation refactored since INSP-03: the `SessionRecord`/`SessionCreateRequest`/`ISessionManager`
  types moved from `frontend/src/lib/harness/types.ts` to `frontend/packages/harness-contract/src/types.ts`
  under the D-APP-48 harness-contract package extraction. INSP-03 R006/R007 cite the old `types.ts`
  path; the PASS conclusions still hold, only the file location changed. Recorded as STILL CURRENT with
  a note, not STALE_ASSESSMENT (the conclusion is not overtaken, only the pointer lags).
- Governing decision D-APP-41 (eager legacy conversion, Option D) governs R001/R003/R004/R010/R016 and
  the F-001 duplicate acceptance. Its Scope Boundaries clause withholds authorization for SDK transcript
  placement finalization — context for why placement stays open, but not a permission that could anchor
  ACCEPTED_DIVERGENCE (see fan-in correction above). R009/ACC-004 are ALIGNED because their conditional
  requirement/check is met as worded; the placement decision itself is excluded scope (EXC-005) carried
  on DEL-04-01.
- DEP-05-01-008 (DEL-04-01 / OI-002 SDK transcript placement) re-verified ACTIVE/TBD: DEL-04-01 remains
  IN_PROGRESS with transcript/session placement a live residual gated on D-APP-52 (owner act). The
  transcript-placement deferral in the DEL-05-01 kit is therefore still accurate, not stale.

## Least-confident rows (self-flagged; alternative reading that would flip each)
- **R002 (PARTIALLY_IMPLEMENTED, MEDIUM):** classified partial because turns/ and sdk/ are not eagerly
  materialized (only session.json + demand-driven events.jsonl). Alternative reading -> ALIGNED: the
  spec verb is "MUST support ... as the physical layout"; a folder that can host those subpaths arguably
  "supports" the layout without pre-creating empty dirs, and INSP-03 itself rates the gap Low/acceptable.
  Flip hinges on whether "support" means "materialize" or "be compatible with".
- **R009 (now ALIGNED, MEDIUM; originally self-flagged as ACCEPTED_DIVERGENCE):** I noted the ALIGNED
  alternative reading (conditional MUST fully met at the metadata layer); fan-in verification adopted
  exactly that reading, since the open OI-002 placement question is excluded scope (line 21 / EXC-005)
  carried on DEL-04-01, leaving no divergence on this row to accept.
- **R013 (now PARTIALLY_IMPLEMENTED, MEDIUM; originally self-flagged as ACCEPTED_DIVERGENCE):** I noted
  the PARTIALLY_IMPLEMENTED alternative (missing positive test treated as an implementation gap); fan-in
  adopted it — Spec Verification (line 65) requires a redaction/security test for session metadata, none
  exists (verifier grep concurs), and with LatestDecision NONE_FOUND, ACCEPTED_DIVERGENCE was
  definitionally unavailable. Residual: add a session.json secret-exclusion test.
- **ACC-004 (now ALIGNED, MEDIUM; originally self-flagged as ACCEPTED_DIVERGENCE):** mirrors R009 and
  flipped with it — the E-002 check (residual note present, no placement claim) is satisfied as worded.
- **UNMAPPED-1 (IMPLEMENTED_UNDOCUMENTED, MEDIUM):** the assertSafeSessionId path-traversal guard is
  material live behavior with no requirement mapping and no direct test. Alternative -> fold into R011/R012
  (stable/safe IDs) and drop as a separate unmapped row if a reviewer reads those requirements as
  implicitly covering input validation.
- **UNMAPPED-2 (IMPLEMENTED_UNDOCUMENTED, LOW):** the instruction-root/WORKING_ROOT_CONFLICT containment guard
  appears on DEL-05-01's named surface but likely belongs to a PKG-03 working-root deliverable.
  Alternative -> fold into R005 ("bound to normalized project root") and drop, if R005 is read to include
  containment enforcement. Left as a low-confidence unmapped row for R3 cross-package synthesis to resolve.

## Register-defect summary
No REGISTER_DEFECT rows emitted. Cross-checks performed against the live tree at fac46e33f/HEAD:
- `_REFERENCES.md`: all 7 references (REF-001..REF-007) recomputed by shasum — every ExpectedSHA256
  MATCHES the live file, including the absolute-path agent-file REF-007. No drift.
- `Dependencies.csv` (12 rows): live targets verified. DEP-05-01-006 code targets (session-manager.ts,
  session-manager.test.ts) exist; DEP-05-01-005 corpus refs MATCH; DEP-05-01-008 (DEL-04-01/OI-002)
  correctly TBD (still open); DEP-05-01-007 correctly RETIRED. Internally consistent.
- `_DEPENDENCIES.md`: summary counts (Total 12 / ACTIVE 11 / RETIRED 1; SatisfactionStatus
  NOT_APPLICABLE 4 / SATISFIED 4 / TBD 4) reconcile exactly with Dependencies.csv. The documented
  ID_FORMAT_HELPER_MISMATCH warning is self-recorded and expected (validator wants PKG-000 form), not a defect.
- Minor non-register wording lag (NOT a defect): the kit labels the authority corpus "D-APP-38 corpus v2"
  (Datasheet line 46, Specification line 55) while AUTHORITY_MAP records the current snapshot as v6
  (RATIFIED 2026-07-11). Per MR-11 the v6 re-ratification was lifecycle-scoped and did not change these
  doc contents — all reference hashes are byte-identical to the recorded values — so reference integrity
  holds and the label lag is a cosmetic R5 doc-refresh candidate, not a register or reference defect.

## Method deviations
None. Followed the pinned plan §§6-7, R2_METHOD_ADDENDUM MR-1..MR-11, and the R0 exemplar format
(19-column header verbatim). No tests executed, no dependencies installed, writes confined to the two
authorized files under R2_WAVES/PKG-05/.
