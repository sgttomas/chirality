# Gate 5 Coverage Review Packet

Generated UTC: 2026-06-17T15:36:53Z

Status: Gate 5 is OPEN pending human section-coverage attestation.

## Upstream Basis

- Gate 4 accepted snapshot: `domains/chirality/_Decomposition/gate_snapshots/GATE4_KTY_20260615T042414Z`
- Accepted KTY ledger: `domains/chirality/_Decomposition/Domain_Ledger_Gate4_KTY_Draft.csv`
- Accepted source-unit authority: `domains/chirality/_Decomposition/Gate2_Source_Unit_Register.csv`

## Review Surfaces

- Gate 5 package: `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260617T153653Z/`
- Coverage review HTML root: `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260617T153653Z/coverage_review_html/`
- Section coverage register: `domains/chirality/_Decomposition/Section_Coverage_Register.csv`
- Source coverage summary: `domains/chirality/_Decomposition/Source_Coverage_Summary.csv`

## Telemetry

| Metric | Value |
|---|---:|
| UnitCount | 21912 |
| INUnitCount | 21256 |
| OUTUnitCount | 147 |
| TBDUnitCount | 509 |
| SourceCount | 158 |
| SectionCount | 5035 |
| InScopeSectionCount | 5035 |
| SectionsWithZeroCoverageCount | 1402 |
| CategoryCount | 30 |
| KnowledgeTypeCount | 98 |
| SubjectCount | 630 |
| UnassignedINUnits | 0 |
| UnitsWithoutKnowledgeTypeMapping | 0 |

Coverage density distribution is computed over in-scope sections using IN atoms per roughly 50 source lines.

| Coverage class | Sections |
|---|---:|
| `cov-empty` | 1402 |
| `cov-low` | 3 |
| `cov-mid` | 875 |
| `cov-high` | 2755 |

## Zero-Coverage Review

`OI-024` remains open until the human attests zero-coverage sections as scaffold-for-fill/boilerplate or routes affected source units back to Phase 2 re-dispatch.

