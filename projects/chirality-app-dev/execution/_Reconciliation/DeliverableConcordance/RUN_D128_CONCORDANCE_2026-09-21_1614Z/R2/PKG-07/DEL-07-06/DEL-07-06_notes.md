# DEL-07-06 Reference Hash and Snapshot Conventions: R2 forward notes (pass 1)

Basis: frozen tree `00115c719`. Ledger: `DEL-07-06_claims.csv` (59 rows). Validator: `RESULT PASS errors=0 warnings=0`.

## 1. Census

Rows: 59 in total. 56 rows cover the 29 indexed units (all `CLM`; this deliverable has no `REM` or `REMTXT` units), and 3 are run-local `REGISTER-n` rows.

| Disposition | Rows |
|---|---:|
| ALIGNED | 30 |
| STALE_SPECIFICATION | 19 |
| NOT_AUDITABLE | 7 |
| PARTIALLY_IMPLEMENTED | 2 |
| STALE_ASSESSMENT | 1 |

| ClaimType × Disposition | Rows |
|---|---:|
| REQUIREMENT / ALIGNED | 20 |
| REQUIREMENT / PARTIALLY_IMPLEMENTED | 1 (CLM-010.14, REQ-014) |
| REQUIREMENT / STALE_SPECIFICATION | 1 (CLM-018) |
| ACCEPTANCE / ALIGNED | 8 |
| ACCEPTANCE / PARTIALLY_IMPLEMENTED | 1 (CLM-012.6) |
| ACCEPTANCE / STALE_SPECIFICATION | 1 (CLM-019) |
| ACCEPTANCE / STALE_ASSESSMENT | 1 (CLM-021.1, VER-001) |
| EXCLUSION / ALIGNED | 2 |
| STATE_ASSERTION / STALE_SPECIFICATION | 9 |
| CONTEXT_CLAIM / NOT_AUDITABLE | 7 |
| CONTEXT_CLAIM / STALE_SPECIFICATION | 5 |
| REGISTER_DEFECT / STALE_SPECIFICATION | 3 |

- **SEE rows (counted separately):** 21 rows carry `SEE:`.
  - 12 point to the REF-006/hash finding: `REGISTER-1` directly, or `CLM-001` for its verbatim repeats.
  - 8 are `CLM-012.n` verification rows pointing to their `CLM-010.n` requirement rows.
  - 1 is CLM-029 → CLM-028.
- **Distinct findings without SEE rows:** 38 rows. There are 8 non-ALIGNED, non-SEE rows: CLM-007, CLM-010.14, CLM-019, CLM-020, CLM-021.1, CLM-026, CLM-027, CLM-028. REGISTER-1 and REGISTER-3 are also distinct findings; REGISTER-2 SEEs REGISTER-1.
- **Split rate:** 5 of 29 units split (17%).
  - CLM-004: 4 rows (a condition table of independently dispositionable rows).
  - CLM-010: 16 rows (requirements table, REQ-001..016). The index lists no SubItems here because the rows use the `DEL-07-06-REQ-nnn` form.
  - CLM-012: 8 rows (index SubItems REQ-001, 002, 006, 008, 012, 014, 015, 016).
  - CLM-014: 2 rows (AC-001, and the unnumbered output list).
  - CLM-021: 2 rows (VER-001, and the Pass 3 table).
- No errata (pass 1).

## 2. Least-confident rows

No row is LOW. The MEDIUM rows with a real alternative reading:

- **CLM-010.10 (REQ-010, void approval on content change).** Read here as a human-review convention, and so ALIGNED. The deliverable is a DOC_UPDATE and CLM-009 excludes implementation. Alternative reading: under subject-test rule 2, it is a product control (approval), and the live path has no mechanism that voids an approval when content changes. That reading gives `DOCUMENTED_UNIMPLEMENTED` with no legacy code, so R4-Q1 would still not apply. K-AUTH-2 lists `_STATUS.md` rules, the CHANGE workflow and human review as its enforcement surfaces, which supports the reading taken.
- **CLM-010.14 / CLM-012.6 (REQ-014, PARTIALLY_IMPLEMENTED).**
  - The "with REF-006 hash warning" suffixes survive in the Source cells.
  - The D-APP-56 current-state notes (SoW :28, :116, :224, :342) declare that wording to be history.
  - PRD no longer reproduces at the frozen basis, so the requirement's trigger is live again.
  - Alternative readings: `ALIGNED` (the suffixes are visible) or `STALE_SPECIFICATION` (the notes neutralise the warning).
