# R0 Calibration Report — Deliverable–Implementation Concordance Run

- **Run:** `RUN_D55_CONCORDANCE_2026-07-11_1904Z` (D-APP-55, Option A — whole corpus)
- **Phase:** R0 method calibration (pinned plan §8/R0)
- **Source state:** `main` = `4c8ed8907`; pinned method
  `plans/PLAN_2026-07-10_deliverable_implementation_reconciliation.md` @ `551f84ef6`
  (verified byte-identical to the live tree at dispatch)
- **Date:** 2026-07-11
- **Assembled by:** app-dev work loop orchestrator, fan-in over three parallel
  `fable` TASK agents (one per sample deliverable, disjoint write scopes per
  `RUN_BASIS.md` roster)

> **Epistemic status: immutable, source-state-bound evidence artifact.** Not
> authority, not a queue. No disposition here is a human ruling. The proposed
> method revisions in §4 are agent recommendations awaiting the owner's R0
> review; R2 scaling does not proceed until the owner rules on this report
> (D-APP-55 ruling, owner direction of record).

## 1. What ran

Full §§6–7 method on the three-deliverable calibration sample recorded in
`RUN_BASIS.md`: `DEL-02-01` (UI claim class / stale-assessment risk),
`DEL-03-04` (behavioral runtime claim class / D-APP-40 decision mapping),
`DEL-10-01` (doc-only acceptance / layered-gate derivation / F-APP-3
discipline). Read-only discovery; each agent wrote exactly its
`<DEL-ID>_claims.csv` + `<DEL-ID>_notes.md` in this folder. Merged ledger:
`R0_CLAIM_LEDGER.csv` (77 rows). All three CSVs validate deterministically
against the §6 contract: 19 columns, controlled §7 dispositions only,
DeliverableID scoping correct (csv.reader pass recorded by the orchestrator).

## 2. Claim census (77 rows)

| | DEL-02-01 | DEL-03-04 | DEL-10-01 | Total |
|---|---:|---:|---:|---:|
| Rows | 21 | 28 | 28 | 77 |
| ALIGNED | 9 | 24 | 22 | 55 |
| STALE_SPECIFICATION | 5 | 1 | 3 | 9 |
| IMPLEMENTED_UNDOCUMENTED | 3 | 2 | 2 | 7 |
| STALE_ASSESSMENT | 2 | 0 | 0 | 2 |
| STALE_VERIFICATION | 1 | 0 | 0 | 1 |
| IMPLEMENTED_DIFFERENTLY | 1 | 0 | 0 | 1 |
| PARTIALLY_IMPLEMENTED | 0 | 1 | 0 | 1 |
| ACCEPTED_DIVERGENCE | 0 | 0 | 1 | 1 |
| AUTHORITY_CONFLICT / UNKNOWN / DEFERRED_AGENT_WORKFLOW | 0 | 0 | 0 | 0 |

ClaimTypes: REQUIREMENT 38, ACCEPTANCE 14, EXCLUSION 12, IMPLEMENTED_UNMAPPED 8,
REMAINING_WORK 5.

## 3. Calibration verdicts against the plan §8/R0 criteria

1. **Authority precedence — PASS.** Zero `AUTHORITY_CONFLICT` rows across all
   three claim classes; the run-local `AUTHORITY_MAP.md` sufficed everywhere.
   Precedence note 1 ("a ruled decision may amend/interpret") is the
   load-bearing line — it prevented spurious conflicts on both the DEL-02-01
   corpus-vs-pivot tension and the DEL-10-01 SPEC-§18-vs-ruled-tools tension —
   keep it verbatim for R2. One strengthening identified (§4 MR-11).
2. **Evidence granularity — line ranges are the norm, and cheap.** File-level
   was insufficient for behavioral rows (shared files span deliverables;
   findings often hinge on what a test does NOT assert; taxonomy claims are
   branch-level). Doc-heavy rows achieved hash-level binding (sha256
   recompute, pin-diff-empty). One convention gap for doc-only
   `ImplementationEvidence` (§4 MR-10).
3. **False-positive rate — low and self-surfaced.** Each agent named its
   least-confident rows and the alternative reading that would flip them
   (DEL-02-01: REQ-004..006 ALIGNED-vs-STALE_VERIFICATION, UNMAPPED-3/4;
   DEL-03-04: UNMAPPED-1, REQ-014; DEL-10-01: ACC-001/EXC-001 scope-vs-posture
   reading, ACC-002, UNMAPPED-2). These are flagged in the notes for reviewer
   spot-check per plan §10; none is load-bearing for the method verdict.
