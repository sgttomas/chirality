# Sealed brief — SCA-002 Gate 5 ledger metadata repair candidate

Role: bounded nondelegating ephemeral Agent 2 author under Runtime SCOPE_CHANGE. Model: `gpt-5.6-sol`, medium reasoning. Role/nondelegation instruction-asserted.

Objective: prepare, but do not apply, the exact one-file metadata-only `RUNTIME_SCOPE_LEDGER.csv` repair required by the independent SCA-002 poststate audit. Resolve only the contradiction between the newly amended current account-control `DecisionRef`/`Notes` and the actual Gate 2–4 approval/application. Preserve the approved account-authority substance and every other canonical value.

Read repository/Runtime/SCOPE_CHANGE instructions; SCA-002 immutable snapshot and active pointer; current canonical ledger; final author-v2 candidate/review; Gate 2–4 grant; poststate audit snapshot `projects/chirality-runtime/execution/_Evaluation/DecompCoverage/COV_SCA002_ACCOUNT_AUTH_POSTSTATE_2026-09-07_2050/`, especially `RETURN.md`, issue log and report.

Write only under `scope/author-v3-ledger-repair/`. Produce:

- complete ledger `POSTIMAGE/RUNTIME_SCOPE_LEDGER.csv`;
- exact one-file `CANDIDATE.patch` against current canonical ledger;
- `PREIMAGE_INDEX.json`, `POSTIMAGE_INDEX.json`, `CHECKS.json`, `RETURN.md`, `MANIFEST.json`.

Required content:

- `DecisionRef` truthfully records published Root D36; Runtime Gate 2 impact, Gate 3 exact candidate and Gate 4 propagation approval; exact SCA-002 application; Gate 5 poststate audit blocker and pending repair/clean rerun/owner acceptance; publication/Root adoption/SOW propagation pending.
- `Notes` states the narrow account-control supplement is applied canonical but remains not effective for dependent reliance until Runtime publication/main identity and required Root successor adoption; project authorization and all full-wire/source gates remain; no activation. Explicitly define `CandidateState = GATE3_REVIEW_NOT_ACCEPTED` as the preserved historical migration/decomposition candidate-stratum field, not current SCA-002 Gate 3 status.
- Keep `CandidateState` byte-value unchanged to avoid redefining its schema in this metadata repair.
- Change only `DecisionRef` and `Notes`. Preserve one row, all other columns, seven carriers, four objectives, 66 inherited requirements, nine holds plus R16-B, historical SOW basis `9f21e4b86c304343b92ccd9ef10895b28c1a4f48`, `root-runtime-1` epoch 1 and all wire/source gates.
- Do not edit canonical, SCA-002, audit snapshots, SOWs, source, Root, pointers, Git or processes.

Verify CSV parsing, field-level diff, no overclaim, exact current preimage, patch applicability/whitespace and manifest hashes. Return `READY_FOR_INDEPENDENT_REVIEW` or blocker. The repair requires separate owner approval before application.