- **CLM-006 (Construction), ALIGNED.** No separate convention artifact exists. The content lives inside the SoW, which replaced Datasheet/Specification/Guidance/Procedure.md in `14e94bd0b` on 2026-07-13. Alternative reading: `DOCUMENTED_UNIMPLEMENTED` if "components" means separate artifacts.
- **CLM-021.1 (VER-001), STALE_ASSESSMENT.** The only review on record is INSP-03 (2026-06-21). It cites deleted files and a pre-D-APP-38 caveat, and its source-state check would fail at the frozen basis. Alternative reading: `STALE_VERIFICATION`.
- **REGISTER-3 (dependency evidence anchors to deleted files).** Taken as `STALE_SPECIFICATION` under Addendum 5 rule 1 ("a file said to exist"). The alternative, `REMAINING_STATE_MISMATCH` (lagging provenance), is recorded as `ALSO:`.
- **CLM-019/026/027/028 (substitution artifacts).** CauseTag is `CARRIER_PROPAGATION`: the D-APP-56 R5 P40 carrier edit replaced warning tokens with "MATCH", which left incoherent sentences. An alternative CauseTag is `DOC_HYGIENE`, recorded as `CAUSE2` on most of these rows.

## 3. Register-defect summary

- **REGISTER-1 (`_REFERENCES.md`).** REF-002 (CONTRACT), REF-003 (SPEC) and REF-006 (PRD) record `MATCH`, but none reproduces: `HASH-RECOMPUTE@00115c719`, `REFERENCE_HASHES.csv` `Match=NO`.
  - The recorded hashes equal corpus `v23` in `execution/_Reconciliation/References/AUTHORITY_CORPUS.json`, which is still `current_version`.
  - Three later commits on 2026-09-12 edited the docs without the corpus bump that D-APP-38 requires: `95b342519` and `7f1e9f387` (CONTRACT), and `9eaddb596` (SPEC, PRD).
  - DIRECTIVE, TYPES and PLAN were recomputed here and do reproduce.
  - REF-007/009/010 (Root `workflows/`) were not recomputed; they are outside the evidence roots.
  - SoW restatements take `SEE:` to this row: CLM-001/004.1/007/008/014.2/015/017/018/022/025.
- **REGISTER-2 (`_DEPENDENCIES.md`:29, :85; `Dependencies.csv` DEP-07-06-013).** The present-tense "REF-006 is MATCH" is restated, and it is the premise of the DEP-07-06-013 retirement.
- **REGISTER-3 (`Dependencies.csv` EvidenceFile/SourceRef; `_DEPENDENCIES.md` register table).** Evidence is anchored in Datasheet.md, Procedure.md and Specification.md, which were deleted on 2026-07-13.
- **Not raised as a defect: `_STATUS.md` header fields.** "Authorization Basis D-APP-19" and "Checking Approval SHA" remain while the state is IN_PROGRESS. D-APP-54 keeps those approval SHAs as historical evidence, so they are not a lag.
- **D-APP-127 application map:** all five carriers are `NO`. None of them describes engine or Runtime topology, so no `CARRIER_PROPAGATION` finding arises from D-GOV-43 for this deliverable.

## 4. Direction and cause

- **CauseTags:**
  - `DOC_HYGIENE`: 14 rows (the hash/reference defects, including the REQ-014 rows).
  - `CARRIER_PROPAGATION`: 5 rows (substitution artifacts from the D-APP-56 R5 P40 edit).
  - `PRE_V3_DRIFT`: 3 rows. The 2026-07-13 replacement of the four documents left CLM-020 records and REGISTER-3 anchors naming deleted files, and VER-001's only review predates it.
- **CAUSE2 secondaries:**
  - `CARRIER_PROPAGATION` on CLM-007 (REF-007 path superseded at corpus v21 and never carried into the SoW) and on REQ-014.
  - `DOC_HYGIENE` on CLM-019/020/021.1/027/028.
- **CONTEXT records used:** none. Every divergent row has `DirectionEvidence = NONE_FOUND`.
- **Searches behind each NONE_FOUND:**
  - `_DECISIONS/_REGISTER.md`, grepped for `corpus|AUTHORITY_CORPUS|re-hash|v24`: only the D-APP-38 row matched.
  - `_REGISTER.md`, grepped for `production contract|Scope of Work|SOW_V1`: no ruling covers the 2026-07-13 SoW replacement.
  - CONTEXT sources (`plans/steers`, listed AgentRuns), grepped for "corpus drift": no CONTEXT hit. The drift deferral appears only in the non-CONTEXT `AgentRuns/HELP-HUMAN-APP-20260919-LOOP-WORKGRAPH/REVIEW_BRIEF.md:24`, which RUN_BASIS §5 records as a known basis defect.
