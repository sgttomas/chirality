# Gate 3 Category Assignment Review Packet

Generated: 2026-06-15T02:19:06Z

## Purpose

This packet summarizes the Gate 3 assignment refinement. It is a review aid, not an acceptance record.

## Current Counts

- Original ambiguous assignment findings: 881
- Open ambiguous assignment findings: 0
- Resolved forced decisions: 881
- Assignment changes applied to draft ledger: 87
- Atom splits: 0

## Category Summary

| CategoryID | Category | Resolved findings | Changed assignments | Top source docs |
|---|---|---:|---:|---|
| `CAT-001` | Epistemic and Professional-Practice Foundations | 135 | 3 | SRC-DOCS-THESIS-06-PROFESSIONAL-PRACTICE:29; SRC-AGENTS-AGENT-AUDIT-EPISTEMIC:28; SRC-DOCS-THESIS-APPENDIX-C-APEGA-MAPPING:19; SRC-DOCS-THESIS-02-LITERATURE-REVIEW:17; SRC-DOCS-THESIS-03-PHILOSOPHICAL-FRAMEWORK:11; SRC-PROFESSIONAL-ENGINEERING:8 |
| `CAT-002` | Governance and Agent Instruction Architecture | 25 | 1 | SRC-AGENTS-AGENT-DECOMP-BASE:6; SRC-AGENTS:2; SRC-AGENTS-AGENT-AUDIT-GOVERNANCE:2; SRC-AGENTS-AGENT-DOMAIN-HYPERGRAPH:2; SRC-PROFESSIONAL-ENGINEERING:1; SRC-AGENTS-AGENT-AUDIT-DECOMP:1 |
| `CAT-003` | Decomposition Lifecycle and Domain Structuring | 206 | 30 | SRC-AGENTS-AGENT-AUDIT-DECOMP:30; SRC-SKILLPACK-DEPENDENCY-EXTRACT:25; SRC-SKILLPACK-DOMAIN-SOURCE-ATOMIZE:19; SRC-SKILLPACK-ESTIMATE-SNAPSHOT:19; SRC-AGENTS-AGENT-DOMAIN-DECOMP:16; SRC-AGENTS-AGENT-ORCHESTRATOR:16 |
| `CAT-004` | Task, Skill, and Tool Execution Contracts | 107 | 16 | SRC-SKILLPACK-DBM-DRAFT-REVIEW:15; SRC-SKILLPACK-DELIVERABLE-CONSISTENCY:14; SRC-SKILLPACK-ESTIMATE-SNAPSHOT:9; SRC-SKILLPACK-DEPENDENCY-EXTRACT:8; SRC-SKILLPACK-DRAWING-TITLEBLOCK-PAGE:8; SRC-SKILLPACK-LENS-REGISTER:7 |
| `CAT-005` | Source Fidelity, Retrieval, and Validation Infrastructure | 22 | 0 | SRC-SKILLPACK-DOMAIN-SOURCE-ATOMIZE:7; SRC-SKILLPACK-ESTIMATE-SNAPSHOT:6; SRC-SKILLPACK-DEPENDENCY-EXTRACT:4; SRC-AGENTS-AGENT-DOMAIN-DECOMP:2; SRC-DOCS-THESIS-BIGGER-PICTURE-CHIRALITY-PRD-AMENDMENT-DOMAIN-ENGINE-INTEGRATION:2; SRC-TOOLS-REGISTRY:1 |
| `CAT-006` | Audit, Review, Reconciliation, and Evaluation | 174 | 4 | SRC-AGENTS-AGENT-AUDIT-GOVERNANCE:34; SRC-AGENTS-AGENT-AUDIT-DECOMP:31; SRC-AGENTS-AGENT-EQUATION-AUDIT:31; SRC-AGENTS-AGENT-AUDIT-EPISTEMIC:12; SRC-AGENTS-AGENT-EVALUATION:8; SRC-DOCS-THESIS-APPENDIX-C-APEGA-MAPPING:5 |
| `CAT-007` | Publication, Aggregation, Hypergraph, and Synthesis | 88 | 0 | SRC-SKILLPACK-DBM-DRAFT-REVIEW:64; SRC-AGENTS-AGENT-DOMAIN-HYPERGRAPH:8; SRC-AGENTS-AGENT-AGGREGATION:4; SRC-SKILLPACK-DECOMPOSITION-PACKAGE-REVIEW:3; SRC-AGENTS-AGENT-DBM-PUBLISHER:1; SRC-AGENTS-AGENT-ORCHESTRATOR:1 |
| `CAT-008` | Document, Asset, Drawing, and Engineering-Data Extraction | 77 | 14 | SRC-SKILLPACK-DEPENDENCY-EXTRACT:22; SRC-AGENTS-AGENT-EQUATION-AUDIT:15; SRC-SKILLPACK-EQUATION-FLAG-INTERPRET:8; SRC-AGENTS-AGENT-PDF2MD:4; SRC-SKILLPACK-ESTIMATE-SNAPSHOT:4; SRC-AGENTS-AGENT-DOMAIN-DECOMP:2 |
| `CAT-009` | Coordination, Change, Scheduling, and Deliverable Workflows | 30 | 0 | SRC-AGENTS-AGENT-ORCHESTRATOR:11; SRC-AGENTS-AGENT-RECONCILIATION:3; SRC-SKILLPACK-ESTIMATE-SNAPSHOT:3; SRC-AGENTS-AGENT-REVIEW:2; SRC-DOCS-THESIS-06-PROFESSIONAL-PRACTICE:2; SRC-AGENTS:1 |
| `CAT-010` | Work-Surface, Project, Product, and Integration Boundaries | 17 | 19 | SRC-DOCS-THESIS-BIGGER-PICTURE-CHIRALITY-OPENPIPESTRESS-BIGGER-PICTURE-DEVELOPMENT-PLAN:8; SRC-WSR-DOMAINS-CHIRALITY:3; SRC-EXPORTS-CHIRALITY-APP-EXPORT-REPORT:2; SRC-README:1; SRC-AGENTS-AGENT-DOMAIN-ENGINE:1; SRC-DOCS-THESIS-BIGGER-PICTURE-CHIRALITY-PRD-AMENDMENT-DOMAIN-ENGINE-INTEGRATION:1 |
| `CAT-011` | Legal, License, and Public-Release Boundaries | 0 | 0 |  |

