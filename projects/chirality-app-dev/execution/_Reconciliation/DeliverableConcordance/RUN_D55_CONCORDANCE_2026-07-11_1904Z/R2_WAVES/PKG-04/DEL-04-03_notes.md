# DEL-04-03 R2 concordance notes — SdkMessageMapper and Provider-Neutral Translation

Run: `RUN_D55_CONCORDANCE_2026-07-11_1904Z`. Source state: `frontend/` at
`fac46e33f`, byte-identical through HEAD `1625b396a` (per W2 dispatch). Behavioral
evidence cites `GATE-TRANSCRIPT(W1@fac46e33f)` (typecheck exit 0; Vitest 667
passed/4 skipped) plus named test cases. Discovery is read-only.

## R1 REQUIREMENT_INDEX gap (recorded per dispatch)

`R1_INVENTORY/REQUIREMENT_INDEX.csv` contains ZERO rows for DEL-04-03 — the
regex parser did not extract this deliverable's requirement IDs. This is a known
parser gap, not an absence of requirements. The claim set here was re-derived
directly from `Specification.md` Requirements table (DEL-04-03-REQ001..REQ014,
lines 28-41), Standards (line 52), Verification (lines 57-65), the Out-of-scope
list (lines 18-22), and the live implementation surface
`frontend/src/lib/harness/sdk-message-mapper.ts` (1274 lines) with its test
`frontend/src/__tests__/lib/sdk-message-mapper.test.ts` (995 lines, 14 cases).
The R1 IMPLEMENTATION_SURFACES / VERIFICATION_INDEX rows for the mapper and its
test are present and were used.

## Census (post fan-in revision)

Total rows: 22.

By ClaimType: REQUIREMENT 14, EXCLUSION 5, IMPLEMENTED_UNMAPPED 1,
REMAINING_WORK 1, REGISTER_DEFECT 1.

By Disposition: ALIGNED 18, PARTIALLY_IMPLEMENTED 1, STALE_ASSESSMENT 1,
IMPLEMENTED_UNDOCUMENTED 1, REMAINING_STATE_MISMATCH 1.

By Confidence: HIGH 15, MEDIUM 7.

HumanDecisionNeeded: NO 21, NEW-PACKET 1 (UNMAPPED-1).

AssessmentEvidence (MR-1 tokens): OVERTAKEN 1 (REQ011), STILL CURRENT 18,
NOT APPLICABLE 3 (UNMAPPED-1, REMAINING-1, REGISTER-1).

## Fan-in verification resolution (revision record)

Two verdicts returned from the W2 fan-in verifier were resolved as follows,
after independently re-verifying the cited decomposition rows and mapper
imports this session:

- **UNMAPPED-2 REFUTED — accepted; row removed.** The former UNMAPPED-2
  (async session-artifact materialization, IMPLEMENTED_UNDOCUMENTED +
  NEW-PACKET) was wrong: `IMPLEMENTED_UNDOCUMENTED` requires no accepted
  mapping anywhere, but decomposition v3.2 assigns the artifact store to
  DEL-05-05 "ToolResultStore and Session Artifacts" (line 322) and child
  output artifact paths to DEL-08-05 "Subagent Child Run Records and
  Artifacts" (line 354) — both re-verified directly this session, as were the
  mapper's imports of `persistToolResultArtifact` / `persistChildOutputArtifact`
  (`sdk-message-mapper.ts` lines 30-31 from `tool-result-artifacts.ts`). The
  mapper is a consumer of owned surfaces, not an unmapped owner. The behavior
  is folded into REQ012's ImplementationEvidence as an owned-surface
  cross-reference; the NEW-PACKET is dropped. **R3 note:** the consumption
  relationship should be cross-checked against the DEL-05-05 ledger (landed in
  W2, `R2_WAVES/PKG-05/DEL-05-05_claims.csv`) and the DEL-08-05 ledger when W3
  lands.