- **Governing ruling used: D-APP-38.** Its reference-integrity model (hybrid tool plus versioned corpus snapshots) is the governing basis cited in LatestDecision. It explains how drift should be handled, not why the bump was skipped.
- **Reachability:**
  - **filesystem.ts scanner (confirmed from the route):** `GET frontend/src/app/api/project/deliverables/route.ts` → `scanProjectDeliverables` (filesystem.ts:1156) → `scanDeliverableDocumentKitContract` (:589, called at :1241) → `addReferenceWarnings` (:536) and the bypass-file check (:937).
  - **Approval-SHA gate (confirmed from the route):** `POST .../deliverable/status/transition/route.ts` → `deliverable-contracts.ts:364` → `transition.ts:92-118`. Its only UI callers are `pipeline-surface.tsx` and `workbench-surface.tsx`. I did not check whether those surfaces are rendered; the route handler itself is the live entry.
  - **MCP path:** `read-tools.ts:938` is `LEGACY_ONLY`, as the pack says.
  - I found no disagreement with `REACHABILITY.csv`.
- **Live-scanner gap:** the live scanner only flags literal `HASH_MISMATCH` text. It never recomputes hashes, so the App cannot surface REGISTER-1.

## 5. Method friction

- **Execution-tree governance scripts:** `execution/_Scripts/references_hash_tool.py`, `validate_dependencies.py` and `execution/_Reconciliation/References/reconcile_authority_corpus.py`.
  - They are the actual "accepted reference hash tooling and dependency-linter tooling" (K-REF-1). They are hand-run governance tools, not product code.
  - The REACH vocabulary has no tag for them, so Addendum 1 item 4 forces `REACH=LEGACY_ONLY` with `UNREACHED`.
  - Read literally, Addendum 6 rule 3 would then attach `R4-Q1`. R4-Q1 is about retained harness code, and these scripts are not that, so I did not cite R4-Q1 on CLM-010.3 and CLM-010.12 (on CLM-010.4 and .5, LIVE code also meets the claim).
  - **Proposal:** a `REACH=TOOLING` tag (or an explicit carve-out) for execution-tree governance scripts, excluded from rule 3. If the verifier applies rule 3 literally, CLM-010.3 and CLM-010.12 would gain `R4-Q1`.
- **Substitution-artifact dispositions:** mechanically edited sentences that became incoherent (not false, just meaningless) fit `STALE_SPECIFICATION` only loosely. A tag such as `OTHER:SUBSTITUTION_ARTIFACT` could be considered.
- **Index gap:** the claim index does not recognise `DEL-07-06-REQ-nnn` IDs in CLM-010 as SubItems. It lists them only under CLM-012, where the short `REQ-nnn` form appears.

## Coverage gaps

These texts are not owned by any indexed unit:

- **SoW frontmatter and Purpose (:1-20):**
  - OUT-001, and the D-APP-80 concordance note that SOW-077 is an OUT boundary-only trace. That note is consistent with decomposition :480.
  - The `decomposition_basis` pin `7b0be4d8…` (a RUN_BASIS §5 known basis defect).
- **SoW "Output and Evaluation Matrix" (:430-434):** it maps OUT-001 to requirement ref `CLM-008`. CLM-008 is the stale current-state note heading, not a requirement unit, which is questionable traceability.
- **`_SEMANTIC.md` and `_SEMANTIC_LENSING.md`:** generated 2026-05-20 and dated. `_SEMANTIC.md` says the state is `INITIALIZED`, a dated snapshot. They are not audited as units.
- **`Assessment_INSP-03` D-APP-56 annotation (:70):** it records the REF-006 MATCH hash as `ac35fba4…`. That differs from the `_REFERENCES.md` value `8649ccba…`, being an older corpus version. It is dated assessment evidence, not declared state.

## 6. Effort

About 25 files or ranges read:

- the deliverable's 8 carrier files;
- CONVENTIONS and RUN_BASIS;
- the evidence pack;
- governing-clause ranges in SPEC, CONTRACT, DIRECTIVE, PLAN and PRD;
- the D-APP-38 ruling and register rows;
- `filesystem.ts`, `transition.ts`, the transition route and `register-reader.ts`;
- the execution scripts and the corpus README/JSON;
- git log/show for the deliverable folder and the docs.

The context budget was not tight.
