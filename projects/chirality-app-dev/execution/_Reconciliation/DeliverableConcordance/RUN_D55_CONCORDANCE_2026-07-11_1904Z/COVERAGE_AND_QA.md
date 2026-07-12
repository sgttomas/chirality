# COVERAGE_AND_QA — R3 coverage report and plan §10 QA assessment

- **Run:** `RUN_D55_CONCORDANCE_2026-07-11_1904Z` (D-APP-55, Option A whole corpus).
- **Phase:** plan §8/R3 coverage mandate + plan §10 acceptance-criteria assessment,
  pinned plan revision `551f84ef6` (re-verified byte-identical in this worktree at
  authoring time) as amended run-locally by `R2_METHOD_ADDENDUM.md` (MR-1..MR-11).
- **Author:** R3 synthesis agent R3-C (Claude Fable 5), 2026-07-12. Read-only
  everywhere except this file and `RUN_SUMMARY.md`.
- **Source-state bind:** worktree HEAD `60db8de85`;
  `git diff --quiet fac46e33f..HEAD -- projects/chirality-app-dev/frontend/` exit 0 —
  frontend byte-identical to the run's verification anchor
  `GATE-TRANSCRIPT(W1@fac46e33f)` (typecheck exit 0; Vitest 667 passed / 4 skipped).
  No STALE_INPUT condition at authoring time.

> **Epistemic status: immutable, source-state-bound evidence artifact; agent
> judgment throughout, never a human ruling.** Not a queue, not a selection
> surface, not authority. No lifecycle transition is made or implied; no workflow
> recommendation is made. Vintage caveats recorded here are QA findings routed to
> the R4 gate; **no ledger row was recoded by this report.**

## 1. Method — deterministic verification scripts

Every quantitative statement below was produced by deterministic Python/csv
scripts over the immutable run artifacts (no model judgment in any count), so the
report is reproducible by re-running the same checks against the same files. The
checks (IDs used throughout):

| Check | What it does | Result |
|---|---|---|
| C1 | Ledger shape: row/column/deliverable/package counts; disposition + ClaimType censuses | 1,115 rows x 19 cols; 53 deliverables; 11 packages — see §2.1 |
| C2 | Ledger deliverable set == `R1_INVENTORY/DELIVERABLE_INVENTORY.csv` set | EQUAL, 53/53 |
| C3 | Every `REQUIREMENT_INDEX.csv` ID maps to ≥1 ledger row (direct + suffix matching); parser-gap enumeration | 616/616 mapped; 0 unmatched; gap detail §2.2 |
| C4 | `IMPLEMENTATION_SURFACES.csv` (155 files) diffed against every cell of every ledger row, all wave notes/`_VERIFICATION.md`, and all R3 artifacts (exact path, then path-segment/basename fallback) | 123 exact-cited; 10 coarser-granularity; 22-file residue — §2.3, finding CQ-F1 |
| C5 | `UNMAPPED_IMPLEMENTATION.csv` keyset vs ledger `IMPLEMENTED_UNMAPPED` rows | EQUAL, 36 = 36, zero divergence either way |
| C6 | All 62 `CONFLICTS_AND_UNKNOWNS.csv` rows: non-empty Owner + SmallestNextAction; packet references resolve; non-packet rows have explicit rationale | PASS — §2.4 |
| C7 | All 161 `PROPOSED_DELIVERABLE_UPDATES.csv` rows: `GatedBy` names a defined R4 packet; every `AffectedClaims` (DeliverableID, ClaimID) pair resolves to a real ledger row | 161/161 gated; 0 unresolvable pairs |
| C8 | MR-2 (Selectable YES only on REMAINING_WORK); MR-1 token scan; DEFERRED_AGENT_WORKFLOW full-cell scan; NormativeSource emptiness/NONE_FOUND discipline | PASS with the known 29-row vintage token gap — §2.2/§3 |
| C9 | PKG-03 F-1 erratum census recomputed from the ledger | Erratum numbers CONFIRMED — §3(b) |
| C10 | DEL-02-01 R0-vintage enumeration (the DEL-03-04-equivalent check) | §3(a2) |
| C11 | Per-package disposition census recomputed and compared against every `PACKAGE_SUMMARIES/PKG-XX.md` census table (PKG-03 via its erratum table), including combined-row handling | ALL 11 summaries reproduce exactly |
| C12 | Wave/R0 row-count reconciliation: Σ(R2 wave ledgers) + retained R0 rows == merged ledger | 1,066 + 49 = 1,115 EQUAL; per-wave 86/423/223/113/89/105/27 |
| C13 | Confidence + HumanDecisionNeeded profile; duplicate (DeliverableID, ClaimID) scan; REMAINING_INVENTORY (69) vs ledger REMAINING_WORK rows (69) per-deliverable | HIGH 805 / MEDIUM 302 / LOW 8; HDN non-NO 66; zero duplicate keys; 69==69 per-deliverable EQUAL |

