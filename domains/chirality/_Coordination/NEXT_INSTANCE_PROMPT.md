# NEXT INSTANCE PROMPT - Chirality DOMAIN_DECOMP

## Entry Protocol

1. Read `/Users/ryan/ai-env/projects/chirality/AGENTS.md`.
2. Read `/Users/ryan/ai-env/projects/chirality/agents/AGENT_DECOMP_BASE.md`.
3. Read `/Users/ryan/ai-env/projects/chirality/agents/AGENT_DOMAIN_DECOMP.md`.
4. Act in the `DOMAIN_DECOMP` persona for `/Users/ryan/ai-env/projects/chirality/domains/chirality`.
5. Read `/Users/ryan/ai-env/projects/chirality/skills/domain-source-atomize/SKILL.md` before any additional Phase 2 atomization work.
6. Read the current decomposition control and handoff surfaces:
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/Chirality_Domain_Decomposition.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/gate_snapshots/_LATEST_GATE1.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/gate_snapshots/_LATEST_GATE2.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/gate_snapshots/GATE2_PHASE2_20260614T204403Z/GATE2_ACCEPTANCE.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/gate_snapshots/GATE2_PHASE2_20260614T204403Z/HANDOFF_STATE.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/gate_snapshots/GATE2_PHASE2_SOURCE_UNIT_AUTHORITY_20260614T211725Z/GATE2_SOURCE_UNIT_AUTHORITY.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/gate_snapshots/GATE2_PHASE2_SOURCE_UNIT_AUTHORITY_20260614T211725Z/HANDOFF_STATE.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/phase2_batches/_LATEST_PHASE2_GATE2.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/Gate2_Source_Unit_Register.csv`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/Category_Assignment_Findings.csv`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/Category_Assignment_Review_Packet.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/Category_Assignment_Findings_Summary.csv`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/Category_Scope_Ratification.csv`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/Domain_Ledger_Gate3_Category_Draft.csv`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/Category_Register.csv`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/gate3_categories/GATE3_CATEGORY_PROPOSAL_20260614T213500Z/HANDOFF_STATE.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/gate3_categories/GATE3_CATEGORY_PROPOSAL_20260614T213500Z/GATE3_CATEGORY_PROPOSAL.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/gate3_categories/_LATEST_GATE3_PROPOSAL.md`
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

## Current Governed State

Gate 2 is closed and accepted for the active Chirality DOMAIN_DECOMP Phase 2 source-unit set.

- Gate 2 acceptance snapshot: `domains/chirality/_Decomposition/gate_snapshots/GATE2_PHASE2_20260614T204403Z`
- Gate 2 source-unit authority addendum: `domains/chirality/_Decomposition/gate_snapshots/GATE2_PHASE2_SOURCE_UNIT_AUTHORITY_20260614T211725Z`
- Gate 2 pointer: `domains/chirality/_Decomposition/gate_snapshots/_LATEST_GATE2.md`
- Phase 2 closure pointer: `domains/chirality/_Decomposition/phase2_batches/_LATEST_PHASE2_GATE2.md`
- Human approval date: 2026-06-14
- Accepted source units: `110`
- Canonical atom ledger: `domains/chirality/_Decomposition/Atomic_Domain_Ledger.csv`
- Accepted atom rows: `19473` (`IN=19403`, `OUT=20`, `TBD=50`)
- Canonical vocabulary map: `domains/chirality/_Decomposition/Vocabulary_Map.csv`
- Accepted vocabulary terms: `2582`
- Phase 2.5 TOC prior pairs: `21964`
- Accepted source-unit register: `domains/chirality/_Decomposition/Gate2_Source_Unit_Register.csv`

The active file-level source manifest remains authoritative for source-file admission:

- Active manifest rows: `225`
- Active manifest SHA-256: `6d9ea9bf796ab83a0e0e01fc5d0d24e095fcb6ce0bf6a6739d4f50fa0296509e`
- Current catalog snapshot: `domains/chirality/_LocalIndexes/snapshots/SRCIDX_20260614T204703Z`
- Current catalog status: structural validation PASS; BM25 smoke query for `derivative-package rule` ranks `@repo/AGENTS.md` first.

## Accepted Batch State

Phase 2 closure accepts these source units as decomposition truth:

| Batch | Accepted source units | Closure status |
| --- | ---: | --- |
| Batch 1 active carry-forward | 9 | `GATE2_ACCEPTED_ACTIVE_CARRY_FORWARD_PARTIAL` |
| Batch 2 agent contracts | 36 | `GATE2_ACCEPTED_IN_PHASE2_CLOSURE` |
| Batch 3 governance/thesis | 22 | `GATE2_ACCEPTED_IN_PHASE2_CLOSURE` |
| Batch 4 grouped skill packs | 38 | `GATE2_ACCEPTED_IN_PHASE2_CLOSURE` |
| Batch 5 work-surface registry | 4 | `GATE2_ACCEPTED_IN_PHASE2_CLOSURE` |
| Batch 6 license | 1 | `GATE2_ACCEPTED_IN_PHASE2_CLOSURE` |

Batch 1 is only partially carried forward for active V1: 11 retired Batch 1 rows remain historical evidence and are not part of the accepted active source-unit set. Batch 4 uses grouped skill-pack source units (`SKP000`..`SKP037`) rather than one accepted source unit per file-level `SK###` manifest row. `SRC-SKILLS-README` and `SRC-SKILLS-SKILL-TEMPLATE` are superseded by grouped source unit `SRC-SKILLPACK-META`.

