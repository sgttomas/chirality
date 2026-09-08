# Sealed brief — exact Runtime SOW successor adoption

Role: nondelegating ephemeral Agent 2 author. Role and nondelegation are instruction-asserted. Model allocation: `gpt-5.6-sol`, medium.

## Purpose and authority

Prepare and apply the minimal Root recognition update for the owner-accepted Runtime DEL-02-06/09 SOW poststates under existing D-GOV-37. No new semantic owner vote is required. Candidate CI must recognize exact branch-local accepted bytes as `accepted-pending-publication`; CHANGE will later publish and perform the fetched-main backcheck.

## Sealed basis

- Repository: `/private/tmp/chirality-runtime-app-sow-publication-20260907`.
- HEAD/main basis: `c5192790f98ec024e7c2728cb1d4df3ae2b2a2dd`.
- Pre-existing staged accepted-SOW selection: exactly 68 paths; index tree `2db8f61803c49ae0f555604a23298a84d9cfcdfe`; staged binary diff SHA-256 `cd45e7354c0248e150deea070aa1a93a8736d81175080a80881a987e0d186f6e`. These 68 paths are read-only for this task and must remain staged and byte-exact.
- Current `.gitattributes` includes PR #752 and must remain byte-exact; do not edit it.
- Owning handoff manifest: `projects/chirality-runtime/execution/_Coordination/AgentRuns/APP_V3_CONSOLIDATED_RESUME_2026-09-07/scope/sow-publication-handoff-manager-v1/MANIFEST.json`, SHA-256 `0e053db4cee2419c7c535a5c702cdff79313829bffc2e48d32208b60b3b1ea17`, 5/5.
- Root input: sibling `ROOT_RUNTIME_INPUT.json`, SHA-256 `59a14a2354abfe785e1e0d8832adcbe73673e2a871371a3a779678b6e5efdb9c`.
- Runtime acceptance manifest: `projects/chirality-runtime/execution/_ScopeChange/ACCEPTANCE_SOW_PROPAGATION_SCA002_SCA003_2026-09-07/OUTPUT_MANIFEST.json`, SHA-256 `e90c7850b6ef22a18db9929b2d8e1c80c22ec04fcd174fac15493469f5de602e`, 9/9.
- Owner acceptance SHA-256: `0329293b691862f9bd1d3ca2977278e3706b278aa3ac4d177f24a289fa016367`.
- Runtime acceptance postimage index SHA-256: `ffac42013c68c2ce2f36469b7e37808fffab0d0f18fa723d9a1d7439a3d3e470`.
- Accepted Runtime subject SHA-256: `37141786ee3806d41402996f9cb7e022bbb071d94efadc46f151f310d2c864a5`; audit snapshot manifest SHA-256 `432aa2e1238d93c4b28e923ba19e12e3bfbaf52152845f8195eb18a9e27665b1`.
- DEL-02-06 predecessor/postimage: `e87e567f7be38e6a98a2c15ee44dd7f5c2e7ebdf72628155ea18a62e539aaa54` → `2e66ee8681800307f5675db63c9870413bb6148bc5cace8e3423ac89b4eeaefe`.
- DEL-02-09 predecessor/postimage: `5e46d0a1538618d69b4e9ae6368b5a71dc96aeb4bc4d2d9c46a6d0b23cbcc46e` → `0d154c0067da5a9152c46497bead5cd16cfe3fc524a0bc0648c103b32822fd3e`.

## Authorized writes

- `docs/governance_harness/_DECISIONS/D-GOV-40_runtime_sow_successor_adoption.md`
- `docs/governance_harness/_DECISIONS/_REGISTER.md`
- `docs/governance_harness/tranche_manifests/ROOT-RUNTIME-SOW-SUCCESSOR-ADOPTION-20260907.yaml`
- `execution/_Coordination/LOOP_RECEIPTS.md`
- `execution/_Coordination/AgentRuns/ROOT_RUNTIME_SOW_SUCCESSOR_ADOPTION_2026-09-07/**`
- `tools/validation/root_runtime_successors.py`
- `tools/validation/test_root_runtime_successors.py`
- `projects/chirality-app-dev/execution/_Coordination/NOTICE_ROOT_RUNTIME_SOW_SUCCESSOR_ADOPTION_2026-09-07.md`
- `projects/chirality-runtime/execution/_Coordination/NOTICE_ROOT_RUNTIME_SOW_SUCCESSOR_ADOPTION_2026-09-07.md`

Do not stage, commit, push, merge, edit `.gitattributes`, edit any of the 68 accepted-SOW paths, or write Runtime/App canonical, source, SOW, supplier, account, fixture, lifecycle, release, or product files.

## Required implementation

Preserve the three existing adoption objects byte-for-byte and in order. Append one exact Runtime-only adoption for the two SOW paths above. App DEL-02-05 is explicitly excluded from the Root policy.

Point the helper at a new immutable policy path/hash. The current acceptance binds a Markdown decision subject and a separate acceptance manifest/postimage index, so implement only the narrow format-aware verifier required to prove the exact frozen acceptance package, subject, audit/application bindings, index projection, current pointer, and two live postimages. Preserve hard-canonical path, symlink, duplicate/member, predecessor, publication, and execution-authority rules. Do not add an arbitrary latest-file path, broad schema fallback, bypass, or generic helper rewrite.

Create D-GOV-40, register, receipt, M2/G4 manifest, run evidence, and both routed notices. State existing D-GOV-37 authority truthfully. Do not quote or invent a new owner vote. Recognition remains `execution_authority=false`.

## Acceptance checks

- Exact 68-path staged preselection remains byte-identical and untouched.
- Prior three adoption objects/order remain exact; only one Runtime pair adoption is appended.
- Positive branch-local composition reports `accepted-pending-publication`, `published=false`, `execution_authority=false`.
- Meaningful negatives cover altered/missing acceptance, subject, manifest/index/member, wrong predecessor/postimage, App-path or unknown-path injection, mixed Runtime SOW revisions, and symlink/type/path violations proportionate to the new schema.
- Existing migration-baseline and all prior successor tests pass.
- Root G0–G4/self-check, affected validation, candidate whitespace, and `git diff --check` pass on the precise combined candidate scope; preserve any broader unrelated diagnostics separately.
- Freeze a complete candidate diff and exhaustive hash/byte manifest, self-excluding only where necessary, for separate independent review.
