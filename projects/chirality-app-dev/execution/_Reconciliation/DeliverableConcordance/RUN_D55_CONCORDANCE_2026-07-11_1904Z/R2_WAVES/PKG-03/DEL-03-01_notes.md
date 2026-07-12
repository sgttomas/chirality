# R2 notes — DEL-03-01 AgentEnginePort and Engine Conformance Suite (PKG-03)

Run `RUN_D55_CONCORDANCE_2026-07-11_1904Z`, W2 wave. Source state: `frontend/` at
`fac46e33f` (byte-identical through HEAD `1625b396a`; verified `git rev-parse HEAD`).
Verification bound to `GATE-TRANSCRIPT(W1@fac46e33f)` (typecheck exit 0; Vitest 667
passed/4 skipped) plus named test file/case per MR-3. No tests executed by this agent.

## Census

Total rows: 22.

By ClaimType: REQUIREMENT 15; EXCLUSION 5; REMAINING_WORK 1; REGISTER_DEFECT 1.

By Disposition: ALIGNED 17; PARTIALLY_IMPLEMENTED 3; ACCEPTED_DIVERGENCE 1;
REMAINING_STATE_MISMATCH 1.

Confidence: HIGH 13; MEDIUM 9; LOW 0.

Fan-in correction (accepted): REQ-008 was originally filed PARTIALLY_IMPLEMENTED;
the wave verifier refuted it citing the D-APP-18 ruling record (line 32: live-
conformance limitations are "Known limitations accepted by this ruling (not
preconditions)") and MR-8's second arm. I re-verified that wording in
execution/_Coordination/_DECISIONS/D-APP-18_RULING_2026-06-20.md and accepted:
REQ-008 is now ACCEPTED_DIVERGENCE (D-APP-18 governing), Confidence HIGH, with the
CODEV-001 BLOCKED_TBD evidence-record lag retained in RemainingWork.

## Derivation and scope decisions

- **Requirement set re-derived from Specification.md** (15 REQ IDs REQ-001..REQ-015).
  The R1 REQUIREMENT_INDEX also listed bare `REQ-001..REQ-015` — those are the
  Specification Verification-matrix back-references (duplicate regex hits), not a
  second requirement family. No parser-gap for this deliverable: all 15 IDs parsed.
- **ACCEPTANCE rows: none emitted (MR-4).** The Datasheet "Conditions"/"Attributes"
  (Provider-neutral core, Route compatibility, SSE compatibility, Terminal outcomes,
  Accepted-turn persistence, SDK metadata boundary, Production-default gate,
  Source-state status) are 1:1 restatements of REQ-002/007/008/011/012/006/010/015
  and are folded into those REQ rows rather than duplicated. No datasheet-distinct
  scenario condition exists.
- **IMPLEMENTED_UNMAPPED rows: none.** This deliverable's own surface is the narrow
  contract (`agent-engine-port.ts`, `engine-conformance.ts`) and the runtime contract
  doc; every construct on it maps to a REQ. The adjacent material behaviors that lack
  a mapping (interrupt-time permission-broker clearing; additive `interruption.*` /
  `message.*` audit events) live on DEL-03-04's adapter surface and are already
  captured as `UNMAPPED-1`/`UNMAPPED-2` in the sibling R0 packet
  (`R0_CALIBRATION/DEL-03-04_claims.csv`); not duplicated here per the dispatch's
  no-duplication direction.
- **D-APP-46/D-APP-48 path relocation** (contract spine extracted to
  `@chirality/harness-contract`, in-repo `frontend/src/lib/harness/*` retained as
  back-compat shims): treated as evidence-pointer drift only. INSP-03 rows citing the
  old `frontend/src/lib/harness/agent-engine-port.ts` etc. are marked STILL CURRENT
  with the drift noted; no `STALE_*` disposition on that basis alone (the assessment's
  own D-APP-46 Forward Note already records the relocation).
- **_REFERENCES.md re-verified live (MR-10 SNAPSHOT+LIVE-REVERIFY):** recomputed
  sha256 of docs/DIRECTIVE,CONTRACT,SPEC,TYPES,PLAN,PRD — all 6 equal the recorded
  Expected/Actual hashes at `fac46e33f`. REF-006 MATCH holds; REQ-015 ALIGNED. No
  reference-register defect.
