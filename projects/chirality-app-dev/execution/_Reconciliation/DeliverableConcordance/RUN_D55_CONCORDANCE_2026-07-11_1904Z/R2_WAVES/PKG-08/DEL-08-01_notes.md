# DEL-08-01 concordance notes — R2 Wave-3 (PKG-08)

Deliverable: DEL-08-01 Instruction Root Packaging and Agent Conformance (Type: TEST_SUITE).
Source state: frontend/ reviewed at fac46e33f (byte-identical through HEAD 74150b3a8;
last frontend commit d2f1cb7ff, working tree clean). Behavioral rows bind to
GATE-TRANSCRIPT(W1@fac46e33f) (typecheck exit 0; Vitest 667 passed/4 skipped) plus named tests.

## Census

Rows: 21 total.

ClaimType:
- REQUIREMENT: 14 (DEL0801-REQ001..014)
- ACCEPTANCE: 1 (DEL0801-ACC-001)
- EXCLUSION: 4 (DEL0801-EXC-001..004)
- IMPLEMENTED_UNMAPPED: 1 (UNMAPPED-1)
- REMAINING_WORK: 1 (REMAINING-1)

Disposition:
- ALIGNED: 21 (all 14 REQ, the ACC, all 4 EXC, REMAINING-1, and UNMAPPED-1 carrying a
  cross-deliverable handle to DEL-09-04)

REGISTER_DEFECT rows: 0.

## Fan-in corrections applied (2026-07-11, accepted after independent re-verification)

1. **UNMAPPED-1 re-dispositioned IMPLEMENTED_UNDOCUMENTED -> ALIGNED (cross-deliverable
   handle: DEL-09-04).** The original row failed the W3 corpus-wide mapping test: packaged-SDK
   verification has an accepted sibling mapping — decomposition v3.2 line 363 assigns DEL-09-04
   "prove required instruction-root assets plus SDK packaging posture are valid" (artifact:
   "SDK subprocess packaging probe"), and DEL-09-04 Specification.md DEL-09-04-REQ-008 (line 32)
   requires verifying the SDK subprocess/binary in the packaged layout. Both sources re-verified
   directly. HumanDecisionNeeded NEW-PACKET -> NO; RemainingWork now carries only the R3
   script-location-vs-owning-requirement reconciliation note.
2. **DEL0801-REQ002 verification evidence corrected (disposition unchanged ALIGNED; Confidence
   MEDIUM -> HIGH).** The row's "no named test drives the inside-instruction-root rejection
   branch" claim was a false absence: frontend/src/__tests__/api/working-root/validate-route.test.ts
   lines 51-57 ("rejects a project root inside the instruction root", 409 WORKING_ROOT_CONFLICT)
   and frontend/src/__tests__/api/harness/routes.test.ts lines 248-263 ("rejects projectRoot
   selections that overlap instruction root", 409 through the session-create route) both drive it.
   Both test files re-verified directly. VerificationEvidence now cites them; the moot
   RemainingWork test suggestion was removed (NONE_OBSERVED).

## Method notes / re-derivation

- The R1 REQUIREMENT_INDEX.csv, IMPLEMENTATION_SURFACES.csv, and VERIFICATION_INDEX.csv
  contain ZERO rows for DEL-08-01 (the known regex parser gap noted in the brief §5). The
  claim set was re-derived directly from Specification.md, which declares 14 requirements
  (DEL0801-REQ001..014), a Standards table, a Verification matrix, and a 4-item Out-of-scope list.
- The INSP-03 assessment (2026-06-21, @d92ef1253) uses IDs `REQ-08-01-00n`; these map 1:1
  by number to the spec's `DEL0801-REQ00n`. The Specification was not rewritten after INSP-03
  (same 14 claims, same substance), so MR-9 old-ID remapping is not triggered beyond noting the
  ID-format equivalence. All 14 were rated PASS; every cited implementation surface and test
  persists at fac46e33f, so each carries `STILL CURRENT`.
- Reviewed source path note: the assessment's paths are relative to WORKING_ROOT
  (projects/chirality-app-dev/); `frontend/` lives there, not at the repo root.

## PKG-08 FROZEN_PROCESS_INPUT handling (plan §3 boundary 8)

DEL-08-01 is a TEST_SUITE that *validates* agent instruction files, the agent roster, and
subagent governance. The validator/script/test surfaces it owns (frontend/src/lib/harness/
agent-instruction.ts, agent-roster.ts, subagent-governance.ts, subagent-bridge.ts, options.ts,
tool-path-policy.ts; frontend/scripts/verify-instruction-root-integrity.mjs; and their tests)
are product runtime/verification code under AUTHORITY_MAP's Implementation/Verification classes —
NOT frozen. The frozen inputs are the agents/AGENT_*.md files and AGENTS.md the validator reads.
Every claim here resolves on concordance FACTS (does the cited validator/test exist; does it
check what the SPEC section 7 / section 1.1 contract requires), which the brief keeps in scope.
No claim's resolution required judging or changing the DESIGN of the agent instruction contract,
so no row is DEFERRED_AGENT_WORKFLOW. The SPEC/CONTRACT/TYPES clauses the tests validate against
are authority corpus (normative), not agent-workflow surfaces.

## Cross-reference / register check (MR-5 duty)

- `_REFERENCES.md` REF-001..007 re-verified against the live tree this run: all seven ExpectedSHA256
  == recomputed live shasum (MATCH), including REF-006 docs/PRD.md (ac35fba40...). REF-007
  AGENT_SOFTWARE_DECOMP.md (cross-repo-root agents/ path) also MATCH.
- `Dependencies.csv` (15 rows) is internally consistent with the `_DEPENDENCIES.md` metrics table
  (6 ANCHOR / 9 EXECUTION; 1 IMPLEMENTS_NODE, 5 TRACES_TO_REQUIREMENT; 8 document prerequisites,
  1 unresolved; 6 SATISFIED / 9 PENDING) and with the D53A closure coverage row
  `DEL-08-01,Y,15,Y,Y`. DEL-08-01 is not among the 11 deliberately-open D53A residual rows.
- No REGISTER_DEFECT emitted. Two observations, neither rising to a defect:
  1. All 8 EXECUTION document-prerequisite rows (DEP-007..014) carry SatisfactionStatus=PENDING
     even though their `_REFERENCES.md` sources are MATCH and accessible; the row Notes say
     "source listed as MATCH". This is the conservative extraction's satisfaction model (SEMANTIC_READY
     maturity, not mere existence), is uniform across siblings, and was accepted by the D53A
     schema-valid closure — read as by-design, not metadata lag.
  2. Declared Upstream/Downstream are `TBD` in `_DEPENDENCIES.md` (extraction ran CONSUMER_CONTEXT=NONE).
     Per the W3 rule (docs/SPEC.md §5.2: Declared sections are human-owned, TBD by design, distinct
     from the agent-owned Extracted register), a bare Declared-TBD is NOT a register defect.
     DEP-08-01-015 ("TBD current instruction-root source tree", PENDING/UNKNOWN) is a deliberately
     open EXECUTION prerequisite, likewise not a defect.

