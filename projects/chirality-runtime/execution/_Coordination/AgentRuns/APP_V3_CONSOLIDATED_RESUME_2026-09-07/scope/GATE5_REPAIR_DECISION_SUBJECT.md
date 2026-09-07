# SCA-002 Gate 5 ledger-repair decision subject

Status: `PASS_DECISION_READY_METADATA_REPAIR`; owner approval required before application.

## Why a separate decision is required

The owner-approved SCA-002 patch was applied exactly. Independent actual-poststate AUDIT_DECOMP verified its bytes, snapshot, pointer and all conserved invariants, but blocked Gate 5 closure because the authoritative ledger's newly amended `DecisionRef` and `Notes` still said Runtime approval/application were pending. The audit return is `projects/chirality-runtime/execution/_Evaluation/DecompCoverage/COV_SCA002_ACCOUNT_AUTH_POSTSTATE_2026-09-07_2050/RETURN.md`, SHA256 `912d287934e65e3d224194803f5f54f872a35868e673d47c220186a5282979f1`; output manifest SHA256 `f2044a82fe16474865c6c1f99d66aa9c886851afedb1b72d22924f9ed7cc8369`.

This correction is a new exact authoritative-ledger postimage, so `agents/AGENT_SCOPE_CHANGE.md` requires human confirmation of the corrective impact (Gate 2, lines 268/343), formal approval of the exact amendment (Gate 3, lines 347/403), and approval of its limited propagation/application plan (Gate 4, lines 407/485). The earlier narrow semantic-boundary vote and SCA-002 patch approval cannot be stretched to silently rewrite different bytes.

## Exact reviewed correction

- Canonical preimage: `RUNTIME_SCOPE_LEDGER.csv`, SHA256 `e3621b3cef4f58644c26d830e5f991e699e955413e15842b4f615dcb67a61920`.
- Exact one-file patch: `author-v4-ledger-repair/CANDIDATE.patch`, SHA256 `64c2748759644761e1924c59cb6dcc6eb70d0046e5d5daae2f0627a3038a43be`.
- Exact postimage: `author-v4-ledger-repair/POSTIMAGE/RUNTIME_SCOPE_LEDGER.csv`, SHA256 `e07accd8ad81429a83bd53673de97af38c721dd03799a5bc6af89d12f9d29854`.
- Author manifest: SHA256 `7645678894c9d5f704d29d4207e60a4654275c2e702ab2dab7a12e630e397109`.
- Independent final review: `review-v4-ledger-repair/RETURN.md`, SHA256 `ba00128c7fe7008d83ea54534192746d47d3f30fccd8a7b63e93c994d3f8085a`, verdict `PASS_DECISION_READY_METADATA_REPAIR`.
- Review manifest: SHA256 `65257a958fc70bf62a468c36f9ab1165f0f13e57b61e8bd2460601ed24ebda6b`.

Only `DecisionRef` and `Notes` change. Every other ledger field, including `CandidateState`, remains byte-identical. The postimage records SCA-001 custody Stage 1 and SOW Stage 2 accurately, separates their remaining publication/adoption from future SCA-002 account-authority SOW propagation, records SCA-002 actual approval/application and audit blocker, and retains pending clean audit/Gate 5/publication/adoption work. `CandidateState = GATE3_REVIEW_NOT_ACCEPTED` is explicitly defined as historical migration/decomposition candidate-stratum metadata rather than current SCA-002 status.

## Precise requested approval

> I approve exact Runtime ledger repair patch SHA256 `64c2748759644761e1924c59cb6dcc6eb70d0046e5d5daae2f0627a3038a43be`, producing `RUNTIME_SCOPE_LEDGER.csv` SHA256 `e07accd8ad81429a83bd53673de97af38c721dd03799a5bc6af89d12f9d29854`. Apply only this one-file metadata correction, create its new immutable repair snapshot, update the Runtime scope-change pointer as the protocol permits, and rerun the independent poststate audit. This is exact-text metadata repair, not a repeat vote on the narrow semantic boundary and not approval of Git publication, Root adoption, future DEL-02-06/09 SOW bytes, source, supplier, lifecycle, protected fixtures or release.

After application and a clean independent audit rerun, the owner must separately accept the corrected Gate 5 poststate. Until then SCA-002 closure and CHANGE publication remain held.

