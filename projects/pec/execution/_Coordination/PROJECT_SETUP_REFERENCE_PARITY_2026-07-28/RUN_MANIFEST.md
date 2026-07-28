# PROJECT_SETUP — PEC Reference and Live-Pointer Parity

Status: `APPLIED AND VALIDATED — GIT CLOSEOUT READY`
Date: 2026-07-28
Immutable basis: `main@4cd25b348196f7e6dfa925d8c7938184924cb383`
Owning role: `PROJECT_SETUP`

## Owner direction of record

> “Finish out your plan now (attaining your goal) with self merge of PRs and auto approve for owners rulings, which should still be recorded in the usual manner with your recommendation standing as what I approved.”

## Recommendation and disposition

PROJECT_SETUP recommends the smallest downstream parity tranche that closes
SCA-003's reference-packet obligation:

1. re-pin all 64 deliverable `_REFERENCES.md` packets from PRD v2.1 /
   decomposition revision 1.1 to accepted PRD v2.2 / revision 1.3;
2. align the five current PEC orientation/control pointers found stale by the
   execution-time scan;
3. append next-free PEC Receipt 116; and
4. retain this immutable evidence package and exact live-effect manifest.

Under the owner direction above, this recommendation stands as approved.
No new product meaning or production authority is created.

## Accepted basis

- PRD v2.2 SHA-256: `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba`.
- Decomposition revision 1.3 SHA-256: `3f65ea0e47036a2baa66cb60923f8b779525ae00d747425f93f8b69431151787`.
- Scope ledger SHA-256: `3cca281f7019a4544b6d4e6ab631a30125429525106f5d65b16aac270ebd50f5`.
- Deliverables register SHA-256: `b27ff4631f4966931990bbf9c033d2593d3dd8ac51b09e0d5112002b98afbc40`.
- SCA-003 snapshot:
  `projects/pec/execution/_ScopeChange/SCA-003_2026-07-28_0824/`.
- Execution-time scan: 64 reference packets; 64 stale v2.1 pins; 64 stale
  revision-1.1 pins; zero missing packets.

## Exact effect

`WRITE_SURFACES.csv` lists exactly 70 governed live effects: 69 replacements
(64 reference packets plus five current pointer surfaces) and one append to
the PEC receipt ledger. The evidence directory is additive run evidence;
`ARTIFACT_HASHES.sha256` hashes every evidence artifact except itself.

## Preservation fence

`PRESERVATION_HASHES.csv` freezes the protected preimages. ScopeOfWork
contracts, the active reliance hold, lifecycle state, decomposition topology
and registers, dependencies, implementation, estimates, and schedules are
outside the write manifest and must remain byte-identical or absent as
recorded.

`PEC-HOLD-001` remains `ACTIVE`. Its deterministic preflight allows
`exact-correction-preparation` and `candidate-validation`; this tranche
performs neither production reliance nor promotion.