## Source-Unit Authority Basis

`OI-018` is closed by human direction. `Gate2_Source_Unit_Register.csv` is the accepted Phase 3 source-unit authority; `Source_Manifest.csv` remains the file-level source-admission manifest. Batch 4 grouped skill-pack source units (`SKP000`..`SKP037`) represent 153 file-level `SKILL_CONTRACTS` rows through `source_components` maps. Phase 3 may proceed from the accepted 110-source-unit surface, but downstream wording must not claim every individual `SK###` file was separately atomized.

## Gate 3 Open State

Gate 3 category refinement is generated but not accepted.

- Proposal pointer: `domains/chirality/_Decomposition/gate3_categories/_LATEST_GATE3_PROPOSAL.md`
- Latest refinement snapshot: `domains/chirality/_Decomposition/gate3_categories/GATE3_CATEGORY_REFINEMENT_20260615T021906Z`
- Categories: `11`
- Draft category-assigned ledger: `domains/chirality/_Decomposition/Domain_Ledger_Gate3_Category_Draft.csv`
- Assigned IN atoms: `19403` / `19403`
- Ambiguous assignment findings: `881` resolved forced decisions, `0` open in `Category_Assignment_Findings.csv`
- Boundary decisions: `domains/chirality/_Decomposition/Category_Boundary_Decisions.csv`
- Dense calibration note: `domains/chirality/_Decomposition/Gate3_Ratification_Calibration.md`
- Ratification status: `SCOPE_REFINEMENT_NEEDED` for all Categories in `Category_Scope_Ratification.csv`

Dense embeddings completed for Gate 3. The source_v2 index is READY, category scopes and primary-function boundary rules were refined, and all 881 advisory ambiguous-assignment findings were closed without atom splits. Dense ratification still returns `SCOPE_REFINEMENT_NEEDED` for all 11 Categories under the default 0.75 cosine threshold. Gate 3 cannot close until the human explicitly approves a calibrated ratification threshold/basis or directs further category refinement.

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

## Next Recommended Action

Continue Gate 3 review from `GATE3_CATEGORY_REFINEMENT_20260615T021906Z`: inspect the refined 11-category register, the 87 draft assignment changes, and `Gate3_Ratification_Calibration.md`; then obtain an explicit human ruling on the calibrated dense-ratification threshold/basis or perform another refinement pass. Treat `Atomic_Domain_Ledger.csv`, `Vocabulary_Map.csv`, `cross_source_toc_matrix.*`, `Gate2_Source_Unit_Register.csv`, and the Gate 2 snapshots as the accepted upstream truth; `Domain_Ledger_Gate3_Category_Draft.csv` is draft until Gate 3 is accepted.

Do not start hypergraph publication, DBM publication, dense embeddings, public export, or separate project-domain decomposition from this handoff unless the human explicitly authorizes that work.
