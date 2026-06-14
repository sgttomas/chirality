# Batch 2 Setup - Agent Contracts

Package role: snapshot / handoff artifact

BatchID: `BATCH2_AGENT_CONTRACTS_20260614T032003Z`

Status: ATOMIZATION_COMPLETE_GATE2_OPEN

Generated UTC: 2026-06-14T03:20:03Z

Atomization Completed UTC: 2026-06-14T05:07:20Z

## Accepted Upstream Snapshot

- Gate 1 acceptance snapshot: `domains/chirality/_Decomposition/gate_snapshots/GATE1_20260614T005942Z`
- Gate 2 Batch 1 acceptance snapshot: `domains/chirality/_Decomposition/gate_snapshots/GATE2_BATCH1_20260614T023234Z`
- Source manifest: `domains/chirality/_Sources/Source_Manifest.csv`
- Source manifest SHA-256: `acd2fd88ff66be89b33d5cde05ab15cbcb584adea2fd25e661d9ea9eb0f64b04`
- Current source catalog snapshot: `domains/chirality/_LocalIndexes/snapshots/SRCIDX_20260614T031420Z`
- Supersedes stale setup: `domains/chirality/_Decomposition/phase2_batches/BATCH2_AGENT_CONTRACTS_20260614T024251Z/`
- Source-copy policy: `source_files_copied=false`

## Scope

This regenerated Batch 2 setup is the active Phase 2 setup package for admitted agent instruction contracts after source-boundary cleanup. It includes every current `AGENT_CONTRACTS` source with `AtomizeInV1=YES`, excludes retired `SRC-AGENTS-AGENT-DELIVERABLE-TASK` / `AG013`, and performs setup plus completed Batch 2 atomization: `TASK + domain-source-atomize` outputs exist for all 36 selected sources, merged batch-scoped ledgers were produced, and Gate 2 review is open.

