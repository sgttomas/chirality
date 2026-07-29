# GRANT-2026-07-29 — Bounded merge-execution grant for the remaining loop-readiness transition PRs (CANDIDATE)

Status: DRAFT — CANDIDATE ONLY. This file has no effect until the owner
issues it by token. It grants nothing by existing, by being committed, or by
being merged (K-AUTH-1). The owner token grammar lives in
`docs/PRD_ROOT.md` annex §5.3.1; transcription records never define or
extend it.

GrantID: GRANT-2026-07-29
PolicyBasis: `docs/PRD_ROOT.md` Rev 7 annex §5.3.1 (adopted by D-GOV-31,
effective merge `ea3db3607fbcbb7ce5f65bab31268a7eca431adb`)
Drafted: 2026-07-29, bounded Agent 2 AUTHOR run GOV-STEP4-OPERATIVE-20260729
(HELPS_HUMANS lane under HELP_HUMAN)

## Grant definition (per annex §5.3.1, all fields mandatory)

- **Authoring actor:** bounded Agent 2 runs dispatched under the
  loop-readiness transition program's Agent 1 lanes (HELP_HUMAN Agent 0
  session of record supervising).
- **Merge executor:** the supervising agent session, executing via the
  owner-authenticated `gh` CLI (GitHub merge actor `sgttomas`).
- **Scope:** transition-program pull requests from `gov/step4-*` and
  `gov/step5-*` branches into `main` of the Chirality monorepo — no other
  branches, repositories, or paths.
- **Duration / expiry:** from owner issuance through 2026-08-12 (inclusive);
  void thereafter.
- **Recording:** this grant is recorded strictly BEFORE any exercise; it is
  never recorded or reconstructed after the fact.

## Exclusions

Expressly prohibited under this grant, verbatim from annex §5.3.1:

- agent-authored semantic auto-approval;
- content mutation after approval;
- force push, rebase, or invented conflict resolution;
- any authority beyond the named scope and expiry;
- lifecycle or issuance authority inferred merely from merge permission.

Additional exclusions specific to this grant:

- no merge without a per-PR owner approval of the exact final branch HEAD
  (the approved source SHA pinned in a durable record — the tranche
  manifest's `m2_gate.merge_execution_grant.approved_source_sha` field —
  before the merge executes);
- grant recorded strictly before exercise; any merge preceding the issued
  record of this grant is outside it.

## Execution authority is not semantic approval

Per annex §5.3.1: this grant, if issued, authorizes merge execution within
its recorded scope and term only. It never constitutes semantic approval of
future unknown content. Each merge still requires a human approval vehicle
bound to the exact source HEAD, verification that HEAD remains unchanged, and
a separately recorded effective merge identity. The four closeout identities
(semantic approval, approved source SHA, merge authorization, effective merge
SHA) remain distinct and observable for every merge.

## Issuance

This candidate becomes a live grant only when the owner returns the issuance
token naming this exact file by SHA8 of its SHA-256:

```text
ISSUE GRANT-2026-07-29 <sha8-of-this-file> — Ryan Tufts <date>
```

The binding SHA-256 of this file is computed and presented by the supervising
session at issuance; the token is lawful only against that exact byte
identity. If this file changes, any previously presented SHA8 is void and a
new one must be presented. A declined or unreturned token leaves this file a
frozen unissued candidate, superseding nothing.
