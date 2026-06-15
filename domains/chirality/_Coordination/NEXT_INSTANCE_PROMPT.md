# NEXT INSTANCE PROMPT — Chirality DOMAIN_DECOMP (CLOSED)

## Status: terminal — no active gate

The Chirality self-domain decomposition is complete. DOMAIN_DECOMP Gates 1–6 are closed and accepted; Gate 6 Publish was accepted by `GATE6_PUBLISH_20260615T044434Z` and is the accepted basis for downstream work. There is no pending gate and no active development loop driving this domain.

Authoritative state lives in `domains/chirality/_Decomposition/`:

- `Chirality_Domain_Decomposition.md` — main control surface (working surface)
- `Gate6_Publication_Readiness.md` — Gate 6 acceptance packet
- `gate_snapshots/GATE{1..6}_*` — accepted immutable snapshots
- `Open_Issues_Register.csv` — 23 of 24 issues closed (only `OI-022` open, deferred)

Do not re-run DOMAIN_DECOMP from Phase 1 against this domain. Earlier revisions of this file framed pre-Gate-3 atomization/category work; those instructions are superseded by Gate 6 acceptance. Treat the gate snapshots and the decomposition document as truth over any older narrative.

## Only remaining caveat — OI-022 (deferred by human direction)

Live source-hash drift exists for two accepted source docs after their retrieval query-mode docs changed post-build:

- `@repo/tools/REGISTRY.md`
- `@repo/tools/retrieval/README.md`

`OI-022` is INFO severity and explicitly requires no action for Gate 6 closure. If/when the operator chooses to refresh the source database, do it as a **governed update/amendment** to the accepted basis — not a silent rebuild over accepted snapshot truth. Use the Rebuild Commands below.

## Resuming future work (if needed)

Future change to this accepted decomposition is a **scope-change cycle**, not a fresh decomposition. Act as `SCOPE_CHANGE` (see `agents/AGENT_SCOPE_CHANGE.md`) against the accepted Gate 6 basis, preserving the source-fidelity (AOP-08) and source-unit authority rules below. Source-driven fills of scaffold-for-fill surfaces (per Gate 5 / `OI-024`) also run through scope-change cycles.

To launch from the monorepo root, fill `init/init-prompt.md` with the chosen agent instruction file, the agent name, and `/Users/ryan/ai-env/projects/chirality/domains/chirality` as the target workspace.

## Source-Unit Authority Basis (reference)

`OI-018` is closed by human direction. `Gate2_Source_Unit_Register.csv` is the accepted Phase 3 source-unit authority; `Source_Manifest.csv` remains the file-level source-admission manifest. Batch 4 grouped skill-pack source units (`SKP000`..`SKP037`) represent 153 file-level `SKILL_CONTRACTS` rows through `source_components` maps. Downstream wording must not claim every individual `SK###` file was separately atomized.

## Rebuild Commands (reference — for a governed OI-022 refresh)

How to rebuild the source catalog when the source boundary or companions change:

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
