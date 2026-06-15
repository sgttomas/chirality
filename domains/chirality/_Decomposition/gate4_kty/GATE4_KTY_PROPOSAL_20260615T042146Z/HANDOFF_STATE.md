# Gate 4 Handoff State - KTY / Subject Proposal

Generated: 2026-06-15T04:21:46Z

## Verdict

Gate 4 is ACCEPTED by `GATE4_KTY_20260615T042414Z`. The KTY/Subject proposal is accepted.

## Accepted Upstream Snapshot(s)

- `domains/chirality/_Decomposition/gate_snapshots/GATE1_20260614T005942Z/`
- `domains/chirality/_Decomposition/gate_snapshots/GATE2_PHASE2_20260614T204403Z/`
- `domains/chirality/_Decomposition/gate_snapshots/GATE2_PHASE2_SOURCE_UNIT_AUTHORITY_20260614T211725Z/`
- `domains/chirality/_Decomposition/gate_snapshots/GATE3_CATEGORIES_20260615T030833Z/`
- `/Users/ryan/ai-env/projects/chirality/domains/chirality/_LocalIndexes/snapshots/SRCIDX_20260614T204703Z` (`source_v2`, BM25 + dense, accepted for atom retrieval despite deferred source-doc freshness cadence)

## Current Gate 4 Draft Artifacts

- `domains/chirality/_Decomposition/Knowledge_Type_Register.csv`
- `domains/chirality/_Decomposition/Knowledge_Subject_Register.csv`
- `domains/chirality/_Decomposition/Domain_Ledger_Gate4_KTY_Draft.csv`
- `domains/chirality/_Decomposition/KTY_Scope_Ratification.csv`
- `domains/chirality/_Decomposition/KTY_Assignment_Summary.csv`
- `domains/chirality/_Decomposition/KTY_Assignment_Findings.csv`
- `domains/chirality/_Decomposition/Gate4_Coverage_Telemetry.csv`

## Counts

- Proposed Knowledge Types: 50
- Proposed Knowledge Subjects with mapped units: 98
- IN atoms mapped to KTY/Subject: 19403 / 19403
- PRD source atoms retaining primary location and associated with DBM/PRD publication KTY: 199
- Low-confidence advisory assignment findings: 5932
- Blocking calibrated KTY verdicts: 0

## Rerun Requirements

- If KTY names, descriptions, or Subject boundaries change, rerun `tools/decomp/propose_gate4_kty.py` or manually update the draft registers and ratification evidence consistently.
- If any UnitStatement text changes or atoms split/merge, rebuild the source database and retrieval index before Gate 4 ratification resumes.
- Do not proceed to Gate 5 coverage closure until Gate 4 is explicitly accepted by the human.

## Remaining Blockers

- None. Gate 4 is accepted.
