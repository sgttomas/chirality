# R0 Calibration Notes — DEL-02-01 Desktop Shell and Matrix Navigation

- **Run:** `RUN_D55_CONCORDANCE_2026-07-11_1904Z` (D-APP-55, Option A)
- **Deliverable:** DEL-02-01, PKG-02 Desktop Shell, Navigation, and Operator State
- **Source state:** `main` = `4c8ed8907` (verified live: `git rev-parse HEAD` in the run worktree)
- **Agent role:** TASK (Type-2 bounded executor), phase R0 method calibration
- **Date:** 2026-07-11
- **Method:** pinned plan `plans/PLAN_2026-07-10_deliverable_implementation_reconciliation.md` @ `551f84ef6` §§5–8; shared kernel `docs/DELIVERABLE_CONCORDANCE_METHOD.md` (RATIFIED); run-local `AUTHORITY_MAP.md`

> **Epistemic status: evidence artifact, not authority.** Nothing here is a
> ruling, a lifecycle action, or a work-selection surface. Dispositions are
> agent classifications for human review; every human-owned decision is
> flagged, not made.

## 1. Claim census

21 claim rows in `DEL-02-01_claims.csv`.

By ClaimType:

| ClaimType | Count |
|---|---:|
| REQUIREMENT | 11 |
| EXCLUSION | 4 |
| IMPLEMENTED_UNMAPPED | 4 |
| ACCEPTANCE | 1 |
| REMAINING_WORK | 1 |

By Disposition:

| Disposition | Count | Rows |
|---|---:|---|
| ALIGNED | 9 | REQ-004/005/006/009/010, EXC-001/002/003, REMAINING-1 |
| STALE_SPECIFICATION | 5 | REQ-002/007/008 (PRD/TYPES pre-pivot routing text), EXC-004 (dependency-deferral wording), ACC-001 (hash-mismatch condition) |
| IMPLEMENTED_UNDOCUMENTED | 3 | UNMAPPED-2 (/chat), UNMAPPED-3 (deliverable-rows launcher), UNMAPPED-4 (portal persona picker) |
| STALE_ASSESSMENT | 2 | REQ-001, REQ-011 |
| STALE_VERIFICATION | 1 | REQ-003 (header active-state has no covering test) |
| IMPLEMENTED_DIFFERENTLY | 1 | UNMAPPED-1 (matrix cell personas vs TYPES §4.3/§3.4) |

Derived summary (not a deliverable verdict): the deliverable's own
four-document kit is current and matches implementation and tests for every
behavioral requirement; the discordant surfaces are (a) the 2026-06-20
INSP-03 assessment, (b) pre-pivot wording still standing in the RATIFIED
authority corpus (PRD §7.2/§8.1 FR-001/§8.2 FR-008; TYPES §4.1/§4.3/§3.4),
and (c) three run-scoped kit statements (dependency deferral, PRD hash
warning) overtaken by later ruled work.

Dependency re-verification (plan §5): all 8 `Dependencies.csv` rows re-read
live and consistent with the D53A provenance baseline (`coverage.csv` row
`DEL-02-01,Y,8,Y,Y`). DEL-02-01 was not in the D53A ten-deliverable
reconciliation scope, so its 4 EXECUTION rows still carry
`SatisfactionStatus=TBD`. One currency finding not expressible as a claim row
under the §6 row-generation rule: `DEP-02-01-005` still records the
implementation workspace as `TargetType=UNKNOWN`/`TBD`, while Procedure.md's
ADQ-13 evidence slots have named the exact `frontend/` paths since
2026-06-21 — register metadata lags implementation (REMAINING_STATE_MISMATCH
in character; recorded here because dependency rows are not claims under §6).

Lifecycle note: `_STATUS.md` header still carries `Checking Approval SHA` and
the D-APP-19 authorization basis above an `IN_PROGRESS` state. Under D-APP-54
and AUTHORITY_MAP precedence note 2 these are preserved historical evidence,
so no LIFECYCLE_REASSESSMENT_REQUIRED row was raised; flagged for the R3
synthesizer in case corpus-wide header shape deserves one packet.

## 2. R0 calibration self-report (plan §8/R0 criteria)