| SourceDocID | Prefix | RepoRelPath | Sections | In-scope Sections | Dispatch Units |
|---|---|---|---:|---:|---:|
| `SRC-AGENTS-AGENT-AGGREGATION` | `AG001` | `agents/AGENT_AGGREGATION.md` | 24 | 24 | 1 |
| `SRC-AGENTS-AGENT-AUDIT-AGENTS` | `AG002` | `agents/AGENT_AUDIT_AGENTS.md` | 20 | 20 | 1 |
| `SRC-AGENTS-AGENT-AUDIT-DECOMP` | `AG003` | `agents/AGENT_AUDIT_DECOMP.md` | 35 | 35 | 1 |
| `SRC-AGENTS-AGENT-AUDIT-DEP-CLOSURE` | `AG004` | `agents/AGENT_AUDIT_DEP_CLOSURE.md` | 19 | 19 | 1 |
| `SRC-AGENTS-AGENT-AUDIT-EPISTEMIC` | `AG005` | `agents/AGENT_AUDIT_EPISTEMIC.md` | 50 | 50 | 1 |
| `SRC-AGENTS-AGENT-AUDIT-GOVERNANCE` | `AG006` | `agents/AGENT_AUDIT_GOVERNANCE.md` | 74 | 74 | 1 |
| `SRC-AGENTS-AGENT-AUDIT-HYPERGRAPH-CLOSURE` | `AG007` | `agents/AGENT_AUDIT_HYPERGRAPH_CLOSURE.md` | 29 | 29 | 1 |
| `SRC-AGENTS-AGENT-AUDIT-SCOPE-CLOSURE` | `AG008` | `agents/AGENT_AUDIT_SCOPE_CLOSURE.md` | 46 | 46 | 1 |
| `SRC-AGENTS-AGENT-CHANGE` | `AG009` | `agents/AGENT_CHANGE.md` | 32 | 32 | 1 |
| `SRC-AGENTS-AGENT-CONTEXT-TRANSPOSE` | `AG010` | `agents/AGENT_CONTEXT_TRANSPOSE.md` | 44 | 43 | 1 |
| `SRC-AGENTS-AGENT-DBM-PUBLISHER` | `AG011` | `agents/AGENT_DBM_PUBLISHER.md` | 32 | 32 | 1 |
| `SRC-AGENTS-AGENT-DECOMP-BASE` | `AG012` | `agents/AGENT_DECOMP_BASE.md` | 48 | 47 | 1 |
| `SRC-AGENTS-AGENT-DOMAIN-DECOMP` | `AG014` | `agents/AGENT_DOMAIN_DECOMP.md` | 53 | 53 | 1 |
| `SRC-AGENTS-AGENT-DOMAIN-ENGINE` | `AG015` | `agents/AGENT_DOMAIN_ENGINE.md` | 56 | 56 | 1 |
| `SRC-AGENTS-AGENT-DOMAIN-HYPERGRAPH` | `AG016` | `agents/AGENT_DOMAIN_HYPERGRAPH.md` | 30 | 30 | 1 |
| `SRC-AGENTS-AGENT-DRAWING-EXTRACT` | `AG017` | `agents/AGENT_DRAWING_EXTRACT.md` | 61 | 61 | 1 |
| `SRC-AGENTS-AGENT-EQUATION-AUDIT` | `AG018` | `agents/AGENT_EQUATION_AUDIT.md` | 42 | 42 | 1 |
| `SRC-AGENTS-AGENT-EVALUATION` | `AG019` | `agents/AGENT_EVALUATION.md` | 26 | 26 | 1 |
| `SRC-AGENTS-AGENT-EVALUATION-DEPENDENCY-AUDIT` | `AG020` | `agents/AGENT_EVALUATION_DEPENDENCY_AUDIT.md` | 24 | 24 | 1 |
| `SRC-AGENTS-AGENT-EVALUATION-REPORT` | `AG021` | `agents/AGENT_EVALUATION_REPORT.md` | 21 | 21 | 1 |
| `SRC-AGENTS-AGENT-EVALUATION-STRUCTURE-AUDIT` | `AG022` | `agents/AGENT_EVALUATION_STRUCTURE_AUDIT.md` | 25 | 25 | 1 |
| `SRC-AGENTS-AGENT-HELPS-HUMANS` | `AG023` | `agents/AGENT_HELPS_HUMANS.md` | 51 | 51 | 1 |
| `SRC-AGENTS-AGENT-HELP-HUMAN` | `AG024` | `agents/AGENT_HELP_HUMAN.md` | 39 | 39 | 1 |
| `SRC-AGENTS-AGENT-ORCHESTRATOR` | `AG025` | `agents/AGENT_ORCHESTRATOR.md` | 49 | 49 | 1 |
| `SRC-AGENTS-AGENT-PDF2MD` | `AG026` | `agents/AGENT_PDF2MD.md` | 42 | 42 | 1 |
| `SRC-AGENTS-AGENT-PREPARATION` | `AG027` | `agents/AGENT_PREPARATION.md` | 74 | 74 | 1 |
| `SRC-AGENTS-AGENT-PROJECT-DECOMP` | `AG028` | `agents/AGENT_PROJECT_DECOMP.md` | 39 | 39 | 1 |
| `SRC-AGENTS-AGENT-RECONCILIATION` | `AG029` | `agents/AGENT_RECONCILIATION.md` | 33 | 33 | 1 |
| `SRC-AGENTS-AGENT-REVIEW` | `AG030` | `agents/AGENT_REVIEW.md` | 37 | 37 | 1 |
| `SRC-AGENTS-AGENT-SCHEDULING` | `AG031` | `agents/AGENT_SCHEDULING.md` | 36 | 36 | 1 |
| `SRC-AGENTS-AGENT-SCOPE-CHANGE` | `AG032` | `agents/AGENT_SCOPE_CHANGE.md` | 33 | 33 | 1 |
| `SRC-AGENTS-AGENT-SKILLMAKER` | `AG033` | `agents/AGENT_SKILLMAKER.md` | 38 | 38 | 1 |
| `SRC-AGENTS-AGENT-SOFTWARE-DECOMP` | `AG034` | `agents/AGENT_SOFTWARE_DECOMP.md` | 44 | 44 | 1 |
| `SRC-AGENTS-AGENT-TASK` | `AG035` | `agents/AGENT_TASK.md` | 40 | 40 | 1 |
| `SRC-AGENTS-AGENT-TOOLMAKER` | `AG036` | `agents/AGENT_TOOLMAKER.md` | 38 | 38 | 1 |
| `SRC-AGENTS-AGENT-WORKING-ITEMS` | `AG037` | `agents/AGENT_WORKING_ITEMS.md` | 20 | 20 | 1 |