## 2. Plan §8/R3 coverage mandate

### 2.1 All deliverables — 53/53 (C1, C2)

`CLAIM_CONCORDANCE.csv`: 1,115 rows, 19 columns (§6 header), 53 distinct
deliverables across all 11 packages; the deliverable set is identical to the R1
inventory. Per-package rows: PKG-00 27, PKG-01 89, PKG-02 107, PKG-03 89, PKG-04
115, PKG-05 116, PKG-06 131, PKG-07 125, PKG-08 98, PKG-09 113, PKG-10 105.
Run-wide disposition census (final, script-derived):

| Disposition | Rows |
|---|---:|
| ALIGNED | 833 |
| STALE_SPECIFICATION | 94 |
| PARTIALLY_IMPLEMENTED | 64 |
| REMAINING_STATE_MISMATCH | 53 |
| IMPLEMENTED_UNDOCUMENTED | 28 |
| STALE_ASSESSMENT | 23 |
| IMPLEMENTED_DIFFERENTLY | 6 |
| DOCUMENTED_UNIMPLEMENTED | 5 |
| ACCEPTED_DIVERGENCE | 5 |
| STALE_VERIFICATION | 4 |
| AUTHORITY_CONFLICT / UNKNOWN / DEFERRED_AGENT_WORKFLOW | 0 |
| **Total** | **1,115** |

ClaimTypes: REQUIREMENT 700, EXCLUSION 178, ACCEPTANCE 79, REMAINING_WORK 69,
REGISTER_DEFECT 53 (MR-5 extension), IMPLEMENTED_UNMAPPED 36.

### 2.2 All requirements (C3) — including the known parser gap

Every one of the 616 `REQUIREMENT_INDEX.csv` IDs maps to at least one ledger row
for its deliverable (0 unmatched after direct + controlled suffix matching; the
suffix step is needed only where a wave used spec-native ClaimID styles, e.g.
DEL-04-04's index `REQ-001` vs ledger `PC-REQ-001`, DEL-01-03's `REQ-01` vs
`DEL-01-03-REQ-01` — style divergence already recorded as R3A-055, with the
full-ledger uniqueness check clean: zero duplicate (DeliverableID, ClaimID) pairs).