## Boundary Decisions

- `G3BR-001` Primary-function routing: Assign by the atom's principal function, not every keyword it touches.
- `G3BR-002` Normative governance boundary: Agent architecture, authority, precedence, invariants, and governance grammar route to CAT-002; specific agent procedures route to their operational category.
- `G3BR-003` Decomposition boundary: Decomposition lifecycle, atomization, ledgers, KTY/category/subject assignment, and scope-change remediation planning route to CAT-003.
- `G3BR-004` Generic execution contract boundary: Generic TASK, skill metadata, brief-schema, runtime override, and tool-policy content routes to CAT-004; domain-specific operations route to the domain operation category.
- `G3BR-005` Extraction boundary: Transcription, extraction, crops, bboxes, drawings, assets, equations, equipment, and estimates route to CAT-008; independent review of those outputs routes to CAT-006.
- `G3BR-006` Audit/review boundary: Independent checks, findings, verdicts, QA, closure, review gates, and evaluation route to CAT-006 even when the checked object belongs elsewhere.
- `G3BR-007` Publication/synthesis boundary: DBM, aggregation, hypergraph, concordance, semantic matrix, and publication packages route to CAT-007; upstream decomposition truth and independent review do not.
- `G3BR-008` Work-surface boundary: Repository topology, domains/, projects/, exports, Domain Engine, OpenPipeStress, profile artifacts, and protected paths route to CAT-010 unless explicitly legal/license text.
- `G3BR-009` Narrow source-fidelity boundary: CAT-005 is limited to SourceRefs, ContentHash, manifests, source catalogs, indexes, chunks, retrieval, anchors, hashes, telemetry, and reproducibility.
- `G3BR-010` Narrow legal/license boundary: CAT-011 is limited to LICENSE, MIT permissions, copyright, warranty, liability, public legal notices, and explicit license-clause atoms.
- `G3BR-011` No atom splits in this refinement: Existing ambiguous findings are resolved as forced category decisions; UnitStatement text and ContentHash values are unchanged.
- `G3BR-012` Dense threshold remains human-gated: The default 0.75 cosine threshold remains recorded; any calibrated dense basis requires explicit human approval before Gate 3 closure.