4. **Scope vs current behavior — held.** All three agents kept
   ruled-but-unmapped behavior out of requirement rows via
   `IMPLEMENTED_UNMAPPED`, resisting silent scope adoption (plan §3 boundary 1)
   at the hardest spots (DEL-02-01 `/chat` surface; DEL-03-04 additive event
   vocabulary and stub adapter; DEL-10-01 future-boundary exclusions).
5. **RemainingWork usefulness — executable.** Doc repairs and small tests are
   `## Remaining`-ready near-verbatim; corpus amendments and ownership/mapping
   questions correctly resolve to R4 packet inputs rather than deliverable
   items (plan §3 boundary 9 respected).

Sample-specific calibration questions, answered:

- **DEL-02-01 (pilot observation):** CONFIRMED from the live tree — INSP-03
  (2026-06-20 @ `50b063f3e`) reports the loop-first pivot as spec drift while
  the current spec (ADQ-13 rewrite), implementation, and tests agree at
  `4c8ed8907`. Refinement: the pre-pivot wording residue now lives one level
  UP, in the RATIFIED PRD/TYPES text (see §5 finding 1).
- **DEL-03-04 (LatestDecision mapping):** clean — D-APP-40 bound directly on 1
  row and interpretively on 6 more, with the ruling's boundary respected;
  refinement MR-7.
- **DEL-10-01 (gate derivation):** §6 columns sufficient for layered gates
  (verbatim-concatenated suffixes; NO-if-any-gate-unsatisfied); gate vs
  stage-gate expressible via `HumanDecisionNeeded`; F-APP-3 never blocked
  evidence — cross-project gate status derived entirely from app-dev's own
  pinned surfaces; D-APP-37 doc-only basis worked as per-row verification
  basis (reuse pattern for the rest of PKG-10 in R2).

## 4. Proposed run-local method revisions (for owner review before R2)

Consolidated and deduplicated from the three notes files (§§3–4 of each);
sources cited. None touches agent instruction files or workflow contracts
(plan §3 boundary 8). Per plan §8/R0 these revise the RUN-LOCAL method only;
the pinned plan itself is not edited.

| # | Revision | Source notes |
|---|---|---|
| MR-1 | `Disposition` records live concordance; assessment recency lives exclusively in `AssessmentEvidence`, which MUST carry a machine-scannable verdict token (`OVERTAKEN` / `STILL CURRENT` / `NOT APPLICABLE`); reserve `STALE_ASSESSMENT` as Disposition for rows where the overtaken conclusion is the operative defect | all three (converged independently) |
| MR-2 | `SelectableUnderCurrentLoop` derived only for `REMAINING_WORK` rows; `NO`-by-definition otherwise (a `YES` on a non-REMAINING row is machine-detectable as an error) | all three |
| MR-3 | Bless the "recorded-pass + byte-identity" indirect verification binding (newest recorded full-suite pass @ SHA X + `git diff X..<source state> -- frontend/` empty), both elements named per row; R1 precomputes the newest recorded-pass SHA once for all R2 agents; preferably the orchestrator runs frontend gates once per wave in a disposable environment and publishes the transcript in the run folder for citation | DEL-02-01 §3.2, DEL-03-04 §3.3–3.4 |
| MR-4 | Fold Datasheet restatements into REQ rows; emit ACCEPTANCE rows only for datasheet-distinct conditions, and let ACC rows cite covering REQ evidence | DEL-02-01 §3.3, DEL-03-04 §3.5 |
| MR-5 | Give register defects a ledger home: one run-local `REGISTER-<n>` row type (or a standardized notes-section contract) for dependency/reference register defects so R3 receives them in the ledger, not prose | DEL-02-01 §3.4, DEL-03-04 §3.6 |
| MR-6 | `RemainingGate` = concatenated verbatim suffixes; `SelectableUnderCurrentLoop` = NO if ANY gate unsatisfied; cross-project gate status derived ONLY from the consuming project's own pinned surfaces, else `UNKNOWN` (F-APP-3-safe rule) | DEL-10-01 §5 |
| MR-7 | `LatestDecision` controlled suffix distinguishing "governs" from "context" (e.g. `D-APP-40` vs `D-APP-40 (context)`) for machine filterability | DEL-03-04 §4 |
| MR-8 | STALE_SPECIFICATION vs ACCEPTED_DIVERGENCE tie-break: flatly-false text → STALE_SPECIFICATION (repair-shaped); gate-acknowledging text + permitting ruling → ACCEPTED_DIVERGENCE (no repair implied) | DEL-10-01 §4.3 |
| MR-9 | Where a spec was rewritten after its assessment, `AssessmentEvidence` must cite `old-REQnnn` and state the old-ID→claim mapping (or "no direct conclusion") | DEL-10-01 §4.4 |
| MR-10 | Enumerated verification-basis vocabulary for doc-only claims — `DOC-BASIS(D-APP-nn)`, `RUN-INSPECTION@<sha>`, `RULING-RECORD(D-APP-nn)`, `SNAPSHOT+LIVE-REVERIFY(<snapshot>)` — plus the "documentary claim + exact doc sections" convention for `ImplementationEvidence` on doc-only rows | DEL-10-01 §4.5, §3(b) |
| MR-11 | AUTHORITY_MAP strengthening: state explicitly how a later corpus re-ratification interacts with an earlier ruled pivot whose text has not yet been transcribed into the corpus (the v6 mint was lifecycle-scoped; ruled pivots stand) | DEL-02-01 §2(a) |