**The REQUIREMENT_INDEX parser gap, fully enumerated (larger than any single
receipt's passing mention):**

- **13 deliverables with ZERO indexed IDs:** DEL-00-01, DEL-00-02, DEL-01-02,
  DEL-02-05, DEL-04-03, DEL-04-05, DEL-05-01, DEL-05-02, DEL-05-03, DEL-07-05,
  DEL-08-01, DEL-08-04, DEL-09-02.
- **4 deliverables with a single truncated artifact ID** (`REQ-06`, `REQ-07`,
  `REQ-09`, `REQ-10` — regex fragments, not real requirement IDs): DEL-06-03,
  DEL-07-01, DEL-09-05, DEL-10-03.

Per-deliverable confirmation that no claim coverage was lost: each gap
deliverable's claim set was re-derived directly from its `Specification.md` by
the owning R0/R2 agent (R1_NOTES declared the index "a coverage checklist, not a
claim ledger"; the W2 dispatch brief named the then-known gap deliverables
explicitly — Receipt 20; W5/W7 verified the gap for DEL-01-02 and both PKG-00
deliverables — Receipts 30/32; R3A-058 records the class). Script confirmation:
every gap deliverable carries a full REQUIREMENT claim set in the merged ledger —
DEL-00-01: 8, DEL-00-02: 10, DEL-01-02: 25, DEL-02-05: 10, DEL-04-03: 14,
DEL-04-05: 17, DEL-05-01: 16, DEL-05-02: 15, DEL-05-03: 13, DEL-07-05: 18,
DEL-08-01: 14, DEL-08-04: 11, DEL-09-02: 16 (and the four truncated-ID
deliverables carry 15/12/14/12 REQUIREMENT rows respectively). The index artifact
is incomplete; requirement coverage is not.

**R1_NOTES sweep commitments (both §10-relevant, both discharged):**

1. *Decision-to-deliverable applicability* — judged per claim row at R2 (MR-7
   `LatestDecision`, zero empty cells run-wide), swept at R3:
   `PROPOSED_DECISION_FINDINGS.md` §7 verified all 66 non-NO
   `HumanDecisionNeeded` cells (63 NEW-PACKET + 3 pseudo-citations checked
   against `DECISION_INDEX.csv` and the live register) and placed each in
   exactly one packet; the index's one known thinness (D-APP-35 under-linking)
   is recorded as R3A-060.
2. *Unmapped-implementation sweep* — `IMPLEMENTATION_SURFACES.csv` diffed against
   all ledger evidence citations. Performed by this report (C4); result in §2.3.

### 2.3 All material implementation surfaces (C4, C5) — the R1-committed sweep

`UNMAPPED_IMPLEMENTATION.csv` reconciles exactly: its 36 rows are precisely the
ledger's 36 `IMPLEMENTED_UNMAPPED` rows (keyset equality both directions; zero
rows in either artifact absent from the other).

The 155-file surface index diffs against the merged ledger as follows:

- **123 files (79%)** are cited by exact path in at least one ledger evidence cell.
- **10 files** carry no exact-path citation but are covered at coarser, verifiable
  granularity or by an existing R3 item:
  `src/app/api/harness/session/[id]/route.ts` and `.../session/list/route.ts`
  (path segments cited by DEL-03-03-REQ-001's route-catalog claim; the
  uncataloged-routes question is R3A-017 / R4-P30);
  `src/app/api/working-root/scope/route.ts` (segment cited: DEL-02-03-REQ-007,
  DEL-07-03-REQ-010, DEL-08-03-REQ-010);
  `src/app/chat/page.tsx` (DEL-02-01 UNMAPPED-2, `/chat` surface → R4-P29);
  `src/app/pipeline/page.tsx` and `src/app/workbench/page.tsx`
  (DEL-02-01-REQ-002 route evidence);
  `src/app/not-found.tsx` (basename cited: DEL-06-04-REQ-005, DEL-09-03-REQ-006);
  `src/components/shell/loop-shell.tsx` (stem cited: DEL-02-01 REQ-001 /
  EXC-001 / UNMAPPED-4);
  `src/lib/dependencies/csv-utils.ts` (basename cited: DEL-07-05 REQ-018);
  `packages/harness-contract/src/index.ts` (12-LOC barrel of a package cited in
  151 rows).
- **22 files (≈14% of the index, ≈4,830 LOC) have NO citation at any
  granularity** — not in any ledger cell, any wave notes or `_VERIFICATION.md`,
  or any other R3 artifact — and are not listed in `UNMAPPED_IMPLEMENTATION.csv`.
  This is **finding CQ-F1** (§4) and the caveat on §10 bullet 5 (§3). The full
  residue, with affinity classification (agent judgment only — no scope is
  adopted and no mapping is asserted; the affinity says which existing R4
  packet family the file most plausibly rides with):

