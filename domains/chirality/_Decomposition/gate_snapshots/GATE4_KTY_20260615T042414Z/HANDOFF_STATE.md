# Gate 4 Handoff State - Chirality DOMAIN_DECOMP KTY / Subjects

Package role: snapshot / handoff artifact

Status: Gate 4 accepted; Gate 5 Coverage is ready to start.

Generated UTC: 2026-06-15T04:24:14Z

## Accepted Upstream Snapshot(s)

- Gate 1: `domains/chirality/_Decomposition/gate_snapshots/GATE1_20260614T005942Z`
- Gate 2: `domains/chirality/_Decomposition/gate_snapshots/GATE2_PHASE2_20260614T204403Z`
- Gate 2 source-unit authority: `domains/chirality/_Decomposition/gate_snapshots/GATE2_PHASE2_SOURCE_UNIT_AUTHORITY_20260614T211725Z`
- Gate 3: `domains/chirality/_Decomposition/gate_snapshots/GATE3_CATEGORIES_20260615T030833Z`
- Gate 4: `domains/chirality/_Decomposition/gate_snapshots/GATE4_KTY_20260615T042414Z`
- Retrieval package: `domains/chirality/_LocalIndexes/snapshots/SRCIDX_20260614T204703Z` (`source_v2`, BM25 + dense)

## Accepted Gate 4 Artifacts

- `domains/chirality/_Decomposition/Knowledge_Type_Register.csv`
- `domains/chirality/_Decomposition/Knowledge_Subject_Register.csv`
- `domains/chirality/_Decomposition/Domain_Ledger_Gate4_KTY_Draft.csv`
- `domains/chirality/_Decomposition/KTY_Scope_Ratification.csv`
- `domains/chirality/_Decomposition/KTY_Assignment_Summary.csv`
- `domains/chirality/_Decomposition/KTY_Assignment_Findings.csv`
- `domains/chirality/_Decomposition/Gate4_Coverage_Telemetry.csv`

## Accepted Counts

- Knowledge Types: 50
- Knowledge Subjects: 98
- IN atoms mapped to KTY/Subject: 19403 / 19403
- PRD atoms also associated with DBM/PRD publication KTY: 199 / 199
- Blocking calibrated KTY verdicts: 0

## Derivative-Package Status

`KTY_Scope_Ratification.csv` is accepted diagnostic retrieval evidence under the calibrated basis. It does not replace the accepted KTY/Subject register truth. The local source index remains a derived retrieval package citing accepted source/decomposition truth.

## Source Freshness Caveat

`OI-022` remains deferred by human direction. The accepted source database was not rebuilt for post-build source-doc drift in `tools/REGISTRY.md` and `tools/retrieval/README.md`; this cadence remains outside Gate 4 closure.

## Rerun Requirements

- If any atom text changes, or atoms split/merge, rebuild the source database and retrieval index before Gate 5 coverage verification consumes the change.
- If KTY names, Subject boundaries, PRD/DBM association policy, or unit mappings change, create a Gate 4 refinement/amendment snapshot before proceeding downstream.
- Gate 5 should consume the accepted Gate 4 ledger and registers listed above.

## Next Action

Proceed to Phase 5 Coverage verification from accepted Gate 4 snapshot `GATE4_KTY_20260615T042414Z`. Do not start hypergraph publication, DBM publication, public export, or separate project-domain decomposition unless the human explicitly authorizes that work.