## Least-confident rows (self-flagged; all rechecked at fan-in — recheck outcomes noted)

- **DEL0801-REQ002 — RESOLVED at fan-in (now ALIGNED, HIGH).** Originally flagged for a supposed
  missing enforcement-branch test; that was a false absence corrected above (see Fan-in
  corrections item 2). No alternative reading survives: the rejection path is route-tested twice.
- **DEL0801-REQ010 (ALIGNED, MEDIUM — CONFIRMED at fan-in).** The validator implements MISSING_WRITE_SCOPE (error) and
  UNKNOWN_WRITE_SCOPE (warning), but no negative fixture omits WRITE_SCOPE or supplies an
  out-of-vocabulary value; only the valid `deliverable-local` case is asserted. Alternative reading:
  the requirement's "Validator checks WRITE_SCOPE value" is only positively demonstrated, so a strict
  reviewer could call the value-check verification STALE_VERIFICATION until a negative fixture exists.
- **DEL0801-REQ012 (ALIGNED, HIGH — CONFIRMED at fan-in; flagged for the shared-surface nuance).** The fail-closed conformance
  is fully tested, but its implementation evidence (subagent-governance.ts / subagent-bridge.ts) is the
  same surface EXC-003 declares owned by DEL-08-04. Alternative reading: if DEL-08-04 is the sole owner of
  that runtime code, REQ012's "implementation" for a TEST_SUITE deliverable is really its fixtures/tests
  (which do exist), and the row stays ALIGNED — but an R3 reviewer may prefer to record the evidence as a
  cross-deliverable citation rather than DEL-08-01-owned implementation.
- **DEL0801-EXC-003 (ALIGNED, MEDIUM — CONFIRMED at fan-in).** Declares the subagent bridge implementation
  out-of-scope (DEL-08-04), yet subagent-bridge.ts/subagent-governance.ts are cited as DEL-08-01 conformance
  evidence. Alternative reading: if those files are found unmapped or double-claimed at R3, this is a
  REMAINING_STATE_MISMATCH (ownership metadata disagreement) rather than a clean exclusion.
- **UNMAPPED-1 — REFUTED at fan-in (now ALIGNED, HIGH, cross-deliverable handle DEL-09-04).** The
  originally flagged alternative reading was in fact correct: decomposition v3.2 line 363 and
  DEL-09-04-REQ-008 already own packaged-SDK verification, so the W3 accepted-sibling-mapping rule
  applies (see Fan-in corrections item 1).

## Other observations (not claim-flipping)

- agent-roster.ts also carries direct-chat persona gating (isDirectChatPersona / selectDirectChatPersonas /
  assertDirectChatPersona, D-APP-24 Type-0/Type-1 restriction). That behavior belongs to the direct-chat /
  persona-surface deliverables (cf. DEL-02-01's UNMAPPED-2 /chat and UNMAPPED-4 persona-picker rows), not to
  DEL-08-01's test-suite scope, so it is not emitted as a DEL-08-01 unmapped surface. REQ006 uses only the
  roster's AGENT_*.md naming/discovery aspect.
- "No test exists" style absence claims in the REQ008/REQ009/REQ010 notes were grepped against the frontend
  test trees before asserting: the malformed-marker-pair branch, the per-non-AGENT_TYPE-row omission, and the
  missing/unknown WRITE_SCOPE fixtures are genuinely absent at fac46e33f; the positive/other-negative cases
  they sit beside do exist.