| # | Path (under `frontend/`) | LOC | Affinity (agent judgment) |
|---:|---|---:|---|
| 1 | `src/app/globals.css` | 2098 | PKG-02 shell styling (R0-vintage granularity; R4-P29 family) |
| 2 | `src/app/page.tsx` | 10 | PKG-02 root redirect wrapper (R4-P29 family) |
| 3 | `src/app/api/working-root/deliverable/content/route.ts` | 24 | working-root API family (siblings cited by DEL-02-03/DEL-07-03); route-catalog question R4-P30 |
| 4 | `src/components/shell/chat-markdown.tsx` | 74 | shell view component (DEL-02-01 family) |
| 5 | `src/components/shell/document-view.tsx` | 232 | shell view component (DEL-02-01 family) |
| 6 | `src/components/shell/file-picker.tsx` | 299 | shell view component (DEL-02-01 family) |
| 7 | `src/components/shell/session-list-view.tsx` | 233 | shell view component (DEL-02-01 family) |
| 8 | `src/components/shell/subagent-stream-view.tsx` | 65 | shell event-view (DEL-05-04's `transcript-stream-view.tsx` sibling is cited; this one is not) |
| 9 | `src/components/shell/tool-stream-view.tsx` | 72 | shell event-view (same family) |
| 10 | `src/components/workspace/harness-events-provider.tsx` | 111 | workspace event plumbing (DEL-02-01/PKG-02 family) |
| 11 | `src/lib/shell/ansi.ts` | 14 | shell helper |
| 12 | `src/lib/shell/document-view-state.ts` | 53 | shell helper |
| 13 | `src/lib/shell/harness-event-buffer.ts` | 19 | shell event plumbing |
| 14 | `src/lib/shell/harness-event-views.ts` | 324 | shell event plumbing |
| 15 | `src/lib/workspace/navigation-intent.ts` | 54 | workspace navigation helper |
| 16 | `src/types/chirality-window.d.ts` | 23 | Electron bridge typing (PKG-09 packaging family) |
| 17 | `electron/preload.ts` | 21 | Electron bridge (PKG-09 packaging family) |
| 18 | `src/lib/harness/scripted-agent-sdk-proof.ts` | 133 | D-APP-18 proof-harness affinity (PKG-03/PKG-09) |
| 19 | `scripts/assert-harness-contract-deps.mjs` | 82 | build/validation tooling (PKG-09 family) |
| 20 | `scripts/generate-tool-catalog.mjs` | 60 | catalog generator (its output `tool-catalog` data is cited in 10 rows; the generator is not) |
| 21 | `scripts/pec-scratch-server.mjs` | 180 | PEC fixture affinity (R3A-016 / R4-P27 staged-surface partition) |
| 22 | `scripts/run-pec-bridge-rehearsal.ts` | 610 | PEC rehearsal affinity (same family) |

Reading of the residue (agent judgment): the concentration in `components/shell/`
and `lib/shell/` is a direct footprint of the DEL-02-01 R0-vintage ledger — its
21 rows evidence the shell at route/test granularity rather than per-component
file (R3A-056), so the shell's helper components were never individually claimed
or explicitly unmapped. The scripts/electron slice is tooling no wave's
deliverable-scoped sweep reached. Since run CSVs are immutable and this report is
the sweep's record of note, the residue is **routed to the R4 gate as a QA
finding**: it intersects the vintage packets (R4-P11/R4-P43 via R3A-056) and the
ownership packets R4-P29/R4-P30/R4-P27; disposition of each file (claim, list as
deliberate unmapped tooling, or ignore as immaterial) is owner business at R4.

### 2.4 Every unresolved row accounted (C6)

All 62 `CONFLICTS_AND_UNKNOWNS.csv` items carry a non-empty Owner and a non-empty
SmallestNextAction (script-verified; zero exceptions). Status: 49 OPEN, 13
RECORDED. Packet accounting:

- Every `R4-Pnn` reference in the CSV resolves to a packet defined in
  `PROPOSED_DECISION_FINDINGS.md` (50 packets defined; zero dangling references).
- 17 rows carry no packet reference; each has an explicit non-packet rationale
  on its own row, and each was cross-checked against the packet set:
  - R3A-009..012 (METHOD_RATIFICATION, "record-only") — these have packet
    equivalents R4-P11..P14 (superseding-note test; STALE_ASSESSMENT vs
    STALE_SPECIFICATION split; dated-note discipline; corpus-wide
    accepted-mapping test). Correspondence verified by content.
  - R3A-042..048 (REPAIR_TRANCHE, "R5 tranche, owner-gated at R4") — these are
    tranches A–G, packet equivalents R4-P38..P44 (v1→v6 label pins; CHECKING
    wording; REF-006 sweep; REF-007/008 paths; DepClosure pointer; noteless
    INSP-03 — gated by R4-P11; relocated evidence pointers). Verified by content.
  - R3A-050 (method edge case) — carried inside the R4-P14 fold (TYPES §6.2
    question), verified.
  - R3A-053, R3A-055, R3A-057, R3A-058, R3A-060 — genuinely record-only
    (reconciled cross-checks, terminology, coverage/index caveats on immutable
    run artifacts); rationale explicit on each row; nothing awaits a ruling.
- The four standing contests (R3A-001..004) route to packets R4-P17..P20, one
  each, with both readings and the deciding question preserved.

Companion proposal surface (C7): all 161 `PROPOSED_DELIVERABLE_UPDATES.csv` rows
are gated by a defined packet (`GatedBy` valid 161/161) and every AffectedClaims
pair resolves to a real ledger row (0 unresolvable pairs after multi-deliverable
row handling). REMAINING coverage (C13): the 69 R1 `REMAINING_INVENTORY.csv`
items correspond 1:1 per-deliverable with the ledger's 69 REMAINING_WORK rows;
exactly 56 rows carry `SelectableUnderCurrentLoop=YES` (the ungated set, all
REMAINING_WORK — zero MR-2 violations) and 13 are gated.

## 3. Plan §10 acceptance criteria — bullet-by-bullet verdicts

Known caveats carried honestly per the R3 dispatch: (a) DEL-03-04 and DEL-02-01
ledgers are R0-calibration vintage (pre-MR-1..11, never re-run in R2 — R3A-056);
(b) the PKG-03.md census transposition (spot-check F-1), corrected by append-only
erratum. Vintage caveats are QA findings routed to the R4 gate (they intersect
packets R4-P11 and R4-P43); **no ledger row is recoded here.**

1. **"100% of live deliverables and current requirement IDs are indexed."**
   **PASS-WITH-CAVEAT.** 53/53 deliverables indexed and ledgered (C2); all 616
   indexed requirement IDs map to ledger rows (C3). Caveat: the index itself
   under-enumerates — 13 zero-ID deliverables + 4 truncated-ID deliverables
   (§2.2) — mitigated by per-wave re-derivation from `Specification.md`
   (confirmed per deliverable, §2.2) and recorded as R3A-058. The criterion is
   met by the ledger; the index artifact alone would not meet it.
2. **"Every claim has a normative source or is explicitly IMPLEMENTED_UNMAPPED."**
   **PASS.** Zero empty `NormativeSource` cells run-wide; all 29 rows whose
   source cell is a NONE_FOUND-style declaration are `IMPLEMENTED_UNMAPPED`
   rows; all 36 IMPLEMENTED_UNMAPPED rows are typed and mirrored 1:1 in
   `UNMAPPED_IMPLEMENTATION.csv` (C5, C8).
3. **"Every behavioral ALIGNED claim has exact implementation and verification
   evidence tied to the reviewed source state."** **PASS-WITH-CAVEAT.** 671 rows
   cite `GATE-TRANSCRIPT(W1@fac46e33f)` in VerificationEvidence, 536 of them
   ALIGNED; frontend byte-identity `4c8ed8907 = fac46e33f = HEAD` held at every
   wave dispatch, both R3 syntheses, the §10 spot check, and this report.
   Caveat (vintage citation form, binding still valid): 24 DEL-03-04 rows cite
   the blessed Receipt-4 fallback (`61d70bdb0` + byte-identity) instead of the
   W1 transcript; DEL-02-01 rows bind directly at `4c8ed8907` (8 rows name the
   SHA), re-blessed by R1's byte-identity verification. Note: this is a
   *third* citation form — the spot-check's §7.3 wording groups DEL-02-01 under
   the Receipt-4 fallback, which is imprecise (finding CQ-F3).
4. **"Every existing inspection assessment is classified as current, stale, or
   non-applicable at claim level."** **PASS-WITH-CAVEAT.** 1,086/1,115 rows
   carry the exact MR-1 machine token; the 29 token-less rows are exactly the
   R0-vintage set (27 DEL-03-04 + 2 DEL-02-01 — script-confirmed, C8) and
   classify the assessment in prose. Within that set, 4 DEL-03-04 rows
   (REQ-004/REQ-005/ACC-002/ACC-003) sit on the wrong side of the run's own
   noteless-supersession precedent — the spot-check's WOULD-RECODE
   (STALE_ASSESSMENT) items, routed to R4-P11/R4-P43, not recoded. The
   DEL-02-01 equivalent check is finding-free at disposition level (§3a2 below).
5. **"Every material implementation surface is mapped or listed as unmapped."**
   **PASS-WITH-CAVEAT.** The mapped-or-listed discipline holds for 133/155
   files (123 exact + 10 coarser-granularity/packet-covered); the 22-file
   residue of §2.3 (CQ-F1) is neither cited nor listed. The sweep itself — the
   R1-committed check — is hereby performed and recorded; the residue is routed
   to R4. Until an owner disposes of it, this bullet is not fully satisfied at
   exact-path granularity.
6. **"Every live deliverable's present or absent ## Remaining section is
   checked."** **PASS.** 69/69 R1-inventoried Remaining items have ledger
   REMAINING_WORK rows, per-deliverable counts equal (C13); gate suffixes
   carried verbatim (MR-6); 56 ungated rows are the run's only Selectable=YES
   values (zero MR-2 violations); spot-check verified verbatim text
   reproduction on its sample.
7. **"Every agent-file or agent-workflow implication is classified
   DEFERRED_AGENT_WORKFLOW, recorded without a redesign recommendation, and
   excluded from proposed deliverable updates."** **PASS.** Full-cell scan:
   the token appears in zero of the 1,115 rows' cells (C8) — the run's
   sweep result is that no row *required* the deferral disposition, with
   per-deliverable boundary affirmations in the agent-adjacent packages' notes
   and the PKG-08 fan-in audit. `AGENT_WORKFLOW_OBSERVATIONS.md` carries the
   two genuinely workflow-dependent boundary observations, evidence-only, with
   no recommendation; its non-item audit confirms no R5 tranche or proposed
   update edits agent instructions, indexes/matrices, or skill contracts (the
   one conditional — R4-P33's frontmatter-contract portion — is explicitly
   split out to the owner-led program).
8. **"Every conflict and unknown has an owner and smallest next action."**
   **PASS.** 62/62 rows, script-verified; every OPEN item routes to a defined
   packet or carries an explicit record-only rationale, with the
   packet-equivalence table verified (§2.4).
9. **"Package summaries are reproducible from the claim ledger."**
   **PASS-WITH-CAVEAT.** Script C11 recomputed every package's disposition
   census from `CLAIM_CONCORDANCE.csv` and compared it against every census
   table in `PACKAGE_SUMMARIES/PKG-00..10.md`: all 11 reproduce exactly —
   PKG-03 via its 2026-07-12 append-only erratum, whose corrected numbers
   (DEL-03-04: 28 rows = ALIGNED 24 / PARTIALLY_IMPLEMENTED 1 /
   STALE_SPECIFICATION 1 / IMPLEMENTED_UNDOCUMENTED 2; package total 89;
   package ALIGNED 72, ACCEPTED_DIVERGENCE 1) this report independently
   re-verified by script (C9), including byte-identity of the R0 DEL-03-04
   rows to the merged ledger. Caveat: the original PKG-03 table (F-1
   wrong-deliverable transposition at W2 fan-in) remains in place above the
   erratum per append-only discipline; bullet 9 is satisfied only through the
   erratum, and F-1 stands as the run's one derived-artifact REFUTED finding.
10. **"A reviewer spot-checks all high-risk claims plus a representative sample
    of other dispositions."** **PASS.** `R3_SPOT_CHECK.md` (independent §10
    reviewer): 101 selections / 100 unique rows — all 8 LOW-confidence rows,
    40 of the 61-row high-risk union (cap disclosed), all 4 standing contests,
    all 28 DEL-03-04 rows, and a 30-row all-disposition all-package stratum;
    **100/100 CONFIRMED, 0 REFUTED, 0 UNVERIFIABLE, 0 STALE_INPUT.** Two
    parenthetical imprecisions in that record are corrected by this report
    (CQ-F2, CQ-F3); neither affects any row verdict.

