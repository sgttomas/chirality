# Deepcut Human Draft DBM Review Execution Plan

## Purpose

This plan tells a future agent how to review a human-prepared Design Basis Memorandum (DBM) for the West Doe Deepcut scope against the governed Deepcut knowledge base.

The review is not a publication run and is not a DBM_PUBLISHER rerun. The colleague's DBM is a candidate document. Governed Deepcut DOMAIN/SCA/KTY/KA state remains the reference truth. The review produces candidate findings for human disposition; it does not update governed truth, `_LATEST.md`, publication package pointers, or accepted snapshots.

The execution topology is:

1. Reference health check and shared review substrate
2. Global DBM Reviewer
3. One CAT Reviewer per Deepcut category
4. Findings Aggregator
5. RECONCILIATION pass
6. Evidence bundle for human source navigation
7. Human disposition through REVIEW or a review disposition register

## Why This Topology

The failed pre-authoring concordance model showed that a sparse controlled-fact register can narrow the review or authoring surface. A human draft review needs broader engineering judgment:

- The whole DBM must work as a governing senior-engineer design-basis document.
- Each category must be checked against its own KTY/KA truth, not just against extracted values.
- Cross-category issues must be separated from local CAT findings and handled by RECONCILIATION.
- Humans need a navigable evidence bundle so they can validate feedback against draft locations and governed source material without reconstructing the review path from agent prose.
- Humans retain acceptance and disposition rights under HELPS_HUMANS. Agents prepare evidence and candidate findings; humans decide.

CAT-level review is useful because the Deepcut knowledge base is organized by CAT -> KTY -> KA. Each CAT reviewer can read the entire draft DBM for context while owning only the findings tied to KTYs in its assigned CAT. This gives parallel depth without letting any local reviewer become the whole authority.

## Governing Inputs

Use these Deepcut publication planning artifacts as review scaffolding:

- `domain-test/domains/West_Doe_Deepcut_DBM/_Publication/DBM/_Planning/Publication_Input_Manifest.md`
- `domain-test/domains/West_Doe_Deepcut_DBM/_Publication/DBM/_Planning/Publication_Schema.md`
- `domain-test/domains/West_Doe_Deepcut_DBM/_Publication/DBM/_Planning/Publication_Rules.md`
- `domain-test/domains/West_Doe_Deepcut_DBM/_Publication/DBM/_Planning/Section_Map.csv`

Use accepted DOMAIN/SCA state, mapped KTY/KA artifacts, supersession state, open issues, and current Deepcut registers as authority. The old `Publication_Concordance_Register.csv` may be read only as historical context if needed; it must not be used as the completeness checklist.

The draft DBM should be placed under a review run folder, for example:

`domain-test/domains/West_Doe_Deepcut_DBM/_Publication/DBM/_Review/REVIEW-YYYYMMDD-HUMAN-DRAFT/Draft_DBM.md`

If the source draft is Word or PDF, preserve the original file in the same review folder and convert a working Markdown copy for line-addressable review.

## Execution Steps

### 1. Reference Health Check

Before reviewing the draft, confirm the review basis is usable:

- `Publication_Input_Manifest.md`, `Publication_Schema.md`, `Publication_Rules.md`, and `Section_Map.csv` exist.
- `Section_Map.csv` artifact paths resolve to real KTY/KA files.
- Latest `_ScopeChange/_LATEST.md` and any accepted supersession state are identified.
- Retired, tombstoned, archived-stubbed, or no-factual-use KTYs are not treated as active design-basis authority.
- Any missing governed input is recorded as `EVIDENCE_INCOMPLETE`; do not silently lower the review standard.

Prepare the shared review substrate once at the start of the run. If `dbm-draft-review` and its deterministic review tools exist, use the tools directly or run the skill in substrate-preparation mode if available. If the skill does not yet exist, perform the same checks manually and write equivalent review artifacts.

The shared substrate should include:

- `Section_Coverage.csv`
- `Draft_Claims.csv`
- `TBD_Inventory.csv`
- `Body_Thinness.csv`
- `Evidence_Bundle_Summary.md`

The Global DBM Reviewer and CAT Reviewers consume this substrate alongside their own governed-truth reads. They should not rerun extraction work unless the substrate is missing or unreliable.

If `dbm-draft-review` emits `Candidate_Findings.csv` during this step, treat those rows as Global DBM Reviewer candidate findings unless the human explicitly requests a separate single-pass review. The multi-agent topology remains the governing review method for this plan.

