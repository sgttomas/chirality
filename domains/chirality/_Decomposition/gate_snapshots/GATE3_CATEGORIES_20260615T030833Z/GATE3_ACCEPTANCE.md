# Gate 3 Acceptance - Chirality DOMAIN_DECOMP Categories

Package role: snapshot / handoff artifact

Gate: Gate 3 Categories

Scope: Accepted 11-category structural partition over the active Gate 2 source-unit surface

Status: ACCEPTED

Accepted UTC: 2026-06-15T03:08:33Z

Human confirmation:

```text
now record Gate 3 as approved and proceed accordingly.
```

## Accepted Basis

Categories are accepted as a governed structural partition and navigation facet. Dense embeddings and BM25 are accepted as retrieval/discovery mechanisms across the full ledger, not as hard category-membership gates. The default 0.75 cosine threshold remains recorded as diagnostic evidence for broad category-to-atom comparisons, not as a closure floor.

The default `0.75` cosine threshold remains recorded in `Category_Scope_Ratification.csv` as diagnostic evidence. It is not the hard membership or closure floor for Gate 3 because Category embeddings are broad structural descriptors, not centroids for every assigned atom. Retrieval modes may intentionally surface cross-category associations.

## Accepted Upstream Truth

- Gate 1 acceptance snapshot: `domains/chirality/_Decomposition/gate_snapshots/GATE1_20260614T005942Z`
- Gate 2 acceptance snapshot: `domains/chirality/_Decomposition/gate_snapshots/GATE2_PHASE2_20260614T204403Z`
- Gate 2 source-unit authority addendum: `domains/chirality/_Decomposition/gate_snapshots/GATE2_PHASE2_SOURCE_UNIT_AUTHORITY_20260614T211725Z`
- Source catalog / retrieval snapshot: `domains/chirality/_LocalIndexes/snapshots/SRCIDX_20260614T204703Z` (`source_v2`, BM25 + dense READY)
- Accepted canonical ledger SHA-256: `a7e28a2ff0902b4b86ad650c661612aa9bc413bc78213181570f93d64367e588`
- Accepted vocabulary map SHA-256: `5f48d0e49aecd92be36f4c149832237b6c7ff6a456c12ced35ab20c69c26a899`
- Accepted source-unit register SHA-256: `2901efdbbebce5b58f152e1592d5ca4141b99f77fee15df24fa9786347b8e61e`

## Accepted Gate 3 Artifacts

| Artifact | SHA-256 |
|---|---|
| `Category_Register.csv` | `6153bb0b9f8788029aa84d983f77b34939333bed365e698f43258f802fc151f4` |
| `Domain_Ledger_Gate3_Category_Draft.csv` | `7c42c8d7a791f463c603f84d1c9799dbbd87b14aa9a02b9d9319db19135f1121` |
| `Category_Scope_Ratification.csv` | `a6128c0beec77794835df978347bb8731c19bb476787bf8f00ba1137d4b309b1` |
| `Category_Assignment_Findings.csv` | `20a23aa8bf35782fa4cfe6a0f26b656c3136a338a54621564a3f7486c82fee5d` |
| `Category_Assignment_Findings_Summary.csv` | `3a342cb27646f96d1299bb95d07cd5d9d0b5419f0c8e03ddd2c970175fa6e156` |
| `Category_Assignment_Summary.csv` | `047ebaa56d0502f6eff81ee7999c99611155c6df95829ab70254b9ff40d5413a` |
| `Category_Boundary_Decisions.csv` | `20b75e2bc03b670a8982af52bc6c89f04e119f9cd9e0b619bd1285dc73bbce24` |
| `Category_Assignment_Review_Packet.md` | `117459d01f86d8eec8a7a285bfd6aa793e27ddde696cb7aeb34053c6bd7772a7` |
| `Gate3_Ratification_Calibration.md` | `35d3353f9337881c3d803a24bf3d7a0415a606e11b23c7a0496d195e55afedb5` |

## Accepted Category Telemetry

| Metric | Value |
|---|---:|
| Categories | 11 |
| Gate 2 atom rows | 19473 |
| IN atoms | 19403 |
| IN atoms with exactly one Category | 19403 |
| OUT/TBD rows without Category assignment | 70 |
| Ambiguous assignment findings | 881 |
| Open assignment findings | 0 |
| Resolved assignment findings | 881 |
| Boundary-rule assignment changes | 87 |
| Atom splits in Gate 3 | 0 |
| Blocking scope verdicts after acceptance | 0 |

## Source Freshness Caveat

Current live source-catalog validation reports known hash drift after this repository's retrieval query mode documentation update because `@repo/tools/REGISTRY.md` and `@repo/tools/retrieval/README.md` no longer match `SRCIDX_20260614T204703Z`. Gate 3 is accepted against the frozen accepted Gate 2/Gate 3 snapshot basis above. `OI-022` records the human decision to defer source-database update cadence outside this Gate decision/process.

## Gate 3 Verdict

Gate 3 is accepted. The 11-category partition is the governed structural ontology/navigation facet for Gate 4. `Atomic_Domain_Ledger.csv`, `Vocabulary_Map.csv`, `Gate2_Source_Unit_Register.csv`, the accepted Gate 2 snapshots, and this Gate 3 snapshot are the accepted upstream truth for Phase 4.

This acceptance does not create Knowledge Type, Knowledge Subject, coverage, hypergraph, DBM publication, or public export truth.
