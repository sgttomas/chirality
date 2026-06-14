# Gate 2 Source-Unit Authority Addendum - Chirality DOMAIN_DECOMP Phase 2

Package role: snapshot / handoff artifact

Gate: Gate 2 Atomization / Normalization

Scope: Closure of grouped skill-pack source-unit caveat before Gate 3

Status: ACCEPTED / CAVEAT_CLOSED

Accepted UTC: 2026-06-14T21:17:25Z

Human direction:

```text
Close the caveat by recording that basis.
```

## Decision

`Gate2_Source_Unit_Register.csv` is the accepted source-unit authority for Phase 3 and later DOMAIN_DECOMP phases. `Source_Manifest.csv` remains the file-level source-admission manifest; it is not required to provide one row per accepted source unit when a human-accepted source unit is a grouped source backed by a component map.

This closes `OI-018`.

## Recorded Basis

- Accepted source-unit register: `domains/chirality/_Decomposition/Gate2_Source_Unit_Register.csv`
- Accepted source-unit count: `110`
- Grouped skill-pack source units: `38` (`SKP000`..`SKP037`)
- Skill-contract manifest component rows represented by grouped source units: `153`
- Grouped-source provenance: Batch 4 asset manifests under `domains/chirality/_Decomposition/source_asset_manifests/` with `source_components` maps.
- SourceRef basis: atom `SourceRef` values cite original repo component files via `@repo/<component RepoRelPath>:L####|domains/chirality/_Decomposition/source_review_html/<SourceDocID>.html#<SectionID>`.
- Generated pack markdown is a worker/review substrate, not provenance truth.

## Interpretation

For Phase 3, the invariant is one accepted source-unit authority row per accepted Phase 2 source unit, not one file-level manifest row per accepted source unit. The accepted register bridges three admitted source-unit models:

| Source-unit model | Authority |
| --- | --- |
| Manifest-backed single source | `Source_Manifest.csv` plus `Gate2_Source_Unit_Register.csv` |
| Active Batch 1 carry-forward | `Gate2_Source_Unit_Register.csv` plus prior accepted Batch 1 evidence |
| Grouped component-map source | `Gate2_Source_Unit_Register.csv` plus Batch 4 `source_components` maps |

Downstream registers and prose may say that the skill-contract area was accepted as 38 grouped skill-pack source units. They must not claim that each individual `SK###` file-level manifest row was separately atomized as its own accepted source unit.

## Upstream Truth Preserved

- Gate 2 acceptance snapshot: `domains/chirality/_Decomposition/gate_snapshots/GATE2_PHASE2_20260614T204403Z`
- Accepted canonical ledger: `domains/chirality/_Decomposition/Atomic_Domain_Ledger.csv`
- Accepted vocabulary map: `domains/chirality/_Decomposition/Vocabulary_Map.csv`
- Accepted source-unit register: `domains/chirality/_Decomposition/Gate2_Source_Unit_Register.csv`
- Source manifest: `domains/chirality/_Sources/Source_Manifest.csv`
- Current catalog snapshot: `domains/chirality/_LocalIndexes/snapshots/SRCIDX_20260614T204703Z`

## Gate 3 Effect

Gate 3 may proceed from the accepted 110-source-unit Phase 2 surface without an open grouped-source caveat. Category proposal and retrieval-driven ratification must consume `Gate2_Source_Unit_Register.csv` for source-unit membership and may use `Source_Manifest.csv` for file-level provenance/admission only.