### 2. Global DBM Reviewer

The Global DBM Reviewer reads the entire draft DBM and the planning artifacts. It does not deeply adjudicate every KTY. It checks whole-document quality and review substrate:

- section coverage against the approved schema and run-specific section map,
- body thinness and summary-only sections,
- senior-engineer DBM style and governing-document register,
- table treatment and omitted design-basis table classes,
- TBD/TBC/assumption handling,
- supersession and current-state presentation at the document level,
- traceability and provenance sufficiency for review.

Output global candidate findings to `Global_Findings.csv` or the shared review finding register with `ReviewerScope=GLOBAL`.

### 3. CAT Reviewers

Dispatch one reviewer per active Deepcut CAT. Each CAT reviewer:

- reads the entire draft DBM for context,
- reads only its assigned CAT's KTY/KA governed content as the owned authority set,
- uses `Section_Map.csv` to identify where the CAT's KTY/KA content should appear in the DBM,
- checks whether the draft materially represents the CAT's governed design-basis content,
- checks values, configurations, operating modes, interfaces, design constraints, assumptions, TBDs, and supersession-sensitive statements,
- writes only CAT-owned candidate findings.

Use inline TASK/subagent briefs for CAT reviewers unless a dedicated CAT-scoped review skill exists. Do not require a new skill before executing this plan. Each CAT brief must name:

- assigned `CAT`,
- owned KTYs and KA files, preferably enumerated from `Section_Map.csv`,
- read scope: full draft DBM, planning artifacts, shared substrate, and assigned CAT KTY/KA authority set,
- write scope: only `CAT_<CAT-ID>_Findings.csv` under the review run folder,
- required finding schema and controlled taxonomy,
- instruction to label cross-category issues as `CrossCATCandidate=YES` and defer resolution to RECONCILIATION.

If same-model subagents are not available, run the same CAT briefs sequentially.

Each CAT finding must include:

- `FindingID`
- `ReviewerScope`
- `CAT`
- `KTY`
- `KA`
- `DBMSection`
- `DraftLocation`
- `DraftText`
- `FindingType`
- `Severity`
- `GovernedTruthRef`
- `SupersessionRef`
- `Explanation`
- `EvidenceSource`
- `CrossCATCandidate`
- `Origin`

Set `Origin=AGENT_CHECK` for agent-prepared findings. Set `CrossCATCandidate=YES` when the reviewer notices a possible cross-category issue; do not resolve cross-CAT conflicts inside a CAT review.

Use this controlled finding taxonomy:

- `Incorrect`: draft contradicts governed KTY/SCA/supersession truth.
- `Unsupported`: draft makes a claim not warranted by the governed knowledge base.
- `Missing`: governed material exists but is absent from the draft.
- `Flattened`: draft converts TBD/conflict/assumption into a firm fact.
- `Outdated`: draft uses superseded source DBM content.
- `Incomplete`: draft has the right topic but lacks required engineering detail.

### 4. Findings Aggregator

The Findings Aggregator merges Global and CAT outputs into one human-facing finding register:

`Review_Findings.csv`

The aggregator:

- deduplicates overlapping findings,
- preserves all source reviewer references,
- normalizes finding type and severity,
- checks that each finding has draft location and governed-truth evidence,
- separates local CAT findings from cross-CAT candidates,
- links each finding to one or more evidence bundle entries,
- writes an executive review summary.

The aggregator does not accept, waive, or reject findings. Human disposition fields remain `TBD`.

Recommended disposition register columns:

- `FindingID`
- `FindingType`
- `Severity`
- `ReviewerScope`
- `CAT`
- `KTY`
- `KA`
- `DBMSection`
- `DraftLocation`
- `Explanation`
- `EvidenceSource`
- `Origin`
- `ProposedDisposition`
- `HumanDisposition`
- `HumanNotes`
- `DispositionDate`

Allowed `HumanDisposition` values:

- `TBD`
- `ACCEPT_AS_IS`
- `REVISE`
- `WAIVE_WITH_RATIONALE`
- `DEFER`
- `NOT_APPLICABLE`

### 5. RECONCILIATION

Run RECONCILIATION after aggregation. The reconciliation pass reads the whole draft DBM, the aggregated finding register, and the cross-CAT candidates.

