# Sealed brief — fresh SCA-003 ledger-repair poststate audit

Role: dedicated nondelegating `AUDIT_DECOMP` Agent 2 under Runtime SCOPE_CHANGE. Model: `gpt-5.6-sol`, medium reasoning. Role/nondelegation instruction-asserted. Do not delegate.

EXECUTION_ROOT: `/private/tmp/chirality-runtime-custody-amendment-20260906/projects/chirality-runtime/execution`
DECOMPOSITION_PATH: `/private/tmp/chirality-runtime-custody-amendment-20260906/projects/chirality-runtime/execution/_Decomposition/Chirality_Runtime_SOFTWARE_DECOMP_v1_0.md`
SCOPE: `PKG-02_Runtime_Product`
DECOMP_VARIANT: `SOFTWARE`
RUN_LABEL: `SCA003_LEDGER_REPAIR_POSTSTATE`
REQUESTED_BY: `SCOPE_CHANGE`
EXPECTED_SOURCE_SNAPSHOT: `/private/tmp/chirality-runtime-custody-amendment-20260906/projects/chirality-runtime/execution/_ScopeChange/SCA-003_2026-09-07_1616/SNAPSHOT_MANIFEST.json`
EXPECTED_HANDOFF_PHASE: `SCA-003 exact metadata repair applied; Gate 5 owner acceptance pending`

Read and obey repository `AGENTS.md`, `agents/AGENT_AUDIT_DECOMP.md`, Runtime `AGENTS.md` and loop entry. Read the exact v6 owner grant, decision subject, author/review manifests, live canonical decomposition, immutable SCA-001/SCA-002/SCA-003 snapshots, current scope pointer, first blocked audit, and exact external PKG02 owner decision evidence cited by the ledger.

Write only a new immutable audit snapshot under `{EXECUTION_ROOT}/_Evaluation/DecompCoverage/` and its permitted `_LATEST.md` pointer. Use a collision-free folder beginning `COV_SCA003_LEDGER_REPAIR_POSTSTATE_2026-09-07`. Produce every required AUDIT_DECOMP artifact plus `INPUT_PINS.json`, deterministic `CHECKS.json`, `OUTPUT_MANIFEST.json`, and `RETURN.md`.

Independently verify only the corrected poststate and conserved invariants:

- canonical ledger SHA256 equals approved v6 postimage `bffda2701dea3667a63f72194404db72b20520802a7d840af13ac456fb1f149d`; only `DecisionRef`/`Notes` changed from preimage `e3621b3...`; the other two SCA-002 canonical files retain hashes `19baaea2...` and `413687ca...`;
- SCA-003 snapshot manifest members and `_ScopeChange/_LATEST.md` pointer are complete, exact, and honest; SCA-002 and first blocked audit remain immutable history;
- the ledger records the first audit blocker as dated history and its metadata inconsistency as resolved without a repair-pending or proposed/candidate self-label; clean audit and separate Gate 5 acceptance remain future acts;
- owner-accepted HOST-P1, POLICY-R1 and ACCOUNT-WIRE-V1 contract basis is accurately distinguished from still-unmet source/implementation, supplier identity/qualification, signing/identity proof, paired Runtime/App/CLI conformance, recovery/lifecycle, protected-fixture, hold, hosted-readiness, and release gates;
- `CandidateState = GATE3_REVIEW_NOT_ACCEPTED` remains historical migration/decomposition metadata rather than current SCA-002/SCA-003 approval state;
- one SOW, one package, seven carriers, four objectives, 66 qualified inherited requirements, nine holds plus R16-B, historical basis `9f21e4b...`, `root-runtime-1` epoch 1, project authorization, security/exclusion boundaries, and no activation remain;
- no SOW, source, deliverable lifecycle/context/dependency, supplier, process, credential, protected-fixture, hold, Git, hosted-readiness, Root-adoption, publication, or release action is claimed or introduced.

Do not repair or modify canonical/SCA/coordination/prior audit evidence. Return `NON_BLOCKING_PASS`, `WARNINGS`, or `BLOCKED`, exact paths/hashes, and on PASS the precise separate Gate 5 poststate owner-acceptance subject under `agents/AGENT_SCOPE_CHANGE.md` lines 590–597. The audit grants no closure or publication.

## Normalized parameters

- Snapshot timestamp: `2026-09-07T22:27:00Z`
- Snapshot folder: `COV_SCA003_LEDGER_REPAIR_POSTSTATE_2026-09-07_2227`
- Concrete labels: Package / Deliverable
- Prior comparison mode: not requested
- Role and nondelegation evidence: instruction-asserted; no delegation performed
