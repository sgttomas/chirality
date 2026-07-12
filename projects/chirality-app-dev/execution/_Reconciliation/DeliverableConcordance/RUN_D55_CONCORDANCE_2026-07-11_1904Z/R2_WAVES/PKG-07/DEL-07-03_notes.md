# DEL-07-03 concordance notes — RUN_D55_CONCORDANCE_2026-07-11_1904Z (PKG-07, W3)

Deliverable: DEL-07-03 Deliverable Metadata and Document Kit Contracts.
Reviewed source state: frontend/ at `fac46e33f` (byte-identical through HEAD
`74150b3a8`); scanner implementation landed at commit `73ccf07d5`
(2026-06-21, "Add deliverable contract scanner"), which is present at the
reviewed state. Behavioral rows bind to `GATE-TRANSCRIPT(W1@fac46e33f)`
(typecheck exit 0; Vitest 667 passed/4 skipped).

## Census

Row count total: 17.

By ClaimType:
- REQUIREMENT: 10 (DEL-07-03-REQ-001..010)
- ACCEPTANCE: 1 (ACC-001, REF-006 hash posture)
- EXCLUSION: 4 (EXC-001..004)
- REGISTER_DEFECT: 1 (REGISTER-1)
- REMAINING_WORK: 1 (REMAINING-1)

By Disposition (as corrected at W3 fan-in; see revision note below):
- ALIGNED: 14 (REQ-001..009 — with AssessmentEvidence=OVERTAKEN on
  REQ-001,002,003,004,005,006,007,009 — plus EXC-001..004 and REMAINING-1)
- STALE_SPECIFICATION: 2 (REQ-010; ACC-001)
- REMAINING_STATE_MISMATCH: 1 (REGISTER-1)

## Fan-in revision note (W3)

My initial submission classed REQ-001,002,003,004,005,006,007,009 as
STALE_ASSESSMENT — exactly the class self-flagged below with the alternative
reading that would flip it. The fan-in verifier refuted the class on that
alternative reading, and I independently re-verified the basis before
correcting: (a) the ADQ-07 Superseding Note (Assessment lines 15-24) expressly
recasts the matrix FAIL/PARTIAL/TBD cells as the recorded pre-scanner state and
points at current evidence, so the file no longer presents them as current
truth and MR-1's reserve condition for STALE_ASSESSMENT ("some surface still
presents the stale conclusion as current truth") is not met; (b) repo-wide grep
confirms the precedents I had cited (R0 DEL-02-01; W2 DEL-04-03) carry no
superseding note and are distinguishable — only DEL-07-02 and DEL-07-03
assessments have one; (c) sibling DEL-07-02 treats the structurally identical
ADQ-06 note as ALIGNED + AssessmentEvidence=OVERTAKEN. All eight rows are now
ALIGNED with AssessmentEvidence retaining the OVERTAKEN token verbatim, and the
R5 matrix-annotation repair note stays in RemainingWork. All live-fact findings
(scanner implementation, tests, hashes) were confirmed and are unchanged.

## Headline finding

The INSP-03 assessment (2026-06-21, reviewed SHA `210b5b7427`) rated this
deliverable one of "the least complete PKG-07 deliverables," with REQ-002/006/009
FAIL, REQ-003/007 TBD, and REQ-001/004/005/010 PARTIAL — but its own top-of-file
**ADQ-07 Superseding Note** (Assessment lines 15-24) records that the ADQ-07
scanner (`scanDeliverableDocumentKitContract` in
`frontend/src/lib/workspace/filesystem.ts`, commit `73ccf07d5`) subsequently
implemented the G2 gap. The live scanner + two test files
(`workspace-deliverable-contract-scanner.test.ts`,
`deliverables-route.test.ts`) satisfy REQ-001 through REQ-009; REQ-010's additive
`/api/project/deliverables` integration exists and is fixture-locked. The
conformance matrix cells were never rewritten, so the per-requirement FAIL/PARTIAL/TBD
conclusions are comprehensively overtaken → 8 ALIGNED rows carrying
AssessmentEvidence=OVERTAKEN (disposition per the fan-in revision note above),
with the R5 matrix-annotation repair recorded in RemainingWork.