For this review, RECONCILIATION may synthesize directly from the available evidence without dispatching Type 2 audit tasks. Its role is to evaluate cross-category and cross-section coherence from the draft, aggregated findings, `Section_Map.csv`, and cross-CAT candidates. Do not force the task through an unrelated Type 2 registry entry.

It checks:

- shared design parameters used in multiple sections,
- utilities/process interface consistency,
- equipment configuration repeated across categories,
- operating assumptions shared across disciplines,
- supersession/current-state consistency across sections,
- duplicate or conflicting candidate findings.

RECONCILIATION writes either reconciliation candidate findings or a no-cross-cutting-finding statement. Human disposition remains separate.

### 6. Evidence Bundle

Build a separate evidence bundle after aggregation and RECONCILIATION:

`Review_Evidence_Bundle.md`

The purpose of this file is human navigation and validation. It should let the human move from each review finding to:

- the exact draft DBM location,
- the CAT/KTY/KA governed source location,
- the quoted or summarized governed truth,
- the reviewer explanation,
- any supersession/open-item context,
- related findings or cross-CAT reconciliation notes.

The evidence bundle is not a second findings register and is not authority. It is a source-navigation package. It may later be useful as input context for a subsequent DBM_PUBLISHER run to improve trace appendix or reference injection, but that downstream use requires explicit authorization and must not turn the review bundle into governed truth.

Recommended structure:

1. `Review Evidence Index`
   - table keyed by `EvidenceID`
   - columns: `FindingID`, `ReviewerScope`, `CAT`, `KTY`, `KA`, `DBMSection`, `DraftLocation`, `GovernedTruthRef`, `EvidenceType`, `RelatedEvidenceIDs`
2. `Finding Evidence Blocks`
   - one block per finding
   - includes draft excerpt, governed source excerpt or concise source summary, source paths, line references when available, and reviewer rationale
3. `Cross-CAT Evidence`
   - evidence blocks tied to RECONCILIATION candidates
4. `Source Navigation Appendix`
   - grouped links by CAT/KTY/KA so the human can inspect source files directly
5. `Limitations`
   - missing files, unavailable line references, unresolved supersession state, or review dimensions that could not be assessed

When quoting source text, keep excerpts short and use summaries where possible. The goal is fast source validation, not duplicating the knowledge base.

Every row in `Review_Findings.csv` must reference at least one `EvidenceID` in `Review_Evidence_Bundle.md`. Findings that cannot be tied to source evidence must be labelled as review limitations, not asserted as governed discrepancies.

### 7. Human Disposition

Present the review report, `Review_Findings.csv`, and `Review_Evidence_Bundle.md` to the human. The human dispositions findings directly or through REVIEW.

If using REVIEW formally, treat the review run folder as the review target. Use REVIEW for finding capture and disposition tracking, not for lifecycle promotion. Gate 5 lifecycle-transition semantics do not apply unless the human explicitly turns this review output into a lifecycle-managed deliverable.

No pointer updates, accepted package pointer changes, `_LATEST.md` edits, or governed truth edits are allowed unless explicitly authorized after review.

## Output Package

Write review outputs under the review run folder:

- `Draft_DBM.md`
- original source draft, if applicable
- `Review_Input_Manifest.md`
- `Global_Findings.csv`
- `CAT_<CAT-ID>_Findings.csv` for each CAT
- `Review_Findings.csv`
- `Review_Evidence_Bundle.md`
- `Review_Report.md`
- `Reconciliation_Findings.csv` or `Reconciliation_Report.md`
- `Review_Disposition.csv`

If review-substrate tools are available, also write:

- `Section_Coverage.csv`
- `Draft_Claims.csv`
- `TBD_Inventory.csv`
- `Body_Thinness.csv`
- `Evidence_Bundle_Summary.md`

## Subagent Guidance

If same-model subagents are available and the human authorizes parallel execution, use them for CAT reviewers. Do not degrade models for CAT review, aggregation, or reconciliation. Each CAT reviewer must have a bounded brief naming its CAT, read scope, write scope, and finding schema.

If subagents are not available, run the same topology sequentially.

## Guardrails

- The human draft is candidate content, not authority.
- The old pre-authoring concordance register is not the review checklist.
- Tools, when available, only prepare review substrate. They do not decide adequacy, materiality, or acceptance.
- Agents prepare candidate findings with rationale and evidence.
- Humans disposition findings and authorize any downstream updates.
- Cross-CAT issues are labelled and handed to RECONCILIATION, not resolved independently by a CAT reviewer.