- **REQ014 CONTESTED — flipped ACCEPTED_DIVERGENCE → ALIGNED.** The deciding
  instrument permitting the TBD-until-probe state is the requirement's own
  ASSUMPTION wording (Specification.md line 41), so the deliverable satisfies
  the requirement as written; MR-8's second arm needs a ruling permitting a
  bounded difference, and D-APP-52 gates DEL-04-01's live-LLM demonstration,
  not this kit's wording. This also matches the sibling DEL-04-05 ASSUMPTION
  precedent (ALIGNED). The residual (promote TBD fixtures once DEL-04-01/OI-001
  lands; no `_STATUS.md` Remaining item tracks it) is unchanged and recorded in
  the row. The contest is acknowledged for `_VERIFICATION.md`.

UNMAPPED-1 (message.*/queue.* lane) was CONFIRMED by the verifier and is
retained unchanged, as were the other rechecked rows including REQ011
STALE_ASSESSMENT.

## Key concordance findings

- **REQ011 is the one materially stale assessment (STALE_ASSESSMENT).** INSP-03
  (2026-06-20, SHA `ce0ab7093`) rated REQ011 PARTIAL because the Section 9
  validator named `section9.adapter_message_mapper` while the spec then said
  `section9.sdk_message_mapper` (Gap 1). ADQ-04 (2026-06-21, recorded in the
  deliverable MEMORY.md and `docs/harness/runtime_evidence_reconciliation.md`)
  reconciled the spec to `section9.adapter_message_mapper`. At `fac46e33f` the
  validator (`frontend/scripts/validate-harness-section9.mjs` line 39) and the
  spec (`Specification.md` line 52) agree; the assessment's PARTIAL is the only
  surface still presenting the naming mismatch as open, hence STALE_ASSESSMENT
  with an R5 supersede/annotate remaining item. ADQ-04 is an evidence/
  reconciliation record, not a `D-APP-nn` register decision, so `LatestDecision`
  is `NONE_FOUND` and ADQ-04 is cited narratively (MR-7).

- **REQ008 (PARTIALLY_IMPLEMENTED) is the one live coverage gap.** Deterministic
  mapping is implemented by construction (pure synchronous functions over
  ordered content), and ordered-output fixtures exist, but no test re-runs the
  same input and asserts equality. `runtime_evidence_reconciliation.md` line 45
  explicitly records repeated-input golden assertions as a deferrable later
  tranche. Assessment REQ008 PARTIAL persists (STILL CURRENT).

- **REQ011/REQ013 divergence from INSP-03 PARTIAL:** for REQ013 the INSP-03
  PARTIAL describes the *intended* terminal-ownership split (mapper translates;
  TurnEngine/event store own cleanup and durability), which `Specification.md`
  line 40 mandates — so live surfaces agree and the disposition is ALIGNED, not
  a defect.

- **Register defect (REGISTER-1):** `_DEPENDENCIES.md` Declared Upstream (line
  14) and Declared Downstream (line 18) still read "TBD - no accepted dependency
  edges have been extracted yet" while the same file's register (lines 36-57)
  and `Dependencies.csv` hold 11 ACTIVE extracted rows (DEP-04-03-001..011). Same
  defect class flagged on DEL-04-01 (REGISTER-1). REMAINING_STATE_MISMATCH.

- **Cross-reference / dependency check:** all 11 `Dependencies.csv` rows are
  ACTIVE / SatisfactionStatus=TBD; none carry D-APP-53 satisfaction annotations.
  DEP-04-03-007 (PREREQUISITE to DEL-04-01) and DEP-04-03-008/009 (INTERFACE to
  the runtime-contract and SSE/UIEvent surfaces) remain open — consistent with
  the mapper being downstream of DEL-03-01/DEL-03-03 and DEL-04-01. The
  historical DepClosure SCC-001 record (six-node SCC incl. DEL-04-03) is a prior
  provenance baseline only. No cross-project surfaces were read (F-APP-3).

