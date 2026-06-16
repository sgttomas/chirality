# Gate 5 Coverage Review Packet

Generated UTC: 2026-06-16T16:26:57Z

Status: Gate 5 is OPEN pending human section-coverage attestation.

## Upstream Basis

- Gate 4 accepted snapshot: `domains/chirality/_Decomposition/gate_snapshots/GATE4_KTY_20260615T042414Z`
- Accepted KTY ledger: `domains/chirality/_Decomposition/Domain_Ledger_Gate4_KTY_Draft.csv`
- Accepted source-unit authority: `domains/chirality/_Decomposition/Gate2_Source_Unit_Register.csv`

## Review Surfaces

- Gate 5 package: `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260616T162657Z/`
- Coverage review HTML root: `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260616T162657Z/coverage_review_html/`
- Section coverage register: `domains/chirality/_Decomposition/Section_Coverage_Register.csv`
- Source coverage summary: `domains/chirality/_Decomposition/Source_Coverage_Summary.csv`

## Telemetry

| Metric | Value |
|---|---:|
| UnitCount | 11809 |
| INUnitCount | 11140 |
| OUTUnitCount | 107 |
| TBDUnitCount | 562 |
| SourceCount | 92 |
| SectionCount | 3046 |
| InScopeSectionCount | 3046 |
| SectionsWithZeroCoverageCount | 987 |
| CategoryCount | 16 |
| KnowledgeTypeCount | 59 |
| SubjectCount | 279 |
| UnassignedINUnits | 0 |
| UnitsWithoutKnowledgeTypeMapping | 0 |

Coverage density distribution is computed over in-scope sections using IN atoms per roughly 50 source lines.

| Coverage class | Sections |
|---|---:|
| `cov-empty` | 987 |
| `cov-low` | 2 |
| `cov-mid` | 381 |
| `cov-high` | 1676 |

## Zero-Coverage Review

`OI-024` remains open until the human attests zero-coverage sections as scaffold-for-fill/boilerplate or routes affected source units back to Phase 2 re-dispatch.

