# NEXT INSTANCE PROMPT - Chirality DOMAIN_DECOMP

## Entry Protocol

1. Read `/Users/ryan/ai-env/projects/chirality/AGENTS.md`.
2. Read `/Users/ryan/ai-env/projects/chirality/agents/AGENT_DECOMP_BASE.md`.
3. Read `/Users/ryan/ai-env/projects/chirality/agents/AGENT_DOMAIN_DECOMP.md`.
4. Act in the `DOMAIN_DECOMP` persona for `/Users/ryan/ai-env/projects/chirality/domains/chirality`.
5. Read `/Users/ryan/ai-env/projects/chirality/skills/domain-source-atomize/SKILL.md` before any Phase 2 atomization work.
6. Read the current decomposition control and handoff surfaces:
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/Chirality_Domain_Decomposition.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/gate_snapshots/_LATEST_GATE1.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/gate_snapshots/_LATEST_GATE2.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/gate_snapshots/GATE2_BATCH1_20260614T023234Z/HANDOFF_STATE.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/phase2_batches/_LATEST_BATCH1_GATE2.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/phase2_batches/_LATEST_BATCH2_SETUP.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/Validation_Checks.csv`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/Open_Issues_Register.csv`
7. Read the Chirality domain-pack source surfaces:
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/README.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/domain-pack.yaml`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Sources/SOURCE_BOUNDARY.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Sources/Source_Manifest.csv`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/Source_Decomp_Prefix_Map.csv`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_LocalIndexes/_LATEST.md`
8. Run `git status --short` before coordination-sensitive planning or edits.

## Active Direction

Continue from accepted Batch 1 Gate 2, but treat it as prior-boundary evidence for active reuse until the source-boundary amendment is accepted or Batch 1 is rebaselined.

Source-boundary cleanup has retired 21 rows from active V1 indexing and atomization:

- `SRC-FRONTEND-*` / `HX001`..`HX009` for `frontend/README.md` and `frontend/docs/...`.
- `SRC-AGENTS-AGENT-DELIVERABLE-TASK` / `AG013`, because `agents/AGENT_DELIVERABLE_TASK.md` was archived as obsolete.
- `SRC-CLAUDE` / `RT003`, `SRC-INIT` / `RT004`, and `SRC-DOCS-*` / `DG001`..`DG009` for eleven root/governance sources whose live repo files are now archived or removed.

Current active manifest:

- Active rows: `221`
- SHA-256: `acd2fd88ff66be89b33d5cde05ab15cbcb584adea2fd25e661d9ea9eb0f64b04`
- Retired prefixes reserved in `Source_Decomp_Prefix_Map.csv`: `AG013`, `HX001`..`HX009`, `RT003`, `RT004`, `DG001`..`DG009`
- Batch 0 generated companion files for retired frontend/AG013 rows were removed.
- Prior-boundary Batch 1 companions for the eleven newly retired sources were retained as historical evidence; prefix-map active companion paths were cleared.
- Batch 2 was regenerated as `BATCH2_AGENT_CONTRACTS_20260614T032003Z`, excluding retired `AG013`; fan-out/fan-in is complete and Gate 2 is open.

Gate 2 for `BATCH1_BINDING_GOVERNANCE_20260614T011101Z` remains **accepted** for its original 22-source binding-governance scope, but 11 of those sources are now retired from active V1. Do not use the accepted Batch 1 ledger for active Gate 3 or downstream closure without explicit carry-forward or a rebaseline.

The previous Batch 2 setup package `BATCH2_AGENT_CONTRACTS_20260614T024251Z` is **superseded stale evidence** because it selected retired `AG013`. Use only `BATCH2_AGENT_CONTRACTS_20260614T032003Z` for Batch 2 review. Do not promote Batch 2 atoms to accepted decomposition truth until Gate 2 is human-accepted.

## Current Validation State

The source catalog and BM25 retrieval index were rebuilt after Batch 2 atom-review section-node refresh:

- Latest source catalog: `domains/chirality/_LocalIndexes/snapshots/SRCIDX_20260614T050727Z`
- `validate_source_database.py`: `PASS` with 0 blockers and 0 warnings
- Source docs: `232`
- Artifacts: `454`
- Chunks: `11652`
- Retrieval: `BM25_ONLY`, rows `11652`
- Smoke query `derivative-package rule`: rank 1 `SRC-AGENTS` section node

Important warning: source catalog validation is structural. The catalog still contains retained Batch 1 prior-boundary ledger/section companions that reference the eleven newly retired sources. Batch 2 also remains unaccepted at Gate 2. This is intentional evidence retention and review staging, not current active-boundary closure.

## Rebuild Commands

Rebuild the source catalog when the source boundary or companions change:

```sh
python3 tools/source_catalog/build_source_database.py \
  --domain-root domains/chirality \
  --repo-root . \
  --source-manifest domains/chirality/_Sources/Source_Manifest.csv
```

Then validate:

```sh
python3 tools/source_catalog/validate_source_database.py \
  --snapshot domains/chirality/_LocalIndexes/_LATEST.md \
  --domain-root domains/chirality \
  --repo-root .
```

Then rebuild BM25 retrieval:

```sh
python3 tools/retrieval/build_source_index.py \
  --snapshot domains/chirality/_LocalIndexes/_LATEST.md \
  --no-embeddings
```