### 3(a) Vintage caveat detail — the two R0-vintage ledgers

**(a1) DEL-03-04 (28 rows, known from `R3_SPOT_CHECK.md` §5, restated for the
record):** 28/28 evidence-CONFIRMED at source state; 0 STALE_INPUT; 24 CURRENT;
4 WOULD-RECODE(STALE_ASSESSMENT) under the run-harmonized noteless-supersession
precedent (REQ-004, REQ-005, ACC-002, ACC-003 — INSP-03 PARTIALs overtaken by
ORN-09, assessment noteless); 27/28 rows lack the MR-1 machine token; 24
behavioral rows cite the Receipt-4 fallback form; MR-7/MR-10 vocabulary absent
on the vintage rows; **2 missing MR-5 REGISTER_DEFECT rows** ((i)
`_DEPENDENCIES.md` digest ACTIVE 10 / RETIRED 0 vs DEP-03-04-008 RETIRED;
(ii) DEP-03-04-006/007/009 SatisfactionStatus TBD against implemented
prerequisites). Routed to R4-P11/R4-P43 (and the TBD class to R4-P15).

**(a2) DEL-02-01 (21 rows) — the equivalent check, enumerated by this report
from `R0_CALIBRATION/DEL-02-01_claims.csv` (byte-identical to the merged rows,
script-verified) and its R0 notes:**