| SourceDocID | Zero sections | In-scope sections | Review HTML |
|---|---:|---:|---|
| `SRC-DEL-DEL-00-02-SCC-001-RUNTIME-SDK-SESSION-TOOLING-CLOSURE` | 109 | 165 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260616T162657Z/coverage_review_html/SRC-DEL-DEL-00-02-SCC-001-RUNTIME-SDK-SESSION-TOOLING-CLOSURE.html` |
| `SRC-DEL-DEL-00-01-SCC-002-PKG-10-POLICY-PROPOSAL-CLOSURE` | 36 | 83 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260616T162657Z/coverage_review_html/SRC-DEL-DEL-00-01-SCC-002-PKG-10-POLICY-PROPOSAL-CLOSURE.html` |
| `SRC-DOCS-SPEC` | 28 | 91 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260616T162657Z/coverage_review_html/SRC-DOCS-SPEC.html` |
| `SRC-FRONTEND-SRC` | 25 | 201 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260616T162657Z/coverage_review_html/SRC-FRONTEND-SRC.html` |
| `SRC-DEL-DEL-10-04-DOMAIN-PROFILE-VALIDATION-AND-OPENPIPESTRESS-FIXTURE` | 19 | 34 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260616T162657Z/coverage_review_html/SRC-DEL-DEL-10-04-DOMAIN-PROFILE-VALIDATION-AND-OPENPIPESTRESS-FIXTURE.html` |
| `SRC-DEL-DEL-06-03-INITIAL-CHIRALITY-MCP-READ-TOOLS` | 18 | 39 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260616T162657Z/coverage_review_html/SRC-DEL-DEL-06-03-INITIAL-CHIRALITY-MCP-READ-TOOLS.html` |
| `SRC-DEL-DEL-07-01-WORKING-ROOT-VALIDATION-AND-INSTRUCTION-ROOT-PROTECTION` | 18 | 36 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260616T162657Z/coverage_review_html/SRC-DEL-DEL-07-01-WORKING-ROOT-VALIDATION-AND-INSTRUCTION-ROOT-PROTECTION.html` |
| `SRC-DEL-DEL-07-06-REFERENCE-HASH-AND-SNAPSHOT-CONVENTIONS` | 18 | 34 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260616T162657Z/coverage_review_html/SRC-DEL-DEL-07-06-REFERENCE-HASH-AND-SNAPSHOT-CONVENTIONS.html` |
| `SRC-DEL-DEL-08-03-PIPELINE-CATEGORY-AND-TASK-SCOPE-DISPATCH` | 18 | 40 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260616T162657Z/coverage_review_html/SRC-DEL-DEL-08-03-PIPELINE-CATEGORY-AND-TASK-SCOPE-DISPATCH.html` |
| `SRC-DEL-DEL-09-06-NETWORK-KEY-ATTACHMENT-AND-RENDERER-SECURITY-CHECKS` | 18 | 34 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260616T162657Z/coverage_review_html/SRC-DEL-DEL-09-06-NETWORK-KEY-ATTACHMENT-AND-RENDERER-SECURITY-CHECKS.html` |
| `SRC-DEL-DEL-01-02-RELIANCE-BOUNDARY-REGISTER` | 17 | 61 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260616T162657Z/coverage_review_html/SRC-DEL-DEL-01-02-RELIANCE-BOUNDARY-REGISTER.html` |
| `SRC-DEL-DEL-04-05-ANTHROPIC-PROVIDER-KEY-BASE-URL-AND-NETWORK-BRIDGE` | 17 | 40 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260616T162657Z/coverage_review_html/SRC-DEL-DEL-04-05-ANTHROPIC-PROVIDER-KEY-BASE-URL-AND-NETWORK-BRIDGE.html` |
| `SRC-DEL-DEL-07-05-DEPENDENCIES-CSV-V3-1-READER-WRITER-AND-LINTER` | 16 | 39 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260616T162657Z/coverage_review_html/SRC-DEL-DEL-07-05-DEPENDENCIES-CSV-V3-1-READER-WRITER-AND-LINTER.html` |
| `SRC-DEL-DEL-05-01-CANONICAL-SESSION-FOLDER-AND-LEGACY-SESSION-MIGRATION` | 15 | 34 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260616T162657Z/coverage_review_html/SRC-DEL-DEL-05-01-CANONICAL-SESSION-FOLDER-AND-LEGACY-SESSION-MIGRATION.html` |
| `SRC-DEL-DEL-07-04-STATUS-TRANSITION-API-AND-MCP-TOOL` | 15 | 37 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260616T162657Z/coverage_review_html/SRC-DEL-DEL-07-04-STATUS-TRANSITION-API-AND-MCP-TOOL.html` |
| `SRC-DEL-DEL-10-01-DOMAINENGINEPROFILE-CONTRACT-DRAFT` | 15 | 35 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260616T162657Z/coverage_review_html/SRC-DEL-DEL-10-01-DOMAINENGINEPROFILE-CONTRACT-DRAFT.html` |
| `SRC-DEL-DEL-02-03-WORKING-ROOT-FILE-TREE-AND-SCOPE-SCAN-UI` | 14 | 34 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260616T162657Z/coverage_review_html/SRC-DEL-DEL-02-03-WORKING-ROOT-FILE-TREE-AND-SCOPE-SCAN-UI.html` |
| `SRC-DEL-DEL-02-04-TOOLKIT-OPTIONS-AND-LOCAL-UI-STATE` | 14 | 32 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260616T162657Z/coverage_review_html/SRC-DEL-DEL-02-04-TOOLKIT-OPTIONS-AND-LOCAL-UI-STATE.html` |
| `SRC-DEL-DEL-04-01-SDK-PROBE-AND-VERSION-PINNED-ADOPTION-DECISION` | 14 | 32 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260616T162657Z/coverage_review_html/SRC-DEL-DEL-04-01-SDK-PROBE-AND-VERSION-PINNED-ADOPTION-DECISION.html` |
| `SRC-DEL-DEL-07-02-EXECUTION-ROOT-SCAFFOLDING-FROM-DECOMPOSITION` | 14 | 36 | `domains/chirality/_Decomposition/gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260616T162657Z/coverage_review_html/SRC-DEL-DEL-07-02-EXECUTION-ROOT-SCAFFOLDING-FROM-DECOMPOSITION.html` |

## Gate 5 Closure Condition

Gate 5 cannot close until the human explicitly confirms: Coverage and mappings are acceptable; section-coverage gaps have been ruled on as scaffold-for-fill/boilerplate or routed back for Phase 2 re-dispatch; open issues list is correct.
