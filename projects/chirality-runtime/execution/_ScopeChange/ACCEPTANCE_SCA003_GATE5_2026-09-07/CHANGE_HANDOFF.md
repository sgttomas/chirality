# CHANGE handoff — accepted Runtime account-authority scope chain

Status: `READY_FOR_CONTROLLED_GIT_PUBLICATION` under the existing standing CHANGE grant.

Publish only the SCA-002→SCA-003 owning chain selection:

1. Canonical decomposition files:
   - `projects/chirality-runtime/execution/_Decomposition/ACCOUNT_CONTROL_AUTHORITY_DISPOSITION.md` — `19baaea22ba3a5b2dc465c30f7e8273db7b1833fd4a9bf6c2de0fc6056dcdd9d`
   - `projects/chirality-runtime/execution/_Decomposition/Chirality_Runtime_SOFTWARE_DECOMP_v1_0.md` — `413687ca6a857f5464a3205e9f9c4b29ace512c8d2b67dfa095ef3640fab883e`
   - `projects/chirality-runtime/execution/_Decomposition/RUNTIME_SCOPE_LEDGER.csv` — `bffda2701dea3667a63f72194404db72b20520802a7d840af13ac456fb1f149d`
2. Scope snapshots and current pointer:
   - complete `projects/chirality-runtime/execution/_ScopeChange/SCA-002_2026-09-07_ACCOUNT_AUTHORITY/`, sealed by manifest `8865716ba1fb55188658ae39ae9cef06ef17290b0801552621e93faee76aeda3`
   - complete `projects/chirality-runtime/execution/_ScopeChange/SCA-003_2026-09-07_1616/`, sealed by manifest `ce84376323a5d213c8a6dadcbf47534ecba407a9128543250f55e4b13eaaaa48`
   - complete `projects/chirality-runtime/execution/_ScopeChange/ACCEPTANCE_SCA003_GATE5_2026-09-07/` and `projects/chirality-runtime/execution/_ScopeChange/_LATEST.md`
3. Audit snapshots and current pointer:
   - complete `projects/chirality-runtime/execution/_Evaluation/DecompCoverage/COV_SCA002_ACCOUNT_AUTH_POSTSTATE_2026-09-07_2050/`, sealed by manifest `f2044a82fe16474865c6c1f99d66aa9c886851afedb1b72d22924f9ed7cc8369`
   - complete `projects/chirality-runtime/execution/_Evaluation/DecompCoverage/COV_SCA003_LEDGER_REPAIR_POSTSTATE_2026-09-07_2227/`, sealed by manifest `93e17c03c0091b16abbf9b8a8d31c06dcce33f7048b2e1f6f215bd097bf79012`
   - `projects/chirality-runtime/execution/_Evaluation/DecompCoverage/_LATEST.md` — `74f4ccdeff8a96f0b5ab0220915c5b268eec92d8ae9070609b0a544661c1310e`
4. Complete SCOPE_CHANGE evidence only at `projects/chirality-runtime/execution/_Coordination/AgentRuns/APP_V3_CONSOLIDATED_RESUME_2026-09-07/scope/`, including original and repair candidates/reviews, owner grants, audits, temporal recheck, and Gate 5 decision evidence.

The exact `scope/` evidence selection contains 103 files and 409979 bytes. Its tree digest is SHA256 `101b5fa5d9bb57dedbd3c130d9142a2fa3e3e8b7136721c33e60dc8e9f988850`, computed over newline-terminated sorted records `<file_sha256> <bytes> <path_relative_to_scope>`.

Explicit exclusions: do not stage `.custody-npm-cache`; sibling `pkg02` supplier/full-wire outputs; SCA-001 custody/SOW evidence; other Runtime AgentRuns; COV_D36 snapshots; source, test, lifecycle, status, dependency, hold, credential, process, protected-fixture, hosted-readiness, Root-adoption, or release changes. CHANGE must fail closed on any unexpected path, hash drift, merge conflict, or non-fast-forward publication condition.

Suggested commit message: `docs(runtime): accept narrow account authority scope change`
