# Deterministic Validation Result — Tandem Review Pass 1

Stage: charter step 4 (validate returns deterministically), run by the EVALUATION-role
supervising manager on 2026-07-26, before fan-in and before any reciprocal challenge.

Validator: `validation/validate_reports.py` (this directory; run with python3 against
the freeze commit `da31c19b5656dd74615e308c4215688971d33dc9`).
Raw output: `validation/validation_raw.json`.

## Checks applied

- V1 report exists and is non-empty
- V2 frontmatter carries the exact frozen basis identity (freeze commit, manifest SHA-256, charter SHA-256, reviewer, lens)
- V3 all seven required report sections present
- V4 finding blocks parse; all 12 required fields present; enums respected
- V5 FindingID format and prefix correct; unique within each report
- V6 frontmatter finding_count matches parsed findings
- V7 evidence anchors resolve at the freeze commit (path-style anchors)
- V8 coverage matrix contains all 21 product x layer rows (ROOT/APP/PEC x 7 layers)
- V9 boundary matrix contains all 9 minimum shared functions
- V10 FindingID namespaces disjoint across the two reports

## Documented leniencies (applied identically to both reports)

- L1: a boundary-matrix function is satisfied by documented aliases
  (e.g. "Work surface / human-agent mediation" satisfies "work-surface").
- L2: an enum field may carry a parenthetical epistemic qualifier after the enum
  token; the token governs, the qualifier is recorded as a warning.
- V7 scope: anchors that are validated tool output (grep censuses, recomputed
  hashes, glob summaries) rather than plain paths are permitted by the charter's
  EvidenceRefs definition; they are recorded as warnings, not failures. Spot-checks
  of plain-path anchors resolved at the freeze commit.

## Results

### Reviewer A — REVIEWER_A_PASS1_REPORT.md

- Verdict: **PASS_WITH_WARNINGS**
- Findings parsed: 26 (severity: {'REVIEW': 7, 'WARN': 11, 'INFO': 8})
- Hard issues: 0
- Warnings: 8 (of which unresolved tool-output-style anchors: 8)

Warnings (non-blocking):

- V7: A-F-002 evidence anchor does not resolve at freeze: 'execution/PKG-*/1_Working/DEL-*/ScopeOfWork.md frontmatter'
- V7: A-F-005 evidence anchor does not resolve at freeze: 'execution/PKG-01_.../DEL-01-01_.../_CONTEXT.md'
- V7: A-F-005 evidence anchor does not resolve at freeze: 'grep count: 21/45 SOWs match "ResponsibleParty. remains .TBD"'
- V7: A-F-007 evidence anchor does not resolve at freeze: 'DEL-01-01/ScopeOfWork.md'
- V7: A-F-010 evidence anchor does not resolve at freeze: 'projects/chirality-app-dev/execution/_Coordination/NOTICE_D-GOV-{21,23,24,26}*.md'
- V7: A-F-010 evidence anchor does not resolve at freeze: 'projects/pec/execution/_Coordination/ and _DomainEngines/pec/'
- V7: A-F-010 evidence anchor does not resolve at freeze: 'docs/governance_harness/_DECISIONS/D-GOV-26_owner_gated_closeout.md register row'
- V7: A-F-018 evidence anchor does not resolve at freeze: 'git log: 612c35226 "Merge pull request'

### Reviewer B — REVIEWER_B_PASS1_REPORT.md

- Verdict: **PASS_WITH_WARNINGS**
- Findings parsed: 23 (severity: {'REVIEW': 7, 'WARN': 14, 'INFO': 2})
- Hard issues: 0
- Warnings: 13 (of which unresolved tool-output-style anchors: 12)

Warnings (non-blocking):

- V7: B-F-002 evidence anchor does not resolve at freeze: 'git cat-file -t 416b29033bbacb0bc3648d84033272b7ab4e6e11 → "could not get object info"'
- V7: B-F-003 evidence anchor does not resolve at freeze: 'programmatic census of decomposition_basis across projects/chirality-app-dev/execution/PKG-*/1_Working/DEL-*/ScopeOfWork.md'
- V7: B-F-003 evidence anchor does not resolve at freeze: 'git show <pin>:…SOFTWARE_DECOMP_v3_2.md hashed at b4d2c9ab2/ff59428ff/0724f26f6/2770fda4c → a907cda33835ebf0… vs live 952d3cbf81b0…'
- V7: B-F-004 evidence anchor does not resolve at freeze: 'recomputed live sha256 of all 12 sourcePaths at da31c19b5 → 0 OK / 12 STALE'
- V7: B-F-006 evidence anchor does not resolve at freeze: 'find over projects/pec/execution/_Coordination and _DomainEngines/pec: no NOTICE_D-GOV_* file'
- V7: B-F-006 evidence anchor does not resolve at freeze: 'grep -c "NOTICE_D-GOV" projects/chirality-app-dev/loop/LOOP_RECEIPTS.md → 0'
- V7: B-F-007 evidence anchor does not resolve at freeze: 'execution/PKG-01_*/1_Working/DEL-01-01_*/ScopeOfWork.md'
- V4-L2: B-F-013 Confidence carries qualifier beyond enum token: "MEDIUM (the live consumer's current behavior with the frozen instance was not executed in this review)"
- V7: B-F-016 evidence anchor does not resolve at freeze: 'recomputed live sha256 of projects/chirality-app-dev/docs/PRD.md = ef638f43ccae…'
- V7: B-F-017 evidence anchor does not resolve at freeze: 'recomputed sha256 agents/AGENT_SOFTWARE_DECOMP.md = ad849d9a9274…'
- V7: B-F-017 evidence anchor does not resolve at freeze: "AGENTS overlays' Path Anchors sections"
- V7: B-F-018 evidence anchor does not resolve at freeze: 'programmatic grep census across the three SOW corpora'
- V7: B-F-020 evidence anchor does not resolve at freeze: 'programmatic recompute over both manifests'

### Cross-report

- FindingID namespace overlap: none

## Disposition

Both returns are ACCEPTED into the frozen pass-1 record. No return was rejected;
no reviewer was asked to revise after freezing. The two validator defects found
during validation (a frontmatter key regex unable to match digits, and a
case-sensitive enum-token regression) were validator bugs, fixed and rerun; they
implied no report defect. Reports were frozen (hashed) before this validation and
were not modified by it.
