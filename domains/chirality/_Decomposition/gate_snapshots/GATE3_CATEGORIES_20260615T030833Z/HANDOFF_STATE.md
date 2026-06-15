# Gate 3 Handoff State - Chirality DOMAIN_DECOMP Categories

Package role: snapshot / handoff artifact

Status: Gate 3 accepted; Gate 4 Knowledge Type / Knowledge Subject proposal is ready to start.

Generated UTC: 2026-06-15T03:08:33Z

## Accepted Upstream Snapshot(s)

- Gate 1: `domains/chirality/_Decomposition/gate_snapshots/GATE1_20260614T005942Z`
- Gate 2: `domains/chirality/_Decomposition/gate_snapshots/GATE2_PHASE2_20260614T204403Z`
- Gate 2 source-unit authority: `domains/chirality/_Decomposition/gate_snapshots/GATE2_PHASE2_SOURCE_UNIT_AUTHORITY_20260614T211725Z`
- Gate 3: `domains/chirality/_Decomposition/gate_snapshots/GATE3_CATEGORIES_20260615T030833Z`
- Retrieval package: `domains/chirality/_LocalIndexes/snapshots/SRCIDX_20260614T204703Z` (`READY`, BM25 + dense)

## Accepted Gate 3 State

- Categories: 11
- Assigned IN atoms: 19403 / 19403
- Non-IN rows without Category assignment: 70
- Assignment findings: 881 resolved, 0 open
- Scope ratification: `CLUSTER_COHERENT` under human-approved calibrated structural-partition basis
- Dense/BM25 role: retrieval/discovery evidence, not a hard category-membership gate
- Atom splits or UnitStatement edits in Gate 3: 0

## Derivative-Package Status

- `Category_Scope_Ratification.csv` is an accepted diagnostic ratification register under the calibrated basis, not a substitute for the accepted Category partition.
- `_LocalIndexes/snapshots/SRCIDX_20260614T204703Z` remains a derived local catalog/retrieval package citing accepted source/decomposition truth.
- The Gate 3 category-assigned ledger file retains its historical `Draft` filename, but its Category assignments are accepted by this snapshot.

## Closure Verdict

- Gate 1 Intake: CLOSED / ACCEPTED
- Gate 2 Atomization / Normalization: CLOSED / ACCEPTED
- Gate 3 Categories: CLOSED / ACCEPTED
- Gate 4 Knowledge Types / Knowledge Subjects: READY_TO_START
- Gate 5 Coverage: NOT_STARTED
- Gate 6 Publish: NOT_STARTED

## Source Freshness Caveat

`validate_source_database.py` currently reports known hash mismatches for `@repo/tools/REGISTRY.md` and `@repo/tools/retrieval/README.md` because those accepted source files changed after `SRCIDX_20260614T204703Z` was built. The human deferred source-database update cadence outside this Gate decision/process. Gate 4 planning may start from the accepted Gate 3 snapshot; `OI-022` is not a Phase 4 entry blocker.

## Rerun Requirements

- If any atom text changes or any atom is split, rebuild the source database and retrieval index before Gate 4 ratification resumes.
- If category names, scopes, or assignments change after this snapshot, create a new Gate 3 amendment/refinement snapshot before consuming the change downstream.
- Gate 4 should consume `Category_Register.csv`, `Domain_Ledger_Gate3_Category_Draft.csv`, `Atomic_Domain_Ledger.csv`, `Vocabulary_Map.csv`, `Gate2_Source_Unit_Register.csv`, and the accepted Gate 1-3 snapshots.

## Next Action

Proceed to Phase 4: propose Knowledge Types and Knowledge Subjects within each accepted Category, map IN atoms to best-effort Subjects, and run KTY scope ratification under the same structural-partition/retrieval-discovery distinction unless the human directs a different calibrated basis.