- **_STATUS.md `blocked-on: D-APP-47, D-APP-48, D-T0-09, D-30`** is a CHECKING-era
  header field (recorded 2026-07-04), not a `## Remaining` gate. The D-APP-54
  rebaseline set state to IN_PROGRESS and the sole `## Remaining` item is UNGATED, so
  the blocked-on field does not gate selectability. Not converted to a register-defect
  row (MR-5 scope is Dependencies.csv/_DEPENDENCIES.md/_REFERENCES.md); flagged here as
  stale header metadata for R3/R5 awareness. D-APP-47 and D-APP-48 are both RULED
  (shim migration + publishability mechanism), so the "blocked-on" framing is itself
  overtaken.

## Register-defect summary

- **REGISTER-1 (REMAINING_STATE_MISMATCH, HIGH):** `_DEPENDENCIES.md` prose lags the
  live `Dependencies.csv`. The CSV has `DEP-03-01-006` at `Status=RETIRED`
  (RUL-SCC-001-RESIDUAL-001), but `_DEPENDENCIES.md` still lists it as ACTIVE/PENDING,
  states "Dependencies.csv v3.1 contains 8 ACTIVE rows", and the Lifecycle Summary
  reports ACTIVE 8 / RETIRED 0 / PENDING 5. Live truth: 7 ACTIVE + 1 RETIRED, PENDING 4
  (DEP-03-01-003/005/007/008). Metadata-lag repair for an authorized R5 dependency
  tranche.

## Least-confident rows (self-flagged; alternative reading that would flip them)

The fan-in verifier should recheck these plus every non-ALIGNED row.

1. **REQ-004 (ALIGNED, MEDIUM).** Live `AgentEnginePort.interrupt` is a REQUIRED
   member (agent-engine-port.ts:15), while SPEC 10.2 (line 619) and REQ-004/Datasheet
   describe `interrupt?` as OPTIONAL/"MAY". I read the requirement (interrupt exposed
   and conformance-verified) as satisfied and the optional→required delta as a bounded
   strengthening. **Alternative reading → IMPLEMENTED_DIFFERENTLY** (behavior/type
   differs materially from the normative optional wording), or **STALE_SPECIFICATION**
   for the Datasheet "Optional operation" line if the mandatory port is taken as the
   accepted current state.

2. **REQ-008 (ACCEPTED_DIVERGENCE, HIGH — resolved by fan-in).** Originally filed
   PARTIALLY_IMPLEMENTED with ACCEPTED_DIVERGENCE self-flagged as the alternative
   reading; the fan-in verifier refuted the original and I accepted the alternative
   after re-verifying the D-APP-18 ruling record's "Known limitations accepted by
   this ruling (not preconditions)" wording (MR-8 second arm). No longer a
   low-confidence row; the CODEV-001 evidence-record lag stays in RemainingWork.

3. **REQ-010 (PARTIALLY_IMPLEMENTED, MEDIUM).** The named conformance cases are
   covered, but spread across `engine-conformance.test.ts` plus routes/redaction/mapper
   suites, and Section 9 linkage (DEP-03-01-008 → DEL-09-02) + live-SDK rows remain
   BLOCKED_TBD. **Alternative reading → ALIGNED** if "engine conformance tests SHALL
   cover …" is read at the suite level (coverage exists somewhere in the test corpus)
   and the Section-9/live-SDK items are treated as out-of-slice validation handoffs
   rather than gaps in this deliverable.

4. **REQ-014 (PARTIALLY_IMPLEMENTED, MEDIUM).** `runtime_engine_contract.md` has a
   "Conformance Gates" section but no crisp fallback-criteria section and no
   reliance-boundary (DEL-01-02) cross-link (grep at fac46e33f finds neither
   "fallback" criteria nor "reliance"). **Alternative reading → ALIGNED** if the
   contract-level K-ENGINE-5 fallback doctrine plus the Conformance Gates list is
   accepted as satisfying "the contract documentation SHALL record fallback criteria",
   treating the missing DEL-01-02 cross-link as a pointer nicety not a substantive gap.

5. **REQ-005 (PARTIALLY_IMPLEMENTED, MEDIUM) — lower-risk.** `AgentEngineRunInput`
   carries session/message/opts/contentBlocks; project-root/persona/mode are reachable
   via SessionRecord/ResolvedOpts, but attachment summaries and an explicit cancellation
   signal are not port-level fields. **Alternative reading → ALIGNED** if the named
   concepts are accepted as satisfied through the composed session/opts types and
   out-of-band interrupt/stream-cancel, which is how the running system supplies them.

## Method deviations

None. Applied MR-1..MR-11, the 19-column §6 header verbatim, and the §7 dispositions
plus the MR-5 REGISTER_DEFECT extension. No lifecycle transitions, no test execution,
no writes outside the two wave files. No cross-project execution trees were read
(F-APP-3); cross-tier gates (D-T0-09/D-30) were not adjudicated and do not gate the
sole UNGATED `## Remaining` item.