**(a) Authority precedence.** The AUTHORITY_MAP sufficed for every row; no
AUTHORITY_CONFLICT was needed. The one hard derivation: live RATIFIED
PRD/TYPES text (WORKBENCH-destination, header-nav-to-three-routes) versus the
ruled D-APP-28/30/31/32 loop-first pivot. Resolved via precedence note 1 ("a
ruled decision may amend/interpret") plus the D-APP-28 ruling's explicit
supersession language, plus the fact (Receipt 10) that the v6 corpus mint was
scoped to lifecycle semantics and did not re-adjudicate navigation. Verdict:
derivable, but only because the ruling text was explicit — a weaker ruling
would have forced AUTHORITY_CONFLICT. The map would be stronger if it stated
how a later corpus re-ratification interacts with an earlier ruled pivot
whose text has not yet been transcribed into the corpus.

**(b) Evidence granularity.** File-level was not enough for the load-bearing
rows; line ranges were needed wherever the finding hinges on what a test does
NOT assert (REQ-003, REQ-004..006) and on single data structures
(`NAVIGATION_ITEMS` at shell-frame.tsx:16-20; `MATRIX_ROWS` at
agent-matrix-cells.ts:42-136). Line ranges were cheap to capture and should
stay the norm for behavioral rows. Verification binding required a chain, not
a file: no `node_modules` exists in the run worktree, and installing one to
re-execute Vitest would have mutated the read-only tree, so test evidence was
bound as: named test files at `4c8ed8907` + `git diff d2f1cb7ff..4c8ed8907 --
frontend/` empty (frontend byte-identical since its last commit) + recorded
full-suite pass (Vitest 667 passed/4 skipped, typecheck pass) in
`loop/LOOP_RECEIPTS.md` Receipts 3–4. That chain is honest but weaker than a
fresh run; see §4 friction item 2.

**(c) False-positive risk.** Least confident rows, in order: (1)
REQ-004/005/006 marked ALIGNED — implementation is verified by static data +
type-union enforcement + a render execution, but no named assertion checks
the 3x4 shape or visible labels; a stricter reader would mark these
STALE_VERIFICATION, and I chose ALIGNED-with-MEDIUM-confidence to avoid
manufacturing three findings whose repair is one small test. (2) UNMAPPED-3/4
— the deliverable-rows launcher and persona picker may be deliberate
convenience UI already understood as inside "route query handling"; marking
them IMPLEMENTED_UNDOCUMENTED could over-report. (3) REQ-003
STALE_VERIFICATION assumes the spec's promised "UI assertion" never existed;
I did not archaeology the 50b063f3e tree to confirm it never passed there.

**(d) Scope vs current behavior.** Hardest to keep at three places: the
`/chat` surface (current behavior, ruled by D-APP-24/27, but no deliverable
scope anywhere I could find — recording it as this deliverable's UNMAPPED row
risks implying DEL-02-01 ownership, which is exactly the mapping decision a
human must make); the matrix cell personas (behavior tested and deliberate,
TYPES text contrary — kept as IMPLEMENTED_DIFFERENTLY rather than letting the
tests' existence read as scope); and the OPERATIVE deliverable-rows launcher
(REQ-011 documents its keys as evidence, which tempts silent scope adoption —
resisted per plan boundary 1).

**(e) Usefulness of RemainingWork statements.** Mostly executable as
`## Remaining` items: the R5 doc repairs (EXC-004, ACC-001, the two
STALE_ASSESSMENT annotations) and the three small tests (REQ-003, REQ-004..006
consolidated) each name file, change, and acceptance shape. The corpus
amendments (REQ-002/007/008, UNMAPPED-1) are NOT deliverable-executable —
they are owner-gated authority-doc edits requiring a decision packet plus
D-APP-38 version bump — and are phrased as packet inputs, not work items.
The ownership/mapping rows (UNMAPPED-2/3/4) resolve to one consolidated R4
category-4 packet, not three items.

## 3. Method friction and proposed run-local method revisions

1. **One-disposition-per-row loses a real dual finding (plan §7).**
   REQ-002/007/008 are simultaneously stale-corpus-text and stale-assessment;
   the Disposition carries the repair-dominant value and the stale-assessment
   fact survives only in `AssessmentEvidence`. Proposed run-local revision:
   R2 instruction that when STALE_SPECIFICATION and STALE_ASSESSMENT co-occur,
   Disposition carries the live-authority finding and `AssessmentEvidence`
   MUST begin with `OVERTAKEN`/`STILL CURRENT`/`NOT APPLICABLE` as a
   machine-scannable prefix (adopted in this CSV) so R3 can still count stale
   assessments per claim.
2. **Verification binding without executing tests (plan §6 evidence bar).**
   The read-only discipline plus a dependency-less worktree means R2 agents
   cannot re-run Vitest without mutating the tree. Proposed run-local
   revision: the orchestrator runs the frontend gates once per wave at the
   pinned SHA in a disposable environment and publishes the transcript in the
   run folder; R2 rows then cite that transcript instead of each agent
   re-deriving the Receipt-3/4 + unchanged-tree chain.
3. **Datasheet acceptance duplication (plan §6 row-generation).** Datasheet
   attributes restate Specification requirements 1:1; generating rows for
   both would double-count. Adopted rule (propose making it explicit for R2):
   fold restatements into the REQ row and emit ACCEPTANCE rows only for
   datasheet-distinct conditions (here: ACC-001).
4. **Dependency-register currency has no claim slot (plan §6).** The
   `DEP-02-01-005` staleness had to live in prose (§1). Proposed run-local
   revision: allow an optional `DEPENDENCY` ClaimType (or a per-deliverable
   dependency-currency note field in the notes contract) so R3 can aggregate
   register-lag findings.
5. **`SelectableUnderCurrentLoop` is ill-defined for non-work rows.** For
   REQUIREMENT/EXCLUSION rows with `RecordedRemaining=NONE_RECORDED` the
   column can only mean "no recorded item exists to select" (recorded as NO).
   Propose R2 guidance fixing that reading so NO is not misread as "blocked."
6. **DEFERRED_AGENT_WORKFLOW boundary check.** Nothing in this deliverable
   required judging agent instruction files; the matrix cell-roster question
   (UNMAPPED-1) is product UI + TYPES vocabulary, not an agent-workflow
   contract, so it was NOT routed as DEFERRED_AGENT_WORKFLOW. One adjacent
   observation for `AGENT_WORKFLOW_OBSERVATIONS.md` if the owner wants it:
   the matrix guard test binds UI cells to the on-disk `agents/AGENT_*.md`
   roster (agent-matrix-cells.test.ts lines 42-71), so any future
   agent-roster change silently changes product test truth — recorded here as
   an observation only, no recommendation (plan §3 boundary 8).

No agent-workflow changes are proposed anywhere in this packet.

## 4. Pilot-observation verdict

**CONFIRMED.** The pilot observation (plan §2, RUN_BASIS sample table) that
DEL-02-01 carries stale-assessment risk — the inspection assessment reporting
the loop-first pivot as specification drift while current spec and
implementation are aligned — is re-derived as true from the live tree at
`4c8ed8907`:

- `Assessment_INSP-03_DEL-02-01.md` (2026-06-20, reviewed SHA `50b063f3e`)
  line 24 calls the header change "spec drift from the older baseline
  wording"; line 39 (Gap 1) says "Header-navigation requirements are stale
  after the loop-first pivot"; line 40 (Gap 2) says spec destination language
  "still says WORKBENCH"; lines 23/29/30/33 rate REQ-001/007/008/011 PARTIAL
  against pre-pivot wording.
- The current `Specification.md` (rewritten by ADQ-13 on 2026-06-21, per
  `MEMORY.md` and `Evidence_ADQ-13_UI_Specs_Render_Tests.md`) is loop-first
  throughout (Scope lines 9–11; REQ-001/002/007/008 wording), and the
  implementation at `4c8ed8907` matches it
  (`frontend/src/components/shell/shell-frame.tsx:16-20`;
  `frontend/src/lib/portal/agent-matrix-cells.ts:1-14`), with render/routing
  tests in place.
- Therefore INSP-03's drift findings and its PARTIAL ratings for
  REQ-001/002/007/008/011, plus Gaps 1–4 (Gap 3 AMD-01 resolved by D-APP-36;
  Gap 4 hash mismatch resolved by D-APP-35/38), are overtaken. The assessment
  is classified stale per claim in the CSV (`STALE_ASSESSMENT` rows REQ-001
  and REQ-011; `OVERTAKEN` prefixes on REQ-002/007/008; `STILL CURRENT` where
  it holds: REQ-004/005/006/009/010 and, partially, REQ-003).

One refinement the pilot wording misses: the pivot's wording residue is no
longer in the deliverable spec at all — it now lives one level up, in the
RATIFIED PRD/TYPES text (claims REQ-002/007/008, UNMAPPED-1), which is an
owner-gated corpus amendment, not a deliverable repair.
