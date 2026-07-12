# DEL-03-03 Harness API and SSE Compatibility Adapter — R2 concordance notes

Run: `RUN_D55_CONCORDANCE_2026-07-11_1904Z` (Wave 2, PKG-03). Source state:
`frontend/` at `fac46e33f`, byte-identical through HEAD `1625b396a`
(orchestrator-verified). Behavioral verification cites
`GATE-TRANSCRIPT(W1@fac46e33f)` (typecheck exit 0; Vitest 667 passed / 4
skipped) plus named test files/cases. No tests executed by this agent.

## Census

20 claim rows (+ header).

By ClaimType: REQUIREMENT 10, EXCLUSION 4, ACCEPTANCE 2, IMPLEMENTED_UNMAPPED 1,
REMAINING_WORK 1, REGISTER_DEFECT 2.

By Disposition: ALIGNED 16, PARTIALLY_IMPLEMENTED 1, IMPLEMENTED_UNDOCUMENTED 1,
REMAINING_STATE_MISMATCH 2.

(Revised at fan-in: REQ-010 flipped PARTIALLY_IMPLEMENTED -> ALIGNED per the
verifier's REFUTED verdict, accepted after independent re-verification of
Specification.md line 35; see "Least-confident rows" item 1 and "Fan-in
revision record" below.)

By Confidence: HIGH 12, MEDIUM 8, LOW 0.

AssessmentEvidence tokens (MR-1): STILL CURRENT 9, OVERTAKEN 2, NOT APPLICABLE 9.

## Re-derivation vs R1 REQUIREMENT_INDEX

R1 regex scan listed exactly the ten spec requirement IDs (REQ-001..010); the
re-derivation from `Specification.md` confirms those ten plus four Out-of-scope
exclusion bullets (EXC-001..004), two datasheet-distinct acceptance conditions
(ACC-001 active-turn, ACC-002 disconnect; MR-4 folds the compatibility/
stream-termination/source-state conditions into their covering REQ rows), one
IMPLEMENTED_UNMAPPED route-catalog finding, the single `## Remaining` bootstrap,
and two register defects. No parser gap for this deliverable (the ten IDs were
scanned cleanly).

## Key judgments

- Behavioral core of the deliverable (route-shape preservation, eight-name SSE
  compatibility, UIEvent/HarnessEvent separation, mapper boundary, transport-
  adapter delegation, terminal/disconnect stream behavior) is ALIGNED and
  suite-bound. REQ-004 and ACC-002 carry AssessmentEvidence OVERTAKEN by the
  same ORN-09 close (commit `24f40d5d8`) that overtook the sibling DEL-03-04
  REQ-004/ACC-002 disconnect-persistence gaps.
- One artifact-completeness requirement is PARTIALLY_IMPLEMENTED: REQ-008 (kit
  artifacts). Route adapter tests and a substantial UI event contract doc
  (`frontend/docs/harness/runtime_engine_contract.md`) exist, but the dedicated
  SSE compatibility fixture README and populated fixtures do not. This residual
  is NOT recorded in `_STATUS.md ## Remaining` (which holds only the concordance
  bootstrap), so REQ-008 carries HumanDecisionNeeded = NEW-PACKET
  (produce-artifacts vs ruled-deferral acceptance choice), mirroring the sibling
  R0 precedent of routing bounded acceptance choices to NEW-PACKET.
- REQ-010 (route adapter test index) is ALIGNED: Procedure.md lines 70-78 list
  every SPEC 17.1/PRD 9.1 route with explicit TBD capture status — the interim
  state the requirement expressly permits ("a fixture path or `TBD` capture
  status") before exact compatibility assertions are closed, and its
  Verification column requires only that every cataloged route appear in the
  index. The fixture-population residual stays homed on REQ-008 and
  Dependencies.csv DEP-03-03-010; nothing is lost by the flip.
- REF-006 (`docs/PRD.md`) hash re-verified live: `shasum -a 256 docs/PRD.md`
  reproduces the recorded `ac35fba4...c30bfd`; REQ-009 ALIGNED on
  DOC-BASIS(D-APP-38).

## Least-confident rows (self-flagged; alternative readings that would flip)

1. **REQ-010 (now ALIGNED, MEDIUM — revised at fan-in).** Originally filed
   PARTIALLY_IMPLEMENTED with ALIGNED as the flagged alternative reading; the
   fan-in verifier REFUTED the original disposition on that exact alternative.
   Accepted after independently re-verifying Specification.md line 35: the
   requirement maps each route to "a fixture path or `TBD` capture status
   before exact compatibility assertions are closed," and its Verification
   column requires only that every SPEC 17.1/PRD 9.1 route appear in the index.
   Procedure.md lines 70-78 satisfy that in the expressly permitted interim TBD
   state. INSP-03's stricter PARTIAL reading is an assessment record, not
   current truth; the fixture-population residual remains homed on REQ-008 and
   DEP-03-03-010.

2. **REQ-001 (ALIGNED, MEDIUM).** Alternative reading: PARTIALLY_IMPLEMENTED.
   Route shapes are preserved and regression-tested, but the requirement's own
   Verification column names a route-shape *fixture-compare* harness that does
   not exist (behavior tests stand in), and INSP-03 rated it PARTIAL for the
   same missing fixture capture. I kept ALIGNED because the behavioral
   requirement ("preserve the existing route shapes") is fully met and verified;
   the missing artifact is a verification-method refinement tracked on
   REQ-010/REQ-008. If the verifier treats the fixture-capture apparatus as part
   of REQ-001's own acceptance, this flips to PARTIALLY_IMPLEMENTED.

3. **REQ-002 (ALIGNED, MEDIUM).** Alternative reading: IMPLEMENTED_DIFFERENTLY.
   REQ-002 and the Datasheet "Turn route role" enumerate "session locking" as a
   route responsibility, but lock acquisition physically lives inside
   `TurnEngine.runTurn` (DEL-03-02 design scope); the live route is a thinner
   adapter that over-satisfies the delegation principle. I kept ALIGNED because
   the requirement's substantive assertion (transport adapter, policy delegated
   to TurnEngine) holds and is strengthened; the "obtains session lock" phrasing
   reads as the route's transitive responsibility. A strict reader could call
   the enumerated-responsibility mismatch IMPLEMENTED_DIFFERENTLY.

4. **UNMAPPED-1 (IMPLEMENTED_UNDOCUMENTED, MEDIUM).** Alternative reading: out of
   scope for DEL-03-03 entirely (no row). The three extra `/api/harness/*`
   routes (events / permission / agents) are on the harness API surface but
   plausibly owned by DEL-05-02 / PKG-06 / PKG-08. I recorded them because the
   deliverable's requirements speak of "each in-scope `/api/harness/*` route"
   and the SPEC 17.1 catalog omits them, making catalog completeness a genuine
   R3 mapping question. If DEL-03-03's surface is read as strictly the seven
   cataloged routes, this row is unnecessary.

## Register-defect summary (MR-5)

- **REGISTER-1** (REMAINING_STATE_MISMATCH): `_DEPENDENCIES.md` Declared
  Upstream/Downstream (lines 14, 18) still say "TBD - no accepted dependency
  edges have been extracted yet," contradicting the same file's ten-row
  Extracted Dependency Register and `Dependencies.csv` (10 rows). Stale
  scaffolding text.
- **REGISTER-2** (REMAINING_STATE_MISMATCH): `_DEPENDENCIES.md` lists
  `DEP-03-03-009` as ACTIVE and reports 10 ACTIVE / 0 RETIRED and
  SatisfactionStatus 5 NOT_APPLICABLE / 5 TBD, but `Dependencies.csv` marks
  `DEP-03-03-009` RETIRED (RUL-SCC-001-TRANCHE-001, 2026-05-24; `DEL-04-03-009`
  is the active replacement edge). The `.md` count tables lag the CSV retirement
  (true live split among CSV rows: 9 ACTIVE / 1 RETIRED; 6 NOT_APPLICABLE /
  4 TBD).

Both are metadata-lag defects in the deliverable-local register, not product
behavior; routed for R5 register repair.

## Non-defect observations (not rows, for R3/R5 context)

- The UI event contract doc `frontend/docs/harness/runtime_engine_contract.md`
  still cites pre-D-APP-48 paths `frontend/src/lib/harness/event-schema.ts` and
  `frontend/src/lib/harness/agent-engine-port.ts`; both relocated to
  `frontend/packages/harness-contract/src/`. Folded into REQ-008 RemainingWork
  (documentation-pointer refresh), not a separate register row.
- Open interface/prerequisite dependency edges DEP-03-03-006 (TurnEngine
  boundary doc), -007 (DEL-03-04 interrupt/cancel), -008 (PKG-05 UIEvent/
  HarnessEvent separation), -010 (fixture capture) remain SatisfactionStatus TBD
  in the CSV and align with the live tree (all target folders/docs exist);
  DEP-03-03-010 (fixture capture) tracks the same residual as REQ-008/REQ-010.
  These are legitimate open edges, not defects.

## Fan-in revision record

One verifier verdict returned REFUTED and was accepted: REQ-010
PARTIALLY_IMPLEMENTED -> ALIGNED (basis re-verified independently against
Specification.md line 35 before editing). Row edits: Disposition,
DeclaredState/ImplementationEvidence/VerificationEvidence rephrased to the
requirement's expressly-permitted interim TBD state, RemainingWork re-pointed
to the REQ-008/DEP-03-03-010 residual home, HumanDecisionNeeded NEW-PACKET ->
NO (the acceptance choice lives on REQ-008, which keeps NEW-PACKET).

MR-1 token decision: REQ-010's AssessmentEvidence keeps STILL CURRENT, not
OVERTAKEN. INSP-03's factual observation (no populated route-to-fixture index)
still holds at fac46e33f and was equally true when assessed — nothing later
overtook it; the disagreement is interpretive (its PARTIAL verdict applied a
stricter reading than the requirement's "or TBD" clause). The cell text states
this explicitly so the token is not read as endorsing the PARTIAL verdict.

## Method deviations

None. Ledger follows the pinned plan §§6-7 header, the R2 Method Addendum
MR-1..MR-11, and the R0 DEL-03-04 sibling precedent (terminal-taxonomy /
LatestDecision handling; no sibling rows duplicated).
