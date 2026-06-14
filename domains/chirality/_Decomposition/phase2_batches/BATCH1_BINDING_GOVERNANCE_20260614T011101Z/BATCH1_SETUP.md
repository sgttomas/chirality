# Batch 1 Setup - Binding Governance Seed

Package role: snapshot / handoff artifact

BatchID: `BATCH1_BINDING_GOVERNANCE_20260614T011101Z`

Status: SETUP_READY

Generated UTC: 2026-06-14T01:12:37Z

## Accepted Upstream Snapshot

- Gate 1 acceptance snapshot: `domains/chirality/_Decomposition/gate_snapshots/GATE1_20260614T005942Z`
- Source manifest: `domains/chirality/_Sources/Source_Manifest.csv`
- Source manifest SHA-256: `f072b1d43eb98b057cdb392a674bc9e7feaffbe483c7f59a06f5557219762fb1`
- Source catalog snapshot: `domains/chirality/_LocalIndexes/snapshots/SRCIDX_20260614T005449Z`
- Retrieval status: `BM25_ONLY`
- Source-copy policy: `source_files_copied=false`

## Scope

Batch 1 is a staged Phase 2 setup package for binding-governance sources. It includes root authority docs except deferred `SRC-LICENSE`, all top-level `docs/*.md` governance files, the skill registry/template docs, tool registry docs, and the two public export package docs named by the readiness handoff.

| SourceDocID | Prefix | RepoRelPath | Dispatch Units |
|---|---|---|---:|
| `SRC-AGENTS` | `RT001` | `AGENTS.md` | 1 |
| `SRC-CHIRALITY-FRAMEWORK` | `RT002` | `CHIRALITY_FRAMEWORK.md` | 1 |
| `SRC-CLAUDE` | `RT003` | `CLAUDE.md` | 1 |
| `SRC-INIT` | `RT004` | `init/INIT.md` | 1 |
| `SRC-PROFESSIONAL-ENGINEERING` | `RT006` | `PROFESSIONAL_ENGINEERING.md` | 1 |
| `SRC-README` | `RT007` | `README.md` | 1 |
| `SRC-DOCS-CONTRACT` | `DG001` | `docs/CONTRACT.md` | 1 |
| `SRC-DOCS-DBM-AGENT-INSTRUCTION-ARCHITECTURE` | `DG002` | `docs/DBM_Agent_Instruction_Architecture.md` | 1 |
| `SRC-DOCS-DIRECTIVE` | `DG003` | `docs/DIRECTIVE.md` | 1 |
| `SRC-DOCS-PLAN` | `DG004` | `docs/PLAN.md` | 1 |
| `SRC-DOCS-PRD-CANDIDATE` | `DG005` | `docs/PRD_CANDIDATE.md` | 1 |
| `SRC-DOCS-SE-DESIGN-ANALYSIS` | `DG006` | `docs/SE_Design_Analysis.md` | 1 |
| `SRC-DOCS-SPEC` | `DG007` | `docs/SPEC.md` | 1 |
| `SRC-DOCS-TYPES` | `DG008` | `docs/TYPES.md` | 1 |
| `SRC-DOCS-WHAT-IS-AN-AGENT` | `DG009` | `docs/WHAT-IS-AN-AGENT.md` | 1 |
| `SRC-SKILLS-README` | `SK001` | `skills/README.md` | 1 |
| `SRC-SKILLS-SKILL-TEMPLATE` | `SK002` | `skills/SKILL_TEMPLATE.md` | 1 |
| `SRC-TOOLS-REGISTRY` | `TL001` | `tools/REGISTRY.md` | 1 |
| `SRC-TOOLS-EXTERNAL-TOOLS` | `TL002` | `tools/EXTERNAL_TOOLS.md` | 1 |
| `SRC-TOOLS-RETRIEVAL-README` | `TL003` | `tools/retrieval/README.md` | 1 |
| `SRC-EXPORTS-CHIRALITY-APP-README` | `HX010` | `exports/chirality-app/README.md` | 1 |
| `SRC-EXPORTS-CHIRALITY-APP-EXPORT-REPORT` | `HX011` | `exports/chirality-app/export-report.md` | 1 |

## Generated Companions

- `Batch_Source_Register.csv` - authoritative companion register for selected source scope.
- `Dispatch_Unit_Register.csv` - authoritative companion register for per-unit brief/output paths.
- `Validation_Checks.csv` - setup validation register.
- `domains/chirality/_Decomposition/dispatch_briefs/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/` - one INIT-TASK brief per dispatch unit.
- `domains/chirality/_Decomposition/dispatch_outputs/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/` - prepared disjoint output directories for future worker CSVs.
- `domains/chirality/_Decomposition/per_source_ledgers/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/` - reserved per-source merge output root.
- `domains/chirality/_Decomposition/vocabulary_seeds/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/` - reserved per-source vocabulary seed output root.

## SourceRef Policy

All rendered briefs include the accepted manifest-backed runtime override:

```text
SOURCE_REF_BASE: @repo/<RepoRelPath>:L####|domains/chirality/_Decomposition/source_review_html/<SourceDocID>.html#<SectionID>
```

## Worker Boundary

No `TASK + domain-source-atomize` workers were dispatched during this setup step. Future workers must read only their assigned `LINE_START..LINE_END`, write only their two allowed CSV targets, and return a valid `RUN_STATUS`.

## Closure Verdict

- Gate 1 Intake: CLOSED / ACCEPTED, unchanged.
- Batch 1 setup: CLOSED / SETUP_READY.
- Phase 2 atomization: NOT_STARTED for this batch.
- Gate 2 normalization: NOT_OPEN.

## Rerun Requirements

- If any selected source file changes, update `Source_Manifest.csv`, rebuild the source catalog and BM25 index, regenerate Batch 0 companions, then regenerate this batch setup.
- If `tools/decomp/build_atomization_brief.py`, `Source_Decomp_Prefix_Map.csv`, or `skills/domain-source-atomize/` changes before worker fan-out, regenerate all briefs in this batch and re-run setup validation.
- After worker fan-out, update `Dispatch_Unit_Register.csv` with run status and counts before any per-source merge.

## Remaining Blockers

- Explicit authorization is still required before starting `TASK + domain-source-atomize` fan-out for Batch 1.
- Per-unit atom CSVs and vocabulary seed CSVs do not exist yet.
- Per-source ledgers, cross-source `Atomic_Domain_Ledger.csv`, `Vocabulary_Map.csv`, and Gate 2 review HTML are not produced by this setup step.