Then confirm the smoke query if retrieval will be used:

```sh
python3 tools/retrieval/query_source_index.py \
  --snapshot domains/chirality/_LocalIndexes/_LATEST.md \
  --query "derivative-package rule" \
  --k 1
```

Expected rank 1 result is `SRC-AGENTS` / `@repo/AGENTS.md`.

## Batch 1 Accepted State

- batch ID: `BATCH1_BINDING_GOVERNANCE_20260614T011101Z`
- selected sources: `22`
- dispatch units: `22`
- merged atom rows: `3274`
- IN rows after merge: `3262`
- OUT rows after merge: `12`
- TBD rows after merge: `0`
- merged vocabulary terms: `670`
- Gate 2 status: `ACCEPTED`
- Phase 2.5 status: `PASS_WITH_PRIOR_BOUNDARY_WARNING`
- active reuse status: `BLOCKED_BY_OI_012` until carry-forward or rebaseline is accepted.

Primary Batch 1 outputs remain:

- `domains/chirality/_Decomposition/Atomic_Domain_Ledger.csv`
- `domains/chirality/_Decomposition/Vocabulary_Map.csv`
- `domains/chirality/_Decomposition/phase2_batches/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/BATCH1_GATE2_HANDOFF.md`

## Batch 2 State

- batch ID: `BATCH2_AGENT_CONTRACTS_20260614T032003Z`
- selected sources: `36` active `AGENT_CONTRACTS` rows
- excluded retired source: `SRC-AGENTS-AGENT-DELIVERABLE-TASK` / `AG013`
- dispatch units: `36`
- rendered INIT-TASK briefs: `36`
- per-unit atom CSVs: `36`
- per-unit vocabulary CSVs: `36`
- raw worker atom rows: `7772` (`IN=7760`, `OUT=4`, `TBD=8`)
- per-source ledgers: `36`
- merged atom rows: `7770` (`IN=7758`, `OUT=4`, `TBD=8`)
- merged vocabulary terms: `968` (`137` multi-source)
- atom-review HTML files: `36`
- Gate 2 status: `OPEN_HUMAN_REVIEW_REQUIRED`

Primary Batch 2 outputs:

- `domains/chirality/_Decomposition/phase2_batches/BATCH2_AGENT_CONTRACTS_20260614T032003Z/BATCH2_SETUP.md`
- `domains/chirality/_Decomposition/phase2_batches/BATCH2_AGENT_CONTRACTS_20260614T032003Z/BATCH2_ATOMIZATION_HANDOFF.md`
- `domains/chirality/_Decomposition/phase2_batches/BATCH2_AGENT_CONTRACTS_20260614T032003Z/Dispatch_Run_Log.csv`
- `domains/chirality/_Decomposition/phase2_batches/BATCH2_AGENT_CONTRACTS_20260614T032003Z/BATCH2_Atomic_Domain_Ledger.csv`
- `domains/chirality/_Decomposition/phase2_batches/BATCH2_AGENT_CONTRACTS_20260614T032003Z/BATCH2_Vocabulary_Map.csv`
- `domains/chirality/_Decomposition/dispatch_outputs/BATCH2_AGENT_CONTRACTS_20260614T032003Z/`
- `domains/chirality/_Decomposition/per_source_ledgers/BATCH2_AGENT_CONTRACTS_20260614T032003Z/`
- `domains/chirality/_Decomposition/vocabulary_seeds/BATCH2_AGENT_CONTRACTS_20260614T032003Z/`

Gate 2 remains open until the human explicitly confirms: “The Batch 2 atom boundaries, IN/OUT/TBD classifications, source bindings, and vocabulary choices are accepted as decomposition truth for the active 36-source agent-contract batch.”

## Open Work

- `OI-005`: active-manifest atomization remains staged/incomplete; active manifest is 221 rows, Batch 1 is prior-boundary accepted, and Batch 2 is complete but unaccepted.
- `OI-007`: Batch 1 Gate 3 is blocked by the prior-boundary issue.
- `OI-009`: source-boundary amendment retires 21 rows after Gate 1 accepted the prior 242-row manifest.
- `OI-012`: 11 accepted Batch 1 sources are retired from active V1; explicit carry-forward or rebaseline is required before active Batch 1 reuse.
- `OI-013`: Batch 2 Gate 2 human review is required before its 7770 merged atom rows and 968 vocabulary terms become accepted decomposition truth.

Closed by the latest pass:

- `OI-008`: stale 37-source Batch 2 setup was superseded by regenerated 36-source setup.
- `OI-011`: retired AG013 is excluded from active Batch 2 and no AG013 output is used by the active merge.

## Non-Goals

Do not start with:

- treating Batch 1 partial `Atomic_Domain_Ledger.csv` or unaccepted Batch 2 batch-scoped ledgers as full-corpus truth;
- running Batch 2 workers from the superseded stale 37-source setup;
- copying live repo source files into `_Sources/` as authoritative source truth;
- admitting `.archive/`, `projects/`, `examples/`, or generated export staging as replacement source truth without explicit source-boundary acceptance;
- dense embedding build as a prerequisite;
- hypergraph generation;
- DBM publication;
- public export changes.

## Closeout

Report files created or changed, validation run, skipped checks and why, remaining human rulings, and whether Batch 1 Gate 2 remains accepted for its original 22-source scope.