## 5. Findings requiring owner attention (R0 evidence; no action taken)

1. **Stale wording has moved up into the RATIFIED corpus** (DEL-02-01
   REQ-002/007/008, UNMAPPED-1): PRD (L473 FR-001, L312 §7.2, L485 FR-008) and
   TYPES §4.1/§4.3/§3.4 still encode pre-pivot WORKBENCH/header-nav routing and
   the old matrix cell-persona roster, superseded by ruled
   D-APP-28/30/31/32 (+ D-APP-24 partially). Repair is an owner-gated corpus
   amendment packet (with D-APP-38 reconciliation), NOT a deliverable repair.
2. **INSP-03 assessments are comprehensively stale in 2 of 3 samples**
   (DEL-02-01: pivot-as-drift; DEL-10-01: all four gap conclusions overtaken;
   DEL-03-04: 2 of 3 gaps closed by ORN-09, pointers drifted on 3 more rows).
   Expect R2 to find this corpus-wide; the AssessmentEvidence column (per MR-1)
   carries it without flipping dispositions.
3. **Register-surface defects found live** (R5-shaped, R4-gated): DEL-03-04
   `_DEPENDENCIES.md` digest contradicts `Dependencies.csv` (DEP-03-04-008
   RETIRED since 2026-05-24, digest still ACTIVE 10/RETIRED 0, wrong tally);
   DEL-02-01 `DEP-02-01-005` workspace still `TargetType=UNKNOWN`/TBD though
   ADQ-13 named the frontend paths in 2026-06-21.
4. **Verification thin spots at the D-APP-36 bar** (DEL-02-01): no test asserts
   header active state (REQ-003) or the 3x4 matrix shape/labels (REQ-004..006);
   one small render test closes all four. DEL-03-04 REQ-006: stub-adapter
   terminal outcomes are UI-only while the event log is available in stub mode
   (NEW-PACKET: persistence parity vs documented exclusion).
5. **Unmapped implementation surfaces** (8 rows total) collapse to ~3 R4
   category-4 ownership/mapping questions: the `/chat` surface + portal
   launchers (DEL-02-01), additive harness-event vocabulary + interrupt-time
   permission-broker clearing (DEL-03-04), domain MCP tool surface possibly
   owned by DEL-10-04/05 (DEL-10-01).

## 6. Method verdict and R2 readiness

The pinned §§6–7 method is **workable at scale as-is**; every friction point
was expressible inside the existing contract, and the proposed revisions are
clarifications and efficiency rules, not structural changes. The three claim
classes (UI, behavioral runtime, doc-only/gated) all produced clean ledgers
with zero conflicts and zero unknowns. R2 wave scaling is ready pending:

1. owner review of this report (D-APP-55 ruling: R0 findings go to the owner
   before R2 scaling — this is the gate);
2. owner disposition on the §4 method revisions (adopt some/all as the
   run-local method for R1/R2);
3. environment decision per MR-3 (per-wave gate transcript vs per-agent
   indirect binding).

Session incidents (transparency, no evidence impact): the DEL-03-04 agent was
interrupted once mid-run by a provider API error after its CSV validated and
was resumed to complete its notes file; the same agent created and removed a
transient `node_modules/.vite` cache during a failed test-execution attempt,
restoring pristine state (its verification rows use the MR-3 indirect binding
instead). Neither incident touched any source or evidence file.
