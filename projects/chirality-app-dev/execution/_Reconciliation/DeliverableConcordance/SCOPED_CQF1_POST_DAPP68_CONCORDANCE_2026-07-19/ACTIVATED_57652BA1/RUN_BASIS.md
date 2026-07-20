# Run Basis — Activated CQ-F1 Concordance

- Run: `APPDEV_LOOP_2026-07-19_CQF1_CONCORDANCE`, current attempt `R1-REPAIR2`
- Role: RECONCILIATION
- Shared source-state basis: `57652ba1cd0905e8f47131e4c4ebf518272f7c16`
- Activation: D-APP-69 Option A, merged on shared `main`
- Scope: 22 unique existing paths in five Remaining containers
- Ordered path-list SHA-256: `2e314f3f601350736032ace2730492c2afa6ab5b21fe26465d799470a195fc36`
- Derivative status: proposal-only evidence; not decomposition, ownership, lifecycle, repair, or release authority

## Fresh preflight

`PASS`. R1-RETRY established the activated discovery basis; R1-REPAIR freshly
re-established it before its child dispatch; and R1-REPAIR2 re-established
the exact basis, corpus, predecessor, verifier, and write boundary before
sealed-child reuse or package mutation:

1. `HEAD` and `origin/main` both resolved to the exact basis. The merge has
   parents `6152908b3246df61150dc91e3558788b05dfb643` and
   `1bbc3b692b2b33471fb109e3d075c31188b3fee9`; intervening PR #288 changed
   piping only and did not change app-dev from the accepted PR head.
2. D-APP-69 Option A, its one register row, this RunID, the frozen manifest,
   read-only boundary, and additive activated output pointer were committed.
3. `CQF1_SCOPE.csv` recomputed to 22 rows, 22 unique paths, zero missing paths,
   and the frozen ordered-list hash above.
4. The exact five live Remaining entries were present and all five containers
   remained `IN_PROGRESS`: DEL-02-01 (14), DEL-03-03 (1), DEL-06-02 (1),
   DEL-09-04 (4), and DEL-10-04 (2).
5. No D-APP superseding D-APP-69 was present. D-APP-56, D-APP-60, D-APP-64,
   D-APP-65, D-APP-68, and D-APP-69 were reopened as current authority.
6. Every scoped source, Remaining container, and relied-on authority surface
   was bound by Git blob and/or content SHA-256 before discovery. The ledger
   records both source bindings for each of the 22 paths.
7. Immutable R1-RETRY return, ledger, proposed mapping, and owner-slate hashes
   matched `5afcca64...`, `22894dd5...`, `5e3a08d0...`, and `e130c681...`.
8. Immutable V1-RETRY return/status/report/findings and both evaluation-child
   returns matched the exact amendment-v3 bindings. V1-001 through V1-004
   reproduced; V1-005 remained a nonblocking observation outside this repair.
9. R1-REPAIR return/status, sealed child brief/return, and current
   ledger/mapping/slate matched the seven exact amendment-v4 hashes.
10. V1-RECHECK return/status/protocol/report/findings/handoff and both child
    launch/return pairs matched all ten exact amendment-v4 hashes. V1R-001 and
    V1R-002 reproduced; V1R-003 remained the sustained v8 control erratum.

The local linked-worktree `main` ref was stale at `be4be0df...`; it was not
used as shared-main evidence. `origin/main` and the current task branch were
the shared accepted basis.

## Pinned method

- Shared method: `docs/DELIVERABLE_CONCORDANCE_METHOD.md`, Revision 1
- Git blob: `137209cb37e8d8204a7f2bd78114b4b5753c6c2e`
- File SHA-256: `abf3e78fce606c4557d61cdbfbdb7292a3d858838f6526da6b433d1bcd0ef627`
- D-APP-55 project-plan revision: `551f84ef6`
- R2 method addendum Git blob: `336c36...`
- Selection overlay: D-APP-60 fast reject plus D-APP-64 reasoned selection

## Authority bindings

| Surface | File SHA-256 | Git blob |
|---|---|---|
| Shared method | `abf3e78fce606c4557d61cdbfbdb7292a3d858838f6526da6b433d1bcd0ef627` | `137209cb37e8d8204a7f2bd78114b4b5753c6c2e` |
| Pinned project plan | `7b8c645d...` | `0f162d...` |
| R2 addendum | `cd154c...` | `336c36...` |
| Decision register | `698720...` | `3142ec...` |
| D-APP-56 | `512ee...` | `29cf...` |
| D-APP-60 | `729668...` | `26b...` |
| D-APP-64 | `c10922...` | `2dfa...` |
| D-APP-65 | `970a...` | `504aaa...` |
| D-APP-68 | `c2187...` | `e3b0...` |
| D-APP-69 | `db669...` | `24b4abff...` |
| CQ-F1 manifest | `8edb...` | `081e...` |

Abbreviated hashes are recorded only as corroborating package metadata; the
full source bindings used for row reproduction are in `CQF1_PATH_LEDGER.csv`
and the five accepted child returns.

## Delegation posture

R1-RETRY used five disjoint read-only slices. R1-REPAIR dispatched exactly one
fresh bounded DEL-02-01 evidence child for all 14 paths, as required by
amendment v3. Its exact source bindings, row order, schema, three focus
findings, and containment passed manager fan-in; its `RETURN.json` SHA-256 is
`b9bfb2923ec3853c4373923a61bca7e340963251e40fab94f3dbf5bdc56480c0`.
R1 remained sole package integration author.

R1-REPAIR2 validated the same sealed child's exact brief and return hashes,
14-row filtered-manifest order, schema, 14 live Git blobs, 14 source SHA-256
values, relied-on SOW/status/dependency/authority state, terminal completeness,
containment, and zero writes. Reuse was exact, so no replacement child was
dispatched. The complete reuse fan-in is recorded in
`DEL02_01_CHILD_PACKAGE_FIDELITY.csv`.

## Verifier-directed repair basis

- V1-001: expanded the `globals.css` boundary inventory to include DEL-02-02
  and DEL-02-05 plus every other materially evidenced boundary.
- V1-002: removed the false DEL-05-04 ChatMarkdown consumer; production
  consumers are exactly ChatPanel and DocumentView.
- V1-003: followed `ansi.ts`'s sole production importer, ChatMarkdown, to a
  DEL-02-01-primary / DEL-02-03-consumer proposal with shared utility retained
  as an alternative.
- V1-004: removed exactly one excess LF from each of the ten named Markdown
  files and required exactly one normal final LF.
- V1R-001: restored FilePicker's DEL-02-04 attachment UI-state and
  DEL-09-06/server enforceable-security boundaries; rejected DEL-06-04
  write/edit enforcement as a substitute.
- V1R-002: restored ownerless/shared and capability-split alternatives for
  `globals.css`, a shared-application-infrastructure alternative for the
  provider, and split-file plus ownerless/shared alternatives for event views.
- V1R-003: retained
  `NON_CONSEQUENTIAL_CONTROL_LABEL_ERRATUM_SUSTAINED`; current evidence uses
  only `projects/chirality-app-dev/frontend/src/app/globals.css` and
  `projects/chirality-app-dev/frontend/src/lib/shell/ansi.ts`.

All 22 source paths and five Remaining entries stayed byte-identical. The
other 18 row conclusions and groups 4–9 were carried forward under unchanged
source, authority, predecessor-child, and V1 evidence. Groups 1–3 were
reissued with unchanged populations `5+4+6`, and the complete 14-row fidelity
matrix reports 5 exact, 5 faithful-compression, and 4 repaired-material-loss
rows with zero unexplained omission, substitution, or semantic flattening.