- **PRD HASH_MISMATCH context:** the kit repeatedly qualifies PRD-derived slices
  (FR-074/FR-075/FR-083/FR-116) as HASH_MISMATCH warning-limited. However this
  deliverable's own `_REFERENCES.md` records REF-006 `docs/PRD.md` as **MATCH**
  at `fac46e33f` (Expected = Actual = `ac35fba4...`), i.e. the same post-D-APP-38
  reconciliation state DEL-04-01 flagged. I did NOT open a separate ACCEPTANCE/
  STALE_SPECIFICATION row for this because DEL-04-03's Specification/Datasheet
  carry the HASH_MISMATCH only as an inline source-state warning (not a distinct
  acceptance condition), and it is folded into the REQ NormativeSource notes.
  Flagged here as a candidate for the same R5 doc-repair sweep as DEL-04-01
  ACC-001 if the orchestrator wants a dedicated row.

## Least-confident rows (self-flagged for fan-in recheck)

The verifier should recheck these plus all non-ALIGNED rows.

1. **REQ014 (originally ACCEPTED_DIVERGENCE, MEDIUM; now ALIGNED after fan-in
   contest)** — original flag: the strongest alternative reading was
   **ALIGNED** (the requirement's own ASSUMPTION text permits the
   TBD-until-probe state), with **REMAINING_STATE_MISMATCH** as a second
   alternative (the probe-refresh residual and DEP-04-03-007 are real yet no
   DEL-04-03 `_STATUS.md` Remaining item tracks them). The fan-in verifier
   contested my original pick and I flipped to ALIGNED — see the fan-in
   resolution section above for the deciding basis.

2. **REQ006 (ALIGNED, MEDIUM)** — alternative reading **PARTIALLY_IMPLEMENTED**:
   REQ006 lists "turn cancellation" as an initial category and the mapper emits
   no `turn.cancelled`. I read it ALIGNED because REQ006 is qualified "where
   corresponding source inputs are present" and cancellation-source
   classification is owned by TurnEngine (REQ013), so there is no mapper-visible
   cancellation input to map.

3. **REQ003 (ALIGNED, MEDIUM)** — alternative reading **PARTIALLY_IMPLEMENTED**
   on the verification method: the Specification names "provider-neutral leakage
   tests [that] inspect mapped outputs for unapproved top-level SDK fields," but
   there is no dedicated leakage test file and no exhaustive negative field
   sweep — leakage is enforced structurally (SDK data confined under `adapter*`
   keys) and verified by positive `toMatchObject` shape plus redaction
   assertions. I read it ALIGNED because the provider-neutral posture is
   structurally guaranteed; the gap is test-form, not behavior.

4. **REQ013 (ALIGNED, MEDIUM)** — alternative reading keeps INSP-03's PARTIAL as
   operative. I judged the ownership split to be spec-intended (line 40), making
   it ALIGNED with `RemainingWork = NONE_OBSERVED`.

5. **UNMAPPED-1 (IMPLEMENTED_UNDOCUMENTED, MEDIUM)** — could instead be read as
   canonical-type emissions already owned by the HarnessEvent-type/TYPES
   contract. I classified it as material live behavior on the mapper surface
   lacking a DEL-04-03 requirement mapping and routed the ownership question to
   a NEW-PACKET / R3 coverage query rather than adopting scope (plan boundary
   1). CONFIRMED by the fan-in verifier; retained. (The former UNMAPPED-2,
   flagged here on the same ownership uncertainty, was REFUTED on exactly that
   alternative reading — the artifact surfaces have owners of record — and was
   removed; see the fan-in resolution section.)

## Register-defect summary

- **REGISTER-1** — `_DEPENDENCIES.md` narrative Declared Upstream/Downstream
  sections stale vs the 11-row extracted register in the same file and in
  `Dependencies.csv`. REMAINING_STATE_MISMATCH, HIGH. Register-hygiene R5
  tranche; identical pattern to DEL-04-01 REGISTER-1.

## Method deviations

None from the pinned plan §§6-7 or the R2 Method Addendum (MR-1..MR-11). One
judgment call recorded above (PRD HASH_MISMATCH not given its own row because the
DEL-04-03 kit carries it as an inline warning rather than a distinct acceptance
condition). No lifecycle transition, no deliverable-document edits, no test
execution, no cross-project reads.