## Generated Companions

- `Batch_Source_Register.csv` - authoritative companion register for selected source scope.
- `Dispatch_Unit_Register.csv` - authoritative companion register for per-unit brief/output paths.
- `Validation_Checks.csv` - setup, worker QA, merge, render, and Gate 2 status validation register.
- `Dispatch_Run_Log.csv` - per-dispatch-unit run counts and output status.
- `BATCH2_ATOMIZATION_HANDOFF.md` - atomization completion handoff and Gate 2 open state.
- `BATCH2_Atomic_Domain_Ledger.csv` - batch-scoped merged atom ledger.
- `BATCH2_Vocabulary_Map.csv` - batch-scoped merged vocabulary map.
- `domains/chirality/_Decomposition/dispatch_briefs/BATCH2_AGENT_CONTRACTS_20260614T032003Z/` - one INIT-TASK brief per dispatch unit.
- `domains/chirality/_Decomposition/dispatch_outputs/BATCH2_AGENT_CONTRACTS_20260614T032003Z/` - prepared disjoint output directories for worker CSVs.
- `domains/chirality/_Decomposition/per_source_ledgers/BATCH2_AGENT_CONTRACTS_20260614T032003Z/` - reserved per-source merge output root.
- `domains/chirality/_Decomposition/vocabulary_seeds/BATCH2_AGENT_CONTRACTS_20260614T032003Z/` - reserved per-source vocabulary seed output root.

## SourceRef Policy

All rendered briefs include the accepted manifest-backed runtime override:

```text
SOURCE_REF_BASE: @repo/<RepoRelPath>:L####|domains/chirality/_Decomposition/source_review_html/<SourceDocID>.html#<SectionID>
```

## Worker Boundary

Workers must read only their assigned `LINE_START..LINE_END`, write only their two allowed CSV targets, and return a valid `RUN_STATUS`. Fan-out is authorized from this regenerated 36-source setup only.

## Closure Verdict

- Gate 1 Intake: PRIOR_BOUNDARY_ACCEPTED; current active boundary requires source-boundary amendment acceptance before claiming current Gate 1 closure.
- Batch 1 Gate 2: ACCEPTED_PRIOR_BOUNDARY; active reuse blocked by OI-012.
- Stale Batch 2 setup `BATCH2_AGENT_CONTRACTS_20260614T024251Z`: SUPERSEDED_STALE.
- Regenerated Batch 2 setup `BATCH2_AGENT_CONTRACTS_20260614T032003Z`: CLOSED / SETUP_READY_REGENERATED.
- Batch 2 Phase 2 atomization: COMPLETE / QA_PASS (`raw_atoms=7772`, `merged_atoms=7770`, `vocab_terms=968`).
- Batch 2 Gate 2 normalization: OPEN / HUMAN_REVIEW_REQUIRED.

## Rerun Requirements

- If any selected source file changes, update `Source_Manifest.csv`, rebuild the source catalog and BM25 index, regenerate affected companions, then regenerate this batch setup.
- If `tools/decomp/build_atomization_brief.py`, `Source_Decomp_Prefix_Map.csv`, or `skills/domain-source-atomize/` changes before worker fan-out, regenerate all briefs in this batch and re-run setup validation.
- After worker fan-out, update `Dispatch_Unit_Register.csv` with run status and counts before per-source merge.

## Remaining Blockers

- Batch 2 Gate 2 human review is required before the 7770 merged Batch 2 atom rows and 968 vocabulary terms become accepted decomposition truth.
- Batch 2 contains 8 merged `TBD` rows for review.
- Active Batch 1 reuse remains blocked by OI-012 until explicit carry-forward or rebaseline.