- **Census:** ALIGNED 9, STALE_SPECIFICATION 5, IMPLEMENTED_UNDOCUMENTED 3,
  STALE_ASSESSMENT 2, STALE_VERIFICATION 1, IMPLEMENTED_DIFFERENTLY 1.
- **WOULD-RECODE under the harmonized precedent: ZERO rows.** Unlike DEL-03-04,
  DEL-02-01's overtaken noteless INSP-03 PARTIAL conclusions are *already* coded
  as defects on the correct side of the R4-P11/P12 line: assessment-only
  staleness → STALE_ASSESSMENT (REQ-001, REQ-011); kit/corpus surfaces still
  carrying the stale wording → STALE_SPECIFICATION (REQ-002, REQ-007, REQ-008,
  EXC-004, ACC-001); the coverage-gap PARTIAL → STALE_VERIFICATION (REQ-003).
  All 9 ALIGNED rows rest on STILL-CURRENT INSP-03 PASS conclusions. The R0
  DEL-02-01 packet is internally consistent with the run's settled precedent.
- **MR-1 tokens:** 19/21 rows carry a scannable token in prose; 2 lack one —
  REQ-003 (nonstandard "STILL PARTIALLY CURRENT") and EXC-004 (no token).
  These are the run's only token-less rows outside DEL-03-04 (29 total, C8).