## REQUIREMENT_INDEX parser gap (R1)

`R1_INVENTORY/REQUIREMENT_INDEX.csv` lists both the real IDs
`DEL-07-03-REQ-001..010` (lines 386-395) AND bare `REQ-001..010` (lines 396-405).
The bare IDs are a duplicate scan of the generic requirement labels, not distinct
claims. I re-derived the claim set from `Specification.md` Requirements table
(lines 26-35): exactly ten requirements, REQ-001..REQ-010. No parser under-count
here (the known zero-scan gap did not apply); the over-count of bare IDs is noted
but carries no separate claims.

## Least-confident rows (mandatory self-flag — alternative reading that flips them)

1. **REQ-001,002,003,004,005,006,007,009 (STALE_ASSESSMENT, the whole class).**
   The single load-bearing judgment: does the assessment's own ADQ-07 Superseding
   Note (Assessment lines 15-24) already neutralize the staleness, making these
   ALIGNED with `AssessmentEvidence = OVERTAKEN` instead of STALE_ASSESSMENT?
   [RESOLVED at fan-in: the alternative reading below prevailed; rows are now
   ALIGNED per the fan-in revision note above. Original reasoning preserved for
   the record.]
   - My original call: STALE_ASSESSMENT. The header note is a pointer; the Requirements
     Conformance Matrix cells (Assessment lines 34-43) and Gap Inventory G2
     (lines 49-52) still literally read FAIL/PARTIAL/TBD as current conclusions,
     the live surfaces (requirement text + implementation + tests) agree, and
     §7 defines STALE_ASSESSMENT as exactly "an assessment conclusion overtaken by
     later implementation or tests." MR-1's reserve condition ("live surfaces agree
     AND some surface still presents the stale conclusion as current truth") is met
     by the un-rewritten matrix cells. This follows the R0 DEL-02-01 exemplar
     precedent (REQ-001/REQ-011 STALE_ASSESSMENT for an overtaken INSP conclusion
     still readable as current).
   - Alternative that flips them: read the superseding note as sufficient
     annotation, so the matrix is no longer "presented as current truth" → all
     eight become ALIGNED, `AssessmentEvidence = OVERTAKEN`, with the matrix-annotation
     work moved into RemainingWork only. The whole class stands or falls together;
     the fan-in verifier should adjudicate the class, not row by row.

2. **REQ-010 (STALE_SPECIFICATION vs STALE_ASSESSMENT).** Two stale surfaces
   collide: the INSP-03 PARTIAL rating (assessment-stale) AND the Specification.md
   Requirements-table entry itself, which is prefixed "ASSUMPTION:" and carries
   "Integration test TBD after implementation location is selected" (line 35) plus
   a Verification-row "Integration test TBD" (line 79) — both now false. I applied
   the MR-8 tie-break (kit text flatly asserting a now-false state →
   STALE_SPECIFICATION) because the false assertion is in the requirement's own
   spec cell, not only in the assessment. Alternative: treat it like the other
   eight (STALE_ASSESSMENT) and fold the spec-text repair into RemainingWork.

3. **REQ-008 (ALIGNED, MEDIUM).** Rated ALIGNED because INSP-03 rated it PASS
   (still current) and the scanner is read-only by construction — grep for
   `writeFile/mkdir/rm/unlink/appendFile` in `filesystem.ts` returns nothing, so
   instruction-root mutation is structurally impossible, and `normalizeProjectRoot`
   (lines 256-279) bounds the root. Alternative that weakens it to
   PARTIALLY_IMPLEMENTED: the requirement's Verification column asks for explicit
   "Path containment tests; instruction-root protection fixtures," and no dedicated
   path-traversal/escape test exercises *this* scanner (only a missing-root 404
   test). I judged the no-write structural guarantee sufficient for ALIGNED and
   logged the additive-test option as non-blocking RemainingWork.