| SourceDocID | Zero sections | In-scope sections | Review HTML |
|---|---:|---:|---|
| `SRC-CODE-VALIDATION` | 120 | 308 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260617T153653Z/coverage_review_html/SRC-CODE-VALIDATION.html` |
| `SRC-DOCS-SCOPECHANGE-OPENPIPESTRESS-PRD-V0-2` | 22 | 145 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260617T153653Z/coverage_review_html/SRC-DOCS-SCOPECHANGE-OPENPIPESTRESS-PRD-V0-2.html` |
| `SRC-CODE-CORE` | 21 | 239 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260617T153653Z/coverage_review_html/SRC-CODE-CORE.html` |
| `SRC-DOCS-PRD` | 21 | 111 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260617T153653Z/coverage_review_html/SRC-DOCS-PRD.html` |
| `SRC-DOCS-SCOPECHANGE-OPENPIPESTRESS-PRD-V0-2-SCOPE-CHANGE-BRIEF` | 21 | 93 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260617T153653Z/coverage_review_html/SRC-DOCS-SCOPECHANGE-OPENPIPESTRESS-PRD-V0-2-SCOPE-CHANGE-BRIEF.html` |
| `SRC-DEL-DEL-05-03-FUNDAMENTAL-STRESS-RECOVERY-MODULE` | 19 | 32 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260617T153653Z/coverage_review_html/SRC-DEL-DEL-05-03-FUNDAMENTAL-STRESS-RECOVERY-MODULE.html` |
| `SRC-DEL-DEL-13-04-PHYSICAL-TO-ANALYTICAL-TRANSFORMATION-CONTRACT` | 16 | 45 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260617T153653Z/coverage_review_html/SRC-DEL-DEL-13-04-PHYSICAL-TO-ANALYTICAL-TRANSFORMATION-CONTRACT.html` |
| `SRC-DEL-DEL-07-03-MATERIAL-COMPONENT-AND-RULE-PACK-EDITORS` | 15 | 35 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260617T153653Z/coverage_review_html/SRC-DEL-DEL-07-03-MATERIAL-COMPONENT-AND-RULE-PACK-EDITORS.html` |
| `SRC-DEL-DEL-10-04-BUILD-PACKAGING-AND-CI-CD-PIPELINE` | 15 | 33 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260617T153653Z/coverage_review_html/SRC-DEL-DEL-10-04-BUILD-PACKAGING-AND-CI-CD-PIPELINE.html` |
| `SRC-DEL-DEL-12-02-PRIVATE-DATA-REDACTION-AND-EXPORT-CONTROLS` | 15 | 40 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260617T153653Z/coverage_review_html/SRC-DEL-DEL-12-02-PRIVATE-DATA-REDACTION-AND-EXPORT-CONTROLS.html` |
| `SRC-DEL-DEL-02-02-UNIT-SYSTEM-AND-DIMENSIONAL-ANALYSIS-CORE-CONTRACT` | 14 | 37 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260617T153653Z/coverage_review_html/SRC-DEL-DEL-02-02-UNIT-SYSTEM-AND-DIMENSIONAL-ANALYSIS-CORE-CONTRACT.html` |
| `SRC-DEL-DEL-03-05-RIGID-COMPONENT-MODELS-FOR-VALVES-FLANGES-REDUCERS-AND-SPECIALTY-ITEMS` | 14 | 31 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260617T153653Z/coverage_review_html/SRC-DEL-DEL-03-05-RIGID-COMPONENT-MODELS-FOR-VALVES-FLANGES-REDUCERS-AND-SPECIALTY-ITEMS.html` |
| `SRC-DEL-DEL-05-04-ANALYSIS-STATUS-SEMANTICS` | 14 | 35 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260617T153653Z/coverage_review_html/SRC-DEL-DEL-05-04-ANALYSIS-STATUS-SEMANTICS.html` |
| `SRC-DEL-DEL-07-06-ACCESSIBILITY-AND-USABILITY-BASELINE` | 14 | 32 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260617T153653Z/coverage_review_html/SRC-DEL-DEL-07-06-ACCESSIBILITY-AND-USABILITY-BASELINE.html` |
| `SRC-DEL-DEL-12-05-SECURITY-THREAT-MODEL` | 14 | 40 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260617T153653Z/coverage_review_html/SRC-DEL-DEL-12-05-SECURITY-THREAT-MODEL.html` |
| `SRC-DEL-DEL-17-09-EXPORT-ADAPTER-SDK-AND-ADDITIONAL-TARGETS` | 14 | 41 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260617T153653Z/coverage_review_html/SRC-DEL-DEL-17-09-EXPORT-ADAPTER-SDK-AND-ADDITIONAL-TARGETS.html` |
| `SRC-DEL-DEL-01-03-CONTRIBUTOR-CERTIFICATION-WORKFLOW` | 13 | 36 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260617T153653Z/coverage_review_html/SRC-DEL-DEL-01-03-CONTRIBUTOR-CERTIFICATION-WORKFLOW.html` |
| `SRC-DEL-DEL-03-03-BEND-AND-ELBOW-COMPONENT-MODEL-FIELDS` | 13 | 30 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260617T153653Z/coverage_review_html/SRC-DEL-DEL-03-03-BEND-AND-ELBOW-COMPONENT-MODEL-FIELDS.html` |
| `SRC-DEL-DEL-04-06-SOLVER-DIAGNOSTICS-AND-SINGULARITY-DETECTION` | 13 | 34 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260617T153653Z/coverage_review_html/SRC-DEL-DEL-04-06-SOLVER-DIAGNOSTICS-AND-SINGULARITY-DETECTION.html` |
| `SRC-DEL-DEL-06-02-SANDBOXED-UNIT-AWARE-EXPRESSION-EVALUATOR` | 13 | 32 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260617T153653Z/coverage_review_html/SRC-DEL-DEL-06-02-SANDBOXED-UNIT-AWARE-EXPRESSION-EVALUATOR.html` |

## Gate 5 Closure Condition

Gate 5 cannot close until the human explicitly confirms: Coverage and mappings are acceptable; section-coverage gaps have been ruled on as scaffold-for-fill/boilerplate or routed back for Phase 2 re-dispatch; open issues list is correct.