- **MR-3 citation form:** 0/21 rows cite `GATE-TRANSCRIPT(W1@fac46e33f)` and
  0/21 cite the Receipt-4 `61d70bdb0` fallback; the rows bind directly at
  `4c8ed8907` (8 rows name the SHA; the rest cite test files/lines without a
  SHA). Binding validity rests on R1's byte-identity verification
  (`4c8ed8907` = `fac46e33f`), which held through this report's own re-check.
- **MR-5 REGISTER_DEFECT rows: ZERO exist** (ClaimType scan). The R0 notes
  record two register-defect-class facts that the R2 method would ledger as
  `REGISTER-<n>` rows and that therefore are **missing rows**, exactly parallel
  to DEL-03-04's: (i) `DEP-02-01-005` still records the implementation
  workspace as `TargetType=UNKNOWN`/TBD while Procedure.md has named the exact
  `frontend/` paths since 2026-06-21 (notes' "register metadata lags
  implementation, REMAINING_STATE_MISMATCH in character"); (ii) the 4 EXECUTION
  rows carry `SatisfactionStatus=TBD` against implemented prerequisites (the
  Declared-TBD class of R4-P15, itself contested). Note the ledgered EXC-004
  covers a *kit-wording* dependency-deferral staleness, not these register
  facts. Routed to R4-P11/R4-P43/R4-P15. This also refutes a spot-check
  parenthetical — finding CQ-F2.
- **Residual R0-notes flag:** the DEL-02-01 R0 notes flagged "corpus-wide
  `_STATUS.md` header shape (`Checking Approval SHA` above IN_PROGRESS)" to R3
  in case it deserved a packet. No packet names it explicitly; the nearest
  class is R4-P39 (CHECKING-lifecycle wording), and the notes' own analysis
  (headers are preserved historical evidence under D-APP-54 / precedence note
  2, so no row was raised) stands. Recorded here as accounted-with-note
  (CQ-F5); no action proposed.

### 3(b) F-1 erratum verification (C9)

Script-recomputed from the merged ledger: PKG-03 = 89 rows; DEL-03-04 column =
28 rows (ALIGNED 24, PARTIALLY_IMPLEMENTED 1, STALE_SPECIFICATION 1,
IMPLEMENTED_UNDOCUMENTED 2); package totals ALIGNED 72, PARTIALLY_IMPLEMENTED 7,
REMAINING_STATE_MISMATCH 5, ACCEPTED_DIVERGENCE 1, IMPLEMENTED_UNDOCUMENTED 3,
STALE_SPECIFICATION 1. **Every figure in the PKG-03.md erratum table matches;
every figure in the original (pre-erratum) DEL-03-04 column and package total
does not.** The erratum's diagnosis (transposition of the DEL-02-01 R0 census)
is consistent with C10's DEL-02-01 figures. R0 DEL-03-04 rows verified
byte-identical (cell-by-cell) to the merged ledger rows.

## 4. Findings register (everything not plain-PASS, including NEW defects)

Known items carried: R0-vintage caveats (§3a, → R4-P11/P43/P15), F-1 erratum
(§3b, corrected), REQUIREMENT_INDEX parser gap (§2.2, R3A-058), contest
visibility asymmetry (spot-check F-3, faithfulness observation only).

**NEW findings from this coverage verification:**

- **CQ-F1 (coverage residue, routed to R4).** 22 of 155 indexed implementation
  surfaces (≈4,830 LOC, incl. the 2,098-LOC `globals.css` and six substantive
  shell view components) have no citation at any granularity anywhere in the
  run's evidence and are not listed as unmapped (§2.3 table). Dominantly a
  DEL-02-01 R0-granularity footprint plus tooling outside every wave's
  deliverable scope. Caveats §10 bullet 5.
- **CQ-F2 (spot-check parenthetical REFUTED, minor).** `R3_SPOT_CHECK.md` F-2
  states of DEL-02-01: "MR-5 register rows DO exist for it." Script scan:
  DEL-02-01 has **zero** REGISTER_DEFECT rows; its register-defect facts live
  only in R0 notes prose, i.e. DEL-02-01 has ~2 missing MR-5 rows just as
  DEL-03-04 does (§3a2). No row verdict is affected; the F-2 *conclusion*
  (exposure is method vintage, not evidence quality) stands — strengthened,
  since the missing-row condition is now known to be symmetric across both
  R0-vintage ledgers.
- **CQ-F3 (spot-check wording imprecision, minor).** `R3_SPOT_CHECK.md` §7.3
  groups DEL-02-01's rows under the "blessed Receipt-4 fallback" binding; in
  fact 0/21 DEL-02-01 rows cite `61d70bdb0` — they bind directly at
  `4c8ed8907` (§3a2). The binding is valid either way; only the citation-form
  description was off.
- **CQ-F4 (parser-gap extent, record).** The REQUIREMENT_INDEX gap is 13
  zero-ID + 4 truncated-ID deliverables (§2.2) — broader than the 7 named in
  the W2 dispatch brief (Receipt 20) and additive to the W5/W7 confirmations.
  All 17 confirmed covered by re-derived claim sets; index-only defect
  (R3A-058 class), no coverage loss.
- **CQ-F5 (accounted-with-note).** The DEL-02-01 R0-notes header-shape flag to
  R3 is not named by any packet; nearest class R4-P39; the notes' own
  D-APP-54-based no-action analysis stands (§3a2).

No other discrepancy was found by any check: zero MR-2 violations, zero
DEFERRED_AGENT_WORKFLOW occurrences, zero duplicate claim keys, zero dangling
packet references, zero unresolvable proposal rows, zero empty Owner/
SmallestNextAction cells, zero empty NormativeSource cells, and exact row-count
reconciliation across R0/R2/merged ledgers (1,066 + 49 = 1,115).

## 5. QA conclusion

Under plan §10, the **discovery program's acceptance criteria are met** — six
bullets PASS outright; four PASS-WITH-CAVEAT (bullets 1, 3, 4, 5, 9 caveats are
each enumerated, evidence-bound, and routed to named R4 packets or recorded as
immutable-artifact notes; none is silent). The repair-program criterion of §10
is **out of scope by design**: this run stops at the R4 human decision gate with
zero repairs executed. All caveats and findings above are agent judgments for
owner review at R4; nothing here rules, adopts, transitions, or repairs anything.