4. **ACC-001 (STALE_SPECIFICATION, HIGH).** The REF-006 hash posture. Confidence
   is high on the fact (live `_REFERENCES.md` REF-006 = MATCH; I recomputed
   `shasum -a 256 docs/PRD.md` = `ac35fba40...`, reproducing the recorded value),
   but the disposition choice between STALE_SPECIFICATION (kit still asserts
   HASH_MISMATCH) and ACCEPTED_DIVERGENCE was resolved against ACCEPTED_DIVERGENCE
   per the W3 rule: D-APP-35/D-APP-38 do not *defer/accept a bounded difference*,
   they *reconcile it to MATCH*, so the residual kit wording is repair-shaped
   (STALE_SPECIFICATION), matching the R0 exemplar ACC-001 treatment.

## Register-defect summary

- **REGISTER-1 (REMAINING_STATE_MISMATCH).** `Dependencies.csv` DEP-07-03-005
  (the docs/PRD.md prerequisite) still carries `Confidence=MEDIUM` and a Notes
  "source warning: ... REF-006 HASH_MISMATCH," and `_DEPENDENCIES.md` Run Notes
  line 57 records "[WARNING] SOURCE_HASH_MISMATCH ... REF-006 as HASH_MISMATCH."
  Both are stale metadata lag versus live `_REFERENCES.md` REF-006 = MATCH
  (verified hash). Repair is doc/metadata-scoped; full register re-extraction is
  DEL-07-05-owned but is not required to correct the note text.
- **No other register defects.** The Extracted Register metrics in
  `_DEPENDENCIES.md` (ACTIVE 10 / ANCHOR 2 / EXECUTION 8 / UPSTREAM 10 /
  DOWNSTREAM 0) reconcile exactly with the ten `Dependencies.csv` rows
  (DEP-001/002 ANCHOR; DEP-003..010 EXECUTION; all Direction UPSTREAM). The
  `Declared Upstream`/`Declared Downstream` "TBD" sections are **not** flagged:
  per the W3 rule (docs/SPEC.md §5.2), Declared sections are human-owned and
  TBD-by-design, distinct from the agent-owned Extracted register.

## Method / scope observations

- No decision governs DEL-07-03 or PKG-07 in `R1_INVENTORY/DECISION_INDEX.csv`
  (empty on both keys) → `LatestDecision = NONE_FOUND` on all REQ/EXC rows.
  D-APP-35/D-APP-38 govern only the REF-006 hash row (ACC-001) and appear as
  context on REGISTER-1. D-APP-54 (lifecycle rebaseline) and D-APP-55 (activation)
  are corpus/lifecycle context; D-APP-55 governs REMAINING-1's gate flip.
- Scanner findings are exposed only through `/api/project/deliverables` (an
  adjacent project API), not `/api/working-root/scope`; `scanProjectScopes` and
  the `knowledgeTypes` buckets are sibling scope (shell/knowledge-type deliverables)
  and were not claimed here. No material live behavior on this deliverable's scanner
  surface lacks a requirement mapping, so **no IMPLEMENTED_UNMAPPED rows** were
  emitted (every finding category maps to REQ-001..009).
- No PKG-08 / FROZEN_PROCESS_INPUT surface bears on this deliverable; no
  DEFERRED_AGENT_WORKFLOW or AUTHORITY_CONFLICT rows arose.
- "No test exists" was asserted only after a real search: I grepped the frontend
  test tree for the scanner symbol and for containment/root tests. The
  similarly-named `src/__tests__/api/working-root/deliverable-contracts.test.ts`
  is **not** related to this scanner — it exercises DEL-05-03 status/transition/
  dependencies routes.

## No method deviations; no blockers.
