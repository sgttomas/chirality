# D-APP-75 — Effective-State Closeout

Status: `EFFECTIVE_STATE_CLOSEOUT`
DecisionID: `D-APP-75`
Date: 2026-07-27
Owning loop: Chirality App Dev
Candidate basis: `main@fb16e32ed60bb4f384cf1e07a83c4a14ff63bbae`
Original ruling SHA-256: `b3d335c0f352778c5f3623e4cb4d14ee759a38bcf2f3e14dad9ad67ba4dd8b40`
ApplicationCommit: `4cdf469cf3aa3f76681e52aeeb7e833c52e1faee`
EffectiveCommit: `18e5dda568689daadaa05aff65bd4b810489409b`
EffectivePR: `#363`
RecordConvention: additive closeout; original ruling remains byte-identical

## Purpose

Record the already completed Git integration of the D-APP-75 APP-HOLD-1
application. This file creates no new authority. It supersedes only stale
current-state statements in the original ruling and App decision-register row
that say Git closeout or PR merge remains pending.

## Deterministic identity

Git establishes:

1. `4cdf469cf3aa3f76681e52aeeb7e833c52e1faee` is the APP-HOLD-1 application
   commit;
2. `18e5dda568689daadaa05aff65bd4b810489409b` is the two-parent merge of PR
   #363 and contains that application commit;
3. both are ancestors of the candidate basis;
4. the application and merge tree IDs are identical:
   `8f27be8597e105d0d1d77f8fbf3dbb7c46f0a78f`; and
5. the enumerated APP-HOLD-1 live, proposal, catalog, and instruction
   surfaces are unchanged from the merge through the candidate basis.

The corrected live-test file remains SHA-256
`2d8d846b9aa9db7b47023a8f6af76649530e0a3c308fad7367c065a8f0bdcd2b`.
The frozen candidate package and original D-APP-75 ruling remain unchanged.

## Effect

D-APP-75 is integrated and effective at PR #363 merge
`18e5dda568689daadaa05aff65bd4b810489409b`.

APP-HOLD-1 remains scan-authoritative, entry-path independent, fail-closed,
and no-repin. Its separately ruled override mechanism remains unchanged.

## Scope limits

This closeout does not:

- amend the original D-APP-75 ruling or frozen candidate bytes;
- repin any `ScopeOfWork.md` or other contract;
- add, remove, or release a held target;
- create a runtime exception mechanism;
- approve any App or Root SCOPE_CHANGE gate;
- change product architecture, lifecycle, release, or professional reliance;
  or
- dispose D-APP-48/49 or any other OD gate.

Git identity and passing checks are evidence of integration, not a new human
decision.