## Changed Assignment Samples

- `HBA-RT002-00023` `CAT-005` -> `CAT-001` by `G3BR-007`: Epistemic retrieval concept is professional/epistemic foundation.
- `HBA-HX011-00012` `CAT-001` -> `CAT-010` by `G3BR-008`: Export reports describe public/product work-surface topology.
- `HBA-RT007-00034` `CAT-005` -> `CAT-010` by `G3BR-008`: README export rows describe public/product boundary.
- `HBA-RT007-00082` `CAT-005` -> `CAT-010` by `G3BR-008`: README export rows describe public/product boundary.
- `HBA-RT007-00094` `CAT-003` -> `CAT-010` by `G3BR-008`: domains/projects/work-surface topology routes to CAT-010.
- `HBA-RT007-00120` `CAT-005` -> `CAT-010` by `G3BR-008`: README export rows describe public/product boundary.
- `HBA-RT007-00131` `CAT-005` -> `CAT-010` by `G3BR-008`: README export rows describe public/product boundary.
- `HBA-TL001-00003` `CAT-005` -> `CAT-004` by `G3BR-004`: Generic deterministic tool mechanics route to CAT-004.
- `HBA-TL001-00005` `CAT-005` -> `CAT-004` by `G3BR-004`: Generic deterministic tool mechanics route to CAT-004.
- `HBA-TL001-00006` `CAT-005` -> `CAT-004` by `G3BR-004`: Generic deterministic tool mechanics route to CAT-004.
- `HBA-TL001-00007` `CAT-005` -> `CAT-004` by `G3BR-004`: Generic deterministic tool mechanics route to CAT-004.
- `HBA-TL001-00008` `CAT-005` -> `CAT-004` by `G3BR-004`: Generic deterministic tool mechanics route to CAT-004.
- `HBA-TL001-00011` `CAT-005` -> `CAT-004` by `G3BR-004`: Generic deterministic tool mechanics route to CAT-004.
- `HBA-TL001-00012` `CAT-005` -> `CAT-004` by `G3BR-004`: Generic deterministic tool mechanics route to CAT-004.
- `HBA-TL001-00013` `CAT-005` -> `CAT-004` by `G3BR-004`: Generic deterministic tool mechanics route to CAT-004.
- `HBA-TL001-00032` `CAT-005` -> `CAT-008` by `G3BR-005`: Extraction mechanics route to CAT-008.
- `HBA-TL001-00033` `CAT-005` -> `CAT-008` by `G3BR-005`: Extraction mechanics route to CAT-008.
- `HBA-TL001-00039` `CAT-005` -> `CAT-008` by `G3BR-005`: Extraction mechanics route to CAT-008.
- `HBA-TL001-00042` `CAT-005` -> `CAT-008` by `G3BR-005`: Extraction mechanics route to CAT-008.
- `HBA-TL001-00045` `CAT-005` -> `CAT-008` by `G3BR-005`: Extraction mechanics route to CAT-008.
- `HBA-TL001-00050` `CAT-005` -> `CAT-004` by `G3BR-004`: Generic deterministic tool mechanics route to CAT-004.
- `HBA-TL001-00065` `CAT-005` -> `CAT-004` by `G3BR-004`: Generic deterministic tool mechanics route to CAT-004.
- `HBA-TL001-00079` `CAT-005` -> `CAT-008` by `G3BR-005`: Extraction mechanics route to CAT-008.
- `HBA-TL001-00081` `CAT-005` -> `CAT-008` by `G3BR-005`: Extraction mechanics route to CAT-008.
- `HBA-TL001-00105` `CAT-005` -> `CAT-004` by `G3BR-004`: Generic deterministic tool mechanics route to CAT-004.
- `HBA-TL001-00122` `CAT-005` -> `CAT-008` by `G3BR-005`: Extraction mechanics route to CAT-008.
- `HBA-TL001-00133` `CAT-005` -> `CAT-004` by `G3BR-004`: Generic deterministic tool mechanics route to CAT-004.
- `HBA-TL001-00136` `CAT-005` -> `CAT-004` by `G3BR-004`: Generic deterministic tool mechanics route to CAT-004.
- `HBA-TL001-00148` `CAT-005` -> `CAT-008` by `G3BR-005`: Extraction mechanics route to CAT-008.
- `HBA-TL001-00153` `CAT-005` -> `CAT-004` by `G3BR-004`: Generic deterministic tool mechanics route to CAT-004.
- `HBA-TL001-00156` `CAT-005` -> `CAT-004` by `G3BR-004`: Generic deterministic tool mechanics route to CAT-004.
- `HBA-TL001-00160` `CAT-005` -> `CAT-004` by `G3BR-004`: Generic deterministic tool mechanics route to CAT-004.
- `HBA-AG015-00075` `CAT-005` -> `CAT-010` by `G3BR-008`: Domain-engine artifact/profile rows define integration boundaries.
- `HBA-AG015-00092` `CAT-005` -> `CAT-010` by `G3BR-008`: Domain-engine artifact/profile rows define integration boundaries.
- `HBA-AG015-00099` `CAT-005` -> `CAT-010` by `G3BR-008`: Domain-engine artifact/profile rows define integration boundaries.
- `HBA-AG015-00101` `CAT-005` -> `CAT-010` by `G3BR-008`: Domain-engine artifact/profile rows define integration boundaries.
- `HBA-AG015-00126` `CAT-005` -> `CAT-010` by `G3BR-008`: Domain-engine artifact/profile rows define integration boundaries.
- `HBA-AG015-00127` `CAT-005` -> `CAT-010` by `G3BR-008`: Domain-engine artifact/profile rows define integration boundaries.
- `HBA-AG015-00200` `CAT-005` -> `CAT-010` by `G3BR-008`: Domain-engine artifact/profile rows define integration boundaries.
- `HBA-AG015-00249` `CAT-011` -> `CAT-010` by `G3BR-008`: Permission/profile/workspace atom is a boundary topic, not license law.
- `HBA-AG015-00282` `CAT-011` -> `CAT-010` by `G3BR-008`: Permission/profile/workspace atom is a boundary topic, not license law.
- `HBA-AG015-00309` `CAT-005` -> `CAT-010` by `G3BR-008`: Domain-engine artifact/profile rows define integration boundaries.
- `HBA-AG015-00369` `CAT-005` -> `CAT-010` by `G3BR-008`: Domain-engine artifact/profile rows define integration boundaries.
- `HBA-AG015-00379` `CAT-005` -> `CAT-010` by `G3BR-008`: Domain-engine artifact/profile rows define integration boundaries.
- `HBA-AG023-00037` `CAT-011` -> `CAT-001` by `G3BR-010`: Professional/legal-risk foundation is not an explicit license term.
- `HBA-AG032-00235` `CAT-005` -> `CAT-003` by `G3BR-003`: KTY remediation manifests are decomposition/scope-change machinery.
- `HBA-AG032-00236` `CAT-005` -> `CAT-003` by `G3BR-003`: KTY remediation manifests are decomposition/scope-change machinery.
- `HBA-AG032-00237` `CAT-005` -> `CAT-003` by `G3BR-003`: KTY remediation manifests are decomposition/scope-change machinery.
- `HBA-AG032-00238` `CAT-005` -> `CAT-003` by `G3BR-003`: KTY remediation manifests are decomposition/scope-change machinery.
- `HBA-AG032-00239` `CAT-005` -> `CAT-003` by `G3BR-003`: KTY remediation manifests are decomposition/scope-change machinery.
